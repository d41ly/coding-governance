#!/usr/bin/env python3
"""composition.py — a build's composition pinned per step, read at the pin, and moved at the next step
boundary (TOOL-dDeclaredLoop-26).

    python composition.py --fixture --plant <case>
    python composition.py --selftest

THE PIN. A build runs each step under the composition it entered that step with. The composition
revision is the commit HEAD names when a move is recorded (`derive_composition_revision`), and
`loop_transition.py`'s writer records its first eight hex digits as the move's `composition` field, on
its trailer and its log record; a `--field composition=<value>` is refused, the value being derived.
`read_step_composition(root, moves)` answers `(commit, state)` for a build's moves, newest first: the
newest move's pin, `pinned`, or HEAD's commit, `unpinned`, where no move or the newest carries none.

THE READ AT THE PIN. `read_composition_at(root, rev)` answers what `loop_items.read_composition` answers,
composed at `rev`: in place where `rev` is HEAD's commit, otherwise in a scratch worktree detached at
`rev` under the host temp directory, removed in a `finally`, so every read the `compose --kind item`
verb makes at HEAD reads the pin while the code that runs is this tree's. `loop_items.read_composed_items`
takes the revision and reads through it, and `position.py` reads a build's items there. Its `kind` and
`rows` reach the verb's `--kind` and `--rows -`, so `scenario.py` reads the scenario composition at a
pin and hands a placed scenario's activated rows to their kind's composition (TOOL-dDeclaredLoop-27).

THE CARRY. A tag absent from the composition at a pin is redirected when the one tag resolver, the
playbook kit's `gov_tag.py show <tag> --json`, found under the repository being read, answers exactly one
successor for it and that successor is in the same composition (`derive_successor`).
`read_tag_successors(root, tag)` answers the `Successor` line of the tag's `retired` rows as a list, `[]`
for an ending with none, or None where no record ended it; LookupError where the resolver does not
answer. `derive_carried_witnesses(root, named, tags)` adds each witness held under a redirected tag
under its successor.

THE ORDERS. At a move whose previous move was pinned at another commit, `write_ended_orders` composes at
HEAD and files one `item-ended` order for each tag the build's moves name that the composition lacks and
the rule does not redirect. `read_tag_policy(key, root, build)` reads a tag-valued key at the build's pin
through the policy kit's `resolve` and answers each member redirected, filing one `policy-renamed` order
per redirected member for the owner to re-pin the guarded policy file. An order is one file,
`.governance/outbox/loop-<kind>-<slug>.md`, written by `write_loop_order` as UTF-8 with LF line ends, so a
retried boundary rewrites the same file.

`--fixture --plant <case>` builds a scratch repository through `loop_items.build_scratch_tree`, adds the
build `tFix` and names its branch `main`, records the plant's moves through the writer, prints each
observation and closes with `loop: fixture · <case> · held` or `· MISSED <why>`. The cases are `PLANTS`.
`--selftest` runs every plant through `loop_lib.run_selftest_cases` over one scratch base, reset per plant.
Exit 0 held, 1 missed, 2 where the scratch could not be built.

WHAT THIS DOES NOT CHECK: any kind but the item and scenario kinds at a pin; the definition's steps and transition
tables at a pin, which are read from this kit's own file; that the owner acted on an order; a successor
chain longer than one record, since the resolver answers the record that ended the tag.
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_items import build_scratch_tree, derive_definition_rel, read_composed_items, read_composition  # noqa: E402
from loop_lib import read_memory_tree, resolve_kit_dir, run_selftest_cases  # noqa: E402
from loop_parents import read_policy_kit  # noqa: E402
from loop_transition import read_transition_records, read_transitions  # noqa: E402
from loop_witness import (read_clean_env, read_git, remove_tree, resolve_commit, run_fixture_git,  # noqa: E402
                          write_fixture_files)

SAY = "loop"
PINNED, UNPINNED = "pinned", "unpinned"
OUTBOX = ".governance/outbox"
ITEM_ENDED, POLICY_RENAMED = "item-ended", "policy-renamed"
#: An order's kind and slug: values of the tag and key grammars, never a path separator.
ORDER_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
RESOLVER = "gov_tag.py"
FX_BUILD = "tFix"
FX_UNIT = "TOOL-tFix-1"
FX_OLD, FX_NEW, FX_NEW_B = "item.design.decompose", "item.design.regroup", "item.design.regroup-b"
FX_KEY = "review.breakpoints"
PLANTS = {"rename": "C2 renames item.design.decompose to item.design.regroup: the pin, the read at it, the carry",
          "ended": "C2 removes item.design.decompose with no successor: one item-ended order",
          "split": "C2 splits item.design.decompose in two: one item-ended order and no carry",
          "policy-rename": "the rename, review.breakpoints naming the old tag: redirected, one policy-renamed order",
          "unpinned": "one hand-written move with no composition: read unpinned at HEAD, the next move pins"}
#: Each plant's C2 change record: `(action, successor, after)`; `unpinned` writes none.
CHANGES = {"rename": ("rename", FX_NEW, "none"), "policy-rename": ("rename", FX_NEW, "none"),
           "ended": ("remove", "none", "none"),
           "split": ("split", "%s,%s" % (FX_NEW, FX_NEW_B), "%s@0123abcd,%s@0123abcd" % (FX_NEW, FX_NEW_B))}


# ------------------------------------------------------------------------------------------ the pin
def derive_composition_revision(root):
    """The composition revision of the repository at `root`: the full commit HEAD names. ValueError
    where HEAD names no commit."""
    sha = resolve_commit(root, "HEAD")
    if sha is None:
        raise ValueError("HEAD names no commit in %s, so no composition revision is read" % pathlib.Path(root).as_posix())
    return sha


def read_step_composition(root, moves):
    """`(commit, state)` of a build's step from its `moves`, newest first: the newest move's `composition`
    resolved to its commit, `pinned`; HEAD's commit, `unpinned`, where no move or the newest carries no
    pin. ValueError where a pin names no commit, naming the move's commit."""
    pin = moves[0].get("composition") if moves else None
    if not pin:
        return derive_composition_revision(root), UNPINNED
    sha = resolve_commit(root, pin)
    if sha is None:
        raise ValueError("the move at %s pins composition=%s, which names no commit in %s" % (
            str(moves[0].get("commit"))[:8], pin, pathlib.Path(root).as_posix()))
    return sha, PINNED


def read_composition_at(root, rev, kind="item", rows=None):
    """`(exit, payload, lines)` of `read_composition` of `kind` composed at `rev`, `rows` the activated
    rows it hands on (TOOL-dDeclaredLoop-27): in place where `rev` is HEAD's commit, otherwise in a scratch
    worktree detached at it and removed in a `finally`. ValueError where `rev` names no commit or git
    cannot check it out."""
    root = pathlib.Path(root).absolute()
    sha = resolve_commit(root, rev)
    if sha is None:
        raise ValueError("the pin %s names no commit in %s" % (rev, root.as_posix()))
    if sha == derive_composition_revision(root):
        return read_composition(root, kind, rows)
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="pin-")).absolute()
    try:
        if read_git(root, "worktree", "add", "--detach", str(scratch), sha)[0] != 0:
            raise ValueError("git could not check out %s in a scratch worktree of %s" % (sha[:8], root.as_posix()))
        return read_composition(scratch, kind, rows)
    finally:
        read_git(root, "worktree", "remove", "--force", str(scratch))
        if scratch.exists():
            remove_tree(scratch)
            read_git(root, "worktree", "prune")


# ------------------------------------------------------------------------------------------ the carry
def read_tag_successors(root, tag):
    """The successors the change records end `tag` with, read by the tag resolver under `root`: a list,
    `[]` for an ending with none; None where no record ended it. LookupError naming the resolver where
    it does not resolve or does not answer."""
    root = pathlib.Path(root).absolute()
    try:
        kit = resolve_kit_dir("playbook", RESOLVER, root / pathlib.Path(derive_definition_rel()).parent)
    except LookupError as e:
        raise LookupError("the tag resolver %s does not resolve under %s: %s" % (RESOLVER, root.as_posix(), e)) from None
    try:
        p = subprocess.run([sys.executable, str(kit / RESOLVER), "show", tag, "--json"], cwd=str(root),
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300,
                           env=read_clean_env(PYTHONIOENCODING="utf-8"))
    except subprocess.TimeoutExpired:
        raise LookupError("the tag resolver %s show %s did not return within 300 s" % (RESOLVER, tag)) from None
    if p.returncode == 1:
        return None
    try:
        rows = json.loads(p.stdout) if p.returncode == 0 else None
    except ValueError:
        rows = None
    if not isinstance(rows, list):
        said = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]
        raise LookupError("the tag resolver %s show %s exited %d: %s" % (
            RESOLVER, tag, p.returncode, said[-1] if said else "no JSON"))
    retired = [r for r in rows if isinstance(r, dict) and r.get("kind") == "retired"]
    if not retired:
        return None
    heirs = str(retired[-1].get("text", "")).partition("**Successor:**")[2].strip()
    return [] if heirs in ("", "none") else [h.strip() for h in heirs.split(",") if h.strip()]


def derive_successor(root, tag, tags):
    """`(successor or None, successors read)`: the one successor `tag` is redirected to, where `tag` is
    absent from `tags`, the resolver answers exactly one successor and `tags` holds it."""
    if tag in tags:
        return None, None
    heirs = read_tag_successors(root, tag)
    return (heirs[0] if heirs and len(heirs) == 1 and heirs[0] in tags else None), heirs


def derive_carried_witnesses(root, named, tags):
    """`named`, `{item tag: witness commit}`, with each witness held under a tag absent from `tags` added
    under its successor where the tag is redirected."""
    out = dict(named)
    for tag, commit in named.items():
        if tag:
            heir = derive_successor(root, tag, tags)[0]
            if heir:
                out.setdefault(heir, commit)
    return out


# ------------------------------------------------------------------------------------------ the orders
def render_loop_order(kind, fields, ask):
    """One order's text: its heading, a `- **Key:** value` line per field, then the ask."""
    return "# loop order · %s\n\n%s\n%s\n" % (kind, "".join("- **%s:** %s\n" % kv for kv in fields), ask)


def write_loop_order(root, kind, slug, text):
    """Write one order as `<OUTBOX>/loop-<kind>-<slug>.md` under `root`, UTF-8 with LF line ends: its
    repo-relative path. ValueError where the kind or the slug is outside `ORDER_NAME`."""
    for what, value in (("kind", kind), ("slug", slug)):
        if not (isinstance(value, str) and ORDER_NAME.fullmatch(value)):
            raise ValueError("the order %s %r is outside %s" % (what, value, ORDER_NAME.pattern))
    rel = "%s/loop-%s-%s.md" % (OUTBOX, kind, slug)
    path = pathlib.Path(root, rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return rel


def write_ended_orders(root, build, moves):
    """At a move of `build`, `moves` its recorded moves newest first: compose at HEAD, the new pin, and
    file one `item-ended` order per tag the moves name that the composition lacks and no single held
    successor carries. `(order paths, None)`, or `([], why)` where the composition does not answer 0.
    LookupError where the tag resolver does not answer."""
    before = read_step_composition(root, moves)[0]
    rc, payload, lines = read_composition(root)
    if rc != 0:
        return [], (lines[0] if lines else "compose exited %d" % rc)
    tags = {r.get("tag") for r in payload["rows"]}
    head = derive_composition_revision(root)
    paths = []
    for tag in sorted({m.get("item") for m in moves if m.get("item")} - tags):
        heir, heirs = derive_successor(root, tag, tags)
        if heir:
            continue
        read = "no change record ended it" if heirs is None else ", ".join(heirs) or "none"
        text = render_loop_order(ITEM_ENDED, [("Build", build), ("Item", tag), ("From", before[:8]), ("To", head[:8]),
                                              ("Successors", read)],
                                 "The build %s holds a witness under %s, which the composition at %s lacks and no single "
                                 "successor it holds carries: decide where that work goes." % (build, tag, head[:8]))
        paths.append(write_loop_order(root, ITEM_ENDED, "%s-%s" % (build, tag), text))
    return paths, None


def read_tag_policy(key, root, build):
    """The members of the tag-valued policy `key` at `build`'s pin, read through the policy kit's
    `resolve`, each absent from the composition at the pin and redirected read as its successor, with
    one `policy-renamed` order filed per redirected member. ValueError on a policy refusal or a pin
    naming no commit; LookupError where a kit or the resolver does not answer."""
    root = pathlib.Path(root).absolute()
    rev = read_step_composition(root, read_transitions(build, root))[0]
    policy, _guard = read_policy_kit()
    try:
        value = policy.resolve(key, str(root), rev).value
    except policy.Refusal as e:
        raise ValueError("%s does not resolve at %s: %s" % (key, rev[:8], e)) from None
    members = list(value) if isinstance(value, (list, tuple, set, frozenset)) else [value]
    tags = {r.get("tag") for r in read_composed_items(root, rev)}
    out = []
    for member in members:
        heir = derive_successor(root, member, tags)[0] if isinstance(member, str) else None
        if heir:
            write_loop_order(root, POLICY_RENAMED, "%s-%s" % (key, member), render_loop_order(
                POLICY_RENAMED, [("Key", key), ("Tag", member), ("Successor", heir), ("At", rev[:8])],
                "%s names %s, which a change record renamed to %s: re-pin the key in the policy file to %s." % (
                    key, member, heir, heir)))
        out.append(heir or member)
    return out


# ------------------------------------------------------------------------------------------ the plants
def build_composition_base():
    """`(top, base sha)`: `build_scratch_tree`'s repository with the build `tFix` and its one spec
    committed and its branch named `main`. The directory is removed on any failure."""
    top = build_scratch_tree()[0]
    try:
        for key, value in (("user.name", "fx"), ("user.email", "fx@example.invalid"), ("commit.gpgsign", "false"),
                           ("core.autocrlf", "false")):
            run_fixture_git(top, "config", key, value)
        write_fixture_files(top, {
            ".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\n',
            "memory/builds/%s/README.md" % FX_BUILD: "---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\n"
                                                     "roster: TOOL\nids: %s\n---\n\n# %s\n" % (FX_BUILD, FX_UNIT, FX_BUILD),
            "memory/builds/%s/spec/2026-01-01-spec-%s.md" % (FX_BUILD, FX_UNIT):
                "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n" % FX_UNIT})
        run_fixture_git(top, "add", "-A")
        run_fixture_git(top, "commit", "-q", "-m", "the build %s" % FX_BUILD)
        run_fixture_git(top, "branch", "-M", "main")
        return top, run_fixture_git(top, "rev-parse", "HEAD")
    except BaseException:
        remove_tree(top)
        raise


def write_plant_retag(top, case):
    """C2: the scratch definition's `FX_OLD` re-tagged `FX_NEW` throughout and `case`'s change record
    written through the memory-tree kit's `write_change`, committed."""
    defn = top / derive_definition_rel()
    text = defn.read_text(encoding="utf-8")
    if FX_OLD not in text:
        raise ValueError("the scratch definition holds no %s to re-tag" % FX_OLD)
    defn.write_text(text.replace(FX_OLD, FX_NEW), encoding="utf-8", newline="")
    read_memory_tree("build_records.py")
    from build_records import write_change
    action, successor, after = CHANGES[case]
    write_change(top, FX_BUILD, FX_UNIT, FX_OLD, action, "semantic", "none", after, "none — the fixture's C2",
                 successor=successor)
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "C2: %s %s" % (action, FX_OLD))
    return run_fixture_git(top, "rev-parse", "HEAD")


def read_order_names(top):
    """The file names under the scratch's outbox, sorted."""
    folder = pathlib.Path(top, OUTBOX)
    return sorted(p.name for p in folder.iterdir()) if folder.is_dir() else []


def run_composition_plant(case, base):
    """One plant over the scratch `base`, `(top, sha)`, reset to its commit first: -> 0 held, 1 missed."""
    import loop_transition
    top, sha = base
    run_fixture_git(top, "reset", "-q", "--hard", sha)
    run_fixture_git(top, "clean", "-qfdx")
    print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
    misses = []

    def check_owed(label, held, said):
        print("%s: fixture · %s · %s" % (SAY, label, said))
        if not held:
            misses.append("%s: %s" % (label, said))

    def write_plant_move(state, item, outcome):
        rc = loop_transition.main(["record", "--build", FX_BUILD, "--root", str(top), "--from", state, "--item", item,
                                   "--outcome", outcome, "--witness", "HEAD"])
        if rc != 0:
            raise ValueError("record --from %s --item %s exited %d" % (state, item, rc))

    def read_tags(rev):
        return {r.get("tag") for r in read_composed_items(top, rev)}

    try:
        if case == "unpinned":
            head = run_fixture_git(top, "rev-parse", "HEAD")
            run_fixture_git(top, "commit", "-q", "--allow-empty", "-m", "move\n\nGov-Transition: planning -> designing · "
                            "build=%s · item=item.plan.exit · sha=%s" % (FX_BUILD, head[:8]))
            head = run_fixture_git(top, "rev-parse", "HEAD")
            pin, state = read_step_composition(top, read_transitions(FX_BUILD, top))
            check_owed("pin", (pin, state) == (head, UNPINNED), "%s · %s" % (pin[:8], state))
            write_plant_move("designing", FX_OLD, "goal-fork")
            got = read_transitions(FX_BUILD, top)[0].get("composition")
            check_owed("next move", got == head[:8], "composition=%s" % got)
            check_owed("orders", not read_order_names(top), "%d order(s)" % len(read_order_names(top)))
        else:
            if case == "policy-rename":
                write_fixture_files(top, {".governance/policy.toml": '[review]\nbreakpoints = ["%s"]\n' % FX_OLD})
                run_fixture_git(top, "add", "-A")
                run_fixture_git(top, "commit", "-q", "-m", "the plant's breakpoint")
            write_plant_move("planning", "item.plan.exit", "recorded")
            c1 = run_fixture_git(top, "rev-parse", "HEAD")
            write_plant_move("designing", FX_OLD, "goal-fork")
            c2 = write_plant_retag(top, case)
            pin, state = read_step_composition(top, read_transitions(FX_BUILD, top))
            check_owed("pin after C2", (pin, state) == (c1, PINNED), "%s · %s" % (pin[:8], state))
            if case == "rename":
                tags = read_tags(pin)
                check_owed("composition at the pin", FX_OLD in tags and FX_NEW not in tags,
                           "%s %s · %s %s" % (FX_OLD, FX_OLD in tags, FX_NEW, FX_NEW in tags))
                import position
                before = os.environ.get(position.HANDOVER)
                os.environ[position.HANDOVER] = "unit\t%s\tREADY\n" % FX_UNIT
                try:
                    pos = position.derive_position(top, FX_BUILD)
                finally:
                    if before is None:
                        os.environ.pop(position.HANDOVER, None)
                    else:
                        os.environ[position.HANDOVER] = before
                want = "composition@%s · %s" % (c1[:8], PINNED)
                check_owed("position reads", want in pos["read"], " | ".join(r for r in pos["read"] if r.startswith(
                    "composition@")) or "no composition read")
            if case == "policy-rename":
                got = read_tag_policy(FX_KEY, top, FX_BUILD)
                check_owed("policy before the move", got == [FX_OLD], "%s %s" % (FX_KEY, got))
            revision = derive_composition_revision(top)
            write_plant_move("planning", "item.plan.exit", "recorded")
            moves = read_transitions(FX_BUILD, top)
            check_owed("move at C2", moves[0].get("composition") == c2[:8] == revision[:8],
                       "composition=%s · C2 %s" % (moves[0].get("composition"), c2[:8]))
            pin = read_step_composition(top, moves)[0]
            named = {}
            for m in moves:
                named.setdefault(m.get("item"), m.get("commit"))
            carried = derive_carried_witnesses(top, named, read_tags(pin))
            orders = [n for n in read_order_names(top) if n.startswith("loop-%s-" % ITEM_ENDED)]
            if case in ("rename", "policy-rename"):
                check_owed("carry", carried.get(FX_NEW) == named.get(FX_OLD),
                           "%s under %s · %s" % (str(carried.get(FX_NEW))[:8], FX_NEW, len(orders)) + " item-ended order(s)")
                if orders:
                    misses.append("a redirected item filed %s" % orders)
            else:
                check_owed("orders", orders == ["loop-%s-%s-%s.md" % (ITEM_ENDED, FX_BUILD, FX_OLD)], " ".join(orders) or
                           "no item-ended order")
                check_owed("carry", FX_NEW not in carried, "%s carried: %s" % (FX_NEW, FX_NEW in carried))
            if case == "rename":
                rec = (read_transition_records(FX_BUILD, top) or [{}])[-1].get("fields", {})
                trailer = next((m for m in moves if m.get("source") == "trailer"), {})
                check_owed("channels", trailer.get("composition") == rec.get("composition") == revision[:8],
                           "trailer %s · log %s" % (trailer.get("composition"), rec.get("composition")))
            if case == "policy-rename":
                got = read_tag_policy(FX_KEY, top, FX_BUILD)
                names = [n for n in read_order_names(top) if n.startswith("loop-%s-%s-" % (POLICY_RENAMED, FX_KEY))]
                check_owed("policy after the move", got == [FX_NEW] and len(names) == 1, "%s %s · %s" % (
                    FX_KEY, got, " ".join(names) or "no policy-renamed order"))
    except (subprocess.CalledProcessError, OSError, ValueError, LookupError, KeyError) as exc:
        misses.append("the plant could not run: %s %s" % (exc, (getattr(exc, "stderr", "") or "").strip()[:300]))
    print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
    return 1 if misses else 0


def run_selftest():
    """Every plant over one scratch base through `run_selftest_cases`: -> 0 when every case holds."""
    try:
        base = build_composition_base()
    except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
        print("%s: composition selftest · UNARMED · the scratch could not be built: %s" % (SAY, exc))
        return 2
    try:
        cases = [(c, ["--fixture", "--plant", c], 0, "%s: fixture · %s · held" % (SAY, c), "") for c in PLANTS]
        return run_selftest_cases(lambda argv: run_composition_plant(argv[2], base), cases,
                                  "%s: composition selftest" % SAY)
    finally:
        remove_tree(base[0])


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if argv == ["--selftest"]:
        return run_selftest()
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        try:
            base = build_composition_base()
        except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
            print("%s: fixture · UNARMED · the scratch could not be built: %s" % (SAY, exc))
            return 2
        try:
            return run_composition_plant(argv[2], base)
        finally:
            remove_tree(base[0])
    print("usage: python composition.py --fixture --plant <%s> | --selftest" % "|".join(PLANTS), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
