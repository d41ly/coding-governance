#!/usr/bin/env python3
"""settings-merge.py — idempotently wire a hook into a target repo's .claude/settings.json.
Stdlib only (json, argparse, pathlib); py>=3.10 (write_text newline=).

# gov:kit settings-merge@1.16

The default hook, with no --fragment (shape mirrors WIRE-INTO-PROJECT.md and
<prefix>/hooks/agent-cap.js verbatim):

    {"hooks": {"PreToolUse": [
      {"matcher": "Workflow|Agent",
       "hooks": [{"type": "command",
                  "command": "node \\"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\\""}]}]}}

Idempotent by structure: a re-run finds the existing matcher group already carrying the fragment's
marker in a command and makes NO change (apply-twice-changed = 0). Existing keys and any other
groups under that event are preserved; a foreign command inside the matcher group is kept alongside.

A wired target is DETECTED by grepping the fragment's `marker` in .claude/settings.json — JSON
carries no comment marker, so that command substring IS the deployer's "is-it-wired?" signal, and
it is what <prefix>/check-wiring.sh joins each arm on.

Usage:
    python <prefix>/settings-merge.py [SETTINGS_FILE] [--fragment F] [--hook-path P] [--check]
    python <prefix>/settings-merge.py --selftest      (or: --resolve-fragment F)
      SETTINGS_FILE  default .claude/settings.json (resolved from cwd = target repo root)
      --fragment     a JSON file declaring {name, event, matcher, marker, hook_path} plus the
                     optional {interpreter, args}; omitted = the built-in agent-cap PreToolUse
                     fragment (matcher "Workflow|Agent")
      --hook-path    override the fragment's hook_path (the copied hook, repo-relative)
      --check        report drift without writing: exit 1 if a merge WOULD change the file
      --unwire       with --fragment: remove that fragment's entry instead of merging it, from
                     its event+matcher group only (dropping a group it empties); a foreign
                     command is kept and an absent entry is exit 0 (TOOL-aRepatriatedFork-11)
      --resolve-fragment  print the fragment's hook_path with `{kit}`/`{here}` expanded, then
                     exit — the value the merge would write; check-wiring.sh carries the same
                     verb and the hook-destinations gate asserts the two agree
      --resolve-hook P  print P, a repo-relative hook path already expanded, or the target's
                     `adopter-owned` copy of it from `.governance/install.json`; exit 2 on a row
                     it refuses. check-wiring.sh CALLS this rather than reading the receipt itself
    With neither, agent-cap's copy is located by `[kit.agent-cap] prefix` in the target's
    `.governance/deploy.toml` when one is declared, and by this file's own install prefix
    otherwise — an entry may be installed somewhere other than where settings-merge.py sits.
      --selftest     run the in-file assert suite in a tempdir; exit 0 on pass
Exit: 0 wired (already present OR merged this run) · 1 --check found drift · 2 error.

THE FRAGMENT SCHEMA, and which fields vary. Five keys are REQUIRED — `name` (messages only),
`event`, `matcher`, `marker`, `hook_path` — and two are OPTIONAL, `interpreter` (`node` or `bash`,
default `node`) and `args` (a list of tokens, default empty). The entry's shape is otherwise FIXED:
`type: command` and the `${CLAUDE_PROJECT_DIR}` spelling vary for nobody. The two optional keys
exist because the kickoff engine is a bash script that takes a verb (`--card --write`), and the
three fragments shipped before them carry neither, so they render byte-identically to before. Args
render as UNQUOTED argv tokens joined by single spaces — the one shape under which a marker is a
substring of the command in BOTH readers, this file's plain view and check-wiring's
whitespace-stripped one — so the loader admits only a closed character class for them.

Dedup is a substring test on the marker AND the hook's basename (`check_ours`), scoped to the event:
an entry carrying both under the same event is THIS hook wherever it sits — the marker alone
took an adopter's `--write-log` hook for the card writer (F5 of the aReplayedCard closing review). Since TOOL-dRetiredFork-14 one whose whole rendered
command differs is REWRITTEN in place (a stale path OR a changed argument list); since
TOOL-aReplayedCard-2 one sitting in a group whose matcher is not the fragment's is MOVED to the
fragment's group, and the group it left is dropped if that emptied it. Two fragments declaring one
matcher share one group, which is how `merge` has always grouped.
"""
from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
import tempfile
from pathlib import Path, PurePosixPath

# TOOL-aRepatriatedFork-46: a SIBLING kit is reached through the resolver, which reads the install receipt
# first, never by joining its name to this file's own directory.
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
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
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
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

KIT_SETTINGS_MERGE_VERSION = "1.16"  # gov:kit settings-merge@1.16 — engine identity
HOOK_MARKER = "agent-cap.js"  # the loose join: dedup key AND the deployer's "is-it-wired?" grep target
# The kit NAME a hook path carries when no hooks kit resolves in this install. It names the miss and
# exists nowhere, so `main`'s existence refusal fires on it. Spelled once: the selftest reads it too.
NO_HOOKS_KIT = "no-agent-cap-kit-resolved"


def _kit_rel() -> str:
    """Where this kit sits, relative to the target repo root — DERIVED, never spelled.

    `.claude/hooks/` used to be the wired location and it had one property nobody wrote down: it is
    the SAME PATH IN EVERY REPO, so a hook_path naming it was correct for every adopter without
    anyone resolving anything. Moving the wired copy under the kit directory gives that property up,
    and a constant naming gov's own prefix would be wrong in every tree that installs elsewhere.

    This script's docstring already fixes cwd as the target repo root, so the kit's own directory
    relative to cwd IS the prefix. The fallback is the kit-root NAME alone, which is a default and
    not a path — a repo that somehow runs this from outside its own tree gets the conventional
    answer rather than an absolute path baked into a settings file.
    """
    try:
        return Path(__file__).resolve().parent.relative_to(Path.cwd().resolve()).as_posix()
    except (ValueError, OSError):
        return "tools"  # a name-only default when run from outside the tree it writes into; whether it should refuse instead is the settings-merge owner's call (TOOL-aRepatriatedFork-2 section 8 F4)


# A path fragment and nothing else — the character class govkit's own `demand_safe_token` grades
# `prefix` with, plus containment. This value is target-supplied and lands inside a command string
# Claude Code executes, which is the class govkit reproduced twice; a `prefix` carrying a shell
# metacharacter or climbing out of the tree is refused here rather than resolved.
_SAFE_PREFIX = re.compile(r"^[A-Za-z0-9_.~@+-]+(?:/[A-Za-z0-9_.~@+-]+)*$")


def _load_declared_prefix(kit_id: str, root: Path = Path(".")) -> str | None:
    """The install home the TARGET declared for `kit_id`, out of `.governance/deploy.toml`.

    `_kit_rel()` answers "where does THIS FILE live", and that is the right answer for agent-cap
    only while both entries share one install home. A target may give an entry its own:
    `[kit.agent-cap] prefix = ".claude"` puts the hook there while settings-merge.py stays at the
    top-level prefix. Deriving agent-cap's home from this file's then names a path that is not
    there — the merge REFUSES to wire, and `--check` reports DRIFT against a settings.json that was
    correct all along. REPRODUCED on a fixture before this was written, and pinned by selftest 12.

    None whenever the declaration is absent, unreadable or unsafe. Absent is the common case and it
    is not a failure: an adopter who copy-installed the kits by hand per WIRE-INTO-PROJECT.md has no
    deploy.toml, and the derivation above is exactly right for them. `tomllib` is 3.11+, so a 3.10
    interpreter also lands here and keeps the pre-existing behaviour rather than crashing.
    """
    try:
        import tomllib
    except ImportError:
        return None
    try:
        with (root / ".governance" / "deploy.toml").open("rb") as fh:
            deploy = tomllib.load(fh)
    except (OSError, ValueError):
        return None
    if not isinstance(deploy, dict):
        return None
    per = (deploy.get("kit") or {}).get(kit_id) or {}
    pfx = (per.get("prefix") if isinstance(per, dict) else None) or deploy.get("prefix")
    if not isinstance(pfx, str) or not pfx.strip("/"):
        return None
    pfx = pfx.strip("/")
    if not _SAFE_PREFIX.match(pfx) or ".." in pfx.split("/"):
        print(f"settings-merge: ignoring an unsafe prefix for {kit_id} in .governance/deploy.toml: "
              f"{pfx!r} — a prefix becomes a path inside a command Claude Code runs", file=sys.stderr)
        return None
    return pfx


def _resolve_agent_cap_dir() -> Path | None:
    """agent-cap's kit directory in THIS install, through the sibling-kit resolver, or None.

    TOOL-aRepatriatedFork-46: the receipt is read first, so a hooks kit homed under another name is
    found; the probes are this file's own directory and its parent, which is where the kit's NAME
    used to be typed after this file's prefix.
    """
    try:
        return resolve_kit_dir("hooks", "agent-cap.js", Path(__file__).resolve().parent)
    except LookupError:
        return None


def _resolve_agent_cap_hook_path(root: Path = Path(".")) -> str:
    """agent-cap's shipped copy: the resolved kit where it sits in the target, else the declaration.

    ONE composition, in one place, so the arm that stages the break has something to red on. It is
    also the only reader of `_load_declared_prefix`: the `{kit}` fragments need no lookup at all,
    because a fragment ships beside its hook, so resolving `{kit}` against the FRAGMENT's own
    location already follows whatever prefix that kit was installed at.

    TOOL-aRepatriatedFork-46: the sibling-kit resolver answers first, because it reads the install
    receipt, which records where the kit LANDED. A top-level `prefix` answers where kits go by
    default, and a hooks kit homed under another name contradicted it: the declaration named a path
    the receipt had moved. The declaration still answers where the resolver finds no kit inside the
    target, joined to the kit directory's NAME in this install. A kit found nowhere yields a path that
    names the miss and exists nowhere, so the existence refusal in `main` fires on it: the wiring is
    REFUSED, never pointed at a guessed prefix.
    """
    kit = _resolve_agent_cap_dir()
    if kit is not None:
        try:
            return kit.relative_to(Path(root).resolve()).as_posix() + "/agent-cap.js"
        except ValueError:
            pass  # a kit outside the target this merge writes into
    name = kit.name if kit is not None else NO_HOOKS_KIT
    declared = _load_declared_prefix("agent-cap", root)
    if declared:
        return f"{declared}/{name}/agent-cap.js"
    return f"{_kit_rel()}/{name}/agent-cap.js"


# The built-in fragment. Identical to the three values this script hardcoded before --fragment
# existed, so a no-argument run is unchanged in behaviour AND in what it prints.
AGENT_CAP = {
    "name": "agent-cap",
    "event": "PreToolUse",
    # A LIST OF EXACT STRINGS separated by `|`, in ONE group — not a regular expression, and not two
    # fragments. The hook fires for `Workflow`, where it reads the script, and for `Agent`, where a
    # direct spawn used to meet no rule at all. One group means one marker and no dedup question:
    # the merge below finds the existing group by this exact matcher value.
    "matcher": "Workflow|Agent",
    "marker": HOOK_MARKER,
    "hook_path": _resolve_agent_cap_hook_path(),
}
_FRAGMENT_KEYS = tuple(AGENT_CAP)
# The two OPTIONAL keys and their defaults. `interpreter` is a CLOSED pair, refused by name outside
# it: the value is the first word of a command Claude Code runs, so an open set would be a way to
# put an arbitrary program there through a data file. `args` render UNQUOTED, so each token is held
# to a character class that cannot carry whitespace, a quote or a shell metacharacter.
_INTERPRETERS = ("node", "bash")
_DEFAULT_INTERPRETER = "node"
_SAFE_ARG = re.compile(r"^[A-Za-z0-9_.=/:@+-]+$")


def load_fragment(path: Path) -> dict:
    """Read + validate a fragment file. Every required key must be a non-empty string; the two
    optional ones are defaulted when absent and refused when malformed.

    A fragment missing `marker` would leave the dedup test and check-wiring's arm nothing to join
    on, so this refuses rather than defaulting: a silently marker-less fragment re-appends its hook
    on every run and reports UNWIRED forever.
    """
    try:
        frag = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise ValueError(f"cannot read fragment {path}: {e}") from e
    if not isinstance(frag, dict):
        raise ValueError(f"fragment {path} is not a JSON object")
    bad = [k for k in _FRAGMENT_KEYS if not isinstance(frag.get(k), str) or not frag[k].strip()]
    if bad:
        raise ValueError(f"fragment {path} missing/empty: {', '.join(bad)}")
    out = {k: frag[k] for k in _FRAGMENT_KEYS}
    interp = frag.get("interpreter", _DEFAULT_INTERPRETER)
    if interp not in _INTERPRETERS:
        raise ValueError(f"fragment {path} names interpreter {interp!r}; the closed set is "
                         f"{', '.join(_INTERPRETERS)} — it is the first word of a command Claude Code runs")
    args = frag.get("args", [])
    if not isinstance(args, list) or any(not isinstance(a, str) or not _SAFE_ARG.match(a) for a in args):
        raise ValueError(f"fragment {path} args must be a list of tokens matching {_SAFE_ARG.pattern}; "
                         f"they render UNQUOTED into a command Claude Code runs")
    out["interpreter"], out["args"] = interp, args
    return out


def render_command(hook_path: str, interpreter: str = _DEFAULT_INTERPRETER, args=()) -> str:
    # forward slashes on purpose: ${CLAUDE_PROJECT_DIR} + POSIX path is identical on every OS.
    # ARGUMENTS ARE UNQUOTED and single-space joined — the shape the live check-wiring entry has
    # always had, and the one under which a marker is a substring of the command in both readers.
    # `load_fragment` is what makes that safe: every token passed the closed class above.
    return f'{interpreter} "${{CLAUDE_PROJECT_DIR}}/{hook_path}"' + "".join(f" {a}" for a in args)


def resolve_hook_path(hook_path: str, frag_file: str | None = None) -> str:
    """Expand a `{kit}`- or `{here}`-relative hook_path against the fragment's own location.

    A fragment is DATA shipped verbatim, so it cannot name gov's prefix and stay correct for an
    adopter who installs elsewhere. `.claude/hooks/` used to hide that problem by being the same
    path in every repo; naming the kit directory gives that up, so the fragment names the kit
    SYMBOLICALLY and this resolves it. A path with no placeholder is returned untouched, so an
    explicit --hook-path and every older fragment keep working exactly as before.

    `{here}` is the fragment's OWN directory. It exists for a `kind = "flat"` kit: the kickoff engine
    ships to `{prefix}/manifest-check.sh` and its fragments sit beside it, so `{kit}` — two
    directories up — names `skills/` in gov and the parent of the prefix in an adopter, neither of
    which holds the engine. It resolves ONLY against a fragment file: with none there is no "here",
    and an empty derivation refuses rather than guessing a prefix.
    """
    # RESOLVED AGAINST THE FRAGMENT'S OWN LOCATION when one was supplied, and only otherwise
    # against this script's. The two differ whenever a repo installs its kits at more than one
    # prefix -- and the checker's own fixtures do exactly that -- so deriving from settings-merge's
    # directory would write a command naming a kit root the hook does not live under. A fragment
    # sits at <kit>/<dir>/x.fragment.json, so two parents up is its kit prefix, empty at the root.
    if frag_file:
        here = Path(frag_file).resolve().parent
        try:
            here_rel = here.relative_to(Path.cwd().resolve()).as_posix()
        except (ValueError, OSError):
            here_rel = None
        if "{here}" in hook_path:
            if here_rel is None:
                raise ValueError(f"cannot resolve {{here}} for {frag_file}: it is not under {Path.cwd()}, "
                                 f"the target root every path here is relative to")
            hook_path = hook_path.replace("{here}/", (here_rel + "/") if here_rel != "." else "")
        rel = _kit_rel() if here_rel is None else PurePosixPath(here_rel).parent.as_posix()
        if rel == ".":
            rel = ""
        return resolve_owned_hook(hook_path.replace("{kit}/", (rel + "/") if rel else ""))
    if "{here}" in hook_path:
        raise ValueError("a {here} hook_path resolves only against a fragment file, and none was given")
    return hook_path.replace("{kit}", _kit_rel())


# govkit's grade for an `[[own]].path`, carried here because govkit ships to no target: the STRICT
# token class of its `demand_safe_token`, the containment of its `demand_contained_dest` and the
# normpath equality `resolve_owned_rows` demands. `measure_contract_parity` re-grades the receipt's
# copy of that path with the same three before using it, because the receipt is a tracked file anyone
# can edit. This is that rule, not a third one: the class admits no `\`, `"`, `$`, backtick or space.
_OWNED_PATH = re.compile(r"\A[A-Za-z0-9_./~@+-]+\Z")


def resolve_owned_hook(path: str) -> str:
    """TOOL-aRepatriatedFork-36. A hook the target keeps ELSEWHERE, declared rather than guessed.

    A fragment names gov's copy beside its kit. A target running its own copy at another path
    declares it `[[own]]`, which `govkit adopt` records as an `adopter-owned` receipt row carrying
    the SAME `source` as gov's engine row at `path`. Joined on that source exactly; with no receipt,
    no engine row at `path`, or no owned row for its source, `path` comes back unchanged.

    THE ONLY READER OF THAT JOIN, since the round-1 fold. check-wiring.sh carried a second one in
    awk, which never decoded JSON: a compact receipt, a `\\u` escape, a backslash or an embedded quote
    split the two answers, and the parity gate could not see it because gov keeps no receipt. It
    calls `--resolve-hook` now, so the two readers cannot disagree.

    A JOINED ROW IS GRADED, and a row that fails REFUSES (ValueError) rather than falling back: the
    owned path lands inside a command Claude Code runs, so a `$(...)` in it is code, and a silent
    fall-back would wire gov's copy while the operator believes their own runs. Refused too:
    - an owned file whose NAME differs from the hook's, because `check_ours` joins on that name, so
      every merge would append a duplicate that `--unwire` can never remove;
    - an ambiguous join, two sources at `path` or two owned paths for one source, where any pick is
      a guess about which the operator meant.
    """
    try:
        rows = json.loads((Path.cwd() / ".governance" / "install.json").read_text(encoding="utf-8"))
        rows = [f for f in rows.get("files") or [] if isinstance(f, dict)]
    except (OSError, ValueError, AttributeError):
        return path
    srcs = {f.get("source") for f in rows
            if f.get("path") == path and f.get("role") != "adopter-owned" and f.get("source")}
    if len(srcs) > 1:
        raise ValueError(f"the receipt carries {len(srcs)} rows at {path} with different sources, "
                         f"so the adopter-owned join is ambiguous: {sorted(map(str, srcs))}")
    if not srcs:
        return path
    src = srcs.pop()
    owned = sorted({f.get("path") for f in rows
                    if f.get("role") == "adopter-owned" and f.get("source") == src}, key=str)
    if not owned:
        return path
    where = f"the receipt's adopter-owned row for {src}"
    if len(owned) > 1:
        raise ValueError(f"{where} names {len(owned)} paths, so the join is ambiguous: {owned}")
    p = owned[0]
    if not isinstance(p, str) or not _OWNED_PATH.match(p):
        raise ValueError(f"{where} is {p!r}, outside the class govkit grades an [[own]] path with "
                         f"({_OWNED_PATH.pattern}); it would land inside a command Claude Code runs")
    norm = posixpath.normpath(p)
    if p != norm or norm == ".." or norm.startswith("../") or posixpath.isabs(norm):
        raise ValueError(f"{where} is {p!r}, which is not a canonical path inside the repository")
    if PurePosixPath(p).name != PurePosixPath(path).name:
        raise ValueError(f"{where} is {p!r}, whose file name is not the hook's "
                         f"{PurePosixPath(path).name!r}; the merge joins on that name, so every run "
                         f"would append a second entry and --unwire could remove none")
    return p


def check_ours(command, marker: str, hook_path: str) -> bool:
    """THE ONE JOIN: a command is this fragment's hook when it carries the marker AND the hook's
    basename. The marker alone was the join, and two shipped markers are bare flags (`--write`,
    `--replay`): an adopter's own SessionStart hook carrying `--write-log` was moved, overwritten
    and reported as the wired card writer, silently (the aReplayedCard closing review, F5).
    `check-wiring.sh`'s `matchers_of` joins on the same pair."""
    text = command if isinstance(command, str) else ""
    return marker in text and PurePosixPath(hook_path).name in text


def set_group(pre: list, matcher: str, marker: str, hook_path: str) -> None:
    """Move the entry carrying `marker` (and the hook's basename — `check_ours`) OUT of every group
    under this event whose matcher is not `matcher`, dropping any group that emptied. The caller
    then lands the fragment's entry in the group holding its matcher, so the hook fires on exactly
    the events the fragment declares.

    The re-match is scoped to marker AND event — `pre` is one event's group list — so a basename
    marker shared across events (`procmon-hook.js` on PostToolUse and on SessionStart) never moves
    the other event's entry. A matcher-less group counts as "differs": that is the shape the two
    SessionStart entries had before TOOL-aReplayedCard-2, and it is the migration this exists for.
    A foreign command in the same group stays where it is, and a group that was empty before this
    ran is left alone — only a group THIS move emptied is dropped.
    """
    kept: list = []
    for g in pre:
        if isinstance(g, dict) and g.get("matcher") != matcher and isinstance(g.get("hooks"), list):
            before = g["hooks"]
            g["hooks"] = [h for h in before
                          if not (isinstance(h, dict) and check_ours(h.get("command", ""), marker, hook_path))]
            if before and not g["hooks"]:
                continue
        kept.append(g)
    pre[:] = kept


def merge(obj: dict, hook_path: str, frag: dict = AGENT_CAP, frag_file: str | None = None) -> dict:
    """Ensure the fragment's hook is present in obj (mutates + returns obj)."""
    hook_path = resolve_hook_path(hook_path, frag_file)
    event, matcher, marker = frag["event"], frag["matcher"], frag["marker"]
    hooks = obj.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        raise ValueError("settings 'hooks' is not an object")
    pre = hooks.setdefault(event, [])
    if not isinstance(pre, list):
        raise ValueError(f"settings 'hooks.{event}' is not an array")
    entry = {"type": "command",
             "command": render_command(hook_path, frag.get("interpreter", _DEFAULT_INTERPRETER),
                                       frag.get("args", ()))}
    set_group(pre, matcher, marker, hook_path)
    group = next((g for g in pre if isinstance(g, dict) and g.get("matcher") == matcher), None)
    if group is None:
        pre.append({"matcher": matcher, "hooks": [entry]})
        return obj
    inner = group.setdefault("hooks", [])
    if not isinstance(inner, list):
        raise ValueError(f"settings {matcher} group 'hooks' is not an array")
    # THE MARKER SAYS "this is our hook"; THE COMMAND SAYS "and it is the right one". Those are
    # two questions and this used to ask only the first, so an already-wired tree was a no-op even
    # when its command named a path the kit no longer ships. That is not a cosmetic gap: it is how a
    # tree keeps a command pointing at a withdrawn file and loses the hook silently.
    #
    # The compare is FRAGMENT-LEVEL, per TOOL-dRetiredFork-14 F0: the fragment supplies hook_path, so
    # a fragment gov owns repaths on the same run as the built-in default, and an adopter who cannot
    # edit that fragment without forking gets the fix for free. The rejected alternative was a
    # `--rewrite-stale-path` flag, which puts the decision on whoever remembers to pass it.
    # It compares the WHOLE rendered command, not the path inside it: a changed argument list is
    # the same drift as a moved file — the hook runs, and does the wrong verb.
    want = entry["command"]
    for h in inner:
        if not isinstance(h, dict) or not check_ours(h.get("command", ""), marker, hook_path):
            continue
        if str(h.get("command", "")) != want:
            h["command"] = want   # REWRITE in place: same hook, right command
        return obj                # found either way -- never append a second entry
    inner.append(entry)
    return obj


def remove_entry(obj: dict, hook_path: str, frag: dict, frag_file: str | None = None) -> dict:
    """`--unwire` (TOOL-aRepatriatedFork-11 S4): the inverse of `merge` for ONE fragment. From the
    group under the fragment's event AND matcher, drop the entry `check_ours` calls this hook, and
    the group too if that emptied it. A foreign command beside it is kept, and nothing under any
    other matcher is read. Absent is not an error: govkit calls this on a rollback, where the entry
    may never have been written."""
    hook_path = resolve_hook_path(hook_path, frag_file)
    pre = obj.get("hooks", {}).get(frag["event"]) if isinstance(obj.get("hooks"), dict) else None
    if not isinstance(pre, list):
        return obj
    kept: list = []
    for g in pre:
        if isinstance(g, dict) and g.get("matcher") == frag["matcher"] and isinstance(g.get("hooks"), list):
            before = g["hooks"]
            g["hooks"] = [h for h in before
                          if not (isinstance(h, dict) and check_ours(h.get("command", ""), frag["marker"], hook_path))]
            if before and not g["hooks"]:
                continue
        kept.append(g)
    pre[:] = kept
    return obj


def _load(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:  # ValueError covers json.JSONDecodeError
        raise ValueError(f"cannot read {path}: {e}") from e
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a JSON object")
    return data


def _dump(obj: dict) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def run(settings_file: str, hook_path: str, check: bool, frag: dict = AGENT_CAP,
        frag_file: str | None = None, unwire: bool = False) -> int:
    path = Path(settings_file)
    existed = path.exists()
    what = f"{frag['name']} {frag['matcher']} hook"
    try:
        before = _dump(_load(path))
        after = _dump((remove_entry if unwire else merge)(json.loads(before), hook_path, frag, frag_file))
    except ValueError as e:
        print(f"settings-merge: {e}", file=sys.stderr)
        return 2
    if before == after:
        print(f"settings-merge: {what} " + ("not wired" if unwire else "already wired") + f" in {settings_file}")
        return 0
    if unwire:
        try:
            path.write_text(after, encoding="utf-8", newline="\n")
        except OSError as e:
            print(f"settings-merge: write failed: {e}", file=sys.stderr)
            return 2
        print(f"settings-merge: unwired {what} from {settings_file}")
        return 0
    if check:
        print(f"settings-merge: DRIFT — {settings_file} is missing the {what}", file=sys.stderr)
        return 1
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        if existed:
            Path(str(path) + ".bak").write_bytes(path.read_bytes())  # byte-faithful, not the normalized parse
        path.write_text(after, encoding="utf-8", newline="\n")
    except OSError as e:
        print(f"settings-merge: write failed: {e}", file=sys.stderr)
        return 2
    print(f"settings-merge: wired {what} into {settings_file}"
          + (f" (backed up to {settings_file}.bak)" if existed else " (created)"))
    return 0


def _selftest() -> int:
    here = Path(__file__).resolve().parent

    def resolve_sibling(home: str, name: str) -> Path | None:
        """A SIBLING kit's file through the resolver (TOOL-aRepatriatedFork-46), or None where it is absent."""
        try:
            return resolve_kit_dir(home, name, here) / name
        except LookupError:
            return None

    hp = ".claude/hooks/agent-cap.js"
    cmd = render_command(hp)
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)

        # 1) absent file -> creates the Workflow|Agent group + agent-cap command, exit 0
        sf = root / ".claude" / "settings.json"
        assert run(str(sf), hp, check=False) == 0
        wf = [g for g in json.loads(sf.read_text(encoding="utf-8"))["hooks"]["PreToolUse"]
              if g.get("matcher") == AGENT_CAP["matcher"]]
        assert len(wf) == 1 and any(h["command"] == cmd for h in wf[0]["hooks"])
        assert "\r" not in sf.read_text(encoding="utf-8")  # LF-only on every OS

        # 2) re-run -> byte-identical (no change); --check on a wired file -> 0
        first = sf.read_text(encoding="utf-8")
        assert run(str(sf), hp, check=False) == 0 and sf.read_text(encoding="utf-8") == first
        assert run(str(sf), hp, check=True) == 0

        # 3) pre-existing unrelated key is preserved through the merge
        sf2 = root / "s2.json"
        sf2.write_text('{"model": "x"}\n', encoding="utf-8")
        assert run(str(sf2), hp, check=False) == 0
        o2 = json.loads(sf2.read_text(encoding="utf-8"))
        assert o2["model"] == "x" and o2["hooks"]["PreToolUse"][0]["matcher"] == "Workflow|Agent"

        # 4) pre-existing group w/ a FOREIGN command -> agent-cap appended, foreign kept, ONE group
        sf3 = root / "s3.json"
        sf3.write_text(json.dumps({"hooks": {"PreToolUse": [
            {"matcher": AGENT_CAP["matcher"],
             "hooks": [{"type": "command", "command": "node other.js"}]}]}}) + "\n", encoding="utf-8")
        assert run(str(sf3), hp, check=False) == 0
        wf3 = [g for g in json.loads(sf3.read_text(encoding="utf-8"))["hooks"]["PreToolUse"]
               if g.get("matcher") == AGENT_CAP["matcher"]]
        cmds = [h["command"] for h in wf3[0]["hooks"]]
        assert len(wf3) == 1 and "node other.js" in cmds and cmd in cmds

        # 5) malformed JSON -> exit 2
        sf4 = root / "s4.json"
        sf4.write_text("{ not json", encoding="utf-8")
        assert run(str(sf4), hp, check=False) == 2

        # 6) --check on an absent file -> drift (1), and nothing written
        sf5 = root / "sub" / "s5.json"
        assert run(str(sf5), hp, check=True) == 1 and not sf5.exists()

        # 6b) --unwire (TOOL-aRepatriatedFork-11 S4): wired by merge beside a FOREIGN command, then
        # removed -> the foreign command stays, the entry is gone, --check reports drift again; a
        # second --unwire is a no-op exit 0; unwiring the only entry drops the group it emptied.
        sfu = root / "su.json"
        sfu.write_text(sf3.read_text(encoding="utf-8"), encoding="utf-8")
        assert run(str(sfu), hp, check=False, unwire=True) == 0
        gu = json.loads(sfu.read_text(encoding="utf-8"))["hooks"]["PreToolUse"]
        assert [h["command"] for h in gu[0]["hooks"]] == ["node other.js"], gu
        assert run(str(sfu), hp, check=True) == 1
        assert run(str(sfu), hp, check=False, unwire=True) == 0
        sfu2 = root / "su2.json"
        assert run(str(sfu2), hp, check=False) == 0 and run(str(sfu2), hp, check=False, unwire=True) == 0
        assert json.loads(sfu2.read_text(encoding="utf-8"))["hooks"]["PreToolUse"] == []

        # --- --fragment: a SECOND hook, on a different event and matcher -----------------------
        recall = {"name": "recall-opened", "event": "PostToolUse", "matcher": "Read",
                  "marker": "recall-opened.js",
                  "hook_path": "{kit}/memory-recall/recall-opened.js"}
        # The PIN is the shipped text, tokens and all -- that is what drift would change. The path
        # used below is the RESOLVED one, because a fixture needs a real directory.
        rhp = resolve_hook_path(recall["hook_path"])

        # 7) a fragment adds ITS block and leaves the agent-cap one alone; re-run is byte-identical
        sf6 = root / "s6.json"
        assert run(str(sf6), hp, check=False) == 0                 # agent-cap first
        cap_only = sf6.read_text(encoding="utf-8")
        assert run(str(sf6), rhp, check=False, frag=recall) == 0
        both = json.loads(sf6.read_text(encoding="utf-8"))["hooks"]
        # PINNED AS A LITERAL, never as AGENT_CAP["matcher"]. This is the arm that has to fail when
        # the shipped matcher narrows back to `Workflow`; asserting it against the constant it is
        # checking would make it agree with any value the constant happens to hold.
        assert [g["matcher"] for g in both["PreToolUse"]] == ["Workflow|Agent"]
        assert [g["matcher"] for g in both["PostToolUse"]] == ["Read"]
        assert recall["marker"] in both["PostToolUse"][0]["hooks"][0]["command"]
        assert cap_only != sf6.read_text(encoding="utf-8")          # it really did change something
        wired = sf6.read_text(encoding="utf-8")
        assert run(str(sf6), rhp, check=False, frag=recall) == 0
        assert sf6.read_text(encoding="utf-8") == wired             # AC10: re-run changes nothing
        assert run(str(sf6), rhp, check=True, frag=recall) == 0
        assert run(str(sf6), hp, check=True) == 0                   # ...and agent-cap still reads wired

        # 8) the fragment's OWN drift is detected independently of agent-cap's
        sf7 = root / "s7.json"
        assert run(str(sf7), hp, check=False) == 0
        assert run(str(sf7), rhp, check=True, frag=recall) == 1

        # 9) a fragment with no marker is REFUSED, not defaulted — a marker-less fragment
        #    re-appends its hook every run and reports UNWIRED forever.
        #    The two OPTIONAL keys are refused when malformed, never defaulted over: an interpreter
        #    outside the pair is a program name in a command Claude Code runs, and an arg outside
        #    the closed class would render unquoted into that same command.
        whole = {"name": "x", "event": "E", "matcher": "M", "marker": "m", "hook_path": "h"}
        for broken in ({"name": "x", "event": "E", "matcher": "M", "hook_path": "h"},
                       {"name": "x", "event": "E", "matcher": "M", "marker": " ", "hook_path": "h"},
                       dict(whole, interpreter="perl"), dict(whole, interpreter=""),
                       dict(whole, args="--x"), dict(whole, args=["a b"]), dict(whole, args=["x;id"]),
                       dict(whole, args=['--x"']), dict(whole, args=[1]),
                       ["not", "an", "object"]):
            bf = root / "frag.json"
            bf.write_text(json.dumps(broken), encoding="utf-8")
            try:
                load_fragment(bf)
                raise AssertionError(f"accepted a bad fragment: {broken}")
            except ValueError:
                pass
        assert main([str(root / "s8.json"), "--fragment", str(root / "nope.json")]) == 2

        # 11) the MERGE is refused when the hook script it would dispatch does not exist. The
        #     wired-but-script-missing state is reachable from two separate WIRE commands run out of
        #     order, and it makes Claude Code run `node` against nothing on every matching call.
        sf9, gone, there = root / "s9.json", root / "gone.js", root / "here.js"
        assert main([str(sf9), "--hook-path", str(gone)]) == 2 and not sf9.exists()
        assert main([str(sf9), "--hook-path", str(gone), "--check"]) == 1, "--check is a report, not a merge"
        there.write_text("// stub\n", encoding="utf-8")
        assert main([str(sf9), "--hook-path", str(there)]) == 0 and sf9.exists()

        # 12) a PER-ENTRY `prefix` in the target's deploy.toml decides agent-cap's home, and this
        #     file's own location does not. Staged as the reported break: settings-merge at the
        #     top-level prefix, the hook at its own. Before the fix the composition below read
        #     the top-level prefix joined to the hook's own path, and the merge refused a settings.json that was correct.
        gov = root / "dep" / ".governance"
        gov.mkdir(parents=True)
        dep = gov / "deploy.toml"
        dep.write_text('prefix = "scripts"\n\n[kit.agent-cap]\nprefix = ".claude"\n',
                       encoding="utf-8", newline="\n")
        # THE COMPOSITION, not just the reader: reverting the lookup has to red something. This
        # assertion is what fails on the pre-fix engine, which answered "<this file's prefix>/hooks/
        # agent-cap.js" and then refused to wire a tree whose settings.json was already right.
        # The hooks kit's directory NAME in this install, or the miss name where no hooks kit sits
        # beside this file: the entry declares `requires = []`, so a settings-merge-only install is
        # legal, and `.name` on the None the resolver returns there crashed this arm (closing
        # review round 1 M4). The composition asserted below is the same either way.
        _hk_dir = _resolve_agent_cap_dir()
        _hk = _hk_dir.name if _hk_dir is not None else NO_HOOKS_KIT
        assert _resolve_agent_cap_hook_path(gov.parent) == f".claude/{_hk}/agent-cap.js"
        assert _resolve_agent_cap_hook_path(root).endswith(f"/{_hk}/agent-cap.js")     # no deploy.toml -> derived
        assert _load_declared_prefix("agent-cap", gov.parent) == ".claude"
        assert _load_declared_prefix("settings-merge", gov.parent) == "scripts"   # falls back to top-level
        assert _load_declared_prefix("agent-cap", root) is None                   # no deploy.toml at all
        # An unsafe value is REFUSED, not resolved into a command Claude Code runs. Every one of
        # these is VALID TOML on purpose: a value that merely breaks the parse would be rejected by
        # tomllib and the character class would go unexercised.
        for evil in ('../../PWNED', 'x; touch PWNED', 'x$(id)', 'C:/abs'):
            dep.write_text(f'[kit.agent-cap]\nprefix = "{evil}"\n', encoding="utf-8", newline="\n")
            assert _load_declared_prefix("agent-cap", gov.parent) is None, evil

        # 10) the SHIPPED fragment beside this script parses and declares the schema check-wiring
        #     joins on. Skipped, not failed, in a project that did not adopt memory-recall.
        shipped = resolve_sibling("memory-recall", "recall-opened.fragment.json")
        if shipped is not None and shipped.is_file():
            got = load_fragment(shipped)
            # The shipped hook_path is `{here}`-relative (TOOL-aRepatriatedFork-2 S4), so a renamed
            # kit dir resolves; the fixture above keeps `{kit}` because it has no fragment file.
            pinned = dict(recall, hook_path="{here}/recall-opened.js")
            assert {k: got[k] for k in _FRAGMENT_KEYS} == pinned, \
                f"shipped fragment drifted from the pinned schema: {got}"
            # A fragment carrying neither optional key is DEFAULTED, and the defaults are the
            # pre-1.4 render: this is what keeps the three older fragments byte-identical.
            assert (got["interpreter"], got["args"]) == ("node", [])

        # --- TOOL-aReplayedCard-2: interpreter + args, {here}, the whole-command rewrite, the
        #     re-match. The four fragments are located the way the arms locate them — beside this
        #     script in an adopter, at the kit's home in gov — and an arm whose subject is absent
        #     SAYS so rather than passing over nothing.
        def resolve_shipped(*cands: Path) -> Path | None:
            return next((c for c in cands if c.is_file()), None)

        card = resolve_shipped(here / "orientation-card.fragment.json",
                          here.parent / "skills" / "session-kickoff" / "orientation-card.fragment.json")
        replay = resolve_shipped(here / "orientation-replay.fragment.json",
                            here.parent / "skills" / "session-kickoff" / "orientation-replay.fragment.json")
        cw = resolve_shipped(here / "check-wiring.fragment.json")
        pm = resolve_sibling("process-monitor", "procmon-session.fragment.json")

        # 13) the render: a bash fragment with arguments lands as UNQUOTED tokens after the quoted
        #     path, `{here}` resolves to the fragment's own directory, and the token never survives.
        assert render_command("k/x.sh", "bash", ["--card", "--write"]) == \
            'bash "${CLAUDE_PROJECT_DIR}/k/x.sh" --card --write'
        assert render_command("k/x.js") == 'node "${CLAUDE_PROJECT_DIR}/k/x.js"'
        try:
            resolve_hook_path("{here}/x.sh")
            raise AssertionError("{here} resolved with no fragment file to resolve it against")
        except ValueError:
            pass
        # 13b) TOOL-aRepatriatedFork-36: an `adopter-owned` receipt row carrying the source of gov's
        #      engine row at the resolved path moves the hook to the target's own copy; the owned
        #      row alone, with no engine row at that path, joins to nothing.
        _cwd13 = Path.cwd()
        try:
            __import__("os").chdir(root)
            (root / ".governance").mkdir()
            (root / "k").mkdir()
            frag13 = root / "k" / "f.fragment.json"
            frag13.write_text("{}\n", encoding="utf-8")
            rows13 = [{"path": "k/h.js", "role": "engine", "source": "g/k/h.js"},
                      {"path": ".claude/hooks/h.js", "role": "adopter-owned", "source": "g/k/h.js"}]
            rcpt13 = root / ".governance" / "install.json"
            rcpt13.write_text(json.dumps({"files": rows13}) + "\n", encoding="utf-8")
            got13 = resolve_hook_path("{here}/h.js", str(frag13))
            assert got13 == ".claude/hooks/h.js", got13
            rcpt13.write_text(json.dumps({"files": rows13[1:]}) + "\n", encoding="utf-8")
            got13 = resolve_hook_path("{here}/h.js", str(frag13))
            assert got13 == "k/h.js", got13
            # 13c) the round-1 fold: every receipt spelling the retired awk reader split from this
            #      one, as RAW TEXT so the escapes reach the parser undecoded. A decoded path that
            #      passes govkit's [[own]] grade resolves; every other owned row REFUSES, and so does
            #      an ambiguous join or an owned file named differently from the hook (S4).
            eng = '{"path": "k/h.js", "role": "engine", "source": "g/k/h.js"}'
            def build_owned_row(p: str, role: str = "adopter-owned") -> str:
                return '{"path": "%s", "role": "%s", "source": "g/k/h.js"}' % (p, role)
            accepted = {
                "compact one-line JSON": '{"files":[%s,%s]}' % (eng, build_owned_row(".claude/hooks/h.js")),
                "a \\u escape in the role": '{"files": [%s, %s]}' % (eng, build_owned_row(".claude/hooks/h.js", "\\u0061dopter-owned")),
                "a duplicated identical owned row": '{"files": [%s, %s, %s]}' % (eng, build_owned_row(".claude/hooks/h.js"), build_owned_row(".claude/hooks/h.js")),
            }
            refused = {
                "backslashes": build_owned_row("..\\\\..\\\\other\\\\h.js"),
                "a \\u escape to a non-ASCII name": build_owned_row(".claude/caf\\u00e9/h.js"),
                "an embedded quote": build_owned_row('.claude/h\\"x/h.js'),
                "a climbing path": build_owned_row("../other/h.js"),
                "a non-canonical path": build_owned_row(".claude/../hooks/h.js"),
                "an absolute path": build_owned_row("/abs/h.js"),
                "a drive letter": build_owned_row("C:/abs/h.js"),
                "a command substitution": build_owned_row("h/$(touch PWNED)/h.js"),
                "an owned file named differently from the hook": build_owned_row(".claude/hooks/my-h.js"),
            }
            for why, text in accepted.items():
                rcpt13.write_text(text + "\n", encoding="utf-8")
                assert resolve_hook_path("{here}/h.js", str(frag13)) == ".claude/hooks/h.js", why
            for why, row in refused.items():
                rcpt13.write_text('{"files": [%s, %s]}\n' % (eng, row), encoding="utf-8")
                try:
                    got13 = resolve_hook_path("{here}/h.js", str(frag13))
                    raise AssertionError(f"{why}: resolved to {got13!r} instead of refusing")
                except ValueError:
                    pass
            rcpt13.write_text('{"files": [%s, %s, %s]}\n' % (eng, build_owned_row(".claude/hooks/h.js"),
                                                              build_owned_row("x/h.js")), encoding="utf-8")
            try:
                resolve_hook_path("{here}/h.js", str(frag13))
                raise AssertionError("two owned paths for one source resolved instead of refusing")
            except ValueError:
                pass
            # ...and the refusal reaches the MERGE: S4's owned row used to append one duplicate
            # entry per run; now the run exits 2 and writes nothing.
            # Both files EXIST, so the refusal is the only reason the merge can exit 2 here.
            (root / "mine").mkdir()
            (root / "mine" / "my-h.js").write_text("//\n", encoding="utf-8")
            (root / "k" / "h.js").write_text("//\n", encoding="utf-8")
            frag13.write_text(json.dumps({"name": "h", "event": "PostToolUse", "matcher": "Read",
                                          "marker": "h.js", "hook_path": "{here}/h.js"}) + "\n",
                              encoding="utf-8")
            rcpt13.write_text('{"files": [%s, %s]}\n' % (eng, build_owned_row("mine/my-h.js")), encoding="utf-8")
            sf13c = root / "s13c.json"
            assert main([str(sf13c), "--fragment", str(frag13)]) == 2 and not sf13c.exists()
            assert main(["--resolve-hook", "k/h.js"]) == 2
        finally:
            __import__("os").chdir(_cwd13)
        if card and replay:
            sf13 = root / "s13.json"
            for fr in (card, replay):
                assert main([str(sf13), "--fragment", str(fr)]) == 0, fr
            text13 = sf13.read_text(encoding="utf-8")
            assert "{here}" not in text13
            eng = resolve_hook_path("{here}/manifest-check.sh", str(card))
            ss = {g["matcher"]: [h["command"] for h in g["hooks"]]
                  for g in json.loads(text13)["hooks"]["SessionStart"]}
            # PINNED AS LITERALS, never read back from the fragments: these are the arms that must
            # fail when a shipped matcher narrows or an argument is dropped or quoted.
            assert ss == {"startup|clear": [f'bash "${{CLAUDE_PROJECT_DIR}}/{eng}" --card --write'],
                          "resume|compact": [f'bash "${{CLAUDE_PROJECT_DIR}}/{eng}" --card --replay']}, ss
            # 14) a stale entry — wrong path AND a different argument list, same marker — is
            #     rewritten whole in one run; the old spelling survives nowhere.
            sf14 = root / "s14.json"
            stale = f'bash "${{CLAUDE_PROJECT_DIR}}/old/manifest-check.sh" --write --card --stale'
            sf14.write_text(json.dumps({"hooks": {"SessionStart": [
                {"matcher": "startup|clear", "hooks": [{"type": "command", "command": stale}]}]}}) + "\n",
                encoding="utf-8")
            assert main([str(sf14), "--fragment", str(card)]) == 0
            ss14 = json.loads(sf14.read_text(encoding="utf-8"))["hooks"]["SessionStart"]
            assert [h["command"] for g in ss14 for h in g["hooks"]] == \
                [f'bash "${{CLAUDE_PROJECT_DIR}}/{eng}" --card --write'], ss14
            # 14c) F5 — a FOREIGN SessionStart hook whose command carries the bare marker as a
            #      substring (`--write-log`) but not the writer's basename survives the card merge
            #      byte-identical and in its own group; the card lands beside it under its matcher.
            sf14c = root / "s14c.json"
            foreign = 'node "${CLAUDE_PROJECT_DIR}/vendor/mine.js" --write-log'
            sf14c.write_text(json.dumps({"hooks": {"SessionStart": [
                {"matcher": "startup", "hooks": [{"type": "command", "command": foreign}]}]}}) + "\n",
                encoding="utf-8")
            assert main([str(sf14c), "--fragment", str(card)]) == 0
            ss14c = json.loads(sf14c.read_text(encoding="utf-8"))["hooks"]["SessionStart"]
            assert [(g["matcher"], [h["command"] for h in g["hooks"]]) for g in ss14c] == \
                [("startup", [foreign]),
                 ("startup|clear", [f'bash "${{CLAUDE_PROJECT_DIR}}/{eng}" --card --write'])], ss14c
        else:
            print("settings-merge selftest: SKIP arms 13-14 (card fragments) — the kickoff kit is not installed beside this script")

        # 14b) the three fragments shipped BEFORE the optional keys render byte-identically to the
        #      pre-1.4 shape: the command is the interpreter default, the path, and nothing after.
        for older in (resolve_sibling("hooks", "scratch-guard.fragment.json"),
                      resolve_sibling("process-monitor", "procmon-hook.fragment.json"), shipped):
            if older is not None and older.is_file():
                fr = load_fragment(older)
                rp = resolve_hook_path(fr["hook_path"], str(older))
                assert render_command(rp, fr["interpreter"], fr["args"]) == f'node "${{CLAUDE_PROJECT_DIR}}/{rp}"', older

        # 15) the RE-MATCH over the four fragments, in file order, in reverse, in file order again:
        #     three SessionStart groups every time, the shared matcher holding the two re-matched
        #     entries, the entry SET of each group equal across the orders, no group empty.
        four = [card, replay, cw, pm]
        if all(four):
            def run_order(order: list, tag: str) -> dict:
                sf = root / f"s15-{tag}.json"
                for fr in order:
                    assert main([str(sf), "--fragment", str(fr)]) == 0, fr
                ss = json.loads(sf.read_text(encoding="utf-8"))["hooks"]["SessionStart"]
                assert all(g.get("hooks") for g in ss), f"an empty group survived: {ss}"
                assert len(ss) == 3, ss
                return {g["matcher"]: frozenset(h["command"] for h in g["hooks"]) for g in ss}
            o1, o2, o3 = run_order(four, "a"), run_order(four[::-1], "b"), run_order(four, "c")
            assert o1 == o2 == o3, (o1, o2, o3)
            assert set(o1) == {"startup|clear", "resume|compact", "startup|resume|clear"}, set(o1)
            assert len(o1["startup|resume|clear"]) == 2 and len(o1["startup|clear"]) == 1 \
                and len(o1["resume|compact"]) == 1, o1
            # 16) a MATCHER-LESS group holding the check-wiring entry — the shape every tree had
            #     before this — is emptied by the re-match, dropped, and the entry sits under the
            #     fragment's matcher with nothing appended beside it.
            sf16 = root / "s16.json"
            cwp = resolve_hook_path("{here}/check-wiring.sh", str(cw))
            sf16.write_text(json.dumps({"hooks": {"SessionStart": [
                {"hooks": [{"type": "command", "command": render_command(cwp, "bash", ["--session"])}]}]}}) + "\n",
                encoding="utf-8")
            assert main([str(sf16), "--fragment", str(cw)]) == 0
            ss16 = json.loads(sf16.read_text(encoding="utf-8"))["hooks"]["SessionStart"]
            assert [g.get("matcher") for g in ss16] == ["startup|resume|clear"], ss16
            assert [h["command"] for h in ss16[0]["hooks"]] == [render_command(cwp, "bash", ["--session"])], ss16
            # ...and a group the move did NOT empty keeps its foreign command where it was.
            sf16b = root / "s16b.json"
            sf16b.write_text(json.dumps({"hooks": {"SessionStart": [
                {"matcher": "startup", "hooks": [{"type": "command", "command": "node other.js"},
                                                 {"type": "command", "command": render_command(cwp, "bash", ["--session"])}]}]}}) + "\n",
                encoding="utf-8")
            assert main([str(sf16b), "--fragment", str(cw)]) == 0
            ss16b = json.loads(sf16b.read_text(encoding="utf-8"))["hooks"]["SessionStart"]
            assert [(g["matcher"], [h["command"] for h in g["hooks"]]) for g in ss16b] == \
                [("startup", ["node other.js"]),
                 ("startup|resume|clear", [render_command(cwp, "bash", ["--session"])])], ss16b
        else:
            print("settings-merge selftest: SKIP arms 15-16 (the four SessionStart fragments) — "
                  + ", ".join(n for n, f in zip(("card", "replay", "check-wiring", "procmon-session"), four) if not f)
                  + " not installed beside this script")

        # 17) EVERY tracked fragment, applied and read back through check-wiring's OWN `matchers_of`
        #     — the function's real bytes, lifted from the checker beside this script and run under
        #     bash with its settings resolver stubbed to the scratch file — must return the
        #     fragment's matcher. This is the arm that reds when a marker is dash-leading and the
        #     checker's grep reads it as an option, or when a marker is not a substring under the
        #     checker's whitespace-stripped view.
        import os
        import subprocess

        def resolve_bash() -> str | None:
            """The bash that shares THIS filesystem, never the bare NAME: on Windows the loader
            resolves `bash` to System32's WSL launcher first, which sees /mnt/c and its own
            interpreters (`memory/gotchas/subprocess-resolves-a-different-shell.md`). A candidate
            counts only if it RUNS; govkit and corpus_ids carry the same rule, inlined here
            because this file ships alone."""
            for d in os.environ.get("PATH", "").split(os.pathsep):
                for name in ("bash.exe", "bash"):
                    cand = os.path.join(d, name)
                    low = cand.replace("\\", "/").lower()
                    if not os.path.isfile(cand) or "/system32/" in low or "/windowsapps/" in low:
                        continue
                    try:
                        if subprocess.run([cand, "-c", ":"], capture_output=True).returncode == 0:
                            return cand
                    except OSError:
                        pass
            return None

        bash = resolve_bash()
        cwsh = here / "check-wiring.sh"
        try:
            # `encoding="utf-8"` EXPLICITLY, never bare `text=True`: the machine locale is cp125x
            # on the Windows nodes and UTF-8 in CI, so an unencoded decode fails on one and not the
            # other. An adopter's encoding-posture gate is what caught both of these.
            frags = subprocess.run(["git", "ls-files", "*.fragment.json"], capture_output=True,
                                   text=True, encoding="utf-8", check=True).stdout.split()
        except (OSError, subprocess.CalledProcessError):
            frags = None
        if frags is not None and cwsh.is_file() and bash:
            # A ZERO-FRAGMENT LISTING beside a shipped fragment is a broken selector, not a tidy
            # tree — the same refusal check-hook-destinations.sh makes over its own population.
            assert frags or not cw, "git lists no *.fragment.json while one ships beside this script"
            m = re.search(r"^matchers_of\(\) \{.*?^\}", cwsh.read_text(encoding="utf-8"), re.S | re.M)
            assert m, "check-wiring.sh no longer defines matchers_of() in the shape this arm lifts"
            # A FILE, not `bash -c`: on Windows the argv string is re-parsed by the MSYS layer and a
            # multi-line script arrives as one line, so the function body never parses.
            lifted = root / "matchers_of.sh"
            lifted.write_text('settings_json() { printf "%s\\n" "$SJ"; }\n' + m.group(0)
                              + '\nmatchers_of "$1"\n', encoding="utf-8", newline="\n")
            for f in frags:
                fr = load_fragment(Path(f))
                sf = root / "s17.json"
                if sf.exists():
                    sf.unlink()
                assert run(str(sf), resolve_hook_path(fr["hook_path"], f), False, fr, f) == 0, f
                # Forward-slashed, both: a backslashed Windows path handed to MSYS bash loses its
                # separators (`C:UsersDAILY-~1...`), and the arm then reports a missing script.
                got = subprocess.run([bash, lifted.as_posix(), fr["marker"]], capture_output=True,
                                     text=True, encoding="utf-8",
                                     env=dict(os.environ, SJ=sf.as_posix()))
                assert got.returncode == 0, f"{f}: matchers_of exited {got.returncode}: {got.stderr}"
                assert fr["matcher"] in got.stdout.split("\n"), \
                    f"{f}: matchers_of({fr['marker']!r}) returned {got.stdout!r}, not {fr['matcher']!r}"
        else:
            print("settings-merge selftest: SKIP arm 17 (matchers_of over every tracked fragment) — "
                  + ("git is not available" if frags is None
                     else "no check-wiring.sh beside this script" if not cwsh.is_file()
                     else "no bash on PATH shares this filesystem"))

        # 18) THIS FILE ALONE (closing review round 1 M4). The entry declares `requires = []`, so a
        #     target may install settings-merge with no hooks kit beside it, and arm 12 read `.name`
        #     off the None the resolver returns there. The whole selftest re-runs from a copy in a
        #     scratch root holding nothing else; the copy's own run does not recurse.
        if not os.environ.get("SETTINGS_MERGE_SELFTEST_ALONE"):
            alone = root / "alone"
            (alone / ".git").mkdir(parents=True)
            copy = alone / "scripts" / Path(__file__).name
            copy.parent.mkdir()
            copy.write_bytes(Path(__file__).read_bytes())
            got = subprocess.run([sys.executable, str(copy), "--selftest"], capture_output=True,
                                 text=True, encoding="utf-8", cwd=alone,
                                 env=dict(os.environ, SETTINGS_MERGE_SELFTEST_ALONE="1"))
            assert got.returncode == 0 and "selftest: PASS" in got.stdout, \
                f"a settings-merge-only install failed its own selftest: {(got.stdout + got.stderr)[-600:]}"

    print("settings-merge selftest: PASS")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Idempotently wire a hook fragment into .claude/settings.json")
    p.add_argument("settings_file", nargs="?", default=".claude/settings.json")
    p.add_argument("--fragment", default=None)
    p.add_argument("--hook-path", default=None)
    p.add_argument("--check", action="store_true")
    p.add_argument("--unwire", action="store_true")
    p.add_argument("--resolve-fragment", default=None, metavar="F")
    p.add_argument("--resolve-hook", default=None, metavar="P")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args(argv)
    if a.selftest:
        return _selftest()
    if a.unwire and (a.check or not a.fragment):
        print("settings-merge: --unwire takes --fragment and not --check; it removes one fragment's "
              "entry, and the built-in default is never removed by name", file=sys.stderr)
        return 2
    frag = AGENT_CAP
    try:
        if a.resolve_hook:
            # The owned-hook join's ONE reader, printed for check-wiring.sh (the round-1 fold, S3).
            print(resolve_owned_hook(a.resolve_hook))
            return 0
        if a.resolve_fragment:
            # A PRINT VERB, nothing else: the value `merge` would write, so a checker can read the
            # decision instead of re-deriving it beside this file. Twinned on check-wiring.sh.
            frag = load_fragment(Path(a.resolve_fragment))
            print(resolve_hook_path(frag["hook_path"], a.resolve_fragment))
            return 0
        if a.fragment:
            frag = load_fragment(Path(a.fragment))
        # RESOLVED ONCE, HERE, before anything reads it. The existence refusal below and the merge
        # itself must agree on which file they are talking about, and a `{kit}` token reaching the
        # refusal makes it reject a path nobody ever meant to write.
        hook_path = resolve_hook_path(a.hook_path or frag["hook_path"], a.fragment)
    except ValueError as e:
        print(f"settings-merge: {e}", file=sys.stderr)
        return 2
    # Refuse to wire a script that is not there: settings would dispatch `<interpreter> <missing>`
    # on every matching tool call, and check-wiring can only NAME that state, not prevent it.
    # Resolved from the cwd, which the runbook fixes at the target repo root. --check is exempt —
    # it writes nothing, it reports drift, and the hook file is not what it is reporting on.
    # --unwire is exempt too: a rollback removes the hook file before it unwires the entry.
    if not a.check and not a.unwire and not Path(hook_path).exists():
        interp = frag.get("interpreter", _DEFAULT_INTERPRETER)
        print(f"settings-merge: refusing to wire {frag['name']} — {hook_path} does not exist "
              f"(from {Path.cwd()}). Copy the hook there first (or pass --hook-path); wiring a "
              f"missing script makes every matching tool call run `{interp}` against nothing.",
              file=sys.stderr)
        return 2
    return run(a.settings_file, hook_path, a.check, frag, a.fragment, a.unwire)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
