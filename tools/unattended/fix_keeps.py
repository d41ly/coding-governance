#!/usr/bin/env python3
"""fix_keeps.py — the files a fix pass keeps out of its write set (TOOL-dWitnessedBar-21).

    python fix_keeps.py --keeps 'leg:<leg name>'
    python fix_keeps.py --keeps acceptance --spec <the unit's spec>
    python fix_keeps.py --fixture --plant <case>

A fix pass may not edit the check that reds it. `--keeps <red>` prints the red check's own files,
one repo-relative path per line on stdout, exit 0; a refusal goes to stderr, exit 2. Each note the
driver relays goes to stderr opening `fix-of: `: after a leg's keeps, `fix-of: tests <tag> ...`,
the targets of the leg's `tests` edge, or `fix-of: tests none`; and `fix-of: no kept file` where the
set is empty, which admits every declared path. The unattended driver runs this from
`--dispatch --fix-of <red>` and from `--check-commit` on a key holding a `fix-of` row, and refuses a
declared or a staged path among the keeps under its check 49.

`read_leg_files(rows, name, tool_root, tracked)` reads a leg's own files: each word of its `argv` in
the leg manifest, `{prefix}` resolved to the tool root, that carries a `/`, no whitespace, and names
a tracked file, in argv order, so the gate script is the first, then the tracked files under a
`fixtures/` or `fixture/` directory inside that script's own kit directory (TOOL-dWitnessedBar-51 S35). It is the runner's argv-word census
without the census's extension filter, because the census selects shipped sources and this selects
the files a check reads. The manifest is `gate-legs.json` in the directory holding the run-gates kit
that `resolve_kit_dir` finds from here, the reading the memory-tree kit's `routed_commits.py` makes,
and the tool root is that directory relative to the repository. An unknown leg is refused by name.

`read_acceptance_files(spec_text, tracked)` reads the acceptance commands' own files: each word of a
backticked token in the spec's acceptance-criteria section, found by heading text through the
`acceptance_reader` block the spec-token checker owns, that names a tracked file, by its path or
by a basename no other tracked file carries, and that is a check file: a `*.test.sh`, a name ending
`selftest.py`, a `test_*.py`, or a file under a `fixtures/` directory. A product file a command
probes is not kept, so a fix pass can still touch the code it fixes; a probe whose plants live
inside the product keeps nothing (section 8 F2 of the unit's spec).

`--fixture --plant <case>` builds a throwaway repository in the system temp directory holding a copy
of this kit's driver, a leg manifest with the leg `fx canary`, its suite file, a preflighted run, its
build README and its unit spec, drives the driver through the case, prints each call's output
indented and one PASS or FAIL line, and removes the repository: exit 0 when the case holds, 1 when
it does not, 2 where no bash that can see the driver runs.

NOT CHECKED: a file a check reads that its argv does not name, such as a fixture its suite opens by a
computed path; a word naming a directory; and a backticked token that is not in the section headed
acceptance criteria. The keeps bind the declaration and the commit check, so a write a fix pass
makes is graded only once it is staged.
"""
import argparse
import json
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
SAY = "fix-of"
#: The run-gates kit's home and anchor, beside which the leg manifest sits.
RUN_GATES = ("run-gates", "run-gates.sh")
#: The check-file class of section 8 F2: these suffixes, a `test_*.py`, or a file under `fixtures/`.
CHECK_SUFFIXES = (".test.sh", "selftest.py")
#: The directory names whose tracked files inside the gate script's own kit directory a leg keeps.
FIXTURE_DIRS = ("fixtures", "fixture")
PLANTS = {"writes-test-file": "a fix pass of the leg fx canary declaring the leg's suite file",
          "writes-product": "a fix pass of the leg fx canary declaring the product file",
          "commit-test-file": "the product fix pass, then its suite file staged and --check-commit run",
          "acceptance-fixture": "a fix pass after a failed acceptance, its AC naming a fixture and a product file",
          "light-profile": "the keeps of a Tier-1 spec whose acceptance section is its fifth, not its sixth",
          "writes-fixture": "a fix pass of the leg fx canary declaring a file under its kit's fixtures/",
          "unknown-leg": "a fix pass naming a leg the manifest does not carry"}
#: The fixture's tool root, its unit, its leg and its kit's files: `fx` is no directory of a real tool root.
FX_ROOT = "tools"
FX_UNIT = "ARCH-tFix-1"
FX_LEG = "fx canary"
FX_SUITE = FX_ROOT + "/fx/fx.test.sh"
FX_PRODUCT = FX_ROOT + "/fx/fx.sh"
FX_FIXTURE = FX_ROOT + "/fx/fixtures/a.txt"
FX_SPEC = "memory/builds/tFix/spec/one.md"
FX_RUN = "memory/builds/tFix/RUN.md"
KIT_FILES = ("unattended.sh", "lib-unattended.sh", "commit_trailers.py", pathlib.Path(__file__).name)
#: The bound of one driver call inside the fixture, in seconds.
TIMEOUT = 300


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


# >>> resolve_prefix_token -- canonical copy: resolve_prefix_token.py in the gov lib dir (byte-identical; gated)
def resolve_prefix_token(spelled, troot):
    """<spelled> with its {prefix} token resolved against the tool root <troot>.

    An empty or "." root is a root install: the token drops with its slash, and a bare token
    becomes ".". Any other root replaces the token. Text with no token passes unchanged.
    """
    spelled = str(spelled)
    if not troot or troot == ".":
        return spelled.replace("{prefix}/", "").replace("{prefix}", ".")
    return spelled.replace("{prefix}", troot)
# <<< resolve_prefix_token


# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
BASH_NAMES = ("bash.exe", "bash")


def wrong_shell_at(path, wsl):
    """True when `path` is a Windows checkout under WSL: `wsl` set and `path` under a single-letter
    `/mnt/<drive>/`, WSL's mount of a Windows drive (TOOL-dWitnessedBar-27). The twin of the shell
    block `refuse_wrong_shell`'s `wrong_shell_at` in `refuse-wrong-shell.sh` in the gov lib dir; a
    WSL path on its own disk, and any path where no WSL marker is set, is green."""
    p = str(path)
    return bool(wsl) and len(p) > 6 and p.startswith("/mnt/") and "a" <= p[5] <= "z" and p[6] == "/"


def scan_bash(script="", host=""):
    r"""`(found, tried, refusal)`: the bash to run, found by RUNNING each candidate, never by its name.

    GOV_BASH first, and when it is set nothing after it is tried; then Git's own `bin/bash.exe`, the
    third parent of `git --exec-path`; then each PATH directory's BASH_NAMES, a System32 or
    WindowsApps launcher reported and never run. A candidate passes when one run prints `uname -s` as
    its first line and exits 0, `test -f` on `script` included when one is given; on a `windows` host
    the answer must start MINGW or MSYS, so WSL's launcher, which answers `Linux` and drops `$1`, is
    refused under any name (gotcha subprocess-resolves-a-different-shell). Past GOV_BASH every
    candidate is run, `tried` holding one `<candidate>: <why>` for each and a repeat never twice;
    `found` is the first that passed, or "" with `refusal` naming every `tried` line, and the bare name
    `bash` is never returned. `host` is `windows` or `posix`, this host's when empty. No memo: an
    adapter keeps its own, so this stays a function a truth table can call twice. On a `posix` host
    the hosting file is judged first: WSL running it from a Windows checkout under `/mnt/` returns
    no `found`, an empty `tried` and the wrong-shell refusal, before any candidate is tried."""
    host = host or ("windows" if os.name == "nt" else "posix")
    if host == "posix":
        here = os.path.abspath(__file__)
        wsl = bool(os.environ.get("WSL_DISTRO_NAME")) or os.path.exists("/proc/sys/fs/binfmt_misc/WSLInterop")
        if wrong_shell_at(here, wsl):
            return "", [], ("WSL is running " + here + " from a Windows checkout under /mnt/; "
                            "run it with Git's bash (C:/Program Files/Git/bin/bash.exe)")
    tried, seen = [], set()

    def run_probe(cand):
        try:
            r = subprocess.run([cand, "-c", 'uname -s && { [ -z "$1" ] || test -f "$1"; }', "_", str(script)],
                               stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            return "did not run"
        u = r.stdout.decode("utf-8", "replace").replace("\x00", "").split("\n")[0].strip()
        if not u:
            return "did not run"
        if host == "windows" and not u.startswith(("MINGW", "MSYS")):
            return "answered " + u
        return "runs" if r.returncode == 0 else "cannot see " + str(script)

    def check_candidate(cand):
        key = cand.lower() if host == "windows" else cand
        if key in seen:
            return False
        seen.add(key)
        low = cand.lower()
        why = "a launcher" if "/system32/" in low or "/windowsapps/" in low else run_probe(cand)
        tried.append(cand + ": " + why)
        return why == "runs"

    gov = os.environ.get("GOV_BASH", "")
    if gov:
        why = run_probe(gov)
        tried.append(gov + ": " + why)
        if why == "runs":
            return gov, tried, ""
        return "", tried, ("GOV_BASH is set to '" + gov + "' and " + why + ", so nothing after it is tried: "
                           "an override that is set and unusable is refused, never a fall-through")
    try:
        r = subprocess.run(["git", "--exec-path"], stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        ex = r.stdout.decode("utf-8", "replace").strip().replace("\\", "/") if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        ex = ""
    found = ""
    if not ex:
        tried.append("git --exec-path: did not run")
    else:
        cand = "/".join(ex.rstrip("/").split("/")[:-3]) + "/bin/bash.exe"
        if not os.path.isfile(cand):
            tried.append(cand + ": absent")
        elif check_candidate(cand):
            found = cand
    for d in os.environ.get("PATH", "").split(os.pathsep):
        for name in BASH_NAMES:
            cand = (d.rstrip("/\\") + "/" + name).replace("\\", "/")
            if d and os.path.isfile(cand) and check_candidate(cand):
                found = found or cand
    if found:
        return found, tried, ""
    return "", tried, ("no bash runs" + (" that can see " + str(script) if script else "") + ": "
                       + "; ".join(tried) + "; set GOV_BASH to Git's bash")
# <<< resolve_bash_py


# >>> git_env_leaks_py -- canonical copy: git_env_leaks.py in the gov lib dir (byte-identical; gated)
# The eight location variables git EXPORTS to a hook, which reach any subprocess the hook starts and
# name another tree than the one a reader was pointed at; and the four pathspec-mode variables a
# caller can carry, which turn a `:(glob)` pathspec into a literal name that matches nothing.
GIT_ENV_LEAKS = (
    "GIT_DIR",
    "GIT_WORK_TREE",
    "GIT_INDEX_FILE",
    "GIT_OBJECT_DIRECTORY",
    "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    "GIT_COMMON_DIR",
    "GIT_NAMESPACE",
    "GIT_PREFIX",
    "GIT_LITERAL_PATHSPECS",
    "GIT_GLOB_PATHSPECS",
    "GIT_NOGLOB_PATHSPECS",
    "GIT_ICASE_PATHSPECS",
)
# <<< git_env_leaks_py


def read_clean_env(**put):
    """This process's environment less the inline `git_env_leaks` block's `GIT_ENV_LEAKS`, with `put`
    set, so a git call made under a hook reads the tree it was pointed at."""
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS}
    env.update(put)
    return env


# >>> acceptance_reader -- canonical copy: check-spec-tokens.py in the gov tools dir (byte-identical; gated)
# The acceptance section by its heading text and its backticked tokens: `fix_keeps.py` in the
# unattended kit carries this block inline, and the parity table reds a copy that drifts.
TICK = re.compile(r"`([^`\n]+)`")
AC_HEAD = re.compile(r"^## [0-9]+[.] Acceptance criteria[ \t]*$", re.M)


def extract_acceptance(text):
    """The acceptance section by its HEADING TEXT — `extract_gates` with `AC_HEAD` in its place.

    TOOL-aDeferredBar-2. Both bullet-loop joins read it: the ordinal read graded whatever sat sixth,
    which under the light profile is the Gates section. None when the spec carries no such heading,
    which the bullet loop reads as an empty population.
    """
    m = AC_HEAD.search(text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[:nxt.start()] if nxt else rest
# <<< acceptance_reader


def check_check_file(path):
    """True when the repo-relative `path` is a check file by section 8 F2's class."""
    parts = path.split("/")
    name = parts[-1]
    return (name.endswith(CHECK_SUFFIXES) or (name.startswith("test_") and name.endswith(".py"))
            or "fixtures" in parts[:-1])


def read_leg_files(rows, name, tool_root, tracked):
    """The leg `name`'s own files: each word of its `argv`, `{prefix}` resolved against `tool_root`,
    that carries a `/`, no whitespace, and is in `tracked`, in argv order; then every tracked file under
    a `fixtures/` or `fixture/` directory inside the gate script's own kit directory, the first such
    word's `<tool root>/<kit>/`, sorted (TOOL-dWitnessedBar-51 S35). A product module the script imports
    is not kept. LookupError naming an unknown leg."""
    tracked = sorted(set(tracked))
    row = next((r for r in rows if isinstance(r, dict) and r.get("name") == name), None)
    if row is None:
        raise LookupError("no leg named '%s' in the leg manifest, so its own files cannot be read" % name)
    kept, present = [], set(tracked)
    for word in row.get("argv") or []:
        word = resolve_prefix_token(str(word), tool_root)
        if "/" in word and not any(c.isspace() for c in word) and word in present and word not in kept:
            kept.append(word)
    if kept:
        root = (tool_root.strip("/") + "/") if tool_root not in ("", ".") else ""
        rest = kept[0][len(root):] if kept[0].startswith(root) else kept[0]
        kit = root + rest.split("/", 1)[0] + "/" if "/" in rest else kept[0].rsplit("/", 1)[0] + "/"
        for path in tracked:
            inner = path[len(kit):].split("/")[:-1] if path.startswith(kit) else ()
            if any(d in FIXTURE_DIRS for d in inner) and path not in kept:
                kept.append(path)
    return kept


def read_leg_tests(rows, name):
    """The targets of the leg `name`'s `tests` edge, each a `feature.<f>` tag; [] where it has none."""
    row = next((r for r in rows if isinstance(r, dict) and r.get("name") == name), {})
    tests = row.get("tests") or []
    return [str(t) for t in tests] if isinstance(tests, list) else []


def read_acceptance_files(spec_text, tracked):
    """The check files the backticked tokens of the spec's acceptance-criteria section name, in the
    order they are named: a word that is a tracked path, or a bare basename exactly one tracked
    file carries, kept when `check_check_file` holds for it. The section is found by heading text and
    its tokens read by the `acceptance_reader` block, the spec-token checker's own reader carried
    inline (TOOL-dWitnessedBar-51 S19), so a light-profile spec's section is read wherever it sits."""
    tracked = list(tracked)
    paths = set(tracked)
    names = {}
    for path in tracked:
        names.setdefault(path.rsplit("/", 1)[-1], []).append(path)
    section = extract_acceptance(spec_text.replace("\r\n", "\n")) or ""
    kept = []
    for token in TICK.findall(section):
        for word in token.split():
            word = word.strip("'\"")
            path = word if word in paths else None
            if path is None and "/" not in word and len(names.get(word, ())) == 1:
                path = names[word][0]
            if path and check_check_file(path) and path not in kept:
                kept.append(path)
    return kept


def read_leg_manifest(here=KIT):
    """`(repository, tool root, manifest)`: `gate-legs.json` in the directory holding the run-gates
    kit found from `here`, the repository the nearest directory above it holding `.git`, and the tool
    root that directory relative to it. LookupError where either does not resolve."""
    manifest = resolve_kit_dir(*RUN_GATES, here).parent / "gate-legs.json"
    if not manifest.is_file():
        raise LookupError("no leg manifest at %s" % manifest.as_posix())
    repo = next((d for d in (manifest.parent, *manifest.parent.parents) if (d / ".git").exists()), None)
    if repo is None:
        raise LookupError("the leg manifest %s sits in no git repository" % manifest.as_posix())
    return repo, manifest.parent.relative_to(repo).as_posix(), manifest


def read_tracked_files(repo):
    """Every path `git ls-files` lists in `repo`, read with the hook's location variables dropped."""
    p = subprocess.run(["git", "-C", str(repo), "ls-files", "-z"], capture_output=True, timeout=120,
                       env=read_clean_env(), stdin=subprocess.DEVNULL)
    if p.returncode != 0:
        raise LookupError("git ls-files exited %d in %s" % (p.returncode, pathlib.Path(repo).as_posix()))
    return [s for s in p.stdout.decode("utf-8", "replace").split("\0") if s]


def print_keeps(red, spec):
    """`--keeps <red>`: the kept paths on stdout and the notes on stderr, exit 0; a refusal, exit 2."""
    tests = None
    try:
        repo, tool_root, manifest = read_leg_manifest()
        tracked = read_tracked_files(repo)
        if red.startswith("leg:") and red[4:]:
            rows = json.loads(manifest.read_text(encoding="utf-8"))
            if not isinstance(rows, list):
                raise LookupError("the leg manifest %s is not a list of rows" % manifest.as_posix())
            kept = read_leg_files(rows, red[4:], tool_root, tracked)
            tests = read_leg_tests(rows, red[4:])
        elif red == "acceptance":
            if not spec:
                raise LookupError("--keeps acceptance needs --spec <the unit's spec>, whose acceptance commands it reads")
            kept = read_acceptance_files(pathlib.Path(spec).read_text(encoding="utf-8"), tracked)
        else:
            raise LookupError("the red '%s' is neither leg:<leg name> nor acceptance" % red)
    except (LookupError, OSError, ValueError, subprocess.SubprocessError) as exc:
        print("%s: refused · %s" % (SAY, exc), file=sys.stderr)
        return 2
    for path in kept:
        print(path)
    if tests is not None:
        print("%s: tests %s" % (SAY, " ".join(tests) or "none"), file=sys.stderr)
    if not kept:
        print("%s: no kept file" % SAY, file=sys.stderr)
    return 0


# -------------------------------------------------------------------------------- the plants
FX_CONF = """MEMORY_ROOT=memory
UNITS_REGION_CUTOFF="2026-08-19"
PROMPT_BRIEF_CUTOFF="2099-01-01"
PROMPT_BRIEF_SKELETON_CUTOFF="2099-01-01"
LANDER="echo land"
LANDER_MODE="primary"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
GATE_BOUND="3600"
GATE_WALL="21600"
UNIT_STALL_BOUND="1800"
TASK_STALL_BOUND="5400"
RESUME_STALE_BOUND="5400"
WIRING_CHECK="true"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
RESUME_SCHEDULE="on"
RESUME_SCHEDULE_CREATE="TheScheduleCreate"
RESUME_SCHEDULE_DELETE="TheScheduleDelete"
RESUME_SCHEDULE_DELAY="1800"
RESUME_SCHEDULE_LIMIT="6"
RUN_CLAIMS="off"
PHASES_EXTRA=""
DOD_EXTRA=""
"""
FX_README = ("---\nslug: tFix\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: ARCH\n"
             "ids: %s\n---\n\n# tFix\n\n<!-- gen:build-index -->\n**Build status:** OPEN · 1 unit(s)\n\n"
             "<!-- gen:build-units -->\n| Unit | Status | Rev | Last change |\n|---|---|---|---|\n"
             "| [%s — the unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |\n<!-- /gen:build-units -->\n"
             "<!-- /gen:build-index -->\n" % (FX_UNIT, FX_UNIT))
FX_SPEC_TEXT = ("# %s — the unit\n\n**Status:** INPROGRESS · rev-1 · 2026-08-01 · node a · Tier-1 · base 00000000"
                " · streams architecture\n\n## 2. Scope (IN)\n\n- **S1** — `%s` reads its fixture.\n\n"
                "## 6. Acceptance criteria\n\n- **AC1** — When `bash %s %s` runs, it prints `ok`.\n\n"
                "## 7. Gates\n\n`%s`\n\n## 8. Open questions\n\nnone\n" % (FX_UNIT, FX_PRODUCT, FX_PRODUCT,
                                                                          FX_FIXTURE, FX_LEG))
FX_RUN_TEXT = ("# tFix — run state\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Mandate\n"
               "<!-- run:mandate -->\nThe owner authorizes build tFix to merge to main and to push.\n"
               "<!-- /run:mandate -->\n\n## Run facts\n\n## Parked\n")


def run_fixture_git(repo, *args):
    """A git command in a fixture repository, under a fixed identity; CalledProcessError on a failure."""
    return subprocess.run(["git", "-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c",
                           "commit.gpgsign=false", "-c", "core.autocrlf=false", *args], cwd=repo, check=True,
                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                          env=read_clean_env(), timeout=TIMEOUT).stdout.strip()


def write_fixture_files(root, files):
    """Each `{repo-relative path: text}` written LF under `root`."""
    for rel, text in files.items():
        path = pathlib.Path(root, rel)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)


def remove_tree(path):
    """Delete a fixture directory, git's read-only objects made writable first; a refused delete is
    named on stderr and left in the temp directory."""
    def remove_readonly(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    try:
        shutil.rmtree(path, onexc=remove_readonly)
    except OSError as exc:
        print("%s: leaked %s · %s" % (SAY, pathlib.Path(path).as_posix(), exc), file=sys.stderr)


def write_fixture_repo(root):
    """The fixture repository under `root`, its run preflighted on the branch `unit` and committed:
    `(repo, the driver copy)`."""
    repo, origin = root / "r", root / "o.git"
    kit = repo / FX_ROOT / KIT.name
    kit.mkdir(parents=True)
    for name in KIT_FILES:
        shutil.copyfile(KIT / name, kit / name)
    gates = (repo / FX_ROOT).joinpath(*RUN_GATES)
    manifest = [{"name": FX_LEG, "tag": "leg.fx.canary", "tests": ["feature.fx"],
                 "purpose": "the fixture's one leg", "argv": ["bash", "{prefix}/fx/fx.test.sh"]}]
    write_fixture_files(repo, {
        ".unattended.conf": FX_CONF,
        "memory/builds/tFix/README.md": FX_README,
        FX_SPEC: FX_SPEC_TEXT,
        FX_RUN: FX_RUN_TEXT,
        "memory/guides/BUILD-METHOD.md": "# build method (stub)\n\n## M1\n\nExistence is what the driver tests.\n",
        gates.relative_to(repo).as_posix(): "#!/usr/bin/env bash\nexit 0\n",
        FX_ROOT + "/gate-legs.json": json.dumps(manifest, indent=1) + "\n",
        FX_SUITE: "#!/usr/bin/env bash\nbash \"$(dirname \"$0\")/fx.sh\" \"$(dirname \"$0\")/fixtures/a.txt\"\n",
        FX_PRODUCT: "#!/usr/bin/env bash\n[ -f \"$1\" ] && echo ok\n",
        FX_FIXTURE: "a\n"})
    run_fixture_git(repo, "init", "-q", "-b", "main", "--template=")
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-qm", "base")
    run_fixture_git(root, "init", "-q", "--bare", str(origin))
    run_fixture_git(root, "--git-dir", str(origin), "symbolic-ref", "HEAD", "refs/heads/main")
    for where in (("-C", str(repo)), ("--git-dir", str(origin))):
        run_fixture_git(root, *where, "config", "user.email", "fx@example.invalid")
        run_fixture_git(root, *where, "config", "user.name", "fx")
    run_fixture_git(repo, "remote", "add", "fx", str(origin))
    run_fixture_git(repo, "push", "-q", "fx", "main")
    base = run_fixture_git(repo, "rev-parse", "HEAD")
    run_fixture_git(repo, "checkout", "-q", "-b", "unit")
    run_fixture_git(repo, "commit", "-q", "--allow-empty", "-m", "unit work")
    return repo, kit / "unattended.sh", base


def run_plant_driver(bash, driver, repo, *argv):
    """One driver call in the fixture: `(exit, stdout and stderr)`, each line printed indented."""
    env = read_clean_env(GOV_DEFAULT_BRANCH="main", CLAUDE_CODE_SESSION_ID="fixture-session",
                         CLAUDE_PID="999999999")
    try:
        p = subprocess.run([bash, str(driver), *argv], cwd=repo, env=env, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=TIMEOUT, stdin=subprocess.DEVNULL)
        rc, said = p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired:
        rc, said = 124, "the driver passed its %d s bound" % TIMEOUT
    print("%s: driver %s · exit %d" % (SAY, " ".join(argv[:1]), rc))
    for line in said.splitlines():
        print("    " + line)
    return rc, said


def read_run_rows(repo, kind):
    """The run-state file's rows of `kind` for the fixture's unit."""
    text = pathlib.Path(repo, FX_RUN).read_text(encoding="utf-8")
    return [ln for ln in text.splitlines() if re.match(r"^\S+ %s · item [0-9a-f]+ %s · reason " % (
        re.escape(kind), re.escape(FX_UNIT)), ln)]


def check_fixture_plant(plant, root, bad):
    """Build the fixture and drive the driver through `plant`, appending each failure to `bad`.
    -> 2 where no bash that can see the driver runs, else None."""
    repo, driver, base = write_fixture_repo(root)
    bash = scan_bash(str(driver))[0]
    if not bash:
        print("%s: %s · unarmed · %s" % (SAY, plant, scan_bash(str(driver))[2]))
        return 2

    def run_driver(*argv):
        return run_plant_driver(bash, driver, repo, *argv)

    if plant == "light-profile":
        return check_light_profile(repo, bad)
    # a FIRST preflight refuses a carried branch, so local main stands at HEAD for that call alone
    run_fixture_git(repo, "update-ref", "refs/heads/main", "HEAD")
    rc, said = run_driver("--preflight", "tFix", "--keepalive-id", "k1")
    run_fixture_git(repo, "update-ref", "refs/heads/main", base)
    if rc != 0:
        bad.append("--preflight exited %d: %s" % (rc, said[-600:]))
        return None
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-qm", "records(tFix): preflight")
    run_md = pathlib.Path(repo, FX_RUN)
    leg = "leg:" + FX_LEG
    dispatch = ("--dispatch", "tFix", "--pass", FX_UNIT)
    if plant in ("writes-test-file", "writes-fixture", "unknown-leg"):
        before = run_md.read_bytes()
        red, needles = ((leg, ("UNATTENDED check 49 FAILED", FX_SUITE, "gov-tester", "spec-wrong", "feature.fx"))
                        if plant == "writes-test-file" else
                        (leg, ("UNATTENDED check 49 FAILED", FX_FIXTURE)) if plant == "writes-fixture" else
                        ("leg:nope", ("UNATTENDED check 49 FAILED", "nope")))
        writes = {"writes-test-file": FX_SUITE, "writes-fixture": FX_FIXTURE}.get(plant, FX_PRODUCT)
        rc, said = run_driver(*dispatch, "--writes", writes, "--fix-of", red)
        if rc == 0 or not all(n in said for n in needles):
            bad.append("--dispatch --fix-of %s --writes %s exited %d, not non-zero printing %s" % (
                red, writes, rc, " and ".join(needles)))
        if run_md.read_bytes() != before:
            bad.append("the refused dispatch changed %s, so it recorded something" % FX_RUN)
        return None
    if plant in ("writes-product", "commit-test-file"):
        rc, said = run_driver(*dispatch, "--writes", FX_PRODUCT, "--fix-of", leg)
        rows = read_run_rows(repo, "fix-of")
        if rc != 0 or "dispatch declared" not in said:
            bad.append("--dispatch --fix-of %s --writes %s exited %d, not 0 declaring it" % (leg, FX_PRODUCT, rc))
        if len(rows) != 1 or not rows[0].endswith(" · reason " + leg):
            bad.append("%s holds %d fix-of row(s) for %s, not one naming %s: %s" % (FX_RUN, len(rows), FX_UNIT,
                                                                                   leg, rows))
        if plant == "writes-product" or bad:
            return None
        msg = root / "msg.txt"
        write_fixture_files(root, {"msg.txt": "fix(tFix): %s, the product fixed\n\nPass: %s\n" % (FX_UNIT, FX_UNIT)})
        write_fixture_files(repo, {FX_PRODUCT: "#!/usr/bin/env bash\n[ -f \"$1\" ] && echo ok && exit 0\n"})
        run_fixture_git(repo, "add", "--", FX_PRODUCT)
        rc, said = run_driver("--check-commit", str(msg))
        if rc != 0:
            bad.append("--check-commit refused the product file alone, exit %d" % rc)
        write_fixture_files(repo, {FX_SUITE: "#!/usr/bin/env bash\nexit 0\n"})
        run_fixture_git(repo, "add", "--", FX_SUITE)
        rc, said = run_driver("--check-commit", str(msg))
        needles = ("UNATTENDED check 49 FAILED", FX_SUITE, "gov-tester", "spec-wrong")
        if rc == 0 or not all(n in said for n in needles):
            bad.append("--check-commit with %s staged exited %d, not non-zero printing %s" % (
                FX_SUITE, rc, " and ".join(needles)))
        return None
    # acceptance-fixture: the keeps read off the unit's own AC, then the two declarations they bound
    p = subprocess.run([sys.executable, str(driver.parent / pathlib.Path(__file__).name), "--keeps", "acceptance",
                        "--spec", FX_SPEC], cwd=repo, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=read_clean_env(), timeout=TIMEOUT, stdin=subprocess.DEVNULL)
    print("%s: --keeps acceptance · exit %d · %s" % (SAY, p.returncode, " ".join(p.stdout.split()) or "(nothing)"))
    if p.returncode != 0 or p.stdout.split() != [FX_FIXTURE]:
        bad.append("--keeps acceptance exited %d printing [%s], not 0 printing %s alone" % (
            p.returncode, " ".join(p.stdout.split()), FX_FIXTURE))
    rc, said = run_driver(*dispatch, "--writes", FX_FIXTURE, "--fix-of", "acceptance")
    if rc == 0 or "UNATTENDED check 49 FAILED" not in said or FX_FIXTURE not in said:
        bad.append("--dispatch --fix-of acceptance --writes %s exited %d, not non-zero naming it" % (FX_FIXTURE, rc))
    rc, said = run_driver(*dispatch, "--writes", FX_PRODUCT, "--fix-of", "acceptance")
    if rc != 0 or len(read_run_rows(repo, "fix-of")) != 1:
        bad.append("--dispatch --fix-of acceptance --writes %s exited %d, not 0 with one fix-of row" % (FX_PRODUCT, rc))
    return None


def check_light_profile(repo, bad):
    """`light-profile`: a Tier-1 spec with no production-readiness section, its acceptance section the
    fifth, read for its tokens by heading text; the keeps hold the fixture its AC names."""
    light = FX_SPEC_TEXT.replace("## 6. Acceptance criteria", "## 5. Acceptance criteria").replace(
        "## 7. Gates", "## 6. Gates").replace("## 8. Open questions", "## 7. Open questions")
    write_fixture_files(repo, {"memory/builds/tFix/spec/light.md": light})
    tracked = read_tracked_files(repo)
    got = read_acceptance_files(light, tracked)
    print("%s: light-profile keeps · %s" % (SAY, " ".join(got) or "(nothing)"))
    if got != [FX_FIXTURE]:
        bad.append("the light-profile spec's acceptance section kept [%s], not %s alone" % (" ".join(got), FX_FIXTURE))
    return None


def run_fixture(plant):
    """One plant in a scratch directory under the system temp directory: exit 0 PASS, 1 FAIL, 2 unarmed."""
    bad, root = [], pathlib.Path(tempfile.mkdtemp(prefix="fk-"))
    print("%s: fixture · plant %s · %s" % (SAY, plant, PLANTS[plant]))
    try:
        rc = check_fixture_plant(plant, root, bad)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as exc:
        detail = getattr(exc, "stderr", "") or ""
        bad.append("the fixture could not be built: %s %s" % (exc, str(detail).strip()[:300]))
        rc = None
    finally:
        remove_tree(root)
    if rc == 2:
        print("%s: UNARMED %s — no bash that can see the driver runs, which is never a pass" % (SAY, plant))
        return 2
    for why in bad:
        print("%s: FAIL %s · %s" % (SAY, plant, why))
    if bad:
        return 1
    print("%s: PASS %s" % (SAY, plant))
    return 0


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", newline="\n")
    ap = argparse.ArgumentParser(prog="fix_keeps.py", description="The files a fix pass keeps out of its write set.")
    ap.add_argument("--keeps", metavar="RED", help="leg:<leg name>, or acceptance with --spec")
    ap.add_argument("--spec", default="", help="the unit's spec, whose acceptance commands --keeps acceptance reads")
    ap.add_argument("--fixture", action="store_true", help="run one plant in a throwaway repository")
    ap.add_argument("--plant", choices=sorted(PLANTS), help="the case --fixture runs")
    opts = ap.parse_args(argv)
    if opts.fixture:
        if not opts.plant:
            ap.error("--fixture needs --plant <case>")
        return run_fixture(opts.plant)
    if opts.keeps is None:
        ap.error("name --keeps <red>, or --fixture --plant <case>")
    return print_keeps(opts.keeps, opts.spec)


if __name__ == "__main__":
    sys.exit(main())
