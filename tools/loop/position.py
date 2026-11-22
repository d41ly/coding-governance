#!/usr/bin/env python3
"""position.py — where a build is and what runs next, from witnesses alone (TOOL-dDeclaredLoop-7).

    python position.py <slug> [--json | --next-line [--frontier]]   # the position of <slug> in this working directory
    python position.py <slug> --boundary <key|none>     # the item boundary, I12, against a held pointer
    python position.py --check-refusal <tag> <key>      # may the driver record this refusal row
    python position.py --fixture --plant <case>         # one fixture case
    python position.py --selftest                       # every case

`derive_position(repo, slug, definition=None)` reads only witnesses, each through the reader the tree
holds: the run branch's `--first-parent` commits and their `Pass:` trailers through the memory-tree
kit's `read_commits` and `derive_attribution` in the `replace` view; the build's recorded moves through
`loop_transition.read_transitions`, each checked by `loop_table.check_recorded_move`; the steps,
`[states]` and the transition rows through `read_transition_rows`; the items through
`loop_items.read_composed_items` at the build's pin, the commit `composition.read_step_composition` reads
from its newest move, or HEAD's where that move carries none (TOOL-dDeclaredLoop-26), gov's own `[[item]]`
rows where that composition is unarmed in the tree, or the `[[item]]` rows of `definition` where a caller
passes a parsed one, the read printed `composition@<sha8> · pinned` or `· unpinned`; the item rows the
newest move's `scenario` activates, read at the same pin through `scenario.read_activated_rows` and
composed with the items, the read printed `scenario=<value> · <n> activated`, and nothing where that move
carries no scenario (TOOL-dDeclaredLoop-27); the build's own applied flow changes, `adapt.py`'s
`read_flow_layer`, composed after those rows as the build's last layer, so a held, refused or pending
change is absent (TOOL-dDeclaredLoop-28); the witnesses its
moves name through `composition.derive_carried_witnesses`, so a witness under a renamed item reads under
its successor;
the acceptance records through `build_records.read_records` with `read_acceptance`; the run-state file's
facts and parked rows; the remote-tracking tip of the default branch. No status header, README status
word or `phase:` fact decides a step.

Each unit's M2 state comes from the unattended driver's `--plan` rows, handed over in the environment
variable `GOV_POSITION_STATES`, TAB-separated lines: `unit <id> <state>` per row in build order, MISSING
rows included, `ask <id>` for the first undecided ask, `parent <slug> <derived phase>` per `parents:`
build, `bound <seconds>` for the driver's `RESUME_STALE_BOUND`, and `owed <PARK_KINDS_OWED>
<PARK_ACTS_OWED>`, the two space-joined sets. Where the variable is unset or empty, this runs the driver's
`--plan <slug>` with it set empty, which prints those lines in place of its `next:` line, so the driver
keeps the one M2 classifier and the call is not circular.

A unit's step is `none`, then `designed` when its state reads READY (a `DONE` row reading as its grade),
`built` when a pass commit attributed to it has a well-formed acceptance record naming the unit in
`Caused-by` and that commit in `Sha`, `tested` when the run-state `gates-run` fact's graded tip contains
that commit, and `deployed` when the remote-tracking tip does; each step needs the one before it.
While the definition's `acceptance` computed witness has a writer of the `ROUTE_STAND_IN` form, as
`check_computed_witnesses` grades it, the acceptance half is unarmed (TOOL-dDeclaredLoop-45): a unit no
acceptance record names stands on its newest pass commit alone, its unit line ending `· acceptance
unarmed`, and a unit a record names is read as above. An actor writer, or no `acceptance` row, arms it. The
build's step is the step tag of the item on the unit table's forward row out of its least-advanced
unit's state, ties broken by row order, `none` once every unit is deployed. The next item is the first
item of that step, in composition order, whose witness does not hold and whose needs are witnessed. A
witness is read for three kinds of item only: a step's exit, on a recorded move out of that step's
state; the unit table's forward items, on the least-advanced unit's step; and an item a recorded move
names. Every other item's witness is unread, printed as an `evidence` claim, and a need on it is unmet.
The frontier (TOOL-dDeclaredLoop-14) is every item of that step, in composition order, whose witness
does not hold and whose needs are witnessed, so a refused instance stays on it; the next item is its
first entry. The run's `refusal` rows, which the driver's `--refused` writes, are read through runlog's
`read_run_state`, found by `resolve_kit_dir`; where that kit does not resolve the line output says
`refusal — unarmed` and still prints the frontier. Two fields serve the transition writer's path
comparison (TOOL-dDeclaredLoop-28): `witnesses`, each item of the build's step mapped to `held`, `unheld`
or `unread` by the same witness read, and `undeclared`, each tag a recorded move names that the
composition at the pin lacks, mapped to the states the moves naming it left. `--next-line --frontier` prints the frontier's tags,
space-separated, or `none`, on a second line, which `--plan` prints as its `frontier:` line.
`--check-refusal <tag> <key>` prints `loop: refusal held`, exit 0, where the composition declares the
tag and the key is `derive_instance_key`'s shape for it; `loop: refused`, exit 1, otherwise; and
`loop: unarmed`, exit 2, where the composition does not read. An unarmed composition reads gov's own
`[[item]]` rows, as `derive_position` does.

The answer is one of `ANSWERS`, the first that holds: `invalid-input` (no build, a README that does not
parse, a read refusal, a recorded move no build row holds, or a hand-over naming no unit, no MISSING id
and no undecided ask), `stale-remote` (the remote tip's claim not `fresh`: a remote the ladder refuses,
or a tracking tip last fetched longer ago than the bound, the fetch read as the newest of the mtime of
each `FETCH_HEAD` under the common git directory and its `worktrees/*/` that holds a line for the
default branch fetched from the remote's own URL, `git remote get-url` as git writes it into `FETCH_HEAD`,
its user part, every trailing `/` and one `.git` cut from both sides (TOOL-dDeclaredLoop-74,
TOOL-dDeclaredLoop-77), and the tracking ref's newest
reflog entry, or, where none of those is read, the default branch's newest `clone: ` reflog entry; the
ref's `read —` line ends `fetched <n>s ago · from FETCH_HEAD|reflog|clone`, or `fetched never`, which gains
` · core.logAllRefUpdates=false` where the repository's setting reads false (TOOL-dDeclaredLoop-75 S34), and each
skipped `FETCH_HEAD` follows it as `read — <name> · skipped — empty`, `no line for <branch> of <remote>`
or `unreadable`), `terminal` (the state is a `[states]` terminal, or every unit is deployed
and no ask stands), `awaiting` on an owed parked entry or an unpassed hold, `blocked` on a `parents:`
build neither recorded nor derived `LANDED`, `act` with a next item, `awaiting` on an undecided ask, and
`stuck` naming the step's unwitnessed exit. Line output is §4's six line kinds; `--json` the same fields
as one object, each unit carrying `acceptance_armed`, false exactly where its line ends `· acceptance
unarmed` (TOOL-dDeclaredLoop-67 S50); `--next-line` the `next:` shape `render_next_line` picks from `NEXT_SHAPES`. Exit 0 for
every answer but `invalid-input`, which exits 2.

THE ITEM BOUNDARY, I12 (KICK-dKeptSession-13 S1). `derive_item_boundary(repo, slug, pointer, pos=None)`
reads one position, or the `pos` its caller already derived, and returns the build's current item where
it differs from `pointer`, else None. The current item is the `act` answer's `next.key`, the instance
key `derive_instance_key` spells; any other answer is `none`, except `stale-remote` and `invalid-input`,
which say nothing about the item and keep `pointer`. `--boundary <key|none>` derives once and prints
`boundary — <pointer> → <key|none>` or `boundary — none crossed · item <pointer>`, the second form
ending ` · <answer>` for a kept pointer, then `forked — <unit id> · …` or `forked — none`, the units the
same derivation's hand-over grades `FORKED`; it exits 0, and 2 on `invalid-input` after both lines.

THE ABSENT REMOTE (TOOL-dDeclaredLoop-56 S36). Where the ladder names no remote and refuses nothing, or
the tracking ref of its default branch does not resolve, the remote reads absent: the answer is taken on
local witnesses, so no unit reads `deployed`, the interrupt `remote · none` prints, and no remote-tip
claim and no `read` row is added. A tracking ref deleted by hand reads the same, so such a node acts on
its local witnesses.

`--fixture --plant <case>` builds one scratch repository under the host temp folder, plants the case,
prints the engine's lines and one `position: fixture · <case> · held` or `· MISSED <why>` line, and
removes the scratch; it exits as the engine did where the case held, 1 where it missed, 2 where a kit it
needs does not resolve. Every case runs with `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_SYSTEM` naming one empty
file under its scratch top, so no setting of the machine's reaches it (TOOL-dDeclaredLoop-75 S34). `frontier-refused`, `frontier-bad-key`, `plan-frontier`, `built-unarmed`,
`plan-line` and `status-line` run the unattended driver found by `resolve_kit_dir`. `--selftest` runs every case
through `loop_lib.run_selftest_cases`.

WHAT THIS DOES NOT CHECK: a witness reader for any item outside the three kinds above, which lands with
the build that arms the item; a settling row for a parked entry, which the driver's grammar does not
have yet, so every owed entry stands; the mailbox, printed `unarmed`; that a `gates-run` fact names a
green bar rather than the last bar run; a fetch run with `--no-write-fetch-head`, which leaves no
`FETCH_HEAD` and so reads by the reflog where the ref moved, and as stale where it did not; a
`FETCH_HEAD` whose URL git spelled otherwise than `derive_fetch_url` spells the configured URL, its
user part cut by git's rule, then every trailing `/` and one `.git`, such as one git rewrote through a
`url.<base>.insteadOf`, which reads skipped.
"""
import argparse
import copy
import datetime
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from claims import derive_claim_key, derive_claim_verdict, resolve_remote  # noqa: E402
from composition import derive_carried_witnesses, read_step_composition  # noqa: E402
from loop_items import read_composed_items  # noqa: E402
from loop_lib import (NO_STEP, ROUTE_STAND_IN, LoopError, check_computed_witnesses, read_definition,  # noqa: E402
                      read_item_rows, read_memory_tree, resolve_kit_dir, resolve_memory_root, run_selftest_cases)
from loop_parents import read_policy_kit  # noqa: E402
from loop_table import check_recorded_move, derive_from_states, read_transition_rows  # noqa: E402
from loop_transition import read_transitions  # noqa: E402
from scenario import read_activated_rows  # noqa: E402
from loop_witness import read_clean_env, read_git, remove_tree, resolve_bash, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "position"
ANSWERS = ("act", "awaiting", "blocked", "terminal", "stuck", "invalid-input", "stale-remote")
#: The answers that say nothing about the item, so the item boundary keeps its pointer (KICK-dKeptSession-13 F5).
KEPT_ANSWERS = ("stale-remote", "invalid-input")
#: The environment hand-over from the driver's `--plan`.
HANDOVER = "GOV_POSITION_STATES"
#: The reason of the one invalid-input answer that renders the nothing-graded shape.
NOTHING_GRADED = "no tracked spec grades as a unit, no roster id is MISSING and no ask is undecided"
#: The five `next:` shapes `--plan` prints, byte for byte as the driver's ladder printed them, and the
#: fall-through, which no reader matches as an all-clear.
NEXT_SHAPES = {"live-unit": "<id> (READY - build it)",
               "live-state": "<id> (<state>)",
               "missing-unit": "<id> (MISSING - spec it first)",
               "undecided-ask": "<id> (UNDECIDED - plan a unit that closes it, or dispose it)",
               "nothing-graded": "none - no tracked spec grades as a unit (see the NOT A UNIT rows above)",
               "everything-terminal": "none - every tracked spec is terminal",
               "other": "none - <answer>: <reason>"}
UNIT_ID = re.compile(r"[A-Za-z]+-[A-Za-z0-9]+-\d+")
PARKED_ROW = re.compile(r"^[0-9][0-9-]*T[0-9:]*Z (\S+) · item (\S+)")
#: `--plant`'s cases and what each owes.
PLANTS = {"steps": "unit 1 deployed, unit 2 built, unit 3 designed: act at unit 3's step",
          "typed-status": "unit 2's header typed CLOSED, no pass commit: designed, never built",
          "idempotent": "item 1 witnessed by a recorded move naming it: next is item 2, and the key moves with an input",
          "owner-decision": "an owed decision park, unsettled: awaiting",
          "parent-unlanded": "parents: names a build with no landed move and no derived LANDED: blocked",
          "terminal": "the newest recorded move enters landed: terminal",
          "stale-remote": "a remote whose tracking tip's newest reflog entry predates the bound: stale-remote, read from reflog",
          "no-remote": "no remote at all: act on local witnesses, interrupt remote · none, no remote tip claim",
          "fresh-clone": "a clone with no tracking reflog and no FETCH_HEAD: not stale-remote, read from clone",
          "quiet-remote": "stale-remote's aged reflog, then a fetch from a linked worktree: not stale-remote, read from FETCH_HEAD",
          "offline-stale": "fresh-clone, then a fetch whose FETCH_HEAD is dated past the bound: stale-remote, read from FETCH_HEAD",
          "failed-fetch": "stale-remote's aged reflog, then a fetch from a path that does not exist: stale-remote, "
                          "FETCH_HEAD skipped as empty, read from reflog",
          "bad-transition": "a recorded move no build row holds: invalid-input, exit 2",
          "deadlock": "the step's root item needs an item of a later step: stuck",
          "bar-wait": "every unit built, no gates-run fact, no ask: act, and the terminal next: shape",
          "frontier-chain": "A witnessed, B needs A, C needs B, D the next step's root: the frontier is B",
          "frontier-parallel": "A and B with no needs, neither witnessed: the frontier is A and B",
          "frontier-refused": "the driver's --refused on A at its key: one refusal row, A on the frontier",
          "frontier-bad-key": "--refused with a malformed key, then an undeclared tag: exit 1 each, the file unchanged",
          "frontier-none": "the step narrowed to A witnessed and an item whose need is unmet: no frontier",
          "plan-frontier": "the frontier-refused repository, then --plan: frontier: A beneath next:",
          "built-unarmed": "B tested, then A's pass commit and no record under the shipped stand-in writer: A built, "
                           "tagged, acceptance_armed false; --status names A",
          "built-unheld": "built-unarmed and a record naming A at a commit not attributed to A: A designed, no tag",
          "built-armed": "built-unarmed with the writer executor:build.acceptance, then no acceptance row: A designed",
          "fetch-other-branch": "stale-remote's aged reflog, then a fetch of another branch: stale-remote, FETCH_HEAD "
                                "skipped as holding no line for main, read from reflog",
          "clone-without-reflog": "fresh-clone with core.logAllRefUpdates=false: stale-remote, fetched never, the "
                                  "setting named",
          "scp-remote": "stale-remote's aged reflog, then a fetch over an ssh shim from git@example.com:up.git: not "
                        "stale-remote, read from FETCH_HEAD, nothing skipped",
          "ssh-userinfo-remote": "scp-remote over ssh://user@example.com/up.git: not stale-remote, read from FETCH_HEAD, "
                                 "nothing skipped",
          "url-forms": "stale-remote's aged reflog, then a fetch failing at connect from a URL carrying a password: "
                       "stale-remote, FETCH_HEAD skipped as empty, no password printed; each url-forms pair as tabled; "
                       "then FETCH_HEAD naming main of another URL, skipped as no line for main of origin, no "
                       "password printed; then a fetch over git's dumb http from 127.0.0.1, its written URL owed equal",
          "plan-line": "the driver's next: line equals render_next_line's, in three states",
          "status-line": "the driver's --status prints the engine's position line",
          "boundary": "over planted engine answers: the key held is no crossing, another key crosses, awaiting "
                      "crosses to none, stale-remote keeps the pointer, and forked names the FORKED unit"}
FX_SLUG = "tPos"
FX_IDS = ["TOOL-tPos-1", "TOOL-tPos-2", "TOOL-tPos-3"]
FX_ASK = "TOOL-tAsk-1"
FX_OWED = ("decision abort override waiver handoff", "retire supersede defer")
#: The hand-over's bound, in seconds.
FX_BOUND = 5400
#: The frontier plants' A, B and C, of the build's step, and D, the next step's root, as shipped.
FX_A, FX_B, FX_C, FX_D = "item.build.base", "item.build.unit-lease", "item.build.unit-pass", "item.test.merge"
#: The build step's unit-forward item, the one the least-advanced designed unit has not passed.
FX_UNIT = "item.build.acceptance"
#: The plants that run the unattended driver, and so copy its conf into the scratch repository.
FX_DRIVER = ("frontier-refused", "frontier-bad-key", "plan-frontier", "built-unarmed", "plan-line", "status-line")
#: The `url-forms` plant's pairs (TOOL-dDeclaredLoop-77 S3): a configured URL, a URL as git wrote it into
#: `FETCH_HEAD`, and whether `derive_fetch_url` owes them equal.
FX_URL_FORMS = (("git@example.com:up.git", "example.com:up", "equal"),
                ("ssh://user@example.com/up.git", "ssh://example.com/up", "equal"),
                ("example.com:up.git/", "example.com:up", "equal"),
                ("C:/x/up.git//", "C:/x/up", "equal"),
                ("https://user:tok@host.example/r.git", "https://host.example/r", "equal"),   # TOOL-dDeclaredLoop-79 S21
                ("https://user@host.example/r/", "https://host.example/r", "equal"),
                ("git@other.example:up.git", "example.com:up", "unequal"),
                ("C:/x@b/up.git", "C:/y@b/up", "unequal"),
                # TOOL-dDeclaredLoop-82 S19: the regression pairs unattended.sh's norm_endpoint comment records
                ("github.com:alice/repo", "github.com:bob/repo", "unequal"),
                ("git@github.com:alice/repo", "github.com:alice/repo", "equal"))


# ------------------------------------------------------------------------------------------ the reads
def read_blob_id(path):
    """The first eight hex digits of `path`'s git blob id, hashed here rather than by a git spawn."""
    data = pathlib.Path(path).read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()[:8]


def read_handover(repo, slug):
    """The driver's hand-over for `slug`, from `GOV_POSITION_STATES` or, where that is unset or empty,
    from the driver's `--plan` run with it set empty. ValueError where `--plan` refuses; LookupError
    where the driver or a bash to run it does not resolve."""
    text = os.environ.get(HANDOVER, "")
    if not text:
        driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
        bash = resolve_bash(driver)
        if bash is None:
            raise LookupError("no bash can run %s" % driver.as_posix())
        p = subprocess.run([bash, str(driver), "--plan", slug], cwd=str(repo), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=dict(os.environ, **{HANDOVER: ""}), timeout=900)
        if p.returncode != 0:
            said = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]
            raise ValueError("the driver's --plan %s refused: %s" % (slug, said[-1] if said else "exit %d" % p.returncode))
        text = p.stdout
    out = {"units": [], "ask": None, "parents": {}, "bound": None, "owed": ((), ())}
    for ln in text.splitlines():
        f = ln.rstrip("\r").split("\t")
        if f[0] == "unit" and len(f) == 3:
            out["units"].append((f[1], f[2]))
        elif f[0] == "ask" and len(f) == 2 and f[1]:
            out["ask"] = f[1]
        elif f[0] == "parent" and len(f) == 3:
            out["parents"][f[1]] = f[2]
        elif f[0] == "bound" and len(f) == 2 and f[1].isdigit():
            out["bound"] = int(f[1])
        elif f[0] == "owed" and len(f) == 3:
            out["owed"] = (tuple(f[1].split()), tuple(f[2].split()))
    return out


def derive_fetch_url(url):
    """`url` as git spells it on a `FETCH_HEAD` line (TOOL-dDeclaredLoop-74 S1, TOOL-dDeclaredLoop-77 S1):
    the user part cut, then every trailing `/`, then one trailing `.git`. The user part is git's: in a
    `<scheme>://` URL, its scheme of letters, digits, `+`, `.` and `-`, the bytes through the first `@`
    where no `/` comes before it; in an scp form, the bytes through the first `@` where a `:` follows it
    and no `/` comes before the URL's first `:`. A local path keeps every other byte."""
    if "://" in url:
        scheme, rest = url.split("://", 1)
        at, slash = rest.find("@"), rest.find("/")
        if re.fullmatch(r"[A-Za-z0-9+.-]+", scheme) and at >= 0 and (slash < 0 or at < slash):
            url = scheme + "://" + rest[at + 1:]
    elif "@" in url:
        after = url[url.index("@") + 1:]
        colon, slash = url.find(":"), url.find("/")
        if ":" in after and not (0 <= slash < colon):
            url = after
    url = url.rstrip("/")
    return url[:-4] if url.endswith(".git") else url


def check_fetch_head(text, remote, branch, want):
    """The empty string where `text`, a `FETCH_HEAD`'s content, holds a line for `branch` fetched from
    the URL `want` spells, by `derive_fetch_url` of both sides; else the skip reason, `empty` or
    `no line for <branch> of <remote>` (TOOL-dDeclaredLoop-74 S1). An empty `want` keeps no file."""
    if not text.strip():
        return "empty"
    line = re.compile(r"[0-9a-f]{40,64}\t[^\t]*\tbranch '%s' of (.+)" % re.escape(branch))
    for ln in text.splitlines():
        m = line.fullmatch(ln)
        if m and want and derive_fetch_url(m.group(1)) == want:
            return ""
    return "no line for %s of %s" % (branch, remote)


def read_fetch_time(repo, remote, ref, branch):
    """`(at, source, skipped)` of the last fetch of `ref` (TOOL-dDeclaredLoop-65 S1, S2): the newest of
    the mtime of each `FETCH_HEAD` under the common git directory and its `worktrees/*/` that
    `check_fetch_head` keeps for `branch` of `remote` (TOOL-dDeclaredLoop-74 S1), source `FETCH_HEAD`,
    and the time of `ref`'s newest reflog entry, source `reflog`, the first listed on a tie; where none
    is read, the newest `clone: ` entry of `refs/heads/<branch>`'s reflog, source `clone`; else
    `(None, None, skipped)`. A file `os.stat` does not answer is passed over; `skipped` holds one
    `<name> · skipped — <reason>` entry per file the check skips, `<name>` its path under the common
    directory, `unreadable` where it does not open, and a skipped file's time is never read."""
    rc, out = read_git(repo, "rev-parse", "--git-common-dir")
    times, skipped, want = [], [], None
    if rc == 0 and out:
        common = pathlib.Path(repo) / out
        for f in [common / "FETCH_HEAD"] + sorted(common.glob("worktrees/*/FETCH_HEAD")):
            try:
                st = f.stat()
            except OSError:
                continue
            if want is None:  # one spawn per reading, only where a FETCH_HEAD exists
                rc, url = read_git(repo, "remote", "get-url", remote)
                want = derive_fetch_url(url) if rc == 0 else ""
            try:
                why = check_fetch_head(f.read_text(encoding="utf-8", errors="replace"), remote, branch, want)
            except OSError:
                why = "unreadable"
            if why:
                skipped.append("%s · skipped — %s" % (f.relative_to(common).as_posix(), why))
                continue
            times.append((st.st_mtime, "FETCH_HEAD"))
    rc, out = read_git(repo, "reflog", "show", "--date=unix", "-n1", "--format=%gd", ref)
    m = re.search(r"@\{(\d+)\}", out) if rc == 0 else None
    if m:
        times.append((int(m.group(1)), "reflog"))
    if not times:
        rc, out = read_git(repo, "reflog", "show", "--date=unix", "--format=%gd%x09%gs", "refs/heads/%s" % branch)
        for ln in out.splitlines() if rc == 0 else []:
            m = re.search(r"@\{(\d+)\}\t(.*)", ln)
            if m and m.group(2).startswith("clone: "):
                times.append((int(m.group(1)), "clone"))
                break
    if not times:
        return None, None, skipped
    at, source = max(times, key=lambda t: t[0])  # max keeps the first of equal times
    return datetime.datetime.fromtimestamp(at, datetime.timezone.utc), source, skipped


def read_remote_claim(repo, bound, now):
    """`(sha or None, entries, claim)` of the default branch's remote-tracking tip: the claim keyed over
    `<ref>@<sha>`, `at` its last fetch by `read_fetch_time`, judged `remote` against `bound`; `entries`
    the ref's `read` row, `<ref>@<sha8> · fetched <n>s ago · from <source>` or `<ref>@<sha8> · fetched
    never` (TOOL-dDeclaredLoop-65 S3), ` · core.logAllRefUpdates=false` after it where the repository's
    setting reads false (TOOL-dDeclaredLoop-75 S34), the bare ref where the claim is None, then each skipped
    `FETCH_HEAD`'s entry (TOOL-dDeclaredLoop-74 S2). The claim is None where the remote
    reads absent (TOOL-dDeclaredLoop-56 S36): the ladder names no remote and refuses nothing, or the
    tracking ref of its default branch does not resolve. A ladder refusal keeps the claim."""
    remote, branch, _observed, refusal = resolve_remote(repo)
    ref = "refs/remotes/%s/%s" % (remote, branch) if remote and branch else "refs/remotes/?"
    sha, at, entry = None, None, ref
    if remote and branch:
        rc, out = read_git(repo, "rev-parse", "-q", "--verify", "%s^{commit}" % ref)
        sha = out if rc == 0 and out else None
    if not refusal and not sha:
        return None, [ref], None
    skipped = []
    if sha:
        at, fetched, skipped = read_fetch_time(repo, remote, ref, branch)
        entry = "%s@%s · %s" % (ref, sha[:8], "fetched %ds ago · from %s" % (
            max(0, int((now - at).total_seconds())), fetched) if at else "fetched never")
        if not at:   # TOOL-dDeclaredLoop-75 S34: the setting that leaves no reflog to read, named
            rc, out = read_git(repo, "config", "--type=bool", "--get", "core.logAllRefUpdates")
            entry += " · core.logAllRefUpdates=false" if rc == 0 and out == "false" else ""
    source = "%s@%s" % (ref, sha or "?")
    key = derive_claim_key([source])
    verdict = derive_claim_verdict(key, key, "remote", at, now, bound)
    return sha, [entry] + skipped, {"name": "remote tip %s" % ref, "key": key, "verdict": verdict}


def check_is_ancestor(repo, sha, tip):
    """Whether `tip` contains `sha`."""
    return bool(sha and tip) and read_git(repo, "merge-base", "--is-ancestor", sha, tip)[0] == 0


# ------------------------------------------------------------------------------------------ the derivation
def derive_instance_key(item, pass_id, inputs):
    """`<item tag>@<pass>#<inputs>`, `<inputs>` the first eight hex digits of the SHA-1 of the ids the
    witness read, sorted and NUL-joined."""
    raw = b"\0".join(sorted(str(i).encode("utf-8") for i in inputs))
    return "%s@%s#%s" % (item, pass_id, hashlib.sha1(raw).hexdigest()[:8])


def derive_unit_step(word, passes, records, gates_tip, remote_sha, repo, armed=True):
    """`(step, pass commit or None, unarmed)` of one unit: `word` its hand-over state, `passes` the pass
    commits attributed to it newest first, `records` the acceptance records naming it, malformed ones
    included. Unless `armed`, a unit no record names stands on its newest pass commit and `unarmed` is
    true (TOOL-dDeclaredLoop-45); a unit a record names is read as when armed."""
    m = re.fullmatch(r"DONE \((.+)\)", word)
    grade = m.group(1) if m else ("READY" if word == "DONE" else word)
    if grade != "READY":
        return "none", None, False
    unarmed = not armed and not records and bool(passes)
    held = passes if unarmed else [p for p in passes if any(not r["malformed"] and r.get("Sha") == p for r in records)]
    if not held:
        return "designed", None, False
    if not check_is_ancestor(repo, held[0], gates_tip):
        return "built", held[0], unarmed
    if not check_is_ancestor(repo, held[0], remote_sha):
        return "tested", held[0], unarmed
    return "deployed", held[0], unarmed


def derive_frontier(items, witnessed, unheld, unit_id, head):
    """The rows of `items`, the build's step's in composition order, whose tag is not in `witnessed`
    and each of whose needs is met by a tag in `witnessed`, a list entry by any one of its tags; each
    entry as `next` is. `witnessed` maps each held tag to its witness's inputs and `unheld` each tag
    read and not held to its own, so an unread tag is in neither and meets no need."""
    out = []
    for row in items:
        tag = row.get("tag")
        if tag in witnessed:
            continue
        if all(any(t in witnessed for t in (n if isinstance(n, list) else [n])) for n in row.get("needs") or []):
            out.append({"item": tag, "unit": unit_id, "actor": row.get("actor", "?"),
                        "key": derive_instance_key(tag, unit_id, unheld.get(tag) or [head])})
    return out


def derive_next_item(step_items, read_witness, unit_id, head):
    """`(next item or None, claims, frontier)`: the frontier's first entry, a claim per item read,
    `evidence` for an unread witness, and the frontier `derive_frontier` returns."""
    claims, witnessed, unheld = [], {}, {}
    for row in step_items:
        tag = row.get("tag")
        held, inputs = read_witness(tag)
        if held is None:
            claims.append({"name": tag, "key": derive_claim_key(["item=%s" % tag]),
                           "verdict": derive_claim_verdict(derive_claim_key(["item=%s" % tag]), None, "history",
                                                           None, None, None)})
        elif held:
            sources = ["commit=%s" % i for i in inputs]
            key = derive_claim_key(sources)
            claims.append({"name": derive_instance_key(tag, unit_id, inputs), "key": key,
                           "verdict": derive_claim_verdict(key, key, "history", None, None, None)})
    tags = [row.get("tag") for row in step_items]
    for row in step_items:
        tags += [t for n in row.get("needs") or [] for t in (n if isinstance(n, list) else [n])]
    for tag in dict.fromkeys(tags):
        held, inputs = read_witness(tag)
        if held:
            witnessed[tag] = inputs
        elif held is not None:
            unheld[tag] = inputs
    frontier = derive_frontier(step_items, witnessed, unheld, unit_id, head)
    return (frontier[0] if frontier else None), claims, frontier


def check_refusal(tag, key, tags):
    """`(held, why)`: whether a refusal row may name `tag` at `key`, `tag` one of the composed `tags`
    and `key` `<tag>@<round|pass>#<inputs>`, `<inputs>` eight lowercase hex digits, as
    `derive_instance_key` writes it."""
    if tag not in tags:
        return False, "the item %s is no tag the composition declares" % tag
    if not re.fullmatch(re.escape(tag) + r"@[^\s@#]+#[0-9a-f]{8}", key):
        return False, "the key %s is not %s's instance shape <tag>@<round|pass>#<eight hex digits>" % (key, tag)
    return True, ""


def read_refusals(text):
    """The `refusal` rows of the run-state `text`, through runlog's `read_run_state`, found by
    `resolve_kit_dir`; one `{"unarmed": why}` entry where that kit does not resolve."""
    try:
        path = resolve_kit_dir("runlog", "model.py", KIT) / "model.py"
        spec = importlib.util.spec_from_file_location("runlog_model", str(path))
        model = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = model  # its dataclasses look their module up by name
        spec.loader.exec_module(model)
    except (LookupError, OSError, ImportError, SyntaxError, AttributeError) as e:
        sys.modules.pop("runlog_model", None)
        return [{"unarmed": "runlog's model does not load beside this kit: %s" % (str(e) or type(e).__name__)}]
    record, _state = model.read_run_state(text)
    return [{"item": r["item"], "key": r["step"] or "", "reason": r["reason"],
             "at": datetime.datetime.fromtimestamp(r["t"], datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
             if r["t"] is not None else ""}
            for r in record["rows"] if r["kind"] == "refusal"]


def derive_interrupts(text, handover, owed, parents_open, claims, now, remote_absent=False):
    """The interrupts in `[position]`'s order: owner decisions, the mailbox, invalidated witnesses, an
    absent remote, dependency gates, the undecided ask. `text` is the run-state file's text, `owed` the
    policy kit's `read_run_fact` where that file exists, `parents_open` the parents not landed,
    `remote_absent` the remote reading absent, `remote · none` (TOOL-dDeclaredLoop-56 S36)."""
    out = []
    kinds, acts = handover["owed"]
    for ln in text.splitlines():
        m = PARKED_ROW.match(ln.rstrip("\r"))
        if m and (m.group(1) in kinds or (m.group(1) == "rescope" and m.group(2) in acts)):
            out.append({"kind": "owner-decision", "subject": "%s · item %s" % m.groups()})
    code = owed(text, "hold-code") if owed else None
    until = (owed(text, "hold-until") or "") if owed else ""
    if code:
        m = re.fullmatch(r"after (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)", until.strip())
        passed = bool(m) and now >= datetime.datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=datetime.timezone.utc)
        if not passed:
            out.append({"kind": "owner-decision", "subject": "hold %s · until %s" % (code, until or "-")})
    out.append({"kind": "mailbox", "subject": "unarmed"})
    out += [{"kind": "invalidated", "subject": c["name"]} for c in claims if c["verdict"] == "re-derived"]
    out += [{"kind": "remote", "subject": "none"}] if remote_absent else []
    out += [{"kind": "dependency", "subject": p} for p in parents_open]
    if handover["ask"]:
        out.append({"kind": "ask", "subject": handover["ask"]})
    return out


def derive_answer(pos, terminal, remote_fresh, every_deployed, nxt, exit_item):
    """`(answer, reason)` by §4's precedence, invalid-input already decided by the caller."""
    kinds = [i["kind"] for i in pos["interrupts"]]
    ask = next((i["subject"] for i in pos["interrupts"] if i["kind"] == "ask"), None)
    if not remote_fresh:
        return "stale-remote", "the default branch's remote-tracking tip is unread or older than its bound"
    if pos["state"] in terminal:
        return "terminal", "the build's state %s is terminal" % pos["state"]
    if every_deployed and not ask:
        return "terminal", "every unit is past its last step"
    if "owner-decision" in kinds:
        return "awaiting", "an owner decision: %s" % next(i["subject"] for i in pos["interrupts"]
                                                          if i["kind"] == "owner-decision")
    if "dependency" in kinds:
        return "blocked", "the parent %s has not landed" % " ".join(
            i["subject"] for i in pos["interrupts"] if i["kind"] == "dependency")
    if nxt:
        return "act", "%s for %s" % (nxt["item"], nxt["unit"])
    if ask:
        return "awaiting", "the undecided ask %s" % ask
    return "stuck", "no item of %s can run and its exit %s is unwitnessed" % (pos["build_step"], exit_item or "-")


def derive_position(repo, slug, definition=None):
    """The `Position` of build `slug` in the repository at `repo` (§4 Data model). `definition`, where
    given, is a parsed definition read instead of the shipped one and the composition."""
    repo = pathlib.Path(repo).absolute()
    pos = {"slug": slug, "state": "none", "build_step": NO_STEP, "units": [], "next": None, "frontier": [],
           "refusals": [], "interrupts": [], "answer": "invalid-input", "reason": "", "read": [], "claims": [],
           "witnesses": {}, "undeclared": {}}
    try:
        derive_position_into(pos, repo, slug, definition)
    except (LoopError, ValueError, OSError, LookupError, KeyError, subprocess.SubprocessError) as e:
        pos.update(answer="invalid-input", reason=str(e) or type(e).__name__)
    return pos


def derive_item_boundary(repo, slug, pointer, pos=None):
    """I12 (KICK-dKeptSession-13 S1): the build's current item where it differs from `pointer`, else
    None. `pos` is a position the caller already derived, else one is derived here. The current item is
    the `act` answer's `next.key`, `none` for every other answer but `KEPT_ANSWERS`, which keep `pointer`."""
    pos = derive_position(repo, slug) if pos is None else pos
    if pos["answer"] in KEPT_ANSWERS:
        return None
    current = pos["next"]["key"] if pos["answer"] == "act" and pos["next"] else "none"
    return current if current != (pointer or "none") else None


def render_boundary_lines(pos, pointer):
    """`--boundary`'s two lines over one position: the crossing or its absence, then the `forked —`
    line, the units its hand-over grades FORKED."""
    to = derive_item_boundary(None, pos["slug"], pointer, pos)
    if to is not None:
        lines = ["boundary — %s → %s" % (pointer, to)]
    else:
        kept = " · %s" % pos["answer"] if pos["answer"] in KEPT_ANSWERS else ""
        lines = ["boundary — none crossed · item %s%s" % (pointer, kept)]
    forked = [u["id"] for u in pos["units"] if u.get("state") == "FORKED"]
    return lines + ["forked — %s" % (" · ".join(forked) or "none")]


def read_build_items(repo, slug, moves, pin, read=None):
    """The composed item rows build `slug` reads at the pin `pin`, `moves` its moves newest first: the
    composition there joined with the item rows the newest move's scenarios activate at the same pin
    (TOOL-dDeclaredLoop-27), then the build's own applied changes, its last layer (TOOL-dDeclaredLoop-28);
    gov's own rows where the composition is unarmed. `read`, where given, gains the scenario's read line.
    The position engine and the termination check both read it (TOOL-dDeclaredLoop-33)."""
    placed = moves[0].get("scenario") if moves else None
    activated = read_activated_rows(repo, pin, placed.split("+")).get("kind.item", []) if placed else []
    if placed and read is not None:
        read.append("scenario=%s · %d activated" % (placed, len(activated)))
    from adapt import read_flow_layer   # it imports loop_transition, as this module does, so here
    layer = read_flow_layer(repo, slug, "item")
    return read_composed_items(repo, pin, (activated + layer) or None)


def derive_position_into(pos, repo, slug, definition):
    """The body of `derive_position`, raising on any refused read."""
    read_memory_tree("gen_build_index.py")
    from build_records import read_acceptance, read_records
    from commit_trailers import derive_attribution, read_commits
    from gen_build_index import Problem, parse_front_matter
    now = datetime.datetime.now(datetime.timezone.utc)
    root = resolve_memory_root(repo)
    builds = repo / root / "builds"
    folder = builds / slug
    if not (folder / "README.md").is_file():
        raise ValueError("the slug %s names no build README under %s" % (slug, builds.as_posix()))
    try:
        fm = parse_front_matter(str(folder / "README.md"), slug)
    except Problem as e:
        raise ValueError("the build README does not parse: %s" % e) from None
    pos["read"].append("%s@%s" % ((folder / "README.md").relative_to(repo).as_posix(), read_blob_id(folder / "README.md")))
    handover = read_handover(repo, slug)
    moves = read_transitions(slug, repo)
    pin, pin_state = read_step_composition(repo, moves)
    pos["read"].append("composition@%s · %s" % (pin[:8], pin_state))
    if definition is None:
        data, where = read_definition(KIT)
        items = read_build_items(repo, slug, moves, pin, pos["read"])
    else:
        data, where = definition, "the caller's definition"
        items = read_item_rows(data, where)
    tables = read_transition_rows(data, where)
    armed = not any(r["name"] == "acceptance" and ROUTE_STAND_IN.fullmatch(r["writer"])
                    for r in check_computed_witnesses(data, where))
    steps = {r["tag"]: r for r in data["step"]}
    item_step = {r.get("tag"): r.get("step") for r in items}
    for m in moves:
        if not check_recorded_move(m, tables):
            raise ValueError("the recorded move %s -> %s on %s at %s is held by no build row" % (
                m.get("from"), m.get("to"), m.get("item"), str(m.get("commit"))[:8]))
    pos["state"] = moves[0]["to"] if moves else "none"
    rc, head = read_git(repo, "rev-parse", "HEAD")
    if rc != 0:
        raise ValueError("HEAD names no commit in %s" % repo.as_posix())
    pos["read"].append("HEAD@%s" % head[:8])
    passes = {}
    for c in read_commits(str(repo), ["--first-parent", "HEAD"], ["Pass"]):
        for uid in derive_attribution(c, "replace", UNIT_ID):
            passes.setdefault(uid, []).append(c["sha"])
    records = {}
    for r in read_records(repo, {"MEMORY_ROOT": root}, "acceptance", read_acceptance):
        if r["build"] == slug:
            records.setdefault(r.get("Caused-by", "").strip("`"), []).append(r)
            if not r["malformed"]:
                pos["read"].append("%s@%s" % (r["path"], read_blob_id(repo / r["path"])))
    run = folder / "RUN.md"
    text, owed = "", None
    if run.is_file():
        text = run.read_bytes().decode("utf-8", "replace")
        pos["read"].append("%s@%s" % (run.relative_to(repo).as_posix(), read_blob_id(run)))
        owed = read_policy_kit()[1].read_run_fact
        pos["refusals"] = read_refusals(text)
    gates = (owed(text, "gates-run") or "").split() if owed else []
    gates_tip = None
    if len(gates) == 2:
        rc, out = read_git(repo, "rev-parse", "-q", "--verify", "%s^{commit}" % gates[1])
        gates_tip = out if rc == 0 else None
    remote_sha, remote_read, remote_claim = read_remote_claim(repo, handover["bound"], now)
    if remote_sha:
        pos["read"].extend(remote_read)
    if remote_claim:
        pos["claims"].append(remote_claim)
    order = ["none"] + list(tables["states"].get("unit", []))
    units, pass_of = [], {}
    for uid, word in handover["units"]:
        step, sha, unarmed = derive_unit_step(word, passes.get(uid, []), records.get(uid, []), gates_tip,
                                              remote_sha, repo, armed)
        units.append({"id": uid, "step": step, "state": word, "unarmed": unarmed})
        pass_of[uid] = sha
    pos["units"] = units
    if not units and not handover["ask"]:
        raise ValueError(NOTHING_GRADED)
    forward = {}
    for row in tables["transition"]:
        if row.get("level") != "unit":
            continue
        for s in derive_from_states(row, tables["states"].get("unit", [])):
            if s in order[:-1] and row.get("to") == order[order.index(s) + 1]:
                forward.setdefault(s, row)
    least = min(units, key=lambda u: order.index(u["step"])) if units else None
    every_deployed = all(u["step"] == order[-1] for u in units)
    if least and least["step"] in forward:
        pos["build_step"] = item_step.get(forward[least["step"]]["item"], NO_STEP)
    exit_item = steps[pos["build_step"]]["exit"] if pos["build_step"] in steps else None
    named = {}
    for m in moves:
        named.setdefault(m.get("item"), m.get("commit"))
    named = derive_carried_witnesses(repo, named, set(item_step))
    exits = {r["exit"]: r["state"] for r in data["step"]}
    unit_items = {row["item"]: row["to"] for row in forward.values()}

    def read_witness(tag):
        """`(held, inputs)` of one item: held None where no reader exists for it."""
        if tag in unit_items and least:
            sha = pass_of.get(least["id"])
            return order.index(least["step"]) >= order.index(unit_items[tag]), [sha] if sha else []
        if tag in exits:
            out = [m["commit"] for m in moves if m.get("from") == exits[tag] != m.get("to")]
            return bool(out), out[:1]
        if tag in named:
            return True, [named[tag]]
        return None, []

    nxt, item_claims, frontier = (None, [], [])
    if least and pos["build_step"] != NO_STEP:
        nxt, item_claims, frontier = derive_next_item([r for r in items if r.get("step") == pos["build_step"]],
                                                      read_witness, least["id"], head)
    pos["next"], pos["frontier"] = nxt, frontier
    pos["claims"] += item_claims
    # the walked path's two reads (TOOL-dDeclaredLoop-28): each item of the step as the engine reads its
    # witness, and each tag a recorded move names that the composition at the pin lacks, with the states
    # the moves naming it left
    if least and pos["build_step"] != NO_STEP:
        for r in items:
            if r.get("step") == pos["build_step"]:
                held = read_witness(r.get("tag"))[0]
                pos["witnesses"][r.get("tag")] = "unread" if held is None else "held" if held else "unheld"
    for m in moves:
        if m.get("item") and m["item"] not in item_step:
            pos["undeclared"].setdefault(m["item"], [])
            if m.get("from") and m["from"] not in pos["undeclared"][m["item"]]:
                pos["undeclared"][m["item"]].append(m["from"])
    parents_open = []
    for p in (fm.get("parents") or "").split():
        landed = handover["parents"].get(p) == "LANDED"
        if not landed and (builds / p).is_dir():
            landed = bool((read_transitions(p, repo) or [{}])[0].get("to") == "landed")
        if not landed:
            parents_open.append(p)
    pos["interrupts"] = derive_interrupts(text, handover, owed, parents_open, pos["claims"], now, remote_claim is None)
    pos["answer"], pos["reason"] = derive_answer(pos, tables["terminal"],
                                                 remote_claim is None or remote_claim["verdict"] == "fresh",
                                                 every_deployed and bool(units), nxt, exit_item)


# ------------------------------------------------------------------------------------------ the output
def render_next_line(pos):
    """The `next:` shape `--plan` prints for a position (§4 "The `next:` line")."""
    ask = next((i["subject"] for i in pos["interrupts"] if i["kind"] == "ask"), None)
    owner = any(i["kind"] == "owner-decision" for i in pos["interrupts"])
    answer = pos["answer"]
    if answer == "act" and pos["next"]:
        unit = next(u for u in pos["units"] if u["id"] == pos["next"]["unit"])
        if unit["step"] in ("built", "tested"):
            return NEXT_SHAPES["undecided-ask"].replace("<id>", ask) if ask else NEXT_SHAPES["everything-terminal"]
        if unit["state"] == "MISSING":
            return NEXT_SHAPES["missing-unit"].replace("<id>", unit["id"])
        if unit["state"] in ("READY", "DONE"):
            return NEXT_SHAPES["live-unit"].replace("<id>", unit["id"])
        m = re.fullmatch(r"DONE \((.+)\)", unit["state"])
        return NEXT_SHAPES["live-state"].replace("<id>", unit["id"]).replace("<state>", m.group(1) if m else unit["state"])
    if answer == "invalid-input" and pos["reason"] == NOTHING_GRADED:
        return NEXT_SHAPES["nothing-graded"]
    if answer == "terminal":
        return NEXT_SHAPES["everything-terminal"]
    if answer == "awaiting" and ask and not owner:
        return NEXT_SHAPES["undecided-ask"].replace("<id>", ask)
    return NEXT_SHAPES["other"].replace("<answer>", answer).replace("<reason>", pos["reason"])


def render_position_lines(pos):
    """The line output (§4 Line output)."""
    lines = ["position — %s · state %s · step %s · answer %s · %s" % (
        pos["slug"], pos["state"], pos["build_step"], pos["answer"], pos["reason"])]
    lines += ["unit — %s · %s%s" % (u["id"], u["step"], " · acceptance unarmed" if u.get("unarmed") else "")
              for u in pos["units"]]
    if pos["next"]:
        n = pos["next"]
        lines.append("next — %s · unit %s · actor %s · key %s" % (n["item"], n["unit"], n["actor"], n["key"]))
    lines.append("frontier — %s" % (" · ".join(f["item"] for f in pos["frontier"]) or "none"))
    lines += ["refusal — unarmed · %s" % r["unarmed"] if "unarmed" in r else
              "refusal — %s · %s · %s" % (r["item"], r["key"], r["reason"]) for r in pos["refusals"]]
    lines += ["interrupt — %s · %s" % (i["kind"], i["subject"]) for i in pos["interrupts"]]
    lines += ["read — %s" % r for r in pos["read"]]
    lines += ["claim — %s · key %s · %s" % (c["name"], c["key"], c["verdict"]) for c in pos["claims"]]
    return lines


# ------------------------------------------------------------------------------------------ the fixture
def render_spec(uid, status):
    """A fixture spec the driver's M2 classifier grades READY."""
    return ("# %s — a unit\n\n**Status:** %s · rev-1 · 2026-01-01 · node a · Tier-2 · base abcdef12 · streams tooling\n\n"
            "## 1. Goal\ng\n## 2. Scope (IN)\n- S1 a thing\n## 3. Non-goals (OUT)\nn\n## 4. Design\nd\n"
            "## 5. Production-readiness checklist\nc\n## 6. Acceptance criteria\n- AC1 it works\n## 7. Gates\n"
            "the bar\n## 8. Open questions\nnone\n## 9. Revision log\n- rev-1\n## 10. Reuse audit\nr\n" % (uid, status))


def render_handover(units, ask=None, parents=None):
    """The hand-over text a fixture plants where the driver does not run."""
    lines = ["bound\t%d" % FX_BOUND, "owed\t%s\t%s" % FX_OWED] + ["unit\t%s\t%s" % u for u in units]
    lines += ["ask\t%s" % ask] if ask else []
    lines += ["parent\t%s\t%s" % p for p in (parents or {}).items()]
    return "\n".join(lines) + "\n"


def write_position_plant(top, case, root):
    """The scratch repository `top/r` for `case`, with its bare remote `top/o.git` where it has one,
    and the clone `top/c` of that remote as the repository for `fresh-clone`, `offline-stale` and
    `clone-without-reflog`;
    `(repo, definition, handover)`."""
    repo = top / "r"
    repo.mkdir()
    ids = FX_IDS[:2] if case in ("typed-status", "bar-wait") or case.startswith("built-") else FX_IDS
    extra = "parents: tPar\n" if case == "parent-unlanded" else ""
    rows = "".join("| [%s — u](spec/2026-01-01-spec-%s.md) | INPROGRESS | rev-1 | 2026-01-01 |\n" % (u, u) for u in ids)
    files = {".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\n',
             "memory/builds/%s/README.md" % FX_SLUG:
                 "---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\nroster: TOOL\nids: %s\n%s---\n\n# %s\n\n"
                 "<!-- gen:build-index -->\n**Build status:** OPEN · %d unit(s)\n\n<!-- gen:build-units -->\n"
                 "| Unit | Status | Rev | Last change |\n|---|---|---|---|\n%s<!-- /gen:build-units -->\n"
                 "<!-- /gen:build-index -->\n" % (FX_SLUG, " ".join(ids), extra, FX_SLUG, len(ids), rows)}
    for n, uid in enumerate(ids):
        status = "CLOSED" if case == "typed-status" and n == 1 else "INPROGRESS"
        files["memory/builds/%s/spec/2026-01-01-spec-%s.md" % (FX_SLUG, uid)] = render_spec(uid, status)
    if case == "parent-unlanded":
        files["memory/builds/tPar/README.md"] = "---\nslug: tPar\nnode: a\nopened: 2026-01-01\nstreams: tooling\n---\n# tPar\n"
    if case in FX_DRIVER:
        for name in (".unattended.conf", ".memory-tree.conf"):
            if not (root / name).is_file():
                raise LookupError("the driver plant copies %s from %s, which holds none" % (name, root.as_posix()))
            shutil.copyfile(root / name, repo / name)
        files.pop(".memory-tree.conf")
    run_fixture_git(repo, "init", "-q", "--template=", "-b", "main")
    write_fixture_files(repo, files)
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "fixture")
    remote = None if case == "no-remote" else top / "o.git"
    if remote:
        run_fixture_git(top, "init", "-q", "--bare", "--template=", str(remote))
        run_fixture_git(repo, "remote", "add", "origin", str(remote))
    fx = run_fixture_git(repo, "remote")   # the fixture remote's name read back from git, never spelled

    def write_pass(uid, record=True):
        """One pass commit for `uid` and, where `record`, the acceptance record naming it; the pass
        commit's sha."""
        write_fixture_files(repo, {"work/%s.txt" % uid: uid + "\n"})
        run_fixture_git(repo, "add", "-A")
        run_fixture_git(repo, "commit", "-q", "-m", "feat: %s\n\nPass: %s" % (uid, uid))
        sha = run_fixture_git(repo, "rev-parse", "HEAD")
        if not record:
            return sha
        read_memory_tree("build_records.py")
        from build_records import write_acceptance
        write_acceptance(repo, FX_SLUG, uid, sha, "stand-in", [("true", 0, "0" * 12)], today="2026-01-01")
        run_fixture_git(repo, "add", "-A")
        run_fixture_git(repo, "commit", "-q", "-m", "records: %s acceptance\n\nPass: none" % uid)
        return sha

    def write_move(src, to, item):
        """One recorded move, a commit carrying its `Gov-Transition` trailer."""
        head = run_fixture_git(repo, "rev-parse", "HEAD")
        run_fixture_git(repo, "commit", "-q", "--allow-empty", "-m", "move\n\nGov-Transition: %s -> %s · build=%s · item=%s · sha=%s" % (
            src, to, FX_SLUG, item, head[:8]))

    run_facts = "# %s run\n\n## Run facts\nphase: BUILDING\nbase: %s\nwitness: %s\nmode: slug\n" % (
        FX_SLUG, "0" * 40, "0" * 40)
    if case in ("steps", "plan-line", "status-line"):
        write_pass(FX_IDS[0])
        tip = run_fixture_git(repo, "rev-parse", "HEAD")
        run_facts += "gates-run: bar-1 %s\n" % tip[:8]
        run_fixture_git(repo, "push", "-q", fx, "main")
        write_pass(FX_IDS[1])
    elif case == "bar-wait":
        for uid in ids:
            write_pass(uid)
    elif case.startswith("built-"):
        unattributed = run_fixture_git(repo, "rev-parse", "HEAD")  # the `fixture` commit names no unit
        if case == "built-unarmed":   # TOOL-dDeclaredLoop-67 S50: B tested, ahead of A, so A is the least advanced
            run_fixture_git(repo, "push", "-q", fx, "main")
            write_pass(FX_IDS[1])
            run_facts += "gates-run: bar-1 %s\n" % run_fixture_git(repo, "rev-parse", "HEAD")[:8]
        write_pass(FX_IDS[0], record=False)
        if case == "built-unheld":
            read_memory_tree("build_records.py")
            from build_records import write_acceptance
            write_acceptance(repo, FX_SLUG, FX_IDS[0], unattributed, "stand-in", [("true", 0, "0" * 12)],
                             today="2026-01-01")
    elif case in ("idempotent", "frontier-chain", "frontier-none"):
        write_move("building", "building", FX_A)
    elif case == "terminal":
        write_move("deploying", "landed", "item.deploy.close")
    elif case == "bad-transition":
        write_move("planning", "landed", "item.plan.input")
    if case == "owner-decision":
        run_facts += "\n## Parked\n\n2026-01-01T00:00:00Z decision · item which-way · reason the fixture's owed decision\n"
    write_fixture_files(repo, {"memory/builds/%s/RUN.md" % FX_SLUG: run_facts})
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "run state")
    if remote and case not in ("steps", "plan-line", "status-line", "built-unarmed"):
        run_fixture_git(repo, "push", "-q", fx, "main")
    if remote:
        run_fixture_git(repo, "remote", "set-head", fx, "main")
    if case in ("stale-remote", "quiet-remote", "failed-fetch", "fetch-other-branch", "scp-remote", "ssh-userinfo-remote",
                "url-forms"):  # the tracking tip kept, its one reflog entry dated 2000-01-01, past any bound
        tip = run_fixture_git(repo, "rev-parse", "refs/remotes/%s/main" % fx)
        run_fixture_git(repo, "update-ref", "-d", "refs/remotes/%s/main" % fx)
        rc, out = read_git(repo, "update-ref", "--create-reflog", "-m", "aged", "refs/remotes/%s/main" % fx, tip,
                           env=read_clean_env(GIT_COMMITTER_NAME="fx", GIT_COMMITTER_EMAIL="fx@example.invalid",
                                              GIT_COMMITTER_DATE="946684800 +0000"))
        if rc:
            raise subprocess.CalledProcessError(rc, "git update-ref", out)
    if case == "quiet-remote":  # a fetch from a linked worktree, which moves nothing and writes its own FETCH_HEAD
        run_fixture_git(repo, "worktree", "add", "-q", "--detach", str(top / "w"))
        run_fixture_git(top / "w", "fetch", "-q", fx)
    if case == "failed-fetch":  # a fetch from a path that does not exist, which leaves FETCH_HEAD at 0 bytes
        run_fixture_git(repo, "remote", "set-url", fx, str(top / "gone.git"))
        rc, out = read_git(repo, "fetch", "-q", fx)
        if rc == 0:
            raise subprocess.CalledProcessError(rc, "git fetch from a path that does not exist exited 0", out)
    if case == "fetch-other-branch":  # TOOL-dDeclaredLoop-75 S12: a FETCH_HEAD holding another branch's line alone
        run_fixture_git(repo, "push", "-q", fx, "HEAD:refs/heads/other")
        run_fixture_git(repo, "fetch", "-q", fx, "other")
    if case in ("scp-remote", "ssh-userinfo-remote"):  # TOOL-dDeclaredLoop-77 S2: a user-part URL fetched over a shim
        shim = top / "ssh-shim.sh"  # sh strips a Windows path's backslashes, so both paths reach it as_posix
        write_fixture_files(top, {shim.name: "exec git-upload-pack '%s'\n" % remote.as_posix()})
        url = "git@example.com:up.git" if case == "scp-remote" else "ssh://user@example.com/up.git"
        run_fixture_git(repo, "remote", "set-url", fx, url)
        rc, out = read_git(repo, "fetch", "-q", fx, env=read_clean_env(GIT_SSH_COMMAND="sh '%s'" % shim.as_posix()))
        if rc:
            raise subprocess.CalledProcessError(rc, "git fetch over the ssh shim", out)
    if case == "url-forms":  # TOOL-dDeclaredLoop-77 S4: a URL carrying a password, its fetch failing at connect
        run_fixture_git(repo, "remote", "set-url", fx, "https://u:SECRET@127.0.0.1:9/r.git")
        # TOOL-dDeclaredLoop-86 S9: no credential helper runs and nothing prompts, so no store entry is written
        rc, out = read_git(repo, "-c", "credential.helper=", "fetch", "-q", fx,
                           env=read_clean_env(GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never"))
        if rc == 0:
            raise subprocess.CalledProcessError(rc, "git fetch from port 9 exited 0", out)
    if case in ("fresh-clone", "offline-stale", "clone-without-reflog"):  # the engine reads the clone, whose remote's HEAD names main
        run_fixture_git(remote, "symbolic-ref", "HEAD", "refs/heads/main")
        # TOOL-dDeclaredLoop-75 S34: a clone that writes no reflog, so no time is read
        unlogged = ["-c", "core.logAllRefUpdates=false"] if case == "clone-without-reflog" else []
        run_fixture_git(top, "clone", "-q", "--template=", *unlogged, str(remote), str(top / "c"))
        repo = top / "c"
    if case == "offline-stale":  # a fetch that moves nothing, its FETCH_HEAD dated back by twice the bound
        run_fixture_git(repo, "fetch", "-q", fx)
        aged = datetime.datetime.now().timestamp() - 2 * FX_BOUND
        os.utime(repo / ".git" / "FETCH_HEAD", (aged, aged))
    definition = None
    data = copy.deepcopy(read_definition(KIT)[0])
    if case in ("idempotent", "frontier-chain", "frontier-none"):
        data["transition"].append({"level": "build", "from": ["building"], "item": FX_A,
                                   "outcome": "pinned", "to": "building", "witness": "the fixture's move"})
    if case == "deadlock":
        next(r for r in data["item"] if r.get("tag") == FX_A)["needs"] = [FX_D]
    if case == "frontier-parallel":
        next(r for r in data["item"] if r.get("tag") == FX_B)["needs"] = []
    if case == "frontier-none":
        # The step's unit-forward item stays, so the build's step is still step.build, its need unmet.
        data["item"] = [r for r in data["item"] if r.get("step") != "step.build" or r.get("tag") in (FX_A, FX_UNIT)]
        next(r for r in data["item"] if r.get("tag") == FX_UNIT)["needs"] = [FX_D]
    if case == "built-armed":
        next(r for r in data["computed-witness"] if r["name"] == "acceptance")["writer"] = "executor:build.acceptance"
    if case not in ("plan-line", "status-line"):
        definition = data
    words = {"typed-status": ["READY", "DONE"]}.get(case, ["READY"] * len(ids))
    handover = render_handover(list(zip(ids, words)), parents={"tPar": "RUNNING"} if case == "parent-unlanded" else None)
    return repo, definition, handover


def run_driver(repo, *argv):
    """`(output, exit)` of the unattended driver for `argv` in `repo`, with no hand-over inherited."""
    driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
    bash = resolve_bash(driver)
    if bash is None:
        raise LookupError("no bash can run %s" % driver.as_posix())
    env = {k: v for k, v in os.environ.items() if k not in (HANDOVER, "GOV_DEFAULT_BRANCH")}
    p = subprocess.run([bash, str(driver), *argv], cwd=str(repo), capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env, timeout=900)
    return p.stdout + p.stderr, p.returncode


def derive_plant_position(repo, definition, handover):
    """`derive_position` over a plant, its hand-over set in this process for the one call."""
    before = os.environ.get(HANDOVER)
    os.environ[HANDOVER] = handover or ""
    try:
        return derive_position(repo, FX_SLUG, definition)
    finally:
        if before is None:
            os.environ.pop(HANDOVER, None)
        else:
            os.environ[HANDOVER] = before


def check_plan_line(repo):
    """The `plan-line` case's misses: the driver's `next:` line against `render_next_line`, in the
    `steps` state, beside an undecided ask, and once every unit is deployed beside it."""
    misses = []
    readme = repo / ("memory/builds/%s/README.md" % FX_SLUG)

    def check_state(label, want):
        out = run_driver(repo, "--plan", FX_SLUG)[0]
        line = next((ln[len("next: "):] for ln in out.splitlines() if ln.startswith("next: ")), None)
        mine = render_next_line(derive_plant_position(repo, None, ""))
        print("%s: fixture · plan-line %s · driver %r · engine %r" % (SAY, label, line, mine))
        if line != mine or not mine.startswith(want):
            misses.append("%s: driver %r, engine %r, owed %r" % (label, line, mine, want))

    check_state("steps", "%s (READY - build it)" % FX_IDS[2])
    text = readme.read_text(encoding="utf-8").replace("slug: %s\n" % FX_SLUG, "slug: %s\nasks: %s\n" % (FX_SLUG, FX_ASK), 1)
    write_fixture_files(repo, {readme.relative_to(repo).as_posix(): text})
    run_fixture_git(repo, "commit", "-q", "-am", "an undecided ask")
    check_state("ask beside READY", "%s (READY - build it)" % FX_IDS[2])
    write_fixture_files(repo, {"work/%s.txt" % FX_IDS[2]: "w\n"})
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "feat: 3\n\nPass: %s" % FX_IDS[2])
    sha = run_fixture_git(repo, "rev-parse", "HEAD")
    read_memory_tree("build_records.py")
    from build_records import write_acceptance
    write_acceptance(repo, FX_SLUG, FX_IDS[2], sha, "stand-in", [("true", 0, "0" * 12)], today="2026-01-01")
    run_path = repo / ("memory/builds/%s/RUN.md" % FX_SLUG)
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "records\n\nPass: none")
    tip = run_fixture_git(repo, "rev-parse", "HEAD")
    text = re.sub(r"gates-run: .*", "gates-run: bar-2 %s" % tip[:8], run_path.read_text(encoding="utf-8"))
    write_fixture_files(repo, {run_path.relative_to(repo).as_posix(): text})
    run_fixture_git(repo, "commit", "-q", "-am", "the bar's fact")
    run_fixture_git(repo, "push", "-q", run_fixture_git(repo, "remote"), "main")
    check_state("every unit deployed beside the ask", "%s (UNDECIDED" % FX_ASK)
    return misses


def run_refusal_plant(case, repo, definition, handover):
    """The misses of the three driver frontier plants: `--refused` on A at the key the frontier gives
    it, or with a malformed key and an undeclared tag, then `--plan` for `plan-frontier`."""
    run_path = repo / ("memory/builds/%s/RUN.md" % FX_SLUG)
    before = run_path.read_bytes()
    key = next(f["key"] for f in derive_plant_position(repo, definition, handover)["frontier"] if f["item"] == FX_A)
    misses = []
    if case == "frontier-bad-key":
        for label, tag, k in (("a malformed key", FX_A, "%s@%s" % (FX_A, FX_IDS[0])),
                              ("an undeclared tag", "item.build.nowhere", "item.build.nowhere@%s#%s" % (FX_IDS[0], "0" * 8))):
            out, rc = run_driver(repo, "--refused", FX_SLUG, "--item", tag, "--key", k, "--reason", "probe")
            print("%s: fixture · %s · %s · exit %d · %s" % (SAY, case, label, rc, out.strip().splitlines()[-1:]))
            if rc != 1 or "UNATTENDED check 48 FAILED" not in out:
                misses.append("%s: exit %d, %r" % (label, rc, out.strip()[-300:]))
        if run_path.read_bytes() != before:
            misses.append("a refused --refused moved the run-state file's bytes")
        return misses
    out, rc = run_driver(repo, "--refused", FX_SLUG, "--item", FX_A, "--key", key, "--reason", "probe")
    print(out.rstrip())
    row = re.compile(r"\S+ refusal · item %s · step %s · reason probe" % (re.escape(FX_A), re.escape(key)))
    text = run_path.read_text(encoding="utf-8")
    rows = [ln for ln in text.splitlines() if row.fullmatch(ln)]
    for ln in rows:
        print("%s: fixture · %s · row %s" % (SAY, case, ln))
    added = len([ln for ln in text.splitlines() if ln.strip()]) - len([ln for ln in before.decode("utf-8").splitlines() if ln.strip()])
    if rc != 0 or len(rows) != 1 or added != 1:
        misses.append("--refused exit %d, %d matching row(s), %d line(s) added: %r" % (rc, len(rows), added, out.strip()[-300:]))
    if case == "plan-frontier":
        lines = run_driver(repo, "--plan", FX_SLUG)[0].splitlines()
        at = next((i for i, ln in enumerate(lines) if ln.startswith("next: ")), None)
        after = lines[at + 1] if at is not None and at + 1 < len(lines) else None
        print("%s: fixture · %s · after next: %r" % (SAY, case, after))
        if after != "frontier: %s" % FX_A:
            misses.append("the line after next: is %r" % after)
    return misses


def check_plant(case, pos, rc, repo):
    """The misses of `case` against the position it derived."""
    steps = [u["step"] for u in pos["units"]]
    claims = {c["name"]: c for c in pos["claims"]}
    kinds = {i["kind"]: i["subject"] for i in pos["interrupts"]}
    tags = [f["item"] for f in pos["frontier"]]
    lines = render_position_lines(pos)
    tracking = "read — refs/remotes/%s/main@" % run_fixture_git(repo, "remote")
    ref_line = next((ln for ln in lines if ln.startswith(tracking)), "")
    want = {"built-unarmed": lambda: "unit — %s · built · acceptance unarmed" % FX_IDS[0] in lines
            and "unit — %s · tested" % FX_IDS[1] in lines,
            "built-unheld": lambda: "unit — %s · designed" % FX_IDS[0] in lines,
            "built-armed": lambda: "unit — %s · designed" % FX_IDS[0] in lines,
"frontier-chain": lambda: tags == [FX_B],
            "frontier-parallel": lambda: tags == [FX_A, FX_B],
            "frontier-none": lambda: pos["build_step"] == "step.build" and tags == [],
            "frontier-refused": lambda: FX_A in tags and [(r.get("item"), r.get("reason")) for r in pos["refusals"]]
            == [(FX_A, "probe")] and pos["refusals"][0]["key"] == next(f["key"] for f in pos["frontier"] if f["item"] == FX_A),
            "steps": lambda: steps == ["deployed", "built", "designed"] and pos["answer"] == "act"
            and pos["build_step"] == "step.build" and any(r.startswith("memory/") for r in pos["read"])
            and any(c["name"].startswith("remote tip") and c["key"].startswith("k1:") and c["verdict"] == "fresh"
                    for c in pos["claims"]),
            "typed-status": lambda: steps[1] == "designed",
            "idempotent": lambda: pos["next"] and pos["next"]["item"] == "item.build.unit-lease"
            and any(n.startswith("item.build.base@") and c["verdict"] == "fresh" for n, c in claims.items()),
            "owner-decision": lambda: pos["answer"] == "awaiting" and "which-way" in kinds.get("owner-decision", ""),
            "parent-unlanded": lambda: pos["answer"] == "blocked" and "tPar" in pos["reason"],
            "terminal": lambda: pos["answer"] == "terminal",
            "stale-remote": lambda: pos["answer"] == "stale-remote" and ref_line.endswith(" · from reflog"),
            "fresh-clone": lambda: pos["answer"] != "stale-remote" and ref_line.endswith(" · from clone"),
            "quiet-remote": lambda: pos["answer"] != "stale-remote" and ref_line.endswith(" · from FETCH_HEAD"),
            "offline-stale": lambda: pos["answer"] == "stale-remote" and ref_line.endswith(" · from FETCH_HEAD"),
            "failed-fetch": lambda: pos["answer"] == "stale-remote" and "read — FETCH_HEAD · skipped — empty" in lines
            and ref_line.endswith(" · from reflog"),
            "fetch-other-branch": lambda: pos["answer"] == "stale-remote"
            and "read — FETCH_HEAD · skipped — no line for main of origin" in lines and ref_line.endswith(" · from reflog"),
            "clone-without-reflog": lambda: pos["answer"] == "stale-remote"
            and ref_line.endswith(" · fetched never · core.logAllRefUpdates=false"),
            "scp-remote": lambda: pos["answer"] != "stale-remote" and ref_line.endswith(" · from FETCH_HEAD")
            and not any("skipped —" in ln for ln in lines),
            "ssh-userinfo-remote": lambda: pos["answer"] != "stale-remote" and ref_line.endswith(" · from FETCH_HEAD")
            and not any("skipped —" in ln for ln in lines),
            "url-forms": lambda: pos["answer"] == "stale-remote" and "read — FETCH_HEAD · skipped — empty" in lines
            and not any("SECRET" in ln for ln in lines + [render_next_line(pos), json.dumps(pos)]),
            "no-remote": lambda: pos["answer"] == "act" and "interrupt — remote · none" in lines
            and not any("remote tip" in ln for ln in lines),
            "bad-transition": lambda: pos["answer"] == "invalid-input" and rc == 2,
            "deadlock": lambda: pos["answer"] == "stuck" and "item.build.exit" in pos["reason"],
            "bar-wait": lambda: pos["answer"] == "act" and pos["build_step"] == "step.test"
            and render_next_line(pos) == NEXT_SHAPES["everything-terminal"]}
    misses = [] if want[case]() else ["the position was %s" % json.dumps(pos)[:600]]
    if case == "failed-fetch":  # TOOL-dDeclaredLoop-74 AC3: a `main` line fetched from a second URL is skipped
        top = repo.parent
        why = check_fetch_head("%s\t\tbranch 'main' of %s" % ("0" * 40, (top / "up2").as_posix()), "origin", "main",
                               derive_fetch_url((top / "o.git").as_posix()))
        print("%s: fixture · %s · another url reads %s" % (SAY, case, why or "kept"))
        if why != "no line for main of origin":
            misses.append("a main line fetched from a second url read %r" % (why or "kept"))
    if case == "url-forms":  # TOOL-dDeclaredLoop-77 S3: each pair as tabled
        for configured, written, owed in FX_URL_FORMS:
            got = "equal" if derive_fetch_url(configured) == derive_fetch_url(written) else "unequal"
            print("%s: fixture · %s · %s against %s · %s" % (SAY, case, configured, written, got))
            if got != owed:
                misses.append("%s against %s read %s, owed %s" % (configured, written, got, owed))
    if case == "idempotent":
        k1 = derive_instance_key("item.build.base", FX_IDS[0], ["a" * 40])
        k2 = derive_instance_key("item.build.base", FX_IDS[0], ["b" * 40])
        print("%s: fixture · key %s · one input moved %s" % (SAY, k1, k2))
        if k1.split("#")[1] == k2.split("#")[1]:
            misses.append("an input SHA left the key unchanged")
    if case == "built-unarmed":
        # TOOL-dDeclaredLoop-67 AC10 (S50): --json names the unarmed half, and the driver's --status reads the
        # unarmed built unit's step past its tag, so A, the least advanced, is its next unit
        p = subprocess.run([sys.executable, str(pathlib.Path(__file__).absolute()), FX_SLUG, "--json"], cwd=str(repo),
                           capture_output=True, text=True, encoding="utf-8", errors="replace",
                           env={k: v for k, v in os.environ.items() if k != HANDOVER})
        try:
            armed = {u["id"]: u.get("acceptance_armed") for u in json.loads(p.stdout)["units"]}
        except (ValueError, KeyError, TypeError):
            armed = {}
        print("%s: fixture · %s · --json acceptance_armed %s" % (SAY, case, armed))
        if armed.get(FX_IDS[0]) is not False or armed.get(FX_IDS[1]) is not True:
            misses.append("--json read acceptance_armed %s, owed false for %s and true for %s: %s" % (
                armed, FX_IDS[0], FX_IDS[1], (p.stdout + p.stderr)[-300:]))
        out = run_driver(repo, "--status", FX_SLUG)[0]
        line = next((ln for ln in out.splitlines() if ln.startswith("unattended: %s · phase " % FX_SLUG)), None)
        print("%s: fixture · %s · driver %r" % (SAY, case, line))
        if not line or " · next %s" % FX_IDS[0] not in line:
            misses.append("the driver's --status line was %r, owed next %s" % (line, FX_IDS[0]))
    return misses


def check_url_forms_rows(top, repo, definition, handover):
    """The misses of the `url-forms` plant's two later readings (TOOL-dDeclaredLoop-82): `FETCH_HEAD`
    written as one line for main of another URL and read with no fetch, owed `stale-remote`, the skip
    entry naming the remote and no `SECRET` on any line or in the JSON (S3); then the git-written row,
    a fetch over git's dumb HTTP protocol from `http.server` on 127.0.0.1 with a user part in the URL
    and every credential helper cleared, `derive_fetch_url` of the configured URL owed equal to the
    URL git wrote (S23). It runs last, so its `FETCH_HEAD` is no earlier reading's."""
    import contextlib
    import functools
    import http.server
    import io
    import threading
    misses = []
    sha = run_fixture_git(repo, "rev-parse", "main")
    write_fixture_files(repo, {".git/FETCH_HEAD": "%s\t\tbranch 'main' of https://other.example/r\n" % sha})
    pos = derive_plant_position(repo, definition, handover)
    lines = render_position_lines(pos)
    for line in lines:
        print(line)
    skip = "read — FETCH_HEAD · skipped — no line for main of origin"
    if pos["answer"] != "stale-remote" or skip not in lines or any(
            "SECRET" in s for s in lines + [render_next_line(pos), json.dumps(pos)]):
        misses.append("the FETCH_HEAD naming another URL read %s" % json.dumps(pos)[:600])
    run_fixture_git(top / "o.git", "update-server-info")
    server = http.server.ThreadingHTTPServer(
        ("127.0.0.1", 0), functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(top)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        configured = "http://user:tok@127.0.0.1:%d/o.git" % server.server_address[1]
        run_fixture_git(repo, "remote", "add", "web", configured)
        with contextlib.redirect_stderr(io.StringIO()):   # the handler's request log
            rc, out = read_git(repo, "-c", "credential.helper=", "fetch", "-q", "web",
                               env=read_clean_env(GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never", NO_PROXY="127.0.0.1"))
    finally:
        server.shutdown()
        server.server_close()
    head = (repo / ".git" / "FETCH_HEAD").read_text(encoding="utf-8").splitlines()
    written = head[0].split(" of ", 1)[1] if rc == 0 and head and " of " in head[0] else None
    got = "equal" if derive_fetch_url(configured) == written else "unequal"
    print("%s: fixture · url-forms · git-written · %s against %s · %s" % (
        SAY, derive_fetch_url(configured), written, got))
    if got != "equal" or "user:tok@" not in configured:
        misses.append("the git-written row read %s: fetch exit %d %s" % (got, rc, out[-300:]))
    return misses


def run_boundary_plant():
    """The `boundary` case's misses (KICK-dKeptSession-13 AC4), over planted engine answers rather
    than a scratch repository: AC4 grades `derive_item_boundary`'s comparison, not the derivation."""
    k1, k2 = "%s@%s#aaaa0001" % (FX_A, FX_IDS[0]), "%s@%s#aaaa0002" % (FX_A, FX_IDS[0])
    units = [{"id": FX_IDS[0], "state": "READY"}, {"id": FX_IDS[1], "state": "FORKED"}]
    misses = []
    for label, answer, nxt, pointer, want in (
            ("the key held", "act", k1, k1, "boundary — none crossed · item %s" % k1),
            ("another key", "act", k2, k1, "boundary — %s → %s" % (k1, k2)),
            ("awaiting", "awaiting", None, k1, "boundary — %s → none" % k1),
            ("none held while awaiting", "awaiting", None, "none", "boundary — none crossed · item none"),
            ("stale-remote", "stale-remote", k2, k1, "boundary — none crossed · item %s · stale-remote" % k1),
            ("invalid-input", "invalid-input", None, k1, "boundary — none crossed · item %s · invalid-input" % k1)):
        pos = {"slug": FX_SLUG, "answer": answer, "next": {"key": nxt} if nxt else None, "units": units}
        lines = render_boundary_lines(pos, pointer)
        print("%s: fixture · boundary · %s · %s" % (SAY, label, " / ".join(lines)))
        if lines != [want, "forked — %s" % FX_IDS[1]]:
            misses.append("%s printed %r, owed %r" % (label, lines, want))
    return misses


def run_plant(case):
    """One fixture case: its lines, then `held` or `MISSED`; the engine's exit where it held."""
    if case == "boundary":   # planted engine answers, so no scratch repository is built
        misses = run_boundary_plant()
        print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
        return 0 if not misses else 1
    top = pathlib.Path(tempfile.mkdtemp(prefix="pos-"))
    # TOOL-dDeclaredLoop-75 S34: the machine's git config reaches no plant, every git under it reading one empty file
    kept = {k: os.environ.get(k) for k in ("GIT_CONFIG_GLOBAL", "GIT_CONFIG_SYSTEM")}
    try:
        (top / "empty.gitconfig").write_bytes(b"")
        os.environ.update(dict.fromkeys(kept, str(top / "empty.gitconfig")))
        root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT)
        repo, definition, handover = write_position_plant(top, case, root)
        if case == "plan-line":
            misses, rc = check_plan_line(repo), 0
        elif case == "status-line":
            out = run_driver(repo, "--status", FX_SLUG)[0]
            print(out.rstrip())
            rc = 0
            misses = [] if any(ln.startswith("position — %s · " % FX_SLUG) for ln in out.splitlines()) else [
                "--status printed no position line"]
        elif case in ("frontier-bad-key", "plan-frontier"):
            misses, rc = run_refusal_plant(case, repo, definition, handover), 0
        else:
            misses = run_refusal_plant(case, repo, definition, handover) if case == "frontier-refused" else []
            readings = [definition]
            if case == "built-armed":  # read again with the acceptance row absent
                readings.append(dict(definition, **{"computed-witness": [
                    r for r in definition["computed-witness"] if r["name"] != "acceptance"]}))
            for reading in readings:
                pos = derive_plant_position(repo, reading, handover)
                rc = 2 if pos["answer"] == "invalid-input" else 0
                for line in render_position_lines(pos):
                    print(line)
                print("next: %s" % render_next_line(pos))
                misses += check_plant(case, pos, rc, repo)
            if case == "url-forms":
                misses += check_url_forms_rows(top, repo, definition, handover)
    except LookupError as e:
        print("%s: fixture · %s · unarmed: %s" % (SAY, case, e))
        return 2
    finally:
        for k, v in kept.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        remove_tree(top)
    print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
    return rc if not misses else 1


def run_selftest():
    """Every plant through `run_selftest_cases`."""
    cases = [(c, ["--fixture", "--plant", c], 2 if c == "bad-transition" else 0, "%s: fixture · %s · held" % (SAY, c), "")
             for c in PLANTS]
    return run_selftest_cases(main, cases, "%s: selftest" % SAY)


def print_check_refusal(tag, key):
    """`--check-refusal`: the composition of the working tree read as `derive_position` reads it, gov's
    own rows where it is unarmed; exit 0 held, 1 refused, 2 where the composition does not read."""
    rc, top = read_git(".", "rev-parse", "--show-toplevel")
    try:
        items = read_composed_items(top if rc == 0 and top else ".")
    except (LoopError, ValueError, OSError, LookupError, KeyError, TypeError, subprocess.SubprocessError) as e:
        print("loop: unarmed · %s" % (str(e) or type(e).__name__))
        return 2
    held, why = check_refusal(tag, key, {r.get("tag") for r in items})
    print("loop: refusal held · %s · %s" % (tag, key) if held else "loop: refused · %s" % why)
    return 0 if held else 1


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="position.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("slug", nargs="?")
    out = ap.add_mutually_exclusive_group()
    out.add_argument("--json", action="store_true", help="one JSON object")
    out.add_argument("--next-line", action="store_true", help="the next: shape alone")
    ap.add_argument("--frontier", action="store_true", help="with --next-line, the frontier's tags on a second line")
    ap.add_argument("--boundary", metavar="KEY", help="the item boundary against the held pointer <key|none>")
    ap.add_argument("--check-refusal", nargs=2, metavar=("TAG", "KEY"), help="may a refusal row name TAG at KEY")
    ap.add_argument("--fixture", action="store_true", help="run one fixture case")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="run every fixture case")
    args = ap.parse_args(argv)
    if args.selftest:
        if args.fixture or args.slug:
            ap.error("--selftest takes no slug and no --fixture")
        return run_selftest()
    if args.check_refusal:
        if args.fixture or args.slug or args.json or args.next_line or args.frontier:
            ap.error("--check-refusal takes a tag and a key and nothing else")
        return print_check_refusal(*args.check_refusal)
    if args.frontier and not args.next_line:
        ap.error("--frontier is a second line of --next-line")
    if args.boundary is not None and (args.json or args.next_line or args.fixture or not args.slug
                                      or not re.fullmatch(r"\S+", args.boundary)):
        ap.error("--boundary takes a slug and one pointer, <key|none>, and nothing else")
    if args.fixture != bool(args.plant) or (args.fixture and args.slug):
        ap.error("--fixture takes --plant <case> and no slug")
    if args.fixture:
        return run_plant(args.plant)
    if not args.slug:
        ap.error("a slug, or --fixture --plant <case>, or --selftest")
    rc, top = read_git(".", "rev-parse", "--show-toplevel")
    pos = derive_position(top if rc == 0 and top else ".", args.slug)
    if args.boundary is not None:
        for line in render_boundary_lines(pos, args.boundary):
            print(line)
    elif args.json:
        # TOOL-dDeclaredLoop-67 S50: the unarmed half as its own field, false exactly where the line ends
        # `· acceptance unarmed`
        print(json.dumps(dict(pos, units=[dict({k: u[k] for k in ("id", "step", "state")},
                                               acceptance_armed=not u["unarmed"]) for u in pos["units"]]),
                         ensure_ascii=False))
    elif args.next_line:
        print(render_next_line(pos))
        if args.frontier:
            print(" ".join(f["item"] for f in pos["frontier"]) or "none")
    else:
        for line in render_position_lines(pos):
            print(line)
    return 2 if pos["answer"] == "invalid-input" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
