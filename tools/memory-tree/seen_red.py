#!/usr/bin/env python3
"""seen_red.py -- `test.seen-red`: one seen-red record per gate a build adds or changes (TOOL-dWitnessedBar-7).

    python <prefix>/memory-tree/seen_red.py --build <slug> [--base <sha>]
    python <prefix>/memory-tree/seen_red.py --fixture --plant <case>

THE RECORD is the seen-red line of an `**Evidences:** <unit>` block of a `journal` record, its grammar
stated once, in HYGIENE.md's "Acceptance ledger" section, and parsed here by `SEEN_RED_RE`. Until
dScopedBuild's `build.acceptance` writes it, the main loop's acceptance-ledger line is the record.
`read_seen_red_records` is its one reader; a line opening `- seen-red` in any other shape is
`ValueError` naming the record and the line, never skipped.

THE OWED SET, `derive_owed_gates`: (a) every leg whose manifest row at HEAD is absent at the base or
carries another `argv`, the manifest `routed_commits.resolve_leg_manifest` locates, both revisions read
in one `tree_lib.read_blobs_at` call; (b) every `New arm:` line inside the Gates section of a spec
under the build's `spec/`, read by the `arm_walk` block, the spec-token checker's own walk carried inline
(indented continuation lines joined, a line quoted in any other section never read): its suite path is
the first whitespace-delimited word of its first ` · ` field and each later word of that field a further
argv element (TOOL-dWitnessedBar-51 S4, S20), resolved to the HEAD legs whose `argv`, each `{prefix}`
resolved against `legacy_ledger.derive_seed_prefix`, holds the path and every further word, one gate any
of those legs satisfies. A line resolving to no leg is named and owes nothing.

`--build` joins each owed gate to a seen-red line naming it in a journal record of that build and
prints `seen-red: <leg> · <red sha8> · <record>` or `seen-red: <leg> · NO RECORD`: exit 1 on any NO
RECORD, 0 when every gate has one, and an empty owed set says so and exits 0. `--base` defaults to the
`base:` fact of the build's `RUN.md` under `## Run facts`. Exit 2 when it cannot answer: no base, a
manifest that does not resolve or read, or a refused line. `--fixture --plant <case>` builds a scratch
repository in the system temp directory, runs `--build` over it and exits as that run does.

WHAT IT DOES NOT CHECK. That a recorded red was observed, or that its SHAs name commits: it reads the
line. A gate whose script changed while its argv did not, unless a `New arm:` line names it (§8 F3).
A leg's other fields, its guard or ceiling. Landed builds' ledgers predate the grammar, so it is run on
a build from this unit on and is no gate over the corpus.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from tree_lib import (  # noqa: E402  the kit's binding reader, block walk, blob and git readers
    GIT_ENV_LEAKS, parse_conf, read_bindings, read_blobs_at, read_evidence_lines, read_git_output, read_text)

SAY = "seen-red"
SEEN_RED_LEAD = "- seen-red"
SEEN_RED_RE = re.compile(r"^- seen-red — `([^`]+)` — red `([0-9a-f]{8,40})` — green `([0-9a-f]{8,40})` — (\S.*)$")
NEW_ARM_LEAD = "New arm:"
SLUG_RE = re.compile(r"[A-Za-z0-9]+")
BASE_RE = re.compile(r"[0-9a-f]{7,40}")
RUN_FACTS = "## Run facts"


# >>> arm_walk -- canonical copy: check-spec-tokens.py in the gov tools dir (byte-identical; gated)
# The Gates section by its heading text and its `New arm:` lines: `seen_red.py` in the memory-tree kit
# carries this block inline, and `resolve-python.test.sh`'s parity table reds a copy that drifts.
GATES_HEAD = re.compile(r"^## [0-9]+[.] Gates[ \t]*$", re.M)


def extract_gates(text):
    """Section 7 by its HEADING TEXT, never by its ordinal.

    TOOL-aJoinedCanon-7. A Tier-1 spec under the light profile may legally drop
    `## 5. Production-readiness checklist`, which slides every later section up one — so the ordinal
    read grades whatever happens to sit seventh, and once the S7 arm below turns a silent read into a
    VERDICT that becomes a red on a spec the format permits. The pattern is check 12's
    acceptance-witness regex with one word changed: bracketed dot, tab class and end anchor intact.

    Returns None when the spec carries NO Gates heading at all. That is a different fact from an
    empty section and the report keeps the two apart, because they have different remedies.
    """
    m = GATES_HEAD.search(text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[:nxt.start()] if nxt else rest


def scan_arm_lines(gates):
    """`gates`' `New arm:` lines, `gates` a Gates section `extract_gates` returned, each joined with its
    indented continuation lines into one string: a line opening `New arm:` starts an arm, an indented
    non-blank line continues the open one, and any other line closes it (TOOL-dWitnessedBar-51 S20)."""
    arms, cur = [], None
    for line in gates.splitlines():
        if line.startswith("New arm:"):
            cur = [line.strip()]
            arms.append(cur)
        elif cur is not None and line[:1] in (" ", "\t") and line.strip():
            cur.append(line.strip())
        else:
            cur = None
    return [" ".join(arm) for arm in arms]
# <<< arm_walk


def read_conf(root):
    """The tree's `.memory-tree.conf` through the kit's one parser, `MEMORY_ROOT` defaulting to
    `memory` as the hygiene engine's does; an absent conf is that default alone."""
    path = pathlib.Path(root, ".memory-tree.conf")
    conf = parse_conf(path.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n"), {}) if path.is_file() else {}
    conf["MEMORY_ROOT"] = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    return conf


def read_tracked(root):
    """Every path git's index holds at `root`; OSError naming the call on failure."""
    return [p for p in read_git_output(root, ("ls-files", "-z")).decode("utf-8").split("\0") if p]


def read_seen_red_records(root):
    """`{leg name: [(red sha, green sha, record path, line number)]}` over every tracked `journal`
    record, the records `tree_lib.read_bindings` binds `journal`, each walked by `read_evidence_lines`.
    A line opening `- seen-red` that breaks the grammar is `ValueError` naming the record and line."""
    tracked = read_tracked(root)
    records: dict = {}
    for rel, bind in read_bindings(str(root), tracked, read_conf(root)).items():
        if bind.get("kind") != "journal":
            continue
        for n, _unit, line in read_evidence_lines(read_text(os.path.join(str(root), rel))):
            if not line.startswith(SEEN_RED_LEAD):
                continue
            m = SEEN_RED_RE.match(line.rstrip())
            if not m:
                raise ValueError("%s:%d: a seen-red line outside its grammar, HYGIENE.md's \"Acceptance ledger\": %s"
                                 % (rel, n, line))
            records.setdefault(m.group(1), []).append((m.group(2), m.group(3), rel, n))
    return records


def read_run_base(text):
    """The `base:` fact of a run-state file: the first line opening `base:` under `## Run facts`, to the
    next `## ` heading, re-read inline as the driver writes it (§8 F5); None where there is none."""
    inside = False
    for line in text.split("\n"):
        line = line.removesuffix("\r")
        if line.startswith("## "):
            inside = line.startswith(RUN_FACTS)
        elif inside and line.startswith("base:"):
            return line[len("base:"):].strip()
    return None


def read_manifest_legs(text, where):
    """`{name: argv}` of one leg manifest's text; ValueError naming `where` when it does not read."""
    try:
        rows = json.loads(text)
    except ValueError as exc:
        raise ValueError("%s does not read as JSON: %s" % (where, exc)) from None
    if not isinstance(rows, list) or not all(isinstance(r, dict) and isinstance(r.get("name"), str) for r in rows):
        raise ValueError("%s is not a list of rows each carrying a name" % where)
    return {r["name"]: r.get("argv") for r in rows}


def derive_owed_gates(root, slug, base):
    """-> (gates, unresolved): each gate a list of leg names any one of which a seen-red line
    satisfies, and each `New arm:` line resolving to no leg as `(spec path, suite path)`. ValueError
    naming why when the manifest does not resolve or read at HEAD or at `base`."""
    import routed_commits                    # noqa: PLC0415  the kit's manifest resolver
    from coverage_join import resolve_prefix_token  # noqa: PLC0415  the kit's `{prefix}` reader
    from legacy_ledger import derive_seed_prefix    # noqa: PLC0415  the tool root a `{prefix}` names
    conf = read_conf(root)
    rel = routed_commits.resolve_leg_manifest(root, conf)
    if not rel:
        raise ValueError("no leg manifest resolves: LEG_MANIFEST is blank and no run-gates kit sits beside this one")
    blobs = read_blobs_at(root, [(base, rel), ("HEAD", rel)])
    texts = {}
    for rev in (base, "HEAD"):
        if blobs.get((rev, rel)) is None:
            raise ValueError("the leg manifest %s does not read at %s" % (rel, rev))
        texts[rev] = read_manifest_legs(blobs[(rev, rel)], "%s at %s" % (rel, rev))
    then, now = texts[base], texts["HEAD"]
    gates, seen = [], set()
    for name, argv in now.items():
        if name not in then or then[name] != argv:
            gates.append([name])
            seen.add((name,))
    troot = derive_seed_prefix(root)
    argvs = {name: [resolve_prefix_token(a, troot) for a in argv] for name, argv in now.items()
             if isinstance(argv, list)}
    spec_dir = "%s/builds/%s/spec/" % (conf["MEMORY_ROOT"], slug)
    unresolved = []
    for spec in sorted(p for p in read_tracked(root) if p.startswith(spec_dir) and p.endswith(".md")):
        section = extract_gates(read_text(os.path.join(str(root), spec)).replace("\r\n", "\n"))
        for arm in scan_arm_lines(section or ""):
            suite = arm[len(NEW_ARM_LEAD):].split(" · ", 1)[0].strip().strip("`")
            words = suite.split()
            legs = [name for name, argv in argvs.items() if words and all(w in argv for w in words)]
            if not legs:
                unresolved.append((spec, suite))
            elif tuple(legs) not in seen:
                seen.add(tuple(legs))
                gates.append(legs)
    return gates, unresolved


def run_build(root, slug, base=None):
    """S5, the join over the tree at `root`: prints one line per owed gate and returns the exit."""
    if not SLUG_RE.fullmatch(slug or ""):
        print("%s: --build %r is not a build slug" % (SAY, slug), file=sys.stderr)
        return 2
    conf = read_conf(root)
    if base is None:
        run = pathlib.Path(root, conf["MEMORY_ROOT"], "builds", slug, "RUN.md")
        base = read_run_base(run.read_bytes().decode("utf-8", "replace")) if run.is_file() else None
        if not base:
            print("%s: no base: --base not given and %s holds no `base:` fact under `%s`"
                  % (SAY, run.relative_to(root).as_posix(), RUN_FACTS), file=sys.stderr)
            return 2
    if not BASE_RE.fullmatch(base):
        print("%s: the base %r is not a lowercase hex sha of 7 to 40 digits" % (SAY, base), file=sys.stderr)
        return 2
    try:
        gates, unresolved = derive_owed_gates(root, slug, base)
        records = read_seen_red_records(root)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        print("%s: %s" % (SAY, exc), file=sys.stderr)
        return 2
    folder = "%s/builds/%s/" % (conf["MEMORY_ROOT"], slug)
    for spec, suite in unresolved:
        print("%s: New arm %s in %s · resolves to no leg · owes nothing" % (SAY, suite, spec))
    if not gates:
        print("%s: %s adds or changes no gate · nothing joined" % (SAY, slug))
        return 0
    red = 0
    for legs in gates:
        hit = next(((leg, r) for leg in legs for r in records.get(leg, ()) if r[2].startswith(folder)), None)
        if hit:
            print("%s: %s · %s · %s" % (SAY, hit[0], hit[1][0][:8], hit[1][2]))
        else:
            print("%s: %s · NO RECORD" % (SAY, " | ".join(legs)))
            red = 1
    return red


# ------------------------------------------------------------------------------------------- the fixture
PLANTS = ("seen", "unseen-gate", "unseen-arm", "unseen-arm-with-args", "arm-outside-gates", "bad-line", "empty")
FIX_SLUG = "dFix"
FIX_BASE_LEG = {"name": "fix base leg", "argv": ["bash", "tools/fix/base.test.sh"]}
FIX_ADDED_LEG = {"name": "fix added leg", "argv": ["bash", "tools/fix/added.test.sh"]}
FIX_ARGS_LEG = {"name": "fix args leg", "argv": ["python", "fix/x.py", "--selftest"]}
FIX_LEDGER = "memory/builds/dFix/build/2026-01-01-build-TOOL-dFix-1-1-acceptance-ledger.md"
FIX_SPEC = "memory/builds/dFix/spec/2026-01-01-spec-TOOL-dFix-1.md"


def run_git_in(top, *args):
    """One git call in a fixture repository, the caller's git location variables set aside;
    RuntimeError naming it on failure."""
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS}
    p = subprocess.run(["git", "-C", str(top), *args], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env, stdin=subprocess.DEVNULL)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), (p.stderr or p.stdout).strip()))
    return p.stdout.strip()


def write_fixture_files(top, files):
    for rel, text in files.items():
        p = pathlib.Path(top, rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))


def write_fixture_commit(top, files, message):
    write_fixture_files(top, files)
    run_git_in(top, "add", "-A")
    run_git_in(top, "commit", "-q", "-m", message)
    return run_git_in(top, "rev-parse", "HEAD")


def render_ledger(line):
    return ("# TOOL-dFix-1 — acceptance ledger\n\n**Serves:** journal TOOL-dFix-1\n\n**Evidences:** TOOL-dFix-1\n"
            "- AC1 — `bash tools/fix/added.test.sh` — exits 0\n%s\n" % line)


def build_fixture(top, plant):
    """The scratch repository `plant` names: a base commit holding one leg, then the plant's change."""
    top.mkdir(parents=True)
    run_git_in(top, "init", "-q", "-b", "main")
    for k, v in (("user.email", "fixture@example.invalid"), ("user.name", "fixture"), ("core.autocrlf", "false"),
                 ("commit.gpgsign", "false"), ("core.hooksPath", ".no-hooks")):
        run_git_in(top, "config", k, v)
    base = write_fixture_commit(top, {
        ".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\nLEG_MANIFEST="gate-legs.json"\n',
        "gate-legs.json": json.dumps([FIX_BASE_LEG] + ([FIX_ARGS_LEG] if plant == "unseen-arm-with-args" else []),
                                     indent=2) + "\n",
        "memory/builds/dFix/README.md": "# dFix\n"}, "base")
    files = {"memory/builds/dFix/RUN.md": "# dFix run\n\n## Run facts\n\nbase: %s\n\n## Parked\n" % base}
    if plant in ("seen", "unseen-gate", "bad-line"):
        files["gate-legs.json"] = json.dumps([FIX_BASE_LEG, FIX_ADDED_LEG], indent=2) + "\n"
    if plant == "seen":
        files[FIX_LEDGER] = render_ledger("- seen-red — `fix added leg` — red `%s` — green `%s` — the added suite "
                                          "with its assertion inverted" % (base[:12], base[:12]))
    elif plant == "bad-line":
        files[FIX_LEDGER] = render_ledger("- seen-red — `fix added leg` — green `%s` — the red sha left out" % base[:12])
    elif plant == "unseen-arm":
        files[FIX_SPEC] = ("# TOOL-dFix-1 — a unit\n\n## 7. Gates\n\n`fix base leg`\n\n"
                           "New arm: tools/fix/base.test.sh · covers AC1 · the plant, staged red by its inverse · none\n")
    elif plant == "unseen-arm-with-args":
        files[FIX_SPEC] = ("# TOOL-dFix-1 — a unit\n\n## 7. Gates\n\n`fix args leg`\n\n"
                           "New arm: fix/x.py --selftest · covers AC1 · the plant, staged red by its inverse · none\n")
    elif plant == "arm-outside-gates":
        files[FIX_SPEC] = ("# TOOL-dFix-1 — a unit\n\n## 4. Design\n\nThe arm this spec quotes:\n\n"
                           "New arm: tools/fix/base.test.sh · covers AC1 · quoted, not declared · none\n\n"
                           "## 7. Gates\n\n`fix base leg`\n")
    write_fixture_commit(top, files, plant)


def run_fixture(plant):
    """`--fixture --plant <plant>`: S5 over the plant's scratch repository; its exit is the run's."""
    from deviation_join import remove_tree  # noqa: PLC0415  the kit's read-only-safe fixture remover
    scratch = tempfile.mkdtemp(prefix="sr")
    try:
        top = pathlib.Path(scratch, plant)
        try:
            build_fixture(top, plant)
        except (OSError, RuntimeError) as exc:
            print("%s: FAIL %s · the plant did not build: %s" % (SAY, plant, exc), file=sys.stderr)
            return 2
        print("%s: fixture %s" % (SAY, plant))
        return run_build(top, FIX_SLUG)
    finally:
        remove_tree(scratch)


USAGE = "usage: seen_red.py --build <slug> [--base <sha>] | --fixture --plant <%s>" % "|".join(PLANTS)


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) == 3 and args[:2] == ["--fixture", "--plant"] and args[2] in PLANTS:
        return run_fixture(args[2])
    if len(args) in (2, 4) and args[0] == "--build" and (len(args) == 2 or args[2] == "--base"):
        try:
            root = read_git_output(os.getcwd(), ("rev-parse", "--show-toplevel")).decode("utf-8").strip()
        except OSError as exc:
            print("%s: %s" % (SAY, exc), file=sys.stderr)
            return 2
        return run_build(pathlib.Path(root), args[1], args[3] if len(args) == 4 else None)
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
