#!/usr/bin/env python3
"""remote_verdict.py — the `remote-ci` verdict slot's reader and the held-CI reader (TOOL-dWitnessedBar-6).

    python remote_verdict.py read [--responses <dir>] --sha <sha>
    python remote_verdict.py held [--responses <dir>] <anchor URL> <workflow file>
    python remote_verdict.py pin

ONE BOUNDED GET, `read_api`: https to the literal host `api.github.com`, no redirect followed, no
credential sent or read, 30 seconds and 4 MiB. A non-200, an oversize body or a non-JSON body is a DEAD
PROBE. `--responses <dir>` points it at canned JSON files named by `derive_response_name` of the request
path, a missing file answering 404: an arm seam, never a conf key.

THE WITNESS RULE, `read_remote_verdict`, for the SHA judged: KEY, a push run of the row's declared
workflow whose `head_sha` is the SHA, the SHA's tree resolved in this clone; WRITER, the run's check suite
app slug `github-actions`, its `path` the declared workflow and its `event` `push`, and the declared job;
LIVENESS, the job's declared bar step concluded `success`, not `skipped`; SOURCE, the files
`verdict.remote.pin-scope` names derive at the SHA the id `verdict.remote.pin` holds, as
`verdict.remote.trust` says. The three keys are read at the landed revision, never at the SHA. Under
`app-only` the source check is skipped and a passing read is GREEN with witness `claimed`, never
`witnessed`; under the other two values pinned files that differ read HELD. No pin set reads HELD, `no
pin`; any other refusal of a key is a DEAD PROBE. The pinned blobs are read from the local object database
and a SHA the clone lacks is a DEAD PROBE, never fetched.

THE PIN, `derive_pin`: `git hash-object --stdin`, which writes nothing, over one `<path> <blob id>` line per
file the scope names, sorted by path, each ending LF. `workflow` names the row's workflow, and
`dispatch-closure` adds this kit's `run-gates.sh`, the leg manifest and `.githooks/gate-env.sh`. `pin`
prints the lines and the id the owner would set at HEAD, and writes nothing; the owner sets it through the
loop kit's `policy_edit.py set verdict.remote.pin <id>`.

THE HELD READER, `read_held_runs`, moved whole from the unattended kit's bash function: the latest
completed scheduled run of the workflow, one TAB row per `held <suite>` job and ONE liveness line, or ONE
DEAD PROBE line. The unattended kit's `write_held_asks` files each red.

WHAT THIS DOES NOT CHECK: that the pinned files are all the bar job executes (`dispatch-closure` pins its
dispatch, never the floor preflight or a leg's own script), or that GitHub's API tells the truth.
"""
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

sys.dont_write_bytecode = True
HERE = pathlib.Path(os.path.abspath(__file__)).parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from verdict_backends import (SHA, TOOL_ROOT, Refusal, Verdict, check_backend, read_backends,  # noqa: E402
                              read_policy_value, read_tree_of, run_git)

SAY = "remote-verdict"
API = "https://api.github.com"
CAP = 4 << 20
GET_BOUND = 30
APP_SLUG = "github-actions"
TRUST = ("pinned-workflow", "owner-reviews-workflow-change", "app-only")
SCOPES = ("workflow", "dispatch-closure")
ANCHOR = re.compile(r"(?:https://github\.com/|ssh://git@github\.com/|git@github\.com:)([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+?)(?:\.git)?/?")
WORKFLOW_FILE = re.compile(r"[A-Za-z0-9._-]+\.ya?ml")
DERIVED_REFUSAL = "a derived default no reader computes yet"  # the policy kit's DERIVED_WHY


class DeadProbe(Exception):
    """A read that could not see what it was asked: its message is why."""


class RefuseRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


OPENER = urllib.request.build_opener(RefuseRedirect)


def derive_response_name(path):
    """The canned file `--responses` answers `path` from: the path after `/repos/<owner>/<repo>/`, query
    included, every character outside [A-Za-z0-9._-] an underscore, then `.json`."""
    rest = re.sub(r"^/repos/[^/]+/[^/]+/", "", path)
    return re.sub(r"[^A-Za-z0-9._-]", "_", rest) + ".json"


def read_api(path, responses=None):
    """The JSON one bounded GET of `path` under api.github.com answers, or its canned file under `responses`;
    a DeadProbe naming the request otherwise."""
    if responses is not None:
        f = pathlib.Path(responses, derive_response_name(path))
        if not f.is_file():
            raise DeadProbe(f"GET {path} answered HTTP 404")
        body = f.read_bytes()[:CAP + 1]
    else:
        req = urllib.request.Request(API + path, headers={"Accept": "application/vnd.github+json",
                                                         "User-Agent": "gov-remote-verdict"})
        try:
            with OPENER.open(req, timeout=GET_BOUND) as r:
                status, body = r.status, r.read(CAP + 1)
        except urllib.error.HTTPError as e:
            raise DeadProbe(f"GET {path} answered HTTP {e.code}") from None
        except Exception as e:
            raise DeadProbe(f"GET {path} did not answer: {type(e).__name__}") from None
        if status != 200:
            raise DeadProbe(f"GET {path} answered HTTP {status}")
    if len(body) > CAP:
        raise DeadProbe(f"GET {path} answered more than the 4 MiB cap")
    try:
        return json.loads(body)
    except ValueError:
        raise DeadProbe(f"GET {path} answered something that is not JSON") from None


def read_anchor(url):
    """(owner, repo) of a github.com repository URL; a DeadProbe otherwise."""
    m = ANCHOR.fullmatch((url or "").strip())
    if not m:
        raise DeadProbe("the anchor URL is not a github.com repository, so there is no public run listing to read: "
                        + (url or "(none)"))
    return m.group(1), m.group(2)


# ------------------------------------------------------------------------------------------ the held reader
def read_held_runs(anchor_url, workflow, responses=None):
    """The latest completed scheduled run of `workflow` at the anchor -> one `held` TAB row per held job and
    ONE liveness line, or ONE DEAD PROBE line."""
    try:
        if not WORKFLOW_FILE.fullmatch(workflow or ""):
            raise DeadProbe("the workflow file name is outside [A-Za-z0-9._-]+ ending .yml or .yaml: " + repr(workflow))
        owner, repo = read_anchor(anchor_url)
        base = f"/repos/{owner}/{repo}/actions"
        runs = read_api(f"{base}/workflows/{workflow}/runs?event=schedule&status=completed&per_page=1",
                        responses).get("workflow_runs") or []
        if not runs:
            raise DeadProbe(f"no completed scheduled run of {workflow} exists at {owner}/{repo}")
        rid, sha = runs[0].get("id"), str(runs[0].get("head_sha") or "")
        # EVERY FIELD BEFORE THE LAST IS NON-EMPTY: the writer splits on TAB, which bash collapses, so an
        # empty sha would shift the conclusion out of its field and a red would read as no verdict at all.
        if not re.fullmatch(r"[0-9a-f]{40}", sha) or not isinstance(rid, int):
            raise DeadProbe("the latest completed scheduled run carries no 40-hex head sha or integer id: %r %r"
                            % (sha, rid))
        jobs, total, page = [], None, 1
        while True:
            got = read_api(f"{base}/runs/{rid}/jobs?per_page=100&page={page}", responses)
            total, batch = got.get("total_count"), got.get("jobs") or []
            jobs += batch
            if not batch or not isinstance(total, int) or len(jobs) >= total or page >= 50:
                break
            page += 1
        if not isinstance(total, int) or len(jobs) != total:
            raise DeadProbe("run %s declares %s job(s) and %d were read" % (rid, total, len(jobs)))
        held = [j for j in jobs if str(j.get("name") or "").startswith("held ") and str(j.get("name"))[5:].strip()]
        if not held:
            raise DeadProbe("run %s at %s carries %d job(s) and none is named held <suite>" % (rid, sha[:8], len(jobs)))
    except DeadProbe as e:
        return ["held reader: DEAD PROBE — %s" % e]
    out, red = [], 0
    for j in held:
        c = str(j.get("conclusion") or "")
        red += c in ("failure", "timed_out")
        # A TAB, a newline, a CR or a NUL in a name would split the row; each becomes U+001F, a control
        # character the writer refuses by name, so the row grammar holds and the refusal stays visible.
        out.append("held\t%s\t%s\t%s\t%s" % (str(j["name"])[5:].translate({0: 31, 9: 31, 10: 31, 13: 31}), sha, rid, c))
    out.append("held reader: run %s at %s · %d held job(s) read · %d red" % (rid, sha[:8], len(held), red))
    return out


# ------------------------------------------------------------------------------------------ the pin
def read_scope_paths(backend, scope):
    """The repository paths `verdict.remote.pin-scope` = `scope` names, this kit's spelled from where it sits."""
    paths = [backend.get("workflow") or ".github/workflows/remote-ci.yml"]
    if scope == "dispatch-closure":
        rc, kit_rel = run_git(HERE, "rev-parse", "--show-prefix")
        kit_rel = kit_rel if rc == 0 else "tools/run-gates/"
        tool_rel = kit_rel.rstrip("/").rpartition("/")[0]
        paths += [kit_rel + "run-gates.sh", (tool_rel + "/" if tool_rel else "") + "gate-legs.json",
                  ".githooks/gate-env.sh"]
    return sorted(paths)


def derive_pin(repo, sha, paths):
    """(lines, id): one `<path> <blob id>` line per path at `sha`, sorted by path, and the object id
    `git hash-object --stdin` gives them; a DeadProbe naming a path `sha` lacks."""
    lines = []
    for p in sorted(paths):
        rc, blob = run_git(repo, "rev-parse", "--verify", "-q", f"{sha}:{p}")
        if rc != 0 or not blob:
            raise DeadProbe(f"{sha[:8]} holds no {p}, so the pinned files do not derive")
        lines.append(f"{p} {blob}\n")
    rc, oid = run_git(repo, "hash-object", "--stdin", data="".join(lines))
    if rc != 0 or not oid:
        raise DeadProbe(f"git hash-object --stdin exited {rc}")
    return lines, oid


def read_remote_keys(repo):
    """(trust, scope, pin or None) at the landed revision; a DeadProbe naming any refusal but the pin's
    derived default, which is no pin."""
    got = {}
    for key, default in (("verdict.remote.trust", TRUST[0]), ("verdict.remote.pin-scope", SCOPES[0]),
                         ("verdict.remote.pin", None)):
        value, refused = read_policy_value(repo, key)
        if refused and not (key == "verdict.remote.pin" and DERIVED_REFUSAL in refused):
            raise DeadProbe(f"{key} does not read: {refused}")
        got[key] = value if value is not None or refused else default
    return got["verdict.remote.trust"], got["verdict.remote.pin-scope"], got["verdict.remote.pin"]


# ------------------------------------------------------------------------------------------ the slot's reader
def read_remote_verdict(backend, sha, tree, repo=".", responses=None):
    """`remote-ci`: the witness rule over `sha`, whose tree is `tree` -> Verdict."""
    try:
        trust, scope, pin = read_remote_keys(repo)
        if trust != "app-only" and not pin:
            return Verdict("HELD", "", "no pin: verdict.remote.pin is unset, so no workflow is pinned; the owner pins "
                                       "it with policy_edit.py set verdict.remote.pin <id>, which `remote_verdict.py pin` prints")
        rc, url = run_git(repo, "remote", "get-url", os.environ.get("GOV_REMOTE") or "origin")
        owner, name = read_anchor(url if rc == 0 else "")
        workflow = backend.get("workflow") or ".github/workflows/remote-ci.yml"
        base = f"/repos/{owner}/{name}"
        runs = read_api(f"{base}/actions/workflows/{workflow.rsplit('/', 1)[-1]}/runs?head_sha={sha}&event=push"
                        "&per_page=10", responses).get("workflow_runs") or []
        # KEY and WRITER, the run's half: the SHA judged, a push, the declared workflow file.
        run = next((r for r in runs if r.get("head_sha") == sha and r.get("event") == "push"
                    and str(r.get("path") or "").split("@")[0] == workflow), None)
        if run is None:
            return Verdict("NONE", "", f"no push run of {workflow} at {sha[:8]} is listed")
        if run.get("status") != "completed":
            return Verdict("NONE", "", f"run {run.get('id')} of {workflow} is {run.get('status')}, not completed")
        jobs = read_api(f"{base}/actions/runs/{run.get('id')}/jobs?per_page=100", responses).get("jobs") or []
        suite = read_api(f"{base}/check-suites/{run.get('check_suite_id')}", responses)
        # WRITER, the platform's own app (§8 F4): the check suite's app slug, never the pusher.
        slug = str((suite.get("app") or {}).get("slug") or "")
        if slug != APP_SLUG:
            return Verdict("NONE", "", f"run {run.get('id')}'s check suite was written by {slug or 'no app'}, not {APP_SLUG}")
        job = next((j for j in jobs if j.get("name") == backend.get("job", "bar")), None)
        if job is None:
            return Verdict("NONE", "", f"run {run.get('id')} carries no job {backend.get('job', 'bar')}")
        # LIVENESS: the declared bar step ran and passed; skipped is no verdict.
        step = next((s for s in job.get("steps") or [] if s.get("name") == backend.get("step")), None)
        concl = str((step or {}).get("conclusion") or "")
        if step is None or concl in ("", "skipped"):
            return Verdict("NONE", "", f"job {job.get('name')}'s bar step " + ("is absent" if step is None else
                                                                               f"concluded {concl or 'nothing'}"))
        if concl != "success":
            return Verdict("RED", "", f"run {run.get('id')}'s bar step concluded {concl}")
        if trust == "app-only":
            return Verdict("GREEN", "claimed", f"run {run.get('id')}, its source unchecked under verdict.remote.trust = app-only")
        # SOURCE, from this clone's object database: the scope's files at the SHA derive the pin.
        if not read_tree_of(repo, sha):
            raise DeadProbe(f"this clone lacks {sha[:8]}, so its pinned files are unread")
        paths = read_scope_paths(backend, scope)
        _lines, oid = derive_pin(repo, sha, paths)
        if oid != pin:
            ask = "until the owner re-pins" if trust == "owner-reviews-workflow-change" else "the owner re-pins or refuses it"
            return Verdict("HELD", "", f"the files verdict.remote.pin-scope = {scope} names ({', '.join(paths)}) derive "
                                       f"{oid[:12]} at {sha[:8]}, not the pin {pin[:12]}; {ask}")
        return Verdict("GREEN", "witnessed", f"run {run.get('id')} of {workflow}, its pinned files at {sha[:8]} deriving the pin")
    except DeadProbe as e:
        return Verdict("DEAD PROBE", "", str(e))


# ------------------------------------------------------------------------------------------ the verbs
def run_read(sha, responses, repo="."):
    """The `read` verb -> 0 GREEN, 1 any other state, 2 refused."""
    try:
        backend = check_backend("remote-ci", read_backends(TOOL_ROOT))
    except Refusal as e:
        print(f"{SAY}: refused · {e}")
        return 2
    full = sha
    if not SHA.fullmatch(sha or ""):
        rc, full = run_git(repo, "rev-parse", "--verify", "-q", f"{sha}^{{commit}}")
        full = full if rc == 0 else ""
    tree = read_tree_of(repo, full)
    v = (read_remote_verdict(backend, full, tree, repo=repo, responses=responses) if tree else
         Verdict("DEAD PROBE", "", f"this clone lacks {sha[:8]}, so its tree is unknown"))
    why = f"witness {v.witness}: {v.why}" if v.witness else v.why
    print(f"verdict: remote-ci · {v.state} · {(full or sha)[:8]} · {why}")
    return 0 if v.state == "GREEN" else 1


def run_pin(repo="."):
    """The `pin` verb: the lines and the id the owner would set at HEAD; writes nothing."""
    try:
        backend = check_backend("remote-ci", read_backends(TOOL_ROOT))
        scope, refused = read_policy_value(repo, "verdict.remote.pin-scope")
        if refused:
            raise Refusal(f"verdict.remote.pin-scope does not read: {refused}")
        rc, head = run_git(repo, "rev-parse", "--verify", "-q", "HEAD")
        if rc != 0:
            raise Refusal("HEAD names no commit here")
        lines, oid = derive_pin(repo, head, read_scope_paths(backend, scope or SCOPES[0]))
    except (Refusal, DeadProbe) as e:
        print(f"{SAY}: refused · {e}")
        return 2
    sys.stdout.write("".join(lines))
    print(f'verdict.remote.pin = "{oid}"')
    return 0


def main(argv):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace", newline="\n")
    ap = argparse.ArgumentParser(prog="remote_verdict.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("verb", choices=["read", "held", "pin"])
    ap.add_argument("args", nargs="*", help="held: <anchor URL> <workflow file>")
    ap.add_argument("--sha", help="read: the commit judged")
    ap.add_argument("--responses", help="an arm seam: canned JSON files answering read_api")
    a = ap.parse_args(argv)
    if a.verb == "read":
        if not a.sha or a.args:
            ap.error("read takes --sha <sha> and no positional argument")
        return run_read(a.sha, a.responses)
    if a.verb == "held":
        if len(a.args) != 2:
            ap.error("held takes <anchor URL> <workflow file>")
        print("\n".join(read_held_runs(a.args[0], a.args[1], a.responses)))
        return 0
    if a.args or a.sha or a.responses:
        ap.error("pin takes no argument")
    return run_pin()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
