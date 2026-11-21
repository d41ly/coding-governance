#!/usr/bin/env python3
"""claim.py — `entry.claim`'s python half: a placed request's claim body, its routes and its first record (TOOL-dPlacedRequest-21).

    python claim.py body --request <key> --slug <slug> --claimant <tag>:<session> [--pieces <n>]
    python claim.py precheck --slug <slug>
    python claim.py read --slug <slug>
    python claim.py route --cause <cause> --slug <slug>
    python claim.py scaffold --slug <slug> --request <key> [--pieces <n>]
    python claim.py record --slug <slug>
    python claim.py --fixture [--plant <case>]

The unattended driver's `--entry-claim <slug> --request <key> [--pieces <n>]` is the act, and every remote
read and write is its own: it calls these verbs in the repository at the current directory, in this order.

BODY reads the request's placement through `placement.py`'s record lines, the ones `placement.py record`
prints, refuses a disposition other than `new`, `patch` and `repeat` (exit 1), a slug `--new-build` would
refuse, and on a repeat a missing or non-positive `--pieces`, on any other a given one (exit 2, one line
naming `--pieces`), and prints the claim commit's message: `gov-claim claims/<slug>`, a blank line and
`render_claim_body`'s keys, shared interface I23: `claimant-key`, `session`, `content-key`, `disposition`,
`reason`, `scenarios`, `facts`, and on a patch `origin-slug` and `origin-sha`, the newest default-branch
commit touching the origin's build folder. The reason is the placement's, already redacted and capped.
PRECHECK runs the memory-tree kit's `check_slug_claimed`, the local pre-check of a fresh claim alone: a
resuming claimant never runs it, since it would find its own claim, scaffold and transition commits.
READ prints `read_claim_body`, the claim ref's keys as this node's cache ref `refs/gov/remote/claims/<slug>`
holds them, the newest commit's keys over the first's, so a later `wait-since:` or `overlap:` reads.
ROUTE prints one `route · <word> · <detail>` line for a lease refusal's cause word: `derive_claim_route`
over `leases` sends `tombstone`, `terminal` and `epoch-fence` to `refuse` whatever `leases` says, the
wait causes `live-holder` and `offered`, and `overlap` under `leases: refuse`, to `stamp` where the claim
body holds no `wait-since`, `wait` while `flow.wait-ceiling` has not passed since it by this node's clock,
and `expired` once it has; `overlap` under `warn` to `noted`; and `offline` to `refuse-offline` under
`leases.offline: refuse`, else `wait-offline`, since no value queues a claim.
SCAFFOLD, on a patch or a repeat, commits the derived plan record, the memory-tree kit's `--placed-build`
README and its contract row, alone, as `records(<slug>): entry.claim's derived plan record`, refusing an
index holding any other staged path; a README already at HEAD is witnessed and writes nothing.
RECORD writes the build's first transition record through `loop_transition.py`'s `write_transition` from
`none`, witnessed by HEAD, its facts the claim's `facts` with `disposition` added and no scenario given,
the writer deriving it: `new` is B1's `item.entry.claim` `claimed` into planning, `repeat` B3's into
designing, and `patch` B2's `item.plan.dedupe` `patch` into designing under its stand-in. A build the
transition log already reads is witnessed and writes nothing. Under `patch.ratify` = `owner` it prints the
owner item first, and `check_patch_ratified`, which `write_transition` calls before any move into
`designing` of a build whose claim body reads `disposition: patch`, holds the record until the build's
folder holds the owner's disposition record of `item.entry.claim` `ratified`, `rejected` holding it for
good; the unit id that record carries is `<FAMILY>-<slug>-1`, the family the README's `roster` names.

Exit 0 written or witnessed · 1 refused, named · 2 not written: a usage error, a kit that does not resolve
or a read that did not answer. `--fixture --plant <case>` runs one case of `PLANTS` in a throwaway
repository with a bare remote under the system temp folder, driving the unattended driver's `--entry-claim`,
and prints `claim: <case> · ... · held` or `MISSED`; `--fixture` alone runs every case through
`loop_lib.run_selftest_cases`, the `loop claim fixtures` leg.

WHAT THIS DOES NOT CHECK: a claim body another node never fetched, since `read_claim_body` and the
`write_transition` gate read this node's cache ref and nothing remote; that the placement's facts still
hold, which `placement.py check` re-read before the record printed; the wait judged on another node's
clock, the waiting node measuring its own wait against its own stamp; and a claimant key's session beyond
its shape.
"""
import argparse
import datetime
import pathlib
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
# one module whether run or imported, so the `PatchHeld` the transition writer raises is the class caught here
sys.modules.setdefault("claim", sys.modules[__name__])
from loop_lib import read_memory_tree, resolve_kit_dir, resolve_memory_root, run_selftest_cases  # noqa: E402
from loop_parents import read_policy_kit  # noqa: E402
from loop_witness import FIXTURE_REMOTE, read_clean_env, read_git, remove_tree, resolve_bash, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "claim"
#: The claims namespace on the remote, shared interface I23, and this node's cache of it, which
#: `write_gov_ref` sets on every write and the driver's fetch fills.
CLAIM_NS, CACHE_NS = "refs/gov/claims", "refs/gov/remote/claims"
#: The claim commit's header line.
CLAIM_HEADER = "gov-claim claims/%s"
#: The claim body's keys, in the order they are written; a later commit on the ref adds `wait-since` or `overlap`.
CLAIM_KEYS = ("claimant-key", "session", "content-key", "disposition", "reason", "scenarios", "facts",
              "origin-slug", "origin-sha")
#: The dispositions a claim opens a build for, and each one's first move: `(item, outcome)` from `none`.
FIRST_MOVES = {"new": ("item.entry.claim", "claimed"), "repeat": ("item.entry.claim", "claimed"),
               "patch": ("item.plan.dedupe", "patch")}
#: The item the owner's ratification of a patch names.
CLAIM_ITEM = "item.entry.claim"
#: The lease refusal causes by route, shared interface I9: never retried, and waited for.
TERMINAL_CAUSES = ("tombstone", "terminal", "epoch-fence")
WAIT_CAUSES = ("live-holder", "offered")
CAUSES = TERMINAL_CAUSES + WAIT_CAUSES + ("overlap", "offline")
#: The scaffold commit's message, the claim verb's own, before the build's first transition record.
SCAFFOLD_MESSAGE = "records(%s): entry.claim's derived plan record"
#: The shapes a claimant key and a body key take.
CLAIMANT = re.compile(r"[a-z]:[A-Za-z0-9-]+")
BODY_KEY = re.compile(r"[a-z][a-z-]*")
REQUEST_KEY = re.compile(r"[0-9a-f]{12}")
UTC = "%Y-%m-%dT%H:%M:%SZ"
NO_VALUE = "none"


class ClaimRefused(ValueError):
    """A verb refused: its message is the whole line printed; `code` its exit."""

    def __init__(self, line, code=1):
        super().__init__(line)
        self.code = code


class PatchHeld(ValueError):
    """`write_transition` refused a patch's move into designing while `patch.ratify` holds it."""


# ------------------------------------------------------------------------------------------ the body
def read_claim_lines(root, key):
    """`{name: value}` of the claim lines `placement.py record` prints for request `key`'s newest block.
    ClaimRefused (exit 1) where the block's check did not pass."""
    from placement import print_claim_lines, read_placement
    from probe import resolve_git_paths
    _top, common = resolve_git_paths()
    rc, lines = print_claim_lines(read_placement(common / "requests" / ("%s.placement" % key)))
    if rc != 0:
        raise ClaimRefused("claim refused — %s · no passed placement: placement.py record prints no claim lines for "
                           "the request, so place and check it first" % key)
    return dict(line.split(": ", 1) for line in lines)


def check_claim_slug(slug):
    """None where `slug` is a build slug as `--new-build` holds one; ClaimRefused (exit 2) otherwise."""
    read_memory_tree("backlog.py")
    import backlog
    if not (backlog.SLUG_RE.match(slug) and slug[0].isalpha() and slug[0].islower()):
        raise ClaimRefused("claim not written — `%s` is not a build slug: the node's own lower-case tag, then a CamelCase "
                           "adjective-noun, letters and digits only" % slug, 2)


def derive_origin_sha(root, origin):
    """The newest commit of the default branch touching `origin`'s build folder, or None. The default branch
    is `refs/remotes/<remote>/HEAD`'s by the loop kit's remote ladder, HEAD where the clone has none."""
    from claims import resolve_remote
    remote, branch, _observed, refusal = resolve_remote(str(root))
    tip = "refs/remotes/%s/%s" % (remote, branch) if remote and branch and not refusal else "HEAD"
    rc, out = read_git(root, "log", "-1", "--format=%H", tip, "--", "%s/builds/%s/" % (resolve_memory_root(root), origin))
    return out if rc == 0 and re.fullmatch(r"[0-9a-f]{40}", out) else None


def render_claim_body(lines, slug, claimant, key, origin_sha=None):
    """The claim commit's message: its header, a blank line and the keys of `CLAIM_KEYS` it carries, from
    `lines`, the placement's claim lines, the claimant key and the request's content key."""
    session = claimant.split(":", 1)[1]
    body = {"claimant-key": claimant, "session": session, "content-key": key}
    for name in ("disposition", "reason", "scenarios", "facts"):
        body[name] = lines.get(name, NO_VALUE)
    if lines.get("disposition") == "patch":
        body["origin-slug"], body["origin-sha"] = lines.get("build", NO_VALUE), origin_sha or NO_VALUE
    return "\n".join([CLAIM_HEADER % slug, ""] + ["%s: %s" % (k, body[k]) for k in CLAIM_KEYS if k in body])


def read_claim_body(root, slug):
    """`{key: value}` of the claim of `slug` as this node's cache ref holds it, the newest commit's keys over the
    first's along its first parents; empty where the ref is absent here."""
    rc, out = read_git(root, "log", "--reverse", "--first-parent", "--format=%x01%B", "%s/%s" % (CACHE_NS, slug), "--")
    body = {}
    if rc != 0:
        return body
    for message in out.split("\x01"):
        for line in message.splitlines()[1:]:
            name, sep, value = line.rstrip("\r").partition(": ")
            if sep and BODY_KEY.fullmatch(name):
                body[name] = value.strip()
    return body


# ------------------------------------------------------------------------------------------ the routes
def derive_claim_route(cause, leases):
    """The route of a lease refusal's `cause` under the policy value `leases` (S5): `refuse` for a terminal
    cause whatever `leases` says, `wait` for a live holder or an offer and for an overlap under `refuse`,
    `noted` for an overlap under `warn`, `offline` for an unreachable remote. ValueError on another cause."""
    if cause in TERMINAL_CAUSES:
        return "refuse"
    if cause in WAIT_CAUSES:
        return "wait"
    if cause == "overlap":
        return "noted" if leases == "warn" else "wait"
    if cause == "offline":
        return "offline"
    raise ValueError("the cause %s is none of %s" % (cause, " ".join(CAUSES)))


def check_wait_expired(since, ceiling_hours, now=None):
    """True where `ceiling_hours` have passed since the UTC stamp `since`, on this node's clock. ValueError on a
    stamp that is not `YYYY-MM-DDTHH:MM:SSZ`."""
    then = datetime.datetime.strptime(since, UTC).replace(tzinfo=datetime.timezone.utc)
    now = now or datetime.datetime.now(datetime.timezone.utc)
    return (now - then).total_seconds() >= float(ceiling_hours) * 3600


def read_claim_policy(root, *keys):
    """`{key: value}` of each policy key, through the policy kit's `resolve` at the landed revision. ClaimRefused
    (exit 2) on a refusal; LookupError where the kit does not resolve."""
    policy, _guard = read_policy_kit()
    try:
        return {k: policy.resolve(k, str(root)).value for k in keys}
    except policy.Refusal as e:
        raise ClaimRefused("claim not written — the policy does not resolve: %s" % e, 2) from None


def check_patch_ratified(root, slug):
    """`auto` under `patch.ratify` = `auto`; under `owner`, `ratified` where the newest disposition record of
    `slug` naming `CLAIM_ITEM` disposes `ratified`, `rejected` where it disposes that, else `held`."""
    if str(read_claim_policy(root, "patch.ratify")["patch.ratify"]) != "owner":
        return "auto"
    from adapt import read_disposition_release
    found = read_disposition_release(root, slug, CLAIM_ITEM, set())
    if found is None:
        return "held"
    return found[1] if found[1] in ("ratified", "rejected") else "held"


def read_anchor_unit(root, slug):
    """`<FAMILY>-<slug>-1`, the anchor id a pre-spec disposition record of `slug` carries, the family the first
    its README's `roster` names; `TOOL-<slug>-1`'s family read as `<FAMILY>` where no roster reads."""
    path = pathlib.Path(root, resolve_memory_root(root), "builds", slug, "README.md")
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    hit = re.search(r"^roster:\s*([A-Z][A-Z0-9]*)", text, re.M)
    return "%s-%s-1" % (hit.group(1) if hit else "<FAMILY>", slug)


# ------------------------------------------------------------------------------------------ the verbs
def write_claim_scaffold(root, slug, key, pieces):
    """The derived plan record of a placed patch or repeat, committed alone: its lines."""
    read_memory_tree("gen_build_index.py")
    import gen_build_index as gbi
    m = resolve_memory_root(root)
    readme = "%s/builds/%s/README.md" % (m, slug)
    if read_git(root, "cat-file", "-e", "HEAD:%s" % readme)[0] == 0:
        return ["%s — %s · scaffold at HEAD, so nothing is written" % (SAY, slug)]
    registry = "%s/%s" % (m, gbi.CONTRACT_REGISTRY)
    staged = [p for p in read_git(root, "diff", "--cached", "--name-only")[1].splitlines() if p.strip()]
    beyond = [p for p in staged if p not in (readme, registry)]
    if beyond:
        raise ClaimRefused("claim not written — %s · the index holds a staged path beyond the scaffold's own, %s, and the "
                           "scaffold commit carries its own files alone" % (slug, beyond[0]))
    said = []
    if readme not in staged:
        body = read_claim_body(root, slug)
        if body.get("disposition") == "patch":
            argv = [slug, "--request", key, "--origin", body.get("origin-slug", "")]
        else:
            argv = [slug, "--request", key, "--playbook", read_claim_lines(root, key).get("playbook", ""),
                    "--pieces", pieces or ""]
        conf = gbi.load_conf(str(root))
        try:
            gbi.cmd_placed_build(str(root), conf, gbi.read_placed_build_args(argv))
        except gbi.Problem as e:
            raise ClaimRefused("claim not written — %s · the derived plan record: %s" % (slug, e), 2) from None
        said.append("%s — %s · wrote %s" % (SAY, slug, readme))
    if read_git(root, "commit", "-q", "-m", SCAFFOLD_MESSAGE % slug)[0] != 0:
        raise ClaimRefused("claim not written — %s · git could not commit the staged scaffold" % slug, 2)
    return said + ["%s — %s · scaffold committed %s" % (SAY, slug, read_git(root, "rev-parse", "HEAD")[1][:8])]


def write_first_transition(root, slug):
    """The build's first transition record from `none`, witnessed by HEAD: its lines. ClaimRefused where the
    claim body does not read, `write_transition` refuses, or `patch.ratify` holds it."""
    from loop_table import TransitionRefused
    from loop_transition import read_transitions, write_transition
    body = read_claim_body(root, slug)
    disposition = body.get("disposition")
    if disposition not in FIRST_MOVES:
        raise ClaimRefused("claim not written — %s · no claim body with a claimed disposition reads in this clone" % slug, 2)
    moves = read_transitions(slug, root)
    if moves:
        return ["%s — %s · first record at %s, so nothing is written" % (SAY, slug, (moves[-1].get("commit") or "-")[:8])]
    said = []
    if disposition == "patch" and check_patch_ratified(root, slug) in ("held", "rejected"):
        said.append("owner item: ratify %s · patch.ratify is owner · dispose %s ratified through the record factory: "
                    "--build %s --unit %s --item %s --disposition ratified --channel <channel>"
                    % (slug, CLAIM_ITEM, slug, read_anchor_unit(root, slug), CLAIM_ITEM))
    facts = dict(p.split("=", 1) for p in body.get("facts", "").split("; ") if "=" in p)
    facts["disposition"] = disposition
    item, outcome = FIRST_MOVES[disposition]
    try:
        move, commit, _wrote, line, lines = write_transition(root, slug, "none", item, outcome, "HEAD", facts, {})
    except PatchHeld as e:
        raise ClaimRefused("\n".join(said + ["claim held — %s · %s" % (slug, e)])) from None
    except TransitionRefused as e:
        raise ClaimRefused("claim refused — %s · no build row holds the first move: %s" % (slug, e)) from None
    except ValueError as e:
        raise ClaimRefused("claim not written — %s · the first record: %s" % (slug, e), 2) from None
    said += lines + ["%s — %s · recorded none -> %s · %s · commit %s" % (SAY, slug, move["to"], item,
                                                                         commit[:8] if commit else "none")]
    return said + ([line] if line else [])


def run_claim_verb(args):
    """One verb in the repository at the current directory: `(exit, lines)`."""
    from probe import resolve_git_paths
    root, _common = resolve_git_paths()
    if args.verb == "body":
        lines = read_claim_lines(root, args.request)
        disposition = lines.get("disposition")
        if disposition not in FIRST_MOVES:
            raise ClaimRefused("claim refused — %s · the placement's disposition %s opens no claimed build: new, patch "
                               "or repeat" % (args.request, disposition))
        check_claim_slug(args.slug)
        counted = (args.pieces or "").isdigit() and int(args.pieces) > 0
        if disposition == "repeat" and not counted:
            raise ClaimRefused("claim not written — a repeat claim takes --pieces <n>, a positive whole number, the count "
                               "the owner asked for; given %s" % ("'%s'" % args.pieces if args.pieces is not None else
                                                                   "none"), 2)
        if disposition != "repeat" and args.pieces is not None:
            raise ClaimRefused("claim not written — --pieces names a repeat's count, and a %s claim takes none" % disposition, 2)
        if not CLAIMANT.fullmatch(args.claimant or ""):
            raise ClaimRefused("claim not written — the claimant key %r is not <fleet tag>:<session>" % args.claimant, 2)
        sha = None
        if disposition == "patch":
            sha = derive_origin_sha(root, lines.get("build", NO_VALUE))
            if sha is None:
                raise ClaimRefused("claim not written — no default-branch commit touches the origin %s's build folder"
                                   % lines.get("build"), 2)
        return 0, render_claim_body(lines, args.slug, args.claimant, args.request, sha).splitlines()
    if args.verb == "precheck":
        read_memory_tree("gen_build_index.py")
        import gen_build_index as gbi
        why = gbi.check_slug_claimed(str(root), gbi.load_conf(str(root)), args.slug)
        if why:
            return 1, ["claim refused — %s · the local pre-check of a fresh claim: %s" % (args.slug, why)]
        return 0, ["%s — %s · the local pre-check finds nothing" % (SAY, args.slug)]
    if args.verb == "read":
        body = read_claim_body(root, args.slug)
        if not body:
            return 1, ["%s — %s · no claim reads at %s/%s" % (SAY, args.slug, CACHE_NS, args.slug)]
        return 0, ["%s: %s" % kv for kv in body.items()]
    if args.verb == "route":
        held = read_claim_policy(root, "leases", "leases.offline", "flow.wait-ceiling")
        try:
            route = derive_claim_route(args.cause, held["leases"])
        except ValueError as e:
            return 2, ["%s — not routed · %s" % (SAY, e)]
        if route == "offline":
            word = "refuse-offline" if held["leases.offline"] == "refuse" else "wait-offline"
            return 0, ["route · %s · leases.offline %s" % (word, held["leases.offline"])]
        if route != "wait":
            return 0, ["route · %s · leases %s" % (route, held["leases"])]
        since = read_claim_body(root, args.slug).get("wait-since")
        ceiling = held["flow.wait-ceiling"]
        if not since:
            return 0, ["route · stamp · flow.wait-ceiling %sh" % ceiling]
        try:
            gone = check_wait_expired(since, ceiling)
        except ValueError:
            return 2, ["%s — not routed · the claim's wait-since %r is no UTC stamp" % (SAY, since)]
        return 0, ["route · %s · waiting since %s · flow.wait-ceiling %sh" % ("expired" if gone else "wait", since, ceiling)]
    if args.verb == "scaffold":
        return 0, write_claim_scaffold(root, args.slug, args.request, args.pieces)
    return 0, write_first_transition(root, args.slug)


# ------------------------------------------------------------------------------------------ the fixture
#: The fixture's request text and its slugs: a repeat, a patch of the fixture's closed build, and a new one.
FX_TEXT = "Run the release playbook again for the widget, zq-claim-marker-21\n"
FX_REPEAT, FX_PATCH, FX_NEW, FX_SESSION, FX_OTHER = "dRunAgain", "dFixPatch", "dFreshClaim", "s-fx", "z:s-other"
FX_PLAYBOOK = "playbooks/zq-release.md"
PLANTS = {"patch-owner-unratified": "a patch under patch.ratify = owner: the owner item printed and the record into "
                                    "designing refused naming patch.ratify",
          "patch-owner-ratified": "the same patch, its owner's disposition record ratified committed: the resumed claim "
                                  "records item.plan.dedupe into designing",
          "patch-owner-rejected": "the same patch, its owner's disposition record rejected: the resumed claim held "
                                  "for good, naming patch.ratify",
          "refusals": "a continue placement refused, --pieces on a patch refused, a stray staged path refusing the "
                      "scaffold and the resumed claim committing it once unstaged, and an unreachable remote under "
                      "leases.offline refuse refused offline",
          "tombstone-warn": "a repeat whose build lease is a tombstone under leases warn: exit 1 naming tombstone, one "
                            "ask line, the lease ref unmoved",
          "claim-twice": "a repeat claimed twice by one claimant: the second skips the pre-check, exits 0 claimed by this "
                         "claimant, the claim ref at one commit and HEAD unmoved",
          "slug-minted-locally": "a slug a local commit already minted: refused naming the local pre-check, no claim ref",
          "slug-taken": "a slug claimed under another key: exit 5 with one route-back row on the request; offline, no "
                        "build folder",
          "repeat-no-pieces": "a repeat with no --pieces: one line naming --pieces, exit 2, no claim ref, no folder",
          "live-holder": "a live holder: exit 4 adding wait-since; past flow.wait-ceiling the resumed claim exits 1 "
                         "with the owner item",
          "stale-holder": "a holder first sighted past leases.expiry-hours: the claim takes the lease over, exits 0 "
                          "claimed with take-announced, the lease's epoch one above the planted one and no wait-since",
          "overlap-warn": "an overlapping branch under leases warn: the claim proceeds with an overlap: key",
          "first-record": "a repeat's scaffold commit, then its transition into designing under scenario.playbook-run",
          "first-record-patch": "a patch under patch.ratify = auto recorded as item.plan.dedupe under stand-in "
                                "dRankedPlan"}


def write_claim_fixture(top, policy):
    """A placement fixture repository under `top` with the unattended driver's conf, `RUN_CLAIMS` on, a bare
    remote, gov's scenario pack, the fixture playbook, an empty contract registry and the policy `policy`,
    committed and pushed, its default branch named, and the request's words kept as `--request` keeps them.
    -> `(repo, request key)`."""
    from placement import write_placement_fixture
    from request import derive_request_content_key
    root = write_placement_fixture(top, policy, driver=True, remote=True, scenarios=())
    write_fixture_files(root, {FX_PLAYBOOK: "# the release playbook\n", "memory/project/readme-contract.txt": ""})
    for name, value in (("user.name", "fx"), ("user.email", "fx@example.invalid"), ("core.autocrlf", "false")):
        run_fixture_git(root, "config", name, value)
    run_fixture_git(root, "add", "-A")
    run_fixture_git(root, "commit", "-q", "-m", "the claim fixture")
    run_fixture_git(root, "push", "-q", FIXTURE_REMOTE, "main")
    run_fixture_git(root, "fetch", "-q", FIXTURE_REMOTE)
    run_fixture_git(root, "remote", "set-head", FIXTURE_REMOTE, "main")
    key = derive_request_content_key(FX_TEXT)
    store = pathlib.Path(run_fixture_git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")) / "requests"
    write_fixture_files(store, {"%s.md" % key: FX_TEXT})
    return root, key


def write_claim_placement(root, key, disposition, build=NO_VALUE, playbook=NO_VALUE):
    """A passed placement block of request `key` written as `placement.py check` leaves one."""
    from placement import ENTRY_FACTS, write_placement_blocks
    store = pathlib.Path(run_fixture_git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")) / "requests"
    entry = ENTRY_FACTS.get(disposition)
    block = {"placed-utc": "2026-11-20T00:00:00Z", "disposition": disposition, "build": build, "breakpoint": NO_VALUE,
             "playbook": playbook, "reason": "the owner asked for it again", "evidence": NO_VALUE,
             "observations": NO_VALUE, "placer": "declared",
             "scenarios": "scenario.%s" % entry if entry else NO_VALUE,
             "facts": "entry=%s" % entry if entry else NO_VALUE, "check": "pass"}
    write_placement_blocks(store / ("%s.placement" % key), [block])


def write_fixture_claim_commit(root, slug, lines, parent=None):
    """One commit over the empty tree on `refs/gov/claims/<slug>` of the fixture's remote, its message the claim
    header and `lines`, parented on `parent` where given."""
    tree = subprocess.run(["git", "mktree"], cwd=str(root), input="", capture_output=True, text=True,
                          encoding="utf-8", check=True, env=read_clean_env()).stdout.strip()
    msg = "\n".join([CLAIM_HEADER % slug, ""] + lines)
    sha = run_fixture_git(root, "commit-tree", tree, *(["-p", parent] if parent else []), "-m", msg)
    run_fixture_git(root, "push", "-q", FIXTURE_REMOTE, "%s:%s/%s" % (sha, CLAIM_NS, slug))
    return sha


def run_claim_plant(case):
    """One case of `PLANTS`: its `claim: <case> · ... · held` or `MISSED` line; 0 held, 1 missed."""
    top = pathlib.Path(tempfile.mkdtemp(prefix="cl-")).absolute()
    seen, bad = [], []
    try:
        check_claim_plant(case, top, seen, bad)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError, LookupError, ValueError) as e:
        bad.append("the plant could not run: %s" % (getattr(e, "stderr", None) or e))
    finally:
        remove_tree(top)
    print("%s: %s · %s · %s" % (SAY, case, " · ".join(seen) or "-", "held" if not bad else "MISSED " + "; ".join(bad)))
    return 0 if not bad else 1


def check_claim_plant(case, top, seen, bad):
    """`case` run in a fixture under `top`, each observation appended to `seen` and each miss to `bad`."""
    from placement import FX_DONE, read_fleet_user, write_foreign_lease
    from probe import read_build_records
    patch = case.startswith("patch") or case == "first-record-patch"
    policy = 'patch.ratify = "owner"\n' if case.startswith("patch-owner") else ""
    root, key = write_claim_fixture(top, policy)
    origin = top / "origin.git"
    slug = FX_PATCH if patch else FX_REPEAT
    write_claim_placement(root, key, "patch" if patch else "repeat", FX_DONE if patch else NO_VALUE,
                          NO_VALUE if patch else FX_PLAYBOOK)
    driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
    bash = resolve_bash(driver)
    if bash is None:
        raise LookupError("no bash can run %s" % driver.as_posix())
    env = read_clean_env(USERNAME=read_fleet_user(), CLAUDE_CODE_SESSION_ID=FX_SESSION, GOV_RUNLOG="0",
                         PYTHONIOENCODING="utf-8")

    def run_entry(the_slug=slug, pieces=None if patch else "3"):
        """`--entry-claim` run in the fixture: `(exit, output)`."""
        argv = [bash, driver.as_posix(), "--entry-claim", the_slug, "--request", key]
        argv += ["--pieces", pieces] if pieces is not None else []
        p = subprocess.run(argv, cwd=str(root), capture_output=True, text=True, encoding="utf-8", errors="replace",
                           env=env, timeout=900)
        return p.returncode, (p.stdout + p.stderr).strip()

    def check(what, got, rc, *needles):
        """A miss where `got`, `(exit, output)`, did not exit `rc` or lacks a needle."""
        seen.append("%s exit %d" % (what, got[0]))
        missing = [n for n in needles if n not in got[1]]
        if got[0] != rc or missing:
            bad.append("%s exited %d, owed %d, missing %r: %s" % (what, got[0], rc, missing, got[1][-600:]))

    def read_remote_log(ref):
        """The remote's commits on `ref`, newest first: `[(sha, message)]`."""
        rc, out = read_git(origin, "log", "--first-parent", "--format=%x01%H%x02%B", ref, "--")
        return [tuple(m.split("\x02", 1)) for m in out.split("\x01") if m.strip()] if rc == 0 else []

    def read_head_files(rev):
        """The paths the commit `rev` changed."""
        return sorted(p for p in run_fixture_git(root, "show", "--format=", "--name-only", rev).splitlines() if p)

    claim_ref = "%s/%s" % (CLAIM_NS, slug)
    readme = "memory/builds/%s/README.md" % slug
    if case.startswith("patch-owner"):   # AC1
        got = run_entry()
        check("unratified", got, 1, "owner item: ratify %s" % slug, "patch.ratify", "TOOL-%s-1" % slug)
        if run_fixture_git(root, "log", "-1", "--format=%B").find("Gov-Transition") >= 0:
            bad.append("an unratified patch recorded a transition")
        if case == "patch-owner-rejected":
            read_build_records().write_disposition(str(root), slug, "TOOL-%s-1" % slug, CLAIM_ITEM, "rejected", "prompt")
            run_fixture_git(root, "add", "-A")
            run_fixture_git(root, "commit", "-q", "-m", "the owner's rejection")
            check("rejected", run_entry(), 1, "rejected for good", "patch.ratify")
            if "Gov-Transition" in run_fixture_git(root, "log", "-1", "--format=%B"):
                bad.append("a rejected patch recorded a transition")
        if case == "patch-owner-ratified":
            read_build_records().write_disposition(str(root), slug, "TOOL-%s-1" % slug, CLAIM_ITEM, "ratified", "prompt")
            run_fixture_git(root, "add", "-A")
            run_fixture_git(root, "commit", "-q", "-m", "the owner's ratification")
            check("ratified", run_entry(), 0, "recorded none -> designing · item.plan.dedupe", "claimed by this claimant")
            trailer = run_fixture_git(root, "log", "-1", "--format=%B")
            if "none -> designing" not in trailer or "item=item.plan.dedupe" not in trailer:
                bad.append("the ratified patch's record reads %r" % trailer[-300:])
    elif case == "refusals":   # S1, S4 and S5's refusal branches the other plants do not reach
        write_claim_placement(root, key, "continue", FX_DONE)
        check("continue", run_entry(), 1, "the placement's disposition continue opens no claimed build")
        write_claim_placement(root, key, "patch", FX_DONE)
        check("pieces on a patch", run_entry(pieces="2"), 2, "--pieces names a repeat's count")
        write_claim_placement(root, key, "repeat", NO_VALUE, FX_PLAYBOOK)
        write_fixture_files(root, {"zq-stray.txt": "stray\n"})
        run_fixture_git(root, "add", "--", "zq-stray.txt")
        check("stray staged", run_entry(), 1, "a staged path beyond the scaffold's own, zq-stray.txt")
        if (root / readme).exists():
            bad.append("the refused scaffold wrote %s" % readme)
        run_fixture_git(root, "reset", "-q", "--", "zq-stray.txt")
        check("resumed", run_entry(), 0, "claimed by this claimant", "scaffold committed", "recorded none -> designing")
        write_fixture_files(root, {".governance/policy.toml": '[leases]\noffline = "refuse"\n'})
        run_fixture_git(root, "commit", "-q", "-am", "leases.offline refuse")
        run_fixture_git(root, "push", "-q", FIXTURE_REMOTE, "main")
        run_fixture_git(root, "fetch", "-q", FIXTURE_REMOTE)
        origin.rename(top / "origin.gone")
        got = run_entry(the_slug="dElsewhereNow")
        origin = top / "origin.gone"
        check("offline refused", got, 1, "lease refused — offline · claims/dElsewhereNow")
    elif case == "tombstone-warn":   # AC2
        write_foreign_lease(root, slug)
        lease = "refs/gov/leases/%s/build" % slug
        tip = read_remote_log(lease)[0][0]
        msg = read_remote_log(lease)[0][1].replace("status: live", "status: landed")
        tree = subprocess.run(["git", "mktree"], cwd=str(root), input="", capture_output=True, text=True,
                              encoding="utf-8", check=True, env=read_clean_env()).stdout.strip()
        stone = run_fixture_git(root, "commit-tree", tree, "-p", tip, "-m", msg)
        run_fixture_git(root, "push", "-q", FIXTURE_REMOTE, "%s:%s" % (stone, lease))
        got = run_entry()
        check("tombstone", got, 1, "tombstone", "ask: %s · tombstone · request %s" % (slug, key))
        if got[1].count("ask: ") != 1:
            bad.append("the refusal printed %d ask lines, not one" % got[1].count("ask: "))
        now = read_remote_log(lease)
        seen.append("lease ref at %d commit(s)" % len(now))
        if now[0][0] != stone:
            bad.append("the lease ref moved past the tombstone to %s" % now[0][0][:8])
        if (root / readme).exists():
            bad.append("a tombstoned claim wrote %s" % readme)
    elif case == "claim-twice":   # AC3
        check("first", run_entry(), 0, "claimed %s" % claim_ref, "recorded none -> designing")
        head = run_fixture_git(root, "rev-parse", "HEAD")
        got = run_entry()
        check("second", got, 0, "claimed by this claimant", "first record at")
        if "the local pre-check" in got[1]:
            bad.append("the resumed claim ran the local pre-check")
        read_memory_tree("gen_build_index.py")
        import gen_build_index as gbi
        why = gbi.check_slug_claimed(str(root), gbi.load_conf(str(root)), slug)
        seen.append("check_slug_claimed %s" % ("refuses" if why else "passes"))
        if not why:
            bad.append("check_slug_claimed passes the claimed slug, so the resume proved nothing")
        if len(read_remote_log(claim_ref)) != 1 or run_fixture_git(root, "rev-parse", "HEAD") != head:
            bad.append("the second run moved the claim ref to %d commits or HEAD" % len(read_remote_log(claim_ref)))
    elif case == "slug-minted-locally":   # AC3
        write_fixture_files(root, {"memory/builds/%s/notes.md" % slug: "minted here\n"})
        run_fixture_git(root, "add", "-A")
        run_fixture_git(root, "commit", "-q", "-m", "a local note")
        check("minted", run_entry(), 1, "the local pre-check of a fresh claim")
        if read_remote_log(claim_ref):
            bad.append("a locally minted slug's claim ref was created")
    elif case == "slug-taken":   # AC4
        write_fixture_claim_commit(root, slug, ["claimant-key: %s" % FX_OTHER, "session: s-other", "content-key: %s" % key])
        check("taken", run_entry(), 5, "claimed under another key", "a fresh slug owed")
        rows = [m for _s, m in read_remote_log("refs/gov/requests/%s" % key) if "route-back · %s" % CLAIM_ITEM in m]
        seen.append("%d route-back row(s)" % len(rows))
        if len(rows) != 1:
            bad.append("the request ref holds %d route-back · %s rows, not one" % (len(rows), CLAIM_ITEM))
        if (root / readme).exists():
            bad.append("a taken slug wrote %s" % readme)
        origin.rename(top / "origin.gone")
        got = run_entry(the_slug="dElsewhereNow")
        origin = top / "origin.gone"
        check("offline", got, 4, "claim not written — offline")
        if (root / "memory" / "builds" / "dElsewhereNow").exists():
            bad.append("an unreachable remote's claim wrote a build folder")
    elif case == "repeat-no-pieces":   # AC5
        got = run_entry(pieces=None)
        check("no pieces", got, 2, "--pieces")
        if len([ln for ln in got[1].splitlines() if ln.strip()]) != 1:
            bad.append("the refusal printed %r, not one line" % got[1])
        if read_remote_log(claim_ref) or (root / "memory" / "builds" / slug).exists():
            bad.append("a repeat with no count wrote a claim ref or a build folder")
    elif case == "live-holder":   # AC6
        write_foreign_lease(root, slug)
        check("first", run_entry(), 4, "wait-since", "exit 4 (waiting)")
        log = read_remote_log(claim_ref)
        if len(log) != 2 or "wait-since: " not in log[0][1]:
            bad.append("the claim ref holds %d commit(s), its newest %r" % (len(log), log[0][1][-120:] if log else ""))
        else:
            write_fixture_claim_commit(root, slug, ["wait-since: 2000-01-01T00:00:00Z"], log[0][0])
        got = run_entry()
        check("past the ceiling", got, 1, "owner item: %s · live-holder past flow.wait-ceiling" % slug,
              "claimed by this claimant")
        if "the local pre-check" in got[1]:
            bad.append("the resumed claim ran the local pre-check")
    elif case == "stale-holder":   # TOOL-dPlacedRequest-100 AC1
        write_foreign_lease(root, slug)
        lease = "refs/gov/leases/%s/build" % slug
        tip, planted = read_remote_log(lease)[0]
        # its first sighting 25 hours back, the row `add_claim_sighting` in the unattended suite writes
        feed = pathlib.Path(run_fixture_git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")) / "gov-feed.log"
        rows = feed.read_text(encoding="utf-8").splitlines() if feed.exists() else []
        seq = max([int(r.split("\t", 1)[0]) for r in rows if r.split("\t", 1)[0].isdigit()] or [0]) + 1
        ago = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=25)).strftime(UTC)
        with feed.open("a", encoding="utf-8", newline="\n") as fh:
            fh.write("%d\t%s\tleases\t%s\t%s\t%s\n" % (seq, lease, run_fixture_git(root, "rev-parse", tip + "^{tree}"),
                                                       tip, ago))
        got = run_entry()
        check("stale", got, 0, "take-announced", "the stale build lease taken over", "entry-claim — %s · claimed" % slug)
        epochs = [re.search(r"^epoch: (\d+)$", m, re.M) for m in (planted, (read_remote_log(lease) or [("", "")])[0][1])]
        seen.append("lease epoch %s -> %s" % tuple(e.group(1) if e else "-" for e in epochs))
        if not all(epochs) or int(epochs[1].group(1)) != int(epochs[0].group(1)) + 1:
            bad.append("the lease's epoch is not one above the planted one")
        log = read_remote_log(claim_ref)
        if not log or any("wait-since: " in m for _s, m in log):
            bad.append("the claim ref holds no commit, or one adding wait-since: %r" % [m[-120:] for _s, m in log])
    elif case == "overlap-warn":   # AC6
        run_fixture_git(root, "checkout", "-q", "-b", "other")
        write_fixture_files(root, {"tools/zq-shared/x.txt": "theirs\n"})
        run_fixture_git(root, "add", "-A")
        run_fixture_git(root, "commit", "-q", "-m", "another branch")
        run_fixture_git(root, "push", "-q", FIXTURE_REMOTE, "other")
        run_fixture_git(root, "checkout", "-q", "main")
        write_fixture_files(root, {"tools/zq-shared/x.txt": "ours\n"})
        run_fixture_git(root, "add", "-A")
        run_fixture_git(root, "commit", "-q", "-m", "this run's edit")
        run_fixture_git(root, "fetch", "-q", FIXTURE_REMOTE)
        check("overlap", run_entry(), 0, "overlap noted", "recorded none -> designing")
        log = read_remote_log(claim_ref)
        if not log or "overlap: " not in log[0][1]:
            bad.append("the claim body holds no overlap: key: %r" % (log[0][1][-200:] if log else ""))
    elif case in ("first-record", "first-record-patch"):   # AC7
        got = run_entry()
        check("claim", got, 0, "scaffold committed", "recorded none -> designing")
        trailer = run_fixture_git(root, "log", "-1", "--format=%B")
        files = read_head_files("HEAD~1")
        seen.append("scaffold %s" % " ".join(files))
        if files != sorted([readme, "memory/project/readme-contract.txt"]):
            bad.append("the scaffold commit carries %r" % files)
        if run_fixture_git(root, "log", "-1", "--format=%s", "HEAD~1") != SCAFFOLD_MESSAGE % slug or read_head_files("HEAD"):
            bad.append("the scaffold and the record are not two commits, the record carrying no file")
        owed = ["none -> designing", "item=item.plan.dedupe", "stand-in=dRankedPlan", "scenario=scenario.patch"] if patch \
            else ["none -> designing", "item=item.entry.claim", "scenario=scenario.playbook-run"]
        missing = [o for o in owed if o not in trailer]
        seen.append("trailer %s" % ("holds " + " ".join(owed) if not missing else "lacks " + " ".join(missing)))
        if missing:
            bad.append("the transition trailer lacks %r: %r" % (missing, trailer[-300:]))
        if read_git(root, "diff", "--cached", "--quiet")[0] != 0:
            bad.append("the scaffold was left staged")


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="claim.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run one fixture case, or every case")
    ap.add_argument("--plant", choices=list(PLANTS))
    sub = ap.add_subparsers(dest="verb")
    body = sub.add_parser("body", help="print the claim commit's message")
    for flag in ("--request", "--slug", "--claimant"):
        body.add_argument(flag, required=True)
    body.add_argument("--pieces")
    for verb, what in (("precheck", "the local pre-check of a fresh claim"), ("read", "print the claim body"),
                       ("record", "write the build's first transition record")):
        sub.add_parser(verb, help=what).add_argument("--slug", required=True)
    route = sub.add_parser("route", help="route a lease refusal's cause")
    route.add_argument("--cause", required=True)
    route.add_argument("--slug", required=True)
    scaffold = sub.add_parser("scaffold", help="commit a patch's or a repeat's derived plan record")
    for flag in ("--slug", "--request"):
        scaffold.add_argument(flag, required=True)
    scaffold.add_argument("--pieces")
    args = ap.parse_args(argv)
    if args.fixture:
        if args.verb:
            ap.error("--fixture takes no verb")
        if args.plant:
            return run_claim_plant(args.plant)
        cases = [(p, ["--fixture", "--plant", p], 0, "%s: %s · " % (SAY, p), "· held") for p in PLANTS]
        return run_selftest_cases(main, cases, "%s: fixtures" % SAY)
    if args.plant or args.verb is None:
        ap.error("a verb, body, precheck, read, route, scaffold or record, or --fixture [--plant <case>]")
    if getattr(args, "request", None) is not None and not REQUEST_KEY.fullmatch(args.request):
        print("claim not written — --request %r is no content key of 12 hex digits" % args.request)
        return 2
    try:
        rc, lines = run_claim_verb(args)
    except ClaimRefused as e:
        print(str(e))
        return e.code
    except (LookupError, OSError) as e:
        print("claim not written — unarmed · %s" % e)
        return 2
    for line in lines:
        print(line)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
