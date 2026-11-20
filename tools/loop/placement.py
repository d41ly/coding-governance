#!/usr/bin/env python3
"""placement.py — a disposition for every request, recorded with its reason, its facts re-checked (TOOL-dPlacedRequest-4).

    python placement.py place --request <key> --return <file> [--reenters <unit id>#<F-id>]
    python placement.py place --request <key> --declared <word> [<build>] [--return <file>] [--reenters <item>]
    python placement.py place --request <key> --owner <disposition record> [--return <file>]
    python placement.py check --request <key>
    python placement.py record --request <key>
    python placement.py --fixture [--plant <case>]

Every verb runs in the repository at the current directory. `<key>` is a request's content key, the twelve
hex digits `request.py` derives, and its record is the node-local file `<git-common-dir>/requests/<key>.placement`
beside the request's local text `<key>.md`: one block per `place`, appended, the newest the placement and the
earlier ones the loop's history. A block is `key: value` lines, ending at a blank line:

    placed-utc · disposition · build · playbook · reason · evidence · observations · placer · scenarios ·
    facts · check · reenters

`disposition` is one member of the loop definition's one closed set, read through `loop_lib.read_dispositions`
and resolved through `resolve_disposition`, so an alias such as `attach` is written as the member it means and
a word outside both is refused naming it. `reason` and `evidence` pass the runlog kit's `render_redacted` and
are cut to `VALUE_CAP` bytes each. `reenters`, the item an owner's late answer re-enters, is written only when a
caller passes it, its shape held by `check_reenters_item`, and a block without it reads `none`.

PLACE. Who places is the policy key `placement`, read through the policy kit's `resolve` at the landed
revision. Under `agent-places` the orientation scout's return, `--return <file>`, is the placement: a block of
`disposition`, `build`, `playbook`, `reason`, `evidence`, `observations`, `scenarios` and `facts` lines, the
observations `; ` joined or `none`, the scenarios the scout found admitted `+` joined, and the request facts
it read as `<name>=<value>` pairs `; ` joined, each name and value one tag segment (TOOL-dPlacedRequest-10). Under `declared-checked` the request's own declaration, `--declared <word> [<build>]`, is
the placement and a return is evidence only. Under `owner-places` `place` writes nothing without `--owner`:
it prints the return as evidence and `placement: owner item — <key>`; with `--owner` the owner's disposition
record naming `item.entry.place-owner` is the placement. Where the return names observations and
`probe.observations` reads `verify-before-place`, `place` opens a probe for each through `probe.py trigger
--cause observation --at item.entry.place` before it writes, and a probe record already holding a verdict is
added to the evidence instead.

CHECK. `check` re-evaluates the newest block's facts from their sources, never from the scout's text, and
writes its verdict into that block's `check:` line: `continue` and `amend` a build that exists, is not
terminal by the memory-tree kit's `derive_status`, and whose build lease the unattended driver's `--claims`
prints free, released, stale or held under this node's fleet tag; `new` the request's words held, its local
text or a prompt record of the named build whose `## The prompt` keys alike; `patch` a terminal build;
`repeat` a playbook path present at HEAD; `unit` refused while `build.unit-holders` is unlanded; `breakpoint`
refused until TOOL-dPlacedRequest-5's check lands; `ask` an ask of the build the evidence names, among the
rows the index generator's `--asks --build` prints; `none` a session card routing no unit. A claimed
observation under `verify-before-place` is `observations-unverified` until its probe record carries a
verdict. A failed fact under `placement.check` = `refuse` prints `placement: refused — <disposition> ·
<fact>` and exits 1, the route back to `item.entry.place`; under `record` it writes `recorded <fact>` and
exits 0. A passed placement whose route enters Plan or Design is held by its `STAND_INS` row: `check` prints
`placement: held-owner`, and the owner item naming the claim ref once `refs/gov/claims/<slug>` exists, until
an owner's disposition record of that build names `item.entry.place` with its word; another word refuses it.

SCENARIOS. `check` re-evaluates every scenario predicate too (TOOL-dPlacedRequest-10). `new`, `amend`,
`patch` and `repeat` select scenarios: the `entry` fact is derived from the disposition by
`derive_entry_fact`, never read from the scout, and a typed `entry` that disagrees is the failed fact
`entry-mismatch <typed> <derived>`. Over the block's facts with that `entry`, the scenario kit's
`derive_admitted_scenarios` answers at HEAD from the scenario composition, gov's pack and the overlay, and
`flow.scenario-default`: a named scenario it does not admit is `scenario-predicate <tag>`, an admitted one
the block does not name `scenario-missing <tag>`, and the shared ones in another order `scenario-order`.
Where none admits, the default is the selection, written `<tag> (default)`, and a block naming none passes.
The other five dispositions select none: a block naming a scenario for one is `scenario-not-placed`. Every
failed fact prints its own line. On a pass, and under `record`, the block's `scenarios:` and `facts:` are
rewritten to the selection and the facts evaluated; `check` prints `placement: facts — <facts>`, and
`placement: scenario · unread · <why>` where the tree holds no scenario composition. A refused default or
composition refuses the check, exit 1.

RECORD. `record` prints the newest block's `disposition`, its `reenters` where it is not `none`, `build`,
`playbook`, `reason`, `scenarios` and `facts` lines, the lines the claim commit carries, when its `check:`
reads `pass` or `recorded`; any other block prints nothing and exits 1.

Exit 0 placed, passed, recorded or held · 1 a refusal, named · 2 a usage error or a kit that does not resolve.
`--fixture --plant <case>` runs one case of `PLANTS` in a throwaway repository under the system temp folder,
printing `placement: <case> · ... · held` or `MISSED`; `--fixture` alone runs every case through
`loop_lib.run_selftest_cases`, the `loop placement fixtures` leg.

WHAT THIS DOES NOT CHECK: that the scout's reason is true, which is why `check` re-reads the facts; that the
request facts the scout read but `entry` are the request's, `check` re-running the predicates over them as
written, so a predicate on a fact the scout never supplies never admits; that two
sessions of one node hold one lease apart, since the claims reader prints a fleet tag and no session; that a
stand-in's later item has landed, its row being deleted by the build that lands it; the `breakpoint`
member's own facts, TOOL-dPlacedRequest-5's; and anything outside this node, the record being node-local.
"""
import argparse
import datetime
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import (SEG, LoopError, read_dispositions, read_memory_tree, resolve_disposition,  # noqa: E402
                      resolve_kit_dir, resolve_memory_root, run_selftest_cases)
from loop_parents import read_policy_kit  # noqa: E402
from loop_witness import read_clean_env, remove_tree, run_fixture_git, write_fixture_files  # noqa: E402
from probe import ProbeRefused, read_build_records, resolve_git_paths  # noqa: E402
from request import KEY_HEX, derive_request_content_key  # noqa: E402

SAY = "placement"
#: A request's content key, as `request.py` derives it.
REQUEST_KEY = re.compile(r"[0-9a-f]{%d}" % KEY_HEX)
#: A block's keys, in the order they are written; `reenters` only where a caller passed an item.
BLOCK_KEYS = ("placed-utc", "disposition", "build", "playbook", "reason", "evidence", "observations", "placer",
              "scenarios", "facts", "check", "reenters")
#: The keys a scout's return may carry.
RETURN_KEYS = ("disposition", "build", "playbook", "reason", "evidence", "observations", "scenarios", "facts")
#: Shared interface I20: the `entry` fact each disposition that selects scenarios derives; the rest select none.
ENTRY_FACTS = {"new": "feature", "amend": "amendment", "patch": "patch", "repeat": "playbook-run"}
#: The mark a selection carries where no scenario admits the request and the default places it.
DEFAULT_MARK = " (default)"
#: The kit home of the kinds register and the namespaces table the fixture's scenario composition copies.
PLAYBOOK_HOME = "playbook"
#: The byte cap on `reason` and `evidence`, after redaction.
VALUE_CAP = 240
#: The item an owner's placement record names, and the item an owner's release of a held placement names.
OWNER_ITEM = "item.entry.place-owner"
PLACE_ITEM = "item.entry.place"
#: The dispositions that open or reopen a build, the ones a claim carries.
NO_VALUE = "none"
#: One row per route a passed placement enters while its step's items are unbuilt (C2-F7): the dispositions
#: it holds, the later item whose landing arms the route, and the build that owns it, which deletes the row.
STAND_INS = ({"route": "step.plan", "dispositions": ("new",), "item": "item.plan.input", "owner": "dRankedPlan"},
             {"route": "step.design", "dispositions": ("amend", "patch", "repeat"), "item": "item.design.reentry",
              "owner": "dIndexedDesign"})
#: The lease verdicts the claims reader prints for a lease nobody holds now.
FREE_VERDICTS = ("released", "terminal", "stale")
SLUG = re.compile(r"[A-Za-z][A-Za-z0-9-]*")
#: The fixture's builds: one live, one closed; its request key and its late answer's item.
FX_LIVE, FX_DONE, FX_NEW, FX_UNIT = "dLive", "dDone", "dFresh", "TOOL-dLive-1"
FX_KEY, FX_ITEM = "3f9c2a71d0e4", "TOOL-tFix-1#F2"
PLANTS = {"each-disposition": "one request placed per member of the set, each with its reason; a reasonless one refused",
          "unknown-word": "adopt refused naming the word and no block written; attach written as amend",
          "agent-places": "placement=agent-places: the scout's return is the placement, placer agent",
          "declared-checked": "placement=declared-checked: the declaration is the placement, placer declared",
          "owner-places": "placement=owner-places: no record prints the owner item and writes nothing; one is placer owner",
          "secret-reason": "a planted token redacted in the reason, and a 1 KB reason cut to 240 bytes",
          "continue-closed": "continue onto a CLOSED build: refused under refuse, recorded under record",
          "amend-leased": "amend onto a build another node's lease holds: refused under refuse, recorded under record",
          "observation": "a claimed observation refused unverified until its probe record carries a verdict",
          "claim-lines": "record prints a passed new and a passed patch block's six lines, scenarios and facts after "
                         "reason, and nothing for a refused block",
          "routes-to-plan": "a passed new placement held for the owner, the owner item naming the claim ref",
          "owner-released": "the owner disposing another word refuses the placement; disposing its own word releases it",
          "prompt-continue": "the driver's prompt-mode check refuses a continue placement and admits a new one",
          "refusals": "each refusal branch the other plants do not reach: a bad key, an unreadable return, a bad "
                      "slug or path, a mismatched mode, each disposition's failing fact and a bad owner record",
          "late-answer": "a re-entering amend kept by check and printed after disposition; a malformed item refused",
          "predicate-fails": "a new placement naming scenario.patch refused scenario-predicate; naming scenario.feature "
                             "it passes",
          "scenario-missing": "a design-only new placement naming scenario.feature alone refused scenario-missing; "
                              "under record its scenarios rewritten to the selection",
          "entry-mismatch": "a new placement typing entry=patch refused entry-mismatch patch feature",
          "continue-with-scenario": "a continue placement naming scenario.feature refused scenario-not-placed",
          "no-admit": "an amend placement over a pack admitting no entry=amendment placed under scenario.feature "
                      "(default) and passed",
          "scenario-refusals": "each scenario refusal the other plants do not reach: a malformed tag or fact, a tag or "
                               "fact twice, the shared scenarios out of order, a default the pack holds no row of and a "
                               "hand-written block's malformed tag at check"}


class PlacementRefused(ValueError):
    """A verb refused: its message is the line's reason; `code` its exit."""

    def __init__(self, why, code=1):
        super().__init__(why)
        self.code = code


# ------------------------------------------------------------------------------------------ the record
def check_reenters_item(value):
    """`value` when it is one `<unit id>#<F-id>`, the `<F-id>` `F` and digits; ValueError naming it otherwise.
    The one check of that shape: TOOL-dFurnishedOrders-16 S9's `check_late_answer` calls it."""
    if not isinstance(value, str) or not re.fullmatch(r"(%s)#F[0-9]+" % read_build_records().ID, value):
        raise ValueError("%r is no <unit id>#<F-id> item, an F-id being F and digits" % (value,))
    return value


def parse_placement_scenarios(text):
    """The scenario tags of a `scenarios:` value, `+` joined, its `(default)` mark dropped; [] for `none` or
    nothing. ValueError naming a tag that is no `scenario.<segment>...` or a tag given twice."""
    text = (text or "").strip()
    if text.endswith(DEFAULT_MARK.strip()):
        text = text[:-len(DEFAULT_MARK.strip())].strip()
    if text in ("", NO_VALUE):
        return []
    tags = [t.strip() for t in text.split("+")]
    for tag in tags:
        head, _sep, rest = tag.partition(".")
        if head != "scenario" or not rest or not all(SEG.fullmatch(s) for s in rest.split(".")):
            raise ValueError("scenarios: %r is no scenario.<segment> tag" % tag)
    if len(set(tags)) != len(tags):
        raise ValueError("scenarios: %s names a scenario twice" % text)
    return tags


def parse_placement_facts(text):
    """`{name: value}` of a `facts:` value, `<name>=<value>` pairs `; ` joined, each name and value one tag
    segment; {} for `none` or nothing. ValueError naming a pair of another shape or a name given twice."""
    text = (text or "").strip()
    if text in ("", NO_VALUE):
        return {}
    facts = {}
    for pair in (p.strip() for p in text.split(";")):
        name, eq, value = pair.partition("=")
        if not (eq and SEG.fullmatch(name) and SEG.fullmatch(value)):
            raise ValueError("facts: %r is no <name>=<value> pair of two tag segments" % pair)
        if name in facts:
            raise ValueError("facts: %s is given twice" % name)
        facts[name] = value
    return facts


def render_placement_facts(facts):
    """`facts`, `{name: value}`, as a `facts:` value: `<name>=<value>` pairs `; ` joined, or `none`."""
    return "; ".join("%s=%s" % kv for kv in facts.items()) or NO_VALUE


def render_capped_value(text):
    """`text` with every secret the runlog kit's `render_redacted` finds replaced, cut to `VALUE_CAP` UTF-8
    bytes at a character boundary. LookupError where the runlog kit does not resolve."""
    runlog = resolve_kit_dir("runlog", "runlog_lib.py", KIT)
    if str(runlog) not in sys.path:
        sys.path.insert(0, str(runlog))
    from runlog_lib import render_redacted
    return render_redacted(text).encode("utf-8")[:VALUE_CAP].decode("utf-8", "ignore").rstrip()


def parse_placement_blocks(path):
    """Every block of the placement file at `path`, oldest first, each `{key: value}`; [] where it is absent."""
    try:
        text = pathlib.Path(path).read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")
    except FileNotFoundError:
        return []
    blocks, cur = [], {}
    for line in text.split("\n") + [""]:
        if not line.strip():
            if cur:
                blocks.append(cur)
            cur = {}
            continue
        key, sep, value = line.partition(": ")
        if sep:
            cur[key.strip()] = value.strip()
    return blocks


def read_placement(path):
    """The newest block of the placement file at `path`, `reenters` read `none` where the block carries no
    such line; None where the file holds no block."""
    blocks = parse_placement_blocks(path)
    if not blocks:
        return None
    return dict(blocks[-1], reenters=blocks[-1].get("reenters") or NO_VALUE)


def render_placement_block(block):
    """`block`'s lines in `BLOCK_KEYS` order, `reenters` only where it is not `none`."""
    return ["%s: %s" % (k, block[k]) for k in BLOCK_KEYS
            if k in block and not (k == "reenters" and block[k] == NO_VALUE)]


def write_placement_blocks(path, blocks):
    """The placement file at `path` rewritten from `blocks`, through a file of this process's own renamed over
    it, so a reader sees the old file or the new one."""
    tmp = path.with_name("%s.%d" % (path.name, os.getpid()))
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n\n".join("\n".join(render_placement_block(b)) for b in blocks) + "\n")
    os.replace(tmp, path)


def add_placement(store, key, fields, placer, reenters=None):
    """Append one block for request `key` to `<store>/<key>.placement`. `fields` holds the return's keys; its
    disposition is resolved to a member, its reason and evidence redacted and capped. `reenters`, when passed,
    is held by `check_reenters_item` before any write. -> the block written. PlacementRefused naming the value
    for a word outside the set, a missing reason or a malformed value; nothing is written then."""
    if reenters is not None:
        try:
            check_reenters_item(reenters)
        except ValueError as e:
            raise PlacementRefused("reenters: %s" % e) from None
    for k, v in fields.items():
        if not isinstance(v, str) or "\n" in v or "\r" in v:
            raise PlacementRefused("%s is not one line" % k)
    word = fields.get("disposition", "").strip()
    if not word:
        raise PlacementRefused("the return carries no disposition")
    try:
        member = resolve_disposition(KIT, word)
    except LoopError as e:
        raise PlacementRefused("the disposition %s is refused: %s" % (word, e)) from None
    reason = fields.get("reason", "").strip()
    if not reason:
        raise PlacementRefused("the disposition %s carries no reason, so the placement would be unrecorded" % member)
    build = fields.get("build", "").strip() or NO_VALUE
    if build != NO_VALUE and not SLUG.fullmatch(build):
        raise PlacementRefused("build %r is no build slug" % build)
    playbook = fields.get("playbook", "").strip() or NO_VALUE
    if playbook != NO_VALUE and (playbook.startswith(("/", "\\")) or ":" in playbook or ".." in playbook.split("/")):
        raise PlacementRefused("playbook %r is no repo-relative path" % playbook)
    observations = fields.get("observations", "").strip()
    count = 0 if observations in ("", NO_VALUE) else len([o for o in observations.split(";") if o.strip()])
    try:
        named = parse_placement_scenarios(fields.get("scenarios"))
        facts = parse_placement_facts(fields.get("facts"))
    except ValueError as e:
        raise PlacementRefused(str(e)) from None
    block = {"placed-utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "disposition": member, "build": build, "playbook": playbook,
             "reason": render_capped_value(reason) or "-",
             "evidence": render_capped_value(fields.get("evidence", "").strip() or NO_VALUE) or NO_VALUE,
             "observations": str(count), "placer": placer, "scenarios": "+".join(named) or NO_VALUE,
             "facts": render_placement_facts(facts), "check": "pending", "reenters": reenters or NO_VALUE}
    store.mkdir(parents=True, exist_ok=True)
    path = store / ("%s.placement" % key)
    write_placement_blocks(path, parse_placement_blocks(path) + [block])
    return block


def read_scout_return(path):
    """`{key: value}` of the scout's return at `path`, its keys among `RETURN_KEYS`. PlacementRefused for an
    unreadable file, a line that is no `key: value`, a key outside them or one given twice."""
    try:
        text = pathlib.Path(path).read_bytes().decode("utf-8-sig").replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as e:
        raise PlacementRefused("the return %s cannot be read: %s" % (path, e)) from None
    fields = {}
    for n, line in enumerate(text.split("\n"), 1):
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        key = key.strip()
        if not sep or key not in RETURN_KEYS:
            raise PlacementRefused("the return's line %d is no key: value of %s" % (n, " ".join(RETURN_KEYS)))
        if key in fields:
            raise PlacementRefused("the return gives %s twice" % key)
        fields[key] = value.strip()
    return fields


def read_owner_record(path):
    """`(disposition, build, record id)` of the owner's disposition record at `path`, which must name
    `OWNER_ITEM` with a member of the set as written. PlacementRefused otherwise."""
    br = read_build_records()
    p = pathlib.Path(path)
    try:
        text = p.read_bytes().decode("utf-8", "replace")
    except OSError as e:
        raise PlacementRefused("the owner's record %s cannot be read: %s" % (path, e)) from None
    rec = br.read_disposition(p.as_posix(), text)
    item, word = rec.get("Item", "").strip("`"), rec.get("Disposition", "").strip("`")
    if rec["malformed"] or item != OWNER_ITEM:
        raise PlacementRefused("%s is no well-formed disposition record naming %s" % (path, OWNER_ITEM))
    if word not in read_dispositions(KIT):
        raise PlacementRefused("the owner's record disposes %s, no member of the set" % word)
    return word, rec.get("build") or NO_VALUE, rec["id"]


def read_placement_policy(root, *keys):
    """`{key: value}` of each policy key, read through the policy kit's `resolve` at the landed revision.
    PlacementRefused (exit 2) on a policy refusal; LookupError where the policy kit does not resolve."""
    policy, _guard = read_policy_kit()
    try:
        return {k: policy.resolve(k, str(root)).value for k in keys}
    except policy.Refusal as e:
        raise PlacementRefused("the policy does not resolve: %s" % e, 2) from None


def read_probe_verdict(store, key):
    """The `Verdict` of the request's entry-time probe record `<key>.probe.md`, or None where it holds none."""
    path = store / ("%s.probe.md" % key)
    if not path.is_file():
        return None
    field = read_build_records().FIELD
    for line in path.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n").split("\n"):
        m = field.match(line)
        if m and m.group(1) == "Verdict":
            return m.group(2).strip()
    return None


def run_observation_probes(root, store, key, subjects):
    """The evidence the probe program adds for `subjects`: the request's probe record where it carries a
    verdict, else one `probe.py trigger` per subject at `PLACE_ITEM`, a trigger already open answering exit 1.
    PlacementRefused (exit 2) where a trigger refuses."""
    verdict = read_probe_verdict(store, key)
    if verdict is not None:
        return ["requests/%s.probe.md %s" % (key, verdict)]
    for subject in subjects:
        p = subprocess.run([sys.executable, str(KIT / "probe.py"), "trigger", "--cause", "observation", "--asker",
                            PLACE_ITEM, "--subject", subject, "--request", key, "--at", PLACE_ITEM],
                           cwd=str(root), capture_output=True, text=True, encoding="utf-8", errors="replace",
                           env=read_clean_env(PYTHONIOENCODING="utf-8"))
        if p.returncode not in (0, 1):
            raise PlacementRefused("the observation probe did not open: %s" % (p.stdout + p.stderr).strip()[-300:], 2)
    return []


def write_placement(args, root, store):
    """The `place` verb: one block written by the value of `placement`, or the owner item printed."""
    value = read_placement_policy(root, "placement", "probe.observations")
    mode, observe = value["placement"], value["probe.observations"]
    fields = read_scout_return(args.ret) if args.ret else {}
    if mode == "owner-places" and not args.owner:
        for k in RETURN_KEYS:
            if k in fields:
                print("%s: evidence — %s: %s" % (SAY, k, render_capped_value(fields[k])))
        print("%s: owner item — %s" % (SAY, args.request))
        return 0
    if (mode == "owner-places") != bool(args.owner) or (mode == "declared-checked") != bool(args.declared):
        raise PlacementRefused("placement is %s, which takes %s" % (mode, {
            "agent-places": "--return and neither --declared nor --owner",
            "declared-checked": "--declared <word> [<build>]",
            "owner-places": "--owner <record>"}.get(mode, "no verb this tool reads")), 2)
    if mode == "agent-places":
        if not args.ret:
            raise PlacementRefused("placement is agent-places, which takes --return <file>", 2)
        placer = "agent"
    elif mode == "declared-checked":
        if len(args.declared) > 2:
            raise PlacementRefused("--declared takes a word and at most one build", 2)
        fields = dict(fields, disposition=args.declared[0],
                      build=args.declared[1] if len(args.declared) == 2 else NO_VALUE,
                      reason=fields.get("reason") or "the request declares %s" % args.declared[0])
        placer = "declared"
    else:
        word, build, rid = read_owner_record(args.owner)
        fields = dict(fields, disposition=word, build=build, reason="the owner's disposition record %s" % rid,
                      evidence="; ".join(x for x in (rid, fields.get("evidence")) if x))
        placer = "owner"
    subjects = [o.strip() for o in fields.get("observations", "").split(";") if o.strip() and o.strip() != NO_VALUE]
    if subjects and observe == "verify-before-place":
        more = run_observation_probes(root, store, args.request, subjects)
        if more:
            fields["evidence"] = "; ".join(x for x in [fields.get("evidence", "")] + more if x and x != NO_VALUE)
    block = add_placement(store, args.request, fields, placer, args.reenters)
    print("%s: placed — %s %s · %s · placer %s · check pending" % (
        SAY, block["disposition"], block["build"], args.request, placer))
    return 0


# ------------------------------------------------------------------------------------------ the facts
def derive_build_status(root, build):
    """The status of `build` by the memory-tree kit's `derive_status` over its README and its specs' headers,
    or None where the build has no README. PlacementRefused where the README or a header does not read."""
    read_memory_tree("gen_build_index.py")
    import gen_build_index
    from loop_transition import read_build_specs
    readme = pathlib.Path(root, resolve_memory_root(root), "builds", build, "README.md")
    if not readme.is_file():
        return None
    try:
        fm = gen_build_index.parse_front_matter(str(readme), build)
        units = [{"status": s} for _uid, s in read_build_specs(build, root) if s]
        return gen_build_index.derive_status(units, fm, readme.as_posix())
    except (gen_build_index.Problem, ValueError, OSError) as e:
        raise PlacementRefused("the build %s's status does not read: %s" % (build, e)) from None


def read_terminal_statuses():
    """The memory-tree kit's TERMINAL statuses."""
    read_memory_tree("tree_lib.py")
    from tree_lib import TERMINAL
    return TERMINAL


def read_build_lease(root, build):
    """None where the build lease of `build` is free or held under this node's fleet tag, as the unattended
    driver's `--claims` prints it, else the fact that fails. An unreadable lease is a fact, never a pass."""
    from breakpoints import run_sourced   # it runs the driver, so here and only for the facts that read a lease
    try:
        rc, out = run_sourced(root, '( load_driver_conf && main --claims ); rc=$?; t=$(resolve_fleet_tag 2>/dev/null)'
                                    ' || t=-; printf "fleet-tag\\t%s\\n" "$t"; exit $rc')
    except (LookupError, OSError, subprocess.TimeoutExpired) as e:
        return "the build lease of %s could not be read: %s" % (build, e)
    lines = [ln.rstrip("\r") for ln in out.splitlines()]
    mine = next((ln.split("\t", 1)[1] for ln in lines if ln.startswith("fleet-tag\t")), "-")
    if rc != 0:
        return "the build lease of %s could not be read: %s" % (build, next(
            (ln for ln in reversed(lines) if ln and not ln.startswith("fleet-tag\t")), "exit %d" % rc))
    if any(ln in ("claims: off", "claims: none") for ln in lines):
        return None
    row = next((ln.split("\t") for ln in lines if ln.split("\t")[0] == build and ln.count("\t") >= 4), None)
    if row is None or row[4] in FREE_VERDICTS:
        return None
    if row[4] in ("live", "held") and row[1] == mine and mine != "-":
        return None
    return "the build lease of %s reads %s, held by %s" % (build, row[4], row[1])


def read_held_prompt(root, build, key):
    """True where a prompt record of `build` holds a `## The prompt` whose words key to `key`."""
    folder = pathlib.Path(root, resolve_memory_root(root), "builds", build, "prompts")
    for rec in sorted(folder.glob("*.md")) if folder.is_dir() else []:
        lines, on, said = rec.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n").split("\n"), False, []
        for line in lines:
            if line.startswith("## "):
                on = line.rstrip() == "## The prompt"
                continue
            if on:
                said.append(line)
        try:
            if said and derive_request_content_key("\n".join(said)) == key:
                return True
        except ValueError:
            continue
    return False


def check_ask_filed(root, build, evidence):
    """None where an id `evidence` names is an ask row the index generator prints for `build`, else the fact."""
    ids = set(re.findall(r"\b%s\b" % read_build_records().ID, evidence))
    gen = pathlib.Path(read_memory_tree("gen_build_index.py")) / "gen_build_index.py"
    p = subprocess.run([sys.executable, str(gen), "--asks", "--build", build], cwd=str(root), capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=read_clean_env(PYTHONIOENCODING="utf-8"))
    if p.returncode != 0:
        return "the asks of %s could not be read: %s" % (build, (p.stdout + p.stderr).strip()[-200:])
    filed = {ln.split("|")[1].strip() for ln in p.stdout.splitlines() if ln.startswith("| ") and ln.count("|") > 2}
    if not ids & filed:
        return "no ask of %s the evidence names is filed" % build
    return None


def read_session_route(common):
    """The units this session's orientation card routes, `- unit:` lines of its `## route` sections; [] with
    no session, no card or no route."""
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    card = pathlib.Path(common, "orientation", "%s.md" % sid)
    if not sid or sid == "absent" or not card.is_file():
        return []
    on, units = False, []
    for line in card.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            on = line.rstrip() == "## route"
        elif on and line.startswith("- unit:"):
            units.append(line[len("- unit:"):].strip())
    return units


def check_disposition_fact(root, common, store, key, block):
    """None where the facts `block`'s disposition rests on hold, read from their sources now, else the fact."""
    word, build = block.get("disposition", ""), block.get("build", NO_VALUE)
    if word in ("continue", "amend", "patch"):
        if build == NO_VALUE:
            return "names no build"
        status = derive_build_status(root, build)
        if status is None:
            return "the build %s does not exist" % build
        terminal = status in read_terminal_statuses()
        if word == "patch":
            return None if terminal else "the build %s is %s, not terminal, so there is nothing to patch" % (build, status)
        if terminal:
            return "the build %s is %s, not live" % (build, status)
        return read_build_lease(root, build)
    if word == "new":
        if (store / ("%s.md" % key)).is_file() or (build != NO_VALUE and read_held_prompt(root, build, key)):
            return None
        return "the request's words are held neither as requests/%s.md nor as a prompt record of %s" % (key, build)
    if word == "repeat":
        path = block.get("playbook", NO_VALUE)
        p = subprocess.run(["git", "cat-file", "-e", "HEAD:%s" % path], cwd=str(root), capture_output=True,
                           env=read_clean_env())
        return None if path != NO_VALUE and p.returncode == 0 else "the playbook %s is not in the tree at HEAD" % path
    if word == "unit":
        return "build.unit-holders is not landed, so the build's driver alone drives its units"
    if word == "breakpoint":
        return "the breakpoint's facts are TOOL-dPlacedRequest-5's check, which is not built"
    if word == "ask":
        return "names no build" if build == NO_VALUE else check_ask_filed(root, build, block.get("evidence", ""))
    if word == "none":
        units = read_session_route(common)
        return "the session's card routes %s, a tracked write" % " ".join(units) if units else None
    return "%s is no disposition this check reads" % word


def read_owner_release(root, build):
    """`(stem, word)` of the owner's newest disposition record of `build` naming `PLACE_ITEM`, or None."""
    if build == NO_VALUE:
        return None
    from adapt import read_disposition_release
    return read_disposition_release(root, build, PLACE_ITEM, ())


def derive_entry_fact(disposition):
    """The `entry` fact `disposition` derives by shared interface I20, `ENTRY_FACTS`; None for a disposition
    that selects no scenario."""
    return ENTRY_FACTS.get(disposition)


def derive_placed_scenarios(facts, rows, default):
    """`(tags, defaulted)`: the scenario kit's `derive_admitted_scenarios` over `facts` and the composed
    `rows`, and whether no row admitted the request, so the default's tag alone is the selection. ValueError
    where `default` names no composed scenario."""
    from scenario import check_default, derive_admitted_scenarios
    fallback = check_default(default, rows)
    probe = "%s(default)" % NO_VALUE   # a row with no predicate, so it is answered only where none admits
    tags = derive_admitted_scenarios(facts, rows + [{"tag": "scenario.%s" % probe}], probe)
    return ([fallback], True) if tags == ["scenario.%s" % probe] else (tags, False)


def check_placement_scenarios(root, block):
    """`(failed facts, scenarios value, facts value, notes)` of `block`'s scenarios re-evaluated: the
    selection's `scenarios:` and the evaluated `facts:` value, both None where nothing was selected, and the
    lines `check` prints before its verdict. PlacementRefused where the composition or the default is
    refused; LookupError where the policy kit does not resolve."""
    from scenario import DEFAULT_KEY, read_scenario_policy, read_scenario_rows
    named = parse_placement_scenarios(block.get("scenarios"))
    entry = derive_entry_fact(block.get("disposition"))
    if entry is None:
        return (["scenario-not-placed %s" % "+".join(named)] if named else []), None, None, []
    facts = parse_placement_facts(block.get("facts"))
    failed = ["entry-mismatch %s %s" % (facts["entry"], entry)] if facts.get("entry", entry) != entry else []
    facts["entry"] = entry
    evaluated = render_placement_facts(facts)
    notes = ["%s: facts — %s" % (SAY, evaluated)]
    try:
        rows = read_scenario_rows(root)
        if rows is None:
            return failed, None, evaluated, notes + [
                "%s: scenario · unread · the scenario composition at HEAD answers unarmed" % SAY]
        want, defaulted = derive_placed_scenarios(facts, rows, read_scenario_policy(root, DEFAULT_KEY, "HEAD"))
    except ValueError as e:
        raise PlacementRefused(str(e)) from None
    failed += ["scenario-predicate %s" % t for t in named if t not in want]
    if not (defaulted and not named):
        failed += ["scenario-missing %s" % t for t in want if t not in named]
    if [t for t in named if t in want] != [t for t in want if t in named]:
        failed.append("scenario-order")
    return failed, "+".join(want) + (DEFAULT_MARK if defaulted else ""), evaluated, notes


def check_placement(root, common, store, key):
    """The `check` verb over request `key`'s newest block. -> `(exit, lines)`, the verdict written into the
    block's `check:` line first, and its `scenarios:` and `facts:` rewritten on a pass or under `record`."""
    path = store / ("%s.placement" % key)
    blocks = parse_placement_blocks(path)
    if not blocks:
        return 1, ["%s: refused — no placement · %s" % (SAY, key)]
    block = blocks[-1]
    value = read_placement_policy(root, "placement.check", "probe.observations")
    fact = None
    if block.get("observations", "0") not in ("0", "") and value["probe.observations"] == "verify-before-place" \
            and read_probe_verdict(store, key) is None:
        fact = "observations-unverified: requests/%s.probe.md carries no verdict" % key
    fact = fact or check_disposition_fact(root, common, store, key, block)
    try:
        failed, chosen, evaluated, notes = check_placement_scenarios(root, block)
    except ValueError as e:   # a malformed line in a block written by hand
        raise PlacementRefused(str(e)) from None
    failed = ([fact] if fact else []) + failed
    word, build = block.get("disposition", "-"), block.get("build", NO_VALUE)
    recorded = value["placement.check"] == "record"
    if not failed or recorded:
        block.update({k: v for k, v in (("scenarios", chosen), ("facts", evaluated)) if v is not None})
    if failed:
        block["check"] = "%s %s" % ("recorded" if recorded else "refused", " · ".join(failed))
        write_placement_blocks(path, blocks)
        return (0 if recorded else 1), notes + ["%s: %s — %s · %s" % (SAY, "recorded" if recorded else "refused",
                                                                         word, f) for f in failed]
    block["check"] = "pass"
    write_placement_blocks(path, blocks)
    row = next((r for r in STAND_INS if word in r["dispositions"]), None)
    answer = read_owner_release(root, build) if row else None
    if answer and answer[1] != word:   # the owner disposed otherwise: a rejection, back to placing
        block["check"] = "refused the owner disposed %s by %s" % (answer[1], answer[0])
        write_placement_blocks(path, blocks)
        return 1, notes + ["%s: refused — %s · the owner disposed %s by %s" % (SAY, word, answer[1], answer[0])]
    if row is None or answer:
        return 0, notes + ["%s: pass — %s %s%s" % (SAY, word, build,
                                                   " · released by %s" % answer[0] if answer else "")]
    lines = []
    claim = "refs/gov/claims/%s" % build
    held = build != NO_VALUE and subprocess.run(["git", "show-ref", "--verify", "--quiet", claim], cwd=str(root),
                                                env=read_clean_env()).returncode == 0
    if held:
        lines.append("%s: owner item — %s %s · claim %s" % (SAY, word, build, claim))
    lines.append("%s: held-owner — %s %s · %s enters %s, whose item %s is unbuilt (%s) · released by an owner "
                 "disposition record naming %s%s" % (SAY, word, build if build != NO_VALUE else key, word, row["route"],
                                                      row["item"], row["owner"], PLACE_ITEM,
                                                      "" if held else " · the owner item follows the claim"))
    return 0, notes + lines


def print_claim_lines(block):
    """The claim lines of `block`: `disposition`, `reenters` where it is not `none`, `build`, `playbook`,
    `reason`, `scenarios` and `facts`, the last two `none` for a block written before TOOL-dPlacedRequest-10.
    -> `(exit, lines)`: 1 and no line for a block whose `check:` is neither `pass` nor `recorded`."""
    if block is None or not (block.get("check") == "pass" or block.get("check", "").startswith("recorded")):
        return 1, []
    keys = ["disposition"] + (["reenters"] if block.get("reenters", NO_VALUE) != NO_VALUE else []) + [
        "build", "playbook", "reason", "scenarios", "facts"]
    return 0, ["%s: %s" % (k, block.get(k, NO_VALUE)) for k in keys]


# ------------------------------------------------------------------------------------------ the fixture
def write_scenario_composition(root, drop=()):
    """A scenario composition written into the fixture `root`, uncommitted: the kinds register and the
    namespaces table of the playbook kit this tree resolves, the scenario schema and gov's pack beside this
    file, each at its place under the tool root, the pack without the scenarios `drop` tags."""
    from loop_items import derive_definition_rel
    from scenario import PACK, render_scenario_row
    kit_rel = pathlib.PurePosixPath(derive_definition_rel()).parent
    playbook = resolve_kit_dir(PLAYBOOK_HOME, "kinds.toml", KIT)
    rows = tomllib.loads((KIT / PACK).read_text(encoding="utf-8")).get("scenario", [])
    files = {(kit_rel.parent / playbook.name / n).as_posix(): (playbook / n).read_text(encoding="utf-8")
             for n in ("kinds.toml", "namespaces.toml")}
    files[(kit_rel / "scenario-schema.toml").as_posix()] = (KIT / "scenario-schema.toml").read_text(encoding="utf-8")
    files[(kit_rel / PACK).as_posix()] = "\n".join(render_scenario_row(r) for r in rows if r.get("tag") not in drop)
    write_fixture_files(root, files)


def write_placement_fixture(top, policy="", driver=False, remote=False, scenarios=None):
    """A repository under `top` holding a live build and a closed one, the stub policy file `policy` and, with
    `driver`, the unattended driver's conf copied from this tree with `RUN_CLAIMS` on where `remote`, a bare
    remote beside it then; with `scenarios`, the tags gov's pack drops there, a scenario composition by
    `write_scenario_composition`, else none. -> the repository."""
    root = top / "repo"
    run_fixture_git(top, "init", "-q", "--template=", str(root))
    run_fixture_git(root, "symbolic-ref", "HEAD", "refs/heads/main")
    fm = "---\nslug: %s\nnode: a\nopened: 2026-11-01\nstreams: tooling\nroster: TOOL\nids: TOOL-%s-1\n---\n\n# %s\n"
    spec = "# TOOL-%s-1 — a unit\n\n**Status:** %s · rev-1 · 2026-11-01 · node a · Tier-2 · base 0123abcd\n"
    files = {".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\nBACKLOG_MODE=builds\n',
             ".governance/policy.toml": policy, "memory/project/stale-header-waiver.txt": "",
             "memory/builds/%s/BACKLOG.md" % FX_LIVE: "# %s — asks\n\n## Asks\n\n- TOOL-%s-9 · filed 2026-11-01 · an "
                                                      "ask filed against the live build\n" % (FX_LIVE, FX_LIVE)}
    for build, status in ((FX_LIVE, "INPROGRESS"), (FX_DONE, "CLOSED")):
        files["memory/builds/%s/README.md" % build] = fm % (build, build, build)
        files["memory/builds/%s/spec/2026-11-01-spec-TOOL-%s-1.md" % (build, build)] = spec % (build, status)
    if driver:
        src = next((d for d in (KIT, *KIT.parents) if (d / ".unattended.conf").is_file()), None)
        if src is None:
            raise LookupError("the driver plants copy .unattended.conf from this tree, which holds none")
        files[".unattended.conf"] = (src / ".unattended.conf").read_text(encoding="utf-8") + \
            '\nSPEC_TOKENS_CLI=""\nRUN_CLAIMS="%s"\n' % ("on" if remote else "off")
    write_fixture_files(root, files)
    if scenarios is not None:
        write_scenario_composition(root, scenarios)
    run_fixture_git(root, "add", "-A")
    run_fixture_git(root, "commit", "-q", "-m", "the placement fixture")
    if remote:
        run_fixture_git(top, "init", "-q", "--bare", "--template=", str(top / "origin.git"))
        run_fixture_git(root, "remote", "add", "origin", str(top / "origin.git"))
        run_fixture_git(root, "push", "-q", "origin", "main")
        run_fixture_git(root, "fetch", "-q", "origin")
    return root


def write_foreign_lease(root, build):
    """A build lease of `build` held live by another node's fleet tag, pushed to the fixture's remote."""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    msg = "gov-claim %s/build\n\n" % build + "".join("%s: %s\n" % kv for kv in (
        ("slug", build), ("node", "z"), ("host", "elsewhere"), ("session", "s-other"), ("keepalive", "k-other"),
        ("status", "live"), ("lease-utc", now), ("beat-utc", now), ("epoch", "1"), ("kind", "build"),
        ("fleet-tag", "z"), ("renews", "yes")))
    tree = subprocess.run(["git", "mktree"], cwd=str(root), input="", capture_output=True, text=True, encoding="utf-8", check=True,
                          env=read_clean_env()).stdout.strip()
    sha = run_fixture_git(root, "commit-tree", tree, "-m", msg)
    run_fixture_git(root, "push", "-q", "origin", "%s:refs/gov/leases/%s/build" % (sha, build))


def run_placement_command(root, *argv, session="absent"):
    """This script as a process in `root` under the session id `session`: `(exit, stdout and stderr)`."""
    p = subprocess.run([sys.executable, str(pathlib.Path(__file__).absolute()), *argv], cwd=str(root),
                       capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=read_clean_env(PYTHONIOENCODING="utf-8", CLAUDE_CODE_SESSION_ID=session))
    return p.returncode, (p.stdout + p.stderr).strip()


def run_placement_plant(case):
    """One case of `PLANTS`: its `placement: <case> · ... · held` or `MISSED` line; 0 held, 1 missed."""
    top = pathlib.Path(tempfile.mkdtemp(prefix="pl-")).absolute()
    seen, bad = [], []
    try:
        check_placement_plant(case, top, seen, bad)
    except (subprocess.CalledProcessError, OSError, LookupError, ValueError) as e:
        bad.append("the plant could not run: %s" % (getattr(e, "stderr", None) or e))
    finally:
        remove_tree(top)
    print("%s: %s · %s · %s" % (SAY, case, " · ".join(seen) or "-", "held" if not bad else "MISSED " + "; ".join(bad)))
    return 0 if not bad else 1


def check_placement_plant(case, top, seen, bad):
    """Run `case` in a fixture under `top`, appending each observation to `seen` and each miss to `bad`."""
    policy = {"agent-places": '', "declared-checked": 'placement = "declared-checked"\n',
              "owner-places": 'placement = "owner-places"\n'}.get(case, "")
    driver = case in ("amend-leased", "late-answer", "prompt-continue", "continue-with-scenario", "no-admit")
    scenarios = {"predicate-fails": (), "scenario-missing": (), "entry-mismatch": (), "continue-with-scenario": (),
                 "no-admit": ("scenario.amendment",), "claim-lines": (),
                 "scenario-refusals": ("scenario.amendment",)}.get(case)
    root = write_placement_fixture(top, policy, driver=driver, remote=case == "amend-leased", scenarios=scenarios)
    store = pathlib.Path(run_fixture_git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")) / "requests"
    rets = top / "returns"
    rets.mkdir()

    def write_request_text():
        """The request's local text, as the driver's `--request` keeps it."""
        write_fixture_files(store, {"%s.md" % FX_KEY: "make it so\n"})

    def write_return(name, **fields):
        path = rets / ("%s.txt" % name)
        path.write_text("".join("%s: %s\n" % kv for kv in fields.items()), encoding="utf-8", newline="\n")
        return str(path)

    def check_case(what, got, rc, *needles):
        """One observation: `got`, `(exit, output)`, owed `rc` and an output holding every needle."""
        seen.append("%s exit %d" % (what, got[0]))
        if got[0] != rc or not all(n in got[1] for n in needles):
            bad.append("%s: exit %d, owed %d holding %s: %s" % (what, got[0], rc, " and ".join(map(repr, needles)),
                                                                 got[1][-300:]))

    def read_newest_block(key=FX_KEY):
        return read_placement(store / ("%s.placement" % key)) or {}

    def run_placed_return(key=FX_KEY, *more, **fields):
        return run_placement_command(root, "place", "--request", key, "--return", write_return(key, **fields), *more)

    def write_policy_commit(text):
        write_fixture_files(root, {".governance/policy.toml": text})
        run_fixture_git(root, "commit", "-q", "-am", "policy")
        if case == "amend-leased":
            run_fixture_git(root, "push", "-q", "origin", "main")
            run_fixture_git(root, "fetch", "-q", "origin")

    if case == "each-disposition":   # AC1
        members = read_dispositions(KIT)
        for n, word in enumerate(members):
            key = "%012x" % (0xa00 + n)
            check_case(word, run_placed_return(key, disposition=word, build=FX_LIVE, reason="placed as %s" % word), 0,
                   "placement: placed — %s" % word)
            got = read_newest_block(key)
            if got.get("disposition") != word or not got.get("reason"):
                bad.append("%s's block reads %s" % (word, got))
        check_case("no reason", run_placed_return("%012x" % 0xaff, disposition="new", build=FX_NEW), 1, "carries no reason")
        if (store / ("%012x.placement" % 0xaff)).exists():
            bad.append("a reasonless placement wrote a block")
    elif case == "unknown-word":   # AC2
        check_case("adopt", run_placed_return(disposition="adopt", reason="r"), 1, "adopt")
        if (store / ("%s.placement" % FX_KEY)).exists():
            bad.append("adopt wrote a block")
        check_case("attach", run_placed_return(disposition="attach", build=FX_LIVE, reason="r"), 0, "placed — amend")
        if read_newest_block().get("disposition") != "amend":
            bad.append("attach was written as %s" % read_newest_block().get("disposition"))
    elif case in ("agent-places", "declared-checked", "owner-places"):   # AC3
        ret = write_return("scout", disposition="continue", build=FX_LIVE, reason="the scout read it as continue")
        if case == "agent-places":
            check_case("place", run_placement_command(root, "place", "--request", FX_KEY, "--return", ret), 0, "placer agent")
            want = ("agent", "continue")
        elif case == "declared-checked":
            check_case("place", run_placement_command(root, "place", "--request", FX_KEY, "--declared", "new", FX_NEW,
                                                  "--return", ret), 0, "placer declared")
            want = ("declared", "new")
        else:
            check_case("no record", run_placement_command(root, "place", "--request", FX_KEY, "--return", ret), 0,
                   "placement: owner item — %s" % FX_KEY, "evidence — disposition: continue")
            if (store / ("%s.placement" % FX_KEY)).exists():
                bad.append("owner-places with no record wrote a block, taking the scout's return as the placement")
            rel = read_build_records().write_disposition(str(root), FX_LIVE, FX_UNIT, OWNER_ITEM, "amend", "terminal")
            check_case("the owner's record", run_placement_command(root, "place", "--request", FX_KEY, "--owner",
                                                               str(root / rel), "--return", ret), 0, "placer owner")
            want = ("owner", "amend")
        got = read_newest_block()
        if (got.get("placer"), got.get("disposition")) != want:
            bad.append("the block reads placer %s disposition %s, owed %s %s" % (
                got.get("placer"), got.get("disposition"), *want))
    elif case == "secret-reason":   # AC5
        token = "ghp_" + "a1B2" * 9
        run_placed_return(disposition="new", build=FX_NEW, reason="the owner pasted %s into the request" % token)
        got = read_newest_block()
        seen.append("reason %s" % got.get("reason", "")[:60])
        if token in got.get("reason", "") or "<redacted:" not in got.get("reason", ""):
            bad.append("the reason was written raw: %s" % got.get("reason"))
        run_placed_return("%012x" % 0xb0b, disposition="new", build=FX_NEW, reason="x" * 1024)
        size = len(read_newest_block("%012x" % 0xb0b).get("reason", "").encode("utf-8"))
        seen.append("a 1024-byte reason written as %d bytes" % size)
        if size != VALUE_CAP:
            bad.append("a 1 KB reason was written as %d bytes, not %d" % (size, VALUE_CAP))
    elif case in ("continue-closed", "amend-leased"):   # AC6
        word, build = ("continue", FX_DONE) if case == "continue-closed" else ("amend", FX_LIVE)
        if case == "amend-leased":
            write_foreign_lease(root, FX_LIVE)
        run_placed_return(disposition=word, build=build, reason="the scout says %s is live and free" % build)
        fact = "is CLOSED, not live" if case == "continue-closed" else "the build lease of %s reads" % FX_LIVE
        check_case("refuse", run_placement_command(root, "check", "--request", FX_KEY), 1,
               "placement: refused — %s" % word, fact)
        write_policy_commit('[placement]\ncheck = "record"\n')
        check_case("record", run_placement_command(root, "check", "--request", FX_KEY), 0, "placement: recorded — %s" % word)
        if not read_newest_block().get("check", "").startswith("recorded "):
            bad.append("the block's check reads %s, not recorded" % read_newest_block().get("check"))
        if case == "amend-leased":   # a lease the reader cannot read is a fact, never a pass
            run_fixture_git(root, "remote", "remove", "origin")
            check_case("unreadable", run_placement_command(root, "check", "--request", FX_KEY), 0,
                       "placement: recorded — amend", "could not be read")
    elif case == "observation":   # AC7
        write_request_text()
        check_case("place", run_placed_return(disposition="new", build=FX_NEW, reason="r", observations="the card drops its route"),
               0, "placed — new")
        if not (store / ("%s.probe-trigger.md" % FX_KEY)).is_file():
            bad.append("no probe was opened for the observation")
        check_case("unverified", run_placement_command(root, "check", "--request", FX_KEY), 1, "observations-unverified")
        (store / ("%s.probe.md" % FX_KEY)).write_text("# probe\n\n- **Verdict:** confirmed\n", encoding="utf-8")
        check_case("verified", run_placement_command(root, "check", "--request", FX_KEY), 0, "held-owner — new",
                   "placement: scenario · unread")   # the fixture holds no scenario composition
    elif case == "claim-lines":   # AC8, and TOOL-dPlacedRequest-10 AC7
        write_request_text()
        run_placed_return(disposition="new", build=FX_NEW, reason="a new widget", evidence="memory/x.md#widget",
                          scenarios="scenario.feature")
        run_placement_command(root, "check", "--request", FX_KEY)
        got = run_placement_command(root, "record", "--request", FX_KEY)
        owed = ["disposition: new", "build: %s" % FX_NEW, "playbook: none", "reason: a new widget",
                "scenarios: scenario.feature", "facts: entry=feature"]
        check_case("record pass", got, 0, *owed)
        if got[1].splitlines() != owed:
            bad.append("record printed %r, not exactly %r" % (got[1].splitlines(), owed))
        run_placed_return(disposition="patch", build=FX_DONE, reason="the landed fix regressed",
                          scenarios="scenario.patch", facts="entry=patch; design-only=false")
        check_case("patch check", run_placement_command(root, "check", "--request", FX_KEY), 0, "held-owner — patch")
        got = run_placement_command(root, "record", "--request", FX_KEY)
        owed = ["disposition: patch", "build: %s" % FX_DONE, "playbook: none", "reason: the landed fix regressed",
                "scenarios: scenario.patch", "facts: entry=patch; design-only=false"]
        check_case("record patch", got, 0)
        if got[1].splitlines() != owed:
            bad.append("record printed %r, not exactly %r" % (got[1].splitlines(), owed))
        run_placed_return(disposition="patch", build=FX_LIVE, reason="r", scenarios="scenario.patch")
        check_case("refused", run_placement_command(root, "check", "--request", FX_KEY), 1, "refused — patch")
        got = run_placement_command(root, "record", "--request", FX_KEY)
        check_case("record refused", got, 1)
        if got[1]:
            bad.append("record printed %r for a refused block" % got[1])
    elif case in ("routes-to-plan", "owner-released"):   # AC9
        write_request_text()
        run_placed_return(disposition="new", build=FX_LIVE, reason="a new build")
        run_fixture_git(root, "update-ref", "refs/gov/claims/%s" % FX_LIVE, "HEAD")
        if case == "routes-to-plan":
            check_case("held", run_placement_command(root, "check", "--request", FX_KEY), 0,
                   "held-owner — new %s" % FX_LIVE, "owner item — new %s · claim refs/gov/claims/%s" % (FX_LIVE, FX_LIVE))
        else:
            read_build_records().write_disposition(str(root), FX_LIVE, FX_UNIT, PLACE_ITEM, "ask", "terminal")
            run_fixture_git(root, "add", "-A")
            run_fixture_git(root, "commit", "-q", "-m", "the owner's rejection")
            check_case("rejected", run_placement_command(root, "check", "--request", FX_KEY), 1,
                       "placement: refused — new · the owner disposed ask by ")
            read_build_records().write_disposition(str(root), FX_LIVE, FX_UNIT, PLACE_ITEM, "new", "terminal")
            run_fixture_git(root, "add", "-A")
            run_fixture_git(root, "commit", "-q", "-m", "the owner's release")
            got = run_placement_command(root, "check", "--request", FX_KEY)
            check_case("released", got, 0, "placement: pass — new %s" % FX_LIVE)
            if "held-owner" in got[1]:
                bad.append("a released placement is still held")
    elif case == "prompt-continue":   # AC10
        from breakpoints import run_sourced
        rec = "memory/builds/%s/prompts/2026-11-01-prompt-mandate.md" % FX_NEW
        fm = "---\nslug: %s\nnode: a\nopened: 2026-11-01\nstreams: tooling\nroster: TOOL\nids: TOOL-%s-1\n" \
             "authorized-by: prompt\n---\n\n# %s\n" % (FX_NEW, FX_NEW, FX_NEW)
        write_request_text()
        for word, build, rc in (("continue", FX_LIVE, 1), ("new", FX_NEW, 0)):
            write_fixture_files(root, {"memory/builds/%s/README.md" % FX_NEW: fm, rec: (
                "# Run mandate\n\n## The prompt\n\n> make it so\n\n## Placement\n\nrequest: %s\ndisposition: %s\n"
                "build: %s\n" % (FX_KEY, word, build))})
            if word == "new":
                run_placed_return(disposition="new", build=FX_NEW, reason="the prompt opens a build")
            run_fixture_git(root, "add", "-A")
            run_fixture_git(root, "commit", "-q", "-m", "the prompt record, %s" % word)
            base = run_fixture_git(root, "rev-parse", "HEAD")
            got = run_sourced(root, 'load_driver_conf || exit 2; AUTH_MODE=prompt; AUTH_CONF_AT=%s; '
                                    'check_prompt_placement %s %s' % (base, FX_NEW, base))
            if rc:
                check_case(word, got, 1, "UNATTENDED check 119 FAILED", "the disposition continue", FX_LIVE)
            else:
                check_case(word, got, 0)
                if "check 119" in got[1]:
                    bad.append("a passed new placement was refused: %s" % got[1][-300:])
    elif case == "refusals":   # every refusal branch the plants above do not reach
        check_case("bad key", run_placement_command(root, "check", "--request", "XYZ"), 2, "no content key")
        check_case("no placement", run_placement_command(root, "check", "--request", FX_KEY), 1,
                   "refused — no placement")
        ret = rets / "odd.txt"
        for what, text, owed in (("odd line", "a sentence with no key\n", "is no key: value"),
                                 ("twice", "reason: a\nreason: b\n", "gives reason twice")):
            ret.write_text(text, encoding="utf-8")
            check_case(what, run_placement_command(root, "place", "--request", FX_KEY, "--return", str(ret)), 1, owed)
        check_case("slug", run_placed_return(disposition="new", build="../x", reason="r"), 1, "is no build slug")
        check_case("playbook", run_placed_return(disposition="repeat", playbook="../etc/pb.md", reason="r"), 1,
                   "no repo-relative path")
        check_case("declared", run_placement_command(root, "place", "--request", FX_KEY, "--declared", "new"), 2,
                   "placement is agent-places")
        if (store / ("%s.placement" % FX_KEY)).exists():
            bad.append("a refused place wrote a block")
        card = pathlib.Path(store.parent, "orientation", "s-fx.md")
        write_fixture_files(card.parent, {card.name: "# card\n\n## route\n- build: %s\n- unit: %s\n" % (FX_LIVE, FX_UNIT)})
        for n, (fields, fact) in enumerate((
                ({"disposition": "unit", "build": FX_LIVE}, "build.unit-holders is not landed"),
                ({"disposition": "breakpoint", "build": FX_LIVE}, "TOOL-dPlacedRequest-5"),
                ({"disposition": "repeat", "playbook": "playbooks/none.md"}, "not in the tree at HEAD"),
                ({"disposition": "ask", "build": FX_LIVE, "evidence": "TOOL-%s-8" % FX_LIVE}, "no ask of %s" % FX_LIVE),
                ({"disposition": "none"}, "routes %s" % FX_UNIT),
                ({"disposition": "new", "build": FX_NEW}, "held neither"),
                ({"disposition": "patch", "build": FX_NEW}, "%s does not exist" % FX_NEW),
                ({"disposition": "continue"}, "names no build"))):
            key = "%012x" % (0xc00 + n)
            run_placed_return(key, reason="the scout's word", **fields)
            check_case(fields["disposition"], run_placement_command(root, "check", "--request", key, session="s-fx"), 1,
                       "placement: refused — %s" % fields["disposition"], fact)
        run_placed_return("%012x" % 0xcff, disposition="ask", build=FX_LIVE, reason="r",
                          evidence="TOOL-%s-9; TOOL-%s-90" % (FX_LIVE, FX_LIVE))
        check_case("ask filed", run_placement_command(root, "check", "--request", "%012x" % 0xcff), 0, "pass — ask")
        write_policy_commit('placement = "owner-places"\n')
        check_case("owner not a record", run_placement_command(root, "place", "--request", FX_KEY, "--owner",
                                                               str(rets / "odd.txt")), 1, "no well-formed disposition record")
        rel = read_build_records().write_disposition(str(root), FX_LIVE, FX_UNIT, OWNER_ITEM, "adopt", "terminal")
        check_case("owner word", run_placement_command(root, "place", "--request", FX_KEY, "--owner", str(root / rel)),
                   1, "disposes adopt, no member")
    elif case == "late-answer":   # AC12
        try:
            add_placement(store, FX_KEY, {"disposition": "amend", "build": FX_LIVE, "reason": "r"}, "owner",
                          FX_ITEM.split("#")[0])
            bad.append("reenters TOOL-tFix-1 was not refused")
        except PlacementRefused as e:
            seen.append("TOOL-tFix-1 refused: %s" % str(e)[:60])
        if (store / ("%s.placement" % FX_KEY)).exists():
            bad.append("a malformed item wrote a block")
        add_placement(store, FX_KEY, {"disposition": "amend", "build": FX_LIVE, "reason": "the owner's late answer"},
                      "owner", FX_ITEM)
        if read_newest_block().get("reenters") != FX_ITEM:
            bad.append("read_placement returned reenters %s" % read_newest_block().get("reenters"))
        check_case("check", run_placement_command(root, "check", "--request", FX_KEY), 0, "— amend %s" % FX_LIVE)
        if read_newest_block().get("check") != "pass" or read_newest_block().get("reenters") != FX_ITEM:
            bad.append("check did not pass keeping the reenters line: %s" % read_newest_block())
        got = run_placement_command(root, "record", "--request", FX_KEY)
        lines = got[1].splitlines()
        if lines[:2] != ["disposition: amend", "reenters: %s" % FX_ITEM]:
            bad.append("record printed %r, the item not right after disposition" % lines)
        add_placement(store, FX_KEY, {"disposition": "amend", "build": FX_LIVE, "reason": "a plain amend"}, "agent")
        if read_newest_block().get("reenters") != NO_VALUE:
            bad.append("a block without the line read %s" % read_newest_block().get("reenters"))
        run_placement_command(root, "check", "--request", FX_KEY)
        got = run_placement_command(root, "record", "--request", FX_KEY)
        check_case("record plain", got, 0, "disposition: amend", "reason: a plain amend")
        if "reenters:" in got[1]:
            bad.append("a block without the line printed one: %s" % got[1])
    elif case in ("predicate-fails", "scenario-missing", "entry-mismatch"):   # TOOL-dPlacedRequest-10 AC1 to AC3
        write_request_text()
        named, facts, owed = {"predicate-fails": ("scenario.patch", "none", "scenario-predicate scenario.patch"),
                              "scenario-missing": ("scenario.feature", "design-only=true",
                                                   "scenario-missing scenario.design-only"),
                              "entry-mismatch": ("scenario.feature", "entry=patch", "entry-mismatch patch feature")}[case]
        run_placed_return(disposition="new", build=FX_NEW, reason="a new widget", scenarios=named, facts=facts)
        check_case("refuse", run_placement_command(root, "check", "--request", FX_KEY), 1,
                   "placement: refused — new · %s" % owed)
        if case == "predicate-fails":
            run_placed_return(disposition="new", build=FX_NEW, reason="a new widget", scenarios="scenario.feature")
            check_case("named right", run_placement_command(root, "check", "--request", FX_KEY), 0, "held-owner — new")
            if read_newest_block().get("check") != "pass":
                bad.append("the right scenario's block reads check %s" % read_newest_block().get("check"))
        elif case == "scenario-missing":
            write_policy_commit('[placement]\ncheck = "record"\n')
            check_case("record", run_placement_command(root, "check", "--request", FX_KEY), 0,
                       "placement: recorded — new · %s" % owed)
            got = read_newest_block().get("scenarios")
            seen.append("scenarios %s" % got)
            if got != "scenario.feature+scenario.design-only":
                bad.append("under record the block's scenarios read %s, not the selection" % got)
    elif case == "continue-with-scenario":   # TOOL-dPlacedRequest-10 AC4
        run_placed_return(disposition="continue", build=FX_LIVE, reason="r")
        check_case("no scenario", run_placement_command(root, "check", "--request", FX_KEY), 0, "pass — continue")
        run_placed_return(disposition="continue", build=FX_LIVE, reason="r", scenarios="scenario.feature")
        check_case("named", run_placement_command(root, "check", "--request", FX_KEY), 1,
                   "placement: refused — continue · scenario-not-placed scenario.feature")
    elif case == "no-admit":   # TOOL-dPlacedRequest-10 AC6
        run_placed_return(disposition="amend", build=FX_LIVE, reason="widen the live build")
        check_case("check", run_placement_command(root, "check", "--request", FX_KEY), 0, "held-owner — amend",
                   "facts — entry=amendment")
        got = read_newest_block()
        seen.append("scenarios %s" % got.get("scenarios"))
        if (got.get("scenarios"), got.get("check")) != ("scenario.feature (default)", "pass"):
            bad.append("the block reads scenarios %s check %s, owed scenario.feature (default) pass" % (
                got.get("scenarios"), got.get("check")))
    elif case == "scenario-refusals":   # every scenario refusal branch the plants above do not reach
        write_request_text()
        for what, fields, owed in (("tag", {"scenarios": "feature"}, "no scenario.<segment> tag"),
                                   ("tag twice", {"scenarios": "scenario.feature+scenario.feature"}, "twice"),
                                   ("fact", {"facts": "design only"}, "no <name>=<value> pair"),
                                   ("fact twice", {"facts": "a=b; a=c"}, "facts: a is given twice")):
            check_case(what, run_placed_return(disposition="new", build=FX_NEW, reason="r", **fields), 1, owed)
        if (store / ("%s.placement" % FX_KEY)).exists():
            bad.append("a malformed scenario or fact wrote a block")
        run_placed_return(disposition="new", build=FX_NEW, reason="r", facts="design-only=true",
                          scenarios="scenario.design-only+scenario.feature")
        check_case("order", run_placement_command(root, "check", "--request", FX_KEY), 1,
                   "placement: refused — new · scenario-order")
        write_policy_commit('[flow]\nscenario-default = "amendment"\n')   # a value the pack here holds no row of
        check_case("default", run_placement_command(root, "check", "--request", FX_KEY), 1, "flow.scenario-default",
                   "scenario.amendment is not in the scenario composition")
        hand = store / ("%s.placement" % FX_KEY)   # a block written by hand, past place's own refusal
        hand.write_bytes(hand.read_bytes() + ("\ndisposition: new\nbuild: %s\nreason: r\nscenarios: feature\n"
                                              % FX_NEW).encode("utf-8"))
        check_case("hand-written", run_placement_command(root, "check", "--request", FX_KEY), 1,
                   "no scenario.<segment> tag")


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="placement.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run one fixture case, or every case")
    ap.add_argument("--plant", choices=list(PLANTS))
    sub = ap.add_subparsers(dest="verb")
    pl = sub.add_parser("place", help="write one placement block")
    pl.add_argument("--request", required=True)
    pl.add_argument("--return", dest="ret")
    pl.add_argument("--declared", nargs="+")
    pl.add_argument("--owner")
    pl.add_argument("--reenters")
    for verb, what in (("check", "re-check the newest block's facts"), ("record", "print the claim lines")):
        sub.add_parser(verb, help=what).add_argument("--request", required=True)
    args = ap.parse_args(argv)
    if args.fixture:
        if args.verb:
            ap.error("--fixture takes no verb")
        if args.plant:
            return run_placement_plant(args.plant)
        cases = [(p, ["--fixture", "--plant", p], 0, "%s: %s · " % (SAY, p), "· held") for p in PLANTS]
        return run_selftest_cases(main, cases, "%s: fixtures" % SAY)
    if args.plant or args.verb is None:
        ap.error("a verb, place, check or record, or --fixture [--plant <case>]")
    if not REQUEST_KEY.fullmatch(args.request):
        print("%s — refused · --request %r is no content key of %d hex digits" % (SAY, args.request, KEY_HEX))
        return 2
    try:
        root, common = resolve_git_paths()
        store = common / "requests"
        if args.verb == "place":
            return write_placement(args, root, store)
        if args.verb == "check":
            rc, lines = check_placement(root, common, store, args.request)
        else:
            rc, lines = print_claim_lines(read_placement(store / ("%s.placement" % args.request)))
        for line in lines:
            print(line)
        return rc
    except (PlacementRefused, ProbeRefused) as e:
        print("%s — refused · %s" % (SAY, e))
        return e.code
    except (LookupError, LoopError, OSError) as e:
        print("%s — refused · unarmed · %s" % (SAY, e))
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
