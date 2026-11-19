# **Serves:** research TOOL-dTrackedAtlas-1
r"""Every dClosedLoop chain build's actual state, read from the tree at one git ref: its spec run, its build run and
the merge that landed it, its units, forks, revisions, deviation records, claim, and whether its next run can start.
The ONE answer the schedule script (`tree_state`, `chain`, `claims`, `graph`) and the Atlas read
(TOOL-dTrackedAtlas-1).

Usage (from a worktree root; `unattended.sh --claims` fills the claim cache, this file only reads it):
  . tools/lib/resolve-python.sh && PY=$(resolve_python)
  "$PY" <this file> [--ref <rev>] [--default-ref <rev>] [--claims cache|none]
prints the state document as JSON. Exit 0; 1 when v2's `[chain]` does not hold 22 builds and 509 clauses; 2 when the
ref or the default-branch ref does not resolve, a git call fails or times out, a needed conf key is absent, a spec
file name outside `[A-Za-z0-9._-]+\.md` is refused, or no answer comes within DERIVE_BOUND seconds, with one
`build-state: <reason>` line on stderr.

A library caller loads it by path (its file name is no module name) and calls `derive`, `read_chain`,
`derive_predecessors` or `read_claims`; it arms no wall bound. Git is read in `root`, a worktree root, and never its working
tree; the code reused is loaded from the repository this file sits in.

THE LANDED PREDICATE (spec section 7, F1 (g)). A run record is `<build>/RUN.md` or a rotated `RUN.LANDED.<blob8>.md`
beside it, read at the ref; its `base:` and `phase:` come from its `## Run facts`. Its kind is README rule 1 at that
base, `deviations.py#derive_run_kind`, the test `unattended.sh#check_spec_run` applies. Its landings are the merges on
the default branch's first-parent history that the ref contains, whose diff against their first parent touches the
build's RUN.md and whose RUN.md carries the run's base. The default branch is `--default-ref`, else the remote-tracking
ref `refs/remotes/<remote>/<branch>` that `tools/lib/resolve_remote.py` names, and the document records both, as
`default_ref` and the `default_commit` it resolves to; one that resolves to no commit is a refusal, never the ref
itself. A build run has landed when a build-kind record has a landing; a DEFERRED unit of a landed build run is
carried, never unbuilt.

WHAT IT DOES NOT CHECK: that the default-branch ref is current, because a landing the remote took and this repository
has not fetched reads not-landed; that a merge touching RUN.md with a run's base is that run's own landing rather than
a merge of its branch for another reason; a run record rotated outside the driver; a record whose base resolves to no
commit, whose kind reads null and which lands nothing; the open forks of a CLOSED or WONTDO spec; claims newer than
the last `unattended.sh --claims`; and a spec whose name git's listing quotes, such as one holding a non-ASCII byte,
`"` or `\`, which is not listed as a spec at all.
"""
import argparse
import collections
import contextlib
import datetime
import fnmatch
import functools
import importlib.util
import io
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
V2 = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
DEVIATIONS = "memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py"
LADDER = "tools/lib/resolve_remote.py"
ROOT = "dTrueNorth"
WHOLE = frozenset({"dTrueNorth"})              # one run, spec and build together (`[answers-2]` item 5)
CID = re.compile(r"`(cl-d[A-Z]\w+-\d{4})`")
ROW = re.compile(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| [^|]+ \|$")
STATUS = re.compile(r"^\*\*Status:\*\* ([A-Z]+)", re.M)
CARRY = re.compile(r"^\*\*(?:Carries|Moved|Retired|Deferred):\*\* (cl-d[A-Z]\w+-\d{4})", re.M)
HEADER = re.compile(r"^\*\*Status:\*\*.*$", re.M)
VERB = re.compile(r" · (closes|advances) ([A-Z]+-[A-Za-z0-9]+-\d+)")
RUN_RECORD = re.compile(r"^RUN(?:\.LANDED\.[0-9a-f]{8})?\.md$")
SPEC_NAME = re.compile(r"^[A-Za-z0-9._-]+\.md$")
FACT = re.compile(r"^([\w-]+):[ \t]*(.*?)[ \t]*$", re.M)
CLAIM_REFS = "refs/gov/remote/runs/"
BEAT_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
RUN_STATES = ("landed", "landed-carrying", "not-landed")
NEXT_STATES = ("done", "running", "held", "stale", "startable", "waiting")
GIT_TIMEOUT = 120
DERIVE_BOUND = 900


class ChainError(Exception):
    """v2's `[chain]` does not hold 22 builds and 509 clauses."""


class StateError(Exception):
    """The ref or the default-branch ref does not resolve, a git call fails or times out, or a needed conf key is
    absent."""


def run_git(root, *args):
    """git's stdout in `root`; StateError naming the call when it fails or outlives GIT_TIMEOUT."""
    try:
        done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=GIT_TIMEOUT)
    except subprocess.TimeoutExpired:
        raise StateError(f"git {' '.join(args)} gave no answer within {GIT_TIMEOUT} s") from None
    if done.returncode:
        raise StateError(f"git {' '.join(args)} failed: {done.stderr.strip()[:200]}")
    return done.stdout


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@functools.lru_cache(maxsize=None)
def load_kits():
    """(deviations, tree_lib, breakpoints) from the repository this file sits in. The deviation population loads its
    siblings by worktree-relative paths, so it is loaded with that repository as the working directory."""
    for kit in ("tools/memory-tree", "tools/loop"):
        if str(REPO / kit) not in sys.path:
            sys.path.insert(0, str(REPO / kit))
    here = os.getcwd()
    os.chdir(REPO)
    try:
        deviations = load_module("build_state_deviations", REPO / DEVIATIONS)
        import breakpoints
        import tree_lib
    finally:
        os.chdir(here)
    return deviations, tree_lib, breakpoints


def read_chain(ref, root="."):
    """v2's `[chain]` at `ref`: its builds in row order, each one's stage, parents and clause ids, and the text."""
    v2 = run_git(root, "show", f"{ref}:{V2}")
    rows = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0] if "\n## [chain]" in v2 else ""
    names = re.findall(r"^\| (d[A-Z]\w+) \|", rows, flags=re.M)
    stage, parents, ids, split = {}, {}, {}, {}
    for ln in rows.split("\n"):
        m = ROW.match(ln)
        if m:
            b = m.group(1)
            stage[b] = m.group(2).strip()
            parents[b] = [p.strip() for p in m.group(3).split(",") if p.strip() in names]
            ids[b] = CID.findall(m.group(4))
            split[b] = len([u for u in m.group(4).split("; ") if u.strip()])
    n_ids = sum(len(v) for v in ids.values())
    if len(ids) != 22 or n_ids != 509 or sum(split.values()) != 509 or any(len(ids[b]) != split[b] for b in ids):
        raise ChainError(f"v2's [chain] at {ref} holds {len(ids)} builds and {n_ids} clause ids "
                         f"({sum(split.values())} by the '; ' split), not 22 and 509; the schedule is derived from "
                         "nothing")
    return {"names": names, "stage": stage, "parents": parents, "clauses": ids, "rows": rows}


def derive_predecessors(build, parents):
    """Policy J's run keys a build's runs wait on: a spec run on dTrueNorth's landing, each parent's spec run (a WHOLE
    parent's build run) and each grandparent's build run; a build run on its own spec run and each parent's build
    run. A WHOLE build is one run, its `build` key holding the spec run's list."""
    if build == ROOT:
        spec = []
    else:
        grand = sorted({g for p in parents[build] for g in parents[p]})
        spec = [("build", ROOT)] + [("build" if p in WHOLE else "spec", p) for p in parents[build]] \
            + [("build", g) for g in grand]
    if build in WHOLE:
        return {"build": spec}
    return {"spec": spec, "build": [("spec", build)] + [("build", p) for p in parents[build]]}


def read_claims(ref, names, root=".", now=None):
    """{slug: claim} for each slug of `names` the claim cache holds under refs/gov/remote/runs/ (no fetch is made).
    A live claim's `stale` is judged against `.unattended.conf`'s RESUME_STALE_BOUND at `ref`."""
    bound = re.search(r'^RESUME_STALE_BOUND="(\d+)"', run_git(root, "show", f"{ref}:.unattended.conf"), flags=re.M)
    if not bound:
        raise StateError(".unattended.conf declares no RESUME_STALE_BOUND, so a live claim's age cannot be read")
    now = now or datetime.datetime.now(datetime.timezone.utc)
    out = {}
    for ln in run_git(root, "for-each-ref", "--format=%(refname)", CLAIM_REFS).split():
        slug = ln.rsplit("/", 1)[1]
        if slug not in names:
            continue
        msg = dict(re.findall(r"^(\w[\w-]*): (.*)$", run_git(root, "log", "-1", "--format=%B", ln), flags=re.M))
        stale = None
        if msg.get("status") == "live":
            try:
                beat = datetime.datetime.strptime(msg.get("beat-utc", ""), BEAT_FORMAT).replace(
                    tzinfo=datetime.timezone.utc)
                stale = (now - beat).total_seconds() > int(bound.group(1))
            except ValueError:
                pass
        out[slug] = {"status": msg.get("status", ""), "node": msg.get("node"), "beat_utc": msg.get("beat-utc"),
                     "stale": stale}
    return out


def read_run_facts(text):
    """{key: value} of a run record's `## Run facts` section, the first line of each key."""
    section = text.split("\n## Run facts", 1)[1].split("\n## ", 1)[0] if "\n## Run facts" in text else ""
    facts = {}
    for key, value in FACT.findall(section):
        facts.setdefault(key, value)
    return facts


def read_conf(root, commit):
    """The memory-tree conf at `commit`, its family prefixes and its fork cutoff."""
    deviations, _, _ = load_kits()
    try:
        with contextlib.redirect_stderr(io.StringIO()):
            conf = deviations.gbi.read_conf_at_rev(str(root), commit)
    except deviations.gbi.Problem as e:
        raise StateError(str(e)) from None
    for key in ("MEMORY_ROOT", "FAMILIES"):
        if not conf.get(key):
            raise StateError(f".memory-tree.conf at {commit[:12]} declares no {key}")
    families = [p.split(":", 1)[1] for p in conf["FAMILIES"].split() if ":" in p]
    return conf, families, conf.get("FORK_ITEM_CUTOFF", "")


def read_blobs(root, requests):
    _, tree_lib, _ = load_kits()
    try:
        return tree_lib.read_blobs_at(str(root), requests)
    except OSError as e:
        raise StateError(str(e)) from None


def scan_forks(root, specs, cutoff):
    """The paths of `specs` ({path: text}) the driver's `plan_state` grades FORKED, in one sourced bash run. Each blob
    keeps its file name, since plan_state dates a spec by its name."""
    if not specs:
        return set()
    _, _, breakpoints = load_kits()
    paths = sorted(specs)
    with tempfile.TemporaryDirectory(prefix="build-state-") as top:
        lines = []
        for i, p in enumerate(paths):
            target = Path(top, str(i), p.rsplit("/", 1)[-1])
            target.parent.mkdir()
            target.write_text(specs[p], encoding="utf-8", newline="\n")
            lines.append(f"printf '%s %s\\n' {i} \"$(plan_state {shlex.quote(target.as_posix())} "
                         f"{shlex.quote(cutoff)})\"")
        script = Path(top, "grade.sh")        # sourced from a file: a thousand calls overflow a command line
        script.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        try:
            rc, out = breakpoints.run_sourced(Path(root).resolve(), f". {shlex.quote(script.as_posix())}")
        except (LookupError, subprocess.TimeoutExpired) as e:
            raise StateError(f"the driver's plan_state could not run: {e}") from None
    graded = dict(re.findall(r"^(\d+) (\w+)$", out, flags=re.M))
    if rc or len(graded) != len(paths):
        raise StateError(f"the driver's plan_state graded {len(graded)} of {len(paths)} specs, exit {rc}: "
                         f"{out.strip()[-200:]}")
    return {p for i, p in enumerate(paths) if graded[str(i)] == "FORKED"}


def resolve_default_ref(root, default_ref):
    """(name, commit) of the default branch landings are measured on: `default_ref` as passed, else
    refs/remotes/<remote>/<branch> as the remote ladder names it. StateError, ending `pass --default-ref <rev>`, when
    the ladder refuses or names no branch, or the name resolves to no commit; never a fall back to the derived ref."""
    if default_ref is None:
        ladder = load_module("build_state_resolve_remote", REPO / LADDER)
        remote, branch, _, refusal = ladder.resolve_remote(root)
        if refusal:
            raise StateError(f"{refusal} Or pass --default-ref <rev>")
        if not remote or not branch:
            raise StateError("the remote ladder names no default branch here; pass --default-ref <rev>")
        name = f"refs/remotes/{remote}/{branch}"
    else:
        name = default_ref
    if name.startswith("-"):
        raise StateError(f"--default-ref takes a revision, not {name}")
    if not run_git_ok(root, "rev-parse", "--verify", "--quiet", f"{name}^{{commit}}"):
        raise StateError(f"the default-branch ref {name} resolves to no commit in {root}; pass --default-ref <rev>")
    return name, run_git(root, "rev-parse", "--verify", "--quiet", f"{name}^{{commit}}").strip()


def derive_landings(root, commit, default_commit, m, names):
    """{slug: [(sha, subject, RUN.md base)]}, oldest first: the merges on `default_commit`'s first-parent line that
    `commit` contains and whose diff against their first parent touches the build's RUN.md, each with the base its
    RUN.md carries."""
    outside = set(run_git(root, "rev-list", f"{commit}..{default_commit}").split())
    cand = {}
    for b in names:
        log = run_git(root, "log", "--first-parent", "--merges", "--format=%H%x09%s", default_commit, "--",
                      f"{m}/builds/{b}/RUN.md")
        cand[b] = [tuple(ln.split("\t", 1)) for ln in reversed(log.splitlines())
                   if "\t" in ln and ln.split("\t", 1)[0] not in outside]
    blobs = read_blobs(root, [(sha, f"{m}/builds/{b}/RUN.md") for b in names for sha, _ in cand[b]])
    return {b: [(sha, subject, read_run_facts(blobs.get((sha, f"{m}/builds/{b}/RUN.md")) or "").get("base"))
                for sha, subject in cand[b]] for b in names}


def derive_next(entry, spec_done, landed, parents, claim):
    """The build's next run under Policy J, what it waits on, and its state against the claim."""
    b = entry["slug"]
    if landed[b]:
        return {"run": None, "waiting_on": [], "state": "done"}
    keys = derive_predecessors(b, parents)
    run = "whole" if b in WHOLE else ("build" if spec_done[b] else "spec")
    done = {("spec", x) for x, d in spec_done.items() if d} | {("build", x) for x, d in landed.items() if d}
    waiting = sorted(f"{k} {x}" for k, x in set(keys["build" if run != "spec" else "spec"]) - done)
    status = claim["status"] if claim else None
    if status == "live" and claim["stale"] is not True:
        state = "running"
    elif status == "held":
        state = "held"
    elif status == "live":
        state = "stale"
    else:
        state = "waiting" if waiting else "startable"
    return {"run": run, "waiting_on": waiting, "state": state}


def derive(ref="HEAD", root=".", claims=True, detail=True, default_ref=None):
    """The state document of every build of v2's `[chain]` at `ref`, in row order, its landings measured on
    `default_ref`, else the remote ladder's default branch."""
    if not run_git_ok(root, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"):
        raise StateError(f"{ref} resolves to no commit in {root}")
    commit = run_git(root, "rev-parse", "--verify", f"{ref}^{{commit}}").strip()
    subject = run_git(root, "log", "-1", "--format=%s", commit).rstrip("\n")
    default_name, default_commit = resolve_default_ref(root, default_ref)
    deviations, tree_lib, _ = load_kits()
    conf, families, cutoff = read_conf(root, commit)
    m = conf["MEMORY_ROOT"]
    chain = read_chain(commit, root)
    names, parents = chain["names"], chain["parents"]

    files = {}
    for b in names:
        prefix = f"{m}/builds/{b}/"
        listed = [p for p in run_git(root, "ls-tree", "-r", "--name-only", commit, prefix).splitlines() if p]
        rest = {p: p[len(prefix):] for p in listed}
        files[b] = {
            "specs": sorted(p for p in listed if rest[p].startswith("spec/") and p.endswith(".md")),
            "runs": sorted(p for p in listed if RUN_RECORD.match(rest[p])),
            "deviations": sorted(p for p in listed if rest[p].startswith("build/") and rest[p].count("/") == 1
                                 and fnmatch.fnmatchcase(rest[p][len("build/"):], "*-deviation-*.md")),
        }
    for b in names:
        for p in files[b]["specs"]:
            if not SPEC_NAME.match(p.rsplit("/", 1)[-1]):
                raise StateError(f"refused spec file name {p} at {commit[:12]}: not [A-Za-z0-9._-]+\\.md")
    wanted = [p for b in names for p in files[b]["specs"] + files[b]["runs"] + (files[b]["deviations"] if detail
                                                                               else [])]
    blobs = {p: text or "" for (_, p), text in read_blobs(root, [(commit, p) for p in wanted]).items()}
    landings = derive_landings(root, commit, default_commit, m, names)

    kinds = {}
    entries, spec_done, landed, terminal_not = [], {}, {}, {}
    for b in names:
        specs = files[b]["specs"]
        statuses, carried_cl = {}, set()
        for p in specs:
            s = STATUS.search(blobs[p])
            statuses[p] = s.group(1) if s else "NONE"
            carried_cl |= set(CARRY.findall(blobs[p]))
        spec_done[b] = bool(specs) and set(chain["clauses"][b]) <= carried_cl \
            and not any(s in ("OPEN", "SPECCED", "NONE") for s in statuses.values())
        unit = {}
        for p in specs:
            hit = tree_lib.parse_spec_h1(p, blobs[p], m, families)
            unit[p] = hit[1] if hit else None

        runs = []
        for p in files[b]["runs"]:
            facts = read_run_facts(blobs[p])
            base, phase = facts.get("base") or None, facts.get("phase") or None
            if base and (b, base) not in kinds:
                kinds[(b, base)] = deviations.derive_run_kind(str(root), b, base, conf, families)[0] \
                    if run_git_ok(root, "rev-parse", "--verify", "--quiet", f"{base}^{{commit}}") else None
            mine = [(i, sha, subj) for i, (sha, subj, mbase) in enumerate(landings[b]) if base and mbase == base]
            runs.append({"record": p, "kind": kinds.get((b, base)), "base": base, "phase": phase,
                         "landings": [{"sha": sha, "subject": subj} for _, sha, subj in mine],
                         "first": mine[0][0] if mine else None})
        runs.sort(key=lambda r: (r["first"] is None, r["first"] if r["first"] is not None else 0, r["record"]))
        for r in runs:
            del r["first"]
        built = [r for r in runs if r["kind"] == "build" and r["landings"]]
        landed[b] = bool(built)
        carried = []
        if landed[b]:
            for p in specs:
                if statuses[p] == "DEFERRED":
                    head = HEADER.search(blobs[p])
                    v = VERB.search(head.group(0)) if head else None
                    carried.append({"unit": unit[p], "verb": v.group(1) if v else None,
                                    "ask": v.group(2) if v else None})
        revisions = forked = devs = None
        if detail:
            revisions = {}
            for p in specs:
                head = HEADER.search(blobs[p])
                h = tree_lib.HDR_RE.match(head.group(0)) if head else None
                if unit[p]:
                    revisions[unit[p]] = int(h.group("rev")) if h else None
            devs = [{k: r[k] for k in ("id", "path", "hand", "risk", "cause")}
                    for r in (deviations.read_record(p, blobs[p]) for p in files[b]["deviations"])]
            terminal_not.update({p: b for p in specs if statuses[p] not in ("CLOSED", "WONTDO")})
        entries.append({
            "slug": b, "stage": chain["stage"][b], "parents": parents[b], "whole": b in WHOLE,
            "spec_run": {"done": spec_done[b]},
            "build_run": {"state": ("landed-carrying" if carried else "landed") if landed[b] else "not-landed",
                          "carried": carried},
            "runs": runs,
            "landing": built[-1]["landings"][-1] if built else None,
            "counts": dict(sorted(collections.Counter(statuses.values()).items())),
            "units": len(specs),
            "revisions": revisions, "forked": forked, "deviations": devs,
            "claim": None, "next": None, "_unit": unit,
        })

    if detail:
        forked_paths = scan_forks(root, {p: blobs[p] for p in terminal_not}, cutoff)
        for e in entries:
            e["forked"] = sorted(e["_unit"][p] or p for p in files[e["slug"]]["specs"] if p in forked_paths)
    cache = read_claims(commit, names, root) if claims else {}
    for e in entries:
        del e["_unit"]
        e["claim"] = cache.get(e["slug"])
        e["next"] = derive_next(e, spec_done, landed, parents, e["claim"])
    return {
        "schema": 1, "ref": ref, "commit": commit, "subject": subject, "default_ref": default_name,
        "default_commit": default_commit, "claims_read": bool(claims),
        "builds": entries,
        "landed": [e["slug"] for e in entries if e["build_run"]["state"] != "not-landed"],
        "ready": [e["slug"] for e in entries if not e["next"]["waiting_on"] and e["next"]["state"] != "done"],
        "startable": [e["slug"] for e in entries if e["next"]["state"] == "startable"],
        "running": [e["slug"] for e in entries if e["next"]["state"] in ("running", "held")],
    }


def run_git_ok(root, *args):
    """True when git exits 0 in `root` within GIT_TIMEOUT; StateError when it outlives it."""
    try:
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                              timeout=GIT_TIMEOUT).returncode == 0
    except subprocess.TimeoutExpired:
        raise StateError(f"git {' '.join(args)} gave no answer within {GIT_TIMEOUT} s") from None


def print_bound_expiry():
    print(f"build-state: no answer within {DERIVE_BOUND} s", file=sys.stderr, flush=True)
    os._exit(2)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Every dClosedLoop chain build's state at a ref, as JSON.")
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--default-ref")
    ap.add_argument("--claims", choices=("cache", "none"), default="cache")
    a = ap.parse_args(argv)
    timer = threading.Timer(DERIVE_BOUND, print_bound_expiry)
    timer.daemon = True
    timer.start()
    try:
        doc = derive(a.ref, claims=a.claims == "cache", default_ref=a.default_ref)
    except ChainError as e:
        print(f"build-state: {e}", file=sys.stderr)
        return 1
    except StateError as e:
        print(f"build-state: {e}", file=sys.stderr)
        return 2
    finally:
        timer.cancel()
    print(json.dumps(doc, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
