#!/usr/bin/env python3
"""owed_rows.py - every row a pass owes, derived from the pass's own diff (PLAY-dOrderedCharter-50).

    python <this kit>/owed_rows.py --base <rev>   # one `owed — <file> <- <row>` line per row missing
    python <this kit>/owed_rows.py --selftest     # each population's failing case, in a scratch repo

FIVE POPULATIONS, each read from <rev> against the working tree:

  leg added     a name in gate-legs.json absent at <rev>. Owes a row in govkit's subject-pins.tsv, a
                descriptor `[[gate_leg]]` row or a registry `[[exempt_leg]]` row, and a dossier claim
                in the codebase map. Its ceiling-evidence.txt row only a measured bar run writes, so it
                prints as a `deferred —` line and leaves the exit unchanged.
  leg removed   a name at <rev> absent now. Owes that no row of subject-pins.tsv, the map's
                baseline.toml or selftest-budgets.txt names it.
  key           every key of every gate-legs.json row. Owes membership in each `KNOWN` copy of
                run-gates.test.sh.
  path deleted  `git diff --diff-filter=D <rev>`, renames read as a delete. Owes that no row of the
                memory root's spawn-idiom-sites.txt, testsuite-count-waivers.txt or
                unarmed-branches.txt names it.
  size          a path changed since <rev>, untracked ones included, that a path-named byte cap of
                the policy kit's census names or matches. Owes its CR-stripped bytes within the value
                `budgets.py resolve <cap>` prints, unless the mode it prints beside it is `warn`:
                a breach the switch admits reds no leg, so it is counted on the summary line.

PRESENCE ONLY. The probe mints no predicate a leg owns: a pin row carrying the wrong subject passes
here and still reds `govkit selfcheck`, and each leg grades its own row. The readers are the legs'
own: govkit's registry and descriptor reads, the codebase-map kit's dossier tree and claimant index,
and the policy kit's census and `budgets.py resolve`, the last as a subprocess. GOV-ONLY: this
kit's descriptor withholds the file from `govkit apply`, which is why it may import the first two.

Exit 1 when any row is owed, 0 with a one-line count when none is, 2 on a refusal: a <rev> that
names no commit, `KNOWN` copies that disagree, an absent registry file, or a reader's failure.
"""
import argparse
import fnmatch
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import tomllib

HERE = pathlib.Path(os.path.abspath(__file__)).parent

# The sibling-kit resolver, INLINED byte-identically from the canonical copy named on its marker
# line and gated by the resolve-python self-test.
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


class Refused(Exception):
    """A refusal: one line, exit 2."""


def load_readers() -> dict:
    """The sibling kits this probe reads through, found from this install by `resolve_kit_dir`."""
    gk = resolve_kit_dir("govkit", "govkit.py", HERE)
    cm = resolve_kit_dir("codebase-map", "map_lib.py", HERE)
    pk = resolve_kit_dir("policy", "budgets.py", HERE)
    for d in (gk, cm):
        if str(d) not in sys.path:
            sys.path.insert(0, str(d))
    import govkit  # noqa: PLC0415
    import map_extractors  # noqa: PLC0415
    import map_lib  # noqa: PLC0415
    return {"G": govkit, "m": map_lib, "ext": map_extractors, "policy": pk}


def run_git(root: pathlib.Path, *args: str) -> str:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env, stdin=subprocess.DEVNULL)
    if p.returncode:
        raise Refused(f"git {' '.join(args)} exited {p.returncode}: {p.stderr.strip()}")
    return p.stdout


def read_first_column(path: pathlib.Path) -> set:
    """The first TAB field of every row that is not blank or a `#` comment. Absent is a refusal."""
    if not path.is_file():
        raise Refused(f"{path.as_posix()} is absent, which is a refusal and never an empty population")
    rows = path.read_text(encoding="utf-8").splitlines()
    return {ln.split("\t")[0].strip() for ln in rows if ln.strip() and not ln.lstrip().startswith("#")}


def read_known_copies(canary: pathlib.Path) -> list:
    """Each `KNOWN = {...}` line of the canary, as a set of keys."""
    if not canary.is_file():
        raise Refused(f"{canary.as_posix()} is absent, so the key population has no KNOWN to read")
    out = []
    for ln in canary.read_text(encoding="utf-8").splitlines():
        s = ln.strip()
        if s.startswith("KNOWN = {") and s.endswith("}"):
            out.append({k.strip().strip('"') for k in s[len("KNOWN = {"):-1].split(",") if k.strip()})
    return out


def read_cap_values(policy: pathlib.Path, root: pathlib.Path, caps: list) -> dict:
    """{cap: (bytes, mode)} as `budgets.py resolve` prints them for the repository at `root`."""
    p = subprocess.run([sys.executable, str(policy / "budgets.py"), "resolve", *caps], cwd=str(root),
                       capture_output=True, text=True, encoding="utf-8", errors="replace",
                       stdin=subprocess.DEVNULL,
                       env={k: v for k, v in os.environ.items() if not k.startswith("GIT_")})
    vals = {}
    for ln in p.stdout.splitlines():
        f = ln.split("\t")
        if len(f) >= 3 and f[1].isdigit():
            vals[f[0]] = (int(f[1]), f[2])
    if p.returncode or set(vals) != set(caps):
        raise Refused(f"budgets.py resolve answered no value for {sorted(set(caps) - set(vals))}: "
                      f"{(p.stderr or p.stdout).strip()}")
    return vals


def derive_owed_rows(root: pathlib.Path, base: str, kits: dict) -> tuple:
    """-> (owed, deferred, warned): two lists of (file, row), and the count of warned size breaches."""
    G, m, ext = kits["G"], kits["m"], kits["ext"]
    rel = lambda p: p.relative_to(root).as_posix()  # noqa: E731
    try:
        run_git(root, "rev-parse", "--verify", "-q", base + "^{commit}")
    except Refused:
        raise Refused(f"--base {base} names no commit in {root.as_posix()}") from None
    legs_p = G.resolve_tool_path(root, "gate-legs.json")
    pins_p = G.resolve_tool_path(root, G.GOVKIT_DIR.name, "subject-pins.tsv")
    canary_p = G.resolve_tool_path(root, HERE.name, "run-gates.test.sh")
    budgets_p = G.resolve_tool_path(root, HERE.name, "selftest-budgets.txt")
    ceiling_p = G.resolve_tool_path(root, HERE.name, "ceiling-evidence.txt")
    map_p = m.map_root(root)
    # ponytail: gov's memory root spelled once; this probe runs in no other tree.
    waivers = [root / "memory" / "project" / n
               for n in ("spawn-idiom-sites.txt", "testsuite-count-waivers.txt", "unarmed-branches.txt")]
    for p in (legs_p, G.derive_registry_path(root), map_p / "baseline.toml"):
        if not p.is_file():
            raise Refused(f"{rel(p)} is absent, which is a refusal and never an empty population")
    legs = json.loads(legs_p.read_text(encoding="utf-8"))
    then = json.loads(run_git(root, "show", f"{base}:{rel(legs_p)}"))
    now_n = {r.get("name") for r in legs if isinstance(r, dict) and r.get("name")}
    then_n = {r.get("name") for r in then if isinstance(r, dict) and r.get("name")}
    added, removed = sorted(now_n - then_n), sorted(then_n - now_n)
    owed, deferred = [], []
    pins = read_first_column(pins_p)
    if added or removed:
        tree = m.load_map_tree(ext.inventory_ids(), root=root,
                               decision_id_re=getattr(ext, "DECISION_ID_RE", m.DEFAULT_DECISION_ID_RE))
    if added:
        reg_p = G.derive_registry_path(root)
        reg = G.load_registry(root)
        r = G.Report()
        descs = G.read_descriptors(root, reg, r)
        if r.problems:
            raise Refused("govkit read_descriptors: " + "; ".join(r.problems))
        claimed = {g.get("name") for d, _ in descs.values() for g in d.get("gate_leg", [])}
        claimed |= {x.get("name") for x in reg.get("exempt_leg", [])}
        idx = m.claimant_index({"gate-legs": added}, m.owners_of(tree), {})["gate-legs"]
        ceilings = read_first_column(ceiling_p)
        for nm in added:
            if nm not in pins:
                owed.append((rel(pins_p), nm))
            if nm not in claimed:
                owed.append((f"a descriptor's [[gate_leg]] or {rel(reg_p)}'s [[exempt_leg]]", nm))
            if idx[nm] == ["UNCLAIMED"]:
                owed.append((f"a dossier's gate-legs claim under {rel(map_p)}/features/", nm))
            if nm not in ceilings:
                deferred.append((rel(ceiling_p), nm))
    if removed:
        held = ((pins_p, pins), (map_p / "baseline.toml", set(tree.baseline.get("gate-legs", ()))),
                (budgets_p, read_first_column(budgets_p)))
        for path, rows in held:
            owed += [(rel(path), f"drop the row naming {nm}") for nm in removed if nm in rows]
    copies = read_known_copies(canary_p)
    if not copies:
        raise Refused(f"{rel(canary_p)} holds no `KNOWN = {{...}}` line, so no key could be graded")
    if any(c != copies[0] for c in copies):
        raise Refused(f"the {len(copies)} KNOWN copies in {rel(canary_p)} disagree: "
                      f"{sorted(set().union(*copies) - set.intersection(*copies))}")
    keys = sorted({k for r in legs if isinstance(r, dict) for k in r})
    owed += [(rel(canary_p), f"`{k}` in each KNOWN copy, with its control pair")
             for k in keys if k not in copies[0]]
    gone = [p for p in run_git(root, "diff", "--name-only", "--no-renames", "--diff-filter=D", base,
                               "--").splitlines() if p]
    for path in waivers:
        rows = read_first_column(path)
        owed += [(rel(path), f"drop the row naming {p}") for p in gone if p in rows]
    changed = run_git(root, "diff", "--name-only", "--no-renames", "--diff-filter=d", base, "--")
    changed += run_git(root, "ls-files", "--others", "--exclude-standard")
    census = tomllib.loads((kits["policy"] / "caps.toml").read_text(encoding="utf-8"))
    caps = [c["name"] for c in census.get("cap", []) if c.get("unit") == "bytes"
            and not c.get("family") and ("/" in c["name"] or "." in c["name"])]
    hits = {}
    for p in sorted(set(changed.splitlines()) - {""}):
        for c in caps:
            # ponytail: fnmatch's `*` crosses `/`; a cap glob deeper than one segment never exists.
            if fnmatch.fnmatchcase(p, c + "*" if c.endswith("/") else c) and (root / p).is_file():
                hits.setdefault(c, []).append(p)
    warned = 0
    if hits:
        vals = read_cap_values(kits["policy"], root, sorted(hits))
        for c, paths in sorted(hits.items()):
            cap_v, mode = vals[c]
            for p in paths:
                n = len((root / p).read_bytes().replace(b"\r", b""))
                if n <= cap_v:
                    continue
                # A breach the switch's `warn` admits reds no leg, so it is counted and not owed.
                if mode == "warn":
                    warned += 1
                    continue
                owed.append((p, f"{n} bytes over cap {c}'s {cap_v}: a trim, or a raise in the "
                                f"minimal guard's one admitted shape"))
    return owed, deferred, warned


def run_probe(root: pathlib.Path, base: str, kits: dict) -> tuple:
    """-> (exit, lines) for one probe of `root` against `base`."""
    try:
        owed, deferred, warned = derive_owed_rows(root, base, kits)
    except (Refused, kits["G"].Refusal, kits["m"].MapError, LookupError, OSError, ValueError) as e:
        return 2, [f"owed_rows: refused · {e}"]
    lines = [f"owed — {f} <- {row}" for f, row in owed]
    lines += [f"deferred — {f} <- {nm}: a measured bar run writes it, at the main loop's close"
              for f, nm in deferred]
    tail = f"since {base} · {len(deferred)} deferred · {warned} size breach(es) the switch's warn admits"
    if owed:
        return 1, lines + [f"owed_rows: {len(owed)} row(s) owed {tail}"]
    return 0, lines + [f"owed_rows: 0 rows owed {tail}"]


# ------------------------------------------------------------------------------------- selftest
FIXTURE = {
    "kits/gate-legs.json": json.dumps([
        {"name": "fx leg", "argv": ["bash", "{prefix}/fx/a.sh"], "subject": "repo"},
        {"name": "old leg", "argv": ["bash", "{prefix}/fx/a.sh"], "subject": "repo"}], indent=2),
    "kits/<gk>/registry.toml": ('[[entry]]\nid = "fx"\ndescriptor = "{prefix}/fx/kit.toml"\n\n'
                                   '[[exempt_leg]]\nname = "old leg"\nwhy = "a fixture leg"\n'),
    "kits/<gk>/subject-pins.tsv": "# pins\nfx leg\trepo\t\nold leg\trepo\t\n",
    "kits/fx/kit.toml": ('id = "fx"\nhome = "fx"\n\n[[gate_leg]]\nname = "fx leg"\nsubject = "repo"\n'
                          'argv = ["bash", "{prefix}/fx/a.sh"]\n'),
    "kits/fx/a.sh": "exit 0\n",
    "kits/fx/gone.sh": "exit 0\n",
    "kits/<rg>/run-gates.test.sh": ('KNOWN = {"name", "argv", "subject"}\n'
                                          'KNOWN = {"name", "argv", "subject"}\n'),
    "kits/<rg>/selftest-budgets.txt": "old leg\t60\t\tfixture\n",
    "kits/<rg>/ceiling-evidence.txt": "fx leg\t1.0\t1\ta\t2026-11-04\trunner\n",
    "memory/map/baseline.toml": "gate-legs = []\n",
    "memory/project/spawn-idiom-sites.txt": "# none\n",
    "memory/project/testsuite-count-waivers.txt": "# none\n",
    "memory/project/unarmed-branches.txt": "kits/fx/gone.sh\texit\t1\ta fixture\tno arm\n",
}


def build_fixture_repo(scratch: pathlib.Path, inventory_ids, cap: str, limit: int, gk: str, rg: str) -> None:
    """FIXTURE at a tool root named `kits`, its kit dirs named as this install names govkit and run-gates."""
    claims = "\n".join(f'{k} = {json.dumps(["fx leg", "old leg", "new leg"] if k == "gate-legs" else [])}'
                       for k in inventory_ids)
    files = dict(FIXTURE)
    files["memory/map/FOUNDATION.md"] = (
        '```toml\nfeature = "foundation"\ntitle = "fixture"\nstatus = "shipped"\nstreams = []\n'
        f'decisions = []\n\n[claims]\n{claims}\n[paths]\nglobs = []\n```\n')
    # The size cap the policy reader answers for THIS repository: refused, at a value the plant crosses.
    files[".governance/policy.toml"] = f'[budgets]\nenforce = "refuse"\n{json.dumps(cap)} = {limit}\n'
    for rel, text in files.items():
        p = scratch / rel.replace("<gk>", gk).replace("<rg>", rg)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
    for args in (("init", "-q", "-b", "main"), ("config", "user.email", "fx@example.invalid"),
                 ("config", "user.name", "fx"), ("config", "core.autocrlf", "false"),
                 ("add", "-A"), ("commit", "-qm", "fixture")):
        run_git(scratch, *args)


def run_selftest() -> int:
    kits = load_readers()
    census = tomllib.loads((kits["policy"] / "caps.toml").read_text(encoding="utf-8"))
    cap = next(c["name"] for c in census["cap"] if c.get("unit") == "bytes" and not c.get("family")
               and "/" in c["name"])
    big = cap.replace("*", "fx") + ("big.md" if cap.endswith("/") else "")
    limit = 100
    gk, rg = kits["G"].GOVKIT_DIR.name, HERE.name
    os.environ["GOV_DEFAULT_BRANCH"] = "main"  # the fixture's one branch, whatever the host's default

    def write_legs(s, fn):
        p = s / "kits/gate-legs.json"
        rows = json.loads(p.read_text(encoding="utf-8"))
        p.write_text(json.dumps(fn(rows), indent=2), encoding="utf-8", newline="\n")

    def add_leg(s):
        write_legs(s, lambda rows: rows + [{"name": "new leg", "argv": ["bash", "{prefix}/fx/a.sh"],
                                           "subject": "repo"}])
        with open(s / "kits/fx/kit.toml", "a", encoding="utf-8", newline="\n") as f:
            f.write('\n[[gate_leg]]\nname = "new leg"\nsubject = "repo"\nargv = ["bash", "{prefix}/fx/a.sh"]\n')

    def remove_leg(s):
        write_legs(s, lambda rows: [r for r in rows if r["name"] != "old leg"])
        (s / "kits" / gk / "subject-pins.tsv").write_text("# pins\nfx leg\trepo\t\n", encoding="utf-8",
                                                          newline="\n")

    def add_stray_key(s):
        write_legs(s, lambda rows: [dict(rows[0], enforce=["x"]), *rows[1:]])

    def add_grown_file(s):
        (s / big).parent.mkdir(parents=True, exist_ok=True)
        (s / big).write_bytes(b"x" * (limit + 1))

    # PLAY-dOrderedCharter-70 S12: five trees each owing what no case above them could, so a population whose
    # append is deleted reds here; the fixture pre-claims and pre-pins only `new leg`.
    def add_bare_leg(s, name="bare leg"):
        write_legs(s, lambda rows: rows + [{"name": name, "argv": ["bash", "{prefix}/fx/a.sh"], "subject": "repo"}])

    def add_unclaimed_leg(s):
        add_bare_leg(s, "unclaimed leg")
        with open(s / "kits/fx/kit.toml", "a", encoding="utf-8", newline="\n") as f:
            f.write('\n[[gate_leg]]\nname = "unclaimed leg"\nsubject = "repo"\nargv = ["bash", "{prefix}/fx/a.sh"]\n')
        with open(s / "kits" / gk / "subject-pins.tsv", "a", encoding="utf-8", newline="\n") as f:
            f.write("unclaimed leg\trepo\t\n")

    def add_owed_free_leg(s):
        add_leg(s)
        with open(s / "kits" / gk / "subject-pins.tsv", "a", encoding="utf-8", newline="\n") as f:
            f.write("new leg\trepo\t\n")

    def split_known(s):
        (s / "kits" / rg / "run-gates.test.sh").write_text(
            'KNOWN = {"name", "argv", "subject"}\nKNOWN = {"name", "argv"}\n', encoding="utf-8", newline="\n")

    def warn_grown_file(s):
        add_grown_file(s)
        (s / ".governance/policy.toml").write_text(f'[budgets]\nenforce = "warn"\n{json.dumps(cap)} = {limit}\n',
                                                   encoding="utf-8", newline="\n")
        run_git(s, "commit", "-qam", "the warn mode lands")

    cases = (
        ("a tree owing nothing", lambda s: None, "HEAD", 0, "owed_rows: 0 rows owed"),
        ("a leg added with no pin row", add_leg, "HEAD", 1, "subject-pins.tsv <- new leg"),
        ("a leg removed whose budget row stays", remove_leg, "HEAD", 1,
         "selftest-budgets.txt <- drop the row naming old leg"),
        ("a key outside KNOWN", add_stray_key, "HEAD", 1, "run-gates.test.sh <- `enforce` in each KNOWN"),
        ("a deleted script unarmed-branches.txt names", lambda s: (s / "kits/fx/gone.sh").unlink(),
         "HEAD", 1, "unarmed-branches.txt <- drop the row naming kits/fx/gone.sh"),
        ("a file grown past its cap", add_grown_file, "HEAD", 1, f"owed — {big} <- {limit + 1} bytes over cap"),
        ("a base naming no commit", lambda s: None, "no-such-rev", 2, "owed_rows: refused"),
        ("a leg with no descriptor row", add_bare_leg, "HEAD", 1,
         "a descriptor's [[gate_leg]] or kits/" + gk + "/registry.toml's [[exempt_leg]] <- bare leg"),
        ("a leg no dossier claims", add_unclaimed_leg, "HEAD", 1, "gate-legs claim under memory/map/features/ <- unclaimed leg"),
        ("two KNOWN copies that differ", split_known, "HEAD", 2, "KNOWN copies in kits/" + rg + "/run-gates.test.sh disagree"),
        ("a leg with no ceiling row", add_owed_free_leg, "HEAD", 0, "deferred — kits/" + rg + "/ceiling-evidence.txt <- new leg"),
        # last: the budgets reader reads the landed policy, so this case commits it and no case runs after it
        ("a breach the warn mode admits", warn_grown_file, "HEAD", 0, "· 1 size breach(es) the switch's warn admits"),
    )
    failed = 0
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="owed-"))
    try:
        build_fixture_repo(scratch, kits["ext"].inventory_ids(), cap, limit, gk, rg)
        for name, plant, base, want_rc, want in cases:
            run_git(scratch, "checkout", "-q", "--", ".")
            run_git(scratch, "clean", "-fdq")
            plant(scratch)
            rc, lines = run_probe(scratch, base, kits)
            if rc == want_rc and any(want in ln for ln in lines):
                print(f"arm ok    {name}")
                continue
            failed += 1
            print(f"arm FAIL  {name} — wanted rc={want_rc} and a line holding {want!r}, got rc={rc}")
            print("".join(f"      {ln}\n" for ln in lines), end="")
    finally:
        # git writes its objects read-only, which a bare rmtree on win32 leaves behind.
        shutil.rmtree(scratch, onexc=lambda f, q, _e: (os.chmod(q, 0o700), f(q)))
    if failed:
        print(f"FAIL — {failed} of {len(cases)} owed-rows fixtures failed")
        return 1
    print(f"PASS — the owed-rows fixtures, {len(cases)} cases")
    return 0


def derive_rule_text() -> str:
    """The rule PLAY-dOrderedCharter-50 S6 hands off, each writer spelled from this install."""
    repo = next((d for d in (HERE, *HERE.parents) if (d / ".git").exists()), HERE.parent)

    def derive_kit_spelling(home, anchor):
        try:
            return (resolve_kit_dir(home, anchor, HERE) / anchor).relative_to(repo).as_posix()
        except (LookupError, ValueError):
            return f"<prefix>/{home}/{anchor}"
    me = (HERE / "owed_rows.py").relative_to(repo).as_posix() if repo in HERE.parents else "owed_rows.py"
    pin_w = derive_kit_spelling("govkit", "govkit.py")
    map_w = derive_kit_spelling("codebase-map", "gen_map.py")
    return (
        "THE RULE (PLAY-dOrderedCharter-50 S6). A pass that adds or retires a leg, adds a manifest\n"
        f"key, deletes a path or grows a capped file runs `python {me} --base HEAD` as the\n"
        "LAST probe of the pass, before its commit, and writes every owed row in that commit.\n"
        "Each row's writer:\n"
        f"  a subject-pins.tsv row     python {pin_w} selfcheck --write; a pass whose\n"
        "                             role refuses that command returns the row to the main loop,\n"
        "                             which writes it before the next dispatch\n"
        "  [[gate_leg]] / [[exempt_leg]]  by hand: the leg's kit.toml when an adopter carries it,\n"
        "                             else the registry, with its why\n"
        "  a dossier claim            by hand in the dossier's gate-legs claims, then\n"
        f"                             python {map_w} --write\n"
        "  a KNOWN key                by hand in both KNOWN copies of run-gates.test.sh, with a\n"
        "                             control pair\n"
        "  a row naming a removed leg or a deleted path   deleted by hand (a pin row: selfcheck --write)\n"
        "  a file over its cap        a trim, or a raise in the minimal guard's one admitted shape\n"
        "  a deferred ceiling row     the main loop's close, after a measured bar:\n"
        "                             derive-ceilings.py --write\n")


def main(argv=None) -> int:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(prog="owed_rows.py", description=__doc__.split("\n")[0],
                                 epilog=derive_rule_text(), formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", help="the revision the pass started from; HEAD before the pass commits")
    ap.add_argument("--selftest", action="store_true", help="each population's failing case, in a scratch repo")
    a = ap.parse_args(argv)
    if a.selftest:
        return run_selftest()
    if not a.base:
        ap.error("--base <rev>, or --selftest")
    try:
        kits = load_readers()
    except (LookupError, ImportError) as e:
        print(f"owed_rows: refused · {e}")
        return 2
    root = next((d for d in (HERE, *HERE.parents) if (d / ".git").exists()), None)
    if root is None:
        print(f"owed_rows: refused · no repository holds {HERE.as_posix()}")
        return 2
    rc, lines = run_probe(root, a.base, kits)
    print("\n".join(lines))
    return rc


if __name__ == "__main__":
    sys.exit(main())
