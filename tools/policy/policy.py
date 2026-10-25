"""policy.py - the policy kit's module: its catalogue, the value check, the shape audit, the
shrink-only list of keys that carry no summary or no usage (TOOL-dGroundRules-1), the direction
check over the loop bound and deadline rows (TOOL-dGroundRules-11), and the reader
(TOOL-dGroundRules-2) with its one resolution order (TOOL-dGroundRules-3), its invalid-file
branch (TOOL-dGroundRules-4), the JSON mirror the hooks read (TOOL-dGroundRules-5), and the
shrink-only list of the legacy policy homes, derived from the files they guard (TOOL-dGroundRules-7),
gov's own and withheld from installs, so `lists --write` never creates it (TOOL-dGroundRules-17).
The size caps' half, the census, the switch and the `[budgets]` table's schema rule `validate`
calls, is `budgets.py` beside this file (TOOL-dGroundRules-9).

    python <this kit>/policy.py lists --check   # both lists against their derivations and baselines
    python <this kit>/policy.py lists --write   # drain both lists; neither ever gains a row
    python <this kit>/policy.py scaffold        # print the starter .governance/policy.toml
    python <this kit>/policy.py get <key> [--rev <rev>] [--explain] [--json]   # one key's value
    python <this kit>/policy.py check [--rev <rev>]   # the file at a revision, HEAD by default
    python <this kit>/policy.py mirror --write | --check | --print   # .governance/policy.json, rendered at HEAD
    python <this kit>/policy.py settings [--write|--check] [<file>]  # the harness's two concurrency settings

The catalogue, `catalogue.toml` beside this file, is the schema: one row per policy key. A file key
is matched to a row as a tuple of SEGMENTS, never as a joined string, because a quoted TOML segment
such as `budgets."AGENTS.md"` carries a dot. An exact name outranks a placeholder (`<word>`) or a
final `*`, each matching exactly one segment, and fewer placeholders outrank more.

THE READER reads `.governance/policy.toml` as committed at the landed revision, never from the
working tree, and parses it with tomllib, never by sourcing it: `read_policy_key`'s contract in the
unattended kit, carried to TOML. The landed revision is the remote tip the remote ladder names, or
with no remote at all the local default branch, and every reason names its sha through the read's
one `rev_phrase`, which the mirror's render spells `{rev}` (TOOL-dGroundRules-65). A key resolves in
RESOLUTION_ORDER, spelled once: the file's value, then the catalogue default with its reason. A
file `validate` refuses never reads a default: the whole file falls back to its last valid revision
on the first-parent history, or refuses at a line, as that revision's `policy-file.on-invalid` says.

THE MIRROR, `.governance/policy.json`, is the copy JavaScript reads, since a hook cannot parse TOML.
`render_mirror` renders it for one revision, carrying the blob ids of the policy file and of the
catalogue there; `mirror --write` writes it at HEAD, which every landing runs through this kit's
`[[generated]]` row; `policy-mirror.js` beside this file is its one reader, and takes a key from
the landed revision's mirror only while both ids match the blobs there.

THE AGENT LIMIT, `runtime.agents-in-flight` (TOOL-dGroundRules-10), is lowered by `resolve_read` to a
`FANOUT_CAP` line `.agent-cap.conf` holds at the revision read, its legacy home, and never raised by
it, so `get`, the mirror and the settings render read one value (TOOL-dGroundRules-15).
`settings --write` renders the resolved limit at HEAD into the harness's two concurrency settings
in the settings file in force, `GOV_SETTINGS_JSON` else `.claude/settings.json`, which this kit's
`[[generated]]` row regenerates at every landing (TOOL-dGroundRules-21 S34).

Exit 0 green, 1 red, 2 usage or a refused read.
"""
import contextlib
import json
import os
import posixpath
import re
import subprocess
import sys
import tempfile
import tomllib
from collections import namedtuple
from pathlib import Path

KIT_POLICY_VERSION = "1.0"
KIT = Path(__file__).resolve().parent
CATALOGUE = "catalogue.toml"
POLICY_REL = ".governance/policy.toml"
# The git variables every git call here drops, INLINED byte-identically from the canonical copy named
# on its marker line and gated by the resolve-python self-test (TOOL-dGroundRules-21 S9): a reader
# started inside a hook or a fixture reads the repository it was pointed at, never the one the
# hook's environment names, and a pathspec it passes is never read as a literal.
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
# One TOML key, dotted bare or quoted segments, and nothing after it: the shape `parse_key` admits
# before tomllib decodes it, so `a = {b` or `a = 0 #` is refused rather than read as a key.
KEY_SEGMENT = r"""(?:[A-Za-z0-9_-]+|"(?:[^"\\\x00-\x1f\x7f]|\\.)*"|'[^'\x00-\x08\x0a-\x1f\x7f]*')"""
KEY_SHAPE = re.compile(rf"[ \t]*{KEY_SEGMENT}(?:[ \t]*\.[ \t]*{KEY_SEGMENT})*[ \t]*")
LIST = "unsummarised-keys.txt"
LIST_HEADER = (
    "# unsummarised-keys.txt - GENERATED by `python <this kit>/policy.py lists --write`, never edited.\n"
    "# The catalogue rows with no `summary` or no `usage`, sorted. SHRINK-ONLY: `lists --check` reds a\n"
    "# row the catalogue no longer owes, a row the catalogue owes and this list lacks, and a row the\n"
    "# list at the compare base did not carry. Give a row both fields, then `lists --write`.\n"
)
SCAFFOLD_OWNER = "dGroundRules"
SCAFFOLD_HEADER = (
    "# .governance/policy.toml - this repository's policy: one value per key, each checked against the\n"
    "# policy kit's catalogue.toml. Every key, its allowed values and its default: help/policy.md.\n"
)
REQUIRED = ("name", "allowed", "default", "owner")
OPTIONAL = ("empty", "summary", "usage", "registry", "direction")
SET_TYPES = ("set", "list")
COUNT_TYPES = ("count", "retry-count", "round-count", "route-back-count", "agent-count")
DURATION_TYPES = ("hours", "days", "seconds")
# The loop bound and deadline population, DERIVED from each row's typed-range noun and never typed as
# names (TOOL-dGroundRules-11): each member declares `direction = "raise-loosens"`. Every duration is
# a deadline, one that bounds no loop included, because over-inclusion fails safe.
LOOP_BOUND_TYPES = ("retry-count", "round-count", "route-back-count")
DEADLINE_TYPES = DURATION_TYPES
BARE = re.compile(r"[A-Za-z0-9_-]+")


def load_catalogue(kit):
    """The catalogue's rows in file order. A file that does not parse raises tomllib's error, whose
    message names the line."""
    doc = tomllib.loads((Path(kit) / CATALOGUE).read_text(encoding="utf-8"))
    return doc.get("key", [])


def render_json(v):
    return json.dumps(v, ensure_ascii=False)


def check_member(value, options):
    # Type AND value: `True == 1` and `2 == 2.0` in Python, and neither is the member a list names.
    return any(type(value) is type(o) and value == o for o in options)


def check_derived(default):
    return isinstance(default, dict) and set(default) == {"derived"}


DERIVED_WHY = "a derived default no reader computes yet"  # the refusal `read_default_value` makes of one


def render_dotted(segs):
    return ".".join(s if BARE.fullmatch(s) else render_json(s) for s in segs)


def check_value(row, value):
    """A reason `row` refuses `value`, or None when it admits it. Deny by default: a member outside
    a closed list is refused even where the row's `registry` names members a registry will add."""
    allowed = row.get("allowed")
    if isinstance(allowed, list):
        return None if check_member(value, allowed) else f"{render_json(value)} is not one of {render_json(allowed)}"
    if not isinstance(allowed, dict):
        return "the row's `allowed` is neither a list nor a table"
    if check_member(value, allowed.get("or", [])):
        return None
    t = allowed.get("type")
    if t == "enum":
        of = allowed.get("of", [])
        if check_member(value, of):
            return None
        reg = f"; {allowed['registry']} is admitted once a registry adds it" if "registry" in allowed else ""
        return f"{render_json(value)} is not one of {render_json(of)}{reg}"
    if t in SET_TYPES:
        if not isinstance(value, list):
            return f"{render_json(value)} is not an array"
        if not value:
            return "[] is refused: this set is never empty" if row.get("empty") == "never" else None
        for m in value:
            if "of" in allowed and check_member(m, allowed["of"]):
                continue
            if "item" in allowed and isinstance(m, str) and re.fullmatch(allowed["item"], m):
                continue
            return f"member {render_json(m)} is not admitted"
        if len({render_json(m) for m in value}) != len(value):
            return f"{render_json(value)} repeats a member"
        return None
    if t == "map":
        if not isinstance(value, dict):
            return f"{render_json(value)} is not a table"
        for k, v in value.items():
            if not check_member(v, allowed.get("of", [])):
                return f"{k} = {render_json(v)} is not one of {render_json(allowed.get('of', []))}"
        return None
    if t in COUNT_TYPES or t in DURATION_TYPES:
        if isinstance(value, str) and "pattern" in allowed:
            return None if re.fullmatch(allowed["pattern"], value) else f"{render_json(value)} is not of the form {allowed['pattern']}"
        if isinstance(value, bool) or not isinstance(value, int if t in COUNT_TYPES else (int, float)):
            return f"{render_json(value)} is not {'an integer' if t in COUNT_TYPES else 'a number'}"
        if "min" in allowed and value < allowed["min"]:
            return f"{render_json(value)} is below the minimum {allowed['min']}"
        if "max" in allowed and value > allowed["max"]:
            return f"{render_json(value)} is above the maximum {allowed['max']}"
        return None
    if t in ("pattern", "name"):
        rx = allowed.get("regex" if t == "pattern" else "item", "")
        if isinstance(value, str) and re.fullmatch(rx, value):
            return None
        return f"{render_json(value)} does not match {rx}"
    return f"the row's `allowed` type {render_json(t)} is not one this kit knows"


Resolution = namedtuple("Resolution", "value source reason")   # source: file | preset | default | last-valid


class Refusal(Exception):
    """A read the reader refuses, naming a path, a line (0 where it names none) and why."""

    def __init__(self, path, line, why):
        super().__init__(path, line, why)
        self.path, self.line, self.why = path, line, why

    def __str__(self):
        return f"policy: refused · {self.path}:{self.line} · {self.why}"


class DerivedDefault(Refusal):
    """A row whose default is { derived = ... }, which no reader computes yet (TOOL-dGroundRules-21
    S12): `get` and the mirror refuse it as any Refusal, and the caps module alone reads it as no file
    value (TOOL-dGroundRules-62)."""


def read_catalogue_row(path, catalogue):
    """The row of `catalogue`, `load_catalogue`'s rows, that a key path (a tuple of segments) names.
    A catalogue `name` is split on `.`, since no name carries a quoted segment; an exact segment
    outranks a `<word>` or `*` one, each standing for exactly one segment, and fewer of those outrank
    more. The module's one key-to-row matcher. No row is a Refusal naming the catalogue."""
    best = None
    for row in catalogue:
        pat = str(row.get("name", "")).split(".")
        if len(pat) != len(path):
            continue
        wild = 0
        for p, s in zip(pat, path):
            if p == s:
                continue
            if p == "*" or (p.startswith("<") and p.endswith(">")):
                wild += 1
                continue
            break
        else:
            if best is None or wild < best[0]:
                best = (wild, row)
    if best is None:
        raise Refusal((KIT / CATALOGUE).as_posix(), 0, f"{render_dotted(path)} is not a catalogue key")
    return best[1]


def scan_keys(doc, rows, prefix=()):
    """Yield (segments, row or None, value) for each key of a parsed policy document. A table is
    descended into unless a map-valued row names it, so a table's leaves are the keys graded."""
    for k, v in doc.items():
        segs = prefix + (k,)
        try:
            row = read_catalogue_row(segs, rows)
        except Refusal:
            row = None
        is_map = row is not None and isinstance(row.get("allowed"), dict) and row["allowed"].get("type") == "map"
        if isinstance(v, dict) and not is_map:
            yield from scan_keys(v, rows, segs)
        else:
            yield segs, row, v


def check_shape(rows):
    """(key, why) for each row the catalogue's own shape refuses."""
    out = []
    for i, row in enumerate(rows):
        key = str(row.get("name") or f"row {i + 1}")
        for f in REQUIRED:
            if f not in row:
                out.append((key, f"lacks the required field `{f}`"))
        for f in row:
            if f not in REQUIRED + OPTIONAL:
                out.append((key, f"carries the unknown field `{f}`"))
        allowed = row.get("allowed")
        is_set = isinstance(allowed, dict) and allowed.get("type") in SET_TYPES
        if is_set and "empty" not in row:
            out.append((key, "is set-valued and declares no `empty` rule, never or allowed"))
        if "empty" in row and not is_set:
            out.append((key, "declares `empty` and is not set-valued"))
        if "empty" in row and row["empty"] not in ("never", "allowed"):
            out.append((key, f"declares `empty` {render_json(row['empty'])}, which is neither never nor allowed"))
        if "allowed" in row and "default" in row and not check_derived(row["default"]):
            why = check_value(row, row["default"])
            if why:
                out.append((key, f"its own row refuses its default: {why}"))
        if "usage" in row and "allowed" in row:
            try:
                doc = tomllib.loads(str(row["usage"]))
            except tomllib.TOMLDecodeError as exc:
                out.append((key, f"its usage does not parse: {exc}"))
                continue
            hits = [v for _segs, r, v in scan_keys(doc, [row]) if r is row]
            if len(hits) != 1:
                out.append((key, f"its usage sets {len(hits)} value(s) of {key}, not one"))
            else:
                why = check_value(row, hits[0])
                if why:
                    out.append((key, f"its usage is refused by its own row: {why}"))
    return out


def derive_bounds(rows):
    """The loop bound and deadline rows in file order: each row whose `allowed` is a typed range of a
    LOOP_BOUND_TYPES or DEADLINE_TYPES noun. No row is named; the noun is the rule."""
    return [r for r in rows if isinstance(r.get("allowed"), dict)
            and r["allowed"].get("type") in LOOP_BOUND_TYPES + DEADLINE_TYPES]


def check_direction(rows):
    """(key, why) for each loop bound or deadline row that declares no `direction`, and each row
    whose `direction` is anything but raise-loosens, the one value a row may declare."""
    bounds = derive_bounds(rows)
    out = []
    for i, row in enumerate(rows):
        key = str(row.get("name") or f"row {i + 1}")
        if "direction" in row:
            if row["direction"] != "raise-loosens":
                out.append((key, "direction must be raise-loosens"))
        elif row in bounds:
            out.append((key, "a loop bound or deadline declares no direction"))
    return out


def derive_unsummarised(rows):
    """The sorted names of the rows with an empty or absent `summary` or `usage`."""
    return sorted(str(r["name"]) for r in rows if r.get("name") and (not r.get("summary") or not r.get("usage")))


def run_git(root, *args):
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS}
    try:
        r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env)
    except OSError:
        return None
    return r.stdout if r.returncode == 0 else None


def read_blob_at(repo, rev, path):
    """The text of `path` in the commit `rev` names, decoded as strict UTF-8, or None where that
    commit holds no such path. The module's one blob reader: the policy file's and the size caps'
    limits file's reads both come through it (TOOL-dGroundRules-21 S11). Bytes that are not UTF-8
    raise UnicodeDecodeError, which each caller turns into its own refusal (S10)."""
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS}
    try:
        r = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"], capture_output=True, env=env)
    except OSError:
        return None
    # The text layer's newline reading, which every reader here was written against.
    return r.stdout.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n") if r.returncode == 0 else None


@contextlib.contextmanager
def run_without_git_env():
    """The process environment without GIT_ENV_LEAKS for the `with` body, restored after: the
    inlined canonical blocks run git with the inherited environment, so a caller strips it here.
    ponytail: not thread-safe, which no caller needs today."""
    saved = {v: os.environ.pop(v) for v in GIT_ENV_LEAKS if v in os.environ}
    try:
        yield
    finally:
        os.environ.update(saved)


# The remote ladder (TOOL-dLadderedRemote-1), INLINED byte-identically from the canonical copy
# named on its marker line and gated by the resolve-python self-test: a kit may not import a sibling.
# >>> remote_ladder_py -- canonical copy: resolve_remote.py in the gov lib dir (byte-identical; gated)
def resolve_remote(root):
    """-> (remote, branch, observed, refusal) for the repository at <root>. Fetches nothing.

    remote    GOV_REMOTE, else branch.<current>.remote unless it is ".", else the ONLY remote.
              Several remotes and none chosen, or a chosen name that is not a remote here, is a
              REFUSAL naming GOV_REMOTE. No remote at all is remote "" and NO refusal: the caller
              keeps its own no-remote fallback.
    observed  the branch refs/remotes/<remote>/HEAD names, or "". A caller whose GOV_DEFAULT_BRANCH
              only CROSS-CHECKS the observation reads this one.
    branch    GOV_DEFAULT_BRANCH, else observed, else "".
    A refusal empties the other three, so no caller can pick a remote the ladder refused.
    """
    import os
    import subprocess

    def read(*args):
        try:
            p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return ""
        return p.stdout.strip() if p.returncode == 0 else ""

    names = read("remote").split()
    listed = " ".join(names) or "none"
    # FULL refs, never `--short`: a tag or branch sharing the name makes the short form ambiguous
    # (`heads/x`, `remotes/r/x`), and the prefix is stripped exactly instead.
    cur = read("symbolic-ref", "--quiet", "HEAD")
    cur = cur[len("refs/heads/"):] if cur.startswith("refs/heads/") else ""
    remote, how = os.environ.get("GOV_REMOTE") or "", "GOV_REMOTE"
    if not remote and cur:
        remote, how = read("config", "branch." + cur + ".remote"), "branch." + cur + ".remote"
        if remote == ".":
            remote = ""
    if not remote and len(names) == 1:
        remote = names[0]
    if not remote and len(names) > 1:
        where = "branch " + cur if cur else "a detached HEAD"
        return "", "", "", ("cannot choose a remote: GOV_REMOTE is unset, %s has no configured remote, "
                            "and this repository has %d remotes (%s). Name it: export GOV_REMOTE=<remote>."
                            % (where, len(names), listed))
    if remote and remote not in names:
        return "", "", "", ("%s names %s, which is no remote of this repository (%s). Name one that is: "
                            "export GOV_REMOTE=<remote>." % (how, remote, listed))
    observed = ""
    if remote:
        pre = "refs/remotes/" + remote + "/"
        head = read("symbolic-ref", "--quiet", pre + "HEAD")
        if head.startswith(pre) and len(head) > len(pre):
            observed = head[len(pre):]
    return remote, os.environ.get("GOV_DEFAULT_BRANCH") or observed, observed, ""
# <<< remote_ladder_py


# The compare base both shrink-only lists read (TOOL-dGroundRules-21 S7, S23), INLINED byte-identically
# from the canonical copy named on its marker line and gated by the resolve-python self-test; the
# codebase map's baseline carries the same block, so the two kits grade a branch by one rule.
# >>> compare_base_py -- canonical copy: compare_base.py in the gov lib dir (byte-identical; gated)
def resolve_compare_base(root):
    """-> (sha or None, why): the revision a shrink-only list at <root> is compared against.

    The merge bar rule: the remote the inlined ladder resolves and the branch its HEAD names (`main`
    when none is named), its merge-base with HEAD where that is a PROPER ancestor of HEAD, else the
    remote tip. So a branch is graded on what IT changed, and a key the default branch deleted after
    the branch opened is not misread as one the branch added. Fetches nothing: no remote-tracking
    ref, no answer; a ladder refusal is no answer either, and says why. The OBSERVED branch, never
    GOV_DEFAULT_BRANCH: an environment value must not move the base a shrink-only assert grades.
    """
    import subprocess

    def read(*args):
        try:
            p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return ""
        return p.stdout.strip() if p.returncode == 0 else ""

    remote, _branch, observed, refusal = resolve_remote(root)
    if refusal:
        return None, refusal
    if not remote:
        return None, "no remote to compare against"
    branch = observed or "main"
    tip = read("rev-parse", "--verify", "-q", "refs/remotes/" + remote + "/" + branch + "^{commit}")
    if not tip:
        return None, "no %s/%s ref to compare against (never fetched)" % (remote, branch)
    head = read("rev-parse", "--verify", "-q", "HEAD")
    mb = read("merge-base", "HEAD", tip)
    if mb and mb != head:
        return mb, "merge-base of HEAD and %s/%s" % (remote, branch)
    return tip, "%s/%s tip" % (remote, branch)
# <<< compare_base_py


# ---- the reader (TOOL-dGroundRules-2) ---------------------------------------------------------

def resolve_commit(repo, rev):
    """The full sha of the commit `rev` names in `repo`, or a Refusal naming `rev`. A rev that opens
    with `-` names no commit: git would read it as an option."""
    sha = "" if rev.startswith("-") else (run_git(repo, "rev-parse", "--verify", "-q", f"{rev}^{{commit}}") or "").strip()
    if not sha:
        raise Refusal(POLICY_REL, 0, f"{rev} names no commit in this repository")
    return sha


def derive_landed_revision(repo):
    """-> (full sha, how it was found). The remote is the ladder's alone, `resolve_remote` being this
    module's one `git remote` read: the landed ref is refs/remotes/<remote>/<branch>, the branch the
    ladder's else main, and with no remote at all the local refs/heads/<branch>. A ladder refusal, or
    a ref that names no commit, is a Refusal. Where the ladder named no branch and the `main` fallback
    names no commit, the Refusal names that fallback and how to name the default branch
    (TOOL-dGroundRules-73)."""
    with run_without_git_env():  # the ladder's block is canonical and inherits this process's environment
        remote, branch, _observed, refusal = resolve_remote(repo)
    if refusal:
        raise Refusal(POLICY_REL, 0, refusal)
    fallback = not branch
    branch = branch or "main"
    ref = f"refs/remotes/{remote}/{branch}" if remote else f"refs/heads/{branch}"
    try:
        sha = resolve_commit(repo, ref)
    except Refusal as exc:
        if not fallback:
            raise
        if remote:
            raise Refusal(POLICY_REL, 0, f"{exc.why}, and main is only the fallback: refs/remotes/{remote}/HEAD "
                          f"names no branch and GOV_DEFAULT_BRANCH is unset. Name the default branch: "
                          f"git remote set-head {remote} -a, or export GOV_DEFAULT_BRANCH=<branch>.") from None
        raise Refusal(POLICY_REL, 0, f"{exc.why}, and main is only the fallback: this clone has no remote and "
                      f"GOV_DEFAULT_BRANCH is unset. Name the local default branch: "
                      f"export GOV_DEFAULT_BRANCH=<branch>.") from None
    if remote:
        return sha, f"{remote}/{branch}, the landed revision"
    return sha, f"local {branch}: this clone has no remote"


def read_policy_text(repo, rev):
    """The policy file's text in the commit `rev` names, decoded as UTF-8 by `read_blob_at`, or None
    where that commit holds no such path. A rev naming no commit is a Refusal; bytes that are not
    UTF-8 raise UnicodeDecodeError. One leading U+FEFF, the BOM an editor or a PowerShell write adds,
    is stripped by every parse, by the one helper below, as the `.agent-cap.conf` reader tolerates
    one (TOOL-dGroundRules-25 S30). The working-tree file is never opened."""
    return read_blob_at(repo, resolve_commit(repo, rev), POLICY_REL)


def derive_bomless_text(text):
    """`text` less one leading U+FEFF, the BOM an editor or a PowerShell write adds and tomllib
    rejects: the one strip every reader of the policy file calls before it parses
    (TOOL-dGroundRules-32 S12). `guard.py` imports no reader, so it mirrors this inline."""
    return text[1:] if text.startswith("\ufeff") else text


def parse_policy(text):
    """{key path: value} for each leaf of a policy file's text, through tomllib alone: a table is
    descended into and is never a value. Text that is not TOML raises tomllib.TOMLDecodeError."""
    out, todo = {}, [((), tomllib.loads(derive_bomless_text(text)))]
    while todo:
        prefix, node = todo.pop()
        for k, v in node.items():
            if isinstance(v, dict):
                todo.append((prefix + (k,), v))
            else:
                out[prefix + (k,)] = v
    return out


def parse_key(key):
    """A CLI key's path, a tuple of segments, by TOML's own key grammar: `<key> = 0` loaded with
    tomllib and its one key walked, so `budgets."CLAUDE.md"` is two segments. A string that is not
    one TOML key is a Refusal."""
    try:
        if not KEY_SHAPE.fullmatch(key):
            raise ValueError(key)
        node, path = tomllib.loads(f"{key} = 0"), ()
    except ValueError:  # tomllib.TOMLDecodeError is one
        raise Refusal(POLICY_REL, 0, f"{render_json(key)} is not one TOML key") from None
    while isinstance(node, dict):
        (seg, node), = node.items()
        path += (seg,)
    return path


# ---- the invalid-file branch (TOOL-dGroundRules-4) --------------------------------------------

Problem = namedtuple("Problem", "line key why")   # key "" for text that is not TOML
TABLE_HEADER = re.compile(r"[ \t]*\[\[?(.*?)\]\]?[ \t]*(?:#.*)?")
ASSIGNED_KEY = re.compile(rf"[ \t]*{KEY_SEGMENT}(?:[ \t]*\.[ \t]*{KEY_SEGMENT})*[ \t]*(?==)")


def derive_key_line(text, path):
    """The 1-based line of a policy file's text that assigns the key path `path`, reading each table
    header and each assignment's key with `parse_key`; 0 where the key sits in an inline table or no
    line assigns it."""
    # ponytail: a line inside a multi-line string or array that looks like `k = v` is read as one;
    # the cost is a wrong line number on such a file, never a wrong verdict.
    table = ()
    for n, ln in enumerate(text.splitlines(), 1):
        hdr, key = TABLE_HEADER.fullmatch(ln), ASSIGNED_KEY.match(ln)
        try:
            if hdr:
                table = parse_key(hdr[1])
                if table == path:
                    return n
            elif key:
                full = table + parse_key(key[0])
                if full == path:
                    return n
                if path[:len(full)] == full:
                    return 0  # the key sits in this line's inline table
        except Refusal:
            continue
    return 0


def validate(text, rows=None, census=None):
    """[Problem] for a policy file's text, [] for a valid one. Text that is not TOML is one problem at
    the decoder's line, key "". Text that parses yields one per leaf its catalogue row refuses, by
    `check_value`, and one per leaf no row matches, each at the line `derive_key_line` finds, then the
    `[budgets]` table's own rule, `budgets.check_budgets` over the cap census `census`, the working
    directory's by default (TOOL-dGroundRules-9). `rows` is `load_catalogue`'s, this kit's by default.
    The module's one judge of a policy file."""
    text = derive_bomless_text(text)
    try:
        doc = tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        at = re.search(r"at line (\d+)", str(exc))  # Python 3.14 carries `lineno`; 3.11 to 3.13 the message
        return [Problem(getattr(exc, "lineno", None) or (int(at[1]) if at else 0), "", str(exc))]
    out = []
    for segs, row, value in scan_keys(doc, load_catalogue(KIT) if rows is None else rows):
        why = "no catalogue row matches this key" if row is None else check_value(row, value)
        if why:
            out.append(Problem(derive_key_line(text, segs), render_dotted(segs), why))
    import budgets  # the caps module beside this file; it imports this one, so never at the top
    return out + budgets.check_budgets(doc, text, census)


def read_checked_text(repo, sha, rows=None):
    """(the policy file's text in the commit `sha` names, `validate`'s problems over it): None and []
    for an absent file. Text that is not UTF-8, as a PowerShell redirect writes it, is decoded inside
    the handler and handed on as one problem keyed "" with why opening `not UTF-8:`, which the
    invalid branch reads as it reads text that is not TOML (TOOL-dGroundRules-21 S10)."""
    try:
        text = read_policy_text(repo, sha)
    except UnicodeDecodeError as exc:
        return "", [Problem(0, "", f"not UTF-8: {exc}")]
    return text, [] if text is None else validate(text, rows)


def read_last_valid(repo, sha):
    """(sha, parsed table) of the newest revision on `sha`'s first-parent history whose policy file is
    present and `validate` admits, or None. Each commit of `git rev-list --first-parent <sha> --
    <file>` is read through `read_checked_text`; a revision where the file is absent is not valid."""
    for c in (run_git(repo, "rev-list", "--first-parent", sha, "--", POLICY_REL) or "").split():
        text, problems = read_checked_text(repo, c)
        if text is not None and not problems:
            return c, parse_policy(text)
    return None


def check_shallow(repo):
    """True where `repo` is a shallow clone, so a first-parent walk can end at its boundary."""
    return (run_git(repo, "rev-parse", "--is-shallow-repository") or "").strip() == "true"


def read_last_valid_value(path, row, read):
    """Resolution(value, "last-valid", reason) for `path` while the policy file of `read`, a
    `read_revision` read, is invalid: the whole file falls back, never one key. The last valid
    revision is walked to once per read and kept on it. `policy-file.on-invalid` is read from that
    revision by RESOLUTION_ORDER, never from the invalid file; with no valid revision, or with any
    value but `last-valid`, a Refusal at the first problem's line. Else RESOLUTION_ORDER over that
    revision's table, its reason naming the line, the problem, the valid sha, and the revision read
    through `read["rev_phrase"]` alone (TOOL-dGroundRules-65)."""
    sha, first = read["sha"], read["problems"][0]
    what = (f"{first.key}: " if first.key else "") + first.why
    if "last_valid" not in read:
        read["last_valid"] = read_last_valid(read["repo"], sha)
    found = read["last_valid"]
    if found is None and check_shallow(read["repo"]):  # the walk ended at the boundary, not the root
        raise Refusal(POLICY_REL, first.line, f"{what}; history is shallow at {sha[:8]}; fetch more history")
    if found is None:
        raise Refusal(POLICY_REL, first.line, f"{what}; no valid revision of the file precedes {sha[:8]}")
    valid, table = found
    # The valid revision is history the lander's rewrite keeps, so it is named by its own sha8.
    at = f"{valid[:8]}, walked back from {read['rev_phrase']}"
    if "on_invalid" not in read:
        on_path = parse_key("policy-file.on-invalid")
        read["on_invalid"] = read_ordered_value(on_path, read_catalogue_row(on_path, load_catalogue(KIT)), table, at).value
    on = read["on_invalid"]
    if on != "last-valid":  # deny by default: only the one fallback value falls back
        raise Refusal(POLICY_REL, first.line, f"{what}; policy-file.on-invalid is {on} at {valid[:8]}")
    hit = read_ordered_value(path, row, table, at)
    # ponytail: the opening names the revision read without its how-phrase, so it takes the phrase's
    # head before ", ": a sha8 holds no comma and the render's `{rev}` none, so the head is one or the other.
    named = read["rev_phrase"].split(", ", 1)[0]
    return Resolution(hit.value, "last-valid", f"{POLICY_REL} at {named} is invalid, line {first.line}: {what}; "
                      f"read from the last valid revision {valid[:8]}: {hit.reason}")


def check_revision(repo, rev):
    """The `check` verb's verdict on the policy file in the commit `rev` names: one line where it is
    valid, absent, or invalid with a last valid revision under `last-valid`; a Refusal otherwise."""
    read = read_revision(repo, rev)
    sha = read["sha"]
    if read["text"] is None:
        return f"policy: check · {POLICY_REL} is absent at {sha[:8]}, so every key reads its catalogue default"
    if not read["problems"]:
        return f"policy: check · {POLICY_REL} at {sha[:8]} is valid"
    on_path = parse_key("policy-file.on-invalid")
    hit = resolve_read(on_path, read_catalogue_row(on_path, load_catalogue(KIT)), read)
    return f"policy: check · every key falls back to the last valid revision · policy-file.on-invalid is {hit.value}: {hit.reason}"


def read_file_value(path, row, table, rev_phrase):
    """Resolution(value, "file", reason) when the parsed `table` sets `path`, else None. `row` is
    unread: every step of the resolution order shares this signature, `rev_phrase` the read's."""
    if table is None or path not in table:
        return None
    return Resolution(table[path], "file", f"set in {POLICY_REL} at {rev_phrase}")


def read_default_value(path, row, table, rev_phrase):
    """Resolution(the row's default, "default", reason), the reason naming the revision by
    `rev_phrase` and the case: the file absent (`table` None) or present and not setting `path`, then
    any `preset` the file names, which is not applied. A row with no `default` is a Refusal naming
    it, never an invented value, and so is a row whose default is `{ derived = "..." }`: its prose is
    no value, and a table read as one would be (TOOL-dGroundRules-21 S12)."""
    if "default" not in row:
        raise Refusal((KIT / CATALOGUE).as_posix(), 0,
                      f"the row {row.get('name')} carries no default, so {render_dotted(path)} has no value to read")
    if check_derived(row["default"]):
        raise DerivedDefault((KIT / CATALOGUE).as_posix(), 0, f"the row {row.get('name')} carries {DERIVED_WHY}, "
                      f"so {render_dotted(path)} has no value to read until the file sets it")
    at = f"at {rev_phrase}; the catalogue default"
    reason = f"{POLICY_REL} is absent {at}" if table is None else f"not set in {POLICY_REL} {at}"
    if table is not None and ("preset",) in table:
        p = table[("preset",)]
        reason += (f"; the file names preset {p if isinstance(p, str) else render_json(p)}, "
                   "not applied until dKeptSession adds presets to this reader")
    return Resolution(row["default"], "default", reason)


# The one order a key resolves in (TOOL-dGroundRules-3): `resolve` calls each step with (path, row,
# table, rev_phrase) and the first Resolution answers. dKeptSession adds its preset step between the two.
RESOLUTION_ORDER = (read_file_value, read_default_value)


def read_ordered_value(path, row, table, rev_phrase):
    """The first Resolution RESOLUTION_ORDER answers for `path` over a parsed `table`, None for an
    absent file, each reason naming the revision by `rev_phrase`."""
    for step in RESOLUTION_ORDER:
        hit = step(path, row, table, rev_phrase)
        if hit is not None:
            return hit
    # Unreachable while the default step stands, which answers or refuses: deny, never a None value.
    raise Refusal(POLICY_REL, 0, f"no step of the resolution order answers {render_dotted(path)} at {rev_phrase}")


def read_revision(repo, rev=None, rows=None):
    """The per-revision read `resolve_read` answers from (TOOL-dGroundRules-5): the revision, `rev`
    resolved to a full sha, else the landed one, and how it was found; the policy text there;
    `validate`'s problems; and the parsed table, None for an absent or invalid file. The last valid
    revision, its `policy-file.on-invalid` and the agent limit's `FANOUT_CAP` line join it on first
    need. A dict, so a render reads git once for every key. `rev_phrase`, `<sha8>, <how>`, is the one
    spelling of the revision read that every reason names (TOOL-dGroundRules-65); `render_mirror` sets
    it to `{rev}`."""
    sha, how = derive_landed_revision(repo) if rev is None else (resolve_commit(repo, rev), f"--rev {rev}")
    text, problems = read_checked_text(repo, sha, rows)
    table = None if text is None or problems else parse_policy(text)
    return {"repo": repo, "sha": sha, "how": how, "rev_phrase": f"{sha[:8]}, {how}", "text": text,
            "problems": problems, "table": table}


def resolve_read(path, row, read):
    """-> Resolution for the key path `path`, `row` its catalogue row, over one `read_revision` read:
    text `validate` refuses takes `read_last_valid_value`; valid text, and an absent file (table
    None), are answered by RESOLUTION_ORDER. The one composition of the two, and the one home of the
    agent limit's legacy lowering, `derive_lowered_limit`, applied to either branch's answer, so
    `get`, the mirror and the settings render all read the lowered limit (TOOL-dGroundRules-15)."""
    if read["problems"]:
        hit = read_last_valid_value(path, row, read)
    else:
        hit = read_ordered_value(path, row, read["table"], read["rev_phrase"])
    return derive_lowered_limit(hit, read) if path == AGENTS_PATH else hit


def resolve(key, repo=".", rev=None):
    """-> Resolution for `key`: its path and catalogue row, then `resolve_read` over the revision's
    read, `rev` resolved to a full sha, else the landed revision."""
    path = parse_key(key)
    rows = load_catalogue(KIT)
    return resolve_read(path, read_catalogue_row(path, rows), read_revision(repo, rev, rows))


# ---- the agent limit's legacy home (TOOL-dGroundRules-10) ----------------------------------------

AGENTS_PATH = ("runtime", "agents-in-flight")
LEGACY_FANOUT = ".agent-cap.conf"
FANOUT_LINE = re.compile(r"^\s*FANOUT_CAP\s*=(.*)$")


def read_legacy_fanout(repo, rev):
    """-> (n, line) for the last `FANOUT_CAP=<n>` or `FANOUT_CAP="<n>"` line of `.agent-cap.conf` at
    the checkout root in the commit `rev` names, or None where the file or the key is absent. The
    grammar agent-cap's retired clamp read: a BOM and a trailing CR tolerated, the last line winning.
    A value that is not an integer of at least 1 is a Refusal at its line; there is no upper bound."""
    text = run_git(repo, "show", f"{resolve_commit(repo, rev)}:{LEGACY_FANOUT}")
    if text is None:
        return None
    found = None
    for n, ln in enumerate(text.removeprefix("﻿").split("\n"), 1):
        m = FANOUT_LINE.match(ln)
        if m:
            found = (m[1].strip(), n)
    if found is None:
        return None
    raw, line = found
    value = raw[1:-1] if len(raw) >= 2 and raw[0] == raw[-1] == '"' else raw
    if not re.fullmatch(r"[0-9]+", value) or int(value) < 1:
        raise Refusal(LEGACY_FANOUT, line, "FANOUT_CAP must be an integer of at least 1")
    return int(value), line


def derive_lowered_limit(hit, read):
    """`hit`, the Resolution `resolve_read` found for runtime.agents-in-flight over `read`, lowered to
    the `FANOUT_CAP` line `read_legacy_fanout` finds at the read's own revision where that is smaller,
    the source kept and the line named in the reason; a line that does not lower it is named too. The
    conf is read once per read and kept on it; a malformed line is that reader's Refusal, so every
    reader of the limit refuses alike (TOOL-dGroundRules-15)."""
    if "legacy_fanout" not in read:
        read["legacy_fanout"] = read_legacy_fanout(read["repo"], read["sha"])
    found = read["legacy_fanout"]
    if found is None:
        return hit
    n, line = found
    at = f"{LEGACY_FANOUT}:{line}"
    if n < hit.value:
        return Resolution(n, hit.source, f"{hit.reason}; lowered to {n} by FANOUT_CAP at {at}")
    return hit._replace(reason=f"{hit.reason}; FANOUT_CAP={n} at {at} does not lower it")


# ---- the JSON mirror (TOOL-dGroundRules-5) -----------------------------------------------------

MIRROR_REL = ".governance/policy.json"
# Each legacy input the resolution reads, by its path at the revision read: the mirror records its
# blob id under `legacy_blobs`, and the helper reads a mirror whose ids differ at L as STALE. A unit
# adding a resolution input adds its path here (TOOL-dGroundRules-21 S17).
LEGACY_INPUTS = (LEGACY_FANOUT,)


def check_json_value(key, value):
    """`value` where JSON spells it, else a Refusal naming `key`: a TOML date or time, or a float
    that is not finite, has no JSON spelling."""
    try:
        json.dumps(value, allow_nan=False)
    except (TypeError, ValueError):
        raise Refusal(POLICY_REL, 0, f"{key} holds {value!r}, which JSON cannot spell") from None
    return value


def derive_catalogue_rel():
    """This kit's catalogue as a path from the top of the kit's repository, git's own spelling, or
    a Refusal where the kit is in no repository. A repository the kit is copied into at its own
    path, as the fixture does, holds the catalogue at the same path."""
    prefix = run_git(KIT, "rev-parse", "--show-prefix")
    if prefix is None:
        raise Refusal((KIT / CATALOGUE).as_posix(), 0, "the policy kit is in no git repository, so its catalogue has no blob")
    return prefix.strip() + CATALOGUE


def check_pattern_name(name):
    return any(s == "*" or (s.startswith("<") and s.endswith(">")) for s in str(name).split("."))


def render_mirror(repo, rev="HEAD"):
    """The mirror's bytes for the commit `rev` names: the blob ids of the policy file, of this kit's
    catalogue and of each LEGACY_INPUTS file there, null where absent, and the Resolution of every
    catalogue name with no `*` or `<...>` segment and of every key the file there sets that a pattern
    row matches, each through `resolve_read` over ONE `read_revision` read. A key whose resolution
    reaches a derived default is omitted, so the helper reads it through the reader, which refuses
    it (TOOL-dGroundRules-21 S12, §8 F4). Sorted keys, two-space indent, ASCII, LF: one revision
    renders one byte string. Every other Refusal of the resolution passes through.

    THE INVARIANT (TOOL-dGroundRules-65): two commits with the same policy blob, the same catalogue
    blob, the same legacy blobs (TOOL-dGroundRules-21 S17) and the same first-parent history render
    byte-identical mirrors. The read's `rev_phrase` is the placeholder `{rev}`, so no reason names the
    rendered commit, which the lander's commit-tree rewrite replaces; `policy-mirror.js` fills it with
    the landed revision it read."""
    rows = load_catalogue(KIT)
    read = read_revision(repo, rev, rows)
    read["rev_phrase"] = "{rev}"
    paths = {tuple(str(r["name"]).split(".")) for r in rows if r.get("name") and not check_pattern_name(r["name"])}
    keys = {}

    def add(p, row):
        try:
            hit = resolve_read(p, row, read)
        except DerivedDefault:  # its F4 omission; every other Refusal passes through
            return
        key = render_dotted(p)
        keys[key] = {"reason": hit.reason, "source": hit.source, "value": check_json_value(key, hit.value)}
    for p in sorted(paths):
        add(p, read_catalogue_row(p, rows))
    # The keys an invalid file reads come from its last valid revision, which the loop above walked to.
    table = (read.get("last_valid") or (None, None))[1] if read["problems"] else read["table"]
    for p in sorted(table or {}):
        try:
            row = read_catalogue_row(p, rows)
        except Refusal:
            continue
        if check_pattern_name(row["name"]):
            add(p, row)

    def read_blob(rel):
        return (run_git(repo, "rev-parse", "--verify", "-q", f"{read['sha']}:{rel}") or "").strip() or None
    doc = {"catalogue_blob": read_blob(derive_catalogue_rel()), "keys": keys,
           "legacy_blobs": {rel: read_blob(rel) for rel in LEGACY_INPUTS}, "policy_blob": read_blob(POLICY_REL)}
    return (json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def check_mirror_text(want, have):
    """None where the mirror's bytes `have` (None: absent) are the render `want`, else what differs
    first: `absent`, `unparsable`, a blob field, the first key in sorted order whose entry differs or
    that one side lacks, else `bytes`, a spelling no field shows."""
    if have == want:
        return None
    if have is None:
        return "absent"
    try:
        doc = json.loads(have.decode("utf-8"))
    except ValueError:  # UnicodeDecodeError and JSONDecodeError are both
        return "unparsable"
    if not isinstance(doc, dict) or not isinstance(doc.get("keys"), dict):
        return "unparsable"
    w = json.loads(want)
    for field in ("catalogue_blob", "legacy_blobs", "policy_blob"):
        if doc.get(field) != w[field]:
            return field
    return next((k for k in sorted(set(doc["keys"]) | set(w["keys"])) if doc["keys"].get(k) != w["keys"].get(k)), "bytes")


# ---- the harness's settings (TOOL-dGroundRules-10) -----------------------------------------------

SETTINGS_REL = ".claude/settings.json"
# The harness's own two concurrency settings: a direct spawn over the first is refused, a Workflow
# agent over the second queues. Both carry the one limit.
SETTINGS_VARS = ("CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS", "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS")


def render_settings(obj, n):
    """A copy of the parsed settings object `obj` whose `env` sets both SETTINGS_VARS to the limit
    `n` as a decimal string, every other key and its order kept, `env` created when absent."""
    out = dict(obj)
    out["env"] = {**(out.get("env") or {}), **{v: str(n) for v in SETTINGS_VARS}}
    return out


def cmd_settings(argv):
    """`settings [--write|--check] [<settings-file>]`, run in the repository: both SETTINGS_VARS of
    the settings file in force, resolved as `check-wiring.sh` resolves it: the file named, else
    `GOV_SETTINGS_JSON`, else `.claude/settings.json` under the repository root (TOOL-dGroundRules-21
    S34), against the limit `resolve` gives for runtime.agents-in-flight at HEAD. The variable steers
    only a call naming no file, so the landing's `[[generated]]` row, which names the tracked file,
    never renders elsewhere; a declared `GOV_SETTINGS_JSON` that is not a file refuses, exit 2, as
    `check-wiring.sh` refuses it, never a fallthrough (TOOL-dGroundRules-25 S32). `--check`, the
    default, exits 1 printing one line per variable that is absent or differs, 0 when both match;
    `--write` writes the render only when they differ, the two `env` keys alone and every other key
    kept, through a temporary file beside it and `os.replace`, so no reader meets half a file (S40).
    A Refusal, or a file that is not a JSON object holding an `env` object, exits 2 printing its line."""
    mode = next((a for a in argv if a in ("--write", "--check")), "--check")
    rest = [a for a in argv if a not in ("--write", "--check")]
    if len(rest) > 1 or any(a.startswith("-") for a in rest):
        print(USAGE, file=sys.stderr)
        return 2
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", newline="\n")
    named = rest[0] if rest else os.environ.get("GOV_SETTINGS_JSON") or ""
    rel = named or SETTINGS_REL
    top = (run_git(".", "rev-parse", "--show-toplevel") or "").strip()
    try:
        if not top:
            raise Refusal(rel, 0, "the working directory is in no git repository")
        if named and not rest and not Path(named).is_file():
            raise Refusal(rel, 0, "GOV_SETTINGS_JSON names it, and it is not a file")
        path = Path(named) if named else Path(top, rel)
        n = resolve(".".join(AGENTS_PATH), top, "HEAD").value
        try:
            obj = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
        except (OSError, ValueError) as exc:
            raise Refusal(rel, 0, f"does not read as JSON: {exc}") from None
        if not isinstance(obj, dict) or not isinstance(obj.get("env", {}), dict):
            raise Refusal(rel, 0, "is not a JSON object whose env is an object")
    except Refusal as exc:
        print(exc, file=sys.stderr)
        return 2
    env = obj.get("env", {})
    stale = [v for v in SETTINGS_VARS if env.get(v) != str(n)]
    if mode == "--check":
        for v in stale:
            have = f'"{env[v]}"' if v in env else "absent"
            print(f"policy: settings · {rel} · env.{v} is {have}, {'.'.join(AGENTS_PATH)} resolves {n}")
        if not stale:
            print(f"policy: settings fresh · {rel}")
        return 1 if stale else 0
    if stale:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(prefix=".settings-", suffix=".tmp", dir=path.parent)
        try:
            with os.fdopen(fd, "wb") as f:
                f.write((json.dumps(render_settings(obj, n), indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
            os.replace(tmp, path)
        except BaseException:
            Path(tmp).unlink(missing_ok=True)
            raise
        print(f"policy: settings written · {rel} · both variables at {n}")
    else:
        print(f"policy: settings fresh · {rel}")
    return 0


def parse_list(text):
    """The names of a list file's text: every line after its `#` header, CR stripped, blanks skipped."""
    return [ln.strip() for ln in text.replace("\r", "").split("\n") if ln.strip() and not ln.startswith("#")]


def check_list(kit, compare):
    """-> ((name, why) findings, note) for the shrink-only list against the catalogue and its base,
    `compare` the (sha or None, why) `resolve_compare_base` answered for `kit`."""
    kit = Path(kit)
    d = set(derive_unsummarised(load_catalogue(kit)))
    path = kit / LIST
    listed = parse_list(path.read_text(encoding="utf-8")) if path.is_file() else []
    out = [(n, "lacks a summary or a usage and is not listed") for n in sorted(d - set(listed))]
    out += [(n, "stale: drain it with `lists --write`") for n in sorted(set(listed) - d)]
    prefix = run_git(kit, "rev-parse", "--show-prefix")
    if prefix is None:
        return out, "no base: the kit is in no git repository, so only the catalogue is compared"
    base, why = compare
    if base is None:
        return out, f"no base: {why}; only the catalogue is compared"
    rel = prefix.strip() + LIST  # git's own spelling of the kit dir, so no two path forms are compared
    text = run_git(kit, "show", f"{base}:{rel}")
    if text is None:
        return out, f"no comparison: {rel} is absent at {base[:12]} ({why}), and absent is never an empty list"
    at_base = set(parse_list(text))
    out += [(n, f"added to a shrink-only list above the base {base[:12]}") for n in listed if n not in at_base]
    return out, f"base {base[:12]} ({why}) carried {len(at_base)}, the list carries {len(listed)}"


def write_list(kit):
    """Write L intersect D, sorted, under the header; an absent list is seeded with D. -> the names removed."""
    kit = Path(kit)
    d = derive_unsummarised(load_catalogue(kit))
    path = kit / LIST
    if path.is_file():
        listed = parse_list(path.read_text(encoding="utf-8"))
        keep = sorted(set(listed) & set(d))
        removed = sorted(set(listed) - set(keep))
    else:
        keep, removed = d, []
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LIST_HEADER + "".join(n + "\n" for n in keep))
    return removed


# ---- the legacy policy homes (TOOL-dGroundRules-7) ----------------------------------------------

LEGACY_LIST = "legacy-homes.txt"
# Why an absent list, or any list in an adopter's tree, grades nothing; the plan's row for it is
# `ORDER [project-owned]`, which asks the adopter for nothing (TOOL-dGroundRules-25 S10).
LEGACY_WITHHELD = ("the list is gov's own and is withheld from installs; the plan's ORDER [project-owned] row "
                   "for it is informational, and an adopter does not author the file")
RECEIPT_REL = f"{posixpath.dirname(POLICY_REL)}/install.json"
DEPLOYER_HOME = "govkit"
REGISTRY_REL = f"{DEPLOYER_HOME}/registry.toml"  # the deployer's registry, under the tool root of gov's tree alone


def derive_census_tree(repo):
    """-> ("adopter", the parsed receipt) where the tree under test holds an install receipt
    (TOOL-dGroundRules-22). With none (TOOL-dGroundRules-29): ("source", <d>) where exactly one
    `REGISTRY_REL` sits under a `<d>` 0 to 2 deep, the search govkit's `derive_tool_root`
    makes, since only gov's tree holds the registry; ("unadopted", None) where none does; and two or
    more is a Refusal naming each candidate. A receipt that is not a JSON object is a Refusal naming
    it, never a `source` answer. One whose `kits` is not a list of strings, or whose `prefix` is not a
    relative string free of `..` segments, is ("invalid", that field) (TOOL-dGroundRules-32 S11)."""
    try:
        text = Path(repo, RECEIPT_REL).read_text(encoding="utf-8")
    except FileNotFoundError:
        found = sorted({p.relative_to(repo).as_posix() for pat in ("", "*/", "*/*/")
                        for p in Path(repo).glob(pat + REGISTRY_REL)})
        if len(found) > 1:
            raise Refusal(", ".join(found), 0, f"{len(found)} {REGISTRY_REL} candidates, so the "
                          "tool root is not guessed and no row is graded") from None
        if not found:
            return "unadopted", None
        return "source", posixpath.dirname(posixpath.dirname(found[0]))
    except OSError as exc:
        raise Refusal(RECEIPT_REL, 0, f"the install receipt does not read: {exc}") from None
    try:
        receipt = json.loads(text)
    except ValueError as exc:
        raise Refusal(RECEIPT_REL, 0, f"the install receipt does not parse: {exc}") from None
    if not isinstance(receipt, dict):
        raise Refusal(RECEIPT_REL, 0, "the install receipt does not parse as a JSON object")
    kits, prefix = receipt.get("kits"), receipt.get("prefix")
    if not isinstance(kits, list) or not all(isinstance(k, str) for k in kits):
        return "invalid", "kits"
    if not check_receipt_prefix(prefix):
        return "invalid", "prefix"
    return "adopter", receipt


def check_receipt_prefix(value):
    """True where a receipt's `prefix` is a relative string: it opens with neither `/` nor a backslash,
    carries no drive letter and holds no `..` segment split on either separator (TOOL-dGroundRules-43
    S14). Stricter than the deployer's `demand_contained_dest` on purpose (TOOL-dGroundRules-34 S21):
    that one normalises first and admits `a/..`, this one refuses every `..` segment."""
    return (isinstance(value, str) and not value.startswith(("/", "\\")) and not re.match(r"[A-Za-z]:", value)
            and ".." not in re.split(r"[/\\]", value))


def check_legacy_graded(repo, kit):
    """True where `kit`'s legacy list is graded over the tree at `repo`: the list is present and
    `derive_census_tree` answers neither `adopter` nor `invalid` (TOOL-dGroundRules-76). The one rule
    `cmd_lists` and the gate's `arm_legacy_homes` both ask. A Refusal from the derivation is the
    caller's to report."""
    tree, _held = derive_census_tree(repo)
    return tree not in ("adopter", "invalid") and (Path(kit) / LEGACY_LIST).is_file()


LEGACY_HEADER = (
    "# legacy-homes.txt - GENERATED by `python <this kit>/policy.py lists --write`, never edited.\n"
    "# One row per key a legacy policy home holds, `<home> <key> <mark>`, the mark owner-policy or\n"
    "# mechanic. SHRINK-ONLY: `lists --check` reds a row no home yields, a derived row this list lacks,\n"
    "# and a derived row the list at the compare base lacks. A new key goes in the catalogue instead.\n"
)
Row = namedtuple("Row", "home key mark")
GATE_FILE = ".githooks/gate-env.sh"
TOOL_ROOT = "<tool-root>/"
HOUSE_ANCHOR = "house/policy.toml"  # the roles kit's house file, the anchor `resolve_kit_dir` finds it by
HOUSE_HOME = TOOL_ROOT + "roles/" + HOUSE_ANCHOR   # the drained token is the row's home, verbatim
# The gate file's keys as the clause classifies them: an owner policy dConvergedCharter folds, or a
# mechanic that stays. A gate key this table does not name is `unmarked`, never given a default mark.
GATE_ENV_MARKS = {
    "INHERITED_RED": "owner-policy",
    "INHERITED_RED_MAX_AGE": "owner-policy",
    "GATE_DOC_PATHS": "owner-policy",
    "GATE_WSL_PARITY_RUNS": "owner-policy",
    "GATE_POST_MERGE": "owner-policy",
    "GOV_KITROOT": "mechanic",
    "GATE_WSL_MIRROR_DEFAULT": "mechanic",
    "GOV_GATE_CMD": "mechanic",
    "GOV_BRANCH_GATE_CMD": "mechanic",
    "GOV_PYTHON": "mechanic",
    "GATE_SELFTESTS": "mechanic",
}
SHELL_KEY = re.compile(r"^\s*(?:export\s+)?([A-Z][A-Z0-9_]*)=")
DOCUMENTED_KEY = re.compile(r"^#\s+([A-Z][A-Z0-9_]*)=")
POLICY_KEY_READ = re.compile(r'read_policy_key\s+".*?"\s+([A-Z][A-Z0-9_]*)\b')
RETROFIT_KEY = re.compile(r"_(?:CUTOFF|PIN)$")   # a date cutoff or a scalar pin the retrofit converts


# The kit-dir resolver, INLINED byte-identically from the canonical copy named on its marker line and
# gated by the resolve-python self-test: a kit may not import a sibling, so this kit reaches the roles
# kit's house file and the memory-tree kit's `tree_lib` through it, each named in `kit.toml`'s
# `requires` or announced absent (TOOL-dGroundRules-21 S25, S26).
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


def read_text_or_none(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def scan_shell_keys(lines):
    """The keys `KEY=` lines assign, `export` allowed, each once, in order."""
    return list(dict.fromkeys(m[1] for m in map(SHELL_KEY.match, lines) if m))


def scan_gate_readers(repo):
    """The KEY of each `read_policy_key "<expr>" KEY` call in a tracked shell file that spells the gate
    file's path, outside `memory/` and `help/` and not a `*.test.sh`, comment lines skipped."""
    found = (run_git(repo, "grep", "-l", "-z", "-F", "-e", GATE_FILE, "--", "*.sh", ".githooks/*",
                     ":!memory/", ":!help/", ":!*.test.sh") or "").split("\0")
    keys = []
    for rel in filter(None, found):
        for ln in (read_text_or_none(Path(repo, rel)) or "").splitlines():
            if not ln.lstrip().startswith("#"):
                keys += POLICY_KEY_READ.findall(ln)
    return keys


def derive_legacy_homes(repo, notes):
    """-> [Row] for each key the legacy policy homes of the tree at `repo` hold, sorted by home then key.
    Each home is parsed as text, never sourced, and an absent one yields no rows and adds one line
    naming it to `notes`. The kit confs, each tracked root file named `.*.conf`: every key assigned
    but a retrofit conversion, owner-policy. The gate file: the keys it assigns, the keys its header
    documents, and the keys a tracked shell file naming it reads, less those a kit conf row holds,
    each marked from GATE_ENV_MARKS. The house file, found through `resolve_kit_dir` with home `roles`
    and anchor `house/policy.toml` from this kit's own location, never by joining a name to the tool
    root, a miss being an absent home (TOOL-dGroundRules-21 S25): one row per top-level table,
    `[<table>]`, owner-policy."""
    rows = []
    confs = [c for c in (run_git(repo, "ls-files", "-z", "--", ":(glob).*.conf") or "").split("\0") if c]
    if not confs:
        notes.append("no tracked .*.conf at the repository root, so no kit conf yields a row")
    for conf in confs:
        lines = (read_text_or_none(Path(repo, conf)) or "").splitlines()
        rows += [Row(conf, k, "owner-policy") for k in scan_shell_keys(lines) if not RETROFIT_KEY.search(k)]
    text = read_text_or_none(Path(repo, GATE_FILE))
    if text is None:
        notes.append(f"no {GATE_FILE} in this tree, so that home yields no rows")
    else:
        lines = text.splitlines()
        header = lines[:next((i for i, ln in enumerate(lines) if not ln.startswith("#")), len(lines))]
        held = {r.key for r in rows}
        keys = scan_shell_keys(lines) + [m[1] for m in map(DOCUMENTED_KEY.match, header) if m]
        keys += [k for k in scan_gate_readers(repo) if k not in held]
        rows += [Row(GATE_FILE, k, GATE_ENV_MARKS.get(k, "unmarked")) for k in dict.fromkeys(keys)]
    try:
        text = read_text_or_none(resolve_kit_dir("roles", HOUSE_ANCHOR, KIT) / HOUSE_ANCHOR)
    except LookupError:
        text = None
    if text is None:
        notes.append(f"no {HOUSE_HOME} in this install, so that home yields no rows")
    else:
        try:
            doc = tomllib.loads(text)
        except tomllib.TOMLDecodeError as exc:
            raise Refusal(HOUSE_HOME, 0, f"does not parse, so its tables cannot be listed: {exc}") from None
        rows += [Row(HOUSE_HOME, f"[{t}]", "owner-policy") for t, v in doc.items() if isinstance(v, dict)]
    return sorted(set(rows))


def read_base_pairs(repo, kit, base):
    """-> the (home, key) pairs of this kit's legacy list in the commit `base` names, or None where
    that commit holds no list. `base` is the compare base `cmd_lists` resolved, the one comparison
    the summary list reads too, never the working tree, HEAD or the landed tip (TOOL-dGroundRules-21
    S23)."""
    prefix = run_git(kit, "rev-parse", "--show-prefix")
    if prefix is None:
        raise Refusal((Path(kit) / LEGACY_LIST).as_posix(), 0, "the policy kit is in no git repository, so its list has no compare base")
    text = run_git(repo, "show", f"{base}:{prefix.strip()}{LEGACY_LIST}")
    return None if text is None else {tuple(ln.split(" ")[:2]) for ln in parse_list(text)}


def check_legacy_homes(repo, kit, compare):
    """-> (reports, notes, rows, new): the derived rows of the tree at `repo` against the committed
    list, `kit`'s working-tree file, and the list at the compare base `compare` names, the
    (sha or None, why) `resolve_compare_base` answered. A row's identity is its pair (home, key).
    Reported: (1) a committed row the derivation does not yield, full row compared, as a stale list
    where no home yields its pair and the base's list holds it, else as a typed row; (2) a derived row
    whose pair the committed list lacks; (3) a derived row whose pair the base's list lacks, `new`
    holding those, nothing where there is no base or no list at it, which seeds the baseline; (4) a
    row `unmarked`. The catalogue's path in (3) is derived at runtime."""
    notes = []
    rows = derive_legacy_homes(repo, notes)
    derived = {(r.home, r.key): r.mark for r in rows}
    path = Path(kit) / LEGACY_LIST
    committed = parse_list(path.read_text(encoding="utf-8")) if path.is_file() else []
    sha, why = compare
    at_base = None if sha is None else read_base_pairs(repo, kit, sha)
    reports = []
    for ln in committed:
        f = ln.split(" ")
        pair = tuple(f[:2])
        if len(f) == 3 and derived.get(pair) == f[2]:
            continue
        gone = len(f) == 3 and pair not in derived and at_base is not None and pair in at_base
        reports.append(f"stale list at {ln}, re-run lists --write" if gone else f"typed row {ln}")
    held = {tuple(ln.split(" ")[:2]) for ln in committed}
    reports += [f"stale list at {' '.join(r)}, re-run lists --write" for r in rows if (r.home, r.key) not in held]
    new = []
    if sha is None:
        notes.append(f"no base: {why}; only the derivation is compared")
    elif at_base is None:
        notes.append(f"no list at the base {sha[:8]} ({why}), so this one seeds the baseline")
    else:
        grown = [r for r in rows if (r.home, r.key) not in at_base]
        cat = derive_catalogue_rel() if grown else ""
        new = [f"{r.home} {r.key} is a new legacy home and the list is shrink-only; carry it as a key in {cat} instead"
               for r in grown]
    reports += new + [f"{r.key} in {GATE_FILE} has no mark in GATE_ENV_MARKS" for r in rows if r.mark == "unmarked"]
    return reports, notes, rows, new


def write_legacy_homes(repo, kit, compare):
    """Write the derived rows under the header, sorted, unless a derived row is new to the list at the
    compare base: then write nothing. The list shrinks by this verb and grows by none. -> (new, notes, rows)."""
    _reports, notes, rows, new = check_legacy_homes(repo, kit, compare)
    if not new:
        with open(Path(kit) / LEGACY_LIST, "w", encoding="utf-8", newline="\n") as f:
            f.write(LEGACY_HEADER + "".join(" ".join(r) + "\n" for r in rows))
    return new, notes, rows


def render_toml_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, str):
        return json.dumps(v)
    if isinstance(v, list):
        return "[" + ", ".join(render_toml_value(x) for x in v) + "]"
    raise ValueError(f"no TOML spelling for {v!r}")


def render_scaffold(rows):
    """The starter policy file: each literal-defaulted row this kit's build owns, one table per first
    segment, tables sorted, keys in catalogue order."""
    tables = {}
    for r in rows:
        if r.get("owner") == SCAFFOLD_OWNER and "default" in r and not check_derived(r["default"]):
            segs = str(r["name"]).split(".")
            tables.setdefault(segs[0], []).append((".".join(segs[1:]), r["default"]))
    out = SCAFFOLD_HEADER
    for t in sorted(tables):
        out += f"\n[{t}]\n" + "".join(f"{k} = {render_toml_value(v)}\n" for k, v in tables[t])
    return out


USAGE = ("usage: python policy.py lists --check | lists --write | scaffold | get <key> [--rev <rev>] [--explain] [--json]"
         " | check [--rev <rev>] | mirror --write | mirror --check | mirror --print"
         " | settings [--write|--check] [<settings-file>]")


def cmd_get(argv):
    """`get <key> [--rev <rev>] [--explain] [--json]`, run in the repository to read: the value on
    stdout, a string as itself, a number or a boolean in TOML's spelling, a list one member per line;
    under `--json` one JSON object of the Resolution's three fields instead, the form the mirror
    helper reads through its shim. `--explain` adds `policy: <key> · <source> · <reason>` on stderr.
    A Refusal prints its line there, nothing on stdout, exit 2."""
    import argparse
    ap = argparse.ArgumentParser(prog="policy.py get")
    ap.add_argument("key")
    ap.add_argument("--rev")
    ap.add_argument("--explain", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", newline="\n")  # a shell reading the value gets no CR
    try:
        hit = resolve(args.key, ".", args.rev)
        if args.json:
            check_json_value(args.key, hit.value)
    except Refusal as exc:
        print(exc, file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(hit._asdict(), sort_keys=True))
    for v in [] if args.json else hit.value if isinstance(hit.value, list) else [hit.value]:
        print(v if isinstance(v, str) else render_toml_value(v))
    if args.explain:
        print(f"policy: {args.key} · {hit.source} · {hit.reason}", file=sys.stderr)
    return 0


def cmd_check(argv):
    """`check [--rev <rev>]`, run in the repository to check: the policy file in the commit `rev`
    names, `HEAD` by default, the candidate a push lands. Exit 0 printing one line when it is valid,
    absent, or invalid with a last valid revision under `last-valid`; exit 2 printing the Refusal on
    stderr otherwise."""
    import argparse
    ap = argparse.ArgumentParser(prog="policy.py check")
    ap.add_argument("--rev", default="HEAD")
    args = ap.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", newline="\n")
    try:
        print(check_revision(".", args.rev))
    except Refusal as exc:
        print(exc, file=sys.stderr)
        return 2
    return 0


def cmd_mirror(argv):
    """`mirror --write | --check | --print`, run in the repository: each refuses, exit 2, while an
    input the mirror records, the policy file, this kit's catalogue or a LEGACY_INPUTS file, differs in
    the working tree from its blob at HEAD, each absent on both sides being equal (TOOL-dGroundRules-25
    S20), and then renders at HEAD. `--write` writes `.governance/policy.json`
    only when its bytes differ; `--check` compares them, exit 1 naming the first difference; `--print`
    writes the render's bytes to stdout and no file, the form the policy guard compares a staged
    mirror with (TOOL-dGroundRules-19)."""
    if argv not in (["--write"], ["--check"], ["--print"]):
        print(USAGE, file=sys.stderr)
        return 2
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", newline="\n")
    top = (run_git(".", "rev-parse", "--show-toplevel") or "").strip()
    try:
        if not top:
            raise Refusal(MIRROR_REL, 0, "the working directory is in no git repository")
        cat = derive_catalogue_rel()
        for rel in (POLICY_REL, cat, *LEGACY_INPUTS):
            here = (run_git(top, "hash-object", "--", rel) or "").strip()
            if here != (run_git(top, "rev-parse", "--verify", "-q", f"HEAD:{rel}") or "").strip():
                raise Refusal(rel, 0, "uncommitted changes; the mirror renders a revision, commit first")
        want = render_mirror(top, "HEAD")
    except Refusal as exc:
        print(exc, file=sys.stderr)
        return 2
    if argv == ["--print"]:
        sys.stdout.buffer.write(want)  # the bytes, never the text layer's newline translation
        return 0
    path = Path(top, MIRROR_REL)
    have = path.read_bytes() if path.is_file() else None
    if argv == ["--check"]:
        drift = check_mirror_text(want, have)
        if drift:
            print(f"policy: mirror stale · {MIRROR_REL} · {drift} · run: python {cat[:-len(CATALOGUE)]}policy.py mirror --write")
            return 1
    elif have != want:
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(want)
        doc = json.loads(want)
        print(f"policy: mirror written · {len(doc['keys'])} keys · policy {(doc['policy_blob'] or 'absent')[:8]}"
              f" · catalogue {(doc['catalogue_blob'] or 'absent')[:8]}")
        return 0
    print("policy: mirror fresh")
    return 0


def cmd_lists(argv):
    """`lists --check | --write`: both shrink-only lists, the summary list and the legacy-home list,
    against ONE compare base, `resolve_compare_base` read once here for both (TOOL-dGroundRules-21
    S23), so a branch opened before the default branch dropped a key is never read as adding it."""
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", newline="\n")
    top = (run_git(KIT, "rev-parse", "--show-toplevel") or "").strip()
    with run_without_git_env():  # the block is canonical and inherits this process's environment
        compare = resolve_compare_base(KIT)
    # The legacy list is gov's own and withheld from installs (TOOL-dGroundRules-17): both verbs ask
    # the gate arm's rule, so an absent list or an adopter's tree grades and writes nothing.
    reports, notes, rows, new = [], [], [], []
    try:
        if not top:
            raise Refusal(LEGACY_LIST, 0, "the policy kit is in no git repository, so no legacy home can be read")
        held = check_legacy_graded(top, KIT)  # the arm's rule (TOOL-dGroundRules-76)
        if held:
            reports, notes, rows, new = check_legacy_homes(top, KIT, compare)
    except Refusal as exc:
        print(exc, file=sys.stderr)
        return 2
    if argv == ["--check"]:
        findings, note = check_list(KIT, compare)
        print(f"policy lists: {LIST} · {note}")
        for n, why in findings:
            print(f"  {n}: {why}")
        print(f"policy lists: {LEGACY_LIST} · " + (f"{len(rows)} row(s) derived from the legacy homes"
                                                   if held else f"not graded · {LEGACY_WITHHELD}"))
        for ln in notes:
            print(f"legacy homes: {ln}")
        for r in reports:
            print(f"  legacy homes: {r}")
        n = len(findings) + len(reports)
        print(f"policy lists: {'RED' if n else 'green'} · {n} finding(s)")
        return 1 if n else 0
    for ln in notes:
        print(f"legacy homes: {ln}")
    if new:
        for r in new:
            print(f"  legacy homes: {r}")
        print(f"policy lists: wrote nothing · {len(new)} new legacy home(s), and {LEGACY_LIST} is shrink-only")
        return 1
    removed = write_list(KIT)
    print(f"policy lists: wrote {LIST} · drained {len(removed)}: {', '.join(removed) or 'none'}")
    if held:
        write_legacy_homes(top, KIT, compare)
        print(f"policy lists: wrote {LEGACY_LIST} · {len(rows)} row(s)")
    else:
        print(f"policy lists: {LEGACY_LIST} · not written · {LEGACY_WITHHELD}")
    return 0


def main(argv):
    if argv[:1] == ["get"]:
        return cmd_get(argv[1:])
    if argv[:1] == ["check"]:
        return cmd_check(argv[1:])
    if argv[:1] == ["mirror"]:
        return cmd_mirror(argv[1:])
    if argv[:1] == ["settings"]:
        return cmd_settings(argv[1:])
    if argv == ["scaffold"]:
        # The bytes, LF, never the text layer's newline translation: one output on every platform,
        # equal to the blob git stores for a scaffolded file (TOOL-dGroundRules-21 S1).
        sys.stdout.buffer.write(render_scaffold(load_catalogue(KIT)).encode("utf-8"))
        return 0
    if argv[:1] == ["lists"] and argv[1:] in (["--check"], ["--write"]):
        return cmd_lists(argv[1:])
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
