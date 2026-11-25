#!/usr/bin/env python3
"""floor.py — the default floor's four invariants, each switched by the policy key `floor` (TOOL-dDeclaredLoop-2).

    python floor.py get <member> [--root <path>]    # prints on or off

`FLOOR_INVARIANTS` is the floor's four members, I11's spelling: `verdict-before-move` (a binding verdict
runs before the default branch moves), `record-changes` (every policy change and stage transition
recorded), `guard-self` (the guard protects its own switch off a live run's branch) and
`no-actor-witness` (no stage witness reads actor-typed state).

`read_floor(repo, rev=None)` reads the `[floor]` table at the landed revision, or at `rev`, through the
policy kit's `read_revision`, found through `read_policy_kit`; the key's catalogue default is derived,
"all on", so no `resolve` answers it and the table is read here. An invalid policy file reads as
`policy-file.on-invalid` says, through the reader. Every absent member reads `on`; a member outside the
four, or a value other than `on` and `off`, is a `LoopError`. Where the policy kit does not resolve or
its reader refuses, every member reads `on` and the reason is printed once, to standard error.

Each member's reader prints `floor: <member> off` and reports instead of refusing at `off`: the
pre-push hook's `gate RED` refusal (`verdict-before-move`); the guard's step 3, its push arm and the
transition check (`record-changes`); the guard's step 2 (`guard-self`); and the two refusals of an
actor witness no list row names (`no-actor-witness`). A member is switched `off` only by a staged change
the guard's step 2 lets through: the owner's terminal commit, or, where the landed `policy-file.guard`
is `agents-with-reason` or `agents-within-mandate`, a live run's commit carrying its change record;
under `owner-only` a live run's is refused (TOOL-dBoundRoles-95).

`get` exits 0 printing `on` or `off`, and 2 printing `floor: refused · <why>` for a member outside the
four or a `[floor]` table that does not hold.

WHAT THIS DOES NOT CHECK: the enforcement each member switches, which its reader owns; a value set on an
unlanded branch, which reads from the landed revision only.
"""
import argparse
import pathlib
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import LoopError, resolve_kit_dir  # noqa: E402
from loop_parents import read_policy_kit  # noqa: E402

SAY = "floor"
FLOOR_INVARIANTS = ("verdict-before-move", "record-changes", "guard-self", "no-actor-witness")
FLOOR_VALUES = ("on", "off")


def read_policy_modules():
    """`read_policy_kit`'s two modules, the policy kit's directory moved to the head of `sys.path` first, so
    its `guard` is never this kit's file of that name; LookupError where the policy kit does not resolve."""
    head = str(resolve_kit_dir("policy", "policy.py", KIT))
    if head in sys.path:
        sys.path.remove(head)
    sys.path.insert(0, head)
    held = sys.modules.get("guard")   # a `guard` imported from elsewhere, this kit's included, is not the policy kit's
    if held is not None and pathlib.Path(getattr(held, "__file__", "") or ".").absolute().parent != pathlib.Path(head):
        del sys.modules["guard"]
    return read_policy_kit()


def derive_all_on(why):
    """Every member `on`, the floor's default, and `why` it was read so printed once to standard error."""
    print("%s: every member reads on · %s" % (SAY, why), file=sys.stderr)
    return {m: "on" for m in FLOOR_INVARIANTS}


def read_floor(repo=".", rev=None):
    """`{member: "on" or "off"}` for each of `FLOOR_INVARIANTS`, read from the policy file at the landed
    revision of `repo`, or at `rev`. LoopError for a member outside the four or a value other than on and
    off; every member `on`, the reason printed once, where the policy kit does not resolve or refuses."""
    try:
        policy, _guard = read_policy_modules()
    except LookupError as e:
        return derive_all_on("the policy kit does not resolve: %s" % e)
    try:
        read = policy.read_revision(str(repo), rev)
        table = read["table"]
        if read["problems"]:   # policy-file.on-invalid decides, through the reader's own fallback
            on_path = policy.parse_key("policy-file.on-invalid")
            policy.resolve_read(on_path, policy.read_catalogue_row(on_path, read["rows"]), read)
            table = read["last_valid"][1]
        path = policy.parse_key("floor")
    except policy.Refusal as e:
        return derive_all_on(str(e))
    floor = {}
    for key, value in sorted((table or {}).items()):
        if key[:len(path)] != path:
            continue
        member = key[len(path):]
        if len(member) != 1 or member[0] not in FLOOR_INVARIANTS:
            raise LoopError(policy.POLICY_REL, "%s is no member of the floor: %s" % (
                policy.render_dotted(key), " ".join(FLOOR_INVARIANTS)))
        if value not in FLOOR_VALUES:
            raise LoopError(policy.POLICY_REL, "%s = %s is neither on nor off" % (
                policy.render_dotted(key), policy.render_json(value)))
        floor[member[0]] = value
    return {m: floor.get(m, "on") for m in FLOOR_INVARIANTS}


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="floor.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    get = sub.add_parser("get", help="print one member's value, on or off")
    get.add_argument("member")
    get.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    if args.member not in FLOOR_INVARIANTS:
        print("%s: refused · %s is no member of the floor: %s" % (SAY, args.member, " ".join(FLOOR_INVARIANTS)))
        return 2
    try:
        print(read_floor(pathlib.Path(args.root))[args.member])
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
