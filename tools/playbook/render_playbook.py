#!/usr/bin/env python3
"""render_playbook.py — fill the governance charter template into a target's charter.

WHAT THIS REPLACES. The charter used to ship with a prose companion telling an agent to fill 28
placeholders by hand and delete the conditional blocks their project had no kit for. That companion
is retired: filling is mechanical, so it is a program's job, and what a program cannot decide moved
to the runbook.

THE THREE CLASSES. Every placeholder is DECLARED in the playbook entry's govkit descriptor as one of:

  derived    a named probe here computes it from the target repo. The render PRINTS what it derived,
             so a wrong derivation is visible rather than silent. AN EXPLICIT ANSWER OUTRANKS THE
             PROBE (DEPL-aRepatriatedFork-1 S1): a probe that answers WRONGLY — a submodule's
             `.git/modules/<name>` read as the primary tree — was uncorrectable, so both adopters
             forked the descriptor instead. The note line prints the answer beside what the probe
             would have derived. A probe returning nothing with no answer falls through to REFUSAL,
             never to a default it did not declare — a probe that quietly returns the empty string
             is how a charter ships with a blank where a branch name belongs.
  asked      it must come from the target's deploy.toml answers table. Absent is a refusal NAMING the
             key. Nothing is guessed; that posture is govkit's and this engine inherits it.
  defaulted  a declared default applies, and the render RECORDS that it defaulted. A default silently
             identical to an answer is how an operator ships a value they never chose.

TWO FENCE NAMESPACES, AND NEITHER READS A BOOLEAN.
  <!-- kit:<id> -->      drops when <id> is absent from deploy.toml's `kits`.
  <!-- when:<name> -->   drops when <name> is a MEMBER of deploy.toml's `drop_blocks`.

WHERE A VALUE COMES FROM, in order: deploy.toml's `[charter]` table, then `[answers]`, then (for
`derived`) the probe or (for `defaulted`) the declared default. `[charter]` is the RENDER-ONLY value
class: govkit's `target_context` never reads it, so nothing in it reaches a `ctx` token or an argv,
and it may therefore carry the prose `[answers]` refuses — an em dash, angle brackets, a backtick.
What it may NOT carry is graded by `read_charter_table`.

`drop_blocks` is a LIST, not a set of booleans, and that is load-bearing. govkit's intake writes
every answer as `key = "value"`, so a key "answered false" arrives as the STRING `false` — truthy
under every natural reading — and the block would survive. That is the failure that reads as success,
arriving through type coercion rather than through a name. Membership has no such reading.

Both namespaces REFUSE rather than skip: a `kit:` fence naming a non-entry, a `when:` fence naming an
undeclared block, a `drop_blocks` member matching no fence, and a `kits` member that is not a
registry entry id are each a refusal. An unrecognised name that merely left the block in place would
be a silent no-op.

THE TWO NAMESPACES ARE NOT SYMMETRIC ON THE FENCE SIDE, and that is measured rather than sloppy. A
`drop_blocks` member matching no fence is a typo by construction — the list exists only to name
fences. A `kits` member matching no fence is the NORMAL case: gov selects twenty entries and the
charter carries three `kit:` fences, because most kits have no conditional ruleset. So `kits` is
graded against the REGISTRY, which is the population it is drawn from, and an empty `kits` under an
existing deploy.toml is itself a refusal — it silently drops every conditional block, and intake
cannot write one (`resolve_selection` refuses an empty selection), so it can only be a hand edit.

WHERE THE INPUTS COME FROM, AND WHY IT IS NOT `__file__`'s GRANDPARENT. This engine ships into a
target at `{prefix}/playbook/`, so its grandparent there is the TARGET's repo root — which holds
neither `<prefix>/govkit/entries/playbook.kit.toml` (a registry exemption that never lands in a target)
nor a repo-root charter template (the deployer lands it at the operator-chosen `playbook_path`).
Resolving from the grandparent worked in gov and died in every adopter with an uncaught
FileNotFoundError, straight past `main`'s `except Refusal`. So: the DECLARATIONS are read from beside
the engine when the kit shipped them there and from gov's own tree otherwise, the TEMPLATE from the
target's `playbook_path` answer when it has one, and every one of those reads REFUSES naming the path
it wanted. A missing input is a stated reason, never a traceback.

THE REGION READER IS THIS FILE'S OWN. The memory-tree kit's region helper RAISES when no marker pair
is present, so it serves neither the absent-charter nor the charter-without-a-region state. This
engine therefore CONFORMS to the marker-region contract and adds a fifth reader to its case table; it
does not import that implementation, which would be a cross-kit edge the contract itself forbids.

THE ONE RENDERER OF RECORD (PLAY-dOrderedCharter-20). `--render-scope <scope>` writes a scope and
`--check-render --scope <scope>` compares it, `--target` defaulting to this kit's repository. `charter` is
`render()` above, and `--check` is its check spelled for the adopter. `entry-files` is `CLAUDE.md` and each
other harness alias, the pointer or copy pointing at AGENTS.md, taking `--aliases`, `--mode` and `--force`
and with no `--aliases` the ones `renderers.toml` assigns it. `claims`, check only, runs the parity gate
until the charter's stated values render from sourced fact units. `--check-render` with no scope is the
render gate: every scope, then `renderers.toml` (each instruction file has exactly one renderer of record),
the status arm, and the legacy list under the policy key `instructions.legacy`. A template's
`<!-- units: <selector> -->` line expands to the selected units' lines, one per unit.

THE PRACTICE LINES (PLAY-dOrderedCharter-1). A template's `{{PRACTICES}}` line expands to `- [<name>] <line>`
per active row of `practices.toml` beside this engine, before the placeholder set is collected, so a token
inside a line resolves as it would in the template. The active set is the policy key `charter.practices`,
the `foundation` set where that key is a derived default or no policy kit answers, less each row whose `kit`
is not selected and each `drop_blocks` member naming a row. A template with no such line reads neither the
catalogue nor the key.
"""
from __future__ import annotations

import argparse
import functools
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
def resolve_bash(script):
    r"""The bash that can SEE `script`, by RUNNING each candidate, or None. GOV_BASH first, then the
    bash PATH names, then Git for Windows' two paths, each kept only when `test -f` on the script
    exits 0 under it. On Windows PATH order commonly puts the System32 WSL launcher first, which
    cannot open a `C:/` path, and a stub that exits 127 can sit there too (gotcha
    subprocess-resolves-a-different-shell); being on PATH is not evidence."""
    cands = [os.environ.get("GOV_BASH", ""), shutil.which("bash") or "",
             "C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"]
    tried = []
    for c in cands:
        if not c or c in tried:
            continue
        tried.append(c)
        try:
            r = subprocess.run([c, "-c", 'test -f "$1"', "_", str(script)], capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            continue
        if r.returncode == 0:
            return c
    return None
# <<< resolve_bash_py


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


# >>> render_envelope — canonical copy: envelope.py in the gov lib dir (byte-identical; gated)
def render_envelope(doc, level, direction, body):
    """`body` between the opener and the closer naming `doc`; an empty body renders the two lines alone."""
    if body and not body.endswith("\n"):
        body += "\n"
    return "[%s · Level %d · %s]\n%s[/%s]\n" % (doc, level, direction, body, doc)


def read_envelopes(text):
    """Each whole line of `text` that is an envelope line, in order: `(line number, "open", doc, level,
    direction)` for an opener and `(line number, "close", doc, None, None)` for a closer."""
    import re
    opener = re.compile(r"^\[([^\[\]/][^\[\]]*?) · Level (\d+) · ([^\]]*)\]$")
    closer = re.compile(r"^\[/([^\[\]]+)\]$")
    found = []
    for n, line in enumerate(text.replace("\r\n", "\n").split("\n"), 1):
        m = opener.match(line)
        if m:
            found.append((n, "open", m.group(1), int(m.group(2)), m.group(3)))
            continue
        m = closer.match(line)
        if m:
            found.append((n, "close", m.group(1), None, None))
    return found
# <<< render_envelope


OPEN_RE = re.compile(r'^[ \t]*<!--\s*(kit|when):([A-Za-z0-9_-]+)\s*-->[ \t]*$')
CLOSE_RE = re.compile(r'^[ \t]*<!--\s*/(kit|when):([A-Za-z0-9_-]+)\s*-->[ \t]*$')
PLACEHOLDER_RE = re.compile(r'\{\{([A-Z][A-Z0-9_]*)\}\}')
REGION_OPEN = '<!-- gov:playbook -->'
REGION_CLOSE = '<!-- /gov:playbook -->'
REGION_MARKER_RE = re.compile(r'<!--\s*/?gov:playbook\s*-->')
# TOOL-aDistilledCharter-1. A ONE-LINE REGION holds rules a reader takes in at a glance: every line
# a `- ` bullet, none past ONE_LINE_MAX characters, no continuation. Graded AFTER substitution, which
# is the only moment an adopter's own section 2 exists. The markers survive into the charter.
ONE_LINE_OPEN = '<!-- one-line -->'
ONE_LINE_CLOSE = '<!-- /one-line -->'
ONE_LINE_MAX = 200
# govkit's TOKEN_RX, spelled again because this engine ships without govkit. `{relpath}` and the
# seeded three are govkit-derived, so they are never an operator's key.
ARGV_TOKEN_RE = re.compile(r'(?<!\$)\{([a-z_]+)\}')
ARGV_DERIVED_TOKENS = {'prefix', 'kit_id', 'kit', 'relpath', 'memory_root'}
# PLAY-dOrderedCharter-20: the scopes of the one renderer, and the entry files' wiring.
RENDER_SCOPES = ('charter', 'entry-files')
CHECK_SCOPES = (*RENDER_SCOPES, 'claims')
UNIT_SLOT_RE = re.compile(r'^[ \t]*<!--\s*units:\s*(\S+)\s*-->[ \t]*$', re.M)
CANON = 'AGENTS.md'
ALIAS_PATHS = {'claude': 'CLAUDE.md', 'gemini': 'GEMINI.md', 'copilot': '.github/copilot-instructions.md',
               'cursor': '.cursorrules', 'windsurf': '.windsurfrules'}
GEMINI_SETTINGS = '.gemini/settings.json'
GEMINI_CONFIGURED_RE = re.compile(rf'"fileName"[^\S\n]*:[^\S\n]*(\[[^\S\n]*)?"{re.escape(CANON)}"')
IMPORT_LINE_RE = re.compile(rf'^@\.*/?([^/\n]*/)*{re.escape(CANON)}[^\S\n]*$', re.M)
PARITY_GATE = 'check-playbook-parity.sh'
PRACTICES_LINE_RE = re.compile(r'^[ \t]*\{\{PRACTICES\}\}[ \t]*$', re.M)
# The policy kit's DERIVED_WHY, spelled again because a kit imports no sibling; the selftest runs the real reader.
POLICY_DERIVED_LINE = 'a derived default no reader computes yet'


class Refusal(Exception):
    """A stated reason to write nothing. Every one names what the operator must supply."""


# --------------------------------------------------------------------------- derivation probes
def read_git(root: Path, *args: str) -> str:
    """Run git in the target and return stdout, or the empty string when it cannot answer.

    No inherited `GIT_*` variable reaches git (TOOL-aDistilledCharter-7, R6): a hook reached through a
    `.git` file exports `GIT_DIR`, which outranks `-C` and would answer for the ambient repository."""
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    try:
        r = subprocess.run(['git', '-C', root.as_posix(), *args], env=env,
                           capture_output=True, text=True, encoding="utf-8", timeout=30)
        return r.stdout.strip() if r.returncode == 0 else ''
    except (OSError, subprocess.SubprocessError):
        return ''


def read_conf(root: Path, name: str, key: str) -> str:
    """Read one KEY=value out of a shell-style conf, without sourcing it."""
    p = root / name
    if not p.is_file():
        return ''
    for line in p.read_text(encoding='utf-8', errors='replace').splitlines():
        line = line.strip()
        if line.startswith(f'{key}='):
            # TOOL-aRepatriatedFork-38: a quoted value ends at its matching quote, an unquoted one
            # at a `#` beginning a word; `.strip('"')` kept a trailing comment and a stray quote.
            # rev-3 (C4): whitespace right after `=` ends the assignment; `#` begins a comment only
            # after whitespace, so `K=#x` keeps `#x` and `K= # note` is blank, as bash reads them.
            if line[len(key) + 1:][:1].isspace():
                return ''
            v = line[len(key) + 1:].strip()
            close = v.find(v[0], 1) if v[:1] in ('"', "'") else -1
            if close >= 0:
                return v[1:close]
            return re.split(r'\s#', v, maxsplit=1)[0].strip()
    return ''


def derive_project_name(root: Path, _a: dict, _e: Path | None = None) -> str:
    # The PRIMARY tree's name, never the current directory's. `root.resolve().name` answers whatever
    # worktree the render ran in, so a render from a throwaway branch dir baked that dir's name into a
    # committed charter as the product's identity — and the next render from anywhere else produced a
    # different region, redding the unguarded wiring leg. Same worktree-sensitivity `derive_primary_tree`
    # already carries a comment about, missed one function away.
    return Path(derive_primary_tree(root, _a)).name or root.resolve().name


# The remote ladder (TOOL-dLadderedRemote-2), INLINED byte-identically from the canonical copy
# named on its marker line and gated by the resolve-python self-test.
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


def derive_default_branch(root: Path, _a: dict, _e: Path | None = None) -> str:
    # The OBSERVED branch, never GOV_DEFAULT_BRANCH: a render the bar byte-compares must not move
    # with an operator's environment. The remote is the ladder's, so a node whose remote is not
    # called `origin` renders its real default instead of a local name that happens to match
    # (TOOL-dLadderedRemote-2). A refusal falls back to the local names, as no remote always did.
    _remote, _branch, observed, refusal = resolve_remote(root)
    if refusal:
        print(f'render-playbook: {refusal} The default branch falls back to a local main or master.',
              file=sys.stderr)
    if observed:
        return observed
    for cand in ('main', 'master'):
        if read_git(root, 'rev-parse', '--verify', '--quiet', cand):
            return cand
    return ''


def derive_memory_root(root: Path, _a: dict, _e: Path | None = None) -> str:
    return read_conf(root, '.memory-tree.conf', 'MEMORY_ROOT') or 'memory'


def derive_memory_disciplines(root: Path, _a: dict, _e: Path | None = None) -> str:
    return read_conf(root, '.memory-tree.conf', 'DISCIPLINES')


def derive_id_families(root: Path, _a: dict, _e: Path | None = None) -> str:
    return read_conf(root, '.memory-tree.conf', 'FAMILIES')


def derive_ci_file(root: Path, _a: dict, _e: Path | None = None) -> str:
    d = root / '.github' / 'workflows'  # the target's CI dir, not the review-harness kit
    if d.is_dir():
        hits = sorted(p.name for p in d.iterdir() if p.suffix in ('.yml', '.yaml'))
        if hits:
            return f'.github/workflows/{hits[0]}'
    return ''


def derive_gate_runner(root: Path, _a: dict, _e: Path | None = None) -> str:
    # The run-gates kit through the ONE sibling resolver (TOOL-aRepatriatedFork-2 S3), looked up
    # from this engine when it sits inside the target and from the target's root when it renders a
    # tree it is not installed in. A dir outside the target is no answer, and neither is a miss.
    here = Path(__file__).resolve().parent
    top = root.resolve()
    try:
        kit = resolve_kit_dir('run-gates', 'run-gates.sh', here if top in here.parents else top)
        return f'bash {(kit / "run-gates.sh").relative_to(top).as_posix()}'
    except (LookupError, ValueError):
        pass
    # TOOL-aRepatriatedFork-29 S5 — NO FIXED CANDIDATE LIST. The fallback used to probe three paths
    # at two hard-coded prefixes, so a runner installed anywhere else rendered no bar at all. It now
    # probes under the TARGET'S kit root: the deploy answer's `prefix` when it states one, else every
    # directory at depth 1 or 2 holding the kit — and only an unambiguous single answer is taken.
    #
    # `prefix` IS A TOP-LEVEL deploy.toml KEY, never an `[answers]` one (closing review round 1 M1):
    # `govkit intake` writes it only at the top, and `_a` is the `[answers]` table, so this read
    # found nothing and every flat runner below went unreachable. The target's own file is read
    # when the answers do not carry it.
    home, anchor = 'run-gates', 'run-gates.sh'
    pfx = _a.get('prefix') if isinstance(_a, dict) else None
    if not pfx:
        try:
            pfx = tomllib.loads((top / '.governance' / 'deploy.toml').read_text(
                encoding='utf-8')).get('prefix')
        except (OSError, ValueError):
            pfx = None
    roots = [pfx.strip('/')] if isinstance(pfx, str) and pfx.strip('/') else sorted(
        {p.parent.parent.relative_to(top).as_posix()
         for pat in ('*/', '*/*/') for p in top.glob(f'{pat}{home}/{anchor}')
         if not any(s.startswith('.') for s in p.relative_to(top).parts)})
    if len(roots) != 1:
        return ''
    for rel in (f'{home}/{anchor}', anchor, 'gate.sh'):
        if (top / roots[0] / rel).is_file():
            return f'bash {roots[0]}/{rel}'
    return ''


def derive_lexicon_conf(root: Path, _a: dict, _e: Path | None = None) -> str:
    return '.lexicon.conf' if (root / '.lexicon.conf').is_file() else ''


# NO `derive_machine`, and no probe reading $USERNAME/$COMPUTERNAME at all. One did, and baked one
# node's identity into a charter committed to a shared remote, so every other node's render differed
# and the unguarded wiring leg red for them. The node registry is fleet data the operator states —
# since TOOL-aDistilledCharter-2 in the fleet registry beside this engine, never in the environment.

# --------------------------------------------------------------------------- the fleet registry
# TOOL-aDistilledCharter-2. Gov is the ONE allocator of node tags: `fleet.toml` ships beside this
# engine into every adopter, and every adopter's charter renders its node table from it, so a machine
# carries one tag everywhere. A repository overrides a cell for one node under `[nodes.<tag>]`.
FLEET_NAME = 'fleet.toml'
NODE_KEYS = ('primary_tree', 'worktree_root', 'variances')
# LEGACY v3.x blocks and placeholders are the descriptor's rows carrying `legacy`, read in `render`
# (TOOL-aDistilledCharter-2 rev-2, -9). An adopter's template is a seed `govkit update` never
# rewrites, so the regenerate it runs (unless GOVKIT_RERENDER=0) renders a v3.x template with this
# engine and must not roll the kit back.
#
# The template major version this engine ships with, and the rule is major-only (PLAY-dOrderedCharter-41
# S3). A template whose marker major is below it renders as it always did, may carry a legacy fence,
# and gets the note that a newer one is available to reseed. One at or above it may carry no legacy
# fence and gets no reseed note, a minor behind included.
TEMPLATE_MAJOR = 4
TEMPLATE_MARKER_RE = re.compile(r'<!--\s*governance-template:\s*v([0-9]+)\.([0-9]+)\s*-->')
# The marker's whole line and one blank line after it, which a render drops (PLAY-dOrderedCharter-12 S5).
TEMPLATE_MARKER_LINE_RE = re.compile(rf'^[ \t]*{TEMPLATE_MARKER_RE.pattern}[ \t]*\n(?:[ \t]*\n)?', re.M)


def read_fleet(path: Path) -> list[dict]:
    """The fleet registry's rows sorted by tag, every row graded. Refuses naming the row."""
    try:
        data = tomllib.loads(path.read_text(encoding='utf-8'))
    except OSError as e:
        raise Refusal(f'the fleet registry is not readable at {path.as_posix()} ({e.strerror}); '
                      f'it ships beside the engine, so the playbook-render kit is incomplete here')
    except tomllib.TOMLDecodeError as e:
        raise Refusal(f'the fleet registry at {path.as_posix()} is not valid TOML: {e}')
    rows = data.get('node') or []
    if not rows:
        raise Refusal(f'the fleet registry at {path.as_posix()} names no node, so no node could '
                      f'identify itself from the charter')
    tags, users = set(), []
    for n, row in enumerate(rows, 1):
        tag = row.get('tag')
        if not (isinstance(tag, str) and re.fullmatch(r'[a-z]', tag)):
            raise Refusal(f'fleet row {n}: tag {tag!r} is not one lowercase letter')
        if tag in tags:
            raise Refusal(f'fleet row {n}: tag `{tag}` is already taken by an earlier row')
        for key in ('user', 'projects_root'):
            if not (isinstance(row.get(key), str) and row[key].strip()):
                raise Refusal(f'fleet row {n} (`{tag}`): `{key}` is empty')
        for key in ('host', 'variances'):
            if not isinstance(row.get(key, ''), str):
                raise Refusal(f'fleet row {n} (`{tag}`): `{key}` must be a string')
        clash = check_user_clash(row['user'], users)
        if clash:
            raise Refusal(f'fleet row {n} (`{tag}`): {clash}')
        tags.add(tag)
        users.append((row['user'], tag))
    return sorted(rows, key=lambda r: r['tag'])


def check_user_clash(user: str, held: list[tuple[str, str]]) -> str:
    """Why `user` cannot join a fleet holding `held` (user, tag) pairs, or '' when it can.

    TOOL-aDistilledCharter-7, R3. Every reader of the rendered table matches the USER alone —
    `manifest-check.sh` by equality or the `<user> @` prefix, `run-selftests.sh` by a substring of
    `$USERNAME` — so a second row for one user, on any host, is a node no reader can tell apart, and
    one user name inside another is the substring reader's wrong answer."""
    u = user.strip().lower()
    for other, tag in held:
        o = other.strip().lower()
        if u == o:
            return f'user {user!r} already holds tag `{tag}`, and readers match the user alone'
        if u in o or o in u:
            return (f'user {user!r} and the user {other!r} of tag `{tag}` contain one another, and a '
                    f'reader matching by substring would take the wrong row')
    return ''


def resolve_node_overrides(target: Path, tags: set[str]) -> dict[str, dict]:
    """The target's `[nodes.<tag>]` tables, graded against the fleet's tags and NODE_KEYS."""
    try:
        cfg = tomllib.loads((target / '.governance' / 'deploy.toml').read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {}
    nodes = cfg.get('nodes') or {}
    if not isinstance(nodes, dict):
        raise Refusal('deploy.toml `nodes` must be a table of `[nodes.<tag>]` tables')
    for tag, table in nodes.items():
        if tag not in tags:
            raise Refusal(f'deploy.toml [nodes.{tag}] names a tag the fleet registry does not hold; '
                          f'claim the node in gov first')
        if not isinstance(table, dict):
            raise Refusal(f'deploy.toml [nodes.{tag}] must be a table')
        bad = sorted(set(table) - set(NODE_KEYS))
        if bad:
            raise Refusal(f'deploy.toml [nodes.{tag}] carries {", ".join(bad)}; only '
                          f'{", ".join(NODE_KEYS)} override a node row')
        for key, val in table.items():
            if not (isinstance(val, str) and val.strip()) or '\n' in val:
                raise Refusal(f'deploy.toml [nodes.{tag}] {key} must be a non-empty single line')
    return nodes


def derive_node_table(root: Path, _a: dict, _e: Path | None = None) -> str:
    """The section-3 node table, from the fleet registry beside the engine.

    The SHAPE is every reader's contract: `manifest-check.sh` takes the first table under
    `## Node registry` and matches the user against the Machine/user cell; `run-selftests.sh` and
    the drift audit match a backticked tag and a backticked user token at the head of a row."""
    fleet = read_fleet((_e or Path(__file__).resolve().parent) / FLEET_NAME)
    over = resolve_node_overrides(root, {r['tag'] for r in fleet})
    # TOOL-aDistilledCharter-5. The checkout name is the committed `project_name` answer, never the
    # rendering clone's directory: two nodes with clones named apart would commit two charters and
    # red each other's wiring leg, and a submodule's probe answers `vendor`. A node whose clone sits
    # under another name takes `[nodes.<tag>] primary_tree`.
    try:
        cfg = tomllib.loads((root / '.governance' / 'deploy.toml').read_text(encoding='utf-8'))
    except (OSError, ValueError):
        cfg = {}
    # TOOL-aDistilledCharter-8, N2: the `[answers]` key `checkout_dir` when stated — a product named
    # apart from its clone (`App` cloned as `app/main`) states the clone once — else `project_name`,
    # which `[charter]` may carry too. `[charter]` refuses `checkout_dir`: it names no placeholder (-9, T5).
    def read_answer(name: str, tables: tuple[str, ...]) -> str:
        return next((v.strip() for tbl in tables
                     for k, v in (cfg.get(tbl) or {}).items()
                     if str(k).lower() == name and isinstance(v, str) and v.strip()), '')
    checkout = read_answer('checkout_dir', ('answers',)) or read_answer('project_name',
                                                                        ('charter', 'answers'))
    if not checkout:
        raise Refusal('NODE_TABLE builds every node\'s primary tree from `checkout_dir`, else '
                      '`project_name`, and deploy.toml answers neither. Answer one under [answers] '
                      'rather than letting the rendering clone\'s directory stand in for every node')

    def render_cell(text: str) -> str:
        return text.replace('|', r'\|')
    out = ['| Tag | Machine/user | Primary tree | Worktree root | Variances |',
           '|-----|--------------|--------------|---------------|-----------|']
    for r in fleet:
        o = over.get(r['tag'], {})
        host = r.get('host', '').strip()
        ident = f'{r["user"]} @ {host}' if host else r['user']
        primary = o.get('primary_tree') or f'{r["projects_root"].rstrip("/")}/{checkout}'
        worktrees = o.get('worktree_root') or f'{primary}/.claude/worktrees'
        variances = o.get('variances') or r.get('variances', '').strip() or 'none recorded'
        out.append(f'| `{r["tag"]}` | `{render_cell(ident)}` | `{render_cell(primary)}` | `{render_cell(worktrees)}` '
                   f'| {render_cell(variances)} |')
    return '\n'.join(out)


def derive_role_roster(root: Path, _a: dict, _e: Path | None = None) -> str:
    """The section-3 Agent roles lines, printed by the roles kit's own `roster` verb.

    TOOL-aOrientedCast-18. The roles kit stays the one reader of role files: this probe runs its verb
    and substitutes the stdout verbatim, adding, cutting and reordering nothing, because the line shape
    and its cap are the verb's and the one-line region grades the result. The kit is found through the
    sibling resolver, as `derive_gate_runner` finds its own, so no kit path is spelled here. A miss —
    no kit, a verb that cannot start, a non-zero exit, or an exit 0 printing nothing — prints its cause
    and returns the empty string, so an answer still outranks it and an unanswered miss refuses at
    `resolve_placeholder_raw` naming the key (F2)."""
    here = _e or Path(__file__).resolve().parent
    top = root.resolve()
    home, anchor = 'roles', 'handoff.py'
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    try:
        kit = resolve_kit_dir(home, anchor, here if top in here.parents else top)
        r = subprocess.run([sys.executable, str(kit / anchor), 'roster'], cwd=str(top), env=env,
                           capture_output=True, text=True, encoding='utf-8', errors='replace',
                           timeout=30)
    except LookupError as e:
        why = str(e)
    except (OSError, subprocess.SubprocessError) as e:
        why = f'the roster verb did not run: {e}'
    else:
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
        said = (r.stderr.strip().splitlines() or ['it printed no line'])[0][:240]
        why = f'the roster verb exited {r.returncode}: {said}'
    print(f'render-playbook: ROLE_ROSTER: {why}', file=sys.stderr)
    return ''


def write_fleet_claim(engine_dir: Path, user: str, host: str, projects_root: str,
                      variances: str) -> str:
    """Append a row with the lowest letter the fleet has not used, and return that letter.

    Appends TEXT rather than re-serialising, so the registry's comments survive. Refused in an
    installed copy — recognised, as `resolve_declaration_paths` recognises one, by the descriptor
    sitting beside the engine — because the next update would overwrite a local claim."""
    if (engine_dir / 'playbook.kit.toml').is_file():
        raise Refusal('this engine is an INSTALLED copy, and its fleet registry is gov\'s: a claim '
                      'here is overwritten by the next update. Claim the node in gov\'s checkout, '
                      'then update this repository')
    for key, val in (('--user', user), ('--projects-root', projects_root)):
        if not val.strip():
            raise Refusal(f'{key} is empty')
    for val in (user, host, projects_root, variances):
        if any(ord(c) < 32 or ord(c) == 127 for c in val):
            raise Refusal('a claim value carries a control character')
    path = engine_dir / FLEET_NAME
    fleet = read_fleet(path)
    clash = check_user_clash(user, [(r['user'], r['tag']) for r in fleet])
    if clash:
        raise Refusal(clash)
    taken = {r['tag'] for r in fleet}
    free = next((c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in taken), None)
    if free is None:
        raise Refusal('the fleet holds all 26 tags; a 27th node needs a wider tag alphabet first')
    raw = path.read_bytes()
    eol = b'\r\n' if b'\r\n' in raw else b'\n'
    row = [f'tag = "{free}"', f'user = {json.dumps(user.strip(), ensure_ascii=False)}',
           f'host = {json.dumps(host.strip(), ensure_ascii=False)}',
           f'projects_root = {json.dumps(projects_root.strip(), ensure_ascii=False)}',
           f'variances = {json.dumps(variances.strip(), ensure_ascii=False)}']
    block = eol + b'[[node]]' + eol + eol.join(s.encode('utf-8') for s in row) + eol
    if not raw.endswith(eol):
        raw += eol
    # Parse the WHOLE new file before writing it (R5): a claim that fails here leaves gov's fleet
    # registry untouched, where a write-then-check left every later render refusing.
    try:
        tomllib.loads((raw + block).decode('utf-8'))
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
        raise Refusal(f'the claimed row would leave the fleet registry unreadable ({e}); nothing '
                      f'was written')
    path.write_bytes(raw + block)
    return free


def derive_primary_tree(root: Path, _a: dict, _e: Path | None = None) -> str:
    # The PRIMARY tree, not whichever worktree this render runs from. `--show-toplevel` answers the
    # linked worktree, so a render performed inside one would register that worktree as the node's
    # primary tree — measured on gov's own first render. `--git-common-dir` points at the main
    # repository's .git wherever it is run, and its parent is the primary checkout.
    common = read_git(root, 'rev-parse', '--path-format=absolute', '--git-common-dir')
    if common:
        return Path(common).parent.as_posix()
    top = read_git(root, 'rev-parse', '--show-toplevel')
    return top or root.resolve().as_posix()


def derive_worktree_root(root: Path, _a: dict, _e: Path | None = None) -> str:
    primary = derive_primary_tree(root, _a)
    return f'{primary}/.claude/worktrees' if primary else ''


PROBES = {
    'project_name': derive_project_name,
    'default_branch': derive_default_branch,
    'memory_root': derive_memory_root,
    'memory_disciplines': derive_memory_disciplines,
    'id_families': derive_id_families,
    'ci_file': derive_ci_file,
    'gate_runner': derive_gate_runner,
    'lexicon_conf': derive_lexicon_conf,
    'node_table': derive_node_table,
    'role_roster': derive_role_roster,
    'primary_tree': derive_primary_tree,
    'worktree_root': derive_worktree_root,
}


# --------------------------------------------------------------------------- the fence pass
def check_fences(text: str, entries: set[str], blocks: set[str]) -> list[tuple[str, str]]:
    """Return every (namespace, name) fence, refusing on an unbalanced or undeclared one."""
    stack, seen = [], []
    for n, line in enumerate(text.splitlines(), 1):
        m = OPEN_RE.match(line)
        if m:
            ns, name = m.group(1), m.group(2)
            if ns == 'kit' and name not in entries:
                raise Refusal(f'line {n}: a kit fence names `{name}`, which is not a registry entry '
                              f'id. An unrecognised id would leave the block in place, which is the '
                              f'failure that reads as success')
            if ns == 'when' and name not in blocks:
                raise Refusal(f'line {n}: a when fence names `{name}`, which the descriptor declares '
                              f'nowhere. Declare it as a [[block]] row or remove the fence')
            stack.append((ns, name, n))
            seen.append((ns, name))
            continue
        m = CLOSE_RE.match(line)
        if m:
            if not stack:
                raise Refusal(f'line {n}: a closing fence with no opener: {m.group(1)}:{m.group(2)}')
            ons, oname, _ = stack.pop()
            if (ons, oname) != (m.group(1), m.group(2)):
                raise Refusal(f'line {n}: fence closes {m.group(1)}:{m.group(2)} but the open one is '
                              f'{ons}:{oname}')
    if stack:
        ns, name, n = stack[-1]
        raise Refusal(f'line {n}: fence {ns}:{name} is never closed')
    return seen


def remove_fenced(text: str, drop: set[tuple[str, str]]) -> str:
    """Remove every fenced block whose (namespace, name) is in `drop`, fences included."""
    out, skip_depth = [], 0
    for line in text.splitlines(keepends=True):
        m = OPEN_RE.match(line.rstrip('\n'))
        if m:
            key = (m.group(1), m.group(2))
            if skip_depth or key in drop:
                skip_depth += 1
            continue          # a SURVIVING block loses its markers; a dropped one loses its body too
        m = CLOSE_RE.match(line.rstrip('\n'))
        if m:
            if skip_depth:
                skip_depth -= 1
            continue
        if not skip_depth:
            out.append(line)
    return ''.join(out)


# --------------------------------------------------------------------------- substitution
TABLE_ROW_RE = re.compile(r'^[ \t]*\|')


def build_substitution(text: str, key: str, val: str) -> str:
    """Replace every `{{KEY}}` with `val`, escaped for the HOST CONTEXT of each occurrence.

    A markdown TABLE ROW is a structured host and a verbatim substitution corrupts it: an unescaped
    `|` opens a cell the template never declared, and a newline ends the row early. Measured on gov's
    own §2 node registry, which is the table an agent is told to identify its node from.

    Per OCCURRENCE, not per key: one key can land in a table cell and in prose in the same charter,
    and `\\|` in prose is a backslash a reader sees. What is NOT handled, said plainly rather than
    implied away: a backtick in a value the TEMPLATE wrapped in backticks mangles the code span, and
    no escape fixes that inside one — CommonMark's answer is a longer delimiter run, which is the
    template author's decision. The fix for that class is to stop wrapping free-text cells, which is
    what `{{VARIANCES_A}}` now is.
    """
    token = '{{' + key + '}}'
    if token not in text:
        return text
    out = []
    for line in text.split('\n'):
        if token in line and TABLE_ROW_RE.match(line):
            if '\n' in val or '\r' in val:
                raise Refusal(f'the answer for {key} carries a newline and the template puts it in a '
                              f'table row, which the newline would end early. Give a single-line '
                              f'answer for a cell')
            out.append(line.replace(token, val.replace('|', r'\|')))
        else:
            out.append(line.replace(token, val))
    return '\n'.join(out)


# The `one-line-rule` cap's answer per target repository, asked of the policy kit once per target in a
# process (TOOL-dGroundRules-9).
_ONE_LINE_ANSWERS: dict = {}


def read_one_line_cap(target: Path) -> tuple:
    """`(value, mode, rule)` of the census cap `one-line-rule` for the repository at `target`: the
    policy kit's `budgets.resolve_caps`, handed ONE_LINE_MAX as its default, the kit found by
    `resolve_kit_dir` from this engine, so a `budgets."one-line-rule"` in the target's policy file
    takes the constant's place. No kit, or any refusal of the reader, keeps ONE_LINE_MAX and refuses
    as before, the rule saying why."""
    key = str(Path(target).resolve())
    if key not in _ONE_LINE_ANSWERS:
        why = ''
        try:
            kit = str(resolve_kit_dir('policy', 'budgets.py', Path(__file__).resolve().parent))
            if kit not in sys.path:
                sys.path.insert(0, kit)
            import budgets  # the policy kit's caps module, found above
            try:
                a = budgets.resolve_caps([f'one-line-rule=default:{ONE_LINE_MAX}'], key)['one-line-rule']
                _ONE_LINE_ANSWERS[key] = (a.value, a.mode, a.rule)
            except budgets.policy.Refusal as exc:
                why = f'the policy reader refused: {exc}'
        except (LookupError, ImportError) as exc:
            why = f'no policy kit answered: {exc}'
        if key not in _ONE_LINE_ANSWERS:
            _ONE_LINE_ANSWERS[key] = (ONE_LINE_MAX, 'refuse', f'{why}; an over-length rule refuses as before')
    return _ONE_LINE_ANSWERS[key]


def check_one_line_regions(text: str, cap: tuple | None = None) -> list:
    """Refuse a one-line region holding anything but short single-line bullets.

    Line numbers are the RENDERED body's; the refusal quotes the line so an operator can find it in
    the source it came from — the template for section 1, `[charter] adopter_rules` for section 2.
    What it does NOT grade: what a rule says, or any line outside a region.

    THE LENGTH OBEYS THE SWITCH (TOOL-dGroundRules-9): `cap` is `read_one_line_cap`'s `(value, mode,
    rule)`, ONE_LINE_MAX refusing where none is given. Under `warn` a rule past the value is a
    `BUDGET WARN` line in the returned list and the render goes on; under `refuse` it is refused as
    before, naming the rule. The other refusals are shape, never size, and refuse under `warn` too.
    -> the warned lines."""
    limit, mode, rule = cap or (ONE_LINE_MAX, 'refuse', '')
    warned = []
    inside = 0
    for n, line in enumerate(text.split('\n'), 1):
        bare = line.strip()
        if bare == ONE_LINE_OPEN:
            if inside:
                raise Refusal(f'line {n}: a one-line region opens inside another one, opened at '
                              f'line {inside}')
            inside = n
            continue
        if bare == ONE_LINE_CLOSE:
            if not inside:
                raise Refusal(f'line {n}: a one-line region closes with none open')
            inside = 0
            continue
        if not inside or not bare:
            continue
        quoted = line.strip()[:60]
        if not re.match(r'- \S', line):
            raise Refusal(f'line {n}: a one-line region holds a line that is not a `- ` bullet, '
                          f'so a rule spans two lines or is not a rule: {quoted!r}')
        if limit and len(line.rstrip()) > limit:
            if mode == 'warn':
                warned.append(f'BUDGET WARN — one-line-rule · line {n} {quoted!r} · '
                              f'{len(line.rstrip())} chars over {limit} · {rule}')
                continue
            raise Refusal(f'line {n}: a rule in a one-line region is {len(line.rstrip())} '
                          f'characters, past the {limit} a one-line rule may take: {quoted!r}'
                          + (f' ({rule})' if rule else ''))
    if inside:
        raise Refusal(f'line {inside}: a one-line region is never closed')
    return warned


# --------------------------------------------------------------------------- the region reader
def write_region(charter_path: Path, body: str) -> None:
    """The write mode's ONE write: the region rebuilt around `body`, whatever the file held.

    DEPL-aHalvedInstall-3 rev-3. govkit's `update` runs this kit's write mode as its `[[regenerate]]`
    unless GOVKIT_RERENDER=0 is exported, so the mode must replace an existing region in place and leave the authored prose around it
    alone. Factored out of `main` so the selftest's run-twice arm calls the code the adopter runs."""
    cur = charter_path.read_text(encoding='utf-8') if charter_path.is_file() else None
    charter_path.parent.mkdir(parents=True, exist_ok=True)
    charter_path.write_text(build_region(cur, body), encoding='utf-8', newline='\n')


def load_units_module():
    """The kit's `instruction_units`, imported from beside this engine however it was launched."""
    engine = str(Path(__file__).resolve().parent)
    if engine not in sys.path:
        sys.path.insert(0, engine)
    import instruction_units
    return instruction_units


def derive_renderer_label() -> str:
    """This kit at KIT_PLAYBOOK_RENDER_VERSION, a lock row's `renderer`."""
    import render_playbook   # the module's own constant: as a script, `main` runs above the line defining it
    return f'playbook-render@{render_playbook.KIT_PLAYBOOK_RENDER_VERSION}'


def write_charter_lock(gov_root: Path, target: Path, charter_path: Path, units=()) -> None:
    """PLAY-dOrderedCharter-12 S5: the charter's row of the target's `.governance/instructions.lock`,
    written after every write-mode render: `blob` hashes the bytes `write_region` just wrote, `renderer`
    is this kit at KIT_PLAYBOOK_RENDER_VERSION, `template` the template's path and its version marker,
    the provenance the rendered text no longer carries, and `units` each `(tag, line)` a slot expanded to.
    `instruction_units.write_lock_row` writes it."""
    template = resolve_template_path(gov_root, target, read_deploy(target)[2]).resolve()
    marker = TEMPLATE_MARKER_RE.search(read_input(template, 'the charter template'))
    base = target if template.is_relative_to(target) else gov_root.resolve()
    load_units_module().write_lock_row(
        target, Path(os.path.relpath(charter_path, target)).as_posix(), derive_renderer_label(),
        f'{template.relative_to(base).as_posix()}@v{marker.group(1)}.{marker.group(2)}' if marker else '', units)


def write_empty_lists(target: Path) -> list[str]:
    """PLAY-dOrderedCharter-70 S10: the two lists this kit's checks red when absent, written empty where
    the check looks and the folder exists and the list does not: the positional list under
    `<target>/<MEMORY_ROOT>/project/` (PLAY-dOrderedCharter-72), the pending list under
    `<target>/<prefix>/<kit dir>`. A present file is left alone. -> the paths written, target-relative."""
    iu = load_units_module()
    homes = (('positional-refs.txt', target / derive_memory_root(target, {}).strip('/') / 'project'),
             ('core-pending.txt', target / iu.derive_kit_prefix() / iu.KIT_DIR.name))
    written = []
    for name, home in homes:
        path = home / name
        if home.is_dir() and not path.exists():
            path.write_bytes(b'')
            written.append(path.relative_to(target).as_posix())
    return written


def build_region(charter: str | None, body: str) -> str:
    """Write `body` between the region markers. THREE states, and this reader serves all of them.

    absent charter          -> a file holding only the region
    charter, no region      -> the region appended, every authored byte untouched
    charter with a region   -> the region's contents replaced and nothing else
    """
    block = f'{REGION_OPEN}\n{body.rstrip()}\n{REGION_CLOSE}\n'
    if charter is None:
        return block
    if REGION_OPEN not in charter:
        sep = '' if charter.endswith('\n\n') else ('\n' if charter.endswith('\n') else '\n\n')
        return charter + sep + block
    if charter.count(REGION_OPEN) != 1 or charter.count(REGION_CLOSE) != 1:
        raise Refusal('the charter carries more than one gov:playbook region, so which one the render '
                      'replaces is a matter of scan order')
    head = charter.split(REGION_OPEN)[0]
    tail = charter.split(REGION_CLOSE, 1)[1]
    return head + block.rstrip('\n') + tail


# --------------------------------------------------------------------------- the render
def read_input(path: Path, what: str) -> str:
    """Read a REQUIRED input, or refuse naming the path. Every miss here used to be a traceback."""
    try:
        return path.read_text(encoding='utf-8')
    except OSError as e:
        raise Refusal(f'{what} is not readable at {path.as_posix()} ({e.strerror}). Supply that '
                      f'path — the render has nothing to read and will not guess one')


def resolve_declaration_paths(engine_dir: Path, gov_root: Path) -> tuple[Path, Path]:
    """The descriptor and the registry, from the INSTALLED layout first and gov's own second.

    An installed kit carries both beside the engine, because the deployer's own directory is a
    registry exemption that never lands in a target. Gov has no copy beside the engine and falls
    through to its own tree, which is what keeps one source of truth for these two files.

    TOOL-aRepatriatedFork-29 S5: the fallback is DERIVED from the engine's own location, not joined
    under `gov_root` at a spelled prefix. The engine's parent is gov's tool root; the registry is the
    one `*/registry.toml` there and the descriptor the one `*/entries/playbook.kit.toml`, so neither
    the tool root nor the deployer's directory is named. `gov_root` stays in the signature for the
    template, which sits at the checkout's root.
    """
    desc = engine_dir / 'playbook.kit.toml'
    reg = engine_dir / 'registry.toml'
    tool_root = engine_dir.parent

    def derive_one(pattern: str, fallback: Path) -> Path:
        hits = sorted(tool_root.glob(pattern))
        return hits[0] if len(hits) == 1 else fallback

    return (desc if desc.is_file() else derive_one(f'*/entries/{desc.name}', desc),
            reg if reg.is_file() else derive_one(f'*/{reg.name}', reg))


def resolve_template_path(gov_root: Path, target: Path, answers: dict) -> Path:
    """The charter TEMPLATE this render reads.

    The deployer lands it at the operator-chosen `playbook_path`, so that answer is authoritative
    when a target has one — and when it names a file that is not there, the read REFUSES rather than
    silently falling back to gov's copy, which would render somebody else's template.

    `playbook_path` names the TEMPLATE here, never the charter; the charter is `--charter`. When the
    two are one file `render` refuses (S3), because the render would append a region into its own
    template and the next render would read that region back as template text.
    """
    p = answers.get('playbook_path')
    if isinstance(p, str) and p:
        return target / p
    return gov_root / 'coding-governance-agents.template.md'


def load_declarations(desc_path: Path, reg_path: Path) -> tuple[dict, list[dict], set[str]]:
    desc = tomllib.loads(read_input(desc_path, "the playbook entry's descriptor"))
    reg = tomllib.loads(read_input(reg_path, 'the govkit registry'))
    entries = {e['id'] for e in reg.get('entry', [])}
    return desc, desc.get('block', []), entries


def read_argv_tokens(desc: dict) -> set[str]:
    """Every `{token}` the descriptor puts in a destination or an argv — govkit's `needed_answers`
    walk over the ONE descriptor this engine ships with. The whole-selection join is `govkit check`'s,
    which holds every descriptor; this engine holds only its own."""
    blobs: list[str] = []
    for rule in desc.get('files', []):
        to = rule.get('to')
        blobs += (to if isinstance(to, list) else [to]) if to else []
    for h in desc.get('hole', []):
        blobs += (h.get('discharge') or {}).get('command') or []
    for leg in desc.get('gate_leg', []):
        blobs += (leg.get('argv') or []) + (leg.get('guard') or [])
    blobs += (desc.get('adopt') or {}).get('argv') or []
    blobs += (desc.get('check') or {}).get('argv') or []
    return {t for b in blobs for t in ARGV_TOKEN_RE.findall(b or '')} - ARGV_DERIVED_TOKENS


def read_charter_table(cfg: dict, rows: list[dict], argv_tokens: set[str]) -> dict[str, str]:
    """The `[charter]` table, every key and value graded. Returns `{lowercase key: value}`.

    Refused, naming the key: a key that is an argv token (its value must reach that argv, so it
    belongs in `[answers]`, where this engine's reader would never see it moved); a key no
    `[[placeholder]]` declares (it would supply nothing, silently); a non-string value; a control
    character other than a newline; the `{{` opener (the value would re-enter substitution); and a
    `gov:playbook` region marker (the value would split the region `build_region` rewrites).
    """
    table = cfg.get('charter') or {}
    if not isinstance(table, dict):
        raise Refusal('deploy.toml `charter` must be a table of placeholder keys')
    declared = {r['key'].lower() for r in rows}
    out: dict[str, str] = {}
    for k, v in table.items():
        key = k.lower()
        if key in argv_tokens:
            raise Refusal(f'[charter] {k} names a token an argv or destination of this kit needs. '
                          f'[charter] never reaches an argv, so that value belongs in [answers]')
        if key not in declared:
            raise Refusal(f'[charter] {k} names no declared [[placeholder]], so it would supply '
                          f'nothing. A misspelt key here is otherwise silent')
        if not isinstance(v, str):
            raise Refusal(f'[charter] {k} must be a string')
        bad = sorted({c for c in v if (ord(c) < 32 and c != '\n') or ord(c) == 127})
        if bad:
            raise Refusal(f'[charter] {k} carries control character(s) {"".join(bad)!r}; only a '
                          f'newline is admitted')
        if '{{' in v:
            raise Refusal(f'[charter] {k} carries `{{{{`, which would re-enter placeholder '
                          f'substitution')
        if REGION_MARKER_RE.search(v):
            raise Refusal(f'[charter] {k} carries a gov:playbook region marker, which would split '
                          f'the region the render rewrites')
        out[key] = v
    return out


def resolve_placeholder_value(row: dict, charter: dict, answers: dict,
                              target: Path, engine_dir: Path | None = None) -> tuple[str, str]:
    """One placeholder's value and its note line, as the render AND `--answers` both use it.

    TOOL-aDistilledCharter-7. The trailing newlines of a TOML multi-line string go here (R8), so a
    sibling renderer asking `--answers` gets the value the charter carries; and a value carrying a
    one-line marker is refused (R7), because it could close a region early and escape the grade."""
    val, note = resolve_placeholder_raw(row, charter, answers, target, engine_dir)
    val = str(val).rstrip('\n')
    if ONE_LINE_OPEN in val or ONE_LINE_CLOSE in val:
        raise Refusal(f'the value for {row["key"]} carries a one-line region marker, which would let '
                      f'it close the region the render grades')
    return val, note


def resolve_placeholder_raw(row: dict, charter: dict, answers: dict,
                            target: Path, engine_dir: Path | None = None) -> tuple[str, str]:
    """One placeholder's value as stated. Precedence: `[charter]`, `[answers]`, then the probe
    (derived) or the declared default (defaulted). The one site the three classes share."""
    key, cls = row['key'], row.get('class')
    given = charter.get(key.lower()) or answers.get(key.lower())
    if cls == 'derived':
        probe = PROBES.get(row.get('probe', ''))
        if probe is None:
            raise Refusal(f'{key} declares probe `{row.get("probe")}`, which this engine does '
                          f'not define')
        seen = probe(target, answers, engine_dir)
        if given:
            # F2, RESOLVED: a redundant answer is a note, never a failure. The empty-probe case is
            # gov's own `ci_file`: no workflow exists yet, and the answer says so.
            why = ('probe derives nothing' if not seen else
                   'redundant: the probe derives the same value' if str(given) == seen else
                   f'probe would derive {seen}')
            return given, f'answered  {key} = {given}   ({why})'
        if not seen:
            raise Refusal(f'{key} is derived by probe `{row["probe"]}`, it returned nothing for '
                          f'this target, and no answer overrides it. Supply it under [answers] or '
                          f'[charter] rather than shipping a blank')
        return seen, f'derived   {key} = {seen}'
    if cls == 'asked':
        if given in (None, ''):
            raise Refusal(f'{key} is an ASKED placeholder and deploy.toml supplies no value for it. '
                          f'Refusing to invent one: an answer this tool guesses is one the '
                          f'operator never made and cannot audit')
        return given, f'answered  {key}'
    if cls == 'defaulted':
        if given:
            return given, f'answered  {key}'
        val = row.get('default', '')
        if not val:
            raise Refusal(f'{key} is defaulted and its declared default is empty')
        return val, f'DEFAULTED {key} = {val}   (no answer supplied)'
    raise Refusal(f'{key} declares class `{cls}`, which is not derived, asked or defaulted')


def read_deploy(target: Path) -> tuple[Path, dict, dict]:
    """The target's deploy.toml, parsed, and its `[answers]` keyed lowercase. Absent is a refusal."""
    dep = target / '.governance' / 'deploy.toml'
    if not dep.is_file():
        raise Refusal(f'{dep.as_posix()} does not exist. Run `govkit intake` first — it writes the '
                      f'answers this render reads, once, and refuses to overwrite them afterwards')
    cfg = tomllib.loads(dep.read_text(encoding='utf-8'))
    return dep, cfg, {k.lower(): v for k, v in (cfg.get('answers') or {}).items()}


def read_kits(dep: Path, cfg: dict, entries: set[str]) -> set[str]:
    """The `kits` selection, graded against the registry it is drawn from."""
    kits = set(cfg.get('kits') or [])
    # THE `kits` ARRAY IS GRADED, and it was not. A member is a registry entry id — that is the
    # population it is drawn from — and an unrecognised one selects nothing, so the whole kit section
    # it was meant to keep is DROPPED and `--check` re-renders from the same file and stays green
    # forever. Measured: rewriting `codebase-map` to `codebasemap` deleted the entire codebase-map
    # ruleset from the charter with no word said. The adjacent `drop_blocks` loop refused exactly
    # this shape two lines down; the symmetry gap between them is the defect.
    if not kits:
        raise Refusal(f'{dep.as_posix()} declares no `kits`, so every kit: fence in the template '
                      f'would drop and the charter would lose every conditional ruleset silently. '
                      f'Intake cannot write an empty selection, so this is a hand edit')
    unknown = sorted(k for k in kits if k not in entries)
    if unknown:
        raise Refusal(f'`kits` names {", ".join(unknown)}, which {"is" if len(unknown) == 1 else "are"} '
                      f'not a registry entry id. An unrecognised member selects nothing, so a kit '
                      f'fence it was meant to keep drops instead — the failure that reads as success')
    return kits


def resolve_answers(engine_dir: Path, gov_root: Path, target: Path,
                    keys: list[str]) -> dict:
    """TOOL-aRepatriatedFork-42. The value this engine would use for each of KEYS, for a SIBLING
    renderer that must state the same answer rather than read deploy.toml a second time.

    A key the descriptor declares as a placeholder resolves exactly as `render` resolves it: the
    same precedence, the same probe, the same refusal. `kits` is the selection `render` grades.
    `kit.<entry>.<key>` is the value govkit's `target_context` interpolates for that entry's
    `{<key>}` token: the `[kit.<entry>]` value over the `[answers]` value, or None when neither
    table answers it, where govkit falls back to its own default (`memory` for `memory_root`).
    Any other key is the `[answers]` value, then the file's top-level value, or None when it has
    neither — the caller owns what an absent answer means, because only it knows whether it needs one.

    rev-3 (the closing review's C6): every key compares case-insensitively, as `[answers]` and
    `[charter]` already do here, so one question never has two answers selected by spelling.
    """
    desc, _blocks, entries = load_declarations(*resolve_declaration_paths(engine_dir, gov_root))
    dep, cfg, answers = read_deploy(target)
    rows = desc.get('placeholder', [])
    by_key = {r['key'].upper(): r for r in rows}
    charter = read_charter_table(cfg, rows, read_argv_tokens(desc))
    top = {str(k).lower(): v for k, v in cfg.items()}
    per_entry = cfg.get('kit') if isinstance(cfg.get('kit'), dict) else {}
    out: dict = {}
    for key in keys:
        low = key.lower()
        if key.upper() in by_key:
            out[key] = resolve_placeholder_value(by_key[key.upper()], charter, answers, target,
                                                 engine_dir)[0]
            continue
        if low == 'kits':
            out[key] = sorted(read_kits(dep, cfg, entries))
            continue
        if low.startswith('kit.') and low.count('.') >= 2:
            eid, sub = low[len('kit.'):].rsplit('.', 1)
            table = per_entry.get(eid)
            val = ({str(k).lower(): v for k, v in table.items()}.get(sub)
                   if isinstance(table, dict) else None)
            if not isinstance(val, str):
                val = answers.get(sub)
        else:
            val = answers.get(low, top.get(low))
        out[key] = val if isinstance(val, str) and val else None
    return out


def render_unit_slots(text: str, target: Path, notes: list, slots: list | None = None) -> str:
    """Each `<!-- units: <selector> -->` line replaced by the lines of the units its selector selects, and
    nothing of its own. A selector no namespace registers, a selected unit whose change records retired it
    and an unreadable manifest each refuse; a slot selecting nothing is noted `unarmed`. Each `(tag, line)`
    lands in `slots`, what the lock's row records."""
    if not UNIT_SLOT_RE.search(text):
        return text
    iu = load_units_module()
    from policy_value import read_policy_value
    read_key = functools.partial(read_policy_value, root=target)
    try:
        units, records = iu.read_units(target), iu.read_change_records(target)
    except ValueError as e:    # UnitRowError and the git reader's LevelError
        raise Refusal(f'the units a slot selects are unreadable: {e}') from None

    def render_slot(match) -> str:
        selector = match.group(1)
        fault = iu.check_tag_entry(selector)
        if fault:
            raise Refusal(f'the slot `{selector}` {fault}')
        chosen = iu.derive_unit_selection(units, selector)
        for u in chosen:
            status = iu.derive_status(u.tag, records)
            if status != 'active':
                raise Refusal(f'the slot `{selector}` selects {u.tag}, whose status is {status}: a template '
                              f'selects active units only')
        if not chosen:
            notes.append(f'unarmed   slot {selector} selects no unit')
        try:
            lines = [iu.render_unit(u, read_key, target) for u in chosen]
        except iu.UnitRowError as e:
            raise Refusal(str(e)) from None
        if slots is not None:
            slots.extend((u.tag, line) for u, line in zip(chosen, lines))
        return '\n'.join(lines)

    return UNIT_SLOT_RE.sub(render_slot, text)


def render_practice_lines(catalogue: dict, target: Path, kits: set, cut: list, notes: list) -> list[str]:
    """`- [<name>] <line>` per active row: S4's set, less each `cut` member's row and each row whose `kit` is
    not selected. A derived default, or no policy kit, takes the `foundation` set and notes it; any other
    refused read, a set value that cannot resolve and an empty result refuse."""
    iu = load_units_module()
    from policy_value import PolicyRefused, read_policy_value
    value = None
    try:
        lines, _explain = read_policy_value("charter.practices", target)
    except PolicyRefused as exc:
        if POLICY_DERIVED_LINE in exc.line:
            notes.append('charter.practices — the foundation set: a derived default the policy reader '
                         'leaves to the practice catalogue')
        elif exc.line.startswith('no policy kit found'):
            notes.append('charter.practices — the foundation set: no policy kit in this install, so no '
                         'set can be read')
        else:
            raise Refusal(f'charter.practices: {exc.line}') from None
    else:
        try:
            from instructions_edit import resolve_practices  # loads the memory-tree kit, so only a set value does
        except (LookupError, ImportError) as exc:
            raise Refusal(f'charter.practices holds a set, and resolving it needs the memory-tree kit, '
                          f'which this install lacks: {exc}') from None
        try:
            value = resolve_practices(lines)
        except ValueError as exc:     # its UnitRowError and the git read's LevelError
            raise Refusal(f'charter.practices: {exc}') from None
    try:
        rows = iu.resolve_active_practices(catalogue, value)
    except iu.UnitRowError as exc:
        raise Refusal(str(exc)) from None
    gone = {f'practice.{d}' for d in cut}
    kept = [r for r in rows if r['tag'] not in gone and ('kit' not in r or r['kit'] in kits)]
    if not kept:
        raise Refusal('charter.practices leaves no practice to render, once the rows whose kit is not '
                      'selected and the drop_blocks members are cut')
    return [f"- [{r['tag'].split('.', 1)[1]}] {r['line']}" for r in kept]


def render(engine_dir: Path, gov_root: Path, target: Path,
           charter_path: Path | None = None, slots: list | None = None) -> tuple[str, list[str]]:
    desc, blocks, entries = load_declarations(*resolve_declaration_paths(engine_dir, gov_root))
    dep, cfg, answers = read_deploy(target)
    rows = desc.get('placeholder', [])
    charter = read_charter_table(cfg, rows, read_argv_tokens(desc))
    kits = read_kits(dep, cfg, entries)
    drop_names = list(cfg.get('drop_blocks') or [])

    declared_blocks = {b['name'] for b in blocks}
    for d in drop_names:
        if d not in declared_blocks:
            raise Refusal(f'drop_blocks names `{d}`, which the descriptor declares nowhere. A member '
                          f'that drops nothing is a typo or a block that has already gone')

    template = resolve_template_path(gov_root, target, answers)
    if (charter_path is not None and template.is_file() and charter_path.is_file()
            and os.path.samefile(template, charter_path)):
        raise Refusal(f'the template {template.as_posix()} and the charter '
                      f'{charter_path.as_posix()} are one file, so the render would append a '
                      f'region into its own template. `playbook_path` names the TEMPLATE; point it '
                      f'at the installed template, or pass a different --charter')
    text = read_input(template, 'the charter template')
    present = check_fences(text, entries, declared_blocks)
    marker = TEMPLATE_MARKER_RE.search(text)
    current = bool(marker) and int(marker.group(1)) >= TEMPLATE_MAJOR
    # The LEGACY blocks are the descriptor's `[[block]]` rows carrying `legacy` (TOOL-aDistilledCharter-9,
    # T6): one declaration, never a typed copy. A template at this engine's major carrying one's fence
    # has regained a block v4.0 retired, which is a refusal.
    legacy = {b['name']: b.get('why', '') for b in blocks if b.get('legacy')}
    for ns, name in present:
        if ns == 'when' and name in legacy and current:
            raise Refusal(f'the template is v{marker.group(1)}.{marker.group(2)} and carries the '
                          f'when:{name} fence, a legacy block kept only for older seeded templates')
    # A legacy block whose fence this template does not carry is noted, never refused: it is a v4.0
    # template under a deploy.toml written for v3.x. With the fence present it drops as it always did.
    retired = [d for d in drop_names if d in legacy and ('when', d) not in present]
    drop_names = [d for d in drop_names if d not in retired]
    # PLAY-dOrderedCharter-1 S6: a member naming a catalogue row leaves the active set, fence or none.
    catalogue, cut = None, []
    if PRACTICES_LINE_RE.search(text):
        iu = load_units_module()
        try:
            catalogue = iu.read_practice_catalogue(engine_dir / 'practices.toml')
        except iu.UnitRowError as e:
            raise Refusal(str(e)) from None
        tags = {r['tag'] for r in catalogue['practice']}
        cut = [d for d in drop_names if f'practice.{d}' in tags]
    for d in drop_names:
        if ('when', d) not in present and d not in cut:
            raise Refusal(f'drop_blocks names `{d}` but no when fence in the template carries it')

    drop = {('kit', name) for ns, name in present if ns == 'kit' and name not in kits}
    drop |= {('when', d) for d in drop_names if ('when', d) in present}
    text = remove_fenced(text, drop)
    # PLAY-dOrderedCharter-12 S5: render provenance never loads. The template keeps its marker, which this
    # render and its parity readers read from the source; the lock's charter row carries it (main).
    text = TEMPLATE_MARKER_LINE_RE.sub('', text)

    notes = [f'retired   drop_blocks {d} — {legacy[d]}; remove it from deploy.toml' for d in retired]
    notes += [f'retired   drop_blocks {d} — practice.{d} leaves the active set; charter.practices names the '
              f'set directly' for d in cut]
    if catalogue:
        text = PRACTICES_LINE_RE.sub(
            lambda _m: '\n'.join(render_practice_lines(catalogue, target, kits, cut, notes)), text, count=1)
    if marker and not current:
        notes.append(f'legacy    template v{marker.group(1)}.{marker.group(2)} at '
                     f'{template.as_posix()} — this engine ships v{TEMPLATE_MAJOR}.x; reseed the '
                     f'template from gov, then re-render')
    by_key = {r['key']: r for r in rows}
    for key in sorted(set(PLACEHOLDER_RE.findall(text))):
        row = by_key.get(key)
        if row is None:
            raise Refusal(f'the template carries {{{{{key}}}}} and the descriptor declares no '
                          f'[[placeholder]] row for it, so nothing can supply a value')
        # N6: a legacy row exists only so a SEEDED older template keeps rendering. A template at this
        # engine's major naming one has regained a name v4.0 retired, which is a refusal, not a value.
        if row.get('legacy') and marker and int(marker.group(1)) >= TEMPLATE_MAJOR:
            raise Refusal(f'the template is v{marker.group(1)}.{marker.group(2)} and carries '
                          f'{{{{{key}}}}}, a legacy {row["legacy"]} placeholder kept only for older '
                          f'seeded templates')
        val, note = resolve_placeholder_value(row, charter, answers, target, engine_dir)
        notes.append(note)
        # A TOML multi-line string ends in a newline, and the template line holding the token ends in
        # one too; without the strip every multi-line answer adds a blank line after itself.
        text = build_substitution(text, key, str(val).rstrip('\n'))
    text = render_unit_slots(text, target, notes, slots)
    notes += check_one_line_regions(text, read_one_line_cap(target) if ONE_LINE_OPEN in text else None)
    for ns, name in sorted(set(present)):
        if (ns, name) in drop:
            notes.append(f'dropped   {ns}:{name}')
    return render_charter_envelope(target, charter_path, text), notes


def render_charter_envelope(target: Path, charter_path: Path | None, text: str) -> str:
    """PLAY-dOrderedCharter-3 S4: `text` in the charter's envelope, from the row of the target's own document
    registry whose path matches the charter. No registry in the target, no charter path, or no row matching
    it renders `text` unchanged and says nothing; a registry that does not read refuses."""
    iu = load_units_module()
    if charter_path is None or not iu.derive_kit_file(target, iu.DOCUMENTS).is_file():
        return text
    rel = Path(os.path.relpath(charter_path, target)).as_posix()
    try:
        rows = iu.read_document_registry(target)
    except iu.DocumentRefused as e:
        raise Refusal(str(e)) from None
    row = next((r for r in rows if 'hold' not in r and iu.check_path_match(rel, r['resolved'])), None)
    return text if row is None else render_envelope(rel, row['level'], row['direction'], text)


# --------------------------------------------------------------------------- the arms
# WHY THE FIXTURE IS NOT GOV'S OWN TREE. Every arm below is about a WRONG input, and gov's committed
# `deploy.toml` is a right one — so proving a refusal here would mean corrupting the repo's own
# answers and putting them back. The fixture is a three-file scratch target instead: a descriptor, a
# registry and a template, each holding only what the arm under test reads.
DESC_FIXTURE = '''
[[placeholder]]
key = "VARIANCES_A"
class = "asked"

[[block]]
name = "security"
'''
REG_FIXTURE = '[[entry]]\nid = "lexicon"\n\n[[entry]]\nid = "codebase-map"\n'
TPL_FIXTURE = '''| Tag | Variances |
|-----|-----------|
| `a` | {{VARIANCES_A}} |

<!-- kit:codebase-map -->
the codebase-map ruleset
<!-- /kit:codebase-map -->
'''


def _write_fixture(tmp: Path, kits: str, variances: str) -> tuple[Path, Path]:
    """Write a scratch engine dir + target and return both. `kits` is TOML array source."""
    eng, tgt = tmp / 'engine', tmp / 'target'
    (eng).mkdir(parents=True, exist_ok=True)
    (tgt / '.governance').mkdir(parents=True, exist_ok=True)
    (eng / 'playbook.kit.toml').write_text(DESC_FIXTURE, encoding='utf-8')
    (eng / 'registry.toml').write_text(REG_FIXTURE, encoding='utf-8')
    (tgt / 'CHARTER.md').write_text(TPL_FIXTURE, encoding='utf-8')
    (tgt / '.governance' / 'deploy.toml').write_text(
        f'kits = {kits}\n\n[answers]\nplaybook_path = "CHARTER.md"\n'
        f'variances_a = {variances}\n', encoding='utf-8')
    return eng, tgt


def check_scope_arms(check_arm) -> None:
    """PLAY-dOrderedCharter-20: each scope re-rendered over a fixture target and its bytes compared, the failing
    case a scope holding one byte differently. The claims scope's gate is a stub, its exit what is compared."""
    import contextlib
    import io
    import tempfile

    def run_main(*argv) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = main([str(a) for a in argv])
        return rc, out.getvalue()

    with tempfile.TemporaryDirectory() as td:
        tgt = Path(td).resolve()
        read_git(tgt, 'init', '-q')
        (tgt / '.governance').mkdir()
        (tgt / '.governance' / 'deploy.toml').write_text(
            'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "TPL.md"\n', encoding='utf-8')
        (tgt / 'TPL.md').write_text('# fixture charter\n\n- MUST land.\n', encoding='utf-8')
        rc, said = run_main('--render-scope', 'charter', '--target', tgt)
        check_arm(rc == 0 and '- MUST land.' in (tgt / CANON).read_text(encoding='utf-8'),
                  'the charter scope writes its region', said)
        rc, said = run_main('--check-render', '--scope', 'charter', '--target', tgt)
        check_arm(rc == 0, 'the charter scope compares its own render green', said)
        rendered = (tgt / CANON).read_bytes()
        (tgt / CANON).write_bytes(rendered.replace(b'MUST land.', b'MUST land!'))
        rc, said = run_main('--check-render', '--scope', 'charter', '--target', tgt)
        check_arm(rc == 1 and 'DRIFT' in said, 'one byte off reds the charter scope', said)
        (tgt / CANON).write_bytes(rendered)

        rc, said = run_main('--render-scope', 'entry-files', '--target', tgt, '--aliases', 'claude copilot')
        check_arm(rc == 0 and (tgt / 'CLAUDE.md').read_bytes() == f'@{CANON}\n'.encode('utf-8')
                  and (tgt / ALIAS_PATHS['copilot']).read_bytes() == rendered,
                  'the entry-files scope writes the pointer and the copy', said)
        rows = {r['path'] for r in load_units_module().read_lock(tgt)}
        check_arm({'CLAUDE.md', ALIAS_PATHS['copilot'], CANON} <= rows, 'every scope write records its lock row', str(rows))
        rc, said = run_main('--check-render', '--scope', 'entry-files', '--target', tgt, '--aliases', 'claude copilot')
        check_arm(rc == 0, 'the entry-files scope compares its own render green', said)
        (tgt / ALIAS_PATHS['copilot']).write_bytes(rendered + b'x')
        rc, said = run_main('--check-render', '--scope', 'entry-files', '--target', tgt, '--aliases', 'claude copilot')
        check_arm(rc == 1 and 'stale copy' in said, 'one byte off reds the entry-files scope', said)

        gate = tgt / load_units_module().derive_kit_prefix() / PARITY_GATE
        rc, said = run_main('--check-render', '--scope', 'claims', '--target', tgt)
        check_arm(rc == 1 and PARITY_GATE in said, 'the claims scope reds a tree holding no gate', said)
        gate.parent.mkdir(parents=True, exist_ok=True)
        for code in (0, 1):
            gate.write_text(f'exit {code}\n', encoding='utf-8')
            rc, said = run_main('--check-render', '--scope', 'claims', '--target', tgt)
            check_arm(rc == code, f'the claims scope carries the gate\'s exit {code}', said)


PRACTICE_ROW = '\n[[practice]]\ntag = "practice.{0}"\n{1}line = "{2}"\n[practice.reach]\nbuild = "x"\n'
PRACTICE_TABLE = ('foundation = ["practice.one", "practice.cross-os", "practice.roles"]\n'
                  + PRACTICE_ROW.format('one', '', 'Rule one for {{ANSWER}}.')
                  + PRACTICE_ROW.format('cross-os', '', 'Rule two.')
                  + PRACTICE_ROW.format('roles', 'kit = "roles"\n', 'Rule three.'))
PRACTICE_TEMPLATE = (f'<!-- governance-template: v{TEMPLATE_MAJOR}.5 -->\n\n{ONE_LINE_OPEN}\n{{{{PRACTICES}}}}\n'
                     f'{ONE_LINE_CLOSE}\n')
CROSS_OS_FENCE = '<!-- when:cross-os -->\nthe toolchain section\n<!-- /when:cross-os -->\n'
PRACTICE_REFUSALS = (('a tag outside its shape', 'practice.One', 'tag = "practice.one"', 'tag = "practice.One"'),
                     ('a tag twice', 'held by an earlier row', 'tag = "practice.roles"', 'tag = "practice.one"'),
                     ('an empty line', 'its `line` is empty', 'line = "Rule two."', 'line = ""'),
                     ('no reach', 'no reach.<step> key',
                      '[practice.reach]\nbuild = "x"\n\n[[practice]]\ntag = "practice.cross-os"',
                      '\n[[practice]]\ntag = "practice.cross-os"'),
                     ('a reach key outside its shape', 'reach key `Plan`', 'build = "x"', 'Plan = "x"'),
                     ('an array of non-tables', 'holds no [[practice]] row',
                      PRACTICE_TABLE[PRACTICE_TABLE.index('\n[[practice]]'):], 'practice = ["x"]\n'),
                     ('a foundation entry naming no row', 'names practice.none', '"practice.roles"]',
                      '"practice.none"]'))


def check_practice_arms(check_arm) -> None:
    """PLAY-dOrderedCharter-1: `render` over a target committed on `main`: each refused catalogue, the `kit`
    field, a `drop_blocks` member with and without its fence, and, where a policy kit answers, the three policy
    cases; where none does, those print `unarmed` and the no-policy-kit note is what is asserted."""
    import tempfile

    def render_target(table=PRACTICE_TABLE, kits='["roles"]', tail='', tpl=PRACTICE_TEMPLATE, policy=None,
                      branch='main') -> tuple[str, list, str | None]:
        """-> (body, notes, refusal or None) of one committed fixture target."""
        with tempfile.TemporaryDirectory() as td:
            eng, tgt = Path(td) / 'engine', Path(td) / 'target'
            eng.mkdir()
            (tgt / '.governance').mkdir(parents=True)
            (eng / 'practices.toml').write_text(table, encoding='utf-8')
            (eng / 'playbook.kit.toml').write_text(
                '[[placeholder]]\nkey = "ANSWER"\nclass = "defaulted"\ndefault = "x"\n\n'
                '[[block]]\nname = "cross-os"\n', encoding='utf-8')
            (eng / 'registry.toml').write_text('[[entry]]\nid = "roles"\n\n[[entry]]\nid = "lexicon"\n',
                                               encoding='utf-8')
            (tgt / 'TPL.md').write_text(tpl, encoding='utf-8')
            (tgt / '.governance' / 'deploy.toml').write_text(
                f'kits = {kits}\n{tail}\n[answers]\nplaybook_path = "TPL.md"\n', encoding='utf-8')
            if policy is not None:
                (tgt / '.governance' / 'policy.toml').write_text(policy, encoding='utf-8')
            read_git(tgt, 'init', '-q', '-b', branch)
            read_git(tgt, 'add', '-A')
            read_git(tgt, '-c', 'user.name=fx', '-c', 'user.email=fx@example.invalid', '-c', 'commit.gpgsign=false',
                     'commit', '-qm', 'fixture')
            try:
                return (*render(eng, Path(td), tgt), None)
            except Refusal as e:
                return '', [], str(e)

    for name, want, old, new in PRACTICE_REFUSALS:
        _b, _n, got = render_target(PRACTICE_TABLE.replace(old, new, 1))
        check_arm(got is not None and want in got, f'a catalogue with {name} refuses the render',
                  f'refused with {got!r}')
    body, notes, got = render_target()
    check_arm(got is None and '- [one] Rule one for x.' in body and '- [roles] Rule three.' in body,
              'the render expands the rows and resolves a token inside a line', f'refused {got!r}: {body!r}')
    body, _n, got = render_target(kits='["lexicon"]')
    check_arm(got is None and '[roles]' not in body and '- [one]' in body,
              'a row whose kit is not selected stays out', f'refused {got!r}: {body!r}')
    note = 'retired   drop_blocks cross-os — practice.cross-os leaves'
    for name, tpl in (('with its fence', PRACTICE_TEMPLATE + CROSS_OS_FENCE), ('with no fence', PRACTICE_TEMPLATE)):
        body, notes, got = render_target(tail='drop_blocks = ["cross-os"]', tpl=tpl)
        check_arm(got is None and '[cross-os]' not in body and 'the toolchain section' not in body
                  and any(n.startswith(note) for n in notes), f'a drop_blocks member {name} leaves the set',
                  f'refused {got!r}: {body!r} {notes!r}')
    older = f'<!-- governance-template: v{TEMPLATE_MAJOR}.4 -->\n\n- [one] Kept.\n{CROSS_OS_FENCE}'
    body, notes, got = render_target(tail='drop_blocks = ["cross-os"]', tpl=older)
    check_arm(got is None and '- [one] Kept.' in body and 'the toolchain section' not in body
              and not any(n.startswith(note) for n in notes), 'a template with no practices line renders as before',
              f'refused {got!r}: {notes!r}')
    was = os.environ.pop('GOV_DEFAULT_BRANCH', None)
    try:
        _b, notes, got = render_target()
        said = [n for n in notes if n.startswith('charter.practices — the foundation set')]
        try:
            resolve_kit_dir('policy', 'policy.py', Path(__file__).resolve().parent)
        except LookupError as exc:
            print(f'  unarmed: the unset key, a committed empty set and a repository on master need a policy '
                  f'kit, and {exc}')
            check_arm(got is None and len(said) == 1 and 'no policy kit' in said[0],
                      'with no policy kit the render takes the foundation set and says so', f'{got!r} {notes!r}')
            return
        check_arm(got is None and len(said) == 1 and 'a derived default' in said[0],
                  'an unset key takes the foundation set and says so', f'{got!r} {notes!r}')
        _b, _n, got = render_target(policy='charter.practices = []\n')
        check_arm(got is not None and 'charter.practices' in got and 'this set is never empty' in got,
                  'a committed empty set refuses naming the key and the reader', f'refused with {got!r}')
        _b, _n, got = render_target(branch='master')
        check_arm(got is not None and 'charter.practices' in got and 'names no commit' in got,
                  'a repository on master with no remote refuses naming the key', f'refused with {got!r}')
    finally:
        if was is not None:
            os.environ['GOV_DEFAULT_BRANCH'] = was


def run_selftest() -> int:
    import tempfile
    passed, failed = 0, 0

    def arm(name: str, kits: str, variances: str, want: str | None, in_body: str = ''):
        nonlocal passed, failed
        with tempfile.TemporaryDirectory() as td:
            eng, tgt = _write_fixture(Path(td), kits, variances)
            try:
                body, _ = render(eng, Path(td), tgt)
                got = None
            except Refusal as e:
                body, got = '', str(e)
        if want is None:
            ok = got is None and in_body in body
            detail = f'refused: {got}' if got else f'body lacks {in_body!r}'
        else:
            ok = got is not None and want in got
            detail = 'no refusal at all' if got is None else f'refused with: {got}'
        if ok:
            passed += 1
        else:
            failed += 1
            print(f'  arm FAIL {name} — {detail}')
    # One kit id per line: a comma-joined run of quoted kit names reads to the carried-prefix ban as
    # a path assembled from quoted segments, the registry's own rule (TOOL-aRepatriatedFork-28).
    two_kits = ["codebase-map",
                "lexicon"]
    ok_kits, ok_var = json.dumps(two_kits), '"plain"'

    # H2 — the `kits` array is graded against the registry, in both failing directions.
    arm('a green render survives its own fixture', ok_kits, ok_var, None,
        in_body='the codebase-map ruleset')
    arm('a misspelled kit id is a refusal, not a silently dropped section',
        json.dumps(["codebasemap", two_kits[1]]), ok_var, 'not a registry entry id')
    arm('the misspelling does NOT reach the render', '["codebasemap"]', ok_var, 'codebasemap')
    arm('an empty kits array is a refusal, not a charter with every block dropped',
        '[]', ok_var, 'declares no `kits`')

    # M2 — substitution into a table row is escaped, and a newline in a cell is refused.
    arm('a pipe in a table-cell answer is escaped, so the row keeps its cells',
        ok_kits, '"a | pipe"', None, in_body=r'| `a` | a \| pipe |')
    arm('a backtick in a table-cell answer survives as its own code span',
        ok_kits, '"remote `origin`"', None, in_body='| `a` | remote `origin` |')
    arm('a newline in a table-cell answer is a refusal',
        ok_kits, '"""two\nlines"""', 'carries a newline')

    # The escape is per OCCURRENCE: prose must not gain a backslash.
    with tempfile.TemporaryDirectory() as td:
        eng, tgt = _write_fixture(Path(td), ok_kits, '"a | pipe"')
        (tgt / 'CHARTER.md').write_text('prose {{VARIANCES_A}} here\n', encoding='utf-8')
        body, _ = render(eng, Path(td), tgt)
        if body.strip() == 'prose a | pipe here':
            passed += 1
        else:
            failed += 1
            print(f'  arm FAIL a pipe in PROSE is left alone — got {body.strip()!r}')

    # DEPL-aHalvedInstall-3 rev-3 (closing review M7). THE WRITE MODE IS `update`'s REGENERATE (on
    # unless GOVKIT_RERENDER=0 is exported), so it
    # must be idempotent over an adopted charter and must REPLACE the region on a changed body. A
    # regression to append, or to a no-op, would roll this kit back at every adopter again.
    with tempfile.TemporaryDirectory() as td:
        eng, tgt = _write_fixture(Path(td), ok_kits, ok_var)
        body, _ = render(eng, Path(td), tgt)
        ch = tgt / 'ADOPTED.md'
        ch.write_text('# authored head\n\nkept prose\n', encoding='utf-8')
        write_region(ch, body)
        once = ch.read_bytes()
        write_region(ch, body)
        twice = ch.read_bytes()
        write_region(ch, body + 'a changed line\n')
        changed = ch.read_text(encoding='utf-8')
        ok = (once == twice and b'kept prose' in twice and 'a changed line' in changed
              and changed.count(body.strip().splitlines()[0]) == 1 and 'kept prose' in changed)
        if ok:
            passed += 1
        else:
            failed += 1
            print(f'  arm FAIL the write mode re-run is idempotent and replaces its region — '
                  f'same={once == twice} changed={changed!r}')

    # DEPL-aRepatriatedFork-1. Each case is a whole fixture: a descriptor, a template and the
    # deploy.toml tail below `kits`, so an arm states exactly the input it is about.
    def arm_fixture(name: str, desc: str, tpl: str, deploy: str, want: str | None = None,
             in_body: str = '', in_notes: str = ''):
        nonlocal passed, failed
        with tempfile.TemporaryDirectory() as td:
            eng, tgt = Path(td) / 'engine', Path(td) / 'target'
            eng.mkdir()
            (tgt / '.governance').mkdir(parents=True)
            (eng / 'playbook.kit.toml').write_text(desc, encoding='utf-8')
            (eng / 'registry.toml').write_text(REG_FIXTURE, encoding='utf-8')
            (tgt / 'CHARTER.md').write_text(tpl, encoding='utf-8')
            (tgt / '.governance' / 'deploy.toml').write_text(
                'kits = ["lexicon"]\n\n' + deploy, encoding='utf-8')
            try:
                body, notes = render(eng, Path(td), tgt)
                got = None
            except Refusal as e:
                body, notes, got = '', [], str(e)
        if want is None:
            ok = got is None and in_body in body and any(in_notes in n for n in notes)
            detail = f'refused: {got}' if got else f'body {body!r} notes {notes!r}'
        else:
            ok = got is not None and want in got
            detail = 'no refusal at all' if got is None else f'refused with: {got}'
        if ok:
            passed += 1
        else:
            failed += 1
            print(f'  arm FAIL {name} — {detail}')

    probe_desc = ('[[placeholder]]\nkey = "MEMORY_ROOT"\nclass = "derived"\n'
                  'probe = "memory_root"\n')
    # S1 / AC1 — an answer outranks a probe that DOES answer. The fixture has no .memory-tree.conf,
    # so the probe derives `memory`; the answer says `records`, and the answer must win.
    arm_fixture('an answer outranks a derived probe that answers too', probe_desc,
         'root {{MEMORY_ROOT}}\n',
         '[answers]\nplaybook_path = "CHARTER.md"\nmemory_root = "records"\n',
         in_body='root records', in_notes='(probe would derive memory)')
    # F2 — an answer equal to the probe is a note, never a refusal.
    arm_fixture('an answer equal to its probe is noted as redundant', probe_desc,
         'root {{MEMORY_ROOT}}\n',
         '[answers]\nplaybook_path = "CHARTER.md"\nmemory_root = "memory"\n',
         in_body='root memory', in_notes='redundant: the probe derives the same value')
    # S5 — [charter] outranks [answers], for a derived key too (F3).
    arm_fixture('a [charter] value outranks an [answers] value', probe_desc,
         'root {{MEMORY_ROOT}}\n',
         '[charter]\nmemory_root = "ledger"\n\n'
         '[answers]\nplaybook_path = "CHARTER.md"\nmemory_root = "records"\n',
         in_body='root ledger', in_notes='answered  MEMORY_ROOT = ledger')

    # AC9 — the mandated trailer, which [answers] cannot carry, rides [charter] byte-exact.
    trailer_desc = '[[placeholder]]\nkey = "COMMIT_TRAILER"\nclass = "asked"\n'
    trailer = 'Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>'
    arm_fixture('[charter] carries the commit trailer byte-exact', trailer_desc,
         'end with `{{COMMIT_TRAILER}}`\n',
         f'[charter]\ncommit_trailer = "{trailer}"\n\n[answers]\nplaybook_path = "CHARTER.md"\n',
         in_body=f'end with `{trailer}`', in_notes='answered  COMMIT_TRAILER')

    # AC10 — four hostile [charter] shapes, each refused naming the key.
    ans = '\n\n[answers]\nplaybook_path = "CHARTER.md"\n'
    arm_fixture('a [charter] value carrying the {{ opener is refused', trailer_desc,
         '{{COMMIT_TRAILER}}\n', '[charter]\ncommit_trailer = "a {{MACHINE_A}} b"' + ans,
         want='[charter] commit_trailer carries `{{`')
    arm_fixture('a [charter] value carrying a region marker is refused', trailer_desc,
         '{{COMMIT_TRAILER}}\n', '[charter]\ncommit_trailer = "x <!-- /gov:playbook --> y"' + ans,
         want='[charter] commit_trailer carries a gov:playbook region marker')
    arm_fixture('a [charter] value carrying a control byte is refused', trailer_desc,
         '{{COMMIT_TRAILER}}\n', '[charter]\ncommit_trailer = "a\\u001bb"' + ans,
         want='[charter] commit_trailer carries control character')
    arm_fixture('a [charter] key an argv needs is refused', trailer_desc
         + '\n[[placeholder]]\nkey = "PLAYBOOK_PATH"\nclass = "asked"\n\n'
         '[[files]]\ninclude = ["x"]\nto = "{playbook_path}"\n',
         '{{COMMIT_TRAILER}}\n', '[charter]\nplaybook_path = "CHARTER.md"' + ans,
         want='[charter] playbook_path names a token an argv')
    arm_fixture('a [charter] key naming no placeholder is refused', trailer_desc,
         '{{COMMIT_TRAILER}}\n', '[charter]\ncomit_trailer = "x"' + ans,
         want='[charter] comit_trailer names no declared [[placeholder]]')

    # TOOL-aDistilledCharter-1 — a one-line region admits short single-line bullets and nothing else.
    rules_desc = ('[[placeholder]]\nkey = "ADOPTER_RULES"\nclass = "defaulted"\n'
                  'default = "- none — this repository adds no rules of its own"\n')
    region = f'{ONE_LINE_OPEN}\n%s\n{ONE_LINE_CLOSE}\nend\n'
    arm_fixture('a continuation line in a one-line region is refused', rules_desc,
                region % '- a rule\n  that wraps', ans.lstrip(), want='not a `- ` bullet')
    arm_fixture('an over-length rule in a one-line region is refused', rules_desc,
                region % ('- ' + 'x' * ONE_LINE_MAX), ans.lstrip(), want=f'past the {ONE_LINE_MAX}')
    arm_fixture('an unclosed one-line region is refused', rules_desc,
                f'{ONE_LINE_OPEN}\n- a rule\n', ans.lstrip(), want='never closed')
    arm_fixture('a nested one-line region is refused', rules_desc,
                region % f'{ONE_LINE_OPEN}\n- a rule', ans.lstrip(), want='opens inside another')
    arm_fixture('an unanswered ADOPTER_RULES renders its declared default', rules_desc,
                region % '{{ADOPTER_RULES}}', ans.lstrip(),
                in_body=f'- none — this repository adds no rules of its own\n{ONE_LINE_CLOSE}',
                in_notes='DEFAULTED ADOPTER_RULES')
    arm_fixture('a multi-line adopter_rules answer renders with no blank line added', rules_desc,
                region % '{{ADOPTER_RULES}}',
                '[charter]\nadopter_rules = """\n- one\n- two\n"""' + ans,
                in_body=f'- one\n- two\n{ONE_LINE_CLOSE}', in_notes='answered  ADOPTER_RULES')

    # TOOL-aDistilledCharter-2 — the fleet registry, the node table it renders, and the claim.
    fleet_rows = [('a', 'ann', 'HOSTA', 'C:/p', 'quirk | piped'),
                  ('b', 'bob', '', '/home/bob/src', ''),
                  ('d', 'dee', 'HOSTD', 'C:/p', '')]

    def build_fleet_text(rows) -> str:
        return ''.join(f'[[node]]\ntag = "{t}"\nuser = "{u}"\nhost = "{h}"\n'
                       f'projects_root = "{r}"\nvariances = "{v}"\n\n' for t, u, h, r, v in rows)

    def build_node_render(fleet: str, tail: str = '', checkout: str = 'repo-one',
                          name: str = 'app'):
        with tempfile.TemporaryDirectory() as td:
            eng, tgt = Path(td) / 'engine', Path(td) / checkout
            eng.mkdir()
            (tgt / '.governance').mkdir(parents=True)
            (eng / 'playbook.kit.toml').write_text(
                '[[placeholder]]\nkey = "NODE_TABLE"\nclass = "derived"\nprobe = "node_table"\n',
                encoding='utf-8')
            (eng / 'registry.toml').write_text(REG_FIXTURE, encoding='utf-8')
            (eng / FLEET_NAME).write_text(fleet, encoding='utf-8')
            (tgt / 'CHARTER.md').write_text('## Node registry\n\n{{NODE_TABLE}}\n', encoding='utf-8')
            (tgt / '.governance' / 'deploy.toml').write_text(
                'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "CHARTER.md"\n'
                + (f'project_name = "{name}"\n' if name else '') + tail, encoding='utf-8')
            try:
                return render(eng, Path(td), tgt)[0], None
            except Refusal as e:
                return '', str(e)

    def read_pairs(body: str) -> list:
        return re.findall(r'^\| `([a-z])` \| `([^`]*)`', body, re.M)

    def check_arm(ok: bool, name: str, detail: str) -> None:
        nonlocal passed, failed
        if ok:
            passed += 1
        else:
            failed += 1
            print(f'  arm FAIL {name} — {detail}')

    one, e1 = build_node_render(build_fleet_text(fleet_rows))
    two, e2 = build_node_render(build_fleet_text(fleet_rows), checkout='other-repo')
    three, e3 = build_node_render(build_fleet_text(fleet_rows[::-1]))
    want_pairs = [('a', 'ann @ HOSTA'), ('b', 'bob'), ('d', 'dee @ HOSTD')]
    check_arm(read_pairs(one) == read_pairs(two) == read_pairs(three) == want_pairs
          and '`C:/p/app`' in one and '`C:/p/app`' in two and 'repo-one' not in one
          and r'quirk \| piped' in one,
          'one fleet renders the same (tag, identity) pairs in every repository and row order',
          f'errors {e1, e2, e3}; pairs {read_pairs(one)} / {read_pairs(two)} / {read_pairs(three)}')
    for name, rows, want in (
            ('a repeated tag', fleet_rows + [('a', 'zed', 'Z', 'C:/p', '')], 'already taken'),
            ('a repeated user and host', fleet_rows + [('e', 'ann', 'HOSTA', 'C:/p', '')],
             'already holds tag'),
            # R3: the readers match the user alone, so another host does not make a second row safe.
            ('one user on a second host', fleet_rows + [('e', 'ANN', 'OTHER', 'C:/p', '')],
             'already holds tag'),
            ('one user name inside another', fleet_rows + [('e', 'bobby', 'B2', 'C:/p', '')],
             'contain one another'),
            ('a two-letter tag', fleet_rows + [('ab', 'zed', 'Z', 'C:/p', '')],
             'not one lowercase letter')):
        _b, err = build_node_render(build_fleet_text(rows))
        check_arm(err is not None and want in err, f'the fleet refuses {name}', f'got {err!r}')
    body, err = build_node_render(build_fleet_text(fleet_rows), '\n[nodes.b]\nvariances = "x"\n')
    check_arm(err is None and '| `b` | `bob` | `/home/bob/src/app` | '
          '`/home/bob/src/app/.claude/worktrees` | x |' in body and r'quirk \| piped' in body,
          'a [nodes.<tag>] override moves its one cell and no other row', f'{err!r} {body!r}')
    _b, err = build_node_render(build_fleet_text(fleet_rows), name='')
    check_arm(err is not None and '`project_name`' in err,
              'a node table with no project_name answer refuses rather than naming the clone',
              f'got {err!r}')
    _b, err = build_node_render(build_fleet_text(fleet_rows),
                                '\n[nodes.b]\nprimary_tree = "E:/elsewhere"\n')
    check_arm(err is None and '| `b` | `bob` | `E:/elsewhere` | `E:/elsewhere/.claude/worktrees` |' in _b,
              'a [nodes.<tag>] primary_tree override still wins over project_name', f'{err!r} {_b!r}')
    for name, tail, want in (('a tag the fleet lacks', '\n[nodes.q]\nvariances = "x"\n',
                              'does not hold'),
                             ('an unknown key', '\n[nodes.b]\ncolour = "x"\n', 'only primary_tree')):
        _b, err = build_node_render(build_fleet_text(fleet_rows), tail)
        check_arm(err is not None and want in err, f'[nodes] refuses {name}', f'got {err!r}')
    with tempfile.TemporaryDirectory() as td:
        eng = Path(td)
        (eng / FLEET_NAME).write_text(build_fleet_text(fleet_rows), encoding='utf-8')
        got = write_fleet_claim(eng, 'cy', 'HOSTC', 'D:/w', '')
        rows_after = [r['tag'] for r in read_fleet(eng / FLEET_NAME)]
        try:
            write_fleet_claim(eng, 'CY', 'hostc', 'D:/w', '')
            again = 'no refusal'
        except Refusal as e:
            again = str(e)
        (eng / 'playbook.kit.toml').write_text('', encoding='utf-8')
        try:
            write_fleet_claim(eng, 'new', 'N', 'D:/w', '')
            installed = 'no refusal'
        except Refusal as e:
            installed = str(e)
    check_arm(got == 'c' and rows_after == ['a', 'b', 'c', 'd'] and 'already holds' in again
          and 'INSTALLED' in installed,
          'a claim takes the lowest free letter, once per identity, never in an installed copy',
          f'got {got!r} rows {rows_after} again {again!r} installed {installed!r}')
    arm_fixture('a legacy drop_blocks member with no fence is noted with the descriptor\'s why',
                trailer_desc + '\n[[block]]\nname = "node-table"\nlegacy = "v3"\nwhy = "WHY-X"\n',
                'plain\n', 'drop_blocks = ["node-table"]\n' + ans, in_body='plain',
                in_notes='retired   drop_blocks node-table — WHY-X')
    # TOOL-aDistilledCharter-9, T6: a template at this engine's major carrying a legacy fence is
    # refused, against the SHIPPED descriptor, so the arm fails the day a block loses its legacy mark.
    with tempfile.TemporaryDirectory() as td:
        tgt = Path(td)
        (tgt / '.governance').mkdir()
        (tgt / 'TPL.md').write_text(f'<!-- governance-template: v{TEMPLATE_MAJOR}.0 -->\n'
                                    '<!-- when:node-table -->\nrow\n<!-- /when:node-table -->\n',
                                    encoding='utf-8')
        (tgt / '.governance' / 'deploy.toml').write_text(
            'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "TPL.md"\n', encoding='utf-8')
        here = Path(__file__).resolve().parent
        try:
            render(here, here.parent.parent, tgt)
            got = 'no refusal'
        except Refusal as e:
            got = str(e)
    check_arm('a legacy block kept only for older' in got,
              'a current-major template carrying a legacy fence is refused', f'got {got!r}')
    # PLAY-dOrderedCharter-41 S4: `cross-os` stays a live block, so gov's own template and a seeded
    # previous-minor one each render against the SHIPPED declarations, with and without the member, each
    # in a target committed on `main`. Both carry the `cross-os` fence, so a `legacy` mark on the shipped
    # row reds every render here.
    gov_root = here.parent.parent
    gov_tpl, gov_dep = resolve_template_path(gov_root, here, {}), gov_root / '.governance' / 'deploy.toml'
    seeded = (f'<!-- governance-template: v{TEMPLATE_MAJOR}.4 -->\n\n- [one] Kept.\n<!-- when:cross-os -->\n'
              f'- [cross-os] Across operating systems.\n<!-- /when:cross-os -->\n{CROSS_OS_FENCE}')
    halves = [('a seeded previous-minor template', seeded,
               'kits = ["playbook"]\n\n[answers]\nplaybook_path = "TPL.md"\n')]
    if gov_tpl.is_file() and gov_dep.is_file():
        # Section 4 Evidence's narrowing: the two playbook kits, and answers for the probes they ask.
        narrowed = re.sub(r'(?ms)^kits = \[.*?\]\n', 'kits = ["playbook", "playbook-render"]\n',
                          gov_dep.read_text(encoding='utf-8'), count=1).replace(
            '[answers]\n', '[answers]\nplaybook_path = "TPL.md"\nci_file = "none"\ngate_runner = "none"\n'
            'id_families = "none"\nmemory_disciplines = "none"\n', 1)
        halves.insert(0, ("gov's template", gov_tpl.read_text(encoding='utf-8'), narrowed))
    else:
        print(f'  unarmed: gov\'s template half — {gov_tpl.as_posix()} or {gov_dep.as_posix()} is not '
              f'here, so this install holds no gov template above the engine')
    was = os.environ.pop('GOV_DEFAULT_BRANCH', None)
    try:
        for name, tpl, dep in halves:
            for drop in ('', 'drop_blocks = ["cross-os"]\n'):
                with tempfile.TemporaryDirectory() as td:
                    tgt = Path(td)
                    (tgt / '.governance').mkdir()
                    (tgt / '.governance' / 'deploy.toml').write_text(drop + dep, encoding='utf-8')
                    (tgt / 'TPL.md').write_text(tpl, encoding='utf-8')
                    read_git(tgt, 'init', '-q', '-b', 'main')
                    read_git(tgt, 'add', '-A')
                    read_git(tgt, '-c', 'user.name=fx', '-c', 'user.email=fx@example.invalid',
                             '-c', 'commit.gpgsign=false', 'commit', '-qm', 'fixture')
                    try:
                        render(here, gov_root, tgt)
                        got = None
                    except Refusal as e:
                        got = str(e)
                check_arm(got is None, f'{name} renders {"with" if drop else "without"} drop_blocks cross-os',
                          f'refused with {got!r}')
    finally:
        if was is not None:
            os.environ['GOV_DEFAULT_BRANCH'] = was
    # TOOL-aDistilledCharter-2 rev-2 (closing review round 1, R1). A SEEDED v3.x template renders
    # under THIS engine and its SHIPPED declarations, because `update` never rewrites a seed and a
    # refusal here rolls the kit back. The declarations are the real ones beside this engine, so the
    # arm fails the day a legacy name leaves the descriptor.
    real_engine = Path(__file__).resolve().parent
    v3 = ('<!-- governance-template: v3.5 -->\n<!-- when:node-table -->\n'
          '| `{{TAG_A}}` | `{{MACHINE_A}}` | `{{PRIMARY_TREE_A}}` | `{{WORKTREE_ROOT_A}}` | '
          '{{VARIANCES_A}} |\n<!-- /when:node-table -->\n<!-- when:security-outbound -->\nSSRF\n'
          '<!-- /when:security-outbound -->\naudit {{PROSE_AUDIT}}\n')
    for drops, want_row in (('', True), ('drop_blocks = ["node-table"]\n', False)):
        with tempfile.TemporaryDirectory() as td:
            tgt = Path(td)
            (tgt / '.governance').mkdir()
            (tgt / 'TPL.md').write_text(v3, encoding='utf-8')
            (tgt / '.governance' / 'deploy.toml').write_text(
                'kits = ["lexicon"]\n' + drops + '\n[answers]\nplaybook_path = "TPL.md"\n'
                'machine_a = "u"\nprimary_tree_a = "C:/p/x"\nworktree_root_a = "C:/p/x/w"\n'
                'variances_a = "none"\n', encoding='utf-8')
            try:
                body, notes = render(real_engine, real_engine.parent.parent, tgt)
                err = None
            except Refusal as e:
                body, notes, err = '', [], str(e)
        check_arm(err is None and ('`C:/p/x`' in body) == want_row and 'SSRF' in body
                  and any('reseed' in n for n in notes),
                  f'a v3.x template renders under the shipped declarations '
                  f'({"node-table dropped" if drops else "every block kept"}) and notes a reseed',
                  f'refused: {err}' if err else f'body {body!r} notes {notes!r}')
    import contextlib
    import io
    for outside, want_note in (('## Node registry\n\n| `a` | `u` |\n\n', True), ('# head\n\n', False)):
        with tempfile.TemporaryDirectory() as td:
            tgt = Path(td)
            (tgt / '.governance').mkdir()
            (tgt / '.governance' / 'deploy.toml').write_text(
                'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "TPL.md"\n', encoding='utf-8')
            (tgt / 'TPL.md').write_text('x\n', encoding='utf-8')
            (tgt / 'AGENTS.md').write_text(f'{outside}{REGION_OPEN}\nx\n{REGION_CLOSE}\n',
                                           encoding='utf-8')
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                rc = main(['--target', str(tgt), '--check'])
        check_arm(rc == 0 and ('Node registry' in out.getvalue()) == want_note,
              f'the stale-registry note prints {"when" if want_note else "only when"} a registry '
              f'sits outside the region', f'rc {rc} out {out.getvalue()!r}')

    # TOOL-aDistilledCharter-8 — N2: `checkout_dir` names the clone when the product is named apart;
    # N5: `--check` prints the reseed note; N6: a v4 template naming a legacy placeholder is refused.
    body, err = build_node_render(build_fleet_text(fleet_rows), 'checkout_dir = "app/main"\n',
                                  name='App')
    check_arm(err is None and '`C:/p/app/main`' in body and '`C:/p/App`' not in body,
              'checkout_dir names the clone where the product name differs', f'{err!r} {body!r}')
    for marker_v, want in (('v3.5', 'reseed'), ('v4.0', 'legacy v3 placeholder')):
        with tempfile.TemporaryDirectory() as td:
            tgt = Path(td)
            (tgt / '.governance').mkdir()
            (tgt / 'TPL.md').write_text(f'<!-- governance-template: {marker_v} -->\n'
                                        f'tag {{{{TAG_A}}}}\n', encoding='utf-8')
            (tgt / '.governance' / 'deploy.toml').write_text(
                'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "TPL.md"\n', encoding='utf-8')
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                main(['--target', str(tgt)])   # write mode first; its notes are not the observation
            out, err_out = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err_out):
                rc = main(['--target', str(tgt), '--check'])
        said = out.getvalue() + err_out.getvalue()
        check_arm(want in said and (rc == 0) == (marker_v == 'v3.5'),
                  f'a {marker_v} template naming a legacy placeholder: --check '
                  f'{"prints the reseed note" if marker_v == "v3.5" else "refuses it"}',
                  f'rc {rc}, said {said!r}')

    # TOOL-aDistilledCharter-7 — R5: DEL is refused and the fleet is untouched; R7: a [charter] value
    # carrying a one-line marker is refused; R8: `--answers` agrees with the render; R6: an inherited
    # GIT_DIR does not steer a probe at the ambient repository.
    with tempfile.TemporaryDirectory() as td:
        eng = Path(td)
        (eng / FLEET_NAME).write_text(build_fleet_text(fleet_rows), encoding='utf-8')
        before = (eng / FLEET_NAME).read_bytes()
        try:
            write_fleet_claim(eng, 'eve', 'H3', 'C:/p', 'quirk' + chr(127))
            got = 'no refusal'
        except Refusal as e:
            got = str(e)
        after = (eng / FLEET_NAME).read_bytes()
    check_arm('control character' in got and before == after,
              'a claim carrying DEL is refused and leaves the fleet registry untouched',
              f'got {got!r}, file changed {before != after}')
    arm_fixture('a [charter] value carrying a one-line marker is refused', rules_desc,
                region % '{{ADOPTER_RULES}}',
                f'[charter]\nadopter_rules = """\n- ok\n{ONE_LINE_CLOSE}\nfree prose\n"""' + ans,
                want='carries a one-line region marker')
    with tempfile.TemporaryDirectory() as td:
        eng, tgt = _write_fixture(Path(td), ok_kits, ok_var)
        (eng / 'playbook.kit.toml').write_text(trailer_desc, encoding='utf-8')
        dep = tgt / '.governance' / 'deploy.toml'
        dep.write_text(dep.read_text(encoding='utf-8')
                       + '\n[charter]\ncommit_trailer = """\nTRAILER\n"""\n', encoding='utf-8')
        got = resolve_answers(eng, Path(td), tgt, ['commit_trailer'])
    check_arm(got == {'commit_trailer': 'TRAILER'},
              '--answers strips a multi-line value exactly as the render does', f'got {got!r}')
    ambient = read_git(Path(__file__).resolve().parent, 'rev-parse', '--absolute-git-dir')
    if not ambient:
        print('  arm SKIP an inherited GIT_DIR does not steer a probe — this engine sits in no git '
              'repository, so there is no ambient one to leak')
    else:
        saved = os.environ.get('GIT_DIR')
        os.environ['GIT_DIR'] = ambient
        try:
            with tempfile.TemporaryDirectory() as td:
                seen = derive_primary_tree(Path(td), {})
                want = Path(td).resolve().as_posix()
        finally:
            if saved is None:
                os.environ.pop('GIT_DIR', None)
            else:
                os.environ['GIT_DIR'] = saved
        check_arm(seen == want, 'an inherited GIT_DIR does not steer a probe at the ambient repository',
                  f'derived {seen!r}, wanted {want!r}')

    # S3 / AC5 — the template is never its own charter. Driven through `main`, so the exit code is
    # the one an operator sees, over gov's own declarations and a real registry entry.
    import contextlib
    import io
    with tempfile.TemporaryDirectory() as td:
        tgt = Path(td)
        (tgt / '.governance').mkdir()
        (tgt / '.governance' / 'deploy.toml').write_text(
            'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "AGENTS.md"\n', encoding='utf-8')
        (tgt / 'AGENTS.md').write_text('{{PROJECT_NAME}}\n', encoding='utf-8')
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            rc = main(['--target', str(tgt)])
        left = (tgt / 'AGENTS.md').read_text(encoding='utf-8')
        if rc == 1 and 'are one file' in err.getvalue() and left == '{{PROJECT_NAME}}\n':
            passed += 1
        else:
            failed += 1
            print(f'  arm FAIL a template that is its own charter is refused — rc {rc}, '
                  f'{err.getvalue()!r}, file now {left!r}')

    # PLAY-dOrderedCharter-12 S5 — the render writes its provenance to the lock, never into the charter:
    # the rendered charter carries no version marker and the lock's charter row carries it.
    import instruction_units
    with tempfile.TemporaryDirectory() as td:
        tgt = Path(td)
        (tgt / '.governance').mkdir()
        (tgt / '.governance' / 'deploy.toml').write_text(
            'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "TPL.md"\n', encoding='utf-8')
        (tgt / 'TPL.md').write_text(f'<!-- governance-template: v{TEMPLATE_MAJOR}.4 -->\n\nplain\n',
                                    encoding='utf-8')
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = main(['--target', str(tgt)])
        left = (tgt / 'AGENTS.md').read_text(encoding='utf-8') if rc == 0 else ''
        rows = instruction_units.read_lock(tgt) if rc == 0 else []
    check_arm(rc == 0 and 'plain' in left and not TEMPLATE_MARKER_RE.search(left)
              and [r.get('template') for r in rows] == [f'TPL.md@v{TEMPLATE_MAJOR}.4'],
              'the rendered charter carries no version marker and the lock row carries it',
              f'rc {rc}, charter {left!r}, lock rows {rows!r}')

    # TOOL-aRepatriatedFork-42 — `--answers` states what `render` would use, and grades `kits` alike.
    with tempfile.TemporaryDirectory() as td:
        eng, tgt = _write_fixture(Path(td), ok_kits, ok_var)
        (eng / 'playbook.kit.toml').write_text(
            DESC_FIXTURE + '\n[[placeholder]]\nkey = "GATE_RUNNER"\nclass = "derived"\n'
            'probe = "gate_runner"\n', encoding='utf-8')
        dep = tgt / '.governance' / 'deploy.toml'
        dep.write_text('gov_source = "../gov"\n' + dep.read_text(encoding='utf-8')
                       + 'gate_runner = "bash scripts/gate.sh"\nmanifest_path = "m.md"\n',
                       encoding='utf-8')
        got = resolve_answers(eng, Path(td), tgt, ['GATE_RUNNER', 'kits', 'manifest_path',
                                                   'gov_source', 'nope'])
        want = {'GATE_RUNNER': 'bash scripts/gate.sh', 'kits': two_kits,
                'manifest_path': 'm.md', 'gov_source': '../gov', 'nope': None}
        dep.write_text(dep.read_text(encoding='utf-8').replace('"lexicon"', '"lexcon"'),
                       encoding='utf-8')
        try:
            resolve_answers(eng, Path(td), tgt, ['kits'])
            graded = False
        except Refusal as e:
            graded = 'not a registry entry id' in str(e)
    if got == want and graded:
        passed += 1
    else:
        failed += 1
        print(f'  arm FAIL --answers agrees with render — got {got!r}, kits graded {graded}')

    # TOOL-aRepatriatedFork-42 rev-3 (C4, C6) — one answer whatever the spelling, and govkit's
    # per-entry overlay: `[kit.<entry>]` over `[answers]`, falling back to it, null when neither says.
    with tempfile.TemporaryDirectory() as td:
        eng, tgt = _write_fixture(Path(td), ok_kits, ok_var)
        (eng / 'playbook.kit.toml').write_text(
            DESC_FIXTURE + '\n[[placeholder]]\nkey = "GATE_RUNNER"\nclass = "derived"\n'
            'probe = "gate_runner"\n', encoding='utf-8')
        (tgt / '.governance' / 'deploy.toml').write_text(
            'gov_source = "../gov"\nkits = ' + ok_kits + '\n\n[answers]\n'
            'playbook_path = "CHARTER.md"\nvariances_a = "plain"\nGate_Runner = "bash g.sh"\n'
            'manifest_path = "m.md"\n\n[kit.kickoff-manifest]\nManifest_Path = "x.md"\n',
            encoding='utf-8')
        keys = ['gate_runner', 'GATE_RUNNER', 'KITS', 'Manifest_Path', 'GOV_SOURCE',
                'kit.kickoff-manifest.manifest_path', 'KIT.Kickoff-Manifest.MANIFEST_PATH',
                'kit.memory-tree.manifest_path', 'kit.kickoff-manifest.nope']
        got = resolve_answers(eng, Path(td), tgt, keys)
    want = dict(zip(keys, ['bash g.sh', 'bash g.sh', two_kits, 'm.md', '../gov',
                           'x.md', 'x.md', 'm.md', None]))
    if got == want:
        passed += 1
    else:
        failed += 1
        print(f'  arm FAIL --answers is case-insensitive and applies the per-entry overlay — '
              f'got {got!r}')

    # TOOL-aRepatriatedFork-38 — a conf value keeps no trailing comment, quoted or not.
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / '.memory-tree.conf').write_text(
            'MEMORY_ROOT="mem ory"   # note\nFAMILIES=TOOL   # note\n'
            # rev-3 (C4): a `#` opening the word is data; whitespace after `=` ends it.
            'HASHED=#x\nBLANKED=   # note\n', encoding='utf-8')
        got = tuple(read_conf(Path(td), '.memory-tree.conf', k)
                    for k in ('MEMORY_ROOT', 'FAMILIES', 'HASHED', 'BLANKED'))
    if got == ('mem ory', 'TOOL', '#x', ''):
        passed += 1
    else:
        failed += 1
        print(f'  arm FAIL a conf value keeps no trailing comment — got {got!r}')

    # TOOL-aRepatriatedFork-29 AC6 — the bar fallback probes the TARGET's kit root, not a fixed list:
    # a runner under `vendor/gov/run-gates/` with no receipt renders that path, and two candidate
    # roots render nothing rather than a guess.
    kit_home, kit_anchor = 'run-gates', 'run-gates.sh'
    with tempfile.TemporaryDirectory() as td:
        tgt = Path(td) / 'tgt'
        for n, base in enumerate((('vendor', 'gov'), ('alt',))):
            kd = tgt.joinpath(*base, kit_home)
            kd.mkdir(parents=True)
            (kd / kit_anchor).write_text('#!/bin/sh\n', encoding='utf-8')
            if n == 0:
                one = derive_gate_runner(tgt, {})
        two = derive_gate_runner(tgt, {})
    if one == f'bash vendor/gov/{kit_home}/{kit_anchor}' and two == '':
        passed += 1
    else:
        failed += 1
        print(f'  arm FAIL the bar fallback probes the target kit root — got {one!r} then {two!r}')

    # TOOL-aRepatriatedFork-29 AC11 (closing review round 1 M1) — a FLAT runner under the prefix the
    # target's deploy.toml declares at its top level, which is where intake writes it. One arm per
    # flat candidate main used to find; `7de665e5` read the prefix out of `[answers]` and rendered none.
    # The third prefix is this engine's own tool root, DERIVED: typed, it is a kit-path literal.
    flat = []
    own_root = Path(__file__).resolve().parent.parent.name
    for pfx, rel in (('scripts', 'gate.sh'), ('scripts', kit_anchor), (own_root, kit_anchor)):
        with tempfile.TemporaryDirectory() as td:
            tgt = Path(td) / 'tgt'
            (tgt / '.governance').mkdir(parents=True)
            (tgt / '.governance' / 'deploy.toml').write_text(f'prefix = "{pfx}"\n', encoding='utf-8')
            (tgt / pfx).mkdir()
            (tgt / pfx / rel).write_text('#!/bin/sh\n', encoding='utf-8')
            flat.append((derive_gate_runner(tgt, read_deploy(tgt)[2]), f'bash {pfx}/{rel}'))
    if all(got == want for got, want in flat):
        passed += 1
    else:
        failed += 1
        print(f'  arm FAIL a flat runner under the top-level deploy prefix renders — got {flat!r}')

    # TOOL-aOrientedCast-18 — `{{ROLE_ROSTER}}` is the roles kit's `roster` verb, verbatim. The stub
    # verb sits at td/<home>/<anchor>, found through the resolver's second probe from the target's
    # root; `home` and `anchor` are joined at run time, never spelled as one path. The stub drops a
    # `ran` sentinel beside itself, so the unreached arm's "no sentinel" is proved against a stub the
    # kept-fence arm has already seen run.
    home, anchor = 'roles', 'handoff.py'
    bullets = ('- `gov-a`: the first stub role.', '- `gov-b`: the second stub role.')
    current_tpl = (f'<!-- governance-template: v{TEMPLATE_MAJOR}.4 -->\n<!-- kit:{home} -->\n'
                   f'{ONE_LINE_OPEN}\n{{{{ROLE_ROSTER}}}}\n{ONE_LINE_CLOSE}\n<!-- /kit:{home} -->\n')
    older_tpl = '<!-- governance-template: v3.5 -->\nno roster here\n'

    def write_roster_fixture(td: Path, kit: str, tpl: str, stub: str | None,
                             answered: bool = False) -> tuple[Path, Path, Path]:
        """Write the engine, target and stub verb; `stub` is 'ok', 'fail' or None for no kit."""
        eng, tgt = td / 'engine', td / 'target'
        eng.mkdir()
        (tgt / '.governance').mkdir(parents=True)
        (eng / 'playbook.kit.toml').write_text(
            '[[placeholder]]\nkey = "ROLE_ROSTER"\nclass = "derived"\nprobe = "role_roster"\n'
            f'kit = "{home}"\n', encoding='utf-8')
        (eng / 'registry.toml').write_text(f'[[entry]]\nid = "{home}"\n\n[[entry]]\nid = "lexicon"\n',
                                           encoding='utf-8')
        (tgt / 'CHARTER.md').write_text(tpl, encoding='utf-8')
        (tgt / '.governance' / 'deploy.toml').write_text(
            f'kits = ["{kit}"]\n\n[answers]\nplaybook_path = "CHARTER.md"\n'
            + ('role_roster = "- answered"\n' if answered else ''), encoding='utf-8')
        kd = td / home
        if stub:
            kd.mkdir()
            tail = ("print('stub: no role file to read', file=sys.stderr)\nsys.exit(1)\n"
                    if stub == 'fail' else ''.join(f'print({b!r})\n' for b in bullets))
            (kd / anchor).write_text('import sys\nfrom pathlib import Path\n'
                                     "(Path(__file__).parent / 'ran').write_text('x')\n" + tail,
                                     encoding='utf-8')
        return eng, tgt, kd / 'ran'

    seen = {}   # case -> (body, notes, refusal or None, whether the stub ran, captured stderr)
    for case, kit, tpl, stub, answered in (('kept', home, current_tpl, 'ok', False),
                                           ('pruned', 'lexicon', current_tpl, 'ok', False),
                                           ('older', home, older_tpl, 'ok', False),
                                           ('failing', home, current_tpl, 'fail', False),
                                           ('answered', home, current_tpl, 'fail', True),
                                           ('absent', home, current_tpl, None, False)):
        with tempfile.TemporaryDirectory() as td:
            eng, tgt, ran = write_roster_fixture(Path(td), kit, tpl, stub, answered)
            err = io.StringIO()
            try:
                with contextlib.redirect_stderr(err):
                    body, notes = render(eng, Path(td), tgt)
                got = None
            except Refusal as e:
                body, notes, got = '', [], str(e)
            seen[case] = (body, notes, got, ran.is_file(), err.getvalue())

    body, _n, got, ran, _s = seen['kept']
    check_arm(got is None and ran and f'{ONE_LINE_OPEN}\n{bullets[0]}\n{bullets[1]}\n{ONE_LINE_CLOSE}'
              in body, 'a kept roles fence carries the roster verb\'s lines verbatim in its region',
              f'refused {got!r}, stub ran {ran}, body {body!r}')
    unreached = [seen['pruned'], seen['older']]
    check_arm(all(g is None and not r and not any(b in bd for b in bullets)
                  for bd, _n, g, r, _s in unreached),
              'the roster verb never runs for a pruned fence or a token-less v3.5 template',
              f'(refused, stub ran) per case {[(g, r) for _b, _n, g, r, _s in unreached]}')
    _b, _n, got, _r, said = seen['failing']
    abody, anotes, agot, _r2, _s2 = seen['answered']
    check_arm(got is not None and 'ROLE_ROSTER' in got and 'role_roster' in got
              and 'render-playbook: ROLE_ROSTER:' in said and 'stub: no role file to read' in said
              and agot is None and '- answered' in abody
              and any(n.startswith('answered  ROLE_ROSTER') and n.endswith('(probe derives nothing)')
                      for n in anotes),
              'a failing roster verb prints its reason and refuses, and an answer outranks it',
              f'refused {got!r}, stderr {said!r}; answered: refused {agot!r}, notes {anotes!r}')
    _b, _n, got, _r, said = seen['absent']
    check_arm(got is not None and 'ROLE_ROSTER' in got
              and 'render-playbook: ROLE_ROSTER:' in said and 'looked in' in said,
              'an absent roles kit prints the resolver\'s reason and refuses',
              f'refused {got!r}, stderr {said!r}')
    check_scope_arms(check_arm)
    check_practice_arms(check_arm)

    if failed:
        print(f'render_playbook.selftest FAILED — {failed} of {passed + failed} arm(s)')
        return 1
    print(f'render_playbook.selftest OK — {passed} arm(s)')
    return 0


def derive_entry_aliases(target: Path, aliases: str | None) -> list[str]:
    """The aliases of the `entry-files` scope: `--aliases`, else those of `renderers.toml`'s row for it."""
    if aliases is not None:
        return aliases.split()
    names = {path: name for name, path in ALIAS_PATHS.items()}
    return [names[p] for r in load_units_module().read_renderers(target)
            if r['renderer'] == 'playbook:entry-files' for p in r['paths'] if p in names]


def check_gemini_configured(target: Path) -> bool:
    path = target / GEMINI_SETTINGS
    return path.is_file() and bool(GEMINI_CONFIGURED_RE.search(path.read_text(encoding='utf-8', errors='replace')))


def check_import_line(path: Path) -> bool:
    return bool(IMPORT_LINE_RE.search(path.read_text(encoding='utf-8', errors='replace')))


def check_same_bytes(target: Path, path: Path) -> bool:
    return path.read_bytes() == (target / CANON).read_bytes()


def check_link_target(path: Path) -> bool:
    return Path(os.readlink(path)).name == CANON


def check_entry_files(target: Path, aliases: list[str]) -> int:
    """The `entry-files` scope's compare: each alias a live link, a pointer, a copy of the canonical's bytes
    or, for gemini, its configured settings file."""
    if not (target / CANON).is_file():
        print(f'AGENT-INSTR CHECK FAILED — no canonical {CANON}')
        return 1
    reds = []
    for name in aliases:
        rel = ALIAS_PATHS.get(name)
        path = target / rel if rel else None
        if path is None:
            reds.append(f"unknown alias '{name}'")
        elif name == 'gemini' and not os.path.lexists(path):
            if not check_gemini_configured(target):
                reds.append(f'gemini: neither GEMINI.md nor {GEMINI_SETTINGS} context.fileName={CANON}')
        elif path.is_symlink():
            if not path.exists():
                reds.append(f'{rel} is a DANGLING symlink → {os.readlink(path)}')
            elif not check_link_target(path):
                reds.append(f"{rel} symlinks '{os.readlink(path)}', not {CANON}")
        elif not path.exists():
            reds.append(f"{name} alias '{rel}' missing")
        elif not (check_import_line(path) or check_same_bytes(target, path)):
            reds.append(f'{rel} is a stale copy — re-run with --force to re-sync from {CANON} (or it drifted)')
    for why in reds:
        print(f'AGENT-INSTR CHECK FAILED — {why}')
    if not reds:
        print(f'agent-instructions OK — {CANON} + aliases [{" ".join(aliases)}] correctly wired.')
    return 1 if reds else 0


def write_pointer_or_copy(target: Path, name: str, rel: str, back: str) -> None:
    """A claude alias's `@<canonical>` import, any other alias's copy of the canonical's bytes."""
    path = target / rel
    path.unlink(missing_ok=True)
    if name == 'claude':
        path.write_bytes(f'@{back}\n'.encode('utf-8'))
        print(f'  + {rel} (@{back} import)')
    else:
        shutil.copyfile(target / CANON, path)
        print(f'  + {rel} (copy — no native pointer; drift re-syncs with --force)')


def write_entry_file(target: Path, name: str, mode: str, force: bool) -> str | None:
    """One alias wired, or found wired, returning the file its lock row names; None on a refusal it printed."""
    def print_refusal(why: str) -> None:
        print(f'AGENT-INSTR wire FAILED — {why}')

    rel = ALIAS_PATHS.get(name)
    if rel is None:
        return print_refusal(f"unknown alias '{name}'")
    path = target / rel
    held = os.path.lexists(path)
    if name == 'gemini' and not held and check_gemini_configured(target):
        print(f'  = {GEMINI_SETTINGS} (context.fileName, current)')
        return GEMINI_SETTINGS
    if path.is_symlink():
        if path.exists() and check_link_target(path):
            print(f'  = {rel} (symlink, current)')
            return rel
    elif path.is_file() and check_import_line(path):
        print(f'  = {rel} (pointer, current)')
        return rel
    elif path.is_file() and check_same_bytes(target, path):
        print(f'  = {rel} (copy, current)')
        return rel
    if held and not force:
        return print_refusal(f'{rel} exists and is not {CANON} wiring — pass --force to replace it')
    path.parent.mkdir(parents=True, exist_ok=True)
    back = '../' * rel.count('/') + CANON
    if name == 'gemini' and mode == 'pointer':
        settings = target / GEMINI_SETTINGS
        if settings.is_file():
            return print_refusal(f'gemini: {GEMINI_SETTINGS} exists without context.fileName={CANON} — merge '
                                 f'"context":{{"fileName":"{CANON}"}} in by hand (JSON can\'t be safely auto-merged)')
        settings.parent.mkdir(parents=True, exist_ok=True)
        settings.write_bytes(f'{{\n  "context": {{\n    "fileName": "{CANON}"\n  }}\n}}\n'.encode('utf-8'))
        print(f'  + {GEMINI_SETTINGS} (context.fileName={CANON})')
        return GEMINI_SETTINGS
    if mode == 'symlink':
        path.unlink(missing_ok=True)
        try:
            os.symlink(back, path)
            linked = path.exists()
        except OSError:
            linked = False
        if linked:
            print(f'  + {rel} → {back} (symlink)')
            return rel
        print('  ! symlink unavailable/dangling (Windows Developer Mode?) — falling back')
        write_pointer_or_copy(target, name, rel, back)
    elif mode == 'copy':
        path.unlink(missing_ok=True)
        shutil.copyfile(target / CANON, path)
        print(f'  + {rel} (copy — drift re-syncs with --force)')
    else:
        write_pointer_or_copy(target, name, rel, back)
    return rel


def run_entry_files(target: Path, aliases: list[str], mode: str, force: bool) -> int:
    """The `entry-files` scope's write: each alias wired, its lock row recorded; 1 when one refused."""
    if not (target / CANON).is_file():
        raise Refusal(f'no {CANON} to wire: render the charter, or give the adopter a --source')
    iu, rc = load_units_module(), 0
    for name in aliases:
        rel = write_entry_file(target, name, mode, force)
        if rel is None:
            rc = 1
        else:
            iu.write_lock_row(target, rel, derive_renderer_label(), '')
    return rc


def run_claims_scope(target: Path) -> int:
    """The `claims` scope: the parity gate's three arms, run where the tree under check holds it."""
    gate = target / load_units_module().derive_kit_prefix() / PARITY_GATE
    bash = resolve_bash(gate) if gate.is_file() else None
    if bash is None:
        print(f'render-playbook: red · claims · no bash ran {gate.as_posix()} · remedy: the claims scope is gov\'s '
              f'and needs that gate')
        return 1
    sys.stdout.flush()
    return subprocess.run([bash, gate.as_posix()], cwd=target, stdin=subprocess.DEVNULL).returncode


def run_check_render(engine_dir: Path, gov_root: Path, target: Path, charter_path: Path,
                     scope: str | None, aliases: str | None) -> int:
    """`--check-render`: one scope's compare, or with no scope the render gate: every scope, each instruction
    file's one renderer of record, the status arm, and the legacy list under `instructions.legacy`."""
    if scope == 'entry-files':
        return check_entry_files(target, derive_entry_aliases(target, aliases))
    if scope == 'claims':
        return run_claims_scope(target)
    iu = load_units_module()
    from policy_value import PolicyRefused, read_policy_value
    rc = max(run_charter_scope(engine_dir, gov_root, target, charter_path, True),
             check_entry_files(target, derive_entry_aliases(target, aliases)), run_claims_scope(target))
    reds = iu.check_renderers(target)
    try:
        iu.read_change_records(target)
    except iu.UnitRowError as e:
        reds.append(f'render-playbook: red · status · {e}')
    try:
        reds += iu.check_legacy(target, read_policy_value("instructions.legacy", target)[0][0])
    except PolicyRefused as e:
        reds.append(f'render-playbook: red · instructions.legacy · {e.line} · remedy: repair the committed '
                    f'policy file; a refused read grades under no default')
    for red in reds:
        print(red)
    print(f'render-playbook: gate · {len(reds)} red in the table, the status arm and the legacy list')
    return rc or (1 if reds else 0)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--target')
    ap.add_argument('--charter', default='AGENTS.md')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    # TOOL-aRepatriatedFork-42: another kit's renderer asks for the answers this engine would use.
    ap.add_argument('--answers', nargs='+', metavar='KEY')
    # TOOL-aDistilledCharter-2: a new node claims its tag once, in gov's own checkout.
    ap.add_argument('--claim-node', action='store_true')
    ap.add_argument('--user', default='')
    ap.add_argument('--host', default='')
    ap.add_argument('--projects-root', default='')
    ap.add_argument('--variances', default='')
    # PLAY-dOrderedCharter-20: the one renderer's scopes, and the entry-files scope's three inputs.
    ap.add_argument('--render-scope', choices=RENDER_SCOPES)
    ap.add_argument('--check-render', action='store_true')
    ap.add_argument('--scope', choices=CHECK_SCOPES)
    ap.add_argument('--aliases')
    ap.add_argument('--mode', choices=('symlink', 'pointer', 'copy'), default='pointer')
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args(argv)
    if a.scope and not a.check_render:
        ap.error('--scope names what --check-render compares')

    if a.selftest:
        return run_selftest()
    if a.claim_node:
        try:
            tag = write_fleet_claim(Path(__file__).resolve().parent, a.user, a.host,
                                    a.projects_root, a.variances)
        except Refusal as e:
            print(f'render-playbook: REFUSED — {e}', file=sys.stderr)
            return 1
        print(f'render-playbook — claimed tag `{tag}` for {a.user} @ {a.host or "<no host>"}; '
              f'commit the fleet registry with the governance charter rendered again beside it; every other '
              f'repository receives it at its next govkit update')
        return 0
    engine_dir = Path(__file__).resolve().parent
    if not a.target and (a.render_scope or a.check_render):
        a.target = read_git(engine_dir, 'rev-parse', '--show-toplevel')
    if not a.target:
        ap.error('--target is required')

    gov_root = engine_dir.parent.parent
    target = Path(a.target).resolve()
    charter_path = target / a.charter

    if a.answers:
        try:
            print(json.dumps(resolve_answers(engine_dir, gov_root, target, a.answers)))
        except Refusal as e:
            print(f'render-playbook: REFUSED — {e}', file=sys.stderr)
            return 1
        return 0

    try:
        if a.check_render and a.scope != 'charter':
            return run_check_render(engine_dir, gov_root, target, charter_path, a.scope, a.aliases)
        if a.render_scope == 'entry-files':
            return run_entry_files(target, derive_entry_aliases(target, a.aliases), a.mode, a.force)
    except (Refusal, ValueError, OSError) as e:   # ValueError: the lock module's LevelError, LockError, UnitRowError
        print(f'render-playbook: REFUSED — {e}', file=sys.stderr)
        return 1
    return run_charter_scope(engine_dir, gov_root, target, charter_path, a.check or a.check_render)


def run_charter_scope(engine_dir: Path, gov_root: Path, target: Path, charter_path: Path, check: bool) -> int:
    """The `charter` scope: write the region and its lock row, or with `check` compare it. `--check` and
    `--check-render --scope charter` are one check."""
    # NOT ADOPTED is exit 0, and only in --check. A wiring leg runs unguarded against a tree that
    # has not run intake yet — gov's own, until its charter is rendered — and a leg that refuses
    # there is red for a reason that is not drift. It says so explicitly rather than passing
    # silently, because a leg green for "nothing was measured" is the shape this repo refuses.
    # Writing without a descriptor still REFUSES: that is an operator asking for a render.
    if check and not (target / '.governance' / 'deploy.toml').is_file():
        print(f'render-playbook: NOT ADOPTED — {target.as_posix()} has no .governance/deploy.toml, '
              f'so no region was rendered here and there is nothing to compare')
        return 0

    slots: list = []
    try:
        body, notes = render(engine_dir, gov_root, target, charter_path, slots)
    except Refusal as e:
        print(f'render-playbook: REFUSED — {e}', file=sys.stderr)
        return 1

    survived = PLACEHOLDER_RE.findall(body)

    # TOOL-aDistilledCharter-2 S6. The kickoff card reads the FIRST `## Node registry` of the
    # charter, so an authored one above the region keeps this repository's old tags in force.
    if charter_path.is_file():
        parts = REGION_MARKER_RE.split(charter_path.read_text(encoding='utf-8'))
        if re.search(r'^## Node registry', parts[0] + (parts[2] if len(parts) > 2 else ''), re.M):
            print('render-playbook: NOTE — the charter carries its own `## Node registry` outside '
                  'the rendered region, and readers take the first one, so this repository still '
                  'reads its old tags. Delete that section to adopt the fleet tags')

    if check:
        rc = 0
        # PARITY and PLACEHOLDER COMPLETENESS are two questions, and a render whose descriptor
        # declares nothing for a key is perfectly in sync while telling the agent to invoke a
        # placeholder's name. They fail separately, with separate messages.
        if not charter_path.is_file():
            print(f'render-playbook: {charter_path.as_posix()} does not exist, so there is no region '
                  f'to compare', file=sys.stderr)
            return 1
        cur = charter_path.read_text(encoding='utf-8')
        want = build_region(cur, body)
        # NORMALISE line endings before comparing. This fleet runs core.autocrlf=true and a charter
        # with no eol attribute holds CRLF in the worktree against an LF blob, so a raw compare
        # mismatches on every line for a reason that has nothing to do with drift.
        if cur.replace('\r\n', '\n') != want.replace('\r\n', '\n'):
            print('render-playbook: DRIFT — the charter region differs from a fresh render',
                  file=sys.stderr)
            rc = 1
        if survived:
            print(f'render-playbook: SURVIVING PLACEHOLDER in the render: '
                  f'{", ".join(sorted(set(survived)))}', file=sys.stderr)
            rc = 1
        # N5: the two notes an adopter must act on print here too. `govkit update` runs the
        # regenerate (unless GOVKIT_RERENDER=0) with its output captured, so `--check` is where they are seen.
        for n in notes:
            if n.startswith(('legacy', 'retired')):
                print(f'  {n}')
        if rc == 0:
            print(f'render-playbook OK — region matches a fresh render, no placeholder survived')
        return rc

    if survived:
        print(f'render-playbook: REFUSED — placeholders survived the render: '
              f'{", ".join(sorted(set(survived)))}', file=sys.stderr)
        return 1
    write_region(charter_path, body)
    try:
        write_charter_lock(gov_root, target, charter_path, slots)
        notes += [f"wrote {p} empty: this kit's checks read an absent list as a refusal"
                  for p in write_empty_lists(target)]
    except (Refusal, ValueError) as e:   # ValueError: the lock module's LevelError and LockError
        print(f'render-playbook: REFUSED — the charter is written but its lock row is not: {e}',
              file=sys.stderr)
        return 1
    for n in notes:
        print(f'  {n}')
    print(f'render-playbook — wrote the gov:playbook region into {charter_path.as_posix()}, its '
          f'provenance into .governance/instructions.lock')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))

KIT_PLAYBOOK_RENDER_VERSION = "1.33"  # gov:kit playbook-render@1.33
