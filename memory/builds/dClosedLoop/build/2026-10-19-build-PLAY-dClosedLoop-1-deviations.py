# **Serves:** research PLAY-dClosedLoop-1
"""The deviation population, its join, and the departures report: every departure from the frozen design, or from a
spec once its code has started, joined to a deviation record (the owner's FQ-3, final-questions `[deviation]`,
dTrueNorth's clauses `cl-dClosedLoop-0004` and `cl-dClosedLoop-0005`; the execution plan's P0.1 and P0.2). This is the
bootstrap half, computed from history here until dTrueNorth joins it at the commit and at the close.

Placement (P0.1 row 9): the instruments run on the prepared merge, after `push-main.sh --prepare`, so two specs written
on two branches are read together on the merged tree. README rule 4's close sequence runs `--report` there.

A deviation record lives in the departing build's `build/` folder as `<date>-build-<unit>-deviation-<n>.md`, with:
  - **Departs from:** cl-dClosedLoop-NNNN@<hash8>, or <unit>@rev-N [<section tag>]
  - **Hand-off:** design-to-spec, design-revised, spec-revised, spec-to-code or code-to-record
  - **Before:** and **After:** the text departed from, and the text that replaced it
  - **Cause:** design defect, owner ruling, builder discovery, review finding or external
  - **Reason:** and **Evidence:**
  - **Risk:** editorial, additive, stricter, loosening or breaking
  - **Approver:** author, spec writer or owner, and where the approval is recorded
  - **Follow-through:** amends <clause-id>@<hash8>, supersedes <clause-id>@<hash8> by <clause-id>, new unit <id>,
    gap <id>, ask <id> or usage <key>
  - for a fork's choice: **Bound:** and **Tier:** for a relaxed bound, **Surface:** for a widened one
Approval under the chain's value `author-recorded` (ER:103-104, :189; P0.1 row 6): an approver passes when its
**Approver:** opens with a role the grammar names, whatever the risk. One naming the owner must cite a decision id whose
row `memory/DECISIONS.md` holds at the advertised default-branch tip (`origin/main`; under --report, P), and that row
must name the record's Departs-from clause id or the unit its `new unit` follow-through names. This file holds no
decision id: it reads the row the record cites.

The population, computed and never declared; each member has an address, the hand-off it is, and the record joining it:
  - v2's `Baseline:` differing from the pin BASELINE, listed first; only the owner's re-pin moves the pin, so no record
    joins it (design-revised);
  - each clause of v2's `[chain]` whose hash moved since the pin, or added or removed there, addressed
    `<clause>@<its hash at the pin>` (design-revised);
  - each revision of a chain build's spec that is not an ancestor of its unit's first pass, addressed `<unit>@rev-N`, N
    the header revision it changed (spec-revised). The first pass is the oldest commit reachable from HEAD that carries
    a `Pass:` trailer naming the unit, read as lib-unattended.sh's read_attribution_tokens reads it, so `Pass: none`
    names none; or carries no `Pass:` trailer, names the unit as a whole token in its subject, and writes a path outside
    every memory/builds/ folder, memory/LIVE.md, memory/ledger/, memory/DECISIONS.md and
    memory/project/readme-contract.txt;
  - each revision of a spec that is not an ancestor of the commit adding the newest `spec-audit` record whose
    **Serves:** pins `<unit>@rev-N`, addressed `<unit>@rev-N` (spec-revised). A unit with no pin adds nothing, and the
    summary names it under "no audit pin". Both revision arms except a revision whose text is unchanged once its
    **Status:** line and every gen region are removed, the regions stripped by lib-unattended.sh's GEN_REGION_AWK, read
    from that file;
  - each `amended rev-N` line under an **Evidences:** <unit> block of a `journal` record in a chain build's folder,
    addressed `<unit>@rev-<N-1>`, the revision it departed from (spec-revised);
  - each rescope row of a chain build's RUN.md and rotated RUN.*.md: an `add` joins the record whose **Follow-through:**
    is `new unit <item>` (design-to-spec); a `retire` or `supersede` is addressed `<item>@rev-N`, N the item's header
    revision at the row's commit (spec-revised); a `defer` row is no member;
  - each revision record under a chain build's prompts/ whose ### Goal opens DIVERGENCE: (the /build Skill's stage 5),
    addressed `<unit>@rev-N`, the unit its **Serves:** names and N its spec's header revision at the commit that added
    the record (spec-to-code).
A member joins the record departing from its address, so a hand-back and a revision of one change join one record.

The departures report (P0.2), `--report <slug>`, on the prepared merge. Its range is P..HEAD, P the prepared merge's
first parent: paths from `git diff --name-only P..HEAD`, `Decided:` trailers from `git log P..HEAD`. Its run kind is
derived from the live RUN.md's `base:` by README rule 1's test: an open ask in the build's BACKLOG.md there and a
`roster:units` unit with no spec there make a spec run (`-departures-spec.md`); anything else is a build run
(`-departures-build.md`). Its head names each instrument's blob at HEAD. It lists, in order: each choice whose
`Decided:` trailer or §8 mark carries a non-`none` `widens:`, `relaxes:` or `grants:`, a `widens:` value joining the
record whose **Surface:** is that value and a `relaxes:` value the record whose **Bound:** is; each member; each other
fork (a `Decided:` trailer, a §8 RESOLVED mark, a park row); each unit carried forward with its ask, and each unit the
run added; and each path the range writes outside the build's folder and, for a build run, the `--dispatch --writes`
paths RUN.md records, less memory/LIVE.md, the ledgers, a file whose change is inside gen regions only, and a
BACKLOG.md that gains only ask and SEV rows. Then the build README's `build-coverage` region, cl-dClosedLoop-0003's
coverage, and the output of the product as-built view's `asbuilt_view.py --check`, cl-dClosedLoop-0006, which took
the place of `carries.py --report <slug>` and `asbuilt.py --check` at the report-switch step after dTrueNorth's
landing (the execution plan's [phase-1] retirement table, rows 1 and 2).
Two checks, under --write and --check: the byte compare, and the validating arm, which parses the rendered report.
The arm also holds the report-switch step (PLAY-dClosedLoop-29): a build run of a slug in the retirement table's
"Lands with" column, read from the plan, is red until dClosedLoop's BACKLOG.md at HEAD holds an ask naming
`report-switch`, minted under that slug (P0.6 rule 3) or filed late under dClosedLoop's naming it; the head says which.

Usage (from the worktree root):
  python deviations.py [--policy report|refuse]
      the population on the tree, joined to the records; report lists every member and exits 0, refuse exits 1 on an
      unjoined member or an approver author-recorded refuses
  python deviations.py --fixture [--plant <case>] [--policy report|refuse]
      the same over a temporary git repository whose .memory-tree.conf declares the fixture family FIX (finding 10),
      every population plant in it, or the base and one plant: baseline, clause, subject-pass, pass-none, status-flip,
      two-branch, header-rev, gen, status-gen, gen-text, quote, amended, amended-joined, approver-none, owner-bare,
      owner-er, owner-row5, owner-row1-added, owner-unknown-id, approver, add, handback, audit-pin, defer, fix-record,
      audit-nopin
  python deviations.py --report <slug> [--write|--check]
      print the build's departures report, or write it beside the build's records, or compare it with the written one
  python deviations.py --report <slug> --fixture [--plant <case>] [--control no-arm|base-range]
      the report over the fixture repository, written, committed and checked there: every population plant, or the
      base and one plant, a population plant or kind-spec, kind-build, kind-whole, kind-norun, stub-widens,
      stub-relaxes, stub-grants, stub-drop, omit-grant, record-no-tier, record-no-reason, record-no-surface,
      trailer-relaxes-only, trailer-widens-only, trailer-388-none, trailer-240-none, trailer-rung6, outside-packet,
      outside-product, range, record-late, hand-edit, instrument-byte, switch-missing, switch-foreign, switch-spec,
      switch-late; no-arm drops the validating arm, and base-range reads the range from the run's base
Exit 0 green, 1 on a refusal under refuse or a red check of the report, 2 when nothing is measured: neither the pin's
v2 nor a chain build's spec, or for a report no live RUN.md, no base:, no prepared merge or no roster unit.

What it does not read: whether a record's reason is true or its risk class honest, which the approver and the closing
review judge; a departure in code that changes no spec, which Test's verdict and the closing review catch; a hand edit
inside a gen region, which the strip cannot tell from a render; a hand-back whose record lands in the commit that also
revises the spec, which reads the revised header; whether the README's coverage region is current, which
`gen_build_index.py --check` grades in the bar; a close that never runs `--report`, an owner landing by hand
included (ER:248), which leaves no departures report for the owner to read; whether the report-switch ask says more
than its minter and the word, and whether dClosedLoop's session then makes the switch, which every packet's field 9
and dClosedLoop's own asks-disposed carry; and in a fixture, the tree's own `asbuilt_view.py --check`, which
the report runs in the worktree since the fixture holds none of its inputs.
"""
import argparse
import datetime
import functools
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

B = "memory/builds/dClosedLoop/build/"
V2 = B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
SELF = B + "2026-10-19-build-PLAY-dClosedLoop-1-deviations.py"
# The design baseline, pinned here (P0.1 row 5). Only the owner's re-pin moves it; v2's `Baseline:` line is checked
# against it and never read in its place. asbuilt.py renders from this pin.
BASELINE = "59ff8f2ac04a967751eae00de6856afbea66c033"
INSTRUMENTS = (B + "2026-10-19-build-PLAY-dClosedLoop-1-carries.py", SELF,
               B + "2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py", B + "2026-10-20-build-PLAY-dClosedLoop-1-packet.py")
# The product as-built view, cl-dClosedLoop-0006, which the report runs in asbuilt.py's place since the report-switch
# step at dTrueNorth's landing (the execution plan's [phase-1] retirement table, row 1).
VIEW = "tools/memory-tree/asbuilt_view.py"
# The report-switch step (the execution plan's [phase-1]): a build run landing a row of the retirement table owes an
# ask in dClosedLoop's BACKLOG.md (P0.6 rule 3). The landing set is that table's "Lands with" column, read from PLAN.
PLAN = B + "2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md"
RETIREMENT_HEAD = "| Instrument, or arm | Retired by | Lands with |"
SWITCH_BACKLOG = "memory/builds/dClosedLoop/BACKLOG.md"
SWITCH = "report-switch"
LIB ="tools/unattended/lib-unattended.sh"
ROLES = ("spec writer", "author", "owner")          # the record grammar's approver roles, the longest first
RULINGS = ("ER:240", "ER:388", "ER:328", "P0.8 row 5")
RECORD_SURFACE = ("memory/builds/", "memory/LIVE.md", "memory/ledger/", "memory/DECISIONS.md",
                  "memory/project/readme-contract.txt")
SHARED_RENDERS = ("memory/LIVE.md", "memory/ledger/")
POLICIES = ("report", "refuse")
FIELD = re.compile(r"^- \*\*([A-Z][a-z-]+(?: [a-z]+)?):\*\* (.+)$", re.M)
RESCOPE = re.compile(r"^\S+ rescope · item (add|retire|supersede|defer) (\S+)(?: -> (\S+))? · reason (.*)$", re.M)
DISPATCH = re.compile(r"^\S+ dispatch · item \S+ (\S+) · reason (.*)$", re.M)
PARK = re.compile(r"^\S+ decision · item (.*?) · reason (.*)$", re.M)
LEDGER = re.compile(r"^- (\S+) — amended rev-(\d+)\b")
KEY = re.compile(r"\b(widens|relaxes|grants): (.+?)(?=\s+(?:widens|relaxes|grants):|\s+·\s|;\s|$)")
ENTRY = re.compile(r"^- entry (\d+) · (\w+) · (.*)$", re.M)
CHOICE_KEY = re.compile(r"(widens|relaxes|grants) \[([^\]]*)\](?: joins (\S+))?")
RUN_FILE = re.compile(r"^RUN(?:\.[^/]+)?\.md$")
DIVERGENCE = re.compile(r"^### Goal[ \t]*\n(?:[ \t]*\n)*DIVERGENCE:", re.M)

spec = importlib.util.spec_from_file_location("carries", B + "2026-10-19-build-PLAY-dClosedLoop-1-carries.py")
carries = importlib.util.module_from_spec(spec)
spec.loader.exec_module(carries)
spec = importlib.util.spec_from_file_location("bareids", B + "2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py")
bareids = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bareids)
gbi = bareids.gbi        # the build-index generator: its header, H1, Serves and roster grammars
import row_grammar  # noqa: E402  the memory-tree kit's row regex, on the path bare-ids.py puts the kit on


class Unmeasured(Exception):
    """Nothing measured: exit 2."""


def run_git(root, *args, env=None):
    """git's stdout in `root`, or None when git exits non-zero."""
    done = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=env)
    return done.stdout if done.returncode == 0 else None


def check_ancestor(root, a, b):
    return subprocess.run(["git", "-C", root, "merge-base", "--is-ancestor", a, b], capture_output=True).returncode == 0


def read_chain_clauses(v2_text):
    """[(build, clause id, text, hash8)] of v2's `[chain]`, in row and clause order."""
    chain = v2_text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    out = []
    for ln in chain.split("\n"):
        m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
        if m:
            for c in carries.split_clauses(m.group(2)):
                i = carries.CID.search(c)
                if i:
                    out.append((m.group(1), i.group(1), carries.CID.sub("", c).strip(), carries.clause_hash(c)))
    return out


def read_chain_builds(v2_text):
    chain = v2_text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    return re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)


def read_baseline_line(v2_text):
    """The sha v2's `[clause-ids]` records as `Baseline:`, or None."""
    cid = v2_text.split("\n## [clause-ids]", 1)[1].split("\n## ", 1)[0] if "\n## [clause-ids]" in v2_text else ""
    m = re.search(r"^Baseline: `([0-9a-f]{7,40})`", cid, flags=re.M)
    return m.group(1) if m else None


def check_baseline(v2_text, pin):
    """The member's text when v2's `Baseline:` differs from the pin, else None (P0.1 row 5, finding 7)."""
    line = read_baseline_line(v2_text)
    if line and pin.startswith(line):
        return None
    return f"v2's Baseline moved from {pin[:9]} to {line[:9] if line else 'none'}"


def read_conf_grammar(root):
    """The root's conf, its family prefixes, and an id pattern taking an optional `@rev-N`."""
    conf = gbi.load_conf(root)
    families = [p.split(":", 1)[1] for p in conf["FAMILIES"].split() if ":" in p]
    alt = "|".join(sorted(families)) or "(?!)"
    return conf, families, re.compile(r"((?:" + alt + r")-[A-Za-z0-9]+-\d+)(?:@rev-(\d+))?")


def read_serves(text, fam_re):
    """(kind, [(id, rev or None)]) of a record's first **Serves:** line, as the generator's BIND_RE finds it."""
    for line in list(gbi.unfenced(text))[:gbi.BIND_HEAD_LINES]:
        m = gbi.BIND_RE.match(line)
        if m and m.group("key") == "Serves":
            toks = m.group("rest").split("<!--", 1)[0].split()
            ids = [(x.group(1), int(x.group(2)) if x.group(2) else None)
                   for t in toks[1:] for x in [fam_re.fullmatch(t.strip("`"))] if x]
            return (toks[0] if toks else None), ids
    return None, []


def read_header_rev(text):
    """The `rev-N` of a spec's **Status:** header, as the generator's HDR_RE reads it, or None."""
    for ln in (text or "").split("\n"):
        m = gbi.HDR_RE.match(ln)
        if m:
            return int(m.group("rev"))
    return None


@functools.lru_cache(maxsize=None)
def read_gen_strip():
    """lib-unattended.sh's GEN_REGION_AWK program and the awk that runs it, read from that file and never copied, so
    check 23 and this instrument strip one way (P0.1 row 8a)."""
    found = re.findall(r"^GEN_REGION_AWK='([^']*)'$", Path(LIB).read_text(encoding="utf-8"), flags=re.M)
    awk = shutil.which("awk")
    if len(found) != 1 or not awk:
        raise Unmeasured(f"the gen-region strip needs {LIB}'s one GEN_REGION_AWK and an awk to run it; found "
                         f"{len(found)} and {awk or 'no awk'}")
    return awk, found[0]


def extract_outside_gen(text):
    awk, prog = read_gen_strip()
    return subprocess.run([awk, prog], input=text.encode("utf-8"), capture_output=True, check=True).stdout


def extract_authored(text):
    """A spec's text less its **Status:** line and every gen region (P0.1 row 8a)."""
    return extract_outside_gen(re.sub(r"(?m)^\*\*Status:\*\*.*$", "", text))


def check_material(before, after):
    """True when a revision changes text outside its **Status:** line and every gen region."""
    return extract_authored(before) != extract_authored(after)


def read_specs(root, builds, conf, families):
    """[(build, path, unit)] of each spec in a chain build's spec folder, the unit its H1 defines, or None."""
    out = []
    for b in builds:
        for p in sorted(Path(root, conf["MEMORY_ROOT"], "builds", b, "spec").rglob("*.md")):
            rel = os.path.relpath(p, root).replace("\\", "/")
            hit = gbi.parse_spec_h1(rel, p.read_text(encoding="utf-8"), conf["MEMORY_ROOT"], families)
            out.append((b, rel, hit[1] if hit else None))
    return out


def read_commit_log(root):
    """[(sha, subject, its Pass trailer's value)] of every commit reachable from HEAD, oldest first."""
    out = run_git(root, "log", "--date-order", "--reverse",
                  "--format=%H%x1f%s%x1f%(trailers:key=Pass,valueonly,separator=%x20)%x1e", "HEAD") or ""
    rows = []
    for rec in out.split("\x1e"):
        rec = rec.strip("\n")
        if rec:
            h, s, t = (rec.split("\x1f") + ["", ""])[:3]
            rows.append((h, s, t.strip()))
    return rows


def check_product_commit(root, sha):
    """True when the commit itself writes a path outside the record surface (a merge writes none)."""
    out = run_git(root, "diff-tree", "--root", "--no-commit-id", "--name-only", "-r", "-z", sha) or ""
    return any(p and not p.startswith(RECORD_SURFACE) for p in out.split("\0"))


def read_first_pass(root, unit, log):
    """The unit's first pass (P0.1 row 3): a `Pass:` trailer naming it, or no trailer, the unit a whole token of the
    subject, and a product path written."""
    for sha, subject, trailer in log:
        if trailer:
            names = re.sub(r"[^A-Za-z0-9-]", " ", trailer).split()
            if "none" not in names and unit in names:
                return sha
        elif unit in re.sub(r"[^A-Za-z0-9-]", " ", subject).split() and check_product_commit(root, sha):
            return sha
    return None


def read_spec_revisions(root, path):
    """[(sha, text before, text after)] of each non-merge commit changing the spec, oldest first; its creation is no
    revision. Before is the text at the commit's first parent."""
    out = run_git(root, "log", "--full-history", "--no-merges", "--date-order", "--reverse", "--format=%H %P", "--",
                  path) or ""
    revs = []
    for ln in out.split("\n"):
        if not ln.strip():
            continue
        sha, *parents = ln.split()
        before = run_git(root, "show", f"{parents[0]}:{path}") if parents else None
        if before is not None:
            revs.append((sha, before, run_git(root, "show", f"{sha}:{path}") or ""))
    return revs


def read_adding_commit(root, path):
    out = (run_git(root, "log", "--diff-filter=A", "--format=%H", "--", path) or "").split()
    return out[-1] if out else None


def scan_audit_pins(root, builds, conf, fam_re):
    """{unit: (N, the commit adding the newest `spec-audit` record whose **Serves:** pins `<unit>@rev-N`)}."""
    found = {}
    for b in builds:
        for p in sorted(Path(root, conf["MEMORY_ROOT"], "builds", b, "reviews").glob("*.md")):
            kind, ids = read_serves(p.read_text(encoding="utf-8"), fam_re)
            add = read_adding_commit(root, os.path.relpath(p, root).replace("\\", "/")) if kind == "spec-audit" else None
            for unit, rev in ids:
                if add and rev is not None:
                    found.setdefault(unit, []).append((rev, add))
    pins = {}
    for unit, cands in found.items():
        newest = (run_git(root, "log", "--no-walk=sorted", "--format=%H", *{c[1] for c in cands}) or "").split()
        pins[unit] = next(c for c in cands if newest and c[1] == newest[0])
    return pins


def derive_revision_members(root, specs, log, pins):
    """The members of the two revision arms: after the first pass, and after the audited revision a pin names."""
    members = []
    for b, path, unit in specs:
        revs = read_spec_revisions(root, path) if unit else []
        first = read_first_pass(root, unit, log) if revs else None
        pin = pins.get(unit)
        for sha, before, after in revs:
            after_pass = first is not None and not check_ancestor(root, sha, first)
            after_audit = pin is not None and not check_ancestor(root, sha, pin[1])
            if not (after_pass or after_audit) or not check_material(before, after):
                continue
            rev = read_header_rev(before)
            addr = f"{unit}@rev-{rev if rev is not None else '?'}"
            if after_pass:
                members.append({"kind": "revision", "build": b, "address": addr, "hand": "spec-revised",
                                "what": f"{unit}'s spec changed at {sha[:9]}, not an ancestor of its first pass "
                                        f"{first[:9]}"})
            if after_audit and (not after_pass or f"{unit}@rev-{pin[0]}" != addr):
                members.append({"kind": "audit", "build": b, "address": f"{unit}@rev-{pin[0]}", "hand": "spec-revised",
                                "what": f"{unit}'s spec changed at {sha[:9]}, past its audited revision rev-{pin[0]} "
                                        f"({pin[1][:9]})"})
    return members


def scan_ledger_members(root, builds, conf, fam_re):
    """Each `amended rev-N` line under an **Evidences:** block of a `journal` record, addressed `<unit>@rev-<N-1>`."""
    members = []
    for b in builds:
        for p in sorted(Path(root, conf["MEMORY_ROOT"], "builds", b).rglob("*.md")):
            text = p.read_text(encoding="utf-8")
            if read_serves(text, fam_re)[0] != "journal":
                continue
            rel, unit = os.path.relpath(p, root).replace("\\", "/"), None
            for n, ln in enumerate(text.split("\n"), 1):
                ev = re.match(r"^\*\*Evidences:\*\* `?([^`\s]+)`?", ln)
                if ev or ln.startswith("#"):
                    unit = ev.group(1) if ev else None
                    continue
                a = LEDGER.match(ln)
                if a and unit:
                    k = int(a.group(2))
                    members.append({"kind": "ledger", "build": b, "address": f"{unit}@rev-{k - 1}",
                                    "hand": "spec-revised",
                                    "what": f"{unit}'s ledger line {a.group(1)} amended rev-{k}, in {rel}:{n}"})
    return members


def read_row_commit(root, row, folder):
    out = (run_git(root, "log", "--reverse", "--format=%H", f"-S{row}", "--", folder) or "").split()
    return out[0] if out else None


def scan_rescope_members(root, builds, conf, spec_of):
    """The add, retire and supersede rows of each chain build's RUN.md and rotated RUN.*.md."""
    members = []
    for b in builds:
        folder = Path(root, conf["MEMORY_ROOT"], "builds", b)
        for p in sorted(folder.glob("RUN*.md")):
            if not RUN_FILE.match(p.name):
                continue
            rel = os.path.relpath(p, root).replace("\\", "/")
            for m in RESCOPE.finditer(p.read_text(encoding="utf-8")):
                act, item = m.group(1), m.group(2)
                if act == "add":
                    members.append({"kind": "add", "build": b, "address": f"new unit {item}", "hand": "design-to-spec",
                                    "what": f"the rescope add of {item}, in {rel}"})
                elif act in ("retire", "supersede"):
                    sha = read_row_commit(root, m.group(0), os.path.relpath(folder, root).replace("\\", "/"))
                    rev = read_header_rev(run_git(root, "show", f"{sha}:{spec_of[item]}")) \
                        if sha and item in spec_of else None
                    members.append({"kind": "rescope", "build": b, "hand": "spec-revised",
                                    "address": f"{item}@rev-{rev if rev is not None else '?'}",
                                    "what": f"the rescope {act} of {item}, in {rel}"})
    return members


def scan_handback_members(root, builds, conf, fam_re, spec_of):
    """Each revision record under a chain build's prompts/ whose Goal opens DIVERGENCE:."""
    members = []
    for b in builds:
        for p in sorted(Path(root, conf["MEMORY_ROOT"], "builds", b, "prompts").glob("*.md")):
            text = p.read_text(encoding="utf-8")
            if not DIVERGENCE.search(text):
                continue
            rel = os.path.relpath(p, root).replace("\\", "/")
            ids = read_serves(text, fam_re)[1]
            unit = ids[0][0] if ids else None
            add = read_adding_commit(root, rel)
            rev = read_header_rev(run_git(root, "show", f"{add}:{spec_of[unit]}")) if add and unit in spec_of else None
            members.append({"kind": "handback", "build": b, "hand": "spec-to-code",
                            "address": f"{unit}@rev-{rev if rev is not None else '?'}",
                            "what": f"{unit}'s divergence hand-back in {rel}"})
    return members


def read_record(path, text):
    f = dict(FIELD.findall(text))
    return {"id": Path(path).stem, "path": path, "departs": f.get("Departs from", ""), "hand": f.get("Hand-off", ""),
            "risk": f.get("Risk", ""), "cause": f.get("Cause", ""), "approver": f.get("Approver"),
            "reason": f.get("Reason"), "follow": f.get("Follow-through", ""), "bound": f.get("Bound"),
            "tier": f.get("Tier"), "surface": f.get("Surface")}


def read_records(root, slug=None):
    pat = f"{slug}/build/*-deviation-*.md" if slug else "*/build/*-deviation-*.md"
    return [read_record(os.path.relpath(p, root).replace("\\", "/"), p.read_text(encoding="utf-8"))
            for p in sorted(Path(root, "memory/builds").glob(pat))]


def read_population(root, pin, slug=None):
    """(members, records, facts) of the tree at `root`, measured against the pin; for one build when `slug` is given."""
    conf, families, fam_re = read_conf_grammar(root)
    now = Path(root, V2).read_text(encoding="utf-8")
    builds = read_chain_builds(now)
    old = run_git(root, "show", f"{pin}:{V2}")
    members = []
    moved = check_baseline(now, pin)
    if moved:
        members.append({"kind": "baseline", "build": None, "address": "v2's Baseline: line", "hand": "design-revised",
                        "what": moved})
    if old is not None:
        o = {cid: (b, h) for b, cid, _t, h in read_chain_clauses(old)}
        n = {cid: (b, h) for b, cid, _t, h in read_chain_clauses(now)}
        for cid in sorted(set(o) | set(n)):
            if cid not in n or cid not in o or o[cid][1] != n[cid][1]:
                b, h = o.get(cid) or n[cid]
                what = (f"{cid} removed since the baseline" if cid not in n else f"{cid} added since the baseline"
                        if cid not in o else f"{cid} moved from {o[cid][1]} to {n[cid][1]} since the baseline")
                members.append({"kind": "clause", "build": b, "address": f"{cid}@{h}", "hand": "design-revised",
                                "what": what})
    specs = read_specs(root, builds, conf, families)
    spec_of = {u: p for _b, p, u in specs if u}
    pins = scan_audit_pins(root, builds, conf, fam_re)
    if specs:
        members += derive_revision_members(root, specs, read_commit_log(root), pins)
    members += scan_ledger_members(root, builds, conf, fam_re)
    members += scan_rescope_members(root, builds, conf, spec_of)
    members += scan_handback_members(root, builds, conf, fam_re, spec_of)
    if slug:
        members = [m for m in members if m["build"] in (None, slug)]
        specs = [s for s in specs if s[0] == slug]
    nopin = [u for _b, _p, u in specs if u and u not in pins]
    return members, read_records(root, slug), {"baseline": old is not None, "specs": len(specs), "nopin": nopin,
                                                "conf": conf, "spec_of": spec_of}


def derive_joins(members, records):
    """[(member, the record joining it, or None)]: a record departing from the member's address, or for an add the
    record whose follow-through is `new unit <item>`; the moved baseline joins none."""
    out = []
    for mb in members:
        if mb["kind"] == "baseline":
            rec = None
        elif mb["kind"] == "add":
            rec = next((r for r in records if r["follow"].replace("`", "").strip() == mb["address"]), None)
        else:
            rec = next((r for r in records if r["departs"].split(" [")[0].strip("` ") == mb["address"]), None)
        out.append((mb, rec))
    return out


def read_decision_rows(root, ref, conf):
    """{decision id: its row} of memory/DECISIONS.md at `ref`, read with the kit's row regex, or None."""
    text = run_git(root, "show", f"{ref}:memory/DECISIONS.md")
    if text is None:
        return None
    rowre = row_grammar.derive_row_re(conf)
    return {m.group(1): ln for ln in text.split("\n") for m in [rowre.match(ln)] if m}


def check_approver(rec, rows, conf, ref):
    """Why `author-recorded` refuses the record's approver, or None (P0.1 row 6)."""
    a = (rec["approver"] or "").strip()
    role = next((r for r in ROLES if a.lower().startswith(r)), None)
    if role is None:
        return f"its approver '{a}' names no role the record grammar names" if a else "it records no approver"
    if role != "owner":
        return None
    cited = list(dict.fromkeys(m.group(0) for m in row_grammar.id_pattern(conf).finditer(a)))
    if not cited:
        return f"its approver '{a}' names the owner and cites no decision id"
    clause = re.match(r"`?(cl-d[A-Z]\w+-\d{4})@", rec["departs"])
    unit = re.match(r"new unit `?([^`\s]+)", rec["follow"].strip())
    names = [x.group(1) for x in (clause, unit) if x]
    held = [c for c in cited if c in (rows or {})]
    for c in held:
        if any(re.search(r"(?<![A-Za-z0-9-])" + re.escape(x) + r"(?![A-Za-z0-9-])", rows[c]) for x in names):
            return None
    if not held:
        return f"its approver cites {', '.join(cited)}, which no row of memory/DECISIONS.md at {ref} holds"
    return (f"its approver cites {', '.join(held)}, whose row does not name "
            + (" or ".join(names) if names else "a departed clause or a new unit, and the record names neither"))


def check_records(records, rows, conf, ref):
    """[(record id, why)] for each record whose approver the chain's value refuses, or whose follow-through names no
    clause at a hash."""
    out = []
    for r in records:
        why = check_approver(r, rows, conf, ref)
        if why:
            out.append((r["id"], why))
        if r["follow"].startswith(("amends", "supersedes")) and not re.search(r"cl-d[A-Z]\w+-\d{4}@[0-9a-f]{8}",
                                                                               r["follow"]):
            out.append((r["id"], "its follow-through names no clause at a hash"))
    return out


def print_population(root, pin, policy, label, ref="origin/main"):
    members, records, facts = read_population(root, pin)
    rows = read_decision_rows(root, ref, facts["conf"])
    joined = derive_joins(members, records)
    refused = check_records(records, rows, facts["conf"], ref)
    unjoined = sum(1 for _m, r in joined if r is None)
    print(f"deviations: baseline {pin[:9]} {'read' if facts['baseline'] else 'unread'}, chain-build specs "
          f"{facts['specs']}, members {len(members)} ({unjoined} unjoined), records {len(records)} · refused "
          f"{len(refused)} · policy {policy}{label}")
    for mb, rec in joined:
        print(f"  {mb['what']}, at {mb['address']} ({mb['hand']}): "
              + (f"joins {rec['id']}" if rec else "recorded by nobody"))
    for rid, why in refused:
        print(f"  refused: {rid}: {why}")
    if rows is None:
        print(f"  memory/DECISIONS.md is unread at {ref}, so every owner citation is refused")
    if facts["nopin"]:
        print(f"  no audit pin: {', '.join(facts['nopin'])}")
    if not facts["baseline"] and not facts["specs"]:
        print("deviations: neither the pin's v2 nor a chain build's spec is readable, so nothing is measured and the "
              "run is never green")
        return 2
    return 1 if policy == "refuse" and (unjoined or refused) else 0


def read_keys(text):
    """{key: value} of the first `widens:`, `relaxes:` and `grants:` a trailer or mark carries."""
    out = {}
    for m in KEY.finditer(text):
        out.setdefault(m.group(1), m.group(2).strip().strip("`"))
    return out


def read_prepared_base(root):
    """P: the first parent of the nearest merge on HEAD's first-parent line, as check_prepared_merge finds it."""
    t = (run_git(root, "rev-list", "--first-parent", "--min-parents=2", "--max-count=1", "HEAD") or "").strip()
    if not t:
        return None
    return (run_git(root, "rev-parse", "--verify", "--quiet", f"{t}^1") or "").strip() or None


def derive_run_kind(root, slug, base, conf, families):
    """(kind, open asks, roster units with no spec), README rule 1's test at the run's base."""
    m = conf["MEMORY_ROOT"]
    readme = run_git(root, "show", f"{base}:{m}/builds/{slug}/README.md") or ""
    backlog = run_git(root, "show", f"{base}:{m}/builds/{slug}/BACKLOG.md") or ""
    asks = [a for a, is_open in bareids.read_asks(backlog, conf) if is_open and a.split("-")[1] == slug]
    roster = bareids.read_roster_units(readme, gbi.build_roster_id_re(set(families)))
    defined = set()
    for rel in (run_git(root, "ls-tree", "-r", "--name-only", base, "--", f"{m}/builds/{slug}/spec/") or "").split():
        hit = gbi.parse_spec_h1(rel, run_git(root, "show", f"{base}:{rel}") or "", m, families)
        if hit:
            defined.add(hit[1])
    missing = [u for u in roster if u not in defined]
    return ("spec" if asks and missing else "build"), asks, missing


@functools.lru_cache(maxsize=None)
def run_instrument(*args):
    """(exit, stdout) of a sibling instrument, run in the worktree, which holds its inputs."""
    done = subprocess.run([sys.executable, "-B", *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    return done.returncode, done.stdout.rstrip("\n")


def check_ask_rows_only(root, start, path):
    """True when a BACKLOG.md's change over the range only adds ask and SEV rows (P0.6, rules 3 and 5)."""
    if not re.match(r"^memory/builds/[^/]+/BACKLOG\.md$", path) or run_git(root, "cat-file", "-e", f"{start}:{path}") \
            is None:
        return False
    diff = run_git(root, "diff", "--no-color", "-U0", start, "HEAD", "--", path) or ""
    families = read_conf_grammar(root)[1]
    grammar = gbi.backlog.build_grammar(families)
    for ln in diff.split("\n"):
        if ln.startswith(("---", "+++", "@@", "diff ", "index ")) or not ln:
            continue
        row = gbi.backlog.extract_row(ln[1:], grammar) if ln.startswith("+") else None
        if ln.startswith("-") or (ln[1:].strip() and (row is None or row.cls not in ("ask", "severity"))):
            return False
    return True


@functools.lru_cache(maxsize=None)
def read_switch_slugs():
    """The chain builds whose landing owes the report-switch ask: each slug in the "Lands with" column of the [phase-1]
    retirement table, read from the worktree's plan, in table order."""
    phase1 = Path(PLAN).read_text(encoding="utf-8").split("\n## [phase-1]", 1)[-1].split("\n## ", 1)[0]
    if RETIREMENT_HEAD not in phase1:
        raise Unmeasured(f"{PLAN}'s [phase-1] holds no retirement table headed {RETIREMENT_HEAD}")
    slugs = []
    for ln in phase1.split(RETIREMENT_HEAD, 1)[1].split("\n\n", 1)[0].split("\n")[2:]:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) > 2 and re.fullmatch(r"d[A-Z][A-Za-z]+", cells[2]):
            slugs.append(cells[2])
    return tuple(dict.fromkeys(slugs))


def read_switch_ask(root, slug, families):
    """The report-switch ask `slug`'s landing filed in dClosedLoop's BACKLOG.md at HEAD, or None: an ask row, as the
    index generator's backlog grammar reads it, naming `report-switch`, minted under `slug` (P0.6 rule 3) or filed late
    under dClosedLoop's own slug with `slug` as a whole word in its text, as PLAY-dClosedLoop-25 was for dTrueNorth."""
    grammar = gbi.backlog.build_grammar(families)
    for ln in (run_git(root, "show", f"HEAD:{SWITCH_BACKLOG}") or "").split("\n"):
        row = gbi.backlog.extract_row(ln, grammar)
        if row is None or row.cls != "ask" or SWITCH not in ln:
            continue
        minter = row.target.split("-")[1]
        if minter == slug or (minter == "dClosedLoop" and re.search(rf"\b{slug}\b", ln)):
            return row.target
    return None


def check_gen_only(root, start, path):
    """True when the file exists at both ends of the range and differs only inside gen regions: a render."""
    a, b = run_git(root, "show", f"{start}:{path}"), run_git(root, "show", f"HEAD:{path}")
    return a is not None and b is not None and extract_outside_gen(a) == extract_outside_gen(b)


def read_report_sources(root, slug, pin, control=None):
    """Everything the report renders, read from the tree at `root` (P0.2's sources)."""
    conf, families, fam_re = read_conf_grammar(root)
    m = conf["MEMORY_ROOT"]
    run_path = Path(root, m, "builds", slug, "RUN.md")
    if not run_path.is_file():
        raise Unmeasured(f"{m}/builds/{slug}/RUN.md is absent, so no live run names a base: and the report has no run "
                         "kind")
    run = run_path.read_text(encoding="utf-8")
    base = re.search(r"^base: ([0-9a-f]{7,40})\s*$", run, flags=re.M)
    if not base:
        raise Unmeasured(f"{m}/builds/{slug}/RUN.md records no base:, so the run kind cannot be read")
    base = base.group(1)
    p = read_prepared_base(root)
    if not p:
        raise Unmeasured("HEAD carries no prepared merge on its first-parent line, so the range P..HEAD has no P")
    roster = bareids.read_roster_units(Path(root, m, "builds", slug, "README.md").read_text(encoding="utf-8")
                                       if Path(root, m, "builds", slug, "README.md").is_file() else "",
                                       gbi.build_roster_id_re(set(families)))
    if not roster:
        raise Unmeasured(f"{slug}'s README names no roster unit, so the report has no name")
    kind, asks, missing = derive_run_kind(root, slug, base, conf, families)
    start = base if control == "base-range" else p
    members, records, facts = read_population(root, pin, slug)
    rows = read_decision_rows(root, p, conf)
    trailers = []
    out = run_git(root, "log", "--reverse", "--format=%H%x1f%(trailers:key=Decided,valueonly,unfold,separator=%x1d)%x1e",
                  f"{start}..HEAD") or ""
    for rec in out.split("\x1e"):
        sha, _, vals = rec.strip("\n").partition("\x1f")
        trailers += [(sha, v.strip()) for v in vals.split("\x1d") if v.strip()]
    paths = [x for x in (run_git(root, "diff", "--name-only", "-z", f"{start}..HEAD") or "").split("\0") if x]
    marks = []
    for _b, rel, _u in [s for s in read_specs(root, [slug], conf, families)]:
        for n, ln in enumerate(Path(root, rel).read_text(encoding="utf-8").split("\n"), 1):
            if "RESOLVED (" in ln:
                marks.append((rel, n, ln.strip()))
    run_rel = f"{m}/builds/{slug}/RUN.md"
    parks = [(f"{run_rel}:{run[:x.start()].count(chr(10)) + 1}", x.group(1), x.group(2)) for x in PARK.finditer(run)]
    rescopes = [(x.group(1), x.group(2)) for x in RESCOPE.finditer(run)]
    deferred = [u for act, u in rescopes if act == "defer"]
    product = {w for x in DISPATCH.finditer(run) for w in x.group(2).split()} if kind == "build" else set()
    blobs = [(i, (run_git(root, "rev-parse", "--verify", "--quiet", f"HEAD:{i}") or "").strip()) for i in INSTRUMENTS]
    switch_owed = kind == "build" and slug in read_switch_slugs()
    switch_ask = read_switch_ask(root, slug, families) if switch_owed else None
    return {"switch_owed": switch_owed, "switch_ask": switch_ask,"root": root, "slug": slug, "kind": kind, "asks": asks, "missing": missing, "base": base, "p": p,
            "start": start, "first": roster[0], "members": members, "records": records, "facts": facts, "rows": rows,
            "conf": conf, "trailers": trailers, "paths": paths, "marks": marks, "parks": parks, "deferred": deferred,
            "added": [u for act, u in rescopes if act == "add"], "product": product, "blobs": blobs}


def read_mark_record(records, key, value):
    """The record a non-`none` mark joins: a `relaxes:` value the record whose **Bound:** it is, a `widens:` value the
    record whose **Surface:** it is."""
    field = "bound" if key == "relaxes" else "surface"
    return next((r for r in records if (r[field] or "").strip().strip("`") == value), None)


def render_mark_entry(keys, source, records):
    """A marked choice's entry text, or None when its `widens:`, `relaxes:` and `grants:` are all `none` or absent."""
    if all(keys.get(k, "none") == "none" for k in ("widens", "relaxes", "grants")):
        return None
    parts = []
    for k in ("widens", "relaxes", "grants"):
        v = keys.get(k, "none")
        r = read_mark_record(records, k, v) if k != "grants" and v != "none" else None
        parts.append(f"{k} [{v}]" + (f" joins {r['id'] if r else 'nobody'}" if k != "grants" and v != "none" else ""))
    return "choice · " + " · ".join(parts) + f" · {source}"


def derive_entries(src):
    """[(type, text)]: the report's entries in P0.2's order, marked choices first."""
    recs = src["records"]
    choices, forks = [], []
    for sha, value in src["trailers"]:
        pick, _, why = value.partition(" — ")
        e = render_mark_entry(read_keys(value), f"Decided: {value} · commit {sha[:9]}", recs)
        choices += [("choice", e)] if e else []
        forks += [] if e else [("fork", f"fork · question not recorded · pick {pick} · reason "
                                        f"{why.split(' · ')[0] or 'none'} · Decided: {value} · commit {sha[:9]}")]
    for rel, n, ln in src["marks"]:
        q, _, rest = ln.partition("RESOLVED (")
        pick = rest.split("):", 1)[1].strip() if "):" in rest else rest
        e = render_mark_entry(read_keys(ln), f"§8 {rel}:{n}: {ln}", recs)
        choices += [("choice", e)] if e else []
        forks += [] if e else [("fork", f"fork · question {q.strip(' -*') or 'not recorded'} · pick "
                                        f"{pick.split(' — ')[0]} · reason {pick.partition(' — ')[2] or 'none'} · "
                                        f"§8 {rel}:{n}")]
    for where, item, why in src["parks"]:
        forks.append(("fork", f"fork · question {item} · pick parked · reason {why} · {where}"))
    members = []
    refused = dict(check_records(recs, src["rows"], src["conf"], src["p"]))
    for mb, r in derive_joins(src["members"], recs):
        head = f"member · {mb['address']} · {mb['hand']} · {mb['what']}"
        if r is None:
            members.append(("member", head + " · recorded by nobody"))
            continue
        tail = "".join(f" · {k} {r[k]}" for k in ("bound", "tier", "surface") if r[k])
        members.append(("member", f"{head} · joins {r['id']} · reason {r['reason'] or 'none'} · risk {r['risk'] or 'none'}"
                                  f" · approver {r['approver'] or 'none'} · follow-through {r['follow'] or 'none'}{tail}"
                                  + (f" · refused: {refused[r['id']]}" if r["id"] in refused else "")))
    spec_of = src["facts"]["spec_of"]
    carried = []
    for u in src["deferred"]:
        tail = re.search(r"\badvances (\S+)", Path(src["root"], spec_of[u]).read_text(encoding="utf-8")) \
            if u in spec_of else None
        carried.append(("carried", f"carried · {u} · ask {tail.group(1) if tail else 'none'}"))
    carried += [("added", f"added · {u} · " + ("carried to the build run" if u in src["deferred"] else "built in this run"))
                for u in src["added"]]
    outside = [("outside", f"outside · {p}") for p in src["paths"]
               if not p.startswith(f"memory/builds/{src['slug']}/") and p not in src["product"]
               and not p.startswith(SHARED_RENDERS) and not check_gen_only(src["root"], src["start"], p)
               and not check_ask_rows_only(src["root"], src["start"], p)]
    return choices + members + forks + carried + outside


def read_coverage_region(root, slug):
    """The build README's `build-coverage` region, cl-dClosedLoop-0003's coverage as the index generator rendered it,
    its markers stripped; None when the README or the region is absent."""
    mo, mc = next((o, c) for n, o, c in gbi.GEN_REGIONS if n == "build-coverage")
    readme = Path(root, f"memory/builds/{slug}/README.md")
    text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    a, b = text.find(mo), text.find(mc)
    return text[a + len(mo):b].strip("\n") if 0 <= a < b else None


def render_report(src, entries):
    slug, s = src["slug"], src
    cov = read_coverage_region(src["root"], slug)
    a_exit, a_out = run_instrument(VIEW, "--check")
    lines = [f"# Departures: {slug}, its {s['kind']} run", "", f"**Serves:** journal {s['first']}", "",
             f"Generated by `{SELF}` `--report {slug}` on the prepared merge (README rule 4). Never edit it by hand: "
             "`--check` renders it again and compares the bytes, and its validating arm parses it.", "", "## Head", "",
             f"- run kind: {s['kind']}, read at base `{s['base']}`: open asks {', '.join(s['asks']) or 'none'}; roster "
             f"units with no spec {', '.join(s['missing']) or 'none'}",
             f"- range: `{s['start']}..HEAD`", f"- decisions read at: `{s['p']}`"]
    lines += [f"- instrument `{i}` blob `{b or 'untracked'}`" for i, b in s["blobs"]]
    lines += [f"- no audit pin: {', '.join(s['facts']['nopin']) or 'none'}",
              "- report-switch ask: " + (f"{s['switch_ask']}, in `{SWITCH_BACKLOG}`" if s["switch_ask"]
                                         else "owed, none filed" if s["switch_owed"]
                                         else "not owed, a spec run" if s["kind"] == "spec"
                                         else f"not owed, {slug} lands no row of the [phase-1] retirement table"),
              "", "## Entries", ""]
    lines += [f"- entry {n} · {text}" for n, (_t, text) in enumerate(entries, 1)] or ["none"]
    lines += ["", f"## The coverage region of `memory/builds/{slug}/README.md`", "", "```text",
              cov if cov is not None else "no build-coverage region", "```", "",
              f"## `{VIEW} --check`, exit {a_exit}", "", "```text", a_out, "```"]
    return "\n".join(lines) + "\n"


def check_report(text, src):
    """The validating arm (P0.2): findings from the rendered report and the range's trailers."""
    findings = []
    entries = ENTRY.findall(text)
    types = [t for _n, t, _r in entries]
    if "choice" in types:
        last = max(i for i, t in enumerate(types) if t == "choice")
        other = next((i for i, t in enumerate(types) if t != "choice"), len(types))
        if other < last:
            findings.append(f"entry {entries[last][0]}, a marked choice, comes after entry {entries[other][0]}, a "
                            f"{types[other]}")
    for sha, value in src["trailers"]:
        if f"Decided: {value}" not in text:
            findings.append(f"the Decided: trailer of {sha[:9]} does not appear: {value[:90]}")
    recs = {r["id"]: r for r in src["records"]}
    for n, t, rest in entries:
        for key, val, rid in (CHOICE_KEY.findall(rest.split(" · Decided: ")[0].split(" · §8 ")[0])
                              if t == "choice" else []):
            if key == "grants" or val == "none":
                continue
            need = ("bound", "tier", "reason") if key == "relaxes" else ("surface", "reason")
            r = recs.get(rid)
            lack = [f for f in need if r is None or not r[f]]
            if r is None:
                findings.append(f"entry {n}'s {key}: [{val}] joins no record")
            elif lack:
                findings.append(f"entry {n}'s {key}: [{val}] joins {rid}, which carries no "
                                + " and no ".join(f"**{f.capitalize()}:**" for f in lack))
    for sha, value in src["trailers"]:
        cites = [x for x in RULINGS if x in value]
        keys = read_keys(value)
        lack = [k for k in ("widens", "relaxes") if k not in keys]
        if cites and lack:
            findings.append(f"the trailer of {sha[:9]} cites {cites[0]} and carries no {' and no '.join(k + ':' for k in lack)}")
        if "ER:388" in cites and keys.get("widens") == "none":
            findings.append(f"the trailer of {sha[:9]} cites ER:388 and its widens: is none")
        if "ER:328" in cites and keys.get("relaxes") == "none":
            findings.append(f"the trailer of {sha[:9]} cites ER:328 and its relaxes: is none")
    if src["switch_owed"] and not src["switch_ask"]:
        findings.append(f"report-switch ask owed: {src['slug']} lands a row of the execution plan's [phase-1] "
                        f"retirement table, and {SWITCH_BACKLOG} holds no ask minted under {src['slug']} naming "
                        f"{SWITCH} (P0.6 rule 3)")
    return findings


def check_bytes(path, text):
    """The byte compare: why the written report differs from its render, or None."""
    if not path or not Path(path).is_file():
        return f"no report is written at {path}"
    a, b = Path(path).read_bytes().decode("utf-8", "replace").split("\n"), text.split("\n")
    if a == b and Path(path).read_bytes() == text.encode("utf-8"):
        return None
    n = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    return f"the written report differs from its render from line {n + 1}: {a[n][:100] if n < len(a) else 'EOF'}"


def derive_report_path(src, date):
    return str(Path(src["root"], f"memory/builds/{src['slug']}/build/{date}-build-{src['first']}-departures-"
                                 f"{src['kind']}.md"))


def scan_written_report(src):
    hits = sorted(Path(src["root"], f"memory/builds/{src['slug']}/build").glob(
        f"*-build-{src['first']}-departures-{src['kind']}.md"))
    return str(hits[-1]) if hits else None


def write_report(path, text):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def cmd_report(slug, mode):
    src = read_report_sources(".", slug, BASELINE)
    text = render_report(src, derive_entries(src))
    findings = check_report(text, src)
    if mode == "write":
        path = derive_report_path(src, datetime.date.today().isoformat())
        write_report(path, text)
        findings += [x for x in [check_bytes(path, text)] if x]
        print(f"deviations: wrote {Path(path).as_posix()}")
    elif mode == "check":
        path = scan_written_report(src)
        findings += [x for x in [check_bytes(path, text)] if x]
    else:
        sys.stdout.write(text)
    print(f"deviations: report {slug} · {src['kind']} run · entries {len(ENTRY.findall(text))} · findings "
          f"{len(findings)}")
    for f in findings:
        print(f"  {f}")
    return 1 if findings else 0


# ---------------------------------------------------------------------------------------------- the fixture
FIXTURE_FAMILY = "FIX"     # declared only in the fixture repository's own conf, so the tree's grammar joins none
PLANTS = ("baseline", "clause", "subject-pass", "pass-none", "status-flip", "two-branch", "header-rev", "gen",
          "status-gen", "gen-text", "quote", "amended", "amended-joined", "approver-none", "owner-bare", "owner-er",
          "owner-row5", "owner-row1-added", "owner-unknown-id", "approver", "add", "handback", "audit-pin", "defer",
          "fix-record", "audit-nopin")
REPORT_PLANTS = PLANTS + ("kind-spec", "kind-build", "kind-whole", "kind-norun", "stub-widens", "stub-relaxes",
                          "stub-grants", "stub-drop", "omit-grant", "record-no-tier", "record-no-reason",
                          "record-no-surface", "trailer-relaxes-only", "trailer-widens-only", "trailer-388-none",
                          "trailer-240-none", "trailer-rung6", "outside-packet", "outside-product", "range",
                          "record-late", "hand-edit", "instrument-byte", "switch-missing", "switch-foreign",
                          "switch-spec", "switch-late")
CONTROLS = ("no-arm", "base-range")
# Each approver plant: the clause it moves, and the approver of the record departing from it (P0.1 row 6).
APPROVER_PLANTS = {"owner-bare": ("cl-dClosedLoop-0001", "owner"),
                   "owner-er": ("cl-dClosedLoop-0002", "owner, quoted at ER:189"),
                   "owner-row5": ("cl-dClosedLoop-0003", "owner, FIX-dClosedLoop-6"),
                   "owner-unknown-id": ("cl-dClosedLoop-0005", "owner, FIX-dClosedLoop-99"),
                   "approver-none": ("cl-dClosedLoop-0006", None),
                   "approver": ("cl-dClosedLoop-0007", "author")}
# The unit each plant writes; the base writes FIX-dTrueNorth-1, -2, -3 and -99, and the opened roster is -80 and -81.
PLANT_UNITS = {"subject-pass": "FIX-dTrueNorth-10", "pass-none": "FIX-dTrueNorth-11", "status-flip": "FIX-dTrueNorth-12",
               "two-branch": "FIX-dTrueNorth-13", "header-rev": "FIX-dTrueNorth-14", "gen": "FIX-dTrueNorth-15",
               "status-gen": "FIX-dTrueNorth-16", "gen-text": "FIX-dTrueNorth-17", "quote": "FIX-dTrueNorth-18",
               "amended": "FIX-dTrueNorth-19", "amended-joined": "FIX-dTrueNorth-20",
               "owner-row1-added": "FIX-dTrueNorth-21", "add": "FIX-dTrueNorth-22", "handback": "FIX-dTrueNorth-23",
               "audit-pin": "FIX-dTrueNorth-24", "defer": "FIX-dTrueNorth-25", "fix-record": "FIX-dTrueNorth-26",
               "audit-nopin": "FIX-dTrueNorth-27", "record-late": "FIX-dTrueNorth-28"}
DECISIONS_TEXT = "\n".join([
    "# Decisions", "",
    "- FIX-dClosedLoop-2 · the spec-run close by carry-forward, and dTrueNorth's extra unit FIX-dTrueNorth-99 approved "
    "as a departure (ER:84, ER:232, ER:320)",
    "- FIX-dClosedLoop-3 · the grant every chain build's may: line cites (ER:181)",
    "- FIX-dClosedLoop-4 · the chain's deviation values, report and author-recorded, and the departure from "
    "cl-dClosedLoop-0004 (ER:103-104, ER:189)",
    "- FIX-dClosedLoop-6 · the standing ruling for residual forks (ER:240, ER:388, ER:328)",
    "- FIX-dClosedLoop-7 · the driver-rewriting builds land through their own code, and dPlacedRequest's migration of "
    "cl-dClosedLoop-0120 (ER:248, ER:264)", ""])
TN = "memory/builds/dTrueNorth/"


class Fixture:
    """A temporary git repository holding v2's `[chain]`, the fixture family, and the plants' histories."""

    def __init__(self, root):
        self.root, self.tick, self.n, self.rows = root, 0, 0, []
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        self.env.update(GIT_AUTHOR_NAME="fixture", GIT_AUTHOR_EMAIL="fixture@example.invalid",
                        GIT_COMMITTER_NAME="fixture", GIT_COMMITTER_EMAIL="fixture@example.invalid")
        self.pin = self.v2 = self.base = None

    def run(self, *args):
        self.tick += 1
        env = dict(self.env, GIT_AUTHOR_DATE=f"@{1792576800 + self.tick} +0000",
                   GIT_COMMITTER_DATE=f"@{1792576800 + self.tick} +0000")
        out = run_git(self.root, *args, env=env)
        if out is None:
            raise RuntimeError(f"fixture: git {' '.join(args)} failed in {self.root}")
        return out

    def write_commit(self, files, subject, trailers=(), allow_empty=True):
        for rel, body in files.items():
            p = Path(self.root, rel)
            if body is None:
                p.unlink()
                continue
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(body if isinstance(body, bytes) else body.encode("utf-8"))
        self.run("add", "-A")
        self.run("commit", "-q", *(["--allow-empty"] if allow_empty else []), "-m",
                 subject + ("\n\n" + "\n".join(trailers) if trailers else ""))
        return self.run("rev-parse", "HEAD").strip()

    def render_spec(self, unit, rev, status="OPEN", line="the fixture line holds", records="", extra=""):
        return "\n".join([f"# {unit} — fixture unit", "",
                          f"**Status:** {status} · rev-{rev} · 2026-10-21 · node d · Tier-2 · base 0123abcd · streams "
                          "playbook", "", "## 6. Acceptance criteria", "", f"- AC1: {line}"]
                         + ([extra] if extra else []) + ["", "<!-- gen:spec-records -->", "| Record | Kind |",
                                                         "|---|---|"] + ([records] if records else [])
                         + ["<!-- /gen:spec-records -->", ""])

    def derive_spec_path(self, unit):
        return f"{TN}spec/2026-10-21-spec-{unit}.md"

    def write_spec(self, unit, rev, **kw):
        return self.write_commit({self.derive_spec_path(unit): self.render_spec(unit, rev, **kw)},
                                 f"spec(dTrueNorth): {unit} rev-{rev}", ["Pass: none"])

    def write_pass(self, unit, trailer=True):
        """The unit's `--dispatch --writes` row, then its product commit."""
        out = f"tools/fix-{unit.rsplit('-', 1)[1]}.txt"
        self.add_run_row(f"dispatch · item 0a1b2c3d {unit} · reason {out} {self.derive_spec_path(unit)}")
        return self.write_commit({out: "built\n"}, f"build {unit} from its spec", [f"Pass: {unit}"] if trailer else ())

    def render_record(self, unit, departs, approver, risk="additive", cause="builder discovery", hand="spec-revised",
                      follow="gap gap-build-07", reason="the fixture's departure", **extra):
        self.n += 1
        fields = [("Departs from", departs), ("Hand-off", hand), ("Before", "the text departed from"),
                  ("After", "the text that replaced it"), ("Cause", cause), ("Reason", reason),
                  ("Evidence", "the fixture"), ("Risk", risk), ("Approver", approver), ("Follow-through", follow)]
        fields += [(k.capitalize(), v) for k, v in extra.items()]
        text = "\n".join([f"# {unit} deviation {self.n}", "", f"**Serves:** research {unit}", ""]
                         + [f"- **{k}:** {v}" for k, v in fields if v is not None]) + "\n"
        return f"{TN}build/2026-10-21-build-{unit}-deviation-{self.n}.md", text

    def add_run_row(self, row):
        self.rows.append(f"2026-10-21T10:{len(self.rows) // 60:02d}:{len(self.rows) % 60:02d}Z {row}")
        return self.write_commit({TN + "RUN.md": self.render_run()}, f"unattended(dTrueNorth): {row.split(' · ')[0]}")

    def render_run(self):
        return "\n".join(["# dTrueNorth - run state", "", "## Run facts", "phase: BUILDING", f"base: {self.base}", "",
                          "## Parked", ""] + [r + "\n" for r in self.rows])

    def set_moved_clause(self, cid, words="and a planted amendment "):
        i = self.v2.index(f"`{cid}`")
        self.v2 = self.v2[:i] + words + self.v2[i:]

    def render_prompt(self, unit, divergence):
        goal = ("DIVERGENCE: the spec's §6 cannot be built as written" if divergence
                else "Fix the wording of the spec's fixture line.")
        return "\n".join([f"# Revision — dTrueNorth: {unit}", "", f"**Serves:** research {unit}", "", "## The brief",
                          "", "### Goal", goal, "", "### Items", "1. revise it", ""])

    def render_audit(self, unit, pin):
        return "\n".join([f"# M4 spec audit — {unit}", "", f"**Serves:** spec-audit {unit}"
                          + (f"@rev-{pin}" if pin else ""), "", "**Verdict:** CLEAN", ""])

    def render_ledger(self, unit, rev):
        return "\n".join([f"# {unit} acceptance ledger", "", f"**Serves:** journal {unit}", "",
                          f"**Evidences:** {unit}", f"- AC1 — amended rev-{rev} — the fixture line narrowed, logged in §9",
                          "- AC2 — `fixture` — observed", ""])

    def run_merge(self, branch, subject):
        self.run("merge", "--no-ff", "-q", "-m", subject, branch)


def render_fixture_readme(units):
    return "\n".join(["---", "slug: dTrueNorth", "---", "", "# dTrueNorth — the fixture build", "", gbi.PLAN_OPEN,
                      "| # | Unit |", "|---|---|"] + [f"| {n} | `{u}` |" for n, u in enumerate(units, 1)]
                     + [gbi.PLAN_CLOSE, ""])


def render_fixture_backlog(ask):
    return "\n".join(["# dTrueNorth — asks", "", "## Asks", "",
                      f"- {ask} · filed 2026-10-21 · build every roster unit of this build from its spec", "",
                      "## Dispositions", "", f"- SEV · {ask} · MED · the build's units stay unbuilt", ""])


def render_switch_backlog(ask):
    """dClosedLoop's BACKLOG.md in the fixture: empty at the baseline, then the report-switch ask the landing files,
    its text naming the landing build, as an ask the opening's own grammar reads."""
    rows = [f"- {ask} · filed 2026-10-21 · THE {SWITCH} STEP AT dTrueNorth'S LANDING. the report still reads the "
            "retired instruments · accept the report reads their successors"] if ask else []
    sev = [f"- SEV · {ask} · LOW · the report reads the retired instruments"] if ask else []
    return "\n".join(["# dClosedLoop — asks", "", "## Asks", ""] + rows + ["", "## Dispositions", ""] + sev + [""])


def add_base(fx, plants):
    """The base history, every member joined: a revision, a hand-back and a ledger line on one record; a supersede; a
    clause moved by the owner's row 3; the extra unit added by row 1; and the marked choices, a fork and a park."""
    u1, u2 = "FIX-dTrueNorth-1", "FIX-dTrueNorth-2"
    fx.write_commit({TN + "RUN.md": fx.render_run()}, "unattended(dTrueNorth): preflight", ["Pass: none"])
    fx.write_spec(u1, 1)
    fx.write_commit({f"{TN}prompts/2026-10-21-prompt-{u1}-1-revision.md": fx.render_prompt(u1, True)},
                    f"records(dTrueNorth): {u1}'s divergence hand-back", ["Pass: none"])
    fx.write_pass(u1)
    fx.write_spec(u1, 2, line="the fixture line holds, narrowed")
    path, text = fx.render_record(u1, f"{u1}@rev-1 [acceptance]", "spec writer, re-audited at rev-2")
    fx.write_commit({f"{TN}build/2026-10-21-build-{u1}-1-acceptance-ledger.md": fx.render_ledger(u1, 2), path: text},
                    f"records(dTrueNorth): {u1}'s ledger and its deviation", ["Pass: none"])
    fx.write_spec(u2, 1, extra="\n## 8. Open questions\n\n- F1 which store holds the cache? RESOLVED (agent, 2026-10-21, "
                               "delegated): the tree — v2 answers it")
    fx.add_run_row(f"rescope · item supersede {u2} -> FIX-dTrueNorth-3 · reason building found it two units")
    path, text = fx.render_record(u2, f"{u2}@rev-1 [scope]", "author", follow="new unit FIX-dTrueNorth-3")
    fx.write_commit({path: text}, f"records(dTrueNorth): {u2}'s supersession recorded", ["Pass: none"])
    h = fx.hashes["cl-dClosedLoop-0004"]
    fx.set_moved_clause("cl-dClosedLoop-0004")
    path, text = fx.render_record(u1, f"`cl-dClosedLoop-0004@{h}` [chain]", "owner, FIX-dClosedLoop-4", risk="stricter",
                                  cause="owner ruling", hand="design-revised", follow=f"amends cl-dClosedLoop-0004@{h}")
    fx.write_commit({V2: fx.v2, path: text}, "records(dTrueNorth): cl-dClosedLoop-0004 amended by the owner's row")
    fx.add_run_row("rescope · item add FIX-dTrueNorth-99 · reason dTrueNorth's extra unit, the owner's row 1")
    path, text = fx.render_record("FIX-dTrueNorth-99", "dTrueNorth [chain]", "owner, FIX-dClosedLoop-2",
                                  hand="design-to-spec", follow="new unit FIX-dTrueNorth-99")
    fx.write_commit({path: text, "memory/LIVE.md": "# live\n\nre-rendered\n"},
                    "records(dTrueNorth): the extra unit's record; LIVE.md re-rendered")
    w, r = "the help renderer's public flags", "the 200 ms render bound"
    path, text = fx.render_record(u1, f"{u1}@rev-2 [scope]", "author, citing ER:240", reason="the only option left",
                                  surface=None if "record-no-surface" in plants else w)
    fx.write_commit({path: text}, f"spec(dTrueNorth): {u1}'s renderer surface widened",
                    [f"Decided: took the wider renderer surface — the only option meeting AC2 · ER:240 · widens: {w} · "
                     "relaxes: none"])
    path, text = fx.render_record(u1, f"{u1}@rev-2 [acceptance]", "author, citing ER:328",
                                  reason=None if "record-no-reason" in plants else "the weakest bound, a writer's own",
                                  bound=r, tier=None if "record-no-tier" in plants else "weakest")
    fx.write_commit({path: text}, f"spec(dTrueNorth): {u1}'s render bound relaxed",
                    [f"Decided: dropped the 200 ms render bound — no option was left · ER:328 · widens: none · relaxes: "
                     f"{r}"])
    fx.write_commit({}, f"build {u1}'s policy table",
                    ["Decided: took the policy table change — the build's grant covers it · grants: FIX-dClosedLoop-3 "
                     "the policy table change"])
    fx.write_commit({}, f"build {u1}'s slower path",
                    ["Decided: kept the slower path — it fails only the goal bound · ER:240 · widens: none · relaxes: "
                     "none"])
    fx.add_run_row("decision · item which clock the bound reads · reason options: wall or monotonic; refused: no probe "
                   "decides it")


def add_plant(fx, plant):
    """One plant's history, on its own unit, clause or row, so every plant composes with every other."""
    u, u1 = PLANT_UNITS.get(plant), "FIX-dTrueNorth-1"
    if plant == "baseline":
        fx.set_moved_clause("cl-dClosedLoop-0119", "loosened, so the owner is never asked, ")
        loose = fx.write_commit({V2: fx.v2}, "records(dClosedLoop): cl-dClosedLoop-0119 loosened")
        fx.v2 = re.sub(r"(?m)^Baseline: `[0-9a-f]+`", f"Baseline: `{loose}`", fx.v2)
        fx.write_commit({V2: fx.v2}, "records(dClosedLoop): the baseline re-pointed past the loosening")
    elif plant == "clause":
        fx.set_moved_clause("cl-dClosedLoop-0008")
        fx.write_commit({V2: fx.v2}, "records(dClosedLoop): cl-dClosedLoop-0008 edited, and no record")
    elif plant in APPROVER_PLANTS:
        cid, approver = APPROVER_PLANTS[plant]
        h = fx.hashes[cid]
        fx.set_moved_clause(cid)
        path, text = fx.render_record(u1, f"`{cid}@{h}` [chain]", approver, risk="stricter", cause="review finding",
                                      hand="design-revised", follow=f"amends {cid}@{h}")
        fx.write_commit({V2: fx.v2, path: text}, f"records(dTrueNorth): {cid} amended, approver {approver}")
    elif plant == "owner-row1-added":
        fx.add_run_row(f"rescope · item add {u} · reason the spec audit promoted it")
        path, text = fx.render_record(u, "dTrueNorth [chain]", "owner, FIX-dClosedLoop-2", hand="design-to-spec",
                                      follow=f"new unit {u}")
        fx.write_commit({path: text}, f"records(dTrueNorth): {u}, added by the spec run, cites row 1")
    elif plant == "subject-pass":
        fx.write_spec(u, 1)
        fx.write_pass(u, trailer=False)
        fx.write_spec(u, 2, line="the fixture line, revised after the pass")
    elif plant == "pass-none":
        fx.write_spec(u, 1)
        fx.write_commit({"tools/fix-11.txt": "built\n"}, f"build {u}, attributed to no pass", ["Pass: none"])
        fx.write_spec(u, 2, line="the fixture line, revised")
    elif plant == "status-flip":
        fx.write_spec(u, 1)
        fx.write_commit({fx.derive_spec_path(u): fx.render_spec(u, 1, status="INPROGRESS")}, f"{u} goes INPROGRESS")
        fx.write_spec(u, 2, status="INPROGRESS", line="the fixture line, revised")
    elif plant == "two-branch":
        fx.write_spec(u, 1)
        fx.run("checkout", "-q", "-b", "node-b")
        fx.write_pass(u)
        fx.run("checkout", "-q", "run")
        fx.write_spec(u, 2, line="the fixture line, revised on node a while node b's pass was in flight")
        fx.run_merge("node-b", f"merge: node b's pass of {u}")
    elif plant == "header-rev":
        fx.write_spec(u, 1)
        fx.write_pass(u)
        fx.write_commit({fx.derive_spec_path(u): fx.render_spec(u, 1, status="INPROGRESS")},
                        f"spec(dTrueNorth): {u} INPROGRESS", ["Pass: none"])
        fx.write_spec(u, 2, status="INPROGRESS", line="the fixture line, revised")
        path, text = fx.render_record(u, f"{u}@rev-1 [acceptance]", "spec writer")
        fx.write_commit({path: text}, f"records(dTrueNorth): {u}'s deviation at its header rev-1")
    elif plant in ("gen", "status-gen", "gen-text"):
        fx.write_spec(u, 1)
        fx.write_pass(u)
        fx.write_commit({fx.derive_spec_path(u): fx.render_spec(
            u, 2 if plant == "gen-text" else 1, status="INPROGRESS" if plant == "status-gen" else "OPEN",
            records="| 2026-10-21-review-fixture | spec-audit |",
            line="the fixture line, changed with the render" if plant == "gen-text" else "the fixture line holds")},
            f"records(dTrueNorth): {u}'s spec-records region re-rendered", ["Pass: none"])
    elif plant == "quote":
        quoted = next(t for _b, c, t, _h in read_chain_clauses(fx.v2) if c == "cl-dClosedLoop-0004")
        fx.write_spec(u, 1, extra=f"- AC2: quotes its clause, {quoted}")
    elif plant in ("amended", "amended-joined"):
        files = {f"{TN}build/2026-10-21-build-{u}-1-acceptance-ledger.md": fx.render_ledger(u, 3)}
        if plant == "amended-joined":
            path, text = fx.render_record(u, f"{u}@rev-2 [acceptance]", "spec writer")
            files[path] = text
        fx.write_commit(files, f"records(dTrueNorth): {u}'s ledger")
    elif plant == "add":
        fx.add_run_row(f"rescope · item add {u} · reason a discovery adopted")
    elif plant in ("handback", "fix-record"):
        fx.write_spec(u, 1)
        fx.write_commit({f"{TN}prompts/2026-10-21-prompt-{u}-1-revision.md": fx.render_prompt(u, plant == "handback")},
                        f"records(dTrueNorth): {u}'s revision record", ["Pass: none"])
    elif plant in ("audit-pin", "audit-nopin"):
        fx.write_spec(u, 1)
        fx.write_commit({f"{TN}reviews/2026-10-21-review-{u}.md": fx.render_audit(u, 1 if plant == "audit-pin" else None)},
                        f"review(dTrueNorth): {u}'s spec audit", ["Pass: none"])
        fx.write_spec(u, 2, line="the fixture line, revised after its audit")
    elif plant == "defer":
        fx.write_spec(u, 1)
        fx.add_run_row(f"rescope · item defer {u} · reason specced; built by this build's build run")
    elif plant.startswith("trailer-"):
        value = {"trailer-relaxes-only": "kept the narrower flag set — fewer flags · ER:240 · relaxes: none",
                 "trailer-widens-only": "took the extra subcommand — the only option meeting AC3 · ER:388 · widens: "
                                        "the CLI's subcommand list",
                 "trailer-388-none": "took the external index — it fails veto 2 outside the grant · ER:388 · widens: "
                                     "none · relaxes: none",
                 "trailer-240-none": "kept the plain renderer — it fails only the goal bound · ER:240 · widens: none · "
                                     "relaxes: none",
                 "trailer-rung6": "dropped the 50-line cap — no option was left · ER:328 · widens: none · relaxes: the "
                                  "50-line cap"}[plant]
        files = {}
        if plant == "trailer-rung6":
            path, text = fx.render_record(u1, f"{u1}@rev-2 [non-goals]", "author, citing ER:328",
                                          bound="the 50-line cap", tier="weakest", reason="a writer's own bound")
            files[path] = text
        fx.write_commit(files, f"build {u1}: {plant}", [f"Decided: {value}"])
    elif plant in ("outside-packet", "range"):
        fx.write_commit({"memory/builds/dGroundRules/prompts/2026-10-21-prompt-FIX-dGroundRules-1-packet.md": "x\n"},
                        "records(dTrueNorth): another build's packet written by this run")
    elif plant == "outside-product":
        fx.write_commit({"tools/fix-unrecorded.txt": "built\n"}, f"build {u1}: a file no --writes set names",
                        [f"Pass: {u1}"])
    elif plant == "record-late":
        fx.add_run_row(f"rescope · item add {u} · reason a discovery adopted, its record written late")


def build_fixture(root, plants):
    """The fixture repository at `root`: the pin, a baseline commit opening dTrueNorth, the run's branch with the base
    and each plant, and the prepared merge onto origin/main."""
    fx = Fixture(root)
    run_git(".", "init", "-q", "-b", "main", root)
    for k, v in (("core.hooksPath", ".git/no-hooks"), ("commit.gpgsign", "false"), ("core.autocrlf", "false")):
        fx.run("config", k, v)
    chain = Path(V2).read_text(encoding="utf-8").split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    v2 = "# v2, the fixture's copy of its [chain]\n\n## [chain]" + chain + "\n## [clause-ids] Clause ids\n\nNo baseline.\n"
    files = {".memory-tree.conf": f'MEMORY_ROOT="memory"\nFAMILIES="fixture:{FIXTURE_FAMILY}"\n', V2: v2,
             "memory/DECISIONS.md": DECISIONS_TEXT}
    files.update({i: Path(i).read_bytes() for i in INSTRUMENTS if Path(i).is_file()})
    fx.pin = fx.write_commit(files, "fixture: v2's [chain], the fixture family and the decisions")
    fx.hashes = {cid: h for _b, cid, _t, h in read_chain_clauses(v2)}
    fx.v2 = v2.replace("No baseline.", f"Baseline: `{fx.pin}`, the fixture's own.")
    roster = ["FIX-dTrueNorth-80", "FIX-dTrueNorth-81"]
    c2 = {V2: fx.v2, TN + "README.md": render_fixture_readme(roster), SWITCH_BACKLOG: render_switch_backlog(None)}
    if "kind-spec" in plants or "kind-build" in plants or "switch-spec" in plants:
        c2[TN + "BACKLOG.md"] = render_fixture_backlog("FIX-dTrueNorth-90")
        for u in roster[:1] if "kind-spec" in plants or "switch-spec" in plants else roster:
            c2[fx.derive_spec_path(u)] = fx.render_spec(u, 1)
    fx.base = fx.write_commit(c2, "fixture: the baseline taken, and dTrueNorth opened")
    fx.run("update-ref", "refs/remotes/origin/main", fx.base)
    fx.run("checkout", "-q", "-b", "run")
    add_base(fx, plants)
    if not {"switch-missing", "switch-spec"} & set(plants):
        ask = {"switch-foreign": "FIX-dSafePassage-91", "switch-late": "FIX-dClosedLoop-91"}.get(
            next((p for p in plants if p in ("switch-foreign", "switch-late")), None), "FIX-dTrueNorth-91")
        fx.write_commit({SWITCH_BACKLOG: render_switch_backlog(ask)},
                        "records(dTrueNorth): the report-switch ask filed in dClosedLoop's BACKLOG.md")
    for p in plants:
        add_plant(fx, p)
    if "range" in plants:
        fx.run("checkout", "-q", "main")
        tip = fx.write_commit({"memory/builds/dSafePassage/build/2026-10-21-build-FIX-dSafePassage-1-note.md": "x\n"},
                              "records(dSafePassage): another build lands in its own folder",
                              ["Decided: their own choice — another build's fork · ER:240 · widens: none · relaxes: none"])
        fx.run("update-ref", "refs/remotes/origin/main", tip)
        fx.run("checkout", "-q", "run")
    if "kind-norun" in plants:
        fx.write_commit({TN + "RUN.md": None}, "unattended(dTrueNorth): no live run")
    fx.run("checkout", "-q", "-b", "prep", fx.run("rev-parse", "refs/remotes/origin/main").strip())
    fx.run_merge("run", "merge: dTrueNorth prepared onto origin/main")
    return fx


def derive_stub_entries(entries, plant):
    """A renderer stub (P0.2's red tests): one marked choice put after a member, or one trailer's entry dropped."""
    if plant in ("stub-widens", "stub-relaxes", "stub-grants"):
        key = plant.split("-")[1]
        moved = [e for e in entries if e[0] == "choice" and f"{key} [none]" not in e[1]]
        rest = [e for e in entries if e not in moved]
        at = next((i for i, e in enumerate(rest) if e[0] == "member"), len(rest)) + 1
        return rest[:at] + moved + rest[at:]
    if plant == "stub-drop":
        drop = next((e for e in entries if e[0] == "fork" and "Decided: " in e[1]), None)
        return [e for e in entries if e is not drop]
    if plant == "omit-grant":
        return [e for e in entries if not (e[0] == "choice" and "grants [none]" not in e[1])]
    return entries


def run_report_fixture(slug, plant, control):
    plants = [plant] if plant else list(PLANTS)
    with tempfile.TemporaryDirectory(prefix="deviations-fixture-", ignore_cleanup_errors=True) as root:
        fx = build_fixture(root, plants)
        label = " · fixture" + (f" · plant {plant}" if plant else "") + (f" · control {control}" if control else "")
        try:
            src = read_report_sources(root, slug, fx.pin, control)
        except Unmeasured as exc:
            print(f"deviations: report {slug}{label} · nothing measured: {exc}")
            return 2
        text = render_report(src, derive_stub_entries(derive_entries(src), plant))
        arm = [] if control == "no-arm" else check_report(text, src)
        path = derive_report_path(src, "2026-10-21")
        write_report(path, text)
        fx.write_commit({}, f"records({slug}): the departures report")
        if plant == "record-late":
            late = PLANT_UNITS["record-late"]
            rec_path, rec = fx.render_record(late, "dTrueNorth [chain]", "author", hand="design-to-spec",
                                             follow=f"new unit {late}")
            fx.write_commit({rec_path: rec}, f"records(dTrueNorth): {late}'s record, after the report")
        elif plant == "hand-edit":
            Path(path).write_bytes(Path(path).read_bytes().replace(b"## Entries", b"## Entries, reviewed", 1))
        elif plant == "instrument-byte":
            fx.write_commit({INSTRUMENTS[0]: Path(INSTRUMENTS[0]).read_bytes() + b"\n"},
                            "records(dClosedLoop): carries.py changed by one byte")
        src2 = read_report_sources(root, slug, fx.pin, control)
        text2 = render_report(src2, derive_stub_entries(derive_entries(src2), plant))
        byte = check_bytes(path, text2)
        arm2 = [] if control == "no-arm" else check_report(text2, src2)
        sys.stdout.write(text)
        print(f"deviations: report {slug} · {src['kind']} run · {Path(path).name} · entries {len(ENTRY.findall(text))}"
              f" · byte compare {'red' if byte else 'green'} · validating arm "
              f"{'removed' if control == 'no-arm' else 'red' if arm or arm2 else 'green'}{label}")
        for f in ([byte] if byte else []) + list(dict.fromkeys(arm + arm2)):
            print(f"  {f}")
        return 1 if byte or arm or arm2 else 0


def run_fixture(plant, policy):
    with tempfile.TemporaryDirectory(prefix="deviations-fixture-", ignore_cleanup_errors=True) as root:
        fx = build_fixture(root, [plant] if plant else list(PLANTS))
        return print_population(root, fx.pin, policy, " · fixture" + (f" · plant {plant}" if plant else ""))


def main(argv):
    ap = argparse.ArgumentParser(prog="deviations.py", add_help=True)
    ap.add_argument("--policy", choices=POLICIES, default="report")
    ap.add_argument("--fixture", action="store_true")
    ap.add_argument("--plant")
    ap.add_argument("--report", metavar="SLUG")
    ap.add_argument("--control", choices=CONTROLS)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.plant and a.plant not in (REPORT_PLANTS if a.report else PLANTS):
        sys.exit(f"deviations: no plant {a.plant}" + ("" if a.report else " outside --report"))
    if (a.plant or a.control) and not a.fixture:
        sys.exit("deviations: --plant and --control take --fixture")
    try:
        if a.report:
            if a.report not in read_chain_builds(Path(V2).read_text(encoding="utf-8")):
                sys.exit(f"deviations: {a.report} is no chain build")
            if a.fixture:
                return run_report_fixture(a.report, a.plant, a.control)
            return cmd_report(a.report, "write" if a.write else "check" if a.check else None)
        if a.fixture:
            return run_fixture(a.plant, a.policy)
        return print_population(".", BASELINE, a.policy, "")
    except Unmeasured as exc:
        print(f"deviations: nothing measured: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
