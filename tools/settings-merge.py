#!/usr/bin/env python3
"""settings-merge.py — idempotently wire a hook into a target repo's .claude/settings.json.
Stdlib only (json, argparse, pathlib); py>=3.10 (write_text newline=).

# gov:kit settings-merge@1.5

The default hook, with no --fragment (shape mirrors WIRE-INTO-PROJECT.md and
tools/hooks/agent-cap.js verbatim):

    {"hooks": {"PreToolUse": [
      {"matcher": "Workflow|Agent",
       "hooks": [{"type": "command",
                  "command": "node \\"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\\""}]}]}}

Idempotent by structure: a re-run finds the existing matcher group already carrying the fragment's
marker in a command and makes NO change (apply-twice-changed = 0). Existing keys and any other
groups under that event are preserved; a foreign command inside the matcher group is kept alongside.

A wired target is DETECTED by grepping the fragment's `marker` in .claude/settings.json — JSON
carries no comment marker, so that command substring IS the deployer's "is-it-wired?" signal, and
it is what tools/check-wiring.sh joins each arm on.

Usage:
    python tools/settings-merge.py [SETTINGS_FILE] [--fragment F] [--hook-path P] [--check]
    python tools/settings-merge.py --selftest      (or: --resolve-fragment F)
      SETTINGS_FILE  default .claude/settings.json (resolved from cwd = target repo root)
      --fragment     a JSON file declaring {name, event, matcher, marker, hook_path} plus the
                     optional {interpreter, args}; omitted = the built-in agent-cap PreToolUse
                     fragment (matcher "Workflow|Agent")
      --hook-path    override the fragment's hook_path (the copied hook, repo-relative)
      --check        report drift without writing: exit 1 if a merge WOULD change the file
      --resolve-fragment  print the fragment's hook_path with `{kit}`/`{here}` expanded, then
                     exit — the value the merge would write; check-wiring.sh carries the same
                     verb and the hook-destinations gate asserts the two agree
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
import re
import sys
import tempfile
from pathlib import Path, PurePosixPath

KIT_SETTINGS_MERGE_VERSION = "1.5"  # gov:kit settings-merge@1.5 — engine identity
HOOK_MARKER = "agent-cap.js"  # the loose join: dedup key AND the deployer's "is-it-wired?" grep target


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
        return "tools"


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


def _resolve_agent_cap_hook_path(root: Path = Path(".")) -> str:
    """agent-cap's shipped copy: the target's declaration first, this file's own location second.

    ONE composition, in one place, so the arm that stages the break has something to red on. It is
    also the only reader of `_load_declared_prefix`: the `{kit}` fragments need no lookup at all,
    because a fragment ships beside its hook, so resolving `{kit}` against the FRAGMENT's own
    location already follows whatever prefix that kit was installed at.
    """
    return (_load_declared_prefix("agent-cap", root) or _kit_rel()) + "/hooks/agent-cap.js"


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
        return hook_path.replace("{kit}/", (rel + "/") if rel else "")
    if "{here}" in hook_path:
        raise ValueError("a {here} hook_path resolves only against a fragment file, and none was given")
    return hook_path.replace("{kit}", _kit_rel())


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
        frag_file: str | None = None) -> int:
    path = Path(settings_file)
    existed = path.exists()
    what = f"{frag['name']} {frag['matcher']} hook"
    try:
        before = _dump(_load(path))
        after = _dump(merge(json.loads(before), hook_path, frag, frag_file))
    except ValueError as e:
        print(f"settings-merge: {e}", file=sys.stderr)
        return 2
    if before == after:
        print(f"settings-merge: {what} already wired in {settings_file}")
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
        #     "scripts/hooks/agent-cap.js" and the merge refused a settings.json that was correct.
        gov = root / "dep" / ".governance"
        gov.mkdir(parents=True)
        dep = gov / "deploy.toml"
        dep.write_text('prefix = "scripts"\n\n[kit.agent-cap]\nprefix = ".claude"\n',
                       encoding="utf-8", newline="\n")
        # THE COMPOSITION, not just the reader: reverting the lookup has to red something. This
        # assertion is what fails on the pre-fix engine, which answered "<this file's prefix>/hooks/
        # agent-cap.js" and then refused to wire a tree whose settings.json was already right.
        assert _resolve_agent_cap_hook_path(gov.parent) == ".claude/hooks/agent-cap.js"
        assert _resolve_agent_cap_hook_path(root).endswith("/hooks/agent-cap.js")     # no deploy.toml -> derived
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
        shipped = Path(__file__).resolve().parent / "memory-recall" / "recall-opened.fragment.json"
        if shipped.is_file():
            got = load_fragment(shipped)
            assert {k: got[k] for k in _FRAGMENT_KEYS} == recall, \
                f"shipped fragment drifted from the pinned schema: {got}"
            # A fragment carrying neither optional key is DEFAULTED, and the defaults are the
            # pre-1.4 render: this is what keeps the three older fragments byte-identical.
            assert (got["interpreter"], got["args"]) == ("node", [])

        # --- TOOL-aReplayedCard-2: interpreter + args, {here}, the whole-command rewrite, the
        #     re-match. The four fragments are located the way the arms locate them — beside this
        #     script in an adopter, at the kit's home in gov — and an arm whose subject is absent
        #     SAYS so rather than passing over nothing.
        here = Path(__file__).resolve().parent

        def resolve_shipped(*cands: Path) -> Path | None:
            return next((c for c in cands if c.is_file()), None)

        card = resolve_shipped(here / "orientation-card.fragment.json",
                          here.parent / "skills" / "session-kickoff" / "orientation-card.fragment.json")
        replay = resolve_shipped(here / "orientation-replay.fragment.json",
                            here.parent / "skills" / "session-kickoff" / "orientation-replay.fragment.json")
        cw = resolve_shipped(here / "check-wiring.fragment.json")
        pm = resolve_shipped(here / "process-monitor" / "procmon-session.fragment.json")

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
            foreign = 'node "${CLAUDE_PROJECT_DIR}/tools/mine.js" --write-log'
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
        for older in (here / "hooks" / "scratch-guard.fragment.json",
                      here / "process-monitor" / "procmon-hook.fragment.json", shipped):
            if older.is_file():
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

    print("settings-merge selftest: PASS")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Idempotently wire a hook fragment into .claude/settings.json")
    p.add_argument("settings_file", nargs="?", default=".claude/settings.json")
    p.add_argument("--fragment", default=None)
    p.add_argument("--hook-path", default=None)
    p.add_argument("--check", action="store_true")
    p.add_argument("--resolve-fragment", default=None, metavar="F")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args(argv)
    if a.selftest:
        return _selftest()
    frag = AGENT_CAP
    try:
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
    if not a.check and not Path(hook_path).exists():
        interp = frag.get("interpreter", _DEFAULT_INTERPRETER)
        print(f"settings-merge: refusing to wire {frag['name']} — {hook_path} does not exist "
              f"(from {Path.cwd()}). Copy the hook there first (or pass --hook-path); wiring a "
              f"missing script makes every matching tool call run `{interp}` against nothing.",
              file=sys.stderr)
        return 2
    return run(a.settings_file, hook_path, a.check, frag, a.fragment)


if __name__ == "__main__":
    sys.exit(main())
