# **Serves:** research PLAY-dClosedLoop-1
"""The opening script: every file that opens the 22 chain builds of v2's `[chain]`, written in one commit from its
named source (the execution plan's P0.5, with P0.6's minting rules 1 and 2, P0.7's checks and P0.8 row 9's carrier
list). The plan is `build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` under `memory/builds/dClosedLoop/`.

What `--write` writes, per chain build:
  memory/builds/<slug>/README.md   the authored half only: front matter (`slug`, `node`, `opened`, `streams`,
      `roster`, `ids:` left for the generator, `status: OPEN`, `spec-audit`, `parents`, `may`), the H1 and stage,
      the five slots of the generator's heading canon, the build-level rules 1 to 8 (rule 8 only in a
      driver-changing build), and the authored `roster:units` pair. `gen_build_index.py --write` fills `ids:` and
      the generated regions afterwards.
  memory/builds/<slug>/BACKLOG.md  the one carry-forward ask and its SEV row, for every build but a whole-run one.
  memory/builds/<slug>/prompts/<date>-prompt-PLAY-dClosedLoop-1-packet.md   through the packet instrument's
      `render_packet`, imported by path, so the name claims the id the packet's Serves line lists.
and once: the 22 bound rows of `memory/project/readme-contract.txt`, through the generator's `add_contract_row`; and
dClosedLoop's own `BACKLOG.md` with one clean-reading ask, and its SEV row, per driver-changing build, written whole
when the file is absent; when it is present, each row it lacks is added after the opening's last row of its kind, and
a lacked row before a held one is refused, since the opening adds the ids it mints and never re-files one. It stages
every file it writes, because the index generator reads `git ls-files` and a packet reads the open asks through it.

Ids, fixed for Phase 0 (dispatch 239's brief, item 3), every one built from its parts here, so this file cites none:
  a chain build's roster ids are `<FAMILY>-<slug>-1` to `-<n>`, in clause order, then its extra units;
  its carry-forward ask is the next id after its roster;
  P0.8's rows 1 to 9 are dClosedLoop's ids counted on from row 1's, which the packet instrument declares once as
  `EXTRA_DECISION` (`missing:PLAY-dClosedLoop-2` until the main loop lands it, so ids 2 to 10); the grant is row 2,
  which every `may:` line cites, and the extra unit derives from row 1;
  dClosedLoop's clean-reading asks follow row 9's id, one per driver-changing build: first each build the walk's
  predicate counts, then each only answer 3's arms count, each set in v2's `[chain]` order, so no id the opening
  minted is renumbered (the charter's `[ids]`).

The family rule (walk answer 1, ER:435-436): the build's Stage and its slug's noun, its last capitalised word, matched
in that order and whole words only against `charter` or `playbook` (PLAY), `session` or `kickoff` (KICK) and
`deploy` (DEPL); a build matching none is TOOL. `roster:` is the family, `streams:` its discipline in `FAMILIES`.
The driver-changing rule (walk answer 5, ER:476): a v2 clause names a path or surface of the unattended kit, one of
KIT_TERMS below; a build with an extra unit joins by it, since the plan's only one edits the kit ([phase-1]). The
owner's opening-read answer 3 (ER:638-646) adds two arms, whole words: a clause that re-points a key the kit reads, a
`KEY=` line of its example conf `KIT_CONF` beside a form of "re-point", never one that merely names a key; and a
clause naming the unattended Skill, whose text it edits.
The carrier list (P0.8 row 9): six selectors over the tracked tree, each reduced to entries, a kit directory, a
skill directory or a file, so a new file inside an entry stays covered and a new entry does not.

Usage (from the worktree root):
  python open.py --write [--date YYYY-MM-DD]   write and stage every file of the opening (the date defaults to today)
  python open.py --check     red on any byte of an opened file the derivation does not render (a README's authored
                             half, a chain build's BACKLOG.md, a packet), a missing contract row or clean-reading ask
                             row, a roster that does not carry every clause of its row in exactly one row, and a
                             summary row that disagrees with the files it summarises
  python open.py --summary   P0.5's per-build summary, read from the files the opening wrote, or would write
  python open.py --families  the five-column family table
  python open.py --driver-builds   the driver-changing predicate, its clauses, and its near misses
  python open.py --carriers [--check]   P0.8 row 9's list over the tree at HEAD; with --check, red on a tracked path
                             at HEAD under a selector the list at the opening commit omits, and on a list entry
                             nothing tracked at HEAD sits under
Exit 0 green, 1 on a finding or a refusal, 2 when there is nothing to check.

What it does not check: the generated regions and `ids:` (`gen_build_index.py --check`), the slot contract and its
budgets (`--check-format`), a packet's own arms (`packet.py --check`), whether a rule's or a slot's words say what the
plan means, the contract file's and dClosedLoop's `BACKLOG.md`'s other rows, which later builds write, and whether a
clause's re-point has the kit key it names for its object, since the arm reads the two in one clause.
"""
import argparse
import contextlib
import datetime
import functools
import importlib.util
import io
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

B = "memory/builds/dClosedLoop/build/"
OWN = "dClosedLoop"
PACKET = B + "2026-10-20-build-PLAY-dClosedLoop-1-packet.py"
OWED_BACKLOG = f"memory/builds/{OWN}/BACKLOG.md"
DECISION_ROWS = 9         # P0.8's nine rows; dClosedLoop's clean-reading asks take the ids after them
GRANT_ROW, EXTRA_ROW = 2, 1
WAIVER_DATE = "2026-10-20"  # the owner's walk answer 5 (ER:476), which README rule 8 quotes
FAMILY_WORDS = (("PLAY", ("charter", "playbook")), ("KICK", ("session", "kickoff")), ("DEPL", ("deploy",)))
KIT_TERMS = (("`unattended.sh`", r"(?<![-\w])unattended\.sh\b"), ("`check-unattended.sh`", r"\bcheck-unattended\.sh\b"),
             ("`tools/unattended/`", r"\btools/unattended/"), ("the `/unattended` command", r"`/unattended`"),
             ("the unattended kit", r"\bunattended kit\b"), ("`--plan`", r"`--plan`"), ("`--status`", r"`--status`"),
             ("unattended's verbs", r"\bunattended's verbs\b"), ("run claims", r"\brun claims?\b"))
KIT_CONF = "tools/unattended/.unattended.conf.example"   # its `KEY=` lines: the keys the kit's driver reads (its header)
REPOINT = r"\bre-point(?:s|ed|ing)?\b"
SKILL_TERM = ("the unattended Skill", r"(?i:\bunattended skill\b)")
EXTRA_TEXT = ("the carry-forward condition for every unit a spec run adds, once, and the starting-roster reading it "
              "rests on")   # the execution plan's `[deviations]` row for the extra unit
EXTRA_KIT = "its extra unit, the carry-forward condition in `unattended.sh` (the execution plan's `[phase-1]`)"
CHARTER_FILES = ("coding-governance-agents.template.md", "AGENTS.md", "CLAUDE.md")
WIDTH = 118


class Refusal(Exception):
    """A refusal: exit 1, nothing written."""


class Unmeasured(Exception):
    """Nothing to check: exit 2."""


def load_instrument(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


packet = load_instrument("packet", PACKET)      # with it the carries join, the schedule script and the generator
genindex = packet.genindex


def run_git(*args):
    try:
        return packet.run_git(*args)
    except packet.Refusal as e:
        raise Refusal(str(e))


@functools.lru_cache(maxsize=None)
def read_conf():
    return genindex.load_conf(".")


def derive_decision_id(row):
    """dClosedLoop's id for P0.8's row `row`, or for a clean-reading ask after the nine rows, counted on from row 1's
    id, which the packet instrument declares once as `EXTRA_DECISION`, so the two instruments cannot disagree."""
    m = re.fullmatch(r"missing:([A-Z]+)-" + OWN + r"-(\d+)", packet.EXTRA_DECISION)
    if not m:
        raise Refusal(f"packet.py's EXTRA_DECISION `{packet.EXTRA_DECISION}` is no `missing:` id of {OWN}")
    return f"{m.group(1)}-{OWN}-{int(m.group(2)) + row - EXTRA_ROW}"


def derive_family(stage, slug):
    """(slug noun, word matched or 'none', family) by the owner's rule."""
    noun = re.findall(r"[A-Z][a-z0-9]*", slug)[-1]
    for fam, words in FAMILY_WORDS:
        for cell in (stage, noun):
            m = re.search(r"\b(" + "|".join(words) + r")\b", cell, re.I)
            if m:
                return noun, m.group(1), fam
    return noun, "none", "TOOL"


@functools.lru_cache(maxsize=None)
def read_kit_keys():
    """The keys the unattended kit reads: each `KEY=` line of its example conf, which its driver reads and never
    restates (the conf's header), so no key is typed here."""
    keys = tuple(dict.fromkeys(re.findall(r"^([A-Z][A-Z0-9_]*)=", read_file(KIT_CONF) or "", re.M)))
    if not keys:
        raise Refusal(f"{KIT_CONF} holds no `KEY=` line, so the keys the kit reads cannot be derived")
    return keys


def extract_kit_keys(text):
    """The keys the kit reads that a clause names, whole words."""
    return [k for k in read_kit_keys() if re.search(r"\b" + k + r"\b", text)]


def derive_kit_clauses(clauses):
    """[(clause id, [term labels], walk)] of the clauses that touch the kit: naming a path or surface of it (walk
    answer 5; `walk` true), or by answer 3's arms, naming a key it reads beside a re-point, or naming its Skill."""
    out = []
    for cid, (text, _h, _t) in clauses.items():
        walk = [label for label, rx in KIT_TERMS if re.search(rx, text)]
        more = [f"`{k}` re-pointed" for k in extract_kit_keys(text)] if re.search(REPOINT, text) else []
        more += [SKILL_TERM[0]] if re.search(SKILL_TERM[1], text) else []
        if walk or more:
            out.append((cid, walk + more, bool(walk)))
    return out


def extract_cut(text):
    """The clause's text to its first comma, the roster's Clause cell."""
    cut = text.split(",", 1)[0].strip()
    if "|" in cut or cut.count("`") % 2:
        raise Refusal(f"a clause's text to its first comma holds a pipe or an unclosed code span, either of which "
                      f"would break its roster row: {cut[:80]}")
    return cut


@functools.lru_cache(maxsize=None)
def derive_chain():
    """Every chain build's derived facts, in v2's `[chain]` order."""
    t = packet.read_tree()
    rows, builds = t["rows"], t["builds"]
    disciplines = genindex.read_discipline_map(read_conf())
    extra = packet.schedule.EXTRA
    out = []
    for slug, row in rows.items():
        noun, word, fam = derive_family(row["stage"], slug)
        if fam not in disciplines:
            raise Refusal(f"{slug}'s family {fam} is no family `.memory-tree.conf` declares")
        if extra.get(slug, 0) not in (0, 1):
            raise Refusal(f"{slug} has {extra[slug]} extra units, and the plan's extra unit text names one")
        clauses = [(cid, h, extract_cut(text)) for cid, (text, h, _tok) in builds[slug].items()]
        n = len(clauses) + extra.get(slug, 0)
        kit = derive_kit_clauses(builds[slug])
        keys, bad = packet.extract_gaps(row["gaps"])
        if bad:
            raise Refusal(f"{slug}'s Gaps cell holds parts no rule reads: {', '.join(bad)}")
        out.append({"slug": slug, "stage": row["stage"], "parents": row["parents"], "noun": noun, "word": word,
                    "family": fam, "streams": disciplines[fam], "clauses": clauses, "extra": extra.get(slug, 0),
                    "units": [f"{fam}-{slug}-{i}" for i in range(1, n + 1)],
                    "whole": slug in packet.schedule.WHOLE,
                    "ask": None if slug in packet.schedule.WHOLE else f"{fam}-{slug}-{n + 1}",
                    "kit": kit, "driver": bool(kit) or bool(extra.get(slug)), "gaps": row["gaps"], "n_gaps": len(keys),
                    "walk": any(w for _c, _t, w in kit) or bool(extra.get(slug)),
                    "children": [c for c, r in rows.items() if slug in r["parents"]], "baseline": t["baseline"]})
    row = DECISION_ROWS
    for b in out:
        b["clean"], b["clean_row"] = None, None
    for walk in (True, False):          # the walk's predicate's builds first, so answer 3's ids follow theirs
        for b in out:
            if b["driver"] and b["walk"] is walk:
                row += 1
                b["clean"], b["clean_row"] = derive_decision_id(row), row
    return out


def wrap(text, first="", rest="", width=WIDTH):
    """Lines of at most `width` characters, never breaking inside a backticked span."""
    lines, cur, fresh = [], first, True
    for tok in re.findall(r"(?:`[^`]*`|[^\s`])+", text):
        if not fresh and len(cur) + 1 + len(tok) > width:
            lines.append(cur)
            cur = rest + tok
        else:
            cur += tok if fresh else " " + tok
        fresh = False
    lines.append(cur)
    return lines


def render_rules(b):
    """The build-level rules 1 to 8 of P0.5, rule 8 only in a driver-changing build."""
    s = b["slug"]
    if b["whole"]:
        phase = ("Phase: one whole run specs, audits, builds and lands every unit"
                 + (", the extra unit last" if b["extra"] else "") + ", and closes without carry-forward.")
        report = "`…-departures-build.md`"
    else:
        phase = ("Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting "
                 "roster has a unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a "
                 "departure, and closes by carry-forward. Any other run is the build run: it builds every carried "
                 "unit, deferring none again.")
        report = "`…-departures-spec.md` or `-build.md`"
    rules = [phase,
             f"Read in the packet's order, `packet.py --check {s}` green before the first pass; a moved instrument "
             "blob is a stop, never re-rendered away.",
             "Push the run branch after every pass commit, hold and hand-off.",
             "Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`: "
             f"`deviations.py --report {s}`, a record per member \"recorded by nobody\", the same with `--write` "
             f"(commit it as {report}) and `--check`, then `--authorization` and `--close`; again after a re-prepare.",
             "Deviation values: `report` and `author-recorded`.",
             "Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling "
             "(ER:240, ER:388, ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a "
             "`relaxes:` value joins a record with `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one "
             "with `**Surface:**`, `**Reason:**`; a grant-lifted choice carries `grants: <id> <change>`.",
             "Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask "
             "row in another build's `BACKLOG.md` and the shared renders. The departures report lists the rest."]
    if b["driver"]:
        rules.append(f"The unattended kit's own self-test suites are WAIVED for this build's landing (owner, "
                     f"{WAIVER_DATE}, walk answer 5). A criterion they would observe is amended citing this rule; "
                     f"their clean reading is owed with {b['clean']}.")
    return [ln for r in rules for ln in wrap(r, "- ", "  ")]


def render_readme(b, date):
    s, h = b["slug"], [x[0] for x in genindex.SLOT_CANON]
    grant, extra = derive_decision_id(GRANT_ROW), derive_decision_id(EXTRA_ROW)
    may = grant + (f" {extra}" if b["extra"] else "")
    head = ["---", f"slug: {s}", f"node: {s[0]}", f"opened: {date}", f"streams: {b['streams']}",
            f"roster: {b['family']}", "ids:", "status: OPEN", f"spec-audit: {date}",
            f"parents: {' '.join(b['parents'])}", f"may: {may}", "---", "",
            f"# {s} — the {b['stage']} build of the {OWN} chain", ""]
    k, n = len(b["clauses"]), b["n_gaps"]
    problem = wrap(f"{s} owns {n} gaps at the baseline `{b['baseline'][:9]}`, as its row of v2's `[chain]` names them: "
                   f"{b['gaps']}. Closing every one is this build's goal bound.")
    better = [f"Each of the {k} clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster "
              "unit per clause.", f"Each unit built and landed, so the {n} owned gaps above close."]
    if b["extra"]:
        better.append(f"Its extra unit built: {EXTRA_TEXT}, which every later chain spec run closes with.")
    kids = b["children"]
    worse = [f"Its {n} owned gaps stay open.",
             f"Its {len(kids)} child build{'s' if len(kids) != 1 else ''} wait{'' if len(kids) != 1 else 's'} on it: "
             f"{', '.join(kids)}." if kids else
             "No chain build names it as a parent, and the chain is done only when it lands."]
    body = ([h[0], ""] + problem + ["", h[1], ""] + [ln for x in better for ln in wrap(x, "- ", "  ")]
            + ["", h[2], ""] + [ln for x in worse for ln in wrap(x, "- ", "  ")]
            + ["", h[3], ""] + render_rules(b) + ["", h[4], "", "none", "", genindex.PLAN_OPEN, "",
                                                 "| # | Unit | Carries | Clause |", "|---|---|---|---|"])
    for i, (cid, hh, cut) in enumerate(b["clauses"], 1):
        body.append(f"| {i} | `{b['units'][i - 1]}` | `{cid}@{hh}` | {cut} |")
    if b["extra"]:
        i = len(b["clauses"]) + 1
        body.append(f"| {i} | `{b['units'][i - 1]}` | **Derived:** {extra} | {EXTRA_TEXT} |")
    body.append(genindex.PLAN_CLOSE)
    return "\n".join(head + body) + "\n"


def render_backlog(b, date):
    a = b["ask"]
    return "\n".join([f"# {b['slug']} — asks", "", "## Asks", "",
                      f"- {a} · filed {date} · build every roster unit of this build from its spec, filed by the "
                      "opening so the spec run closes by carry-forward with each unit's spec header advancing this "
                      "ask (README rule 1) · accept every unit of the README's `roster:units` pair is built from its "
                      "spec and CLOSED, the last one's header carrying `closes` for this ask",
                      "", "## Dispositions", "",
                      f"- SEV · {a} · MED · the build's units stay unbuilt and its owned gaps open", ""])


def render_owed_rows(chain, date):
    """dClosedLoop's clean-reading asks and their SEV rows, in id order: ([ask rows], [SEV rows])."""
    asks, sevs = [], []
    for b in sorted((b for b in chain if b["clean"]), key=lambda b: b["clean_row"]):
        s, c = b["slug"], b["clean"]
        asks.append(f"- {c} · filed {date} · THE UNATTENDED KIT'S OWN SELF-TEST SUITES GO UNREAD AT {s}'S LANDING. "
                    f"{s}'s README rule 8 waives the on-demand verdict of "
                    "`tools/unattended/run-unattended-gates.sh --selftests` for that landing (owner, "
                    f"{WAIVER_DATE}, walk answer 5), and the flagged bar its close still runs reads no unattended "
                    f"suite. · accept an owner run of the unattended suites at or after {s}'s landing reads them, "
                    "and every red it shows is triaged, each new one filed as its own ask")
        sevs.append(f"- SEV · {c} · MED · {s}'s driver change lands with the unattended kit's own suites unread")
    return asks, sevs


def render_owed_backlog(chain, date):
    asks, sevs = render_owed_rows(chain, date)
    return "\n".join([f"# {OWN} — asks", "", "## Asks", ""] + asks + ["", "## Dispositions", ""] + sevs) + "\n"


def add_owed_rows(text, chain, date):
    """dClosedLoop's `BACKLOG.md` with each opening row it lacks added after the opening's last row of its kind, every
    other line kept. Refused when it holds no opening row of a kind, or lacks one before a row it holds: the opening
    adds the ids it mints after those it minted, and never re-files one."""
    lines = text.split("\n")
    for kind, rows in zip(("ask", "SEV"), render_owed_rows(chain, date)):
        held = [i for i, r in enumerate(rows) if r in lines]
        lacked = [r for r in rows if r not in lines]
        if not held or (lacked and rows.index(lacked[0]) < held[-1]):
            raise Refusal(f"{OWED_BACKLOG} exists without the opening's {kind} rows in order "
                          f"({len(held)} of {len(rows)} held), and the opening only adds the rows after its last")
        at = lines.index(rows[held[-1]]) + 1
        lines[at:at] = lacked
    return "\n".join(lines)


def derive_opening(date):
    """{path: text} of every file the opening writes but the packets, and the 22 contract rows."""
    chain = derive_chain()
    files = {}
    for b in chain:
        files[f"memory/builds/{b['slug']}/README.md"] = render_readme(b, date)
        if b["ask"]:
            files[f"memory/builds/{b['slug']}/BACKLOG.md"] = render_backlog(b, date)
    files[OWED_BACKLOG] = render_owed_backlog(chain, date)
    return chain, files, [f"memory/builds/{b['slug']}/README.md" for b in chain]


def read_file(path):
    return Path(path).read_bytes().decode("utf-8") if Path(path).is_file() else None


def write_file(path, text):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def add_paths(paths):
    run_git("add", "--", *paths)


def cmd_write(date):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise Refusal(f"--date {date} is not YYYY-MM-DD")
    chain, files, contract = derive_opening(date)
    owed = read_file(OWED_BACKLOG)
    if owed is not None:
        files[OWED_BACKLOG] = add_owed_rows(owed, chain, date)
        if files[OWED_BACKLOG] == owed:
            del files[OWED_BACKLOG]
    for path, text in files.items():
        write_file(path, text)
    conf = read_conf()
    for rel in contract:
        genindex.add_contract_row(".", conf, rel)
    registry = f"{conf['MEMORY_ROOT']}/{genindex.CONTRACT_REGISTRY}"
    add_paths(list(files) + [registry])
    written = []
    for b in chain:
        path, text = packet.render_packet(b["slug"])
        if read_file(path) != text:
            packet.write_packet(path, text)
        written.append(path)
    add_paths(written)
    print(f"open: wrote and staged {len(files)} files, {len(contract)} contract rows in {registry} and "
          f"{len(written)} packets, opened {date}; run `gen_build_index.py --write` next")
    return 0


def read_front(text):
    """{key: value} of a README's front matter, which opens at line 1."""
    lines = text.split("\n")
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return {}
    pairs = (ln.split(":", 1) for ln in lines[1:lines.index("---", 1)] if ":" in ln)
    return {k.strip(): v.strip() for k, v in pairs}


def extract_authored(text):
    """A README's authored half: `ids:` emptied, and everything from the first generated marker cut."""
    lines = text.split("\n")
    marks = {mo for _n, mo, _mc in genindex.GEN_REGIONS}
    end = next((i for i, ln in enumerate(lines) if ln.rstrip("\r") in marks), len(lines))
    out, fm = [], 0
    for i, ln in enumerate(lines[:end]):
        fm += ln == "---"
        out.append("ids:" if fm == 1 and i and ln.startswith("ids:") else ln)
    return "\n".join(out).rstrip("\n") + "\n"


def read_opening_date(chain):
    text = read_file(f"memory/builds/{chain[0]['slug']}/README.md")
    if text is None:
        raise Unmeasured(f"memory/builds/{chain[0]['slug']}/README.md does not exist: nothing is opened to check")
    date = read_front(text).get("opened", "")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise Refusal(f"{chain[0]['slug']}'s README carries `opened: {date}`, no date to render the opening at")
    return date


def check_packet(slug):
    """(exit, line) of `packet.py --check <slug>`, run in this process."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            code = packet.cmd_check(slug)
        except packet.Refusal as e:
            print(f"packet: refused: {e}")
            code = 1
        except packet.Unmeasured as e:
            print(f"packet: {e}")
            code = 2
    return code, buf.getvalue().strip()


def derive_summary(b, readme, backlog, pkt, contract):
    """One summary row read from texts: the README, BACKLOG.md, the packet (size, check exit) and the contract row."""
    fm = read_front(readme or "")
    h1 = re.search(r"^# (\S+) — the (.+) build of the " + OWN + r" chain$", readme or "", re.M)
    units = packet.read_roster(readme or "", b["slug"])
    grammar = genindex.backlog.build_grammar({p.split(":")[1] for p in read_conf()["FAMILIES"].split()})
    asks = [r.target for r in (genindex.backlog.extract_row(ln, grammar) for ln in (backlog or "").split("\n"))
            if r is not None and r.cls == "ask"]
    rule8 = re.search(r"their clean reading is owed with (\S+)\.$", readme or "", re.M)
    return {"stage": h1.group(2) if h1 else "no H1", "parents": fm.get("parents", "absent"), "units": str(len(units)),
            "family": f"{fm.get('roster', 'absent')} · {fm.get('streams', 'absent')}",
            "ask": ", ".join(asks) if asks else "none: whole run" if backlog is None else "none",
            "packet": pkt, "may": f"may: {fm['may']}" if "may" in fm else "absent",
            "spec-audit": fm.get("spec-audit", "absent"),
            "rule 8": f"yes · {rule8.group(1)}" if rule8 else "no", "contract": contract}


def read_contract(path):
    bound, exempt, _pin = genindex.read_contract_rows(".", read_conf())
    return "present, bound" if path in bound else "present, exempt" if path in exempt else "absent"


COLUMNS = (("stage", "Stage"), ("parents", "`parents:`"), ("units", "Units"), ("family", "Family · `streams:`"),
           ("ask", "Carry-forward ask"), ("packet", "Packet"), ("may", "`may:` line"), ("spec-audit", "`spec-audit:`"),
           ("rule 8", "Rule 8 · clean-reading ask"), ("contract", "Contract row"))


def render_summary(rows):
    out = ["| Build | " + " | ".join(h for _k, h in COLUMNS) + " |", "|---" * (len(COLUMNS) + 1) + "|"]
    return out + [f"| {s} | " + " | ".join(r[k] for k, _h in COLUMNS) + " |" for s, r in rows]


def cmd_summary():
    chain = derive_chain()
    try:
        date = read_opening_date(chain)
        source = "the files the opening wrote"
    except Unmeasured:
        date, source = datetime.date.today().isoformat(), "the files the opening would write today (none is written)"
    _c, files, _contract = derive_opening(date)
    rows = []
    for b in chain:
        rp, bp = f"memory/builds/{b['slug']}/README.md", f"memory/builds/{b['slug']}/BACKLOG.md"
        found = packet.scan_packets(b["slug"])
        if len(found) == 1:
            code, _line = check_packet(b["slug"])
            pkt = f"{found[0].stat().st_size} B · `packet.py --check` exit {code}"
        else:
            pkt = f"{len(found)} packets" if found else "not written"
        on_disk = read_file(rp) is not None
        rows.append((b["slug"], derive_summary(b, read_file(rp) if on_disk else files[rp],
                                               read_file(bp) if on_disk else files.get(bp), pkt,
                                               read_contract(rp))))
    print(f"open: summary of the {len(chain)} chain builds, read from {source}, opened {date}")
    print("\n".join(render_summary(rows)))
    return 0


def check_roster(b, readme):
    """The arm that reads every clause of the build's row in exactly one roster row, at its hash."""
    want = {cid: h for cid, h, _cut in b["clauses"]}
    seen = {}
    for _u, n, row in packet.read_roster(readme, b["slug"]):
        for cid, h in re.findall(r"`(cl-d[A-Z]\w+-\d{4})@([0-9a-f]{8})`", row):
            seen.setdefault(cid, []).append((n, h))
    out = [f"roster arm: {b['slug']}: `{cid}` is in {len(seen.get(cid, []))} roster rows, not exactly one"
           for cid in want if len(seen.get(cid, [])) != 1]
    out += [f"roster arm: {b['slug']}: README:{n} carries `{cid}`, no clause of its row" for cid, xs in seen.items()
            if cid not in want for n, _h in xs]
    out += [f"roster arm: {b['slug']}: README:{n} pins `{cid}@{h}`, and the clause hashes {want[cid]}"
            for cid, xs in seen.items() if cid in want for n, h in xs if h != want[cid]]
    return out


def check_opening():
    chain = derive_chain()
    date = read_opening_date(chain)
    _c, files, contract = derive_opening(date)
    findings, compared = [], 0
    for path, text in files.items():
        disk = read_file(path)
        if path == OWED_BACKLOG:
            asks, sevs = render_owed_rows(chain, date)
            lines = (disk or "").split("\n")
            findings += [f"owed asks: {OWED_BACKLOG} lacks the opening's row: {r[:90]}" for r in asks + sevs
                         if r not in lines]
            continue
        compared += 1
        if disk is None:
            findings.append(f"byte compare: {path} does not exist")
            continue
        got = extract_authored(disk) if path.endswith("README.md") else disk
        if got != text:
            a, w = got.split("\n"), text.split("\n")
            n = next((i for i, (x, y) in enumerate(zip(a, w)) if x != y), min(len(a), len(w)))
            findings.append(f"byte compare: {path} differs from its render from line {n + 1}: "
                            f"{a[n][:90] if n < len(a) else 'EOF'}")
    for b in chain:
        bp = f"memory/builds/{b['slug']}/BACKLOG.md"
        if not b["ask"] and read_file(bp) is not None:
            findings.append(f"byte compare: {bp} exists, and the opening writes none for a whole-run build")
    rows, mismatch = [], 0
    for b, rp in zip(chain, contract):
        readme = read_file(rp)
        if readme is None:
            continue                     # the byte compare above already names it; no roster, so no packet renders
        findings += check_roster(b, readme)
        found = packet.scan_packets(b["slug"])
        path, text = packet.render_packet(b["slug"])
        compared += 1
        if len(found) != 1 or found[0].as_posix() != path:
            findings.append(f"byte compare: {b['slug']} holds {len(found)} packets, and the opening writes {path}")
            pkt = f"{len(found)} packets"
        else:
            if read_file(path) != text:
                findings.append(f"byte compare: {path} differs from its render")
            code, line = check_packet(b["slug"])
            if code:
                said = line.splitlines() or ["no output"]
                findings += [f"packet arm: {b['slug']}: {x.strip()}" for x in said[1:] or said]
            pkt = f"{found[0].stat().st_size} B · `packet.py --check` exit {code}"
        want = f"{len(text.encode('utf-8'))} B · `packet.py --check` exit 0"
        got = derive_summary(b, readme, read_file(f"memory/builds/{b['slug']}/BACKLOG.md"), pkt, read_contract(rp))
        exp = derive_summary(b, files[rp], files.get(f"memory/builds/{b['slug']}/BACKLOG.md"), want, "present, bound")
        for k, h in COLUMNS:
            if got[k] != exp[k]:
                mismatch += 1
                findings.append(f"summary arm: {b['slug']}: {h} reads `{got[k]}` in the files, and the derivation "
                                f"gives `{exp[k]}`")
        rows.append(b["slug"])
    print(f"open: check of the opening of {date} · {compared} files byte-compared · roster arm over "
          f"{sum(len(b['clauses']) for b in chain)} clauses · summary arm over {len(rows)} rows, {mismatch} "
          f"disagreements · findings {len(findings)}")
    for f in findings:
        print(f"  {f}")
    return 1 if findings else 0


def cmd_families():
    print("| Build | Stage | Slug noun | Word matched | Family |")
    print("|---|---|---|---|---|")
    for b in derive_chain():
        print(f"| {b['slug']} | {b['stage']} | {b['noun']} | {b['word']} | {b['family']} |")
    return 0


def cmd_driver_builds():
    chain = derive_chain()
    builds = packet.read_tree()["builds"]
    keys = read_kit_keys()
    print("The predicate (P0.5, walk answer 5): a v2 clause names " + ", ".join(lb for lb, _rx in KIT_TERMS)
          + "; \"the driver\" alone is left out, since in v2 it names the loop's driver role. A build with an extra "
          "unit joins by it. The opening read's answer 3 adds two arms, whole words: a clause that re-points a key "
          f"the kit reads, one of the {len(keys)} `KEY=` lines of `{KIT_CONF}` beside a form of \"re-point\", never "
          "one that only names a key; and a clause naming the unattended Skill, whose text it edits.")
    print("")
    print("| Build | Clauses that touch the kit |")
    print("|---|---|")
    for b in chain:
        if b["driver"]:
            cells = ([EXTRA_KIT] if b["extra"] else []) + [f"`{cid}` ({', '.join(t)})" for cid, t, _w in b["kit"]]
            print(f"| {b['slug']} | {'; '.join(cells)} |")
    print("")
    late = [b["slug"] for b in chain if b["driver"] and not b["walk"]]
    print(f"{sum(1 for b in chain if b['driver'])} builds, {sum(len(b['kit']) for b in chain)} clauses; "
          f"{len(late)} of the builds join by answer 3's arms alone ({', '.join(late) or 'none'}), so their "
          "clean-reading asks take the ids after the others'. Near misses, the clauses naming \"unattended\" that "
          "match no term, which the predicate leaves out:")
    print("")
    hits = {cid for b in chain for cid, _t, _w in b["kit"]}
    misses = 0
    for b in chain:
        for cid, (text, _h, _t) in builds[b["slug"]].items():
            m = re.search(r"\bunattended\b", text)
            if m and cid not in hits:
                misses += 1
                print(f"- `{cid}` ({b['slug']}): \"{packet.extract_excerpt(text, m.start(), m.end())}\"")
    driver = sum(1 for b in chain for cid, (text, _h, _t) in builds[b["slug"]].items()
                 if re.search(r"\bthe driver\b", text) and cid not in hits)
    print(("" if misses else "- none\n") + f"\nClauses naming \"the driver\" and no term, left out: {driver}")
    print("\nClauses naming a key the kit reads and no re-point, left out:\n")
    named = [f"- `{cid}` ({b['slug']}): " + ", ".join(f"`{k}`" for k in found)
             for b in chain for cid, (text, _h, _t) in builds[b["slug"]].items() if cid not in hits
             for found in [extract_kit_keys(text)] if found]
    print("\n".join(named) or "- none")
    return 0


def read_tree_paths(ref):
    return [p for p in run_git("ls-tree", "-r", "-z", "--name-only", ref).split("\0") if p]


def derive_entries(paths):
    """({entry: {"selectors": [numbers], "paths": [tracked paths under it]}}, the selectors) over P0.8 row 9's six."""
    conf = read_conf()
    routed = conf.get("ROUTED_PATHS", "").split()
    if not routed:
        raise Refusal("`.memory-tree.conf` declares no ROUTED_PATHS, so the first selector would select nothing")

    def route(p):
        for item in routed:
            if item.endswith("/") and p.startswith(item):
                rest = p[len(item):]
                return item + rest.split("/")[0] + ("/" if "/" in rest else "")
            if p == item:
                return item
        return None

    charter = {CHARTER_FILES[0], conf.get("CHARTER", CHARTER_FILES[1]), CHARTER_FILES[2]}
    selectors = (
        ("routed product paths", f"`.memory-tree.conf` `ROUTED_PATHS`: {' '.join(routed)}", route),
        ("git hooks", "every tracked file under `.githooks/`, which `core.hooksPath` wires",
         lambda p: p if p.startswith(".githooks/") else None),
        ("agent and role files", "every tracked path under `.claude/`, a skill as its directory",
         lambda p: ("/".join(p.split("/")[:3]) + ("/" if p.count("/") > 2 else ""))
         if p.startswith(".claude/") else None),
        ("the charter", "the template and its renders", lambda p: p if p in charter else None),
        ("the method's guides", "every tracked file under `memory/guides/`",
         lambda p: p if p.startswith("memory/guides/") else None),
        ("the root confs", "a root `.<name>.conf`, `.gitattributes`, and every tracked file under `.governance/`",
         lambda p: p if re.fullmatch(r"\.[\w.-]+\.conf|\.gitattributes|\.governance/.+", p) else None))
    out = {}
    for p in paths:
        for i, (_n, _b, sel) in enumerate(selectors, 1):
            e = sel(p)
            if e:
                v = out.setdefault(e, {"selectors": [], "paths": []})
                v["paths"] += [] if p in v["paths"] else [p]
                v["selectors"] += [] if i in v["selectors"] else [i]
    return out, selectors


def render_carriers(entries, selectors, paths, ref):
    out = [f"Governance carriers at {ref}, P0.8 row 9's six selectors: {len(entries)} entries over "
           f"{sum(len(v['paths']) for v in entries.values())} tracked paths."]
    kits = {p[:-len("kit.toml")] for p in paths if p.endswith("/kit.toml") and p.count("/") == 2}
    for i, (name, basis, _s) in enumerate(selectors, 1):
        mine = sorted(e for e, v in entries.items() if i in v["selectors"])
        dirs = [e for e in mine if e.endswith("/")]
        out += ["", f"{i}. {name} ({basis}): {len(mine)} entries, {sum(1 for e in dirs if e in kits)} kits with a "
                    f"`kit.toml`, {sum(1 for e in dirs if e not in kits)} other directories, "
                    f"{len(mine) - len(dirs)} files"]
        out += [f"   - `{e}`" + (" · kit" if e in kits else "") + (f" · {len(entries[e]['paths'])} tracked files"
                                                                       if e.endswith("/") else "") for e in mine]
    return out


def read_opening_commit(chain):
    rel = f"memory/builds/{chain[0]['slug']}/README.md"
    shas = run_git("log", "--diff-filter=A", "--format=%H", "HEAD", "--", rel).split()
    return shas[-1] if shas else None


def cmd_carriers(check):
    head = run_git("rev-parse", "HEAD").strip()
    paths = read_tree_paths(head)
    entries, selectors = derive_entries(paths)
    if not check:
        print("\n".join(render_carriers(entries, selectors, paths, f"HEAD `{head[:12]}`")))
        return 0
    opening = read_opening_commit(derive_chain())
    if not opening:
        raise Unmeasured("no commit in HEAD's history adds a chain build's README, so there is no list at the opening "
                         "commit to check against")
    listed, _s = derive_entries(read_tree_paths(opening))
    findings = [f"{e} ({selectors[v['selectors'][0] - 1][0]}; tracked {v['paths'][0]}) is under a selector, and the "
                f"list at the opening commit {opening[:12]} omits it" for e, v in sorted(entries.items())
                if e not in listed]
    findings += [f"{e} is on the list at the opening commit {opening[:12]}, and nothing tracked at HEAD sits under it"
                 for e in sorted(listed) if e not in entries]
    print(f"open: carriers at HEAD {head[:12]} against the list at the opening commit {opening[:12]} · "
          f"{len(entries)} entries now, {len(listed)} listed · findings {len(findings)}")
    for f in findings:
        print(f"  {f}")
    return 1 if findings else 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="open.py", description="Write and check the opening of the 22 chain builds.")
    modes = ("write", "summary", "families", "driver_builds", "carriers")
    for m in modes:
        ap.add_argument("--" + m.replace("_", "-"), action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--date")
    a = ap.parse_args(argv)
    chosen = [m for m in modes if getattr(a, m)]
    if len(chosen) > 1 or (not chosen and not a.check):
        ap.error("pass one of --write, --check, --summary, --families, --driver-builds or --carriers")
    if a.check and chosen and chosen != ["carriers"]:
        ap.error("--check goes alone, or with --carriers")
    if a.date and not a.write:
        ap.error("--date goes with --write")
    try:
        if a.write:
            return cmd_write(a.date or datetime.date.today().isoformat())
        if a.carriers:
            return cmd_carriers(a.check)
        if a.check:
            return check_opening()
        if a.summary:
            return cmd_summary()
        if a.families:
            return cmd_families()
        return cmd_driver_builds()
    except (Refusal, packet.Refusal) as e:
        print(f"open: refused: {e}")
        return 1
    except (Unmeasured, packet.Unmeasured) as e:
        print(f"open: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
