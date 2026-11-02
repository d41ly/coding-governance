#!/usr/bin/env python3
"""upgrade_steps — the upgrade-step kind: the step row, the succession row, their one reader, the
frozen-row check, and the two helpers a step program writes through (TOOL-dSafePassage-1).

    python <prefix>/govkit/upgrade_steps.py list               # every row, ordered, with its commit
    python <prefix>/govkit/upgrade_steps.py list --window      # each translation-window member
    python <prefix>/govkit/upgrade_steps.py frozen [--base <rev>]   # the `step-rows-frozen` leg
    python <prefix>/govkit/upgrade_steps.py fixture isolation [--plant <case>]   # the contract, observed
    python <prefix>/govkit/upgrade_steps.py fixture walk|update [--plant <case>]  # the walk, observed
    python <prefix>/govkit/upgrade_steps.py fixture lock --plant <case>          # the lock's reclaim
    python <prefix>/govkit/upgrade_steps.py fixture rollback|rollback-update [--plant <case>]  # downs

THE ROWS. A kit descriptor's `[[upgrade]]` rows, rows of the same grammar in
`<prefix>/govkit/steps.toml` for surfaces no descriptor owns, and the registry's `[[retired]]`
succession rows. `read_steps` and `read_retired` parse, validate and order every one of them, at a
revision or in the working tree; govkit calls them and parses no row itself. This reader is the rows'
write boundary, so it DENIES BY DEFAULT and a refusal names the file, the row and the key: an
unknown key; an authored `introduced` or `retired`; a placeholder other than `{gov}`, `{target}`,
`{prefix}` and, in a `down` alone, `{to}` (TOOL-dSafePassage-26 S10); an interpreter other than python and bash; a `{gov}/` program git does not track at the
revision read; a duplicate id; a descriptor row whose `<entry>` is not that descriptor's own id, or
a steps-file row whose `<entry>` IS a registry entry; a `surfaces` item that is not
`<class>:<name>`; a `reverted` that is neither `"down-exit"` nor an argv; and a succession row
whose id is still live or whose successor is not.

THE DERIVED COMMIT. A row's introducing commit, and a succession row's retiring commit, is never
typed, because a row cannot name the commit that lands it and any other typed commit copies a fact
git owns. It is the oldest commit on the default branch's first-parent line whose tree holds a row
with that id, else `unlanded`: the declaring files' blobs are read oldest first along that line,
each first-parent commit's change against its first parent, and the walk stops at the first holding
blob, so a commit reached only through a second parent never introduces a row.

THE ORDER is total: landed rows by their introducing commit's first-parent position, then unlanded
rows; within one commit the steps file first, then the descriptors in registry entry order; within
one file, row order.

FROZEN ROWS. `check_frozen` compares every row present at a base on the default branch with the same
id at the head. A removed `[[upgrade]]` row reds unless a `[[retired]]` row at the head names it; an
edited `up`, `down`, `witness`, `resume`, `reverted` or `surfaces` reds; an edited byte of a program a landed
argv names reds; a removed or edited `[[retired]]` row reds. A correction shipped as a new step is
green, and `needs-target` stays mutable. WHAT IT DOES NOT CHECK: what a step program imports, so a
landed step can still change through an import; whether a correction step reverses its defect; and
any row the default branch has not landed.

THE BEFORE-IMAGE. A step's up writes `.governance/steps/<entry>/<slug>.before.json` at the target
first, through `write_before_image`: every path the up will write or remove, its bytes (base64,
null for absent) and the sha256 the up leaves there (null for removed). An existing image is never
overwritten, so a re-run over a killed up computes from the first image and converges. The down,
`write_from_before_image`, restores each path only where it still holds the image's after-hash or
its before bytes, else refuses naming the path and restores nothing, so a later edit is never
discarded silently; then it removes the image. No path an image lists may lie in the target's git
directory, by its spelling or by where it resolves (TOOL-dSafePassage-76). A step program imports
this file by its own path, because the runner's `-I` drops the script directory from `sys.path`.

THE RECEIPT'S `steps` (TOOL-dSafePassage-3). A schema-4 receipt records each step's progress as
`{"id", "introduced", "state"}` rows, `state` applied, failed (adding `failure`) or rolled-back; an
applied row a down stopped on adds a `failure` that opens with an entry of `DOWN_STOP_PREFIXES`
(TOOL-dSafePassage-43), and a rolled-back row carries none. An applied row the walk passed by its
witness alone, its up never spawned, adds `"via": "witness"` (TOOL-dSafePassage-33): only where
the walk-start receipt held no record of it and no before-image exists (TOOL-dSafePassage-40).
`set_step_state` is the only code that mutates the field and `read_step_states` the only code that
parses it; the writer persists nothing.

WHAT A STEP CAN REACH (TOOL-dSafePassage-7). `run_step_isolated` is the one spawn of a step argv:
from gov's checkout root, under an environment built from the `STEP_ENV_KEEP` allowlist and never
from a copy of the parent's, home and temp in a fresh scratch, git's system and global config
unread, `core.hooksPath` an empty directory, `credential.helper` empty and `protocol.ext.allow`
`never` (TOOL-dSafePassage-37) through `GIT_CONFIG_COUNT`, and a leading `python` run `-I`. The target's own config, which that leaves
live, refuses the step before any spawn where it declares a key a `STEP_REFUSED_KEYS` row matches
(TOOL-dSafePassage-24, TOOL-dSafePassage-29), and so does the config of every submodule repository
`read_target_repositories` finds git can enter from the target (TOOL-dSafePassage-30). A row declaring `needs-target = true` is
`attended` and spawns nothing. `check_needs_target` runs a row beside planted target hooks and
modules and reads `isolated`, `breach`, `needs-target` or `attended`; `fixture isolation` observes
all of it, a `-stub` plant swapping one half of the contract inside the fixture process only.

THE WALK (TOOL-dSafePassage-2). `update --write` calls `run_step_walk` over `derive_pending_steps`,
the rows `read_steps` reads at `--to` less those the receipt records applied: each step's witness,
then for one not holding an `interrupted:` row persisted before its up, its up (or its `resume`
after a failed record), its witness again, its writes staged, and `applied`; the first failure stops
the walk and no down runs. A killed run's lock is reclaimed by the next once `check_holder_dead`
reads its holder dead through the process-monitor census, under the guard `<lock>.reclaim`, and the
staging journal `write_staging_line` appends before every index write tells that run's staging from
an operator's. `fixture walk|lock|update` observe it in scratch repositories.

THE REVERSE WALK (TOOL-dSafePassage-4). `update --rollback --to <rev> --write`, and nothing else,
calls `run_reverse_walk` over `derive_reverse_steps`, the rows introduced after `<rev>` that the
receipt records applied or failed, or records nowhere, newest first: per step its down, a
`down interrupted:` failure persisted before the spawn where the receipt can hold it, then `derive_down_verdict`'s judge
(TOOL-dSafePassage-17): the row's `reverted` argv, which must exit 0, or its down's own exit under
`reverted = "down-exit"` or with no before-image at the spawn on a row the receipt records nowhere or
`applied` with `"via": "witness"` (TOOL-dSafePassage-33), else its witness, which must no longer
hold, before the row reads `rolled-back`; the first stop ends the walk, and a re-run resumes there.
A receipt id gov's HEAD no longer declares is refused before any down, but for one a `[[retired]]`
row names that owes no down to `<rev>` (TOOL-dSafePassage-76).
`write_rollback_record` begins `.governance/outbox/update-reverted-<from8>-<to8>.md` before the
first down and finishes it before `update` returns. `fixture rollback|rollback-update` observe it.

GOV FIRST (TOOL-dSafePassage-8). `update --target <gov's own checkout> --write` runs in SOURCE mode:
the same walk over gov's tree, recorded in gov's source-mode receipt, then `check_gov_first`, which
refuses a declared id the receipt does not list and an `applied` step whose witness no longer holds.

Exit 0 clean, 1 a frozen-row finding or no base to compare against, 2 a refused row, an unreadable
revision or a usage error. `fixture isolation` exits 0 green and 1 on a red, a `-stub` plant's,
`needs-target`'s, `breach`'s, `token`'s and every `local-*` and `submodule-*` plant's by design but
`submodule-main-only`, `-ref-named-config` and `-sound-no-nested`, which exit 0; `fixture walk|lock|update|rollback|
rollback-update` exit as the walk, the take, the reverse walk or `update` exits (a refusing
`rollback-update` plant 1), and 1 with `<family>: FAILED` on an unmet expectation.
"""

from __future__ import annotations

import ast
import base64
import functools
import hashlib
import importlib.util
import json
import ntpath
import os
import pathlib
import posixpath
import re
import shlex
import shutil
import signal
import socket
import stat
import subprocess
import sys
import tempfile
import time
import tomllib
from typing import NamedTuple

HERE = pathlib.Path(__file__).resolve().parent
# Run as a program, this module is `__main__`; registering it under its own name means govkit,
# loaded later by `load_govkit`, imports THIS module rather than a second copy, so there is one
# `Refusal` class and every catcher of it catches what this file raises.
if __name__ == "__main__":
    sys.modules.setdefault("upgrade_steps", sys.modules[__name__])

INTERPRETERS = ("python", "bash")
PLACEHOLDER_RE = re.compile(r"\{(?:gov|target|prefix|to)\}")
STEP_KEYS = ("id", "up", "down", "witness", "resume", "reverted", "surfaces", "needs-target")
RETIRED_KEYS = ("id", "successor", "surfaces")
FROZEN_FIELDS = ("up", "down", "witness", "resume", "reverted", "surfaces")
# The `reverted` value under which a down's own exit 0 decides it took effect (TOOL-dSafePassage-17).
DOWN_EXIT = "down-exit"
ID_RE = re.compile(r"([^/\s]+)/([a-z0-9][a-z0-9.-]*)")
SURFACE_RE = re.compile(r"[a-z][a-z0-9-]*:\S.*")
UNLANDED = "unlanded"
STEPS_FILE = "steps.toml"
REGISTRY_FILE = "registry.toml"
IMAGE_DIR = ".governance/steps"
STEP_STATES = ("applied", "failed", "rolled-back")
# The openings of a stopped down's `failure`, the one `failure` an `applied` row may carry
# (TOOL-dSafePassage-43); every down-stop text is built from an entry here, never retyped.
DOWN_STOP_PREFIXES = ("down interrupted:", "down exit ", "witness still holds after down",
                      "reverted check exits ")
# Why an attended row stops either walk: the forward walk records it as the row's failure, the
# reverse walk prints it beside the order that names the down (TOOL-dSafePassage-2 S5, -4 S4).
ATTENDED_STOP = "attended: the step needs the target's code"
# The suffix of a forward-walk step line whose verdict the receipt cannot hold, being below schema 4
# (TOOL-dSafePassage-15 S2): the verdict is output, and a stop is still a finding of `update`.
NOT_RECORDED_SUFFIX = "(not recorded: receipt below schema 4)"
# The reverse walk's stop at a down that lowers the receipt before its last row, whose later downs
# could not be recorded (TOOL-dSafePassage-18 S3).
LOWERED_STOP = "receipt below schema 4 before the last down"
SHA_RE = re.compile(r"[0-9a-f]{40}")
OID_RE = re.compile(r"[0-9a-f]{40}(?:[0-9a-f]{24})?")  # a blob oid, sha-1 or sha-256
# The host a write lock and a reclaim guard name (TOOL-dSafePassage-2 S6): a holder is judged dead
# only on the host whose process table can see it.
THIS_HOST = socket.gethostname()
# THE ISOLATION CONTRACT's allowlist (TOOL-dSafePassage-7): the names process creation and Python's
# start-up need, none carrying a credential. Every other name, `GIT_ENV_LEAKS` and every token
# variable included, falls out because nothing copies it in; a name joins by a reviewed edit.
# `GOV_PYTHON` joins (TOOL-dSafePassage-75): it names the interpreter the resolver tries first, so
# a step resolves the one gov's gates and hooks resolve; it carries no credential, and it is the
# same class of name as `PATH`, which already decides what a step spawns. `GOV_BASH` joins
# (TOOL-dSafePassage-87): it names the bash `resolve_bash` tries first, so the floor stub runs the
# shell the parent's `resolve_shell_argv` ran before TOOL-dSafePassage-82 moved the row to a python
# argv; it carries no credential and is the same class of name as `PATH`.
STEP_ENV_KEEP = ("PATH", "PATHEXT", "SYSTEMROOT", "SYSTEMDRIVE", "WINDIR", "COMSPEC", "OS",
                 "PROCESSOR_ARCHITECTURE", "NUMBER_OF_PROCESSORS", "LANG", "LC_ALL", "TZ",
                 "GOV_PYTHON", "GOV_BASH")
STEP_PHASES = ("up", "down", "witness", "resume", "reverted")
# Where `check_needs_target` gathers canaries: inside the scratch tree it is handed, so a target
# module planted beside the plants can name its own canary by its own path.
CANARY_DIR = ".gk-canaries"
# The remote the isolation plants write and fetch: a name of the fixture's own, never the default's.
FIXTURE_REMOTE = "gk-fixture"
# The install prefix the fixtures lay their scratch gov and target out at, named once so every
# fixture path is joined from names (TOOL-dSafePassage-82 S3); and the parent directory the
# submodule plants put `p` and `x` under, a fixture name whose printed paths the arms assert.
FIXTURE_PREFIX = "tools"
FIXTURE_SUB_HOME = "lib"
# The empty directory a step's `core.hooksPath` names, under its scratch: a name no kit holds.
STEP_HOOKS_DIR = "no-hooks"
# Every client-side hook name git runs; a name git adds later is unplanted until it is listed here.
CLIENT_HOOKS = ("applypatch-msg", "pre-applypatch", "post-applypatch", "pre-commit",
                "pre-merge-commit", "prepare-commit-msg", "commit-msg", "post-commit", "pre-rebase",
                "post-checkout", "post-merge", "pre-push", "pre-auto-gc", "post-rewrite",
                "sendemail-validate", "fsmonitor-watchman", "p4-changelist", "p4-prepare-changelist",
                "p4-post-changelist", "p4-pre-submit", "post-index-change", "reference-transaction")
FIXTURE_PLANTS = ("hook", "hook-stub", "module", "module-stub", "credential", "credential-stub",
                  "needs-target", "breach", "token", "callers", "local-filter", "local-filter-stub",
                  "local-process", "local-process-stub", "local-fsmonitor", "local-fsmonitor-stub",
                  "local-include", "local-include-stub", "local-gpg", "local-gpg-stub",
                  "local-hook", "local-hook-stub", "submodule-filter", "submodule-filter-stub",
                  "submodule-nested", "submodule-nested-stub", "submodule-unpopulated",
                  "submodule-unpopulated-stub", "submodule-unpopulated-worktree",
                  "submodule-unpopulated-worktree-stub", "submodule-main-only",
                  "local-recent-objects-hook", "local-recent-objects-hook-stub", "local-ext-transport",
                  "local-ext-transport-stub", "autocrlf", "autocrlf-local", "local-url-userinfo",
                  "submodule-url-userinfo", "insteadof-userinfo", "http-url-key-userinfo",
                  "submodule-fsmonitor", "submodule-name-differs", "ssh-scheme-bare-user",
                  "proxy-schemeless-userinfo", "insteadof-dotted-userinfo", "submodule-ref-named-config",
                  "submodule-config-malformed", "gitmodules-malformed", "submodule-nested-name-differs",
                  "submodule-name-slashed", "sendemail-identity-cmd", "submodule-format-unknown",
                  "gitmodules-unreadable", "subsection-password-space", "submodule-modules-link-loop",
                  "gitmodules-fifo", "submodule-modules-not-a-directory", "submodule-sound-no-nested",
                  "submodule-modules-link-nested", "submodule-modules-link-outside",
                  "submodule-modules-root-link", "submodule-modules-link-dangling", "gitmodules-symlink")
# The class a step is refused over (TOOL-dSafePassage-29 S1): every key of the target's own config
# git runs as a program or sends as a credential, as (key pattern, value rule, what runs it). A
# pattern matches case-insensitively on the key git prints, its `<x>` any one or more segments; a
# value rule is `any`, `not a git false`, `begins with !` or `an absolute path`, git-send-email's
# own test (`/` or a drive letter, `C:` alone included), `\` too. selftest's class arm holds it, with
# `STEP_UNREFUSED_KEYS`, to every executor-shaped key `git help --config` lists.
STEP_REFUSED_KEYS = (
    ("filter.<x>.clean", "any", "add, checkout, status"),
    ("filter.<x>.smudge", "any", "add, checkout, status"),
    ("filter.<x>.process", "any", "add, checkout, status"),
    ("core.fsmonitor", "not a git false", "an index refresh"),
    ("diff.external", "any", "diff, log -p"),
    ("diff.<x>.textconv", "any", "diff, log -p"),
    ("diff.<x>.command", "any", "diff, log -p"),
    ("core.sshCommand", "any", "a fetch or a push"),
    ("core.askPass", "any", "a fetch or a push"),
    ("http.extraHeader", "any", "sent as a credential"),
    ("http.<x>.extraHeader", "any", "sent as a credential"),
    # A remote's `url`, a proxy and a credential-file key are graded by `test_credential_bearing`
    # alone, the one source of the credential class (TOOL-dSafePassage-45 S19).
    ("credential.<x>", "any", "a helper, or a credential setting"),
    ("gpg.program", "any", "a signed commit or tag, log --show-signature, verify-commit"),
    ("gpg.<x>.program", "any", "a signed commit or tag, log --show-signature, verify-commit"),
    ("gpg.ssh.defaultKeyCommand", "any", "a signed commit or tag, log --show-signature, verify-commit"),
    ("core.editor", "any", "commit, tag or rebase without a message"),
    ("sequence.editor", "any", "commit, tag or rebase without a message"),
    ("core.gitProxy", "any", "a git:// fetch"),
    ("remote.<x>.uploadpack", "any", "a local or ssh fetch or push"),
    ("remote.<x>.receivepack", "any", "a local or ssh fetch or push"),
    ("core.alternateRefsCommand", "any", "a fetch or a push"),
    ("submodule.<x>.update", "begins with !", "submodule update"),
    ("hook.<x>.command", "any", "the hook event its hook.<x>.event names"),
    ("alias.<x>", "begins with !", "git <alias>"),
    ("alias.<x>.command", "any", "git <alias>"),
    ("trailer.<x>.cmd", "any", "commit --trailer, interpret-trailers"),
    ("trailer.<x>.command", "any", "commit --trailer, interpret-trailers"),
    ("difftool.<x>.cmd", "any", "difftool, mergetool"),
    ("difftool.<x>.path", "any", "difftool, mergetool"),
    ("mergetool.<x>.cmd", "any", "difftool, mergetool"),
    ("mergetool.<x>.path", "any", "difftool, mergetool"),
    ("browser.<x>.cmd", "any", "help -w, web--browse, gui"),
    ("browser.<x>.path", "any", "help -w, web--browse, gui"),
    ("man.<x>.cmd", "any", "help -w, web--browse, gui"),
    ("man.<x>.path", "any", "help -w, web--browse, gui"),
    ("guitool.<x>.cmd", "any", "help -w, web--browse, gui"),
    ("sendemail.ccCmd", "any", "send-email"),
    ("sendemail.toCmd", "any", "send-email"),
    ("sendemail.headerCmd", "any", "send-email"),
    # TOOL-dSafePassage-48 S2: `git help --config` does not list it; git-send-email's option table
    # does (`sendmailcmd`), and send-email runs it through `sh -c`.
    ("sendemail.sendmailCmd", "any", "send-email, through sh -c, by git-send-email's option table"),
    ("gc.recentObjectsHook", "any", "gc, repack --cruft, and the auto-gc of commit and fetch"),
    # TOOL-dSafePassage-42 S7: the last segments `tunnel`, `httpd` and `smtpserver`; an absolute
    # `smtpServer` is a program git runs, a host name is not.
    ("imap.tunnel", "any", "imap-send"),
    ("instaweb.httpd", "any", "instaweb"),
    ("sendemail.smtpServer", "an absolute path", "send-email"))
# TOOL-dSafePassage-48 S1, the class: git-send-email reads each of its keys under
# `sendemail.<identity>` before the bare section, so every `sendemail.<key>` row above stands in its
# identity form too (`sendemail.<x>.ccCmd` and the like), stated once here rather than typed per row.
STEP_REFUSED_KEYS += tuple((p.replace("sendemail.", "sendemail.<x>.", 1), rule, runs)
                           for p, rule, runs in STEP_REFUSED_KEYS if p.startswith("sendemail."))
# The executor-shaped keys the check does not refuse (TOOL-dSafePassage-29 S2), as (key pattern, why).
STEP_UNREFUSED_KEYS = (
    ("merge.<driver>.driver", "a step does not merge, and gov's own checkout declares two (TOOL-dSafePassage-24 §3)"),
    ("core.hooksPath", "TOOL-dSafePassage-7's command-scope pair outranks it"),
    ("core.pager", "git runs a pager only when stdout is a terminal, and a step's output is captured"),
    ("color.pager", "a boolean; it runs nothing"),
    ("column.clean", "a layout option; it runs nothing"),
    ("include.path", "read by --includes, so the included file's own keys are graded"),
    ("includeIf.<condition>.path", "read by --includes, so the included file's own keys are graded"),
    ("advice.ignoredHook", "a boolean advice switch; it runs nothing"),
    ("uploadpack.packObjectsHook", "honoured only from protected config, which the step environment does not set"))
GIT_FALSE = ("false", "no", "off", "0", "")
# How much later than a lock's `started` a census row of its pid may estimate its creation and still
# be the holder (TOOL-dSafePassage-22 S3). It covers the census's whole-second `age_s`, per backend
# (TOOL-dSafePassage-35 S7): `windows-join` rounds it with PowerShell's `[int]`, at most 0.5 s;
# `posix-ps` takes `etimes`, which `ps` truncates, at most 1 s. The 2 s covers the larger, and no
# latency: the clock is read before the census, so a slow census errs toward live.
REUSE_MARGIN_S = 2.0


class Refusal(RuntimeError):
    """A condition that stops govkit before it reads or writes anything further."""


# ------------------------------------------------- argv resolution (TOOL-dSafePassage-35 S24)
# The step module's argv resolution owns its closure: moved here from govkit.py, which binds each
# moved name a reader spells off it back from this module. The sibling-kit resolver is an inline
# copy, byte-identical to the canonical one named on its marker line and gated by the
# resolve-python self-test's parity arm.
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


#: The canonical ctx's marker that every `opt_in` rule lands. Reserved: `target_context` refuses a
#: target that spells it, because it would take every opt-in of that kit without naming one.
OPT_IN_ALL = "opt_in_all"


# The negative lookbehind is load-bearing and was bought by a failing arm. A discharge probe is a
# SHELL command, and shell parameter expansion is spelled `${name}` — so a bare `\{([a-z_]+)\}`
# matched the `{k}` inside `${k}` in a probe's own loop variable and reported a missing answer named
# `k`. Two syntaxes sharing a brace is the collision; refusing to match after a `$` is the fix.
TOKEN_RX = re.compile(r"(?<!\$)\{([a-z_]+)\}")


_BASH: str | None = None


def resolve_bash() -> str:
    """The bash that shares THIS filesystem, not whatever the NAME `bash` resolves to.

    MEASURED on node d, 2026-08-20: a descriptor declares `argv = ["bash", ...]`, govkit is a
    WINDOWS python, and subprocess resolving the bare name goes through the Windows loader —
    which finds C:/Windows/System32/bash.exe, the WSL launcher, before git-bash. WSL then sees a
    different filesystem (the target resolves under /mnt/c/) and a different interpreter: its
    python3 is 3.10.12, so the playbook adopter died on `import tomllib`, which needs 3.11. The
    whole `govkit acceptance matrix` leg was RED for that reason and for no other.

    This is the documented class `memory/gotchas/subprocess-resolves-a-different-shell.md`, and
    the remedy it names is this one: name the EXECUTABLE, never the command. corpus_ids.py
    carries the same function for the memory-tree kit. It is duplicated rather than imported
    because govkit is COPY-INSTALLED as a standalone directory and cannot reach that module.

    A candidate is accepted only if it RUNS — existing on disk is not evidence, the same mistake
    <prefix>/lib/resolve-python.sh documents for the Microsoft Store python3 stub.

    WHAT THIS DOES NOT DO: it does not make a target's own scripts portable, and it does not
    check the interpreter those scripts then pick. It fixes which SHELL runs them and nothing
    else. GOV_BASH overrides, and an override that is set and unusable is a Refusal here rather
    than a silent fall-through — the operator would believe they had chosen.
    """
    global _BASH
    if _BASH:
        return _BASH

    def check_runs(cand: str) -> bool:
        try:
            return subprocess.run([cand, "-c", ":"], capture_output=True).returncode == 0
        except OSError:
            return False

    override = os.environ.get("GOV_BASH")
    if override:
        if check_runs(override):
            _BASH = override
            return _BASH
        raise Refusal(f"govkit: GOV_BASH is set to {override!r} and does not run. An override "
                      f"that is set and unusable is this failure, not a fall-through.")
    for d in os.environ.get("PATH", "").split(os.pathsep):
        for name in ("bash.exe", "bash"):
            cand = os.path.join(d, name)
            if not os.path.isfile(cand):
                continue
            low = cand.replace("\\", "/").lower()
            if "/system32/" in low or "/windowsapps/" in low:
                continue          # a launcher for a DIFFERENT filesystem
            if not check_runs(cand):
                continue          # on disk, cannot execute
            _BASH = cand
            return _BASH
    raise Refusal("govkit: no usable bash on PATH that shares this filesystem — every candidate "
                  "was either a System32/WindowsApps launcher or did not run. Set GOV_BASH.")


def resolve_shell_argv(argv: list[str]) -> list[str]:
    """Replace a LEADING bare `bash` with the resolved executable; every other argv is untouched.

    Only position 0 and only the bash names. A `bash` appearing as an ARGUMENT is a value the
    target chose and is none of govkit's business, and `sh` is left alone because substituting
    bash for it would change the language a target asked for.

    Falls back to the argv unchanged when no bash resolves, so a machine with none behaves
    exactly as it does today instead of newly refusing on a path that never needed this.
    """
    if not argv or argv[0] not in ("bash", "bash.exe"):
        return list(argv)
    try:
        return [resolve_bash()] + list(argv[1:])
    except Refusal:
        return list(argv)


def resolve_tokens(s: str, ctx: dict[str, str]) -> tuple[str, list[str]]:
    """Substitute `{token}`s from the target's answers. Unresolved tokens are RETURNED, not emitted.

    A path with a brace still in it is not a path. Emitting one is how a deployer writes a literal
    `{memory_root}` directory into somebody's repository, so the caller is handed the missing names
    and decides — which for `plan` and `apply --unattended` is a refusal that names the key.
    """
    missing: list[str] = []

    def sub(m: re.Match) -> str:
        k = m.group(1)
        if k in ctx:
            return ctx[k]
        missing.append(k)
        return m.group(0)

    return TOKEN_RX.sub(sub, s), missing


# THE ONE PLACE TARGET-SUPPLIED TEXT BECOMES PART OF A COMMAND, so it is the one place to refuse.
#
# Every token value below comes out of the TARGET's `.governance/deploy.toml`, a file in a repository
# gov does not own. Those values are interpolated by `resolve_tokens` into argv templates GOV wrote —
# `[check].argv`, `[[hole]].discharge.command`, `[[gate_leg]].argv` — several of which are
# `["bash", "-c", "... {kit} ..."]` or `["python", "-c", "... sys.path.insert(0, '{kit}') ..."]`.
# A shell metacharacter or a quote break in a value therefore becomes CODE.
#
# REPRODUCED, twice, on this engine before this guard existed: a target whose `deploy.toml` carried
# `prefix = "tools; touch PWNED-BY-CHECK ;"` made a READ-ONLY `govkit check` — no `--write`, no
# `--run-discharge`, nothing printed — create that file in the target. A second reproduction broke
# out of a `python -c` string the same way. `resolve_shell_argv` is no defence: it rewrites argv[0]
# and nothing else.
#
# WHY IT WAS MISSED, stated because the miss is the interesting part. The fold before this one
# labelled each spawn by WHO AUTHORED THE ARGV TEMPLATE and concluded these sites were gov's. That is
# the wrong question. The template is gov's and the VALUES SUBSTITUTED INTO IT are the target's, so
# the resulting command is target-influenced wherever a token appears — and the declaration asserting
# otherwise was itself the artifact written to stop this class recurring.
#
# A CHARACTER CLASS, not an escaper. Escaping is per-consumer — a value safe in argv is not safe
# inside `bash -c` — and this value reaches several. What every legitimate answer in this repo's
# descriptors actually is: a path fragment. So the refusal is narrow, total, and needs no consumer
# to be correct.
# `\Z` AND NOT `$`: Python's `$` matches BEFORE a final newline, so "tools\n" passed this class
# for as long as it has existed. Round 4 measured it. A trailing newline in a value spliced into a
# `bash -c` string ends the command and starts another one, which is the exact escape the class
# was written to stop.
TOKEN_VALUE_RE = re.compile(r"\A[A-Za-z0-9_./~@+-]*\Z")
# THE ONE ADMITTED COLON, anchored, and nothing else. Round 3 measured that the class above refuses
# `user_skills = "C:/Users/x/.claude/skills"` -- a correct answer on the platform this project's own
# primary node runs on -- with a message about command injection naming nothing the operator did
# wrong. `kickoff-manifest` is in the DEFAULT selection and its rule is `{user_skills}/session-kickoff`,
# so that sat on the common path for every Windows adopter. No arm caught it: both fixtures spell the
# answer in forms that pass (`~/.claude/skills`, `/tmp/gk-fake-skills`).
#
# WHY THIS IS A NARROW WIDENING AND NOT A HOLE. The threat the class exists for is a value leaving its
# argument inside a `bash -c` or `python -c` template, which needs a shell metacharacter: `;` `|` `&`
# `$` a backtick, a quote, a newline, a redirect. `:` is none of those -- it is bash's null command and
# is inert as argument text. What a colon CAN do is make a path absolute on Windows, and that is a
# containment question, answered one function down by `demand_contained_dest`, which reds a
# drive-lettered DESTINATION. So the two guards keep their own jobs: this one grades characters, that
# one grades escape.
#
# ANCHORED AT POSITION 1 AND REQUIRING A FORWARD SLASH. `C:/x` passes; `C:x`, `C:\x`, `a:b` and
# `C:/a;b` do not -- the remainder after the drive is graded by the class above exactly as before, so
# an interior colon or any metacharacter still refuses. Backslash stays refused deliberately: §11
# pins forward slashes on this platform, and admitting both spellings would double the surface for
# nothing.
DRIVE_PREFIX_RE = re.compile(r"^[A-Za-z]:/")


# ---- TWO CLASSES, BECAUSE THERE ARE TWO KINDS OF VALUE AND ONE CLASS GRADED BOTH.
# ---- The strict class above was written for `prefix` -- which becomes a PATH and is interpolated
# ---- into `bash -c` and `python -c` argv templates -- and was then applied to every `answers.*`
# ---- and every `kit.<eid>.*` value as well. Those are not all paths. The playbook charter's
# ---- placeholders are rendered into a MARKDOWN DOCUMENT, and a legitimate override for one carries
# ---- spaces by nature: `gate_runner = "bash <prefix>/run-gates/run-gates.sh"` is a command a reader
# ---- runs, `id_families = "PLAY KICK TOOL DEPL"` is a list.
# ----
# ---- MEASURED, AND IT WAS NOT HYPOTHETICAL. The single class red the `govkit acceptance matrix`
# ---- leg from the commit that introduced it, and it stayed red across two commits because no full
# ---- bar ran in between. The live adopter's answers happen to be all path-shaped, so nothing else
# ---- noticed. That is the same mistake as the drive letter, twice: writing one character class for
# ---- `prefix` and applying it to every value that passes through the same function.
# ----
# ---- THE PROSE CLASS IS STILL AN ALLOWLIST, and it still refuses every injection vector this build
# ---- reproduced. It adds space, comma, equals and colon -- none of which can end an argument or
# ---- start a command -- and admits nothing that can: no `;` `|` `&` `$`, no backtick, no quote, no
# ---- redirect, no parenthesis or brace, no glob, no backslash, no control character. `tools; touch
# ---- PWNED ;` and `$(id)` are refused by it exactly as before.
# ----
# ---- WHAT THE PROSE CLASS DOES NOT PROMISE. An earlier version of this comment said a spaced value
# ---- reaching a `bash -c` template merely WORD-SPLITS, that this is "a correctness bug for the
# ---- operator who wrote it" and "not code execution". THAT WAS FALSE and round 4 proved it: for a
# ---- `python {kit}/<script>` template the injected word becomes the script python runs. A comment
# ---- asserting a guarantee the code does not hold is worse than no comment, because the next reader
# ---- budgets against it.
# ---- The prose class is sound ONLY for a value whose sole consumer is a rendered document, and
# ---- nothing here establishes that per key. What makes it safe today is `SEEDED_TOKENS` above:
# ---- every token that reaches an argv is gov's own and a target cannot supply one. The escape half
# ---- is owned by `demand_contained_dest`, which grades destinations whichever class they came
# ---- through.
# ---- THE KEYS GOV COMPUTES FOR ITSELF, and which a TARGET may therefore never supply.
# ---- ROUND 4's blocker, and it is round 2's blocker reopened by round 2's own fix. `target_context`
# ---- seeds `prefix`, `kit_id` and `kit` from a `prefix` graded by the STRICT class, then walked the
# ---- target's `[answers]` and `[kit.<eid>]` tables and assigned `ctx[k]` UNCONDITIONALLY through
# ---- the PROSE class -- which admits a space. Nothing stopped a target routing a document-class
# ---- value into a shell-class key.
# ----
# ---- REPRODUCED: `[answers] kit = "-m pwned "` makes `ctx["kit"]` that string, and drift-audit's
# ---- shipped hole probe resolves to `python -m pwned /drift_report.py --check` with ZERO
# ---- unresolved tokens. Six shipped descriptors interpolate `{kit}` inside a `-c` string, and
# ---- `cmd_check` spawns every one of them from a READ-ONLY verb with no opt-in flag.
# ----
# ---- THE ENGINE ALREADY KNEW THE SET. `needed_answers` declares exactly these five and refuses to
# ---- ask an operator for any of them, while `target_context` let a target supply all five: two
# ---- functions, one set, opposite answers. That is what this constant ends -- it is READ by both.
# ---- THE SET IS THE THREE KEYS SEEDED ABOVE THE LOOPS, and it is NOT `needed_answers`' five.
# ---- Measured before narrowing, because widening a refusal without enumerating its population is
# ---- the mistake this whole review round is about. `memory_root` is applied by `ctx.setdefault`
# ---- AFTER the loops, so a target that supplies it legitimately wins -- and gov's OWN selftest
# ---- fixtures supply it in `[answers]` at four sites, as does a live adopter. Refusing it would
# ---- have broken the suite and every real install to close a hole it is not part of. `relpath` is
# ---- never a ctx key at all: `resolve_dests` substitutes it per rule with `.replace`, so a target
# ---- supplying it reaches nothing.
# ---- `needed_answers` means "do not ASK for these five"; this means "do not READ these three".
# ---- Different questions, and collapsing them was the first cut of this fix.
SEEDED_TOKENS = ("prefix", "kit_id", "kit")
# The subset a per-ENTRY `[kit.<eid>]` table may set, graded by the STRICT path class. See
# `target_context` for why the split is per-table rather than a name ban.
PER_KIT_PATH_TOKENS = ("prefix", "kit")


ANSWER_VALUE_RE = re.compile(r"\A[A-Za-z0-9_./~@+:, =-]*\Z")


def demand_safe_token(key: str, value: str, where: str, prose: bool = False) -> str:
    """Refuse a target-supplied token value that could leave its argument and become code.

    `prose=False` (the default) is the STRICT class, for a value that becomes a path or is
    interpolated into an argv this engine runs. A leading `<letter>:/` is dropped before grading and
    the REMAINDER graded normally, so a Windows drive letter is admitted and an interior colon is
    not.

    `prose=True` is for a value whose only consumer renders it into a document. See the block above
    `ANSWER_VALUE_RE` for what it admits, what it still refuses, and what it deliberately does not
    promise.
    """
    rx = ANSWER_VALUE_RE if prose else TOKEN_VALUE_RE
    body = value if prose else (value[2:] if DRIVE_PREFIX_RE.match(value) else value)
    if not rx.match(body):
        bad = "".join(sorted({c for c in body if not rx.match(c)}))
        raise Refusal(
            f"the target descriptor's '{key}' is {value!r}, which carries {bad!r}. Token values are "
            f"interpolated into argv this engine RUNS — several shipped probes are `bash -c` and "
            f"`python -c` strings — so a value outside [A-Za-z0-9_./~@+-] can leave its argument and "
            f"become code. Refusing to resolve it ({where}). "
            + ("This value is rendered into a document, so spaces and commas are fine here and "
               "shell metacharacters are not"
               if prose else
               "Every legitimate value here is a path fragment, optionally behind a `C:/` drive "
               "letter")
            + "; if you need one that is not, that is a change to this rule and not to a descriptor")
    return value


def target_context(target: pathlib.Path, deploy: dict, eid: str, desc: dict) -> dict[str, str]:
    """The token values for one entry, from the target descriptor's answers.

    EVERY VALUE IS VALIDATED HERE, at the boundary, rather than at the several places they are
    consumed. See `demand_safe_token` for what was reproduced without it.
    """
    # WHERE A TARGET MAY SPEAK ABOUT A SEEDED TOKEN, per TABLE and per KEY rather than by name.
    #
    # `ce4ef9f3` closed a live injection: a target could put a PROSE-class value -- one that admits
    # a space -- on a key this engine interpolates into a `bash -c` template, and a READ-ONLY
    # `check` would run it. That fix refused `prefix`, `kit_id` and `kit` from both target tables.
    #
    # The refusal is a SUPERSET of the defect, and the surplus is load-bearing for an adopter. The
    # top-level `prefix` below is target-supplied too, and it is safe for exactly one reason: it is
    # graded by the STRICT class, which admits no space, quote, semicolon, backtick or pipe, so a
    # value cannot leave its argument. The defect was the CLASS, not the key. So:
    #
    #   [answers]    refuses all three. It is GLOBAL: a `kit` there collapses every entry into one
    #                home and a `kit_id` renames all of them, so no value is ever legitimate.
    #   [kit.<eid>]  accepts `prefix` and `kit`, graded STRICTLY. A per-entry install home is a path
    #                fragment the OPERATOR owns and this engine cannot derive -- an adopter whose
    #                memory-tree lives at `scripts/` rather than `scripts/memory-tree/` has no other
    #                way to say so, and before this it had none at all. `kit_id` stays refused
    #                everywhere: that is the ENTRY's identity, joined to the receipt's `kit` field,
    #                and not a path.
    per_kit = (deploy.get("kit") or {}).get(eid) or {}
    for _tbl, _label, _allowed in ((deploy.get("answers") or {}, "answers", ()),
                                   (per_kit, f"kit.{eid}", PER_KIT_PATH_TOKENS)):
        for k in _tbl:
            if k in SEEDED_TOKENS and k not in _allowed:
                raise Refusal(
                    f"the target descriptor supplies '{_label}.{k}', which this engine derives "
                    f"({', '.join(SEEDED_TOKENS)}). These are interpolated into argv this engine "
                    f"RUNS -- a `{{{k}}}` inside a `bash -c` or `python -c` template becomes the "
                    f"command. A per-ENTRY install home is settable as `kit.<entry>.prefix` or "
                    f"`kit.<entry>.kit`, graded by the strict path class; the global `[answers]` "
                    f"table and `kit_id` are not. Remove the key: {_label}.{k}")
    prefix = demand_safe_token(
        f"kit.{eid}.prefix" if per_kit.get("prefix") else "prefix",
        (per_kit.get("prefix") or deploy.get("prefix") or "tools").strip("/"),
        f"entry '{eid}'")
    # DERIVED unless the target names it. `{kit}` follows a per-entry `prefix` when only that is
    # given, so an adopter who moves a whole kit family says it once.
    _kit = per_kit.get("kit")
    kit = (demand_safe_token(f"kit.{eid}.kit", _kit.strip("/"), f"entry '{eid}'")
           if isinstance(_kit, str) and _kit else f"{prefix}/{eid}")
    ctx: dict[str, str] = {
        "prefix": prefix,
        "kit_id": eid,
        "kit": kit,
    }
    # TOOL-dSafePassage-8 S3. An `[answers]` value is graded and entered only where THIS entry's own
    # descriptor names its `{token}`: one no template of the entry names never reaches a substitution
    # here, and gov's own charter answers carry `—`, `;` and `<` for the renderer alone. Every value
    # that can reach an argv, a destination or a pattern of the entry is still graded by its class.
    named: set[str] = set()
    _todo: list = [desc]
    while _todo:
        _v = _todo.pop()
        if isinstance(_v, dict):
            _todo += _v.values()
        elif isinstance(_v, list):
            _todo += _v
        elif isinstance(_v, str):
            named.update(TOKEN_RX.findall(_v))
    for k, v in (deploy.get("answers") or {}).items():
        if isinstance(v, str) and k in named:
            ctx[k] = demand_safe_token(f"answers.{k}", v, f"entry '{eid}'", prose=True)
    for k, v in per_kit.items():
        if k == OPT_IN_ALL:
            raise Refusal(f"the target descriptor supplies 'kit.{eid}.{k}', which is reserved: it would "
                          f"take every opt-in of that entry without naming one. Set each rule's own "
                          f"`opt_in` key instead")
        if isinstance(v, str) and k not in PER_KIT_PATH_TOKENS:
            ctx[k] = demand_safe_token(f"kit.{eid}.{k}", v, f"entry '{eid}'", prose=True)
    ctx.setdefault("memory_root", "memory")
    return ctx


class StepRow(NamedTuple):
    """One `[[upgrade]]` row, validated. `introduced` is a commit, `unlanded`, or None where the
    caller asked for no derivation; `file` is repo-relative and `row` 1-based within that file.
    `reverted` is None, `DOWN_EXIT` or an argv (TOOL-dSafePassage-17)."""
    id: str
    up: list
    down: list
    witness: list
    resume: object
    surfaces: list
    needs_target: bool
    file: str
    row: int
    introduced: str | None
    reverted: object = None


class RetiredRow(NamedTuple):
    """One `[[retired]]` row, validated. `successor` is a live id of the same kind, or `none`;
    `retired` is the retiring commit, `unlanded`, or None where no derivation was asked for."""
    id: str
    successor: str
    surfaces: list
    file: str
    row: int
    retired: str | None


def run_git(root, *args: str) -> bytes | None:
    """`git -C <root> <args>`'s stdout bytes, or None where git exits non-zero."""
    p = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    return p.stdout if p.returncode == 0 else None


def resolve_rev(root, rev: str | None) -> str | None:
    """`rev` as a full commit sha, None for the working tree; a rev naming no commit is a refusal."""
    if rev is None:
        return None
    out = run_git(root, "rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}")
    if not out:
        raise Refusal(f"'{rev}' names no commit in {pathlib.Path(root).as_posix()}")
    return out.decode("utf-8").strip()


def read_file_at(root, sha: str | None, rel: str) -> str | None:
    """The text of `rel` in the commit `sha` names, or in the working tree for None; None when absent."""
    if sha is None:
        p = pathlib.Path(root) / rel
        return p.read_text(encoding="utf-8") if p.is_file() else None
    data = run_git(root, "cat-file", "blob", f"{sha}:{rel}")
    return None if data is None else data.decode("utf-8")


def parse_table_rows(text: str, rel: str, table: str, where: str) -> list[dict]:
    """The `[[<table>]]` rows of one TOML file's text, each a table, or a refusal naming the file."""
    try:
        doc = tomllib.loads(text.removeprefix("\ufeff"))
    except tomllib.TOMLDecodeError as e:
        raise Refusal(f"{rel}: not valid TOML at {where}: {e}") from None
    rows = doc.get(table, [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise Refusal(f"{rel}: `{table}` at {where} is not an array of tables")
    return rows


def read_registry_at(root, sha: str | None) -> tuple[str, str, list[dict], list[tuple[str, str]]]:
    """(the tool root, the registry's repo-relative path, its `[[retired]]` rows, [(entry id,
    descriptor path)]) at `sha`, each descriptor path's `{prefix}` resolved through govkit's own
    resolver, so the reader and the deployer cannot place a descriptor in two places."""
    gk = load_govkit()
    tr = gk.derive_tool_root(root)
    rel = f"{tr}/{HERE.name}/{REGISTRY_FILE}" if tr else f"{HERE.name}/{REGISTRY_FILE}"
    where = sha[:8] if sha else "the working tree"
    text = read_file_at(root, sha, rel)
    if text is None:
        raise Refusal(f"{rel}: no registry at {where}, and the rows are read from no other population")
    return tr, rel, parse_table_rows(text, rel, "retired", where), read_registry_entries(text, rel, tr, where)


def read_registry_entries(text: str, rel: str, tr: str, where: str) -> list[tuple[str, str]]:
    """[(entry id, descriptor path)] of one registry text, each `{prefix}` resolved through govkit's
    own resolver against the tool root `tr`."""
    gk = load_govkit()
    return [(e["id"], gk.resolve_prefix_token(e["descriptor"], tr))
            for e in parse_table_rows(text, rel, "entry", where)
            if isinstance(e.get("id"), str) and isinstance(e.get("descriptor"), str)]


def check_argv(value, at: str, tr: str, where: str, read_tracked, down: bool = False) -> list:
    """`value` as a validated argv, else a refusal naming `at` (file, row and key): non-empty
    strings, `argv[0]` an interpreter the runner resolves, only the three placeholders, `{to}` too
    where `down` (TOOL-dSafePassage-26 S10), and every `{gov}/` program a file `read_tracked()`
    names, git's tracked set at the revision read."""
    if not isinstance(value, list) or not value or not all(isinstance(t, str) and t for t in value):
        raise Refusal(f"{at}: an argv is a non-empty list of non-empty strings")
    if value[0] not in INTERPRETERS:
        raise Refusal(f"{at}: argv[0] '{value[0]}' is not one of {', '.join(INTERPRETERS)}, the "
                      f"interpreters the runner resolves")
    for tok in value:
        rest = PLACEHOLDER_RE.sub("", tok)
        if "{" in rest or "}" in rest:
            raise Refusal(f"{at}: '{tok}' carries a placeholder other than {{gov}}, {{target}} and "
                          f"{{prefix}}")
        if "{to}" in tok and not down:
            raise Refusal(f"{at}: '{tok}' carries {{to}}, which resolves only in a step's down, to the "
                          f"--to commit of `update --rollback`")
        if tok.startswith("{gov}/"):
            prog = (f"{tr}/" if tr else "") + tok[len("{gov}/"):]
            if prog not in read_tracked():
                raise Refusal(f"{at}: '{tok}' names {prog}, which is not a tracked file at {where}")
    return value


def check_surfaces(value, at: str) -> list:
    """`value` as a validated `surfaces` list: required, possibly empty, each `<class>:<name>`."""
    if not isinstance(value, list) or not all(isinstance(s, str) and SURFACE_RE.fullmatch(s) for s in value):
        raise Refusal(f"{at}: `surfaces` is a list of `<class>:<name>` items, class [a-z][a-z0-9-]*")
    return value


def read_steps(root, rev: str | None, landed_ref: str | None) -> list[StepRow]:
    """Every `[[upgrade]]` row at `rev` (None: the working tree), validated, in the total order.

    The steps file beside this one first, then each registry entry's descriptor in entry order. With
    `landed_ref` each row's `introduced` is derived along that ref's first-parent line; without it,
    None and the order is declaration order. The derivation reads each walked commit's declaring
    files from that commit's own registry, so a descriptor that moved is read at its old path, and a
    shallow repository, whose history is cut, is a refusal naming `git fetch --unshallow`
    (TOOL-dSafePassage-26 S37)."""
    sha = resolve_rev(root, rev)
    where = sha[:8] if sha else "the working tree"
    tr, reg_rel, _retired, entries = read_registry_at(root, sha)
    entry_ids = {eid for eid, _p in entries}
    files = [(reg_rel[:-len(REGISTRY_FILE)] + STEPS_FILE, None)] + [(p, eid) for eid, p in entries]
    tracked: set[str] = set()

    def read_tracked() -> set[str]:
        if not tracked:
            ls = (run_git(root, "ls-files", "-z") if sha is None
                  else run_git(root, "ls-tree", "-r", "--name-only", "-z", sha))
            tracked.update((ls or b"").decode("utf-8").split("\0"))
        return tracked

    rows: list[StepRow] = []
    seen: dict[str, str] = {}
    for rank, (rel, eid) in enumerate(files):
        text = read_file_at(root, sha, rel)
        if text is None:
            if eid is None:
                continue  # the steps file is optional in a tree that declares no such row
            raise Refusal(f"{rel}: the registry names this descriptor for '{eid}' and it is absent at {where}")
        for n, d in enumerate(parse_table_rows(text, rel, "upgrade", where), 1):
            at = f"{rel} [[upgrade]] row {n}"
            for k in d:
                if k == "introduced":
                    raise Refusal(f"{at} key introduced: the introducing commit is derived from the "
                                  f"default branch's first-parent history and never typed")
                if k not in STEP_KEYS:
                    raise Refusal(f"{at} key {k}: not a key of the step grammar ({', '.join(STEP_KEYS)})")
            sid = d.get("id")
            m = ID_RE.fullmatch(sid) if isinstance(sid, str) else None
            if not m:
                raise Refusal(f"{at} key id: '{sid}' is not `<entry>/<slug>`, slug [a-z0-9][a-z0-9.-]*")
            if eid is not None and m[1] != eid:
                raise Refusal(f"{at} key id: '{sid}' names entry '{m[1]}', and this descriptor is '{eid}'s")
            if eid is None and m[1] in entry_ids:
                raise Refusal(f"{at} key id: '{sid}' names the registry entry '{m[1]}', whose own "
                              f"descriptor declares its steps")
            if sid in seen:
                raise Refusal(f"{at} key id: '{sid}' is declared twice, here and in {seen[sid]}")
            seen[sid] = rel
            for k in ("up", "down", "witness"):
                if k not in d:
                    raise Refusal(f"{at} key {k}: required")
                check_argv(d[k], f"{at} key {k}", tr, where, read_tracked, down=k == "down")
            resume = d.get("resume")
            if resume is not None and resume != "atomic":
                check_argv(resume, f"{at} key resume", tr, where, read_tracked)
            reverted = d.get("reverted")
            if reverted is not None and reverted != DOWN_EXIT:
                if not isinstance(reverted, list):
                    raise Refusal(f"{at} key reverted: '{reverted}' is neither \"{DOWN_EXIT}\" nor an argv")
                check_argv(reverted, f"{at} key reverted", tr, where, read_tracked)
            if "surfaces" not in d:
                raise Refusal(f"{at} key surfaces: required, possibly empty, so an absence is declared")
            check_surfaces(d["surfaces"], f"{at} key surfaces")
            if not isinstance(d.get("needs-target"), bool):
                raise Refusal(f"{at} key needs-target: required, true or false")
            rows.append(StepRow(sid, d["up"], d["down"], d["witness"], resume, d["surfaces"],
                                d["needs-target"], rel, n, None, reverted))
    if landed_ref is None:
        return rows
    if (run_git(root, "rev-parse", "--is-shallow-repository") or b"").strip() == b"true":
        raise Refusal(f"{pathlib.Path(root).as_posix()} is a shallow clone, so the first-parent history "
                      f"each row's introducing commit is derived along is cut; run `git fetch --unshallow`")
    hit = derive_introduced(root, landed_ref, [files[0][0]], "upgrade", [r.id for r in rows],
                            registry=(reg_rel, tr))
    rank_of = {rel: i for i, (rel, _e) in enumerate(files)}
    rows = [r._replace(introduced=hit[r.id][0] if r.id in hit else UNLANDED) for r in rows]
    return sorted(rows, key=lambda r: (r.id not in hit, hit.get(r.id, ("", 0))[1], rank_of[r.file], r.row))


def read_retired(root, rev: str | None, landed_ref: str | None) -> list[RetiredRow]:
    """Every `[[retired]]` row of the registry at `rev` (None: the working tree), validated: its id
    retired, its successor a live id of the same kind or `none`. Step ids are read only when a row
    names one. With `landed_ref` each row's `retired` is derived like a step's introducing commit."""
    sha = resolve_rev(root, rev)
    _tr, reg_rel, raw, entries = read_registry_at(root, sha)
    entry_ids = {eid for eid, _p in entries}
    step_ids: set[str] | None = None
    out: list[RetiredRow] = []
    for n, d in enumerate(raw, 1):
        at = f"{reg_rel} [[retired]] row {n}"
        for k in d:
            if k == "retired":
                raise Refusal(f"{at} key retired: the retiring commit is derived from the default "
                              f"branch's first-parent history and never typed")
            if k not in RETIRED_KEYS:
                raise Refusal(f"{at} key {k}: not a key of the succession grammar ({', '.join(RETIRED_KEYS)})")
        rid, succ = d.get("id"), d.get("successor")
        if not isinstance(rid, str) or not rid or not isinstance(succ, str) or not succ:
            raise Refusal(f"{at} key {'id' if not isinstance(rid, str) or not rid else 'successor'}: required, a string")
        if "surfaces" not in d:
            raise Refusal(f"{at} key surfaces: required, possibly empty, so an absence is declared")
        check_surfaces(d["surfaces"], f"{at} key surfaces")
        is_step = "/" in rid
        if is_step and step_ids is None:
            step_ids = {r.id for r in read_steps(root, sha, None)}
        live = step_ids if is_step else entry_ids
        if rid in live:
            raise Refusal(f"{at} key id: '{rid}' is still a live {'step' if is_step else 'registry entry'}")
        if succ != "none":
            if ("/" in succ) != is_step:
                raise Refusal(f"{at} key successor: '{succ}' is not of the retired id's kind "
                              f"({'a step id' if is_step else 'an entry id'}, or none)")
            if succ not in live:
                raise Refusal(f"{at} key successor: '{succ}' is not live at "
                              f"{sha[:8] if sha else 'the working tree'}")
        out.append(RetiredRow(rid, succ, d["surfaces"], reg_rel, n, None))
    if landed_ref is None:
        return out
    hit = derive_introduced(root, landed_ref, [reg_rel], "retired", [r.id for r in out])
    return [r._replace(retired=hit[r.id][0] if r.id in hit else UNLANDED) for r in out]


def derive_introduced(root, landed_ref: str, files: list[str], table: str,
                      ids: list[str], registry: tuple[str, str] | None = None) -> dict[str, tuple[str, int]]:
    """{id: (commit, first-parent position)} for each of `ids` a `[[<table>]]` row of `files` holds on
    `landed_ref`'s first-parent line: the oldest commit whose change against its first parent left a
    holding blob. With `registry`, (its path, the tool root), the declaring files are `files` plus
    the descriptors the registry names AT EACH WALKED COMMIT, read from that commit's own registry
    blob (TOOL-dSafePassage-26 S37): every path any vintage named is walked, and a blob counts only
    while its path is declared, so a moved descriptor is read at its old path. One `git log` names
    the changed blobs oldest first, `blob_at` reads each through one `cat-file --batch` it is
    handed, every declaring blob is parsed, so an id in any string spelling the reader accepts is
    found (TOOL-dSafePassage-74), and the walk stops at the last hit."""
    want, found = set(ids), {}
    if not (landed_ref and want and files):
        return found
    declared, walked = set(files), list(files)
    cat = subprocess.Popen(["git", "-C", str(root), "cat-file", "--batch"],
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        if registry:
            reg_rel, tr = registry
            for c in (run_git(root, "log", "--first-parent", "--format=%H", landed_ref, "--", reg_rel) or b"").split():
                data = blob_at(root, c.decode("ascii"), reg_rel, cat)
                try:
                    walked += [d for _e, d in read_registry_entries((data or b"").decode("utf-8"), reg_rel, tr, "")]
                except (Refusal, UnicodeDecodeError):
                    continue  # an unreadable vintage declares nothing
            walked = sorted(set(walked)) + [reg_rel]
        log = run_git(root, "log", "--first-parent", "--reverse", "--diff-merges=first-parent", "--raw",
                      "--no-abbrev", "--no-renames", "--format=%x00%H", landed_ref, "--", *walked)
        if log is None:
            raise Refusal(f"git log over {landed_ref} failed in {pathlib.Path(root).as_posix()}")
        for pos, chunk in enumerate(log.decode("utf-8", "replace").split("\0")[1:]):
            lines = chunk.strip("\n").split("\n")
            # The registry's own change first, so a descriptor it adds in this commit is declared.
            for ln in sorted(lines[1:], key=lambda x: not (registry and x.endswith("\t" + registry[0]))):
                if not ln.startswith(":"):
                    continue
                meta, path = ln.split("\t", 1)
                if not meta.split()[3].strip("0"):
                    continue  # a deletion leaves no blob to hold a row
                data = blob_at(root, lines[0].strip(), path, cat)
                if data is None:
                    continue
                text = data.decode("utf-8", "replace")
                if registry and path == registry[0]:
                    try:  # this commit's registry: the declaring files from here on
                        declared = set(files) | {d for _e, d in read_registry_entries(text, path, registry[1], "")}
                    except Refusal:
                        pass
                    if path not in files:
                        continue
                if path not in declared:
                    continue
                try:
                    held = {r.get("id") for r in tomllib.loads(text.removeprefix("\ufeff")).get(table) or []
                            if isinstance(r, dict)}
                except (tomllib.TOMLDecodeError, AttributeError, TypeError):
                    continue  # an unparsable or misshapen vintage holds no row
                for i in want & held:
                    found[i] = (lines[0].strip(), pos)
                    want.discard(i)
            if not want:
                break
    finally:
        cat.stdin.close()
        cat.wait()
    return found


def resolve_claim(eid: str, entry_ids, retired: list[RetiredRow]) -> RetiredRow | None:
    """What a receipt's claim of `eid` resolves to: None when it is a live entry, its succession row
    when a `[[retired]]` row names it, and a refusal when it is neither — a claimed kit dropped with
    no successor would leave its files owned by nobody."""
    if eid in entry_ids:
        return None
    for row in retired:
        if row.id == eid:
            return row
    raise Refusal(f"the receipt claims kit '{eid}', which is no longer a registry entry — refusing "
                  f"rather than dropping it, which would leave its files owned by nobody")


def check_frozen(root, base: str, head: str) -> tuple[int, list[str]]:
    """(landed rows at `base`, one problem line per frozen field, row or program `head` moved)."""
    base_sha, head_sha = resolve_rev(root, base), resolve_rev(root, head)
    tr = load_govkit().derive_tool_root(root)
    was, now = read_steps(root, base_sha, None), {r.id: r for r in read_steps(root, head_sha, None)}
    was_ret = read_retired(root, base_sha, None)
    now_ret = {r.id: r for r in read_retired(root, head_sha, None)}
    problems: list[str] = []
    for row in was:
        cur = now.get(row.id)
        if cur is None:
            if row.id not in now_ret:
                problems.append(f"{row.id}: the landed [[upgrade]] row is gone from {row.file}, and no "
                                f"[[retired]] row names it — restore it, or retire it to its successor")
            continue
        for field in FROZEN_FIELDS:
            if getattr(row, field) != getattr(cur, field):
                problems.append(f"{row.id}: its landed `{field}` was edited in {cur.file} — a landed "
                                f"row is frozen; ship the correction as a new step")
        for argv in (row.up, row.down, row.witness, *(a for a in (row.resume, row.reverted) if isinstance(a, list))):
            for tok in argv:
                if not tok.startswith("{gov}/"):
                    continue
                prog = (f"{tr}/" if tr else "") + tok[len("{gov}/"):]
                if run_git(root, "rev-parse", f"{base_sha}:{prog}") != run_git(root, "rev-parse", f"{head_sha}:{prog}"):
                    problems.append(f"{row.id}: {prog}, a program its landed argv names, moved bytes — "
                                    f"a landed step's program is frozen; ship the correction as a new step")
    for row in was_ret:
        cur = now_ret.get(row.id)
        if cur is None or (cur.successor, cur.surfaces) != (row.successor, row.surfaces):
            problems.append(f"{row.id}: its landed [[retired]] row was "
                            f"{'removed' if cur is None else 'edited'} in {row.file} — a landed "
                            f"succession row is frozen")
    return len(was) + len(was_ret), sorted(set(problems), key=problems.index)


def derive_image_path(target, step_id: str) -> pathlib.Path:
    """The before-image of `step_id` at `target`: `.governance/steps/<entry>/<slug>.before.json`."""
    m = ID_RE.fullmatch(step_id)
    if not m:
        raise Refusal(f"'{step_id}' is not a step id, so it has no before-image")
    return check_contained(target, f"{IMAGE_DIR}/{m[1]}/{m[2]}.before.json")


def derive_contained_rel(rel: str) -> str | None:
    """`rel` normalised, every `\\` folded to `/`, or None where it leaves the target or names no file
    under it (TOOL-dSafePassage-72 S1): it normalises to `.`, `..` or a `../` climb, it is rooted, UNC
    or drive-absolute, or it holds a colon anywhere, which also keeps an NTFS stream out. The one
    answer `check_contained` and govkit's `demand_contained_dest` share."""
    norm = posixpath.normpath(rel.replace("\\", "/"))
    if (norm in (".", "..") or norm.startswith("../") or posixpath.isabs(norm)
            or ntpath.isabs(rel) or ":" in rel):
        return None
    return norm


def check_contained(target, rel: str) -> pathlib.Path:
    """`target`/`rel` normalised, refused where `derive_contained_rel` reads it as leaving the target,
    and where any existing segment on it from the target down is a link or other reparse point, or
    does not read as a path on this node (TOOL-dSafePassage-72 S3, S4). The walk stops at the first
    segment that is absent or a file. The target root itself is not tested: callers resolve it. A
    path in the git directory is refused too, by a `.git` segment in any case with trailing dots or
    spaces stripped, or where it resolves at or under `read_git_dir` (TOOL-dSafePassage-76 S1)."""
    norm = derive_contained_rel(rel)
    if norm is None:
        raise Refusal(f"'{rel}' is not a path inside the target, so no step may write it")
    if ".." in rel.replace("\\", "/").split("/"):
        raise Refusal(f"'{rel}' holds a '..' segment, which a step's own write resolves through any link "
                      f"on the segment before it, so no step may write it")
    cur = pathlib.Path(target)
    for seg in norm.split("/"):
        cur = cur / seg
        try:
            linked = test_path_linked(cur)
        except (OSError, ValueError):
            raise Refusal(f"'{rel}': {cur} does not read as a path on this node, so no step may "
                          f"read or write it") from None
        if linked:
            raise Refusal(f"'{rel}': {cur} is a link or other reparse point, which no step read or "
                          f"write follows, so where it leads is unknown")
        if not cur.is_dir():  # absent, or a file: nothing below it exists
            break
    # TOOL-dSafePassage-76 S1: never into the git directory, by its spelling (any case, trailing dots
    # or spaces) and then by where the path resolves, which catches a short name and a separate one.
    if any(seg.casefold().rstrip(". ") == ".git" for seg in norm.split("/")):
        raise Refusal(f"'{rel}' is inside the repository's git directory, so no step may write it")
    gd = read_git_dir(pathlib.Path(target).resolve())
    if gd and (pathlib.Path(target) / norm).resolve().is_relative_to(gd):
        raise Refusal(f"'{rel}' is inside the repository's git directory {gd.as_posix()}, so no step "
                      f"may write it")
    return pathlib.Path(target) / norm


@functools.lru_cache(maxsize=None)
def read_git_dir(target: pathlib.Path) -> pathlib.Path | None:
    """The resolved git directory of the resolved `target`, `git rev-parse --absolute-git-dir` run
    under `build_step_env` as `read_target_repositories` runs it (TOOL-dSafePassage-76 S1); None where
    git names none, a target outside any repository."""
    # ponytail: a target whose git directory moves mid-process reads the old one; no step moves it
    with tempfile.TemporaryDirectory(prefix="gk-gitdir-", ignore_cleanup_errors=True) as td:
        p = subprocess.run(["git", "-C", str(target), "rev-parse", "--absolute-git-dir"], env=build_step_env(td),
                           stdin=subprocess.DEVNULL, capture_output=True)
    out = p.stdout.decode("utf-8", "replace").strip()
    return pathlib.Path(out).resolve() if p.returncode == 0 and out else None


def write_before_image(target, step_id: str, derive_after) -> dict[str, bytes | None]:
    """The after-state `{path: bytes, or None for removed}` of `step_id`'s up at `target`, with its
    before-image written first.

    With no image, `derive_after(None)` runs the step's pre-write reads against the working tree and
    names every path it will write or remove; the image then records each path's working-tree bytes
    and the sha256 of what the up leaves. An image already there is never overwritten:
    `derive_after` is handed its before bytes instead, and its answer must hash to the image's
    after-hashes, so a re-run over a killed up converges on the first image or refuses.

    The image is written through `write_atomic` (TOOL-dSafePassage-26 S31). One that does not parse,
    an older writer's cut short, reads absent only when no path it lists changed after it was
    written (`read_image_changes`), and is removed; otherwise the up refuses naming it, since its
    before bytes are lost and a down could not restore them."""
    image = derive_image_path(target, step_id)
    held = None
    if image.is_file():
        text = image.read_text(encoding="utf-8", errors="replace")
        try:
            held = json.loads(text)["paths"]
        except (ValueError, KeyError, TypeError):
            changed = read_image_changes(target, image, text)
            if changed:
                raise Refusal(f"{image.relative_to(target).as_posix()}: the before-image does not parse "
                              f"and {', '.join(changed)} changed after it was written, so its before "
                              f"bytes are lost; restore those paths by hand, then remove the image")
            image.unlink()
    if held is not None:
        for p in held:
            check_contained(target, p)  # S6: no path's before bytes reach `derive_after` untested
        before = {p: None if v["before"] is None else base64.b64decode(v["before"]) for p, v in held.items()}
        after = derive_after(before)
        if set(after) != set(held) or any(
                (None if b is None else hashlib.sha256(b).hexdigest()) != held[p]["after"] for p, b in after.items()):
            raise Refusal(f"{image.relative_to(target).as_posix()}: this re-run computes another "
                          f"after-state than the before-image records, so it would not converge; "
                          f"run the step's down first")
        return after
    after = derive_after(None)
    if not after:
        return after
    paths = {}
    for p, data in sorted(after.items()):
        cur = check_contained(target, p)
        was = cur.read_bytes() if cur.is_file() else None
        paths[p] = {"before": None if was is None else base64.b64encode(was).decode("ascii"),
                    "after": None if data is None else hashlib.sha256(data).hexdigest()}
    image.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(image, json.dumps({"step": step_id, "paths": paths}, indent=2, sort_keys=True) + "\n")
    return after


IMAGE_ENTRY_RE = re.compile(r'^    ("(?:[^"\\]|\\.)*"): \{\s*"after": (?:null|"[0-9a-f]*"),\s*"before": (null|")?',
                            re.M)


def read_image_changes(target, image: pathlib.Path, text: str) -> list[str]:
    """The paths a before-image that does not parse lists and that changed after it was written,
    read from its legible entries (`write_before_image`'s layout): a path present and modified after
    the image, or absent where the image recorded bytes or its entry is cut before saying. [] means
    the image may be read as absent."""
    since = image.stat().st_mtime_ns
    changed = []
    for m in IMAGE_ENTRY_RE.finditer(text):
        rel = json.loads(m[1])
        cur = check_contained(target, rel)
        if cur.stat().st_mtime_ns > since if cur.is_file() else m[2] != "null":
            changed.append(rel)
    return changed


def write_from_before_image(target, step_id: str) -> list[str]:
    """Restore every path `step_id`'s before-image records, then remove the image: the down.

    A path is restored only where it still holds the image's after-hash or its before bytes; any
    other path refuses the whole down, naming it, and nothing is written. No image is nothing to
    restore and returns []. Returns the paths restored."""
    image = derive_image_path(target, step_id)
    if not image.is_file():
        return []
    held = json.loads(image.read_text(encoding="utf-8"))["paths"]
    plan, edited = [], []
    for p, v in sorted(held.items()):
        cur = check_contained(target, p)
        now = cur.read_bytes() if cur.is_file() else None
        was = None if v["before"] is None else base64.b64decode(v["before"])
        if now == was or (None if now is None else hashlib.sha256(now).hexdigest()) == v["after"]:
            plan.append((p, cur, was))
        else:
            edited.append(p)
    if edited:
        raise Refusal(f"{', '.join(edited)}: changed since the step's up, so its down would discard "
                      f"that edit; nothing was restored")
    for _p, cur, was in plan:
        if was is None:
            cur.unlink(missing_ok=True)
        else:
            cur.parent.mkdir(parents=True, exist_ok=True)
            cur.write_bytes(was)
    image.unlink()
    for d in (image.parent, image.parent.parent):
        try:
            d.rmdir()
        except OSError:
            break  # ponytail: not empty, another step's image is there
    return [p for p, _c, _w in plan]


def read_step_states(receipt: dict) -> list[dict]:
    """The receipt's `steps` rows, validated: the field's one parser (TOOL-dSafePassage-3, S3).

    A receipt below schema 4 has no rows and may carry no field; one at schema 4 or above must carry
    a list of `{"id", "introduced", "state"}` objects, `state` one of STEP_STATES, an optional
    `failure` as `test_step_row` admits it (TOOL-dSafePassage-43, -49 S16), a null one read as absent,
    `introduced` a 40-hex commit or null, and an `applied` row optionally `"via": "witness"`, the
    walk having applied it by its witness alone (TOOL-dSafePassage-33). Anything else is a refusal
    naming the row, and nothing is repaired."""
    schema = receipt.get("schema", 1)
    at4 = isinstance(schema, int) and not isinstance(schema, bool) and schema >= 4
    if not at4:
        if "steps" in receipt:
            raise Refusal(f"`steps` on a receipt at schema {schema!r}: the field is schema 4's")
        return []
    steps = receipt.get("steps")
    if not isinstance(steps, list):
        raise Refusal(f"a schema-{schema} receipt's `steps` is "
                      + ("absent" if "steps" not in receipt else type(steps).__name__)
                      + ", and schema 4 requires a list")
    for n, row in enumerate(steps, 1):
        at = f"`steps` row {n}" + (f" ({row.get('id')!r})" if isinstance(row, dict) else "")
        if not isinstance(row, dict):
            raise Refusal(f"{at} is {type(row).__name__}, not an object")
        state = row.get("state")
        # TOOL-dSafePassage-33 S1: `via` is legal only as "witness" on an applied row, so a bad mark
        # fails the key-set test below and joins its refusal rather than adding a branch. Whether a
        # `failure` belongs on the row is `test_step_row`'s alone (TOOL-dSafePassage-49 S16).
        marked = state == "applied" and row.get("via") == "witness"
        want = ({"id", "introduced", "state"} | ({"failure"} if "failure" in row else set())
                | ({"via"} if marked else set()))
        if set(row) != want:
            raise Refusal(f"{at} carries the keys {sorted(row)}, where a {state!r} row carries {sorted(want)}"
                          + (f"; `via` {row['via']!r} is legal only as 'witness' on an applied row"
                             if "via" in row and not marked else ""))
        if not isinstance(row["id"], str) or not row["id"]:
            raise Refusal(f"{at}: `id` is not a non-empty string")
        if state not in STEP_STATES:
            raise Refusal(f"{at}: `state` {state!r} is not one of {', '.join(STEP_STATES)}")
        test_step_row(row["id"], state, row.get("failure"))
        intro = row["introduced"]
        if intro is not None and not (isinstance(intro, str) and SHA_RE.fullmatch(intro)):
            raise Refusal(f"{at}: `introduced` {intro!r} is neither a 40-hex commit nor null")
    return steps


def test_step_row(step_id, state, failure) -> None:
    """The row rule (TOOL-dSafePassage-49 S16, S9): None where a `state` row of `step_id` may carry
    `failure`, else a `Refusal` naming the step, and the text where it is one. `failure` is None or
    a non-empty string in every state; an `applied` row carries none or a stopped down's, opening
    with an entry of DOWN_STOP_PREFIXES; a `failed` row carries one; a `rolled-back` row none.
    `set_step_state` and `read_step_states` both call it, so the writer and the reader never
    disagree; a state outside STEP_STATES is the reader's refusal, not this rule's."""
    if failure is not None and not (isinstance(failure, str) and failure):
        raise Refusal(f"{step_id!r}: `failure` {failure!r} is neither absent nor a non-empty string")
    if state == "applied" and failure is not None and not failure.startswith(DOWN_STOP_PREFIXES):
        raise Refusal(f"{step_id!r}: an applied row's `failure` {failure!r} opens with none of the down "
                      f"stops {', '.join(map(repr, DOWN_STOP_PREFIXES))}, and an applied row carries "
                      f"only a stopped down's")
    if state == "failed" and failure is None:
        raise Refusal(f"{step_id!r}: a failed row's `failure` is a non-empty string, and this row has none")
    if state == "rolled-back" and failure is not None:
        raise Refusal(f"{step_id!r}: a rolled-back row carries no `failure`, and this one carries {failure!r}")


def test_steps_recordable(receipt: dict) -> bool:
    """True exactly when `set_step_state` may record a row on `receipt`: its `schema` an int of 4
    or more and its `steps` a list (TOOL-dSafePassage-16). It reads and writes nothing; every
    caller asks it before a record, and the writer refuses by it, so the two never disagree."""
    schema = receipt.get("schema")
    return (isinstance(schema, int) and not isinstance(schema, bool) and schema >= 4
            and isinstance(receipt.get("steps"), list))


def resolve_recorded_introduced(value):
    """The `introduced` the step record stores for the reader's `value` (TOOL-dSafePassage-20): a
    40-hex commit unchanged, None for `UNLANDED` or None, and a refusal naming anything else, so the
    reader's every output kind crosses the one writer and the stored domain stays 40-hex or null."""
    if value is None or value == UNLANDED:
        return None
    if isinstance(value, str) and SHA_RE.fullmatch(value):
        return value
    raise Refusal(f"`introduced` {value!r} is neither a 40-hex commit, the reader's {UNLANDED!r} nor null")


def set_step_state(receipt: dict, step_id, introduced, state, failure=None, via=None) -> dict:
    """Record `step_id` at `state` in the receipt's `steps`: the field's one writer (S3).

    The row moves to the end, so the last `applied` row is the last completed step; a known
    `introduced` survives a call passing None. `via` is written when given, and only "witness" on
    an `applied` row is legal (TOOL-dSafePassage-33); a call passing none keeps the row's mark
    while the row stays `applied` and drops it on a state change (TOOL-dSafePassage-39), so no
    caller passes the mark back by hand. It refuses a receipt `test_steps_recordable` rejects and any row
    `read_step_states` would refuse, mutates `receipt` and persists nothing: the caller writes it.

    The bootstrap: before schema 4 no step row is persisted, so a step's failure or interruption
    on such a receipt goes to `update`'s output and findings only; the `govkit/receipt-schema-4`
    row is written after that step's post-spawn re-read shows schema 4, through this writer, like
    any other row (TOOL-dSafePassage-16).

    `introduced` is the reader's value as `read_steps` returns it: `resolve_recorded_introduced`
    maps it first, so the reader's `unlanded` records null (TOOL-dSafePassage-20)."""
    introduced = resolve_recorded_introduced(introduced)
    test_step_row(step_id, state, failure)
    schema = receipt.get("schema", 1)
    if not test_steps_recordable(receipt):
        raise Refusal(f"a receipt at schema {schema!r} has no `steps` to record '{step_id}' in: a "
                      f"step row is recorded only where `schema` is a number of 4 or more and "
                      f"`steps` is a list; the step govkit/receipt-schema-4 takes it to schema 4 first")
    row = {"id": step_id, "introduced": introduced, "state": state}
    if failure is not None:
        row["failure"] = failure
    if via is not None:
        row["via"] = via
    rows = read_step_states(receipt)
    old = next((r for r in rows if r["id"] == step_id), None)
    if introduced is None and old is not None:
        row["introduced"] = old["introduced"]
    if via is None and state == "applied" and old is not None and old["state"] == "applied" and "via" in old:
        row["via"] = old["via"]  # TOOL-dSafePassage-39 S1: the carry, keyed on the state alone
    read_step_states({"schema": schema, "steps": [row]})  # the writer refuses what the reader would
    receipt["steps"] = [r for r in rows if r["id"] != step_id] + [row]
    return row


def render_toml_scalar(value) -> str:
    """`value`, a bool, int, float or string, in TOML's spelling."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    raise Refusal(f"no TOML scalar spelling for {value!r}")


def render_policy_text(text: str | None, table: str, key: str, value) -> str:
    """`text`, a policy file's, with `key` set to `value` in `[table]`, every other byte kept.

    A line editor: the key's line in the table is rewritten, else one line is added after the
    table's last non-blank line, else the table is appended; the file's line ending and any BOM are
    kept. It refuses its own output unless tomllib reads `value` back at `table.key`, so a key held
    elsewhere (a dotted key, an inline table) is refused rather than shadowed."""
    text = text or ""
    nl = "\r\n" if "\r\n" in text else "\n"
    kspell = key if re.fullmatch(r"[A-Za-z0-9_-]+", key) else json.dumps(key)
    line = f"{kspell} = {render_toml_scalar(value)}"
    lines = text.splitlines(keepends=True)
    header = next((i for i, ln in enumerate(lines)
                   if re.fullmatch(rf"\ufeff?[ \t]*\[[ \t]*{re.escape(table)}[ \t]*\][ \t]*(?:#.*)?", ln.rstrip("\r\n"))), None)
    if header is None:
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += nl
        lines += ([nl] if any(ln.strip() for ln in lines) else []) + [f"[{table}]{nl}", f"{line}{nl}"]
    else:
        end = next((i for i in range(header + 1, len(lines)) if re.match(r"[ \t]*\[", lines[i])), len(lines))
        keyed = re.compile(rf"[ \t]*(?:{re.escape(key)}|{re.escape(json.dumps(key))})[ \t]*=")
        hit = next((i for i in range(header + 1, end) if keyed.match(lines[i])), None)
        if hit is not None:
            # ponytail: the rewritten line drops its own trailing comment, since telling a comment
            # from a `#` inside a string takes a TOML lexer; the down restores the bytes either way.
            lines[hit] = line + (lines[hit][len(lines[hit].rstrip("\r\n")):] or nl)
        else:
            last = max(i for i in range(header, end) if lines[i].strip())
            if not lines[last].endswith("\n"):
                lines[last] += nl
            lines.insert(last + 1, f"{line}{nl}")
    out = "".join(lines)
    try:
        got = tomllib.loads(out.removeprefix("\ufeff")).get(table, {}).get(key)
    except (tomllib.TOMLDecodeError, AttributeError) as e:
        raise Refusal(f"setting {table}.{key} leaves text tomllib does not read: {e}") from None
    if got != value or type(got) is not type(value):
        raise Refusal(f"setting {table}.{key} to {render_toml_scalar(value)} does not read back "
                      f"(tomllib reads {got!r}), so the edit is refused rather than written")
    return out


LINE_ENDING_KEYS = ("core.autocrlf", "core.eol")


def read_line_ending_config(cwd=None) -> list[tuple[str, str]]:
    """The parent's effective `core.autocrlf` and `core.eol` (TOOL-dSafePassage-26 S13), each pair
    only where some scope sets the key, by one `git config` read in `cwd`. The parent's environment
    less git's location variables, so a calling hook's `GIT_DIR` cannot point the read elsewhere."""
    env = {k: v for k, v in os.environ.items()
           if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_PREFIX")}
    try:
        p = subprocess.run(["git", *(["-C", str(cwd)] if cwd else []), "config", "--get-regexp",
                            r"^core\.(autocrlf|eol)$"], capture_output=True, text=True, encoding="utf-8",
                           errors="replace", env=env, stdin=subprocess.DEVNULL)
    except OSError:
        return []
    got = {}
    for ln in p.stdout.splitlines():
        k, _sep, v = ln.partition(" ")
        got[k.lower()] = v  # the last scope printed wins, as git's own read does
    return [(k, got[k]) for k in LINE_ENDING_KEYS if k in got]


def build_step_env(scratch, target=None) -> dict[str, str]:
    """The environment a step runs under (TOOL-dSafePassage-7, S1): a NEW dict of the
    `STEP_ENV_KEEP` names present in the parent, plus the contract's own. Home and temp point into
    `scratch`; git reads no system or global config and prompts for nothing, and through
    `GIT_CONFIG_COUNT`, which outranks the target's own config, runs hooks from the empty
    `<scratch>/no-hooks`, holds the empty credential helper, and refuses the `ext::` transport
    whatever a local `protocol.*`, `url.*` or `remote.*` key says (TOOL-dSafePassage-37 S3). The
    parent's effective `core.autocrlf` and `core.eol` in `target` follow as further pairs, so a
    step hashes and stages as the parent would (TOOL-dSafePassage-26 S13): the count is 3 plus them."""
    scratch = pathlib.Path(scratch)
    env = {k: os.environ[k] for k in STEP_ENV_KEEP if k in os.environ}
    env.update(dict.fromkeys(("HOME", "USERPROFILE", "APPDATA", "LOCALAPPDATA", "XDG_CONFIG_HOME"),
                             str(scratch / "home")))
    env.update(dict.fromkeys(("TMP", "TEMP", "TMPDIR"), str(scratch / "tmp")))
    pairs = [("core.hooksPath", str(scratch / STEP_HOOKS_DIR)), ("credential.helper", ""),
             ("protocol.ext.allow", "never"), *read_line_ending_config(target)]
    env.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull, "GIT_TERMINAL_PROMPT": "0",
                "GCM_INTERACTIVE": "never", "GIT_CONFIG_COUNT": str(len(pairs))})
    for i, (k, v) in enumerate(pairs):
        env[f"GIT_CONFIG_KEY_{i}"], env[f"GIT_CONFIG_VALUE_{i}"] = k, v
    return env


def resolve_step_argv(argv, ctx: dict[str, str], step_id: str = "a step") -> list[str]:
    """`argv` resolved for the contract (S2): `{gov}`, `{target}` and `{prefix}` from `ctx` through
    `resolve_tokens`, a leading `python` as govkit's own interpreter and `-I`, a leading
    `bash` through `resolve_shell_argv`. A token `ctx` does not answer is a refusal naming the step
    and the token, before any spawn."""
    out = []
    for tok in argv:
        got, missing = resolve_tokens(tok, ctx)
        if missing:
            raise Refusal(f"{step_id}: '{tok}' holds {', '.join('{' + m + '}' for m in missing)}, which "
                          f"this run does not answer, so nothing was spawned")
        out.append(got)
    if out and out[0] == "python":
        return [sys.executable, "-I", *out[1:]]
    return resolve_shell_argv(out)


def derive_step_context(row: StepRow, target, gov_root, to: str | None = None) -> dict[str, str]:
    """The placeholder answers a step argv resolves against: `{gov}` gov's tool root, `{target}`
    the target, `{prefix}` the target's install prefix where it has a `deploy.toml`, and `{to}` the
    rollback's 40-hex `--to` where the caller passes it, which only a down of `update --rollback`
    does (TOOL-dSafePassage-26 S10); anywhere else `{to}` is unanswered and refused by
    `resolve_step_argv`. One derivation for the spawn and for the attended order."""
    gk = load_govkit()
    target, gov_root = pathlib.Path(target).resolve(), pathlib.Path(gov_root).resolve()
    tr = gk.derive_tool_root(gov_root)
    ctx = {"gov": (gov_root / tr if tr else gov_root).as_posix(), "target": target.as_posix()}
    if (target / ".governance" / "deploy.toml").is_file():
        ctx["prefix"] = target_context(target, gk.load_deploy(target), row.id.split("/", 1)[0], {})["prefix"]
    if to:
        ctx["to"] = to
    return ctx


def derive_step_mode(row: StepRow) -> str:
    """`attended` for a row declaring `needs-target = true`, which no runner spawns, else
    `isolated`: the row runs under the contract."""
    return "attended" if row.needs_target else "isolated"


def test_path_linked(path) -> bool:
    """True when `path` is a symlink or a junction (TOOL-dSafePassage-56 S1), which `S_ISLNK` alone
    reads False on: one `lstat`, so no link is followed, its reparse tag refusing a junction and any
    other reparse point (TOOL-dSafePassage-59 S5). An absent path reads False."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(st.st_mode) or getattr(st, "st_reparse_tag", 0) != 0


def read_target_repositories(target, read_config) -> list[dict[str, str]] | str:
    """Every repository a git command run in `target` can enter (TOOL-dSafePassage-30 S1), as
    `{"git_dir", "reached_by"}` rows, the target's own first with `reached_by` empty: each gitlink
    of a repository's index whose working directory holds a `.git` entry, walked again over that
    repository's index, and every directory under `<git dir>/modules/` (a submodule's own git
    directory for one) shaped as git opens one, populated or not, the target's `<git dir>` its own
    worktree's (TOOL-dSafePassage-36 S1), never the common one. Each is listed once by its resolved
    path. `read_config(git_dir, reached_by)` reads and grades each repository's config before any
    index-reading command runs in it, and a repository it returns True for is refused, its index
    never read (TOOL-dSafePassage-42 S8). A `modules/` row's `reached_by` is the path its worktree's
    `.gitmodules` maps the name to, or the name and `, by name` where none does (S22). Every git
    call runs under `build_step_env`'s environment; one that fails, or a `Refusal` `read_config`
    raises, returns the call and git's exit as a string, never an empty population."""
    with tempfile.TemporaryDirectory(prefix="gk-repos-", ignore_cleanup_errors=True) as td:
        env = build_step_env(td)

        def run_repo_git(cwd, *args, ok=(0,), reads: str = "") -> str:
            p = subprocess.run(["git", "-C", str(cwd), *args], env=env, stdin=subprocess.DEVNULL,
                               capture_output=True)
            if p.returncode not in ok:
                raise Refusal(f"`git -C {pathlib.Path(cwd).as_posix()} {' '.join(args)}` exits {p.returncode}"
                              + (f", so {reads} does not read" if reads else "")
                              + f": {p.stderr.decode('utf-8', 'replace').strip()}")
            return p.stdout.decode("utf-8", "replace")

        def read_submodule_paths(work) -> dict[str, str]:
            """name -> path of `work`'s `.gitmodules`; `config -f` reads that one file and runs nothing.
            Exit 1 maps none; any other exit is a refusal naming the file (TOOL-dSafePassage-45 S13).
            One that exists and is not a regular file is a refusal naming it first, so exit 1 means
            only "missing, or maps none" (TOOL-dSafePassage-49 S18). The type test is one `lstat`
            before any open, git's read included, since an open of a FIFO blocks (TOOL-dSafePassage-51
            S15, read as TOOL-dSafePassage-59 S8): finding nothing is missing; a link, a junction or any
            other reparse point refuses unfollowed; then anything not a regular file refuses."""
            gm = None if work is None else work / ".gitmodules"
            if gm is None:
                return {}
            try:
                st = os.lstat(gm)
            except FileNotFoundError:
                return {}
            except OSError as e:
                raise Refusal(f"{gm.as_posix()} does not read: it is no regular file ({e}), "
                              f"so which path each submodule name maps to is unknown") from None
            if stat.S_ISLNK(st.st_mode) or getattr(st, "st_reparse_tag", 0) != 0:
                raise Refusal(f"{gm.as_posix()} does not read: it is a link, which is never followed, "
                              f"so which path each submodule name maps to is unknown")
            if not stat.S_ISREG(st.st_mode):
                raise Refusal(f"{gm.as_posix()} does not read: it is no regular file (its mode is "
                              f"{stat.filemode(st.st_mode)}), so which path each submodule name maps to "
                              f"is unknown")
            out = run_repo_git(work, "config", "-z", "-f", ".gitmodules", "--get-regexp", r"^submodule\..*\.path$",
                      ok=(0, 1), reads=(work / ".gitmodules").as_posix())
            return {k[len("submodule."):-len(".path")]: v
                    for k, _, v in (e.partition("\n") for e in out.split("\0") if e)}

        rows: list[dict[str, str]] = []
        seen: set[pathlib.Path] = set()

        def add(git_dir, reached_by: str, work, mark: str = "") -> None:
            d = pathlib.Path(git_dir).resolve()
            if d not in seen:
                seen.add(d)
                rows.append({"git_dir": d.as_posix(), "reached_by": reached_by + mark})
                queue.append((d, reached_by, work, reached_by + mark))

        queue: list[tuple[pathlib.Path, str, pathlib.Path | None, str]] = []
        try:
            target = pathlib.Path(target)
            add(run_repo_git(target, "rev-parse", "--absolute-git-dir").strip(), "", target)
            while queue:
                d, via, work, label = queue.pop(0)
                # graded first: an index read runs `core.fsmonitor`, so a refused repository's never runs
                if not read_config(d, label) and work is not None:
                    for ent in run_repo_git(work, "-c", "core.fsmonitor=false", "ls-files", "-s", "-z").split("\0"):
                        meta, _, path = ent.partition("\t")
                        if meta.startswith("160000 ") and (work / path / ".git").exists():
                            add(run_repo_git(work / path, "rev-parse", "--absolute-git-dir").strip(),
                                f"{via}/{path}".lstrip("/"), work / path)
                if work is None:
                    # TOOL-dSafePassage-49 S7: a `modules/` candidate git will not open, a newer
                    # format for one, reads its config with only a warning, so its keys would be
                    # graded where no step can reach them; after a read that exited 0, any non-zero
                    # exit here refuses, naming it, whatever git's stderr says.
                    opened = subprocess.run(["git", f"--git-dir={d}", "rev-parse", "--git-dir"], cwd=str(d),
                                            env=env, stdin=subprocess.DEVNULL, capture_output=True)
                    if opened.returncode:
                        raise Refusal(f"{d.as_posix()}: git will not open this repository, `git --git-dir="
                                      f"{d.as_posix()} rev-parse --git-dir` exits {opened.returncode}, so the "
                                      f"keys its config lists are none a step reaches through git: "
                                      f"{opened.stderr.decode('utf-8', 'replace').strip()}")
                mods = d / "modules"  # a linked worktree's submodules sit under its own git dir
                # TOOL-dSafePassage-45 S12, read as TOOL-dSafePassage-47 S1 to S3: a repository by
                # git's own directory shape, so no ref or object tree is taken for one. A candidate
                # is listed and only its own `modules/` walked; any other directory is a segment of
                # a name holding `/`. A name's path is mapped through the worktree `w` whose
                # `.gitmodules` declares it, or the name stands, marked `by name` (S13).
                # TOOL-dSafePassage-51 S6: no link is followed, a junction included, which
                # `islink` reads False on; a link, or a directory that will not list, refuses.
                # TOOL-dSafePassage-53: a path git never created is the empty population, the
                # worklist's `continue` being one walk's return; any other listing error refuses.
                # TOOL-dSafePassage-56 S2: every path entered, the root and each `<c>/modules`, is
                # tested for a link before it is listed, so a dangling one is never read as absent.
                walks = [(mods, mods, work, [], "")]
                while walks:
                    base, cur, w, parts, mark = walks.pop(0)
                    if test_path_linked(cur):
                        raise Refusal(f"{cur.as_posix()} is a link the walk would enter, which it never "
                                      f"follows, so where it leads is unknown")
                    try:
                        with os.scandir(cur) as it:
                            listed = sorted(it, key=lambda e: e.name)
                    except FileNotFoundError:
                        continue
                    except OSError as e:
                        raise Refusal(f"{cur.as_posix()} does not list ({type(e).__name__}: {e}), so the "
                                      f"repositories under it are unknown") from None
                    # TOOL-dSafePassage-59 S7: every entry is tested before any type filter, so a
                    # dangling link, or a link to a file, is refused by name, never dropped.
                    for e in listed:
                        c = cur / e.name
                        if test_path_linked(c):
                            raise Refusal(f"{c.as_posix()} is a link under modules/, which the walk never "
                                          f"follows, so where it leads is unknown")
                        if not e.is_dir(follow_symlinks=False):
                            continue
                        if not ((c / "HEAD").is_file() and (c / "objects").is_dir() and (c / "refs").is_dir()):
                            walks.append((base, c, w, parts, mark))
                            continue
                        p = read_submodule_paths(w).get(c.relative_to(base).as_posix())
                        here, m = [*parts, p or c.relative_to(base).as_posix()], mark if p else ", by name"
                        add(c, f"{via}/{'/'.join(here)}".lstrip("/"), None, m)
                        walks.append((c / "modules", c / "modules",
                                      w / p if p and (w / p / ".git").exists() else None, here, m))
        except Refusal as e:
            return str(e)
    return rows


def read_target_local_config(target, refused) -> list[tuple[str, str, str | None, str]] | str:
    """The config rows of every repository `read_target_repositories` finds (TOOL-dSafePassage-24
    S1, TOOL-dSafePassage-30 S2): `git --git-dir=<dir> config --list --show-scope --show-origin
    --includes -z` run in the target under `build_step_env`'s environment, so system and global are
    off, keeping the `local` and `worktree` rows, an included file's among them, as (origin file,
    key, value or None for a bare key, the submodule path reaching it or empty). Each repository's
    rows are read, and graded by `refused(*row)`, as the walk reaches it, before its index is read
    (TOOL-dSafePassage-42 S8). A git dir under the target is passed relative to it, so its origin
    reads `.git/...`. A read that fails returns git's exit and stderr as a string."""
    root, rows = pathlib.Path(target).resolve(), []
    with tempfile.TemporaryDirectory(prefix="gk-cfg-", ignore_cleanup_errors=True) as td:
        def read(d: pathlib.Path, via: str) -> bool:
            gd = d.relative_to(root).as_posix() if d.is_relative_to(root) else d.as_posix()
            p = subprocess.run(["git", "-C", str(target), f"--git-dir={gd}", "config", "--list", "--show-scope",
                                "--show-origin", "--includes", "-z"], env=build_step_env(td),
                               stdin=subprocess.DEVNULL, capture_output=True)
            if p.returncode != 0:
                raise Refusal(f"`git config --list` over {gd} exits {p.returncode}, so {gd}/config or a file it includes does not read: "
                              f"{p.stderr.decode('utf-8', 'replace').strip()}")
            f, mine = p.stdout.decode("utf-8", "replace").split("\0"), []
            for scope, origin, kv in zip(f[0::3], f[1::3], f[2::3]):
                if scope in ("local", "worktree"):
                    key, nl, value = kv.partition("\n")
                    mine.append((origin.removeprefix("file:"), key, value if nl else None, via))
            rows.extend(mine)
            return any(refused(*r) for r in mine)

        repos = read_target_repositories(target, read)
    return repos if isinstance(repos, str) else rows


# TOOL-dSafePassage-38 §4: a `<scheme>://` URL carrying userinfo before its host, and the
# credential-file keys, `<x>` any one or more segments.
CONFIG_USERINFO_RE = re.compile(r"(?i)\b([a-z][a-z0-9+.-]*)://([^/\s@]+)@")
# TOOL-dSafePassage-45 S7: a proxy value is `[protocol://][user[:password]@]proxyhost[:port]`, so its
# userinfo needs no scheme; the keys it is tested on, `<x>` any one or more segments.
PROXY_USERINFO_RE = re.compile(r"(?i)^(?:[a-z][a-z0-9+.-]*://)?[^/\s@]+@")
PROXY_KEY_RE = re.compile(r"(?i)http\.(?:.+\.)?proxy|remote\..+\.proxy")
# S9: the redactor runs to the LAST `@` before the first `/`, so a raw `@` in a password goes too.
REDACT_USERINFO_RE = re.compile(r"(?i)\b([a-z][a-z0-9+.-]*)://[^/\s]*@")
# TOOL-dSafePassage-44 S1: a bare user under these schemes is ssh's login name, not a credential.
SSH_BARE_USER_SCHEMES = ("ssh", "git+ssh", "ssh+git")
# TOOL-dSafePassage-45 S10: the credential keys, held by selftest's credential arm to every key of
# `git help --config` whose last segment, lowercased, ends in a suffix here: each matches one row,
# refused or kept with its reason, or a `STEP_REFUSED_KEYS` row (`core.askPass`). As (key pattern,
# row, why), `<x>` any one or more segments; derived over git 2.54.0.windows.1, node d, 2026-10-23.
CREDENTIAL_KEY_SUFFIXES = ("pass", "key", "cert", "cookiefile", "seed")
STEP_CREDENTIAL_KEYS = (
    *((k, "refused", "read as a client credential") for k in (
        "http.sslKey", "http.<x>.sslKey", "http.sslCert", "http.<x>.sslCert", "http.cookieFile",
        "http.<x>.cookieFile", "http.proxySSLKey", "http.<x>.proxySSLKey", "http.proxySSLCert",
        "http.<x>.proxySSLCert")),
    *((k, "refused", "a stored secret") for k in (
        "imap.pass", "gitcvs.dbPass", "receive.certNonceSeed", "sendemail.smtpPass",
        "sendemail.<x>.smtpPass", "sendemail.smtpSSLClientKey", "sendemail.<x>.smtpSSLClientKey",
        "sendemail.smtpSSLClientCert", "sendemail.<x>.smtpSSLClientCert")),
    ("user.signingKey", "kept", "a public key or its id"),
    ("http.pinnedPubkey", "kept", "a public key or its id"),
    ("interactive.singleKey", "kept", "a boolean"),
    ("http.sslAutoClientCert", "kept", "a boolean"),
    ("trailer.<x>.key", "kept", "a trailer's name"))
CREDENTIAL_FILE_KEY_RE = re.compile("|".join(re.sub(r"<[^>]+>", ".+", re.escape(k))
                                             for k, row, _why in STEP_CREDENTIAL_KEYS if row == "refused"), re.I)


def test_credential_bearing(key: str, value: str | None) -> bool:
    """True when `value`, or the key's whole subsection, its text between the first and the last
    dot, holds a URL carrying userinfo (TOOL-dSafePassage-38 S1, TOOL-dSafePassage-45 S8), when a
    proxy key's value holds userinfo with or without a scheme (S7), or when `key` matches a refused
    `STEP_CREDENTIAL_KEYS` row (S10). An scp-form `user@host:path` holds no `://` and is not
    credential-bearing, and neither is a bare user, no `:` in it, under a scheme
    `SSH_BARE_USER_SCHEMES` names, read from the match inside the tested text (TOOL-dSafePassage-44 S1)."""
    inner = key.split(".", 1)[1].rpartition(".")[0] if key.count(".") >= 2 else ""
    return bool(CREDENTIAL_FILE_KEY_RE.fullmatch(key) or any(
        not (m.group(1).lower() in SSH_BARE_USER_SCHEMES and ":" not in m.group(2))
        for text in (inner, value or "") for m in CONFIG_USERINFO_RE.finditer(text))
        or (PROXY_KEY_RE.fullmatch(key) and PROXY_USERINFO_RE.match((value or "").strip())))


def render_redacted_config(text: str) -> str:
    """`text` with the userinfo of every `<scheme>://<userinfo>@` written as `<redacted>`, to the
    last `@` before the first `/` (TOOL-dSafePassage-45 S9), scheme and host kept
    (TOOL-dSafePassage-38 S2). `text` read as a key first: its tested subsection, the text between
    its first and its last `.`, is redacted from its first `<scheme>://` to its last `@`, whatever
    lies between, so a password holding a space or a `/` goes too (TOOL-dSafePassage-49 S19)."""
    first, last = text.find("."), text.rfind(".")
    if 0 <= first < last:
        inner = text[first + 1:last]
        m, at = re.search(r"(?i)\b[a-z][a-z0-9+.-]*://", inner), inner.rfind("@")
        if m and at >= m.end():
            text = text[:first + 1] + inner[:m.end()] + "<redacted>" + inner[at:] + text[last:]
    return REDACT_USERINFO_RE.sub(lambda m: m.group(0).partition("://")[0] + "://<redacted>@", text)


def check_target_local_config(target) -> list[str]:
    """Each kept row of `read_target_local_config` that a `STEP_REFUSED_KEYS` row matches, its key
    by the pattern and its value by the row's rule (a bare key holds git's true), or that
    `test_credential_bearing` holds True for, as `<key> in <file>`, `(submodule <path>)` after it
    for a row outside the target's own repository, every entry through `render_redacted_config`
    and none carrying a value (TOOL-dSafePassage-24 S2, TOOL-dSafePassage-29 S1,
    TOOL-dSafePassage-30 S3, TOOL-dSafePassage-38 S1 S2). A walk or read that failed is a `Refusal`
    carrying its reason through `render_redacted_config`, never a found key (TOOL-dSafePassage-76 S8)."""
    def check_refused(origin: str, key: str, value: str | None, via: str) -> bool:
        return test_credential_bearing(key, value) or any(
            re.fullmatch(re.sub(r"<[^>]+>", ".+", re.escape(pattern)), key, re.I)
            and (rule == "any"
                 or (rule == "not a git false" and (value is None or value.strip().lower() not in GIT_FALSE))
                 or (rule == "begins with !" and value is not None and value.startswith("!"))
                 or (rule == "an absolute path" and value is not None
                     and re.match(r"[/\\]|[A-Za-z]:", value.strip())))
            for pattern, rule, _runs in STEP_REFUSED_KEYS)

    rows = read_target_local_config(target, check_refused)
    if isinstance(rows, str):
        raise Refusal(render_redacted_config(rows))
    return [render_redacted_config(key) + render_redacted_config(f" in {origin}" + (f" (submodule {via})" if via else ""))
            for origin, key, value, via in rows if check_refused(origin, key, value, via)]


def run_step_isolated(row: StepRow, phase: str, target, gov_root, to: str | None = None) -> dict:
    """Run `phase` of `row` under the contract: the step kind's ONE spawn of a step argv (S3), so the
    walk, the reverse walk, gov first and the leg inherit the contract by calling it.

    From gov's checkout root, with `build_step_env` over a scratch made for the call and cleared
    after it, and `resolve_step_argv`'s argv; output decoded as `run_target_argv` decodes it.
    Returns `{"verdict": "ok" | "failed" | "attended", "rc", "tail"}`, `tail` stderr's last 20
    lines, or, for an up or a down that exits non-zero with nothing on stderr, one line naming that
    and stdout's last line (TOOL-dSafePassage-69 S4). A row that needs target code is `attended` and spawns nothing, but for its witness on
    gov's own tree, source mode, where the target's code is gov's (TOOL-dSafePassage-26 S32); a
    spawn error is `failed` with `rc` None; a phase with no argv is a refusal, and so is a target whose own git
    config `check_target_local_config` finds an executor or a credential in (TOOL-dSafePassage-24).
    `to`, the rollback's `--to`, answers `{to}` in a `down` only (TOOL-dSafePassage-26 S10)."""
    source = pathlib.Path(target).resolve() == pathlib.Path(gov_root).resolve()
    if derive_step_mode(row) == "attended" and not (source and phase == "witness"):
        return {"verdict": "attended", "rc": None, "tail": ""}
    if phase not in STEP_PHASES or not isinstance(getattr(row, phase), list):
        raise Refusal(f"{row.id}: no `{phase}` argv to run; a step runs one of {', '.join(STEP_PHASES)}")
    try:
        found = check_target_local_config(target)
    except Refusal as e:
        raise Refusal(f"{row.id} {phase}: the repositories a step could enter from the target could not be "
                      f"cleared: {e}, so nothing was spawned") from None
    if found:
        raise Refusal(f"{row.id} {phase}: the target's own git config declares what git runs as a program "
                      f"or sends as a credential, {', '.join(found)}, so nothing was spawned: remove it, "
                      f"or run the step attended")
    gov_root = pathlib.Path(gov_root).resolve()
    ctx = derive_step_context(row, target, gov_root, to if phase == "down" else None)
    with tempfile.TemporaryDirectory(prefix="gk-step-", ignore_cleanup_errors=True) as td:
        for d in ("home", "tmp", STEP_HOOKS_DIR):
            (pathlib.Path(td) / d).mkdir()
        try:
            p = subprocess.run(resolve_step_argv(getattr(row, phase), ctx, row.id), cwd=str(gov_root),
                               env=build_step_env(td, target), stdin=subprocess.DEVNULL, capture_output=True,
                               text=True, encoding="utf-8", errors="replace")
        except OSError as e:
            return {"verdict": "failed", "rc": None, "tail": f"{row.id} {phase}: could not spawn: {e}"}
    tail = "\n".join(p.stderr.splitlines()[-20:])
    if phase in ("up", "down") and p.returncode != 0 and not p.stderr.strip():
        # TOOL-dSafePassage-69 S4: the walk reads a failing up's or down's stderr only, so a step that
        # wrote its failure elsewhere is named here rather than stopping the walk with an empty reason.
        last = next((ln.strip() for ln in reversed(p.stdout.splitlines()) if ln.strip()), "(none)")
        tail = (f"{row.id} {phase}: exit {p.returncode} with nothing on stderr, where a step writes its "
                f"failure; stdout's last line: {last}")
    return {"verdict": "ok" if p.returncode == 0 else "failed", "rc": p.returncode, "tail": tail}


def build_tree_git_env() -> dict[str, str]:
    """The parent's environment for a git call that must read ONE tree's own config: no `GIT_*`
    name, so a `GIT_DIR` or `GIT_INDEX_FILE` a calling hook exported cannot point the call at
    another repository, and no system or global config, which are the node's and never the tree's."""
    return {**{k: v for k, v in os.environ.items() if not k.upper().startswith("GIT_")},
            "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}


def write_target_plants(tree, canary_dir) -> list[str]:
    """Plant in `tree`, a SCRATCH COPY of a target, code that names itself in `canary_dir` when it
    runs (S4), and return the planted paths: a hook under every `CLIENT_HOOKS` name in the tree's
    effective hooks directory (its own `core.hooksPath`, else `git rev-parse --git-path hooks`; none
    where git reads no repository), and at its root `sitecustomize.py`, which an interpreter whose
    path holds the tree runs at start-up, and `json.py`, which shadows the standard module."""
    tree, canary_dir = pathlib.Path(tree).resolve(), pathlib.Path(canary_dir).resolve()
    canary_dir.mkdir(parents=True, exist_ok=True)
    env = build_tree_git_env()
    hooks = None
    for args in (("config", "--local", "--get", "core.hooksPath"), ("rev-parse", "--git-path", "hooks")):
        p = subprocess.run(["git", "-C", str(tree), *args], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env)
        if p.returncode == 0 and p.stdout.strip():
            # ponytail: planted where the tree's config points, which is the caller's scratch copy's
            hooks = tree / p.stdout.strip()
            break
    planted = []
    if hooks is not None:
        hooks.mkdir(parents=True, exist_ok=True)
        for name in CLIENT_HOOKS:
            h = hooks / name
            h.write_text(f"#!/bin/sh\n: > '{(canary_dir / f'hook-{name}').as_posix()}'\n",
                         encoding="utf-8", newline="\n")
            h.chmod(0o755)
            planted.append(h.as_posix())
    for mod in ("sitecustomize.py", "json.py"):
        m = tree / mod
        m.write_text(f"open({(canary_dir / f'module-{mod}').as_posix()!r}, 'w').close()\n",
                     encoding="utf-8", newline="\n")
        planted.append(m.as_posix())
    return planted


def read_plant_canaries(canary_dir) -> list[str]:
    """The canaries present in `canary_dir`, sorted: each names the planted code that ran."""
    d = pathlib.Path(canary_dir)
    return sorted(p.name for p in d.iterdir()) if d.is_dir() else []


def check_needs_target(row: StepRow, tree, gov_root) -> str:
    """Run `row`'s up, then its witness, under the contract beside `write_target_plants`' plants in
    `tree`, a scratch copy of a target, and print and return one verdict with the step id (S5):
    `isolated` (both exit 0, no canary ran), `breach` (a canary ran: the step reached target code),
    `needs-target` (a phase failed and no canary ran; the remedy is `needs-target = true`), or
    `attended` (the row declares it, and nothing is spawned)."""
    if derive_step_mode(row) == "attended":
        print(f"isolation: {row.id} · attended · it declares needs-target = true, so nothing ran")
        return "attended"
    canaries = pathlib.Path(tree) / CANARY_DIR
    shutil.rmtree(canaries, ignore_errors=True)
    write_target_plants(tree, canaries)
    failed = None
    for phase in ("up", "witness"):
        r = run_step_isolated(row, phase, tree, gov_root)
        if r["verdict"] != "ok":
            failed = f"its {phase} exits {r['rc']}"
            break
    ran = read_plant_canaries(canaries)
    if ran:
        print(f"isolation: {row.id} · breach · target code ran under the contract: {', '.join(ran)}")
        return "breach"
    if failed:
        print(f"isolation: {row.id} · needs-target · {failed} under the contract and no canary ran, "
              f"so it needs target code: declare needs-target = true, under which it is attended")
        return "needs-target"
    print(f"isolation: {row.id} · isolated · its up and witness exit 0 and no canary ran")
    return "isolated"


def derive_pending_steps(gov_root, receipt: dict, to_commit: str) -> list[StepRow]:
    """The steps `update` walks toward `to_commit` (TOOL-dSafePassage-2 S1): every row `read_steps`
    reads in that commit's tree, in the order it returns, minus each id the receipt's `steps`
    records `applied`. A row landed after `to_commit` is not in its tree, so it is not read; a
    receipt with no `steps` has every row pending. No order is derived here."""
    done = {r["id"] for r in read_step_states(receipt) if r["state"] == "applied"}
    return [r for r in read_steps(gov_root, to_commit, resolve_landed_ref(gov_root) or "")
            if r.id not in done]


def write_staging_line(target, path: str, oid: str | None = "worktree") -> None:
    """Append `{"path", "oid"}` to the staging journal beside the write lock, BEFORE the call that
    writes that index entry (TOOL-dSafePassage-2 S8): `oid` the blob about to be staged, None for a
    deletion, or by default `"worktree"`, a `git add` of the working file, whose blob is hashed here
    through the path's own filters, None where the file is absent. A hash git refuses journals
    nothing, so that path reads dirty after a kill, the safe direction."""
    target = pathlib.Path(target)
    if oid == "worktree":
        oid = None
        if (target / path).is_file():
            out = run_git(target, "hash-object", "--", path)
            if not out:
                return
            oid = out.decode("utf-8").strip()
    journal = target.joinpath(*load_govkit().STAGING_JOURNAL_REL.split("/"))
    journal.parent.mkdir(parents=True, exist_ok=True)
    with open(journal, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps({"path": path, "oid": oid}) + "\n")


def read_staging_journal(target) -> dict[str, str | None]:
    """The staging journal at `target`, `{path: the last line's oid}` (S8). A line that is not one
    `{"path", "oid"}` object, a torn last line from a kill included, vouches for nothing and is
    skipped; no journal is the empty mapping."""
    journal = pathlib.Path(target).joinpath(*load_govkit().STAGING_JOURNAL_REL.split("/"))
    out: dict[str, str | None] = {}
    try:
        lines = journal.read_text(encoding="utf-8").splitlines()
    except OSError:
        return out
    for ln in lines:
        try:
            d = json.loads(ln)
        except ValueError:
            continue
        if (isinstance(d, dict) and set(d) == {"path", "oid"} and isinstance(d["path"], str)
                and (d["oid"] is None or (isinstance(d["oid"], str) and OID_RE.fullmatch(d["oid"])))):
            out[d["path"]] = d["oid"]
    return out


def write_attended_order(target, gov_root, row: StepRow, phase: str = "up",
                         to: str | None = None) -> pathlib.Path:
    """Write the outbox order an `attended` stop leaves (S5),
    `.governance/outbox/update-attended-step-<slug>.md`, the slug `render_order_slug` of the step id:
    the step, its resolved `phase` argv, why it is attended, and what the next walk does. Returns
    its path."""
    gk = load_govkit()
    argv = resolve_step_argv(getattr(row, phase), derive_step_context(
        row, target, gov_root, to if phase == "down" else None), row.id)
    # The order's kind is ATTENDED_ORDER_PREFIX's, so its readers glob what the one writer writes.
    kind = gk.ATTENDED_ORDER_PREFIX.removeprefix("update-").removesuffix("-")
    return gk.write_row_order(
        pathlib.Path(target) / ".governance" / "outbox", kind, row.id,
        f"# An attended upgrade step: {row.id}\n\n"
        f"`govkit update --write` stopped before this step's `{phase}`. Its row declares "
        f"`needs-target = true`: its code needs the target's own code, which the isolation contract "
        f"keeps from every step govkit spawns, so govkit runs none of it.\n\n"
        f"Read it, then run it yourself:\n\n    {shlex.join(argv)}\n\n"
        f"The next `govkit update --write` runs the step's witness first, skips the step once that "
        f"witness holds, and walks the steps after it.\n")


def write_step_record(receipt_path, receipt: dict, row: StepRow, state: str,
                      failure: str | None = None, via: str | None = None) -> None:
    """Record `row` at `state` in `receipt` through `set_step_state` and write the whole receipt to
    `receipt_path` in one atomic write (TOOL-dSafePassage-2 S3): the walk's and the reverse walk's
    one persist."""
    set_step_state(receipt, row.id, row.introduced, state, failure, via)
    write_atomic(receipt_path, json.dumps(receipt, indent=2) + "\n")


def run_step_reread(row: StepRow, phase: str, target, gov_root, receipt_path, receipt: dict,
                    to: str | None = None) -> dict:
    """`run_step_isolated`, then the receipt hand-off (TOOL-dSafePassage-2 S3): `schema` and `steps`
    re-read from `receipt_path` into `receipt`, a key the step took away dropped here too, since a
    step may rewrite the receipt. A receipt that does not read back is a refusal naming the step."""
    got = run_step_isolated(row, phase, target, gov_root, to)
    receipt_path = pathlib.Path(receipt_path)
    try:
        disk = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Refusal(f"{row.id} {phase}: the receipt {receipt_path.as_posix()} does not read back "
                      f"after the spawn ({e}), so the walk records nothing over it") from None
    for k in ("schema", "steps"):
        if k in disk:
            receipt[k] = disk[k]
        else:
            receipt.pop(k, None)
    return got


def read_image_paths(target, step_id: str, index: bool = False) -> list[str]:
    """Every path `step_id`'s before-image at `target` lists, each refused where it is not inside the
    target, then the image's own path; [] where there is no image. Read before a down, which takes
    the image away. With `index`, the image is the copy the index holds, `git show :<image path>`,
    which outlives a down killed before its staging (TOOL-dSafePassage-76 S3): graded as the working
    tree's is. An image that does not parse or lists no paths, from either source, is a refusal
    naming it, never a traceback."""
    image = derive_image_path(target, step_id)
    rel = image.relative_to(target).as_posix()
    if index:
        data = run_git(target, "show", f":{rel}")
        if data is None:
            return []
    elif not image.is_file():
        return []
    try:
        held = json.loads(data.decode("utf-8") if index else image.read_text(encoding="utf-8"))["paths"]
        if not (isinstance(held, dict) and held):
            raise ValueError("no paths")
        paths = sorted(held)
    except (ValueError, KeyError, TypeError):
        if not index:
            raise Refusal(f"{step_id}: its before-image {rel} does not parse or lists no paths, so which "
                          f"paths its step wrote is unknown; put back its committed copy, or where none is "
                          f"committed, remove it, which gives up the before bytes it held; then run again") from None
        raise Refusal(f"{step_id}: the index's copy of its before-image {rel} does not parse or lists no "
                      f"paths, so which paths its down restored is unknown and none was staged; stage "
                      f"the restored paths and the image's removal by hand, then run the rollback again") from None
    for p in paths:
        check_contained(target, p)  # the image is a step's output: no path outside the target
    return paths + [rel]


def write_step_staged(target, step_id: str, paths: list[str], then: str) -> None:
    """Stage a step's writes at `target` (TOOL-dSafePassage-2 S11): each of `paths` journaled first
    (S8), then `git add` where the file is present and `git rm --cached` where it is not. A refusal
    by git names the step and `then`, what the receipt says about it."""
    target = pathlib.Path(target)
    for p in paths:
        write_staging_line(target, p)
    for argv, group in ((["add"], [p for p in paths if (target / p).is_file()]),
                        (["rm", "-q", "--cached", "--ignore-unmatch"],
                         [p for p in paths if not (target / p).is_file()])):
        if group and load_govkit().git_pathspec(target, argv, group).returncode != 0:
            raise Refusal(f"{step_id}: `git {argv[0]}` refused the step's writes "
                          f"({', '.join(group)}), so they are not staged; {then}")


def run_step_walk(gov_root, target, receipt_path, receipt: dict, rows: list[StepRow]) -> dict:
    """Walk `rows`, the pending steps in order, over `target` (TOOL-dSafePassage-2 S2), every spawn
    through `run_step_isolated`. Per step: (1) its witness; exit 0 records `applied`, with `"via":
    "witness"` (TOOL-dSafePassage-33) only where the receipt held no record of the step, or a
    `rolled-back` one, when this walk began and no before-image exists (TOOL-dSafePassage-40, -73's
    `test_up_unrecorded`), its up never spawned; where a before-image exists, the paths it lists and
    the image are staged first, a killed up's writes (TOOL-dSafePassage-76 S2); (2) a row needing target code records `failed` (`attended: ...`), writes the attended
    order and stops; (3) records `failed` (`interrupted: started <utc>, no exit recorded`) BEFORE
    the spawn, so a walk killed with its step leaves that failure; (4) runs the row's `resume` argv
    where the receipt held a `failed` row for it when this walk began and `resume` is an argv, else
    its up; a non-zero exit records `exit <rc>: <last stderr line>` and stops; (5) the witness
    again: exit 0 stages the step's writes and records `applied`, anything else records `witness
    does not hold after up` and stops. No down runs, and the steps before a stop stay applied.

    Each record goes through `set_step_state` into `receipt`, the caller's, and onto `receipt_path`
    in one atomic write (S3), and only where `test_steps_recordable` holds on `receipt`: below schema
    4 none is made, nothing is written, and the step line ends `NOT_RECORDED_SUFFIX`, so a schema-3
    receipt walks to `govkit/receipt-schema-4`, whose `applied` row lands after its up
    (TOOL-dSafePassage-15). After each spawn `schema` and `steps` are re-read from disk, since a
    step may rewrite them. Returns `{"pending", "applied", "skipped", "stopped", "failure",
    "order"}`, `applied` counting the ups run and `skipped` the steps passed by their witness."""
    target, receipt_path = pathlib.Path(target).resolve(), pathlib.Path(receipt_path)
    began = {r["id"]: r["state"] for r in read_step_states(receipt)}  # the walk-start receipt
    began_failed = {sid for sid, state in began.items() if state == "failed"}
    then = "the step stays recorded interrupted and the next walk runs it again"  # moves 1 and 5 stage
    out = {"pending": len(rows), "applied": 0, "skipped": 0, "stopped": None, "failure": None,
           "order": None}

    def write(row: StepRow, state: str, failure: str | None = None, via: str | None = None) -> str:
        # TOOL-dSafePassage-15 S1: below schema 4 the receipt holds no row, so nothing is written and
        # the step line carries the suffix this returns; the schema step's own `applied` row lands
        # after its up, once the re-read brought schema 4 into `receipt`.
        if not test_steps_recordable(receipt):
            return f" {NOT_RECORDED_SUFFIX}"
        write_step_record(receipt_path, receipt, row, state, failure, via)
        return ""

    def run_spawn(row: StepRow, phase: str) -> dict:
        return run_step_reread(row, phase, target, gov_root, receipt_path, receipt)

    def set_stopped(row: StepRow, failure: str) -> dict:
        unrecorded = write(row, "failed", failure)
        print(f"step {row.id} · failed · {failure}{unrecorded}")
        out.update(stopped=row.id, failure=failure)
        return out

    for row in rows:
        # THE WITNESS RUNS EVEN FOR A ROW THAT NEEDS TARGET CODE, under the same contract as any
        # step's: it is how the next walk passes an attended step a person ran by hand (S5, AC5).
        # Its up is what the attended mode keeps from spawning, and move 2 below keeps it so.
        seen = row._replace(needs_target=False)
        if run_spawn(seen, "witness")["verdict"] == "ok":
            # TOOL-dSafePassage-33 S2: the mark that lets the reverse walk read a missing image as
            # "never ran"; move 5 below, after an up, passes none. TOOL-dSafePassage-40 S1: only
            # where nothing says an up spawned; TOOL-dSafePassage-73 S2: the reverse walk's question.
            image = derive_image_path(target, row.id).exists()
            fresh = test_up_unrecorded(began.get(row.id), image)
            if image:
                # TOOL-dSafePassage-76 S2: an up killed after its second witness left its writes and
                # its image unstaged; they are staged here, as move 5 would have.
                write_step_staged(target, row.id, read_image_paths(target, row.id), then)
            unrecorded = write(row, "applied", via="witness" if fresh else None)
            print(f"step {row.id} · skipped (witness holds){unrecorded}")
            out["skipped"] += 1
            continue
        if derive_step_mode(row) == "attended":
            out["order"] = write_attended_order(target, gov_root, row).relative_to(target).as_posix()
            return set_stopped(row, ATTENDED_STOP)
        write(row, "failed", f"interrupted: started "
                f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, no exit recorded")
        phase = "resume" if row.id in began_failed and isinstance(row.resume, list) else "up"
        got = run_spawn(row, phase)
        if got["verdict"] != "ok":
            return set_stopped(row, f"exit {got['rc']}: {(got['tail'].splitlines() or [''])[-1]}")
        if run_spawn(seen, "witness")["verdict"] != "ok":
            return set_stopped(row, "witness does not hold after up")
        # S11. `update` stages what it writes and never commits, a step's writes included: each
        # path the before-image lists, and the image, journaled first (S8).
        write_step_staged(target, row.id, read_image_paths(target, row.id), then)
        unrecorded = write(row, "applied")
        print(f"step {row.id} · applied" + (" · by its resume" if phase == "resume" else "") + unrecorded)
        out["applied"] += 1
    return out


def check_gov_first(receipt: dict, declared: list[StepRow], target) -> list[str]:
    """The landing's check over gov's own SOURCE-mode receipt, after the walk (TOOL-dSafePassage-8
    S2): one problem line per id that misses. The `steps` ids must equal `declared`'s both ways, a
    listed id no row declares passing only as the old id of a `[[retired]]` succession row; and
    every step listed `applied` must have its witness hold NOW on gov's tree, re-run under
    `run_step_isolated` rather than trusted from the record. `target` is gov's own checkout, so it
    is the step's gov root too. Returns [] when gov holds every declared step."""
    target = pathlib.Path(target).resolve()
    rows = {r["id"]: r for r in read_step_states(receipt)}
    by_id = {r.id: r for r in declared}
    problems = [f"{sid}: declared, and gov's receipt does not list it" for sid in by_id if sid not in rows]
    old_ids = {r.id for r in read_retired(target, None, None)}
    problems += [f"{sid}: listed in gov's receipt, and no row declares it nor retires it"
                 for sid in rows if sid not in by_id and sid not in old_ids]
    for sid, rec in rows.items():
        if sid not in by_id:
            continue
        if rec["state"] != "applied":
            problems.append(f"{sid}: listed {rec['state']} in gov's receipt, not applied")
            continue
        if run_step_isolated(by_id[sid], "witness", target, target)["verdict"] != "ok":
            problems.append(f"{sid}: listed applied, and its witness does not hold on gov's tree")
    return problems


def derive_reverse_steps(gov_root, receipt: dict, to_commit: str) -> list[StepRow]:
    """The steps `update --rollback --to <to_commit>` downs (TOOL-dSafePassage-4 S3): every row
    `read_steps` reads at gov's HEAD whose introducing commit is not an ancestor of `to_commit`, an
    unlanded row included, and which the receipt's `steps` records `applied` or `failed`, or records
    nowhere; in the reverse of the walk order, so the steps file's first row is downed last. A
    receipt row whose id HEAD no longer declares is refused before any down: its down is unknown,
    but for an id a `[[retired]]` row of HEAD names (TOOL-dSafePassage-76 S4), which passes where it
    is recorded `rolled-back` or was introduced at an ancestor of `to_commit`, so it owes no down,
    and is refused otherwise; nothing is read from its successor."""
    landed = resolve_landed_ref(gov_root) or ""
    rows = read_steps(gov_root, "HEAD", landed)
    recorded = {r["id"]: r["state"] for r in read_step_states(receipt)}
    gone = sorted(set(recorded) - {r.id for r in rows})
    retired = {r.id: r for r in read_retired(gov_root, "HEAD", None)} if gone else {}
    owed = [sid for sid in gone if sid in retired and recorded[sid] != "rolled-back"]
    if owed:
        tr, reg_rel, _raw, _entries = read_registry_at(gov_root, resolve_rev(gov_root, "HEAD"))
        hit = derive_introduced(gov_root, landed, [reg_rel[:-len(REGISTRY_FILE)] + STEPS_FILE], "upgrade",
                                owed, registry=(reg_rel, tr))
        for sid in owed:
            if sid not in hit or run_git(gov_root, "merge-base", "--is-ancestor", hit[sid][0], to_commit) is None:
                r = retired[sid]
                raise Refusal(f"the receipt records the step {sid} {recorded[sid]}, which {r.file} [[retired]] "
                              f"row {r.row} retires, and it was not introduced at an ancestor of "
                              f"{to_commit[:8]}, so its down is owed and no row declares one; nothing was "
                              f"rolled back")
    gone = [sid for sid in gone if sid not in retired]
    if gone:
        raise Refusal(f"the receipt records the step(s) {', '.join(gone)}, which gov's HEAD no longer "
                      f"declares, so no down argv is known for them; nothing was rolled back")
    return [r for r in reversed(rows) if recorded.get(r.id) != "rolled-back" and (
        r.introduced == UNLANDED
        or run_git(gov_root, "merge-base", "--is-ancestor", r.introduced, to_commit) is None)]


def test_up_unrecorded(state: str | None, image_present: bool) -> bool:
    """Whether no up of a step is on record (TOOL-dSafePassage-73), the one question move 1 of
    `run_step_walk` and move 3 of `run_reverse_walk` ask before marking a row `"via": "witness"`:
    its record, `state`, is None or `rolled-back` (a completed down undid any up before it), and no
    before-image exists, which an up since would have written. A `failed` record says an up may
    have spawned, so it is never read as unrecorded."""
    return state in (None, "rolled-back") and not image_present


def derive_down_verdict(row: StepRow, image_present: bool, down_rc,
                        record: dict | None) -> tuple[bool | None, str]:
    """Move 5 of `run_reverse_walk` (TOOL-dSafePassage-17 S2): `(reverted, phase)`. Where the down's
    own exit decides, `reverted` is `down_rc == 0` and `phase` is `down`: the row declares
    `reverted = "down-exit"`, or declares no `reverted`, had no before-image at the down's spawn
    (`image_present` read before it) and its last receipt `record`, read before the down, is
    `applied` with `"via": "witness"` or None (TOOL-dSafePassage-33's scoped no-image rule: only a
    row no up wrote may read a missing image as "never ran"). Otherwise `reverted` is None and
    `phase` names the check to spawn: `reverted`, the row's argv, its exit 0 the down took effect;
    or `witness`, with no `reverted`, the down reverted when it does NOT hold."""
    never_ran = record is None or (record["state"] == "applied" and record.get("via") == "witness")
    if row.reverted == DOWN_EXIT or (row.reverted is None and not image_present and never_ran):
        return down_rc == 0, "down"
    return None, "witness" if row.reverted is None else "reverted"


def run_reverse_walk(gov_root, target, receipt_path, receipt: dict, rows: list[StepRow],
                     to: str | None = None) -> dict:
    """Down `rows`, `derive_reverse_steps`' order, over `target` (TOOL-dSafePassage-4 S4), every
    spawn through `run_step_reread`. Per step: (1) one recorded `rolled-back` or nowhere runs its
    witness first and is skipped where it does not hold, nothing of it applied; (2) a row needing
    target code stops the walk with `write_attended_order`'s order naming its down; (3) its state
    kept, `failure` `down interrupted: ...` is persisted BEFORE the spawn, a row recorded nowhere
    or `rolled-back` with no before-image marked `"via": "witness"` (TOOL-dSafePassage-39, -73's
    `test_up_unrecorded`); (4) its down, a non-zero
    exit stopping with `down exit <rc>: <last stderr line>`; (5) `derive_down_verdict`'s judge
    (TOOL-dSafePassage-17): the down's own exit under `reverted = "down-exit"`, or with no
    before-image at the spawn on a row recorded nowhere or `applied` via its witness
    (TOOL-dSafePassage-33), the row's `reverted` argv, a non-zero exit stopping with `reverted
    check exits <rc>`, else its witness, exit 0 stopping with `witness still holds after down`,
    `; before-image <path> absent` added where the row had no image; a
    down that took effect stages the paths its before-image listed (read before the down took the
    image away), or with none read, those of the image the index holds (TOOL-dSafePassage-76 S3),
    and the image, and records `rolled-back`. A
    `failed` row is downed like an `applied` one: the down is what tolerates a partial up.

    After the down's re-read, `test_steps_recordable` decides whether that row's records are written
    (TOOL-dSafePassage-18): a down that leaves the receipt below schema 4, the schema step's, writes
    none, the field's absence being its record, and its verdict still reads `rolled-back`. Such a
    down before the last row stops the walk with `LOWERED_STOP`, since no later down could be
    recorded. Move 3's mark is persisted only where the receipt can hold it before the down, and
    the stop fires only at the down that took the receipt below schema 4 (TOOL-dSafePassage-70): on
    a receipt already below it, as after a kill past the schema step's down, every down runs, is
    judged as on a schema-4 receipt, writes no row, and the walk reaches its last row.

    Its one caller is `update --rollback`: a stopped walk, the verify rollback and `apply` run no
    down. Returns `{"downs": [(id, verdict)], "stopped", "failure", "order"}`, `downs` the verdict
    list in the order the rows were reached, which `write_rollback_record` prints. `to`, the
    rollback's `--to`, answers each down's `{to}` (TOOL-dSafePassage-26 S10)."""
    target, receipt_path = pathlib.Path(target).resolve(), pathlib.Path(receipt_path)
    out = {"downs": [], "stopped": None, "failure": None, "order": None}

    def set_stopped(row: StepRow, failure: str) -> dict:
        print(f"step {row.id} · STOPPED · {failure}")
        out["downs"].append((row.id, f"STOPPED {failure}"))
        out.update(stopped=row.id, failure=failure)
        return out

    for n, row in enumerate(rows, 1):
        seen = row._replace(needs_target=False)  # a witness runs under the contract, as the walk's
        # The row's last record, read before move 3 rewrites it: derive_down_verdict's scope.
        record = next((r for r in read_step_states(receipt) if r["id"] == row.id), None)
        state = record["state"] if record else None
        if state in (None, "rolled-back"):
            if run_step_reread(seen, "witness", target, gov_root, receipt_path, receipt)["verdict"] != "ok":
                print(f"step {row.id} · skipped (nothing applied)")
                out["downs"].append((row.id, "skipped (nothing applied)"))
                continue
            state = "applied"
        if derive_step_mode(row) == "attended":
            out["order"] = write_attended_order(target, gov_root, row, "down", to).relative_to(target).as_posix()
            return set_stopped(row, f"{ATTENDED_STOP} — {out['order']} names its down")
        paths = read_image_paths(target, row.id)
        # TOOL-dSafePassage-70 S1: below schema 4 no row can hold the mark, as the forward walk's
        # persist asks; a down never raises the schema, so `held` is false only past the lowering.
        held = test_steps_recordable(receipt)
        # TOOL-dSafePassage-39 S3: a row recorded nowhere with no image had no up on record, so it
        # is marked as the forward walk's witness skip is; a recorded row's mark the writer carries.
        # TOOL-dSafePassage-49 S5: a `rolled-back` row whose witness holds is recorded `applied`
        # here, never `rolled-back` with a failure, and no up is on record since its down completed.
        if held:
            write_step_record(receipt_path, receipt, row, state, f"{DOWN_STOP_PREFIXES[0]} started "
                              f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, no exit recorded",
                              "witness" if test_up_unrecorded(None if record is None else record["state"],
                                                              bool(paths)) else None)
        got = run_step_reread(row, "down", target, gov_root, receipt_path, receipt, to)
        recordable = test_steps_recordable(receipt)  # TOOL-dSafePassage-18 S1: below 4, no row
        if got["verdict"] != "ok":
            failure = f"{DOWN_STOP_PREFIXES[1]}{got['rc']}: {(got['tail'].splitlines() or [''])[-1]}"
            if recordable:
                write_step_record(receipt_path, receipt, row, state, failure)
            return set_stopped(row, failure)
        if held and not recordable and n < len(rows):
            return set_stopped(row, LOWERED_STOP)
        reverted, phase = derive_down_verdict(row, bool(paths), got["rc"], record)
        rc = got["rc"]
        if reverted is None:
            check = run_step_reread(seen, phase, target, gov_root, receipt_path, receipt)
            reverted, rc = (check["verdict"] == "ok") == (phase == "reverted"), check["rc"]
        if not reverted:
            # TOOL-dSafePassage-33 S3: a witness judging a row with no image names the lost image.
            lost = "" if paths else (f"; before-image "
                                     f"{derive_image_path(target, row.id).relative_to(target).as_posix()} absent")
            failure = {"witness": DOWN_STOP_PREFIXES[2] + lost, "reverted": f"{DOWN_STOP_PREFIXES[3]}{rc}"}.get(
                phase, f"{DOWN_STOP_PREFIXES[1]}{rc}")
            if recordable:
                write_step_record(receipt_path, receipt, row, state, failure)
            return set_stopped(row, failure)
        # TOOL-dSafePassage-76 S3: a re-run after a down killed before this staging finds no image
        # in the working tree, so the index's copy names what that down restored.
        write_step_staged(target, row.id, paths or read_image_paths(target, row.id, index=True),
                          "the step stays recorded down interrupted and the next rollback runs its down again")
        if recordable:
            write_step_record(receipt_path, receipt, row, "rolled-back")
        print(f"step {row.id} · rolled-back")
        out["downs"].append((row.id, "rolled-back"))
    return out


def write_rollback_record(target, from_commit: str, to_commit: str, started: str,
                          downs: list | None = None, files: tuple | None = None,
                          stamp: str | None = None) -> pathlib.Path:
    """Write `.governance/outbox/update-reverted-<from8>-<to8>.md`, the record of one `update
    --rollback` (TOOL-dSafePassage-4 S6): begun with `from`, `to` and the start, `not finished`;
    rewritten once `stamp` is known with each down's verdict, the file-row counts (`files`: wrote,
    moved, deleted, withheld, conflicts) and the stamp's fate. Returns its path."""
    rec = (pathlib.Path(target) / ".governance" / "outbox"
           / f"update-reverted-{from_commit[:8]}-{to_commit[:8]}.md")
    rec.parent.mkdir(parents=True, exist_ok=True)
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    lines = [f"# update --rollback {from_commit[:8]} -> {to_commit[:8]}",
             f"started {started} · " + (f"finished {now}" if stamp is not None else "not finished")]
    lines += [f"down {sid}: {verdict}" for sid, verdict in downs or []]
    if files is not None:
        lines.append("files: wrote {} · moved {} · deleted {} · withheld {} · conflicts {}".format(*files))
    if stamp is not None:
        lines.append(f"gov_commit: {stamp}")
    rec.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return rec


def read_lock_holder(lock) -> tuple[bytes | None, dict | None]:
    """(the lock file's bytes, None when absent; its record, None where it is not a JSON object
    naming an integer `pid` and a numeric `started`), the reading `check_holder_dead` judges and
    the bytes a reclaim compares (TOOL-dSafePassage-2 S7)."""
    try:
        raw = pathlib.Path(lock).read_bytes()
    except OSError:
        return None, None
    try:
        rec = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return raw, None
    ok = (isinstance(rec, dict) and type(rec.get("pid")) is int
          and isinstance(rec.get("started"), (int, float)) and not isinstance(rec.get("started"), bool))
    return raw, rec if ok else None


def read_boot_clock() -> float | None:
    """Seconds on the kernel's boot clock, the origin `ps`'s `etimes` counts from, or None where
    `time` defines no `CLOCK_BOOTTIME` (TOOL-dSafePassage-32 S1)."""
    clock = getattr(time, "CLOCK_BOOTTIME", None)
    return None if clock is None else time.clock_gettime(clock)


def read_boot_id() -> str:
    """The kernel's boot id under Linux, `/proc/sys/kernel/random/boot_id`, else "" (S33)."""
    try:
        return pathlib.Path("/proc/sys/kernel/random/boot_id").read_text(encoding="ascii").strip()
    except OSError:
        return ""


PID_NS_LINK = "/proc/self/ns/pid"


def read_pid_namespace() -> str:
    """This process's pid namespace, the `PID_NS_LINK` text `pid:[<inode>]`, or "" where the link
    does not exist, Windows and macOS (TOOL-dSafePassage-31 S1). A link that exists and cannot be
    read raises its OSError, which names the path."""
    return os.readlink(PID_NS_LINK) if os.path.lexists(PID_NS_LINK) else ""


def add_boot_start(record: dict) -> dict:
    """`record` with `started_boot`, the `read_boot_clock` reading, beside its `started`, the key
    left out where the reading is None (TOOL-dSafePassage-32 S2); and the pid namespace it was taken
    in, `platform` (`sys.platform`) and `boot_id` (`read_boot_id`), so WSL and Windows runs on one
    tree, one host name, never judge each other's pid (TOOL-dSafePassage-26 S33), and `pid_ns`
    (`read_pid_namespace`), which tells apart two WSL distros sharing one kernel (TOOL-dSafePassage-31 S2)."""
    boot = read_boot_clock()
    record = {**record, "platform": sys.platform, "boot_id": read_boot_id(), "pid_ns": read_pid_namespace()}
    return record if boot is None else {**record, "started_boot": boot}


def check_holder_dead(record: dict | None) -> tuple[str, str]:
    """(`dead`, `live` or `unknown`, why) for a lock or guard holder (S7). `dead`: its `host` is this
    host or absent, and the process-monitor census holds no row with its pid, or one created more
    than `REUSE_MARGIN_S` after its `started`, a reused pid; `live`: a row with that pid created no
    later than that, and `dead` too where the record's `platform` is this one and its non-empty
    `boot_id` differs from this host's non-empty one, a reboot (TOOL-dSafePassage-35 S26);
    `unknown`: an unreadable record, another host, another `platform`, a `boot_id` of which one side
    is empty (TOOL-dSafePassage-26 S33), a `pid_ns` other than this process's,
    an absent one reading "" (TOOL-dSafePassage-31 S3), or a census that cannot run. The
    clock is read once BEFORE the census is spawned and no later reading enters the estimate, so a
    slow census makes a holder look older, toward `live` (TOOL-dSafePassage-22 S1).

    A `windows-join` row's age is wall against wall and is estimated on `time.time()` against
    `started`; a `posix-ps` row's `etimes` counts from boot, so it is estimated on `read_boot_clock()`
    against `started_boot`; where either boot reading is missing it falls back to the wall and
    never reads reused: a would-be reused holder reads `unknown` (TOOL-dSafePassage-32 S4, S5)."""
    if record is None:
        return "unknown", "its record names no readable pid and start time"
    host = record.get("host")
    if host is not None and host != THIS_HOST:
        return "unknown", f"it was taken on host {host!r}, and this host's process table cannot speak for that one"
    if "platform" in record and record["platform"] != sys.platform:
        return "unknown", (f"it was taken under platform {record['platform']!r}, not this process's "
                           f"{sys.platform!r}, so its pid names a process in another namespace this table "
                           f"cannot speak for")
    # TOOL-dSafePassage-35 S26: on this host and platform, two boot ids that differ mean a reboot
    # ended the holder; one boot id missing proves nothing.
    here_boot = read_boot_id()
    if "boot_id" in record and record["boot_id"] != here_boot:
        if record["boot_id"] and here_boot and "platform" in record:
            return "dead", (f"it was taken under boot_id {record['boot_id']!r}, and this host has booted "
                            f"since, as {here_boot!r}, which ended its holder")
        return "unknown", (f"it was taken under boot_id {record['boot_id']!r}, not this process's "
                           f"{here_boot!r}, so its pid names a process in another namespace this table "
                           f"cannot speak for")
    # TOOL-dSafePassage-31 S3: an absent `pid_ns` is "", so a Linux judge never reads an older lock as its own.
    try:
        here_ns = read_pid_namespace()
    except OSError as e:
        return "unknown", f"this process's pid namespace could not be read ({e})"
    if (record.get("pid_ns") or "") != here_ns:
        taken = f"under pid_ns {record['pid_ns']!r}" if record.get("pid_ns") else "with no pid_ns recorded"
        return "unknown", (f"it was taken {taken}, not this process's {here_ns!r}, so its pid may name a "
                           f"process in another pid namespace this table cannot speak for")
    pid = record["pid"]
    try:
        pm_dir = resolve_kit_dir("process-monitor", "census.py", HERE)
        spec = importlib.util.spec_from_file_location("gk_lock_census", pm_dir / "census.py")
        census = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(census)
        now, now_boot = time.time(), read_boot_clock()
        rows, _counts = census.scan_processes()
    except Exception as e:  # ponytail: any census failure proves nothing, and `unknown` refuses
        return "unknown", f"the process census could not run ({type(e).__name__}: {e})"
    started_boot = record.get("started_boot")
    if isinstance(started_boot, bool) or not isinstance(started_boot, (int, float)):
        started_boot = None
    unjudged = False
    born = [r for r in rows if r.get("winpid") == pid]
    for r in born:
        posix = r.get("backend") != "windows-join"
        boot = posix and now_boot is not None and started_boot is not None
        t0, start = (now_boot, started_boot) if boot else (now, record["started"])
        if t0 - float(r["age_s"]) <= start + REUSE_MARGIN_S:
            return "live", f"pid {pid} is still running and was started before it took the lock"
        unjudged = unjudged or (posix and not boot)  # S5: a wall estimate never reads reused here
    if unjudged:
        return "unknown", (f"pid {pid} is still running, and its lock records no boot-clock start "
                           f"to compare its age with, so a reused pid cannot be told from the holder")
    if born:
        return "dead", f"pid {pid} now names a process started after the lock was taken, a reused pid"
    return "dead", f"no process on this host has pid {pid} any more"


def write_reclaimed_lock(lock, record: dict) -> tuple[str, dict | None, str]:
    """Take over `lock` from a dead holder, writing `record` (S7): `("reclaimed", holder, why)`, or
    the verdict that refused it, `live`, `unknown` or `busy`, with the holder and why.

    Only `dead` is reclaimed, under the guard `<lock>.reclaim` taken with `O_EXCL`: its holder
    re-reads the lock and unlinks it only where the bytes equal the ones it judged, then re-makes it
    with `O_EXCL`, so of two racers exactly one holds the lock and the other reads `busy`. A guard
    whose own holder is dead is cleared and that call reads `busy`, so no call both clears a guard
    and takes one."""
    lock = pathlib.Path(lock)
    raw, holder = read_lock_holder(lock)
    if raw is None:
        return "busy", None, "the lock was released while this run judged it"
    verdict, why = check_holder_dead(holder)
    if verdict != "dead":
        return verdict, holder, why
    guard = lock.with_name(lock.name + load_govkit().RECLAIM_GUARD_SUFFIX)
    try:
        fd = os.open(str(guard), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except (FileExistsError, PermissionError):  # Windows: a guard pending deletion refuses the create
        g_raw, g_holder = read_lock_holder(guard)
        if g_raw is not None and check_holder_dead(g_holder)[0] == "dead" and read_lock_holder(guard)[0] == g_raw:
            remove_shared_file(guard)
            return "busy", holder, (f"cleared the guard {guard.name}, whose holder, pid "
                                    f"{g_holder['pid']}, is no longer running; the next take reclaims")
        return "busy", holder, f"another run holds the guard {guard.name} and is reclaiming this lock"
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(add_boot_start({"pid": os.getpid(), "started": time.time(),
                                                  "host": THIS_HOST})) + "\n")
        if read_lock_holder(lock)[0] != raw:
            return "busy", holder, "the lock changed while this run judged it: another run took it"
        remove_shared_file(lock)
        try:
            fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except (FileExistsError, PermissionError):
            return "busy", holder, "another run took the lock first"
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(record, indent=2) + "\n")
        return "reclaimed", holder, why
    finally:
        remove_shared_file(guard)


def remove_shared_file(path) -> None:
    """Unlink `path`, retrying for up to two seconds while another process has it open: on Windows
    an open handle refuses the unlink, and a racer reading a lock or its guard is exactly that."""
    for _ in range(40):
        try:
            pathlib.Path(path).unlink(missing_ok=True)
            return
        except PermissionError:
            time.sleep(0.05)
    pathlib.Path(path).unlink(missing_ok=True)


# The remote ladder (TOOL-dLadderedRemote-2), INLINED byte-identically from the canonical copy
# named on its marker line and gated by the resolve-python self-test (TOOL-dSafePassage-26 S4):
# the base ladder below reads it here, so this module imports nothing from govkit for it.
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


def resolve_landing_base(root, base: str | None) -> tuple[str, bool, str]:
    """`(sha, boundary, why)`: the commit a push-boundary leg grades from, and whether it is one.

    `--base` when given, else `GATE_PUSH_BASE`, else the merge-base with the remote ladder's default
    branch, the remote's first, then the local branch. `boundary` is True for the first two. On no
    base `sha` is "" and `why` completes the line `no base to compare against`, because no base is a
    FAILED exit 1 for every caller and never a zero-status skip: run-gates judges a leg by its exit
    code, and a silent 0 reads as a pass forever. Extracted from `cmd_epoch` at its second caller,
    `upgrade_steps.py frozen` (TOOL-dSafePassage-1); the step gate is its third (TOOL-dSafePassage-10
    S6), so the legs grading a landing read one base. It lives here, beside the inline remote
    ladder, so this module imports nothing from govkit for it (TOOL-dSafePassage-26 S1, S4).
    """
    boundary = base is not None
    # An ALL-ZERO value reads as UNSET (TOOL-aMendedFleet-111 S3): the hook exports the remote's old
    # sha, forty zeros on a push that CREATES the default branch, and no commit carries that name.
    if base is None and os.environ.get("GATE_PUSH_BASE", "").strip("0"):
        base, boundary = os.environ["GATE_PUSH_BASE"], True
    if base is None:
        # The default base is `check-verdict-epoch.sh`'s. The remote and its branch are the
        # ladder's (TOOL-dLadderedRemote-2); a refusal is the failed exit, naming it, and no remote
        # at all leaves only the local branch.
        remote, dflt, _observed, refusal = resolve_remote(root)
        if refusal:
            return "", boundary, f" · {refusal}"
        dflt = dflt or "main"
        for ref in ((f"{remote}/{dflt}", dflt) if remote else (dflt,)):
            mb = subprocess.run(["git", "-C", str(root), "merge-base", ref, "HEAD"],
                                capture_output=True, text=True, encoding="utf-8")
            if mb.returncode == 0 and mb.stdout.strip():
                base = mb.stdout.strip()
                break
    rb = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "--quiet",
                         f"{base}^{{commit}}"], capture_output=True, text=True, encoding="utf-8") if base else None
    if rb is None or rb.returncode != 0:
        return "", boundary, (f" ({base or 'no merge-base with the default branch'})"
                              " · fetch full history, set GOV_DEFAULT_BRANCH, or pass --base <rev>")
    return rb.stdout.strip(), boundary, ""


def blob_at(root, commit: str, path: str, batch=None) -> bytes | None:
    """Bytes of `path` in the commit `commit` names, from the object store — never from the working
    tree; None where the commit holds no such blob.

    This is the receipt's whole provenance claim. Reading the working tree would make the receipt
    say "these bytes came from <commit>" about bytes that came from whatever the operator had
    checked out and half-edited at the time.

    THE ONE revision-blob reader (TOOL-dSafePassage-26 S14). `batch` is an open
    `git cat-file --batch` process a caller reading many blobs passes, `derive_introduced` among
    them, so a history walk asks one process rather than spawning one `git show` per blob.
    """
    if batch is None:
        out = subprocess.run(["git", "-C", str(root), "show", f"{commit}:{path}"],
                             capture_output=True, check=False)
        return out.stdout if out.returncode == 0 else None
    batch.stdin.write(f"{commit}:{path}\n".encode("utf-8"))
    batch.stdin.flush()
    head = batch.stdout.readline().split()
    if len(head) < 3:
        return None  # `<name> missing`: no such blob at that commit
    return batch.stdout.read(int(head[2]) + 1)[:-1]


def write_atomic(dest, text: str) -> None:
    """Persist `text` at `dest` through a sibling temp file and `os.replace`, so a run that dies
    mid-write leaves the PREVIOUS file rather than a truncated one (DEPL-cMendedVintage-21 S1).

    THE ONE WRITER for every destination `ADOPTER_BAR_PATHS` declares: the gate-leg manifest an
    adopter's whole bar reads, the receipt, `.governance/install.json` (TOOL-dRedressedBar-17), and
    its sidecar `.governance/install.sums`, written before the receipt (TOOL-dRedressedBar-19).
    Two verbs write the manifest since DEPL-cMendedVintage-13, and an exception between opening it
    and finishing it would hand the adopter a manifest that is not JSON — every leg of their bar,
    gone, on a deployer step that was only adding one. A receipt cut short the same way is one the
    next `apply`, `update` or `adopt` cannot parse.

    WHAT THIS DOES NOT CLAIM. No fsync and no directory sync, so this is not crash consistency:
    what it closes is a half-written file left by an EXCEPTION mid-write. Power loss is out of
    scope and always was.

    The temp file is a SIBLING, inside the destination's own directory. Two reasons, and both are
    load-bearing: `os.replace` raises across a filesystem boundary, which a shared temp root makes
    reachable and a sibling makes impossible; and a shared root is writable by principals the
    destination's directory is not, so the file to be renamed into place could be swapped before
    the rename. A stale sibling from a crashed run of an earlier vintage is overwritten here rather
    than swept, because an unknown temp file of unknown vintage is not this engine's to delete.
    """
    dest = pathlib.Path(dest)
    tmp = dest.with_name(dest.name + ".govkit-new")
    try:
        tmp.write_text(text, encoding="utf-8", newline="\n")
        os.replace(tmp, dest)
    finally:
        # THE CLEANUP RUNS ON THE SUCCESS PATH TOO, where `os.replace` has already consumed `tmp`
        # and this raises FileNotFoundError — an OSError, swallowed. Swallowed rather than
        # re-raised because this sits in a `finally`: an exception thrown from here REPLACES the
        # one that brought us here, and the caller would be told the temp file could not be
        # removed instead of why the write failed.
        try:
            tmp.unlink()
        except OSError:
            pass


def load_govkit():
    """The deployer beside this file: the running module where it is the program, else imported by
    its path, for the ten names this module borrows, govkit's `update` state and deployer readers:
    `derive_tool_root`, `resolve_prefix_token`, `load_deploy`, `git_pathspec`, `write_row_order`,
    `ATTENDED_ORDER_PREFIX`, `STAGING_JOURNAL_REL`, `RECLAIM_GUARD_SUFFIX`, `WRITE_LOCK_REL` and
    `take_write_lock` (TOOL-dSafePassage-35 S24). The remote ladder, the landing base, the
    revision-blob reader, the atomic writer (TOOL-dSafePassage-26 S1, S4, S14, S15), argv
    resolution and the kit-dir resolver are this module's own."""
    path = HERE / "govkit.py"
    for name in ("govkit", "__main__"):
        mod = sys.modules.get(name)
        if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
            return mod
    spec = importlib.util.spec_from_file_location("govkit", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["govkit"] = mod
    spec.loader.exec_module(mod)
    return mod


def resolve_landed_ref(root) -> str | None:
    """The default branch a row's introducing commit is derived along: the remote ladder's
    `<remote>/<branch>`, else the local `<branch>`, `main` where nothing names one; None when
    neither resolves, and then every row reads unlanded."""
    remote, branch, _observed, refusal = resolve_remote(root)
    if refusal:
        raise Refusal(refusal)
    branch = branch or "main"
    return next((ref for ref in ((f"{remote}/{branch}", branch) if remote else (branch,))
                 if run_git(root, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")), None)


def cmd_list(root, window: bool) -> int:
    """`list [--window]`: every row in order with its introducing commit and declaring file, the
    succession rows after them; or, under `--window`, each home a step row's `surfaces` declares,
    `open` or `closed by <step id>`. The landed ref is the remote ladder's default branch."""
    landed = resolve_landed_ref(root)
    rows = read_steps(root, None, landed or "")
    retired = read_retired(root, None, landed or "")
    if window:
        homes: dict[str, str | None] = {}
        for r in rows:
            for s in r.surfaces:
                home = s.split(":", 1)[1].split("#", 1)[0]
                if homes.get(home) is None:
                    homes[home] = r.id if r.introduced not in (None, UNLANDED) else None
        for home, by in homes.items():
            print(f"window: {home} · " + (f"closed by {by}" if by else "open"))
        print(f"window: {len(homes)} member(s), {sum(1 for b in homes.values() if b is None)} open · "
              f"landed ref {landed or 'none'}")
        return 0
    print(f"upgrade-steps: {len(rows)} step row(s) · {len(retired)} retired row(s) · landed ref "
          f"{landed or 'none, so every row reads unlanded'}")
    for i, r in enumerate(rows, 1):
        print(f"upgrade-steps: {i} · {r.id} · {r.introduced} · {r.file}")
    for r in retired:
        print(f"upgrade-steps: retired · {r.id} -> {r.successor} · {r.retired} · {r.file}")
    return 0


def cmd_frozen(root, base: str | None) -> int:
    """`frozen [--base <rev>]`: every landed row at the push base, frozen at HEAD (`check_frozen`)."""
    sha, _boundary, why = resolve_landing_base(root, base)
    if not sha:
        print(f"step-rows-frozen: FAILED · no base to compare against{why}")
        return 1
    n, problems = check_frozen(root, sha, "HEAD")
    for p in problems:
        print(f"step-rows-frozen: FAILED · {p}")
    print(f"step-rows-frozen: {n} landed row(s) at {sha[:8]} · {len(problems)} problem(s)")
    return 1 if problems else 0


def read_step_spawn_sites(paths) -> list[tuple[str, int, str]]:
    """(file name, line, enclosing function) of each `subprocess.run`, `subprocess.Popen` or
    `run_target_argv` call in `paths` whose argv expression reads a step row's phase: a subscript or
    attribute named `up`, `down`, `witness` or `resume`, or a `getattr` whose name is one of them or
    is not a literal at all. WHAT IT DOES NOT SEE: an argv read into a local first, which no
    dataflow here follows, so the one sanctioned site keeps its read inside the call."""
    def check_reads_phase(n) -> bool:
        if isinstance(n, ast.Subscript):
            return isinstance(n.slice, ast.Constant) and n.slice.value in STEP_PHASES
        if isinstance(n, ast.Attribute):
            return n.attr in STEP_PHASES
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "getattr" and len(n.args) > 1:
            return not isinstance(n.args[1], ast.Constant) or n.args[1].value in STEP_PHASES
        return False

    sites = []
    for path in map(pathlib.Path, paths):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        fns = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        for call in (n for n in ast.walk(tree) if isinstance(n, ast.Call)):
            f = call.func
            name = f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else ""
            if not (name == "run_target_argv" or (name in ("run", "Popen") and isinstance(f, ast.Attribute)
                                                  and isinstance(f.value, ast.Name) and f.value.id == "subprocess")):
                continue
            argv = call.args[0] if call.args else next((k.value for k in call.keywords if k.arg == "args"), None)
            if argv is None or not any(check_reads_phase(n) for n in ast.walk(argv)):
                continue
            owner = min((fn for fn in fns if fn.lineno <= call.lineno <= fn.end_lineno),
                        key=lambda fn: fn.end_lineno - fn.lineno, default=None)
            sites.append((path.name, call.lineno, owner.name if owner else "<module>"))
    return sites


# The fixture's three step programs and its target-only module (S6, §4 "The check's fixture steps").
FIXTURE_STEPS = {
    "clean.py": (
        "import json, os, subprocess, sys\n"
        "target, prefix, reports = sys.argv[1:4]\n"
        "open(os.path.join(target, 'stepped.txt'), 'w').close()\n"
        "add = subprocess.run(['git', '-C', target, 'add', 'stepped.txt'], capture_output=True)\n"
        "commit = subprocess.run(['git', '-C', target, '-c', 'user.name=gk-step', '-c', 'user.email=gk-step@invalid',\n"
        "                         'commit', '-q', '-m', 'step'], capture_output=True, timeout=60)\n"
        "cred = subprocess.run(['git', 'credential', 'fill'], capture_output=True, timeout=60,\n"
        "                      input=b'protocol=https\\nhost=gk-step.invalid\\n\\n')\n"
        "helpers = subprocess.run(['git', '-C', target, 'config', '--get-all', 'credential.helper'],\n"
        "                         capture_output=True, text=True)\n"
        "hooks = os.environ.get('GIT_CONFIG_VALUE_0', '')\n"
        "with open(os.path.join(reports, 'clean.json'), 'w', encoding='utf-8') as f:\n"
        "    json.dump({'env': sorted(os.environ), 'count': os.environ.get('GIT_CONFIG_COUNT'),\n"
        "               'pairs': sum(k.startswith('GIT_CONFIG_KEY_') for k in os.environ),\n"
        "               'key0': os.environ.get('GIT_CONFIG_KEY_0'),\n"
        "               'pair2': [os.environ.get('GIT_CONFIG_KEY_2'), os.environ.get('GIT_CONFIG_VALUE_2')],\n"
        "               'hooks': sorted(os.listdir(hooks)) if os.path.isdir(hooks) else None,\n"
        "               'isolated': sys.flags.isolated, 'cwd': os.getcwd(), 'prefix': prefix,\n"
        "               'add': add.returncode, 'commit': commit.returncode, 'cred': cred.returncode,\n"
        "               'helpers': helpers.stdout.splitlines()}, f)\n"),
    "status.py": (
        "import subprocess, sys\n"
        "p = subprocess.run(['git', '-C', sys.argv[1], 'status', '--porcelain'], capture_output=True, timeout=60)\n"
        "open(sys.argv[2], 'w', encoding='utf-8').write(str(p.returncode))\n"),
    "update.py": (
        "import subprocess, sys\n"
        "u = subprocess.run(['git', '-c', 'protocol.file.allow=always', '-C', sys.argv[1], 'submodule', 'update',\n"
        "                    '-q', '--init'], capture_output=True, timeout=60)\n"
        "p = subprocess.run(['git', '-C', sys.argv[1], 'status', '--porcelain'], capture_output=True, timeout=60)\n"
        "open(sys.argv[2], 'w', encoding='utf-8').write(f'{u.returncode} {p.returncode}')\n"),
    # TOOL-dSafePassage-37 S4: an unreachable object, then the gc that prunes it; a plain fetch.
    "gc.py": (
        "import subprocess, sys\n"
        "subprocess.run(['git', '-C', sys.argv[1], 'hash-object', '-w', '--stdin'], input=b'gk-unreachable\\n',\n"
        "               capture_output=True, timeout=60)\n"
        "p = subprocess.run(['git', '-C', sys.argv[1], 'gc', '-q', '--prune=now'], capture_output=True, timeout=120)\n"
        "open(sys.argv[2], 'w', encoding='utf-8').write(str(p.returncode))\n"),
    "fetch.py": (
        "import subprocess, sys\n"
        "p = subprocess.run(['git', '-C', sys.argv[1], 'fetch', '-q', sys.argv[3]], capture_output=True, timeout=60)\n"
        "sys.stderr.write(p.stderr.decode('utf-8', 'replace'))\n"
        "open(sys.argv[2], 'w', encoding='utf-8').write(str(p.returncode))\n"
        "sys.exit(p.returncode)\n"),
    # TOOL-dSafePassage-26 S13: the oid git computes for a CRLF file in the target, under the
    # step's environment, written for the parent to compare with its own.
    "hash.py": (
        "import subprocess, sys\n"
        "target, out = sys.argv[1:3]\n"
        "p = subprocess.run(['git', '-C', target, 'hash-object', '--path', 'crlf.txt', 'crlf.txt'],\n"
        "                   capture_output=True, text=True)\n"
        "open(out, 'w').write(p.stdout.strip())\n"
    ),
    "reaches.py": "import sys\nopen(sys.argv[1], 'w').close()\nimport adopter_only\n",
    "opens.py": "import sys\nsys.path.insert(0, sys.argv[1])\nimport adopter_only\n",
}
FIXTURE_ADOPTER_ONLY = (
    "import os\n"
    f"d = os.path.join(os.path.dirname(os.path.abspath(__file__)), {CANARY_DIR!r})\n"
    "os.makedirs(d, exist_ok=True)\n"
    "open(os.path.join(d, 'adopter_only'), 'w').close()\n")


def run_isolation_fixture(plant: str | None) -> int:
    """`fixture isolation [--plant <case>]` (S6): a scratch gov directory holding `FIXTURE_STEPS`
    and a scratch target repository under the temp root, and S1 to S5 observed over them. A `-stub`
    plant swaps one half of the contract in THIS process's globals only, so its red is observed with
    no switch in shipped code. An unmet expectation prints `isolation: FAILED`."""
    if plant == "callers":
        sites = read_step_spawn_sites([pathlib.Path(__file__).resolve(), HERE / "govkit.py"])
        for f, line, fn in sites:
            print(f"isolation: callers · a spawn of a step argv at {f}:{line}, in {fn}")
        if len(sites) == 1 and sites[0][0] == "upgrade_steps.py" and sites[0][2] == "run_step_isolated":
            print("isolation: callers · one spawn site of a step argv, inside run_step_isolated")
            return 0
        print(f"isolation: FAILED · callers · {len(sites)} spawn site(s) of a step argv, where the one "
              f"sanctioned site is inside run_step_isolated" + ("; the probe read nothing" if not sites else ""))
        return 1
    g, saved_env = globals(), dict(os.environ)
    saved = {k: g[k] for k in ("build_step_env", "resolve_step_argv", "check_target_local_config")}
    # A calling hook's GIT_DIR would point every fixture git call elsewhere; the caller's choice of
    # global and system config stays, so the parent's line endings vary (TOOL-dSafePassage-45 S4).
    for k in [k for k in os.environ if k.upper().startswith("GIT_")
              and k.upper() not in ("GIT_CONFIG_GLOBAL", "GIT_CONFIG_NOSYSTEM")]:
        del os.environ[k]
    try:
        with tempfile.TemporaryDirectory(prefix="gk-iso-", ignore_cleanup_errors=True) as td:
            return run_isolation_case(pathlib.Path(td), plant)
    finally:
        g.update(saved)
        os.environ.clear()
        os.environ.update(saved_env)


def run_isolation_case(tmp: pathlib.Path, plant: str | None) -> int:
    """One `fixture isolation` case over the fresh scratch `tmp`; `run_isolation_fixture` restores
    what a `-stub` plant swapped."""
    g = globals()
    gov, target, reports, canaries = tmp / "gov", tmp / "t", tmp / "reports", tmp / "canaries"
    (gov / FIXTURE_PREFIX / "steps").mkdir(parents=True)
    (gov / FIXTURE_PREFIX / HERE.name).mkdir()
    (gov / FIXTURE_PREFIX / HERE.name / REGISTRY_FILE).write_text("", encoding="utf-8")
    for name, text in FIXTURE_STEPS.items():
        (gov / FIXTURE_PREFIX / "steps" / name).write_text(text, encoding="utf-8", newline="\n")
    reports.mkdir()
    quiet = build_tree_git_env()
    # The scratch target through the factory (TOOL-dSafePassage-26 S19): its deploy file and the
    # adopter-only module a breach plant imports, committed once.
    load_fixture_target().build_target(tmp, 'prefix = "tools"\n', target.name,
                                       {"adopter_only.py": FIXTURE_ADOPTER_ONLY})
    witness = ["python", "-c", "import os, sys; sys.exit(not os.path.isfile(sys.argv[1]))", "{target}/stepped.txt"]

    def build_row(slug: str, up: list, needs: bool = False) -> StepRow:
        return StepRow(f"fixture/{slug}", up, ["python", "-c", "pass"], witness, "atomic", [], needs,
                       "fixture", 1, None)

    clean = build_row("clean", ["python", "{gov}/steps/clean.py", "{target}", "{prefix}", reports.as_posix()])
    report = reports / "clean.json"
    fails: list[str] = []

    def check_ok(ok: bool, what: str) -> None:
        if not ok:
            fails.append(what)

    def run_clean() -> dict:
        r = run_step_isolated(clean, "up", target, gov)
        print(f"isolation: {clean.id} · up · {r['verdict']}" + (f" · rc {r['rc']}: {r['tail']}" if r["verdict"] != "ok" else ""))
        try:
            return json.loads(report.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}  # no report, or one a shadowed `json` left empty: read as nothing reported

    def remove_pair(env: dict, key: str) -> dict:
        pairs = [(env.pop(f"GIT_CONFIG_KEY_{i}"), env.pop(f"GIT_CONFIG_VALUE_{i}"))
                 for i in range(int(env.pop("GIT_CONFIG_COUNT")))]
        pairs = [p for p in pairs if p[0] != key]
        for i, (k, v) in enumerate(pairs):
            env[f"GIT_CONFIG_KEY_{i}"], env[f"GIT_CONFIG_VALUE_{i}"] = k, v
        env["GIT_CONFIG_COUNT"] = str(len(pairs))
        return env

    contract_env = saved_build = g["build_step_env"]
    rc = 0
    if plant is None:
        rep = run_clean()
        eol = read_line_ending_config(target)  # TOOL-dSafePassage-26 S13: 3 plus these pairs
        # The contract's own names are what the builder returns over an EMPTY parent: a builder
        # that copies the parent adds nothing there, so the oracle is not the code under test. The
        # carried line-ending pairs are the parent's by design, so their names are named here.
        held = dict(os.environ)
        os.environ.clear()
        try:
            allowed = set(STEP_ENV_KEEP) | set(contract_env(tmp)) | {
                f"GIT_CONFIG_{kv}_{i}" for i in range(3, 3 + len(eol)) for kv in ("KEY", "VALUE")}
        finally:
            os.environ.update(held)
        extra = sorted(set(rep.get("env", [])) - allowed)
        print(f"isolation: {clean.id} · env names outside the allowlist and the contract: {extra or 'none'}")
        print(f"isolation: {clean.id} · GIT_CONFIG_COUNT {rep.get('count')} · {rep.get('pairs')} "
              f"GIT_CONFIG_KEY_<n> pair(s) · pair 2 {rep.get('pair2')} · {rep.get('key0')} holds "
              f"{rep.get('hooks')} · sys.flags.isolated {rep.get('isolated')} · cwd {rep.get('cwd')}")
        check_ok(bool(rep) and rep.get("add") == 0, "clean's report is missing, or its git add failed")
        check_ok(not extra, f"names outside the allowlist reached the step: {extra}")
        # TOOL-dSafePassage-45 S4: the count is the pairs present, never a total typed here.
        check_ok(rep.get("count") == str(rep.get("pairs")) and rep.get("pair2") == ["protocol.ext.allow", "never"]
               and rep.get("key0") == "core.hooksPath" and rep.get("hooks") == [],
               "GIT_CONFIG_COUNT is not the GIT_CONFIG_KEY_<n> pairs present, with protocol.ext.allow = never "
               "at index 2 and core.hooksPath naming an empty directory")
        check_ok(rep.get("isolated") == 1, "the leading python ran without -I")
        check_ok(bool(rep) and pathlib.Path(rep["cwd"]).resolve() == gov.resolve(), "the working directory is not gov's root")
        check_ok(rep.get("prefix") == FIXTURE_PREFIX, "{prefix} did not resolve to the target's install prefix")
        check_ok(check_needs_target(clean, target, gov) == "isolated", "clean does not read isolated")
    elif plant in ("hook", "hook-stub"):
        subprocess.run(["git", "-C", str(target), "config", "core.hooksPath", ".githooks"], env=quiet, check=True)
        planted = write_target_plants(target, canaries)
        check_ok(all(any(p.endswith(f".githooks/{h}") for p in planted) for h in ("post-index-change", "pre-commit")),
               "no post-index-change and pre-commit planted under the target's own core.hooksPath")
        if plant == "hook-stub":
            g["build_step_env"] = lambda scratch, target=None: remove_pair(saved_build(scratch, target), "core.hooksPath")
        rep = run_clean()
        check_ok(rep.get("add") == 0, "clean's git add did not run")
        hit = [c for c in read_plant_canaries(canaries) if c.startswith("hook-")]
        print(f"isolation: hook canary: {'present · ' + ', '.join(hit) if hit else 'absent'}")
        rc = 1 if hit else 0
    elif plant in ("module", "module-stub"):
        write_target_plants(target, canaries)
        os.environ["PYTHONPATH"] = str(target)
        if plant == "module-stub":
            saved_argv = g["resolve_step_argv"]
            g["build_step_env"] = lambda scratch, target=None: dict(os.environ)
            g["resolve_step_argv"] = lambda argv, ctx, step_id="a step": [
                a for a in saved_argv(argv, ctx, step_id) if a != "-I"]
        run_clean()
        hit = [c for c in read_plant_canaries(canaries) if c.startswith("module-")]
        print(f"isolation: module canary: {'present · ' + ', '.join(hit) if hit else 'absent'}")
        rc = 1 if hit else 0
    elif plant in ("credential", "credential-stub"):
        canaries.mkdir()
        cfg = tmp / "planted.gitconfig"
        cfg.write_text(f"[credential]\n\thelper = \"!f() {{ : > '{(canaries / 'credential-helper').as_posix()}'; }}; f\"\n",
                       encoding="utf-8", newline="\n")
        os.environ.update({"GIT_CONFIG_GLOBAL": str(cfg), "GH_TOKEN": "gk-planted-token"})
        if plant == "credential-stub":
            g["build_step_env"] = lambda scratch, target=None: {**remove_pair(saved_build(scratch, target), "credential.helper"),
                                                   "GIT_CONFIG_GLOBAL": os.environ["GIT_CONFIG_GLOBAL"],
                                                   "GH_TOKEN": os.environ["GH_TOKEN"]}
        rep = run_clean()
        hit = read_plant_canaries(canaries)
        token = "GH_TOKEN" in rep.get("env", [])
        print(f"isolation: credential canary: {'present · ' + ', '.join(hit) if hit else 'absent'}")
        print(f"isolation: token: {'present · GH_TOKEN reached the step' if token else 'absent'}")
        print(f"isolation: git credential fill exits {rep.get('cred')} · credential.helper reads {rep.get('helpers')}")
        check_ok(bool(rep) and rep.get("cred") != 0, "git credential fill did not exit non-zero")
        if plant == "credential":
            check_ok(rep.get("helpers") == [""], "credential.helper does not read only the empty value")
        rc = 1 if hit or token else 0
    elif plant == "needs-target":
        ran = reports / "ran-reaches-attended"
        reaches = build_row("reaches", ["python", "{gov}/steps/reaches.py", (reports / "ran-reaches").as_posix()])
        attended = build_row("reaches-attended", ["python", "{gov}/steps/reaches.py", ran.as_posix()], True)
        check_ok(check_needs_target(reaches, target, gov) == "needs-target", "reaches does not read needs-target")
        check_ok((reports / "ran-reaches").is_file(), "reaches never ran, so its needs-target reads nothing")
        check_ok(check_needs_target(attended, target, gov) == "attended", "the declaring copy does not read attended")
        print(f"isolation: {attended.id} · own canary {'present: it spawned' if ran.exists() else 'absent'}")
        check_ok(not ran.exists(), "an attended row spawned")
        rc = 1
    elif plant == "breach":
        opens = build_row("opens", ["python", "{gov}/steps/opens.py", "{target}"])
        check_ok(check_needs_target(opens, target, gov) == "breach", "opens does not read breach")
        rc = 1
    elif plant == "token":
        tok = build_row("token", ["python", "{gov}/steps/clean.py", "{unknown}", "{prefix}", reports.as_posix()])
        try:
            run_step_isolated(tok, "up", target, gov)
            check_ok(False, "a row holding {unknown} was not refused")
        except Refusal as e:
            print(f"isolation: {tok.id} · refused · {e}")
        check_ok(not report.exists(), "the row holding {unknown} spawned")
        rc = 1
    elif plant == "autocrlf":
        # TOOL-dSafePassage-26 S13, AC12: the parent at core.autocrlf=true by command scope, the
        # target holding a CRLF file and no text attribute; the step must hash as the parent does.
        (target / "crlf.txt").write_bytes(b"one\r\ntwo\r\n")
        os.environ.update({"GIT_CONFIG_COUNT": "1", "GIT_CONFIG_KEY_0": "core.autocrlf",
                           "GIT_CONFIG_VALUE_0": "true"})
        out = reports / "hash.txt"
        r = run_step_isolated(build_row("hash", ["python", "{gov}/steps/hash.py", "{target}", out.as_posix()]),
                              "up", target, gov)
        mine = subprocess.run(["git", "-C", str(target), "hash-object", "--path", "crlf.txt", "crlf.txt"],
                              capture_output=True, text=True, encoding="utf-8").stdout.strip()
        raw = subprocess.run(["git", "-C", str(target), "-c", "core.autocrlf=false", "hash-object",
                              "--path", "crlf.txt", "crlf.txt"], capture_output=True, text=True, encoding="utf-8").stdout.strip()
        got = out.read_text(encoding="utf-8").strip() if out.is_file() else ""
        print(f"isolation: fixture/hash · up · {r['verdict']} · the step's oid {got or 'none'} · the parent's "
              f"{mine} · {'equal' if got == mine else 'DIFFERENT'}")
        check_ok(r["verdict"] == "ok" and bool(got) and got == mine, "the step hashed the CRLF file otherwise than the parent")
        check_ok(mine != raw, "LIVENESS: core.autocrlf=true does not move this file's oid, so the plant grades nothing")
    elif plant == "autocrlf-local":
        # TOOL-dSafePassage-35 S27: the target's local core.autocrlf=false wins over the parent's
        # global true, in the step as in the parent.
        (target / "crlf.txt").write_bytes(b"one\r\ntwo\r\n")
        glob = tmp / "global.gitconfig"
        glob.write_text("[core]\n\tautocrlf = true\n", encoding="utf-8", newline="\n")
        os.environ["GIT_CONFIG_GLOBAL"] = str(glob)
        subprocess.run(["git", "-C", str(target), "config", "core.autocrlf", "false"], check=True)
        out = reports / "hash.txt"
        r = run_step_isolated(build_row("hash", ["python", "{gov}/steps/hash.py", "{target}", out.as_posix()]),
                              "up", target, gov)
        mine = subprocess.run(["git", "-C", str(target), "hash-object", "--path", "crlf.txt", "crlf.txt"],
                              capture_output=True, text=True, encoding="utf-8").stdout.strip()
        crlf = subprocess.run(["git", "-C", str(target), "-c", "core.autocrlf=true", "hash-object",
                               "--path", "crlf.txt", "crlf.txt"], capture_output=True, text=True, encoding="utf-8").stdout.strip()
        got = out.read_text(encoding="utf-8").strip() if out.is_file() else ""
        print(f"isolation: fixture/hash · up · {r['verdict']} · the step's oid {got or 'none'} · the parent's "
              f"{mine} · {'equal' if got == mine else 'DIFFERENT'}")
        check_ok(r["verdict"] == "ok" and bool(got) and got == mine,
               "the step hashed the CRLF file otherwise than the parent, whose target says autocrlf=false")
        check_ok(mine != crlf, "LIVENESS: the parent's global autocrlf=true is not what the target's local value overrides")
    elif plant == "local-url-userinfo":
        # TOOL-dSafePassage-35 S8: a credential in the target's remote URL refuses the step, naming
        # the key and its file and never the value; an scp-form remote carries none and runs.
        cfg = target / ".git" / "config"
        user, secret = "gk-planted-user", "gk-planted-secret"
        base_cfg = cfg.read_text(encoding="utf-8")
        cfg.write_text(base_cfg + f"[remote \"{FIXTURE_REMOTE}\"]\n\turl = https://{user}:{secret}@example.invalid/x.git\n",
                       encoding="utf-8", newline="\n")
        try:
            run_clean()
            refused = ""
        except Refusal as e:
            refused = str(e)
            print(f"isolation: {clean.id} · refused · {e}")
        named = f"remote.{FIXTURE_REMOTE}.url in .git/config"
        check_ok(named in refused, f"the step was not refused naming {named}")
        check_ok(user not in refused and secret not in refused, "the refusal prints the URL's user or password")
        check_ok(not report.exists(), "the refused step spawned")
        cfg.write_text(base_cfg + f"[remote \"{FIXTURE_REMOTE}\"]\n\turl = git@example.invalid:x.git\n",
                       encoding="utf-8", newline="\n")
        try:
            rep = run_clean()
            print(f"isolation: scp-form remote · not refused · git add exits {rep.get('add')}")
            check_ok(rep.get("add") == 0, "the scp-form remote: clean's git add did not run")
        except Refusal as e:
            check_ok(False, f"an scp-form remote with no credential was refused: {e}")
        rc = 1
    elif plant == "ssh-scheme-bare-user":
        # TOOL-dSafePassage-44 S5: an ssh-scheme remote and insteadOf key with a bare user carry no
        # credential, so the step spawns.
        cfg = target / ".git" / "config"
        cfg.write_text(cfg.read_text(encoding="utf-8") + "[remote \"origin\"]\n\turl = ssh://git@github.com/o/r.git\n"
                       "[url \"ssh://git@github.com/\"]\n\tinsteadOf = https://github.com/\n",
                       encoding="utf-8", newline="\n")
        try:
            rep = run_clean()
            print(f"isolation: ssh-scheme bare user · not refused · git add exits {rep.get('add')}")
            check_ok(rep.get("add") == 0, "the ssh-scheme bare-user remote: clean's git add did not run")
        except Refusal as e:
            check_ok(False, f"an ssh-scheme remote with a bare user was refused: {e}")
    elif plant == "sendemail-identity-cmd":
        # TOOL-dSafePassage-48 S3: a send-email executor key in its identity form refuses the step
        # before any spawn, naming the key as git prints it and its file.
        canaries.mkdir()
        cfg = target / ".git" / "config"
        cfg.write_text(cfg.read_text(encoding="utf-8") + "[sendemail]\n\tidentity = work\n[sendemail \"work\"]\n"
                       f"\tccCmd = \": > '{(canaries / 'sendemail-cccmd').as_posix()}'\"\n",
                       encoding="utf-8", newline="\n")
        try:
            run_clean()
            refused = ""
        except Refusal as e:
            refused = str(e)
            print(f"isolation: {clean.id} · refused · {e}")
        hit = read_plant_canaries(canaries)
        print(f"isolation: sendemail canary: {'present · ' + ', '.join(hit) if hit else 'absent'}")
        check_ok("sendemail.work.cccmd in .git/config" in refused,
               "the step was not refused naming sendemail.work.cccmd in .git/config")
        check_ok(not report.exists() and not hit, "the refused step spawned, or its executor ran")
        rc = 1
    elif plant in ("submodule-url-userinfo", "insteadof-userinfo", "http-url-key-userinfo",
                   "proxy-schemeless-userinfo", "insteadof-dotted-userinfo", "subsection-password-space"):
        # TOOL-dSafePassage-38 S3: a URL credential in a value or a key segment that no instance row
        # names refuses the step, and the refusal prints the key redacted and never the credential.
        # TOOL-dSafePassage-45 S7, S8: a proxy's scheme-less userinfo, and a dotted user name in a key.
        cred = "https://dspuser38:dsppass38@example.invalid/"
        section, key = {"submodule-url-userinfo": ('submodule "s"]\n\turl = ' + cred + "s.git", "submodule.s.url"),
                        "insteadof-userinfo": (f'url "{cred}"]\n\tinsteadOf = https://example.invalid/',
                                               "url.https://<redacted>@example.invalid/.insteadof"),
                        "http-url-key-userinfo": (f'http "{cred}"]\n\tsslKey = /k',
                                                  "http.https://<redacted>@example.invalid/.sslkey"),
                        "proxy-schemeless-userinfo": ("http]\n\tproxy = dspuser45:dsppass45@proxy:3128", "http.proxy"),
                        "insteadof-dotted-userinfo": ('url "https://first.last:dsppass45@host/"]\n\tinsteadOf = https://h/',
                                                      "url.https://<redacted>@host/.insteadof"),
                        # TOOL-dSafePassage-49 S19: a password holding a space, which S9's pattern stops at.
                        "subsection-password-space": ('http "https://u:se cret@h/"]\n\tsslKey = x',
                                                      "http.https://<redacted>@h/.sslkey")}[plant]
        tokens = (("dspuser45", "dsppass45", "first.last") if plant in ("proxy-schemeless-userinfo", "insteadof-dotted-userinfo")
                  else ("se cret", "cret") if plant == "subsection-password-space" else ("dspuser38", "dsppass38"))
        cfg = target / ".git" / "config"
        cfg.write_text(cfg.read_text(encoding="utf-8") + f"[{section}\n", encoding="utf-8", newline="\n")
        try:
            run_clean()
            refused = ""
        except Refusal as e:
            refused = str(e)
            print(f"isolation: {clean.id} · refused · {e}")
        check_ok(f"{key} in .git/config" in refused, f"the step was not refused naming {key} in .git/config")
        check_ok(not any(t in refused for t in tokens), "the refusal prints the URL's user or password")
        if plant == "subsection-password-space":
            # AC14: the named entries, between TOOL-dSafePassage-24's fixed lead and tail, hold no
            # 3-character piece of the password; the lead's own ` credential` spells `cre` and ` cr`.
            entries = refused.partition("sends as a credential, ")[2].partition(", so nothing was spawned")[0]
            pieces = sorted({tokens[0][i:i + 3] for i in range(len(tokens[0]) - 2)} & {
                entries[i:i + 3] for i in range(len(entries) - 2)})
            print(f"isolation: the refusal's named entries · {entries or 'NONE'} · password pieces in them: "
                  f"{pieces or 'none'}")
            check_ok(f"{key} in .git/config" in entries and not pieces,
                   "the refusal's named entries are absent, or name the key otherwise, or print a piece of the password")
        check_ok(not report.exists(), "the refused step spawned")
        rc = 1
    elif plant.startswith("local-"):
        # TOOL-dSafePassage-24 S4 and TOOL-dSafePassage-29 S4: an executor in the target's own config,
        # each canary naming itself; clean.py commits what it stages, so a signing program and a
        # config-declared pre-commit hook are reached.
        kind = plant.removeprefix("local-").removesuffix("-stub")
        canaries.mkdir()

        def render_runs(name: str, then: str = "") -> str:
            return f"\": > '{(canaries / name).as_posix()}'{then}\""

        cfg, included, gpg = target / ".git" / "config", tmp / "included.gitconfig", tmp / "gpg-canary.sh"
        # TOOL-dSafePassage-37 S4: `recent-objects-hook` gc's a step, `ext-transport` fetches from a
        # remote whose `ext::` command writes the canary, `% ` being that transport's escaped space.
        ran = {"recent-objects-hook": "gc", "ext-transport": "fetch"}.get(kind)
        done = reports / f"{ran}.rc" if ran else report
        step = build_row(ran, ["python", f"{{gov}}/steps/{ran}.py", "{target}", done.as_posix(), FIXTURE_REMOTE]) if ran else clean
        ext = "ext::sh -c " + f": > '{(canaries / 'ext-transport').as_posix()}'".replace("%", "%%").replace(" ", "% ")
        if kind == "gpg":
            gpg.write_text(f"#!/bin/sh\n: > '{(canaries / 'gpg-program').as_posix()}'\nexit 1\n",
                           encoding="utf-8", newline="\n")
            gpg.chmod(0o755)
        planted = {"filter": f"[filter \"canary\"]\n\tclean = {render_runs('filter-clean', '; cat')}\n",
                   "process": f"[filter \"canary\"]\n\tprocess = {render_runs('filter-process')}\n",
                   "fsmonitor": f"[core]\n\tfsmonitor = {render_runs('fsmonitor')}\n",
                   "gpg": f"[commit]\n\tgpgsign = true\n[gpg]\n\tprogram = {gpg.as_posix()}\n",
                   "hook": f"[hook \"canary\"]\n\tcommand = {render_runs('hook-command')}\n\tevent = pre-commit\n",
                   "recent-objects-hook": f"[gc]\n\trecentObjectsHook = {render_runs('recent-objects-hook')}\n",
                   "ext-transport": f"[protocol]\n\tallow = always\n[remote \"{FIXTURE_REMOTE}\"]\n\turl = \"{ext}\"\n"
                                    f"\tfetch = +refs/heads/*:refs/remotes/{FIXTURE_REMOTE}/*\n"}
        if kind == "include":
            included.write_text(planted["filter"], encoding="utf-8", newline="\n")
            cfg.write_text(f"[include]\n\tpath = {included.as_posix()}\n", encoding="utf-8", newline="\n")
        else:
            with cfg.open("a", encoding="utf-8", newline="\n") as f:
                f.write(planted[kind])
        if kind in ("filter", "process", "include"):
            (target / ".gitattributes").write_text("*.txt filter=canary\n", encoding="utf-8", newline="\n")
        if plant == "local-ext-transport-stub":
            g["build_step_env"] = lambda scratch, target=None: remove_pair(saved_build(scratch, target), "protocol.ext.allow")
        elif plant.endswith("-stub"):
            g["check_target_local_config"] = lambda t: []
        key = {"filter": "filter.canary.clean", "process": "filter.canary.process",
               "fsmonitor": "core.fsmonitor", "include": "filter.canary.clean", "gpg": "gpg.program",
               "hook": "hook.canary.command", "recent-objects-hook": "gc.recentobjectshook"}.get(kind)
        where = included.as_posix() if kind == "include" else ".git/config"
        r = {}
        try:
            if ran:
                r = run_step_isolated(step, "up", target, gov)
                print(f"isolation: {step.id} · up · {r['verdict']}" + (f" · rc {r['rc']}: {r['tail']}" if r["verdict"] != "ok" else ""))
            else:
                run_clean()
            refused = ""
        except Refusal as e:
            refused = str(e)
            print(f"isolation: {step.id} · refused · {e}")
        hit = read_plant_canaries(canaries)
        print(f"isolation: {kind} canary: {'present · ' + ', '.join(hit) if hit else 'absent'}")
        if kind == "ext-transport" and not plant.endswith("-stub"):
            check_ok(not refused and r.get("verdict") == "failed" and "transport 'ext' not allowed" in r.get("tail", ""),
                   "the step's fetch did not fail with git's own refusal of the ext transport")
            check_ok(not hit, "the ext:: remote's command ran inside the step")
        elif plant.endswith("-stub"):
            check_ok(not refused and done.exists(), "the stubbed check still refused, so nothing spawned")
        else:
            check_ok(f"{key} in {where}" in refused, f"the step was not refused naming {key} in {where}")
            check_ok(not done.exists() and not hit, "the refused step spawned, or its executor ran")
        if kind == "fsmonitor" and not plant.endswith("-stub"):
            cfg.write_text(cfg.read_text(encoding="utf-8").replace(planted["fsmonitor"], "[core]\n\tfsmonitor = false\n"),
                           encoding="utf-8", newline="\n")
            try:
                rep = run_clean()
                print(f"isolation: core.fsmonitor=false · not refused · git add exits {rep.get('add')}")
                check_ok(rep.get("add") == 0, "core.fsmonitor=false: clean's git add did not run")
            except Refusal as e:
                check_ok(False, f"core.fsmonitor=false was refused: {e}")
        rc = 1
    elif plant.startswith("submodule-") or plant in ("gitmodules-malformed", "gitmodules-unreadable", "gitmodules-fifo",
                                                     "gitmodules-symlink"):
        # TOOL-dSafePassage-30 S4: the filter in a submodule's own config, which the superproject's
        # `git status` runs; `nested` sets it one submodule deeper, `unpopulated` in a submodule the
        # target does not check out. TOOL-dSafePassage-36 S3: `unpopulated-worktree` sets it in a
        # linked-worktree target's own de-initialised submodule, whose step updates it and runs
        # `git status`, and `main-only` in the main worktree's, which that target never enters.
        # TOOL-dSafePassage-42 S8: `fsmonitor` sets `core.fsmonitor` in a checked-out submodule, which
        # an index read there would run; S22: `name-differs` sets the filter in a de-initialised
        # submodule named `nm` at `lib/p`, reached only through `modules/`, then drops its mapping.
        # TOOL-dSafePassage-45 S12: `ref-named-config` gives a checked-out submodule a branch named
        # `config`, `config-malformed` a de-initialised one a config ending `[core`; S13:
        # `gitmodules-malformed` leaves the target's `.gitmodules` unparseable, and
        # `nested-name-differs` nests `in` at `q` inside `nm` at `lib/p`, then de-initialises `nm`.
        # TOOL-dSafePassage-47 S4: `name-slashed` sets it in a de-initialised submodule named `lib/x`,
        # whose repository the walk reaches only through the `lib/` name segment.
        # TOOL-dSafePassage-49 S7: `format-unknown` gives a de-initialised one a repository format
        # git does not know; S18: `gitmodules-unreadable` makes the target's `.gitmodules` a directory.
        # TOOL-dSafePassage-51 S6: `modules-link-loop` links `.git/modules/a/loop` back to
        # `.git/modules`; S15: `gitmodules-fifo` makes the target's `.gitmodules` a FIFO, where one can be.
        # TOOL-dSafePassage-53 S2: `modules-not-a-directory` makes `.git/modules/a` a sound repository
        # whose `modules` is a regular file. TOOL-dSafePassage-54 S1: `sound-no-nested` is the tree
        # git's own `submodule add` writes, no key set and no `modules/` under `.git/modules/sub`.
        # TOOL-dSafePassage-56 S3: `modules-link-nested` makes `.git/modules/a` a sound repository
        # whose `modules` links back to `.git/modules`, `modules-link-outside` one whose `modules`
        # links to a scratch directory holding a repository whose config sets the filter.
        # TOOL-dSafePassage-59 S6: `modules-root-link` makes `.git/modules` itself a link to a scratch
        # directory; S7: `modules-link-dangling` puts a link whose target is gone under it; S8:
        # `gitmodules-symlink` makes the target's `.gitmodules` a symlink, where the host makes one.
        kind =plant.removeprefix("submodule-").removesuffix("-stub")
        linked = kind in ("unpopulated-worktree", "main-only")
        if kind == "gitmodules-fifo" and not hasattr(os, "mkfifo"):
            print("isolation: skip — gitmodules-fifo needs os.mkfifo, which this host lacks")
            return 0
        fx = ["git", "-c", "protocol.file.allow=always", "-c", "user.name=gk-fx", "-c", "user.email=gk-fx@invalid"]

        def run_fx_git(cwd: pathlib.Path, *args: str) -> None:
            subprocess.run([*fx, "-C", str(cwd), *args], env=quiet, capture_output=True, check=True)

        def build_src(name: str, *subs: pathlib.Path) -> pathlib.Path:
            d = tmp / "src" / name
            d.mkdir(parents=True)
            run_fx_git(d, "init", "-q")
            (d / ".gitattributes").write_text("*.txt filter=canary\n", encoding="utf-8", newline="\n")
            (d / "a.txt").write_text("a\n", encoding="utf-8", newline="\n")
            for s in subs:
                run_fx_git(d, "submodule", "add", "-q", *(("--name", "in", s.as_posix(), "q") if kind == "nested-name-differs"
                                                      else (s.as_posix(), s.name)))
            run_fx_git(d, "add", "-A")
            run_fx_git(d, "commit", "-q", "-m", "fx")
            return d

        nested = kind in ("nested", "nested-name-differs")
        sub = build_src("sub", *((build_src("inner"),) if nested else ()))
        run_fx_git(target, "submodule", "add", "-q", *(("--name", "nm", sub.as_posix(), "lib/p")
                                                   if kind in ("name-differs", "nested-name-differs")
                                                   else (sub.as_posix(), "lib/x" if kind == "name-slashed" else "sub")))
        if nested:
            run_fx_git(target, "submodule", "update", "-q", "--init", "--recursive")
        stepped = target
        if linked:
            run_fx_git(target, "commit", "-q", "-m", "fx")
            stepped = tmp / "wt"
            run_fx_git(target, "worktree", "add", "-q", stepped.as_posix())
            run_fx_git(stepped, "-c", "protocol.file.allow=always", "submodule", "update", "-q", "--init")
        deep = {"nested": target / "sub" / "inner", "unpopulated-worktree": stepped / "sub",
                "name-differs": target / FIXTURE_SUB_HOME / "p", "name-slashed": target / FIXTURE_SUB_HOME / "x", "nested-name-differs": target / FIXTURE_SUB_HOME / "p" / "q"}.get(kind, target / "sub")
        key = "core.fsmonitor" if kind == "fsmonitor" else "filter.canary.clean"
        unkeyed = kind in ("ref-named-config", "config-malformed", "gitmodules-malformed", "format-unknown",
                           "gitmodules-unreadable", "modules-link-loop", "gitmodules-fifo", "modules-not-a-directory",
                           "sound-no-nested", "modules-link-nested", "modules-link-outside", "modules-root-link",
                           "modules-link-dangling", "gitmodules-symlink")
        sound = kind in ("ref-named-config", "sound-no-nested")  # the step is not refused, exit 0
        if kind == "ref-named-config":
            run_fx_git(deep, "branch", "config")  # refs/heads/config and logs/refs/heads/config, two files named config
        elif not unkeyed:
            run_fx_git(deep, "config", key, f": > '{(canaries / 'fsmonitor').as_posix()}'" if kind == "fsmonitor"
                   else f": > '{(canaries / 'filter-clean').as_posix()}'; cat")
        if kind in ("unpopulated", "name-differs", "name-slashed", "config-malformed", "format-unknown",
                    "gitmodules-unreadable", "modules-link-loop", "gitmodules-fifo", "modules-not-a-directory",
                    "modules-link-nested", "modules-link-outside", "modules-root-link", "modules-link-dangling",
                    "gitmodules-symlink") or linked:
            run_fx_git(stepped, "submodule", "deinit", "-q", "-f", {"name-differs": "lib/p", "name-slashed": "lib/x"}.get(kind, "sub"))
        else:
            # same size, new mtime: git cannot tell it changed without the clean filter
            (deep / "a.txt").write_text("b\n", encoding="utf-8", newline="\n")
            os.utime(deep / "a.txt", (1, 1))
        shutil.rmtree(canaries, ignore_errors=True)
        canaries.mkdir()
        if kind in ("config-malformed", "gitmodules-malformed"):
            broken = target / ".git" / "modules" / "sub" / "config" if kind == "config-malformed" else target / ".gitmodules"
            with broken.open("a", encoding="utf-8", newline="\n") as f:
                f.write("[core\n")  # an unterminated section: git exits 128, `bad config line`
        elif kind == "format-unknown":
            # `config --list` exits 0 here with only a warning; `rev-parse` exits 128
            run_fx_git(target, "config", "-f", ".git/modules/sub/config", "core.repositoryformatversion", "99")
        elif kind == "gitmodules-unreadable":
            (target / ".gitmodules").unlink()
            (target / ".gitmodules").mkdir()  # `config -f` exits 1 on it, as on a missing file
        elif kind == "gitmodules-fifo":
            (target / ".gitmodules").unlink()
            os.mkfifo(target / ".gitmodules")  # an open blocks until a writer appears
        elif kind == "gitmodules-symlink":
            real = tmp / "gitmodules-real"
            shutil.copyfile(target / ".gitmodules", real)
            (target / ".gitmodules").unlink()
            try:
                os.symlink(real, target / ".gitmodules")
            except (OSError, NotImplementedError) as e:
                print(f"isolation: skip — gitmodules-symlink needs os.symlink, which this host refuses ({e})")
                return 0
        elif kind in ("modules-link-loop", "modules-link-nested", "modules-link-outside", "modules-root-link",
                      "modules-link-dangling"):
            mods = target / ".git" / "modules"
            if kind == "modules-link-loop":
                loop, to = mods / "a" / "loop", mods
                loop.parent.mkdir()
            elif kind == "modules-root-link":
                loop, to = mods, tmp / "modules-root"
                mods.rename(to)
            elif kind == "modules-link-dangling":
                loop, to = mods / "dangling", tmp / "gone"
                to.mkdir()
            else:
                run_fx_git(target, "init", "-q", "--bare", ".git/modules/a")
                loop, to = mods / "a" / "modules", mods
                if kind == "modules-link-outside":
                    to = tmp / "outside"
                    run_fx_git(tmp, "init", "-q", "--bare", "outside/x")
                    run_fx_git(to / "x", "config", "filter.canary.clean", f": > '{(canaries / 'filter-clean').as_posix()}'; cat")
            if os.name == "nt":
                subprocess.run(["cmd", "/c", "mklink", "/J", str(loop), str(to)], capture_output=True, check=True)
            else:
                os.symlink(to, loop, target_is_directory=True)
            if kind == "modules-link-dangling":
                to.rmdir()  # the link stays, its target gone
        elif kind == "modules-not-a-directory":
            run_fx_git(target, "init", "-q", "--bare", ".git/modules/a")
            (target / ".git" / "modules" / "a" / "modules").write_text("", encoding="utf-8")
        elif sound:
            rows = read_target_repositories(target, lambda d, label: False)
            for r in rows if isinstance(rows, list) else ():
                print(f"isolation: population · {r['git_dir']} · reached by {r['reached_by'] or 'the target'}")
            sub_dir = (target / ".git" / "modules" / "sub").resolve()
            check_ok(isinstance(rows, list) and [r["git_dir"] for r in rows]
                   == [(target / ".git").resolve().as_posix(), sub_dir.as_posix()],
                   f"the population is not one row per real repository, the target and sub: {rows}")
            if kind == "ref-named-config":
                check_ok((sub_dir / "refs" / "heads" / "config").is_file(),
                       "LIVENESS: no ref named config was planted, so the walk grades nothing")
            else:
                check_ok((sub_dir / "HEAD").is_file() and not (sub_dir / "modules").exists(),
                       "LIVENESS: git's submodule add wrote no .git/modules/sub, or one holding modules/")
        where = {"filter": ".git/modules/sub/config (submodule sub)",
                 "nested": ".git/modules/sub/modules/inner/config (submodule sub/inner)",
                 "unpopulated": ".git/modules/sub/config (submodule sub)",
                 "unpopulated-worktree": (target / ".git" / "worktrees" / "wt" / "modules" / "sub").resolve().as_posix()
                 + "/config (submodule sub)",
                 "fsmonitor": ".git/modules/sub/config (submodule sub)",
                 "name-differs": ".git/modules/nm/config (submodule lib/p)",
                 "name-slashed": ".git/modules/lib/x/config (submodule lib/x)",
                 "nested-name-differs": ".git/modules/nm/modules/in/config (submodule lib/p/q)"}.get(kind, "")
        done = reports / "status.rc"
        status = (build_row("update", ["python", "{gov}/steps/update.py", "{target}", done.as_posix()]) if linked
                  else build_row("status", ["python", "{gov}/steps/status.py", "{target}", done.as_posix()]))
        if plant.endswith("-stub"):
            g["check_target_local_config"] = lambda t: []
        try:
            r = run_step_isolated(status, "up", stepped, gov)
            print(f"isolation: {status.id} · up · {r['verdict']}")
            refused = ""
        except Refusal as e:
            refused = str(e)
            print(f"isolation: {status.id} · refused · {e}")
        hit = read_plant_canaries(canaries)
        print(f"isolation: {kind} canary: {'present · ' + ', '.join(hit) if hit else 'absent'}")
        if kind == "main-only":
            check_ok(not refused and done.exists() and not hit,
                   "the main worktree's submodule config refused the linked worktree's step, or its filter ran")
        elif sound:
            check_ok(not refused and done.exists(), f"the {kind} submodule refused the step")
        elif unkeyed:
            name = {"config-malformed": ".git/modules/sub/config or a file it includes does not read",
                    "format-unknown": "/.git/modules/sub: git will not open this repository",
                    "modules-link-loop": "/.git/modules/a/loop is a link under modules/",
                    "modules-link-nested": "/.git/modules/a/modules is a link the walk would enter",
                    "modules-link-outside": "/.git/modules/a/modules is a link the walk would enter",
                    "modules-root-link": "/.git/modules is a link the walk would enter",
                    "modules-link-dangling": "/.git/modules/dangling is a link under modules/",
                    "gitmodules-symlink": "/.gitmodules does not read: it is a link",
                    "modules-not-a-directory": "/.git/modules/a/modules does not list (NotADirectoryError"}.get(
                        kind, "/.gitmodules does not read")
            check_ok(name in refused and not done.exists(), f"the step was not refused naming `{name}`, or it spawned")
            # TOOL-dSafePassage-76 S8: the walk's own refusal, never blamed on a config key
            lead = f"{status.id} up: the repositories a step could enter from the target could not be cleared: "
            check_ok(refused.startswith(lead), f"the refusal does not begin `{lead}`: {refused}")
        elif plant.endswith("-stub"):
            check_ok(not refused and done.exists(), "the stubbed check still refused, so nothing spawned")
            if kind != "unpopulated":
                check_ok(hit == ["filter-clean"], "the submodule's filter did not run under the stubbed check")
        else:
            check_ok(f"{key} in {where}" in refused, f"the step was not refused naming {key} in {where}")
            check_ok(not done.exists() and not hit, f"the refused step spawned, or its {key} ran")
        if kind == "name-differs":
            run_fx_git(target, "config", "-f", ".gitmodules", "--unset", "submodule.nm.path")
            try:
                run_step_isolated(status, "up", stepped, gov)
                refused = ""
            except Refusal as e:
                refused = str(e)
                print(f"isolation: {status.id} · the .gitmodules mapping removed · refused · {e}")
            check_ok(f"{key} in .git/modules/nm/config (submodule nm, by name)" in refused,
                   "with no .gitmodules mapping the refusal does not name the submodule `nm, by name`")
        if kind == "nested-name-differs":
            run_fx_git(target, "submodule", "deinit", "-q", "-f", "lib/p")
            # ponytail: the deinit removes `lib/p/q`, the inner's core.worktree, and git then reads no
            # config of it at all (a refusal naming it); the empty directory keeps the label graded.
            (target / FIXTURE_SUB_HOME / "p" / "q").mkdir(parents=True, exist_ok=True)
            try:
                run_step_isolated(status, "up", stepped, gov)
                refused = ""
            except Refusal as e:
                refused = str(e)
                print(f"isolation: {status.id} · the outer submodule unpopulated · refused · {e}")
            check_ok(f"{key} in .git/modules/nm/modules/in/config (submodule lib/p/in, by name)" in refused,
                   "with the outer submodule unpopulated the refusal does not name the inner `in, by name`")
        rc = 0 if kind == "main-only" or sound else 1
    for f in fails:
        print(f"isolation: FAILED · {f}")
    return 1 if fails else rc


# THE WALK'S FIXTURES (TOOL-dSafePassage-2 S9). Their step program, `fx.py`, writes `<slug>.txt` into
# the target through the before-image helper; its witness tests that file. It keeps its canaries
# in `<target>.fx`, a sibling of the target, one file per step and verb with a line per spawn, and
# reads its plants there: `<slug>.fail` exits 1 before any write, `<slug>.block` writes the image,
# then the pid and `<slug>.blocking`, and waits to be killed; `<slug>.block-after` does the same
# after its first file (TOOL-dSafePassage-4). Its down writes `<slug>.down-saw`, each target file's
# path and sha256 as the down found them (`<slug>.down-block` blocking first, TOOL-dSafePassage-39),
# then restores from the image, `<slug>.down-block-after` blocking once it has (TOOL-dSafePassage-76),
# `<slug>.down-fails` exiting
# 1 first and `<slug>.down-keeps` exiting 0 with nothing restored; `<slug>.down-lowers` then sets the
# receipt to schema 3 and takes `steps` out, as the schema step's down does (TOOL-dSafePassage-18).
# `<slug>.witness-absent` makes its witness "the file is absent", and `<slug>.witness-always` one
# that exits 0 whatever the target holds, as a witness reading node state does (TOOL-dSafePassage-17);
# `<slug>.witness-block` blocks a witness that holds, so a walk dies after the up returned and before
# move 5 records it (TOOL-dSafePassage-40).
FIXTURE_WALK_STEP = r'''import importlib.util, os, pathlib, sys, time
verb, target, slug = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
reports = target.with_name(target.name + ".fx")
reports.mkdir(exist_ok=True)
with open(reports / f"{slug}.{verb}", "a", encoding="utf-8") as f:
    f.write(f"{os.getpid()}\n")
def block():
    (reports / f"{slug}.pid").write_text(str(os.getpid()), encoding="utf-8")
    (reports / f"{slug}.blocking").touch()
    for _ in range(600):
        time.sleep(0.5)
if verb == "witness":
    held = (target / f"{slug}.txt").is_file() != (reports / f"{slug}.witness-absent").exists()
    if held and (reports / f"{slug}.witness-block").exists():
        block()
    sys.exit(0 if held or (reports / f"{slug}.witness-always").exists() else 1)
spec = importlib.util.spec_from_file_location("upgrade_steps", pathlib.Path(__file__).resolve().parents[1] / "upgrade_steps.py")
steps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(steps)
if verb == "down":
    import hashlib
    if (reports / f"{slug}.down-block").exists():
        block()
    (reports / f"{slug}.down-saw").write_text("".join(
        f"{p.relative_to(target).as_posix()} {hashlib.sha256(p.read_bytes()).hexdigest()}\n"
        for p in sorted(target.rglob("*")) if p.is_file() and ".git" not in p.relative_to(target).parts),
        encoding="utf-8")
    if (reports / f"{slug}.down-fails").exists():
        sys.stderr.write(f"fx: {slug} down fails by its plant\n")
        sys.exit(1)
    if not (reports / f"{slug}.down-keeps").exists():
        steps.write_from_before_image(target, f"fx/{slug}")
        if (reports / f"{slug}.down-block-after").exists():
            block()
    if (reports / f"{slug}.down-lowers").exists():
        import json
        rp = target / ".governance" / "install.json"
        rec = json.loads(rp.read_text(encoding="utf-8"))
        rec.pop("steps", None)
        rec["schema"] = 3
        rp.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
    sys.exit(0)
if (reports / f"{slug}.fail").exists():
    sys.stderr.write(f"fx: {slug} {verb} fails by its plant\n")
    sys.exit(1)
after = steps.write_before_image(target, f"fx/{slug}", lambda before: {f"{slug}.txt": f"{slug}\n".encode()})
if (reports / f"{slug}.block").exists():
    block()
for p, data in after.items():
    (target / p).write_bytes(data)
    if (reports / f"{slug}.block-after").exists():
        block()
'''
# One walk, as `update` runs it, in a child process the `kill-*` plants can kill.
FIXTURE_WALK_CHILD = r'''import importlib.util, json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
spec = importlib.util.spec_from_file_location("upgrade_steps", sys.argv[1])
us = importlib.util.module_from_spec(spec)
sys.modules["upgrade_steps"] = us
spec.loader.exec_module(us)
gov, target, to = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4]
rp = target / ".governance" / "install.json"
receipt = json.loads(rp.read_text(encoding="utf-8"))
out = us.run_step_walk(gov, target, rp, receipt, us.derive_pending_steps(gov, receipt, to))
print(f"walk: {out['pending']} pending · {out['applied']} applied · {out['skipped']} skipped · stopped at {out['stopped'] or 'none'}")
sys.exit(1 if out["stopped"] else 0)
'''
# One reverse walk toward `to`, as `update --rollback` runs it (TOOL-dSafePassage-4), a refusal
# printed `rollback: refused · Refusal: <reason>` and exiting 1 (TOOL-dSafePassage-76). A fifth
# argument, a step id, is recorded `rolled-back` after the rows are derived and before the walk
# reads the receipt (TOOL-dSafePassage-49 S5), as a concurrent down would leave it.
FIXTURE_REVERSE_CHILD = r'''import importlib.util, json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
spec = importlib.util.spec_from_file_location("upgrade_steps", sys.argv[1])
us = importlib.util.module_from_spec(spec)
sys.modules["upgrade_steps"] = us
spec.loader.exec_module(us)
gov, target, to = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4]
rp = target / ".governance" / "install.json"
receipt = json.loads(rp.read_text(encoding="utf-8"))
rows = us.derive_reverse_steps(gov, receipt, to)
if len(sys.argv) > 5:
    us.set_step_state(receipt, sys.argv[5], None, "rolled-back")
    rp.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"rollback: rows derived {[r.id for r in rows]} · then {sys.argv[5]} recorded "
          f"{next(r['state'] for r in us.read_step_states(receipt) if r['id'] == sys.argv[5])}")
try:
    out = us.run_reverse_walk(gov, target, rp, receipt, rows, to)
except us.Refusal as e:
    print(f"rollback: refused · Refusal: {e}")
    sys.exit(1)
print(f"rollback: {len(out['downs'])} reached · stopped at {out['stopped'] or 'none'}")
print(f"rollback: verdicts {out['downs']}")
sys.exit(1 if out["stopped"] else 0)
'''
# One take of a target's write lock through govkit's `take_write_lock`, held until `<release>`
# exists; `<gate>` makes two racers start together. `-` waits for neither. A sixth argument, seconds,
# delays every return of the census `check_holder_dead` loads, in this process only, so the census
# answers that much after it sampled (TOOL-dSafePassage-22 S4). `wall-step <pid> <born>` instead
# makes the census one `posix-ps` row of <pid>, its age counted on `time.monotonic` from <born>,
# stands `time.monotonic` in for the boot clock and steps `time.time` 10 s forward, in this process
# only (TOOL-dSafePassage-32 S6). `pidns <value>` stands <value> in for this process's
# `read_pid_namespace`, in this process only (TOOL-dSafePassage-31 S4). `bootid <value>` stands
# <value> in for `read_boot_id` the same way (TOOL-dSafePassage-35 S26).
FIXTURE_LOCK_CHILD = r'''import importlib.machinery, importlib.util, os, pathlib, sys, time
sys.stdout.reconfigure(encoding="utf-8")
wall_step = len(sys.argv) > 5 and sys.argv[5] == "wall-step"
pidns = sys.argv[6] if len(sys.argv) > 5 and sys.argv[5] == "pidns" else None
bootid = sys.argv[6] if len(sys.argv) > 5 and sys.argv[5] == "bootid" else None
if len(sys.argv) > 5 and pidns is None and bootid is None:
    _exec = importlib.machinery.SourceFileLoader.exec_module
    def _slow_exec(self, module):
        _exec(self, module)
        if module.__name__ == "gk_lock_census" and wall_step:
            row = {"winpid": int(sys.argv[6]), "backend": "posix-ps"}
            module.scan_processes = lambda *a, **k: (
                [{**row, "age_s": float(int(time.monotonic() - float(sys.argv[7])))}], {})
        elif module.__name__ == "gk_lock_census":
            scan = module.scan_processes
            def slow_scan(*a, **k):
                out = scan(*a, **k)
                time.sleep(float(sys.argv[5]))
                return out
            module.scan_processes = slow_scan
    importlib.machinery.SourceFileLoader.exec_module = _slow_exec
spec = importlib.util.spec_from_file_location("upgrade_steps", sys.argv[1])
us = importlib.util.module_from_spec(spec)
sys.modules["upgrade_steps"] = us
spec.loader.exec_module(us)
gk = us.load_govkit()
if pidns is not None:
    us.read_pid_namespace = lambda: pidns
if bootid is not None:
    us.read_boot_id = lambda: bootid
if wall_step:
    us.read_boot_clock = time.monotonic
    _wall = time.time
    time.time = lambda: _wall() + 10
print(f"lock: taker pid {os.getpid()}", flush=True)
deadline = time.time() + 300
while sys.argv[3] != "-" and not pathlib.Path(sys.argv[3]).exists() and time.time() < deadline:
    time.sleep(0.01)
try:
    gk.take_write_lock(pathlib.Path(sys.argv[2]), "update")
except us.Refusal as e:
    print(f"lock: refused · {e}", flush=True)
    sys.exit(1)
print("lock: taken", flush=True)
while sys.argv[4] != "-" and not pathlib.Path(sys.argv[4]).exists() and time.time() < deadline:
    time.sleep(0.05)
'''
WALK_SCHEMA_PLANTS = ("schema-3", "schema-3-fail", "schema-3-kill")  # TOOL-dSafePassage-15
WALK_PLANTS = ("witness-holds", "fail-k", "kill-step", "resume", "attended", "not-pending",
               "truncated-image", "truncated-image-held", "kill-after-up", "kill-before-stage") + WALK_SCHEMA_PLANTS
LOCK_PLANTS = ("lock-dead", "lock-live", "lock-reused", "lock-foreign-host", "lock-foreign-namespace", "lock-unreadable",
               "lock-foreign-pidns", "lock-no-pidns", "lock-race", "guard-dead", "lock-live-slow-census", "lock-wall-step", "lock-wall-step-no-boot",
               "lock-other-boot", "lock-no-namespace")
UPDATE_PLANTS = ("read-only", "scoped", "scoped-read-only", "update-fail", "kill-walk", "kill-walk-edit",
                 "schema-3-update", "needs-target-source")
ROLLBACK_SCHEMA_PLANTS = ("schema-step", "schema-step-kill", "schema-step-early")  # TOOL-dSafePassage-18
NODE_WITNESS_PLANTS = ("node-witness", "node-witness-refuses")  # TOOL-dSafePassage-17: s2 is the floor row's shape
DOWN_KILLED_PLANTS = ("witness-only-down-killed", "unrecorded-witness-down-killed")  # TOOL-dSafePassage-39
ROLLBACK_PLANTS = ("after-kill", "after-fail", "down-fails", "witness-stays", "unrecorded", "partial-to",
                   "callers", "witness-only", "image-lost", "kill-after-up-image-lost",
                   "rolled-back-witness-holds", "witness-only-reup", "kill-after-down-stage",
                   "kill-after-down-stage-garbled") + NODE_WITNESS_PLANTS + ROLLBACK_SCHEMA_PLANTS + DOWN_KILLED_PLANTS
ROLLBACK_UPDATE_SCHEMA_PLANTS = ("schema-step", "schema-step-kill-before-stamp",  # TOOL-dSafePassage-19
                                 "schema-step-kill-shipped-rows")  # TOOL-dSafePassage-70
ROLLBACK_UPDATE_PLANTS = (("refused", "read-only", "descendant", "scoped", "no-base") + ROLLBACK_UPDATE_SCHEMA_PLANTS
                          + ("schema-up-kill", "retired-step"))  # TOOL-dSafePassage-62, -76


def build_fixture_env(**extra: str) -> dict[str, str]:
    """`build_tree_git_env` with a fixed commit identity: no `GIT_*` name of the caller's, no global
    or system config, so every fixture repository is the same on every node."""
    return {**build_tree_git_env(), "GIT_AUTHOR_NAME": "fx", "GIT_AUTHOR_EMAIL": "fx@e",
            "GIT_COMMITTER_NAME": "fx", "GIT_COMMITTER_EMAIL": "fx@e", **extra}


def load_fixture_target():
    """`fixture_target.py` beside this file, the scratch repositories' one factory
    (TOOL-dSafePassage-26 S19). Loaded only by a fixture: a scratch gov holding a copy of this
    module and not the factory still imports."""
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    import fixture_target
    return fixture_target


def run_fixture_git(cwd, *args: str, date: int | None = None) -> str:
    """`git -C <cwd> <args>` under `build_fixture_env`, its stdout; `date` pins both commit dates."""
    env = build_fixture_env(**({"GIT_AUTHOR_DATE": f"{date} +0000", "GIT_COMMITTER_DATE": f"{date} +0000"}
                               if date else {}))
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env=env).stdout.strip()


def render_fixture_row(slug: str, resume: bool = False, needs: bool = False, reverted: str | None = None) -> str:
    """One `[[upgrade]]` row of the fixture step `fx/<slug>`, its argvs calling `fx.py`, declaring
    `reverted` where given (TOOL-dSafePassage-17)."""
    def render_argv(verb: str) -> str:
        return json.dumps(["python", "{gov}/govkit/steps/fx.py", verb, "{target}", slug])
    return (f'[[upgrade]]\nid = "fx/{slug}"\nup = {render_argv("up")}\ndown = {render_argv("down")}\n'
            f'witness = {render_argv("witness")}\n' + (f'resume = {render_argv("resume")}\n' if resume else "")
            + (f'reverted = {json.dumps(reverted)}\n' if reverted else "")
            + f'surfaces = []\nneeds-target = {"true" if needs else "false"}\n\n')


# The schema step's plants (TOOL-dSafePassage-15), each an (anchor, replacement) over a copy of
# `steps/receipt_schema_4.py`, read in `<target>.fx` as `fx.py` reads its own: `schema.fail` exits
# the up 1 before any write, `schema.block` blocks after the temporary file is written and before
# its rename, writing the pid and `schema.blocking`, until the fixture kills it; `schema.block-after`
# does the same once the rename has landed (TOOL-dSafePassage-19).
FIXTURE_SCHEMA_STEP_PLANTS = (
    ("    code, msg, out = verbs[argv[0]](receipt)\n",
     "    fx = path.parents[1].with_name(path.parents[1].name + \".fx\")\n"
     "    if argv[0] == \"up\" and (fx / \"schema.fail\").exists():\n"
     "        sys.stderr.write(\"fx: schema up fails by its plant\\n\")\n"
     "        return 1\n"
     "    code, msg, out = verbs[argv[0]](receipt)\n"),
    # The step writes through `write_atomic` (TOOL-dSafePassage-26 S46), so the block wraps the
    # rename that helper makes, in this step process only.
    ("        write_atomic(path, json.dumps(out, indent=2) + \"\\n\")\n",
     "        _os, _real = __import__(\"os\"), __import__(\"os\").replace\n"
     "\n"
     "        def _planted(a, b):\n"
     "            for name, after in ((\"schema.block\", False), (\"schema.block-after\", True)):\n"
     "                if after:\n"
     "                    _real(a, b)\n"
     "                if (fx / name).exists():\n"
     "                    (fx / \"schema.pid\").write_text(str(_os.getpid()), encoding=\"utf-8\")\n"
     "                    (fx / \"schema.blocking\").touch()\n"
     "                    __import__(\"time\").sleep(300)\n"
     "        _os.replace = _planted\n"
     "        write_atomic(path, json.dumps(out, indent=2) + \"\\n\")\n"),
)


def write_fixture_schema_step(gkd: pathlib.Path) -> str:
    """Copy `steps/receipt_schema_4.py` into the scratch gov's kit directory `gkd` with
    FIXTURE_SCHEMA_STEP_PLANTS applied, and return its `steps.toml` row as this checkout spells it
    (TOOL-dSafePassage-15 S5). An anchor or row this checkout no longer holds is a refusal."""
    text = (HERE / "steps" / "receipt_schema_4.py").read_text(encoding="utf-8")
    for anchor, planted in FIXTURE_SCHEMA_STEP_PLANTS:
        if anchor not in text:
            raise Refusal(f"steps/receipt_schema_4.py no longer holds the fixture's anchor {anchor.strip()!r}")
        text = text.replace(anchor, planted)
    (gkd / "steps").mkdir(parents=True, exist_ok=True)
    (gkd / "steps" / "receipt_schema_4.py").write_text(text, encoding="utf-8", newline="\n")
    m = re.search(r'\[\[upgrade\]\]\nid = "govkit/receipt-schema-4"\n(?:[a-z-]+ = .*\n)*',
                  (HERE / STEPS_FILE).read_text(encoding="utf-8"))
    if not m:
        raise Refusal(f"{STEPS_FILE} holds no govkit/receipt-schema-4 row for the fixture to copy")
    return m[0] + "\n"


def build_walk_gov(tmp: pathlib.Path, plant: str | None) -> tuple[pathlib.Path, dict[str, str]]:
    """The `walk` family's scratch gov: A, a side branch from A introducing `s3`, B introducing `s1`
    and `s2`, the side branch merged at M, C introducing `s4`, and for `not-pending` D introducing
    `s5`. The side commit is dated before B, so only the first-parent order puts `s3` at M. For a
    schema plant, B introduces the copied `govkit/receipt-schema-4` row first (TOOL-dSafePassage-15, -18)."""
    gov = tmp / "gov"
    gkd = gov / FIXTURE_PREFIX / HERE.name
    (gkd / "steps").mkdir(parents=True)
    load_fixture_target().build_scratch_gov(gov)
    (gkd / REGISTRY_FILE).write_text("", encoding="utf-8")
    shutil.copy2(HERE / "upgrade_steps.py", gkd / "upgrade_steps.py")
    (gkd / "steps" / "fx.py").write_text(FIXTURE_WALK_STEP, encoding="utf-8", newline="\n")
    steps = gkd / STEPS_FILE
    row = {s: render_fixture_row(s, resume=(plant == "resume" and s == "s3"),
                                 needs=(plant == "attended" and s == "s2"),
                                 reverted=DOWN_EXIT if plant in NODE_WITNESS_PLANTS and s == "s2" else None)
           for s in ("s1", "s2", "s3", "s4", "s5")}
    first = ("schema",) if plant in WALK_SCHEMA_PLANTS + ROLLBACK_SCHEMA_PLANTS else ()
    if first:
        row["schema"] = write_fixture_schema_step(gkd)
    sha: dict[str, str] = {}

    def write_commit(name: str, date: int, *rows: str) -> None:
        if rows:
            steps.write_text("".join(row[s] for s in rows), encoding="utf-8", newline="\n")
        run_fixture_git(gov, "add", "-A")
        run_fixture_git(gov, "commit", "-qm", name, date=date)
        sha[name] = run_fixture_git(gov, "rev-parse", "HEAD")

    write_commit("A", 1_700_000_000)
    run_fixture_git(gov, "checkout", "-q", "-b", "side")
    write_commit("S", 1_700_000_010, "s3")
    run_fixture_git(gov, "checkout", "-q", "main")
    write_commit("B", 1_700_000_020, *first, "s1", "s2")
    run_fixture_git(gov, "merge", "-q", "--no-ff", "--no-commit", "side")
    write_commit("M", 1_700_000_030, *first, "s1", "s2", "s3")
    write_commit("C", 1_700_000_040, *first, "s1", "s2", "s3", "s4")
    if plant == "not-pending":
        write_commit("D", 1_700_000_050, "s1", "s2", "s3", "s4", "s5")
    return gov, sha


def build_walk_target(tmp: pathlib.Path, sha_a: str, name: str, steps: list | None = None,
                      files: dict | None = None, schema3: bool = False) -> pathlib.Path:
    """A scratch target repository `tmp/<name>` holding `files` and a schema-4 receipt at `sha_a`
    with `steps`, committed: what the `walk` and `rollback` families walk over. `schema3` forces the
    receipt to schema 3 with `steps` taken out (TOOL-dSafePassage-15)."""
    receipt = {"schema": 4, "gov_commit": sha_a, "kits": [], "files": [], "steps": steps or []}
    if schema3:
        receipt["schema"] = 3
        del receipt["steps"]
    return load_fixture_target().build_target(
        tmp, None, name, {**(files or {}), ".governance/install.json": json.dumps(receipt, indent=2) + "\n"})


def run_fixture_child(child: str, gov: pathlib.Path, t: pathlib.Path, to: str, env: dict,
                      *extra: str) -> tuple[int, str]:
    """Run the fixture program `child` (`FIXTURE_WALK_CHILD` or `FIXTURE_REVERSE_CHILD`) over `t`
    toward `to`, `extra` after its argv, echo its output and return (exit, output)."""
    p = subprocess.run([sys.executable, "-c", child, str(HERE / "upgrade_steps.py"), str(gov), str(t), to, *extra],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=600)
    print(p.stdout + p.stderr, end="")
    return p.returncode, p.stdout + p.stderr


def read_target_bytes(t: pathlib.Path) -> dict[str, bytes]:
    """Every file under `t` but `.git`, by its relative path, and the index as `:index`: the bytes
    two runs are compared on."""
    out = {p.relative_to(t).as_posix(): p.read_bytes() for p in sorted(t.rglob("*"))
           if p.is_file() and ".git" not in p.relative_to(t).parts}
    out[":index"] = run_fixture_git(t, "ls-files", "-s").encode("utf-8")
    return out


def run_killed(argv: list[str], reports: pathlib.Path, slug: str, env: dict) -> str | None:
    """Run `argv` until step `slug` blocks, then kill that process and the step's: None, or what
    went wrong. The kill is TerminateProcess on Windows and SIGKILL elsewhere, so no `finally` runs."""
    p = subprocess.Popen(argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=env)
    marker, deadline = reports / f"{slug}.blocking", time.time() + 300
    while not marker.exists() and p.poll() is None and time.time() < deadline:
        time.sleep(0.05)
    if not marker.exists():
        p.kill()
        p.wait()
        return f"{slug} never blocked (the run exited {p.returncode})"
    step_pid = int((reports / f"{slug}.pid").read_text(encoding="utf-8"))
    p.kill()
    p.wait()
    os.kill(step_pid, getattr(signal, "SIGKILL", signal.SIGTERM))
    time.sleep(1)  # ponytail: the killed step's handles close asynchronously on Windows
    return None


def read_receipt_steps(t: pathlib.Path) -> list[dict]:
    """The `steps` rows of the receipt at `t`."""
    return json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8")).get("steps") or []


def run_walk_fixture(plant: str | None) -> int:
    """`fixture walk [--plant <case>]` (S9): AC1 to AC5 over a scratch gov and target under the temp
    root. An unmet expectation prints `walk: FAILED`; otherwise the exit is the walk's own,
    `fail-k`'s and `attended`'s 1 by design."""
    with tempfile.TemporaryDirectory(prefix="gk-walk-", ignore_cleanup_errors=True) as td:
        tmp = pathlib.Path(td)
        gov, sha = build_walk_gov(tmp, plant)
        env = build_fixture_env()
        fails: list[str] = []

        def check_ok(ok: bool, what: str) -> None:
            if not ok:
                fails.append(what)

        def build_case_target(name: str, steps: list | None = None, files: dict | None = None) -> pathlib.Path:
            return build_walk_target(tmp, sha["A"], name, steps, files, schema3=plant in WALK_SCHEMA_PLANTS)

        def scan(t: pathlib.Path) -> tuple[int, str]:
            return run_fixture_child(FIXTURE_WALK_CHILD, gov, t, sha["C"], env)

        def extract_step_lines(out: str) -> list[str]:
            return [ln for ln in out.splitlines() if ln.startswith(("step fx/", "step govkit/receipt-schema-4 "))]

        def read_canaries(t: pathlib.Path) -> list[str]:
            r = t.with_name(t.name + ".fx")
            return sorted(p.name for p in r.iterdir()) if r.is_dir() else []

        def run_killed_walk(t: pathlib.Path) -> None:
            argv = [sys.executable, "-c", FIXTURE_WALK_CHILD, str(HERE / "upgrade_steps.py"), str(gov), str(t), sha["C"]]
            why = run_killed(argv, t.with_name(t.name + ".fx"), "s3", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            rows = read_receipt_steps(t)
            last = [r["id"] for r in rows if r["state"] == "applied"][-1:]
            s3 = next((r for r in rows if r["id"] == "fx/s3"), {})
            print(f"walk: after the kill · last applied {last} · fx/s3 {s3.get('state')} · {s3.get('failure')}")
            check_ok(last == ["fx/s2"], "the receipt does not read s2 as the last applied row after the kill")
            check_ok(s3.get("state") == "failed" and str(s3.get("failure", "")).startswith("interrupted: started "),
                   "the kill left no interrupted failure for s3: the pre-spawn row was not persisted")

        t = tmp / "t"
        rc = 0
        if plant in (None, "not-pending"):
            pre = [{"id": "fx/s2", "introduced": sha["B"], "state": "applied"}] if plant else []
            t = build_case_target("t", pre)
            rc, out = scan(t)
            want = ["fx/s1", "fx/s3", "fx/s4"] if plant else ["fx/s1", "fx/s2", "fx/s3", "fx/s4"]
            check_ok(extract_step_lines(out) == [f"step {s} · applied" for s in want],
                   f"the step lines are not {want} in that order, each applied")
            check_ok([(r["id"], r["state"]) for r in read_receipt_steps(t)] == [(s, "applied") for s in
                   (["fx/s2"] if plant else []) + want], "the receipt's steps do not list the walk so")
            intro = {r["id"]: r["introduced"] for r in read_receipt_steps(t)}
            check_ok(intro.get("fx/s3") == sha["M"], "s3's introducing commit is not the merge M")
            print(f"walk: fx/s3 introduced at {'M' if intro.get('fx/s3') == sha['M'] else intro.get('fx/s3')}")
            if plant:
                spawned = [c for c in read_canaries(t) if c.startswith(("s2.", "s5."))]
                print(f"walk: canaries of s2 and s5: {spawned or 'none'}")
                check_ok(not spawned, "a step outside the pending set spawned")
            check_ok(rc == 0, f"the walk exited {rc}")
        elif plant == "witness-holds":
            t = build_case_target("t", files={"s2.txt": "s2\n"})
            rc, out = scan(t)
            row = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s2"), {})
            print(f"walk: fx/s2 up canary {'present' if 's2.up' in read_canaries(t) else 'absent'} · row {row.get('state')}"
                  f" · via {row.get('via')}")
            check_ok("step fx/s2 · skipped (witness holds)" in extract_step_lines(out), "s2 is not skipped by its witness")
            check_ok("s2.up" not in read_canaries(t), "s2's up ran over a holding witness")
            check_ok(row.get("state") == "applied" and rc == 0, "s2 does not read applied, or the walk failed")
            check_ok(row.get("via") == "witness", "s2 is not marked applied via its witness (TOOL-dSafePassage-33)")
        elif plant == "truncated-image-held":
            # TOOL-dSafePassage-87 S6: s2's witness holds and its before-image, never committed, is cut
            # short. The walk refuses naming the image and a remedy that applies with no committed
            # copy; the remedy taken, the re-run passes s2 by its witness.
            t = build_case_target("t", files={"s2.txt": "s2\n"})
            image = t / derive_image_path(pathlib.Path("."), "fx/s2")
            full = json.dumps({"step": "fx/s2", "paths": {"s2.txt": {"after": None, "before": None}}}, indent=2)
            image.parent.mkdir(parents=True)
            image.write_text(full[:full.index('"step"')], encoding="utf-8", newline="\n")
            rc, out = scan(t)
            named = "where none is committed, remove it" in out
            print(f"walk: held · rc {rc} · remedy {'named' if named else 'absent'}")
            check_ok(rc == 1 and "s2.before.json does not parse" in out and named,
                     "an unparsable image under a holding witness did not stop the walk naming it and its remedy")
            image.unlink()
            rc, out = scan(t)
            s2 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s2"), {})
            print(f"walk: held · after the remedy · fx/s2 {s2.get('state')} · rc {rc}")
            check_ok(rc == 0 and "step fx/s2 · skipped (witness holds)" in extract_step_lines(out),
                     "the re-run after the remedy did not pass s2 by its witness")
        elif plant == "fail-k":
            t = build_case_target("t")
            t.with_name("t.fx").mkdir()
            (t.with_name("t.fx") / "s3.fail").touch()
            rc, out = scan(t)
            got = {r["id"]: r for r in read_receipt_steps(t)}
            s3 = got.get("fx/s3", {})
            print(f"walk: fx/s3 {s3.get('state')} · {s3.get('failure')} · canaries {read_canaries(t)}")
            check_ok(got.get("fx/s1", {}).get("state") == "applied" and got.get("fx/s2", {}).get("state") == "applied",
                   "s1 and s2 do not stay applied")
            check_ok(s3.get("state") == "failed" and s3.get("failure") == "exit 1: fx: s3 up fails by its plant",
                   "s3's failure does not name exit 1 and its stderr line")
            marked = sorted(sid for sid, r in got.items() if "via" in r)
            print(f"walk: rows whose up ran carrying via: {marked or 'none'}")
            check_ok(not marked, "a row applied by its up carries the witness mark (TOOL-dSafePassage-33)")
            check_ok("s4.up" not in read_canaries(t) and not [c for c in read_canaries(t) if c.endswith(".down")],
                   "the walk went on past the failure, or a down ran")
            check_ok(rc == 1, f"the walk exited {rc}, not 1")
        elif plant in ("kill-step", "resume"):
            t, t2 = build_case_target("t"), build_case_target("t2")
            t.with_name("t.fx").mkdir()
            (t.with_name("t.fx") / "s3.block").touch()
            run_killed_walk(t)
            (t.with_name("t.fx") / "s3.block").unlink()
            rc, out = scan(t)
            rc2, _out2 = scan(t2)
            same = read_target_bytes(t) == read_target_bytes(t2)
            print(f"walk: the re-run's target and receipt {'equal' if same else 'DIFFER from'} an uninterrupted walk's")
            check_ok(same, "the re-run did not converge to an uninterrupted walk's bytes")
            check_ok("step fx/s3 · applied" + (" · by its resume" if plant == "resume" else "") in extract_step_lines(out),
                   "the re-run did not apply s3")
            ups = (t.with_name("t.fx") / "s3.up").read_text(encoding="utf-8").split()
            resumed = (t.with_name("t.fx") / "s3.resume").is_file()
            print(f"walk: fx/s3 up spawned {len(ups)} time(s) · resume {'spawned' if resumed else 'not spawned'}")
            if plant == "resume":
                check_ok(resumed and len(ups) == 1, "the re-run spawned s3's up, not its declared resume")
            else:
                check_ok(len(ups) == 2 and not resumed, "the re-run did not spawn s3's up again")
            check_ok(rc == 0 and rc2 == 0, f"the re-run exited {rc}, the uninterrupted walk {rc2}")
        elif plant == "kill-after-up":
            # TOOL-dSafePassage-40 AC1: killed in move 5's witness, after s3's up wrote its image and
            # file; the re-run passes s3 by its witness and must not mark it. AC3: each evidence alone.
            t = build_case_target("t")
            fx = t.with_name("t.fx")
            fx.mkdir()
            (fx / "s3.witness-block").touch()
            run_killed_walk(t)
            (fx / "s3.witness-block").unlink()
            wrote = (t / "s3.txt").is_file() and derive_image_path(t, "fx/s3").is_file()
            print(f"walk: after the kill · s3.txt and its image {'present' if wrote else 'NOT both present'}")
            check_ok(wrote, "the kill did not land after s3's up wrote its file and image")
            rc, out = scan(t)
            s3 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s3"), {})
            print(f"walk: the re-run · fx/s3 {s3.get('state')} · via {s3.get('via')}")
            check_ok("step fx/s3 · skipped (witness holds)" in extract_step_lines(out), "the re-run did not pass s3 by its witness")
            check_ok(s3.get("state") == "applied" and "via" not in s3 and rc == 0,
                   "s3, whose up ran before the kill, is marked applied via its witness")
            image2 = derive_image_path(pathlib.Path("."), "fx/s2").as_posix()
            # TOOL-dSafePassage-76 S2: move 1 now reads an image it finds, so the planted one is whole.
            whole2 = json.dumps({"step": "fx/s2", "paths": {"s2.txt": {
                "after": hashlib.sha256(b"s2\n").hexdigest(), "before": None}}}, indent=2, sort_keys=True) + "\n"
            for name, what, pre, files in (
                    ("t2", "failed record, no image",
                     [{"id": "fx/s2", "introduced": sha["B"], "state": "failed", "failure": "exit 1: fx"}], {}),
                    ("t3", "no record, image present", None, {image2: whole2})):
                tt = build_case_target(name, pre, {"s2.txt": "s2\n", **files})
                rc_t, _out = scan(tt)
                s2 = next((r for r in read_receipt_steps(tt) if r["id"] == "fx/s2"), {})
                print(f"walk: {what} · fx/s2 {s2.get('state')} · via {s2.get('via')}")
                check_ok(s2.get("state") == "applied" and "via" not in s2 and rc_t == 0,
                       f"s2 ({what}) is marked applied via its witness")
        elif plant == "kill-before-stage":
            # TOOL-dSafePassage-76 AC2: killed in s1's second witness, after its up wrote and before
            # move 5 staged; the re-run passes s1 by its witness and must stage what the up wrote.
            t = build_case_target("t")
            fx = t.with_name("t.fx")
            fx.mkdir()
            (fx / "s1.witness-block").touch()
            argv = [sys.executable, "-c", FIXTURE_WALK_CHILD, str(HERE / "upgrade_steps.py"), str(gov), str(t), sha["C"]]
            why = run_killed(argv, fx, "s1", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (fx / "s1.witness-block").unlink()
            image = derive_image_path(pathlib.Path("."), "fx/s1").as_posix()
            staged = run_fixture_git(t, "diff", "--cached", "--name-only").splitlines()
            print(f"walk: after the kill · staged {staged or 'nothing'} · s1.txt and its image "
                  f"{'present' if (t / 's1.txt').is_file() and (t / image).is_file() else 'NOT both present'}")
            check_ok(not staged and (t / "s1.txt").is_file() and (t / image).is_file(),
                   "the kill did not land after s1's up wrote, before anything was staged")
            rc, out = scan(t)
            staged = run_fixture_git(t, "diff", "--cached", "--name-only").splitlines()
            s1 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s1"), {})
            print(f"walk: the re-run · git diff --cached --name-only lists s1.txt "
                  f"{'yes' if 's1.txt' in staged else 'NO'} · {image} {'yes' if image in staged else 'NO'} · "
                  f"fx/s1 {s1.get('state')}")
            check_ok("s1.txt" in staged and image in staged, "the re-run did not stage s1's write and its before-image")
            check_ok(s1.get("state") == "applied" and rc == 0, f"fx/s1 does not read applied, or the re-run exited {rc}")
        elif plant == "attended":
            t = build_case_target("t")
            rc, out = scan(t)
            s2 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s2"), {})
            orders = sorted((t / ".governance" / "outbox").glob("update-attended-step-*.md"))
            text = orders[0].read_text(encoding="utf-8") if orders else ""
            print(f"walk: fx/s2 {s2.get('state')} · {s2.get('failure')} · order "
                  f"{orders[0].name if orders else 'absent'} · up canary {'present' if 's2.up' in read_canaries(t) else 'absent'}")
            check_ok(s2.get("failure") == ATTENDED_STOP, "s2 is not failed attended")
            check_ok("fx/s2" in text and "fx.py up" in text.replace("'", ""), "the order does not name s2 and its up argv")
            check_ok("s2.up" not in read_canaries(t) and rc == 1, "the attended step spawned, or the walk did not exit 1")
            # The person's turn: s2's up by hand, outside the walk.
            subprocess.run([sys.executable, str(gov / FIXTURE_PREFIX / HERE.name / "steps" / "fx.py"), "up", str(t), "s2"],
                           capture_output=True, env=env, timeout=600)
            rc2, out2 = scan(t)
            check_ok(extract_step_lines(out2) == ["step fx/s2 · skipped (witness holds)", "step fx/s3 · applied",
                                      "step fx/s4 · applied"] and rc2 == 0,
                   "the re-run does not pass s2 by its witness and apply s3 and s4")
        elif plant == "truncated-image":
            # TOOL-dSafePassage-26 S31: s3's before-image cut short, as a writer before the atomic
            # one could leave it. In `t` no path it lists changed since, so it reads absent and is
            # rewritten; in `t2` a path it lists, `kept.txt`, was written after it, so the up refuses.
            image = derive_image_path(pathlib.Path("."), "fx/s3")
            s3row = {"after": hashlib.sha256(b"s3\n").hexdigest(), "before": None}
            kept = {"after": None, "before": base64.b64encode(b"kept\n").decode("ascii")}
            t, t2 = build_case_target("t"), build_case_target("t2")
            for tt, paths in ((t, {"s3.txt": s3row}), (t2, {"kept.txt": kept, "s3.txt": s3row})):
                full = json.dumps({"step": "fx/s3", "paths": paths}, indent=2, sort_keys=True)
                (tt / image).parent.mkdir(parents=True)
                (tt / image).write_text(full[:full.index('"step"')], encoding="utf-8", newline="\n")
            (t2 / "kept.txt").write_text("edited\n", encoding="utf-8", newline="\n")
            at = (t2 / image).stat().st_mtime + 10
            os.utime(t2 / "kept.txt", (at, at))
            rc, out = scan(t)
            try:
                rewritten = json.loads((t / image).read_text(encoding="utf-8"))["paths"]
            except (OSError, ValueError, KeyError):
                rewritten = None
            s3 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s3"), {})
            print(f"walk: unchanged · fx/s3 {s3.get('state')} · image "
                  f"{'rewritten' if rewritten is not None else 'still unparsed'}")
            check_ok(rc == 0 and s3.get("state") == "applied" and rewritten is not None,
                   "a cut-short image over unchanged paths was not rewritten, or the step did not apply")
            rc, out = scan(t2)
            s3 = next((r for r in read_receipt_steps(t2) if r["id"] == "fx/s3"), {})
            print(f"walk: changed · fx/s3 {s3.get('state')} · rc {rc}")
            check_ok(rc == 1 and s3.get("state") == "failed" and "s3.before.json" in str(s3.get("failure"))
                   and not (t2 / "s3.txt").exists(),
                   "a cut-short image over a changed path did not stop the up naming it, or the path moved")
        elif plant in ("schema-3", "schema-3-kill"):
            # TOOL-dSafePassage-15 AC1, AC3: a schema-3 receipt walks to the schema step, whose
            # `applied` row lands after its up; a kill between its temporary file and its rename.
            t = build_case_target("t")
            if plant == "schema-3-kill":
                fx = t.with_name("t.fx")
                fx.mkdir()
                (fx / "schema.block").touch()
                argv = [sys.executable, "-c", FIXTURE_WALK_CHILD, str(HERE / "upgrade_steps.py"), str(gov), str(t), sha["C"]]
                why = run_killed(argv, fx, "schema", env)
                check_ok(why is None, f"the kill was not staged: {why}")
                (fx / "schema.block").unlink()
                try:
                    rec = json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8"))
                except ValueError:
                    rec = {}
                whole = ((rec.get("schema") == 3 and "steps" not in rec)
                         or (rec.get("schema") == 4 and isinstance(rec.get("steps"), list)))
                tmp_file = (t / ".governance" / "install.json.govkit-new").is_file()
                print(f"walk: after the kill · the receipt reads schema {rec.get('schema')}"
                      + (" whole" if whole else ", NOT WHOLE") + f" · the up's temporary file "
                      + ("present" if tmp_file else "absent"))
                check_ok(whole, "the kill left a receipt that is neither schema 3 nor schema 4 whole")
                check_ok(tmp_file, "the kill did not land after the up's temporary file was written")
            rc, out = scan(t)
            want = ["govkit/receipt-schema-4", "fx/s1", "fx/s2", "fx/s3", "fx/s4"]
            rec = json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8"))
            print(f"walk: the receipt reads schema {rec.get('schema')} · first row "
                  f"{(rec.get('steps') or [{}])[0].get('id')} {(rec.get('steps') or [{}])[0].get('state')}")
            check_ok(extract_step_lines(out) == [f"step {s} · applied" for s in want],
                   f"the step lines are not {want} in that order, each applied")
            check_ok(rec.get("schema") == 4 and [(r["id"], r["state"]) for r in read_receipt_steps(t)]
                   == [(s, "applied") for s in want], "the receipt is not schema 4 with the walk's rows, "
                   "the schema step's first")
            check_ok(rc == 0, f"the walk exited {rc}")
            if plant == "schema-3-kill":
                t2 = build_case_target("t2")
                rc2, _out2 = scan(t2)
                same = read_target_bytes(t) == read_target_bytes(t2)
                print(f"walk: the re-run's target and receipt {'equal' if same else 'DIFFER from'} an uninterrupted walk's")
                check_ok(same and rc2 == 0, "the re-run did not converge to an uninterrupted walk's bytes")
        elif plant == "schema-3-fail":
            # TOOL-dSafePassage-15 AC2: the schema step's up fails on a schema-3 receipt, which holds
            # no row, so the walk stops writing nothing and says why.
            t = build_case_target("t")
            t.with_name("t.fx").mkdir()
            (t.with_name("t.fx") / "schema.fail").touch()
            before = (t / ".governance" / "install.json").read_bytes()
            rc, out = scan(t)
            same = (t / ".governance" / "install.json").read_bytes() == before
            print(f"walk: the receipt's bytes {'equal' if same else 'DIFFER from'} their bytes before the run")
            check_ok(extract_step_lines(out) == ["step govkit/receipt-schema-4 · failed · exit 1: fx: schema up fails by its "
                                     f"plant {NOT_RECORDED_SUFFIX}"], "the step line is not the unrecorded failure")
            check_ok(same and rc == 1, f"the receipt changed, or the walk exited {rc}, not 1")
        for f in fails:
            print(f"walk: FAILED · {f}")
        return 1 if fails else rc


def run_lock_fixture(plant: str) -> int:
    """`fixture lock --plant <case>` (S9): AC7 and AC8, each take a child process calling govkit's
    `take_write_lock` over a scratch target whose lock the plant wrote. An unmet expectation prints
    `lock: FAILED`; otherwise the exit is the take's, the refusing plants' 1 by design."""
    with tempfile.TemporaryDirectory(prefix="gk-lock-", ignore_cleanup_errors=True) as td:
        tmp = pathlib.Path(td)
        t = tmp / "t"
        gk = load_govkit()
        lock = t.joinpath(*gk.WRITE_LOCK_REL.split("/"))
        guard = lock.with_name(lock.name + gk.RECLAIM_GUARD_SUFFIX)
        lock.parent.mkdir(parents=True)
        env = build_fixture_env()
        fails: list[str] = []
        sleeper = None

        def check_ok(ok: bool, what: str) -> None:
            if not ok:
                fails.append(what)

        def build_dead_pid() -> int:
            p = subprocess.Popen([sys.executable, "-c", "pass"])
            p.wait()
            return p.pid

        def write_lock_plant(pid: int, started: float, host: str | None = THIS_HOST,
                       started_boot: float | None = None, ns: dict | None = None) -> bytes:
            # `ns` replaces the namespace keys; by default this process's `pid_ns` (TOOL-dSafePassage-31).
            rec = {"pid": pid, "verb": "update", "started": started,
                   "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)),
                   **({"pid_ns": read_pid_namespace()} if ns is None else ns)}
            if host:
                rec["host"] = host
            if started_boot is not None:
                rec["started_boot"] = started_boot
            lock.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
            return lock.read_bytes()

        def run_take(gate: str = "-", release: str = "-", out_file: pathlib.Path | None = None,
                 pidns: str | None = None, bootid: str | None = None):
            argv = [sys.executable, "-c", FIXTURE_LOCK_CHILD, str(HERE / "upgrade_steps.py"), str(t), gate, release]
            argv += ["pidns", pidns] if pidns is not None else []
            argv += ["bootid", bootid] if bootid is not None else []
            argv += ["6"] if plant == "lock-live-slow-census" else []
            argv += ["wall-step", str(holder), str(born)] if plant.startswith("lock-wall-step") else []
            if out_file is None:
                p = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace",
                                   env=env, timeout=600)
                print(p.stdout + p.stderr, end="")
                return p.returncode, p.stdout + p.stderr
            return subprocess.Popen(argv, stdout=open(out_file, "w", encoding="utf-8"),
                                    stderr=subprocess.STDOUT, env=env)

        def parse_taker_pid(out: str) -> int | None:
            m = re.search(r"lock: taker pid (\d+)", out)
            return int(m[1]) if m else None

        def read_held() -> dict:
            return read_lock_holder(lock)[1] or {}

        try:
            rc = 0
            if plant in ("lock-dead", "lock-reused", "lock-live", "lock-foreign-host", "lock-foreign-namespace",
                         "lock-unreadable", "lock-foreign-pidns", "lock-no-pidns", "lock-other-boot", "lock-no-namespace",
                         "lock-live-slow-census", "lock-wall-step", "lock-wall-step-no-boot"):
                if plant == "lock-dead":
                    holder = build_dead_pid()
                    before = write_lock_plant(holder, time.time() - 30)
                elif plant in ("lock-reused", "lock-live"):
                    sleeper = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(300)"])
                    holder = sleeper.pid
                    time.sleep(0.5)
                    # TOOL-dSafePassage-35 S5: a reused lock is 600 s old on the boot clock too,
                    # wherever there is one, so a `posix-ps` judge reads it reused at any latency.
                    boot = read_boot_clock() if plant == "lock-reused" else None
                    before = write_lock_plant(holder, time.time() - (600 if plant == "lock-reused" else 0),
                                        started_boot=None if boot is None else boot - 600)
                elif plant == "lock-live-slow-census":
                    # TOOL-dSafePassage-22: the lock taken at once, so a clock read after the
                    # census's six seconds puts the live holder near `started + 6`, past
                    # REUSE_MARGIN_S by more than 3 s (TOOL-dSafePassage-35 S4).
                    sleeper = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(300)"])
                    holder = sleeper.pid
                    before = write_lock_plant(holder, time.time())
                elif plant.startswith("lock-wall-step"):
                    # TOOL-dSafePassage-32: the holder's age on the boot clock, its lock read on
                    # both clocks (the wall alone for -no-boot), and the judge's wall 10 s ahead.
                    born = time.monotonic()
                    sleeper = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(300)"])
                    holder = sleeper.pid
                    time.sleep(0.5)
                    before = write_lock_plant(holder, time.time(), started_boot=None if plant.endswith("-no-boot")
                                        else time.monotonic())
                elif plant == "lock-foreign-host":
                    holder = build_dead_pid()
                    before = write_lock_plant(holder, time.time() - 30, "gk-elsewhere.invalid")
                elif plant == "lock-foreign-namespace":
                    # TOOL-dSafePassage-26 S33: this host, a dead pid, another platform's record.
                    holder = build_dead_pid()
                    rec = json.loads(write_lock_plant(holder, time.time() - 30))
                    lock.write_text(json.dumps({**rec, "platform": "gk-elsewhere", "boot_id": ""}, indent=2) + "\n",
                                    encoding="utf-8", newline="\n")
                    before = lock.read_bytes()
                elif plant in ("lock-foreign-pidns", "lock-no-pidns"):
                    # TOOL-dSafePassage-31 S4: this host, platform and boot, a dead pid, and another
                    # Linux pid namespace's `pid_ns` or none; the judge's own reading a Linux one.
                    holder = build_dead_pid()
                    ns = {"platform": sys.platform, "boot_id": read_boot_id()}
                    before = write_lock_plant(holder, time.time() - 30, ns={**ns, "pid_ns": "pid:[4026532244]"}
                                        if plant == "lock-foreign-pidns" else ns)
                elif plant == "lock-other-boot":
                    # TOOL-dSafePassage-35 S26: this host and platform, a live pid, and a boot id the
                    # judge's `bootid` stand-in differs from: the reboot ended the holder.
                    sleeper = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(300)"])
                    holder = sleeper.pid
                    before = write_lock_plant(holder, time.time(), ns={"platform": sys.platform, "boot_id": "gk-boot-before",
                                                                 "pid_ns": read_pid_namespace()})
                elif plant == "lock-no-namespace":
                    # TOOL-dSafePassage-35 S26: a dead pid's lock with none of the namespace keys.
                    holder = build_dead_pid()
                    before = write_lock_plant(holder, time.time() - 30, ns={})
                else:
                    holder = None
                    lock.write_text("not a lock\n", encoding="utf-8", newline="\n")
                    before = lock.read_bytes()
                rc, out = run_take(pidns="pid:[4026532221]" if plant.endswith(("-pidns", "-namespace")) else None,
                               bootid="gk-boot-after" if plant == "lock-other-boot" else None)
                if plant == "lock-other-boot":
                    check_ok("this host has booted since" in out, "the reclaim does not name the reboot")
                if plant in ("lock-dead", "lock-reused", "lock-other-boot"):
                    rec = read_held()
                    print(f"lock: held by pid {rec.get('pid')} · host {rec.get('host')} · pid_ns {rec.get('pid_ns')!r}")
                    check_ok(rc == 0 and f"reclaimed {lock.as_posix()}" in out and f"pid {holder} " in out,
                           f"the dead holder pid {holder} was not reclaimed, naming it")
                    check_ok(rec.get("pid_ns") == read_pid_namespace(), "the lock does not record the taker's pid_ns")
                    check_ok(rec.get("pid") == parse_taker_pid(out) and rec.get("host") == THIS_HOST,
                           "the lock does not name the taker's pid and this host")
                else:
                    print(f"lock: the planted lock {'unchanged' if lock.read_bytes() == before else 'CHANGED'}")
                    check_ok(rc == 1 and "another govkit write holds" in out and "reclaim" in out,
                           "the take did not refuse with the holder described and the remedy naming the reclaim")
                    check_ok(lock.read_bytes() == before, "a refusing take changed the lock")
                    check_ok({"lock-live": f"pid {holder} ", "lock-live-slow-census": f"pid {holder} ",
                            "lock-wall-step": f"pid {holder} ", "lock-wall-step-no-boot": f"pid {holder} ",
                            "lock-foreign-host": "gk-elsewhere.invalid",
                            "lock-foreign-namespace": "unknown, it was taken under platform 'gk-elsewhere'",
                            "lock-unreadable": "no readable pid",
                            "lock-foreign-pidns": "unknown, it was taken under pid_ns 'pid:[4026532244]'",
                            "lock-no-pidns": "unknown, it was taken with no pid_ns recorded",
                            "lock-no-namespace": "unknown, it was taken with no pid_ns recorded"}[plant] in out,
                           "the refusal does not describe the holder")
                    if plant in ("lock-no-pidns", "lock-no-namespace"):
                        # AC3: with this process's `pid_ns` "", as off Linux, the census judges it dead.
                        rc2, out2 = run_take(pidns="")
                        print(f"lock: with no pid_ns here, the take exits {rc2}")
                        check_ok(rc2 == 0 and f"reclaimed {lock.as_posix()}" in out2 and f"pid {holder} " in out2,
                               "with no pid_ns on either side the census did not reclaim the dead holder")
                    if plant.startswith("lock-wall-step"):
                        verdict = "unknown" if plant.endswith("-no-boot") else "live"
                        check_ok(f"refusing rather than joining in: {verdict}, " in out,
                               f"the stepped wall clock did not leave the holder {verdict}")
            elif plant == "lock-race":
                write_lock_plant(build_dead_pid(), time.time() - 30)
                gate, release = tmp / "go", tmp / "release"
                outs = [tmp / "r1.out", tmp / "r2.out"]
                racers = [run_take(str(gate), str(release), o) for o in outs]
                time.sleep(1)
                gate.touch()
                deadline = time.time() + 300

                def check_settled(i: int) -> bool:
                    text = outs[i].read_text(encoding="utf-8", errors="replace")
                    return "lock: taken" in text or "lock: refused" in text or racers[i].poll() is not None
                while not all(check_settled(i) for i in (0, 1)) and time.time() < deadline:
                    time.sleep(0.1)
                pid_held = read_held().get("pid")
                release.touch()
                codes = [r.wait(timeout=300) for r in racers]
                texts = [o.read_text(encoding="utf-8", errors="replace") for o in outs]
                print("".join(texts), end="")
                won = [i for i in (0, 1) if codes[i] == 0]
                print(f"lock: racers exit {codes} · the lock names pid {pid_held}")
                check_ok(len(won) == 1, "not exactly one racer took the lock")
                if len(won) == 1:
                    check_ok(pid_held == parse_taker_pid(texts[won[0]]), "the lock does not name the winner")
                    check_ok("busy" in texts[1 - won[0]], "the losing racer did not refuse busy")
            elif plant == "guard-dead":
                before = write_lock_plant(build_dead_pid(), time.time() - 30)
                guard.write_text(json.dumps({"pid": build_dead_pid(), "started": time.time() - 10, "host": THIS_HOST,
                                             "pid_ns": read_pid_namespace()}) + "\n",
                                 encoding="utf-8", newline="\n")
                rc1, out1 = run_take()
                print(f"lock: first take exits {rc1} · guard {'present' if guard.exists() else 'cleared'} · "
                      f"lock {'unchanged' if lock.read_bytes() == before else 'CHANGED'}")
                check_ok(rc1 == 1 and "busy" in out1 and "cleared the guard" in out1 and not guard.exists()
                       and lock.read_bytes() == before, "the first take did not clear the dead guard and refuse busy")
                rc, out = run_take()
                check_ok(rc == 0 and "reclaimed" in out and read_held().get("pid") == parse_taker_pid(out),
                       "the second take did not reclaim the lock")
        finally:
            if sleeper is not None:
                sleeper.kill()
                sleeper.wait()
        for f in fails:
            print(f"lock: FAILED · {f}")
        return 1 if fails else rc


def run_fixture_govkit(gov: pathlib.Path, env: dict, *args: str) -> tuple[int, str]:
    """The scratch gov's own `govkit.py <args>` under `env`: (exit, stdout and stderr)."""
    p = subprocess.run([sys.executable, str(gov / FIXTURE_PREFIX / HERE.name / "govkit.py"), *args], capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=env, timeout=600)
    return p.returncode, p.stdout + p.stderr


def build_update_gov(tmp: pathlib.Path, names, slugs, fails: list[str],
                     schema3: bool = False, down_exit=()) -> tuple[pathlib.Path, dict, str, str, dict]:
    """The `update` and `rollback-update` families' scratch gov: at A copies of this checkout's
    `govkit.py`, `upgrade_steps.py` and the process-monitor census and a `demo` kit whose
    `one.txt` reads `v1`; a target per `names` installed at A by `apply` and committed; at B the
    steps `fx/<slug>` for each of `slugs` and `one.txt` reading `v2`. `schema3` forces each receipt
    `apply` wrote to schema 3 with `steps` taken out before that commit, and puts the copied
    `govkit/receipt-schema-4` row first at B (TOOL-dSafePassage-15). Each slug of `down_exit` is
    rendered with `reverted = "down-exit"`, the floor row's shape (TOOL-dSafePassage-70). A failed
    install is appended to `fails`. Returns (gov, {name: target}, A, B, the env every govkit call
    runs under)."""
    gov = tmp / "gov"
    pm = resolve_kit_dir("process-monitor", "census.py", HERE)
    gkd, demo, pmd = gov / FIXTURE_PREFIX / HERE.name, gov / FIXTURE_PREFIX / "demo", gov / FIXTURE_PREFIX / pm.name
    for d in (gkd, demo, pmd):
        d.mkdir(parents=True)
    for name in ("govkit.py", "upgrade_steps.py", "adopters.toml"):
        shutil.copy2(HERE / name, gkd / name)
    shutil.copy2(pm / "census.py", pmd / "census.py")
    (gkd / REGISTRY_FILE).write_text(
        '[surface]\nglobs = ["{prefix}/*"]\n\n[selection]\ndefault = ["demo"]\n\n'
        '[[entry]]\nid = "demo"\ndescriptor = "{prefix}/demo/kit.toml"\n\n'
        '[[exempt]]\npath = "{prefix}/govkit"\nwhy = "the deployer itself"\n\n'
        '[[exempt]]\npath = "{prefix}/process-monitor"\nwhy = "the census a lock reclaim reads"\n',
        encoding="utf-8", newline="\n")
    (demo / "kit.toml").write_text('id = "demo"\nhome = "demo"\n[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                                   '[adopt]\nargv = []\nmutates_index = false\n', encoding="utf-8", newline="\n")
    (demo / "one.txt").write_text("v1\n", encoding="utf-8", newline="\n")
    load_fixture_target().build_scratch_gov(gov)
    run_fixture_git(gov, "add", "-A")
    run_fixture_git(gov, "commit", "-qm", "A")
    sha_a = run_fixture_git(gov, "rev-parse", "HEAD")
    env = build_fixture_env(GOVKIT_NO_REMOTE_PROBE="1")
    targets = {}
    for name in names:
        t = targets[name] = load_fixture_target().build_target(
            tmp, 'gov_source = "local"\nprefix = "tools"\nkits = ["demo"]\n', name)
        rc, out = run_fixture_govkit(gov, env, "apply", "--target", str(t))
        if rc != 0:
            fails.append(f"the scratch install of {name} failed ({rc}): {out[-600:]}")
        if schema3:
            rp = t / ".governance" / "install.json"
            rec = json.loads(rp.read_text(encoding="utf-8"))
            rec["schema"] = 3
            rec.pop("steps", None)
            rp.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
        run_fixture_git(t, "add", "-A")
        run_fixture_git(t, "commit", "-qm", "install")
    (gkd / "steps").mkdir()
    (gkd / "steps" / "fx.py").write_text(FIXTURE_WALK_STEP, encoding="utf-8", newline="\n")
    (gkd / STEPS_FILE).write_text((write_fixture_schema_step(gkd) if schema3 else "")
                                  + "".join(render_fixture_row(s, reverted="down-exit" if s in down_exit else None)
                                            for s in slugs), encoding="utf-8", newline="\n")
    (demo / "one.txt").write_text("v2\n", encoding="utf-8", newline="\n")
    run_fixture_git(gov, "add", "-A")
    run_fixture_git(gov, "commit", "-qm", "B")
    return gov, targets, sha_a, run_fixture_git(gov, "rev-parse", "HEAD"), env


def run_update_fixture(plant: str | None) -> int:
    """`fixture update [--plant <case>]` (S9): AC6 and AC9 through a scratch gov holding copies of
    this checkout's `govkit.py`, `upgrade_steps.py` and the process-monitor census, a `demo` kit, and
    at B the steps `fx/s1` and `fx/s2`; a target installed at A is moved to B. An unmet expectation
    prints `update: FAILED`; otherwise the exit is `update`'s, `update-fail`'s 1 by design."""
    with tempfile.TemporaryDirectory(prefix="gk-upd-", ignore_cleanup_errors=True) as td:
        tmp = pathlib.Path(td)
        fails: list[str] = []
        gov, targets, sha_a, sha_b, env = build_update_gov(
            tmp, ("t", "t2") if plant in ("kill-walk", "kill-walk-edit", "schema-3-update") else ("t",), ("s1", "s2"),
            fails, schema3=plant == "schema-3-update")
        gkd = gov / FIXTURE_PREFIX / HERE.name

        def check_ok(ok: bool, what: str) -> None:
            if not ok:
                fails.append(what)

        def run_govkit(*args: str) -> tuple[int, str]:
            return run_fixture_govkit(gov, env, *args)

        t = targets["t"]
        reports = t.with_name("t.fx")

        def load_receipt_of(tt: pathlib.Path) -> dict:
            return json.loads((tt / ".governance" / "install.json").read_text(encoding="utf-8"))

        def read_canaries() -> list[str]:
            return sorted(p.name for p in reports.iterdir()) if reports.is_dir() else []

        def read_staged(tt: pathlib.Path) -> set[str]:
            return set(run_fixture_git(tt, "diff", "--cached", "--name-only").splitlines())

        rc = 0
        if fails:
            pass
        elif plant is None:
            rc, out = run_govkit("update", "--target", str(t), "--to", sha_b, "--write")
            print(out, end="")
            lines = out.splitlines()
            at = [i for i, ln in enumerate(lines) if ln.startswith("step fx/")]
            land = [i for i, ln in enumerate(lines) if "tools/demo/one.txt" in ln]
            rerender = [i for i, ln in enumerate(lines) if ln.startswith("govkit update — re-render")]
            print(f"update: write-loop lines end at {max(land, default=None)} · step lines {at} · re-render begins at "
                  f"{min(rerender, default=None)}")
            check_ok(len(at) == 2 and land and rerender and max(land) < min(at) and max(at) < min(rerender),
                   "the step lines are not after the write loop's and before the re-render block's")
            check_ok("govkit update — steps: 2 pending · 2 applied · 0 skipped · stopped at none" in lines,
                   "the summary line does not read 2 pending · 2 applied · 0 skipped · stopped at none")
            check_ok(load_receipt_of(t).get("gov_commit") == sha_b and rc == 0, "the stamp did not move to B")
            want = {"s1.txt", "s2.txt", ".governance/steps/fx/s1.before.json", ".governance/steps/fx/s2.before.json"}
            print(f"update: staged step writes: {sorted(want & read_staged(t))}")
            check_ok(want <= read_staged(t), "a step's write is left unstaged")
        elif plant in ("read-only", "scoped", "scoped-read-only"):
            rc, out = run_govkit("update", "--target", str(t), "--to", sha_b,
                             *(("--kits", "demo", "--write") if plant == "scoped"
                               else ("--kits", "demo") if plant == "scoped-read-only" else ()))
            print(out, end="")
            print(f"update: step canaries {read_canaries() or 'none'}")
            if plant == "read-only":
                check_ok([ln.strip() for ln in out.splitlines() if "would walk" in ln]
                       == ["govkit update —   would walk fx/s1".strip(), "govkit update —   would walk fx/s2".strip()],
                       "the read-only run does not print `would walk` for each of the two steps")
            else:
                check_ok(any(ln.startswith("govkit update — steps: not walked") and ln.endswith("· 2 pending")
                           for ln in out.splitlines()), "the scoped run does not print `steps: not walked` with 2 pending")
                check_ok(plant == "scoped" or "would walk" not in out, "the scoped read-only run prints `would walk`")
            check_ok(not read_canaries(), "a step spawned on a read-only or scoped run")
        elif plant == "update-fail":
            reports.mkdir()
            (reports / "s2.fail").touch()
            rc, out = run_govkit("update", "--target", str(t), "--to", sha_b, "--write")
            print(out, end="")
            got = {r["id"]: r["state"] for r in load_receipt_of(t).get("steps") or []}
            print(f"update: gov_commit {'A' if load_receipt_of(t).get('gov_commit') == sha_a else load_receipt_of(t).get('gov_commit')} · "
                  f"steps {got} · tools/demo/one.txt {(t / FIXTURE_PREFIX / 'demo' / 'one.txt').read_bytes()!r}")
            check_ok(rc == 1 and load_receipt_of(t).get("gov_commit") == sha_a, "a stopped walk let the stamp move")
            check_ok(got == {"fx/s1": "applied", "fx/s2": "failed"}, "s1 is not applied and s2 failed")
            check_ok((t / FIXTURE_PREFIX / "demo" / "one.txt").read_bytes() == b"v2\n", "the file rows did not land")
            check_ok(not [c for c in read_canaries() if c.endswith(".down")], "a down ran")
        elif plant == "needs-target-source":
            # TOOL-dSafePassage-26 S32, AC31: `update` on gov's own tree, source mode, over a row
            # declaring needs-target = true. Its witness runs there, gov's code being the target's:
            # not holding, the walk stops attended at exit 1; holding, the row reads applied, exit 0.
            (gkd / STEPS_FILE).write_text("".join(render_fixture_row(s, needs=s == "s2") for s in ("s1", "s2")),
                                          encoding="utf-8", newline="\n")
            (gov / ".governance").mkdir(exist_ok=True)
            (gov / ".governance" / "deploy.toml").write_text('gov_source = "."\nprefix = "tools"\nkits = ["demo"]\n',
                                                             encoding="utf-8", newline="\n")
            run_fixture_git(gov, "add", "-A")
            run_fixture_git(gov, "commit", "-qm", "a needs-target row")

            def read_row_state(sid: str) -> str | None:
                return next((r.get("state") for r in load_receipt_of(gov).get("steps") or [] if r.get("id") == sid), None)

            rc1, out1 = run_govkit("update", "--target", str(gov), "--write")
            print(out1, end="")
            print(f"update: source mode, witness absent · exit {rc1} · fx/s2 {read_row_state('fx/s2')}")
            check_ok(rc1 == 1 and f"step fx/s2 · failed · {ATTENDED_STOP}" in out1,
                   "a needs-target row whose witness does not hold did not stop the source walk attended")
            (gov / "s2.txt").write_text("s2\n", encoding="utf-8", newline="\n")
            rc, out = run_govkit("update", "--target", str(gov), "--write")
            print(out, end="")
            print(f"update: source mode, witness holds · exit {rc} · fx/s2 {read_row_state('fx/s2')}")
            check_ok(rc == 0 and read_row_state("fx/s2") == "applied",
                   "a needs-target row whose witness holds did not read applied on gov's tree")
        elif plant == "schema-3-update":
            # TOOL-dSafePassage-15 AC4: `update` from a schema-3 receipt `apply` wrote, then again on
            # a second target with the schema step killed during its up, and that target re-run.
            rc, out = run_govkit("update", "--target", str(t), "--to", sha_b, "--write")
            print(out, end="")
            rec = load_receipt_of(t)
            got = [(r.get("id"), r.get("state")) for r in rec.get("steps") or []]
            print(f"update: the receipt reads schema {rec.get('schema')} · steps {got}")
            check_ok(rc == 0 and rec.get("schema") == 4 and got == [("govkit/receipt-schema-4", "applied"),
                   ("fx/s1", "applied"), ("fx/s2", "applied")],
                   "update did not take the schema-3 receipt to schema 4 with the schema step applied first")
            t2 = targets["t2"]
            r2 = t2.with_name("t2.fx")
            r2.mkdir()
            (r2 / "schema.block").touch()
            why = run_killed([sys.executable, str(gkd / "govkit.py"), "update", "--target", str(t2), "--to", sha_b,
                              "--write"], r2, "schema", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (r2 / "schema.block").unlink()
            rc2, out2 = run_govkit("update", "--target", str(t2), "--to", sha_b, "--write")
            print(out2, end="")
            # `carry` is output, recomputed each run (DEPL-dCarriedReceipt-9 S2), and the killed run
            # persisted no receipt below schema 4, so it is the one key the two may differ in (rev-2).
            a, b = load_receipt_of(t), load_receipt_of(t2)
            for rec in (a, b):
                for f in rec.get("files") or []:
                    f.pop("carry", None)
            same = a == b
            print(f"update: the killed target's re-run exits {rc2} · its receipt, carry aside, "
                  f"{'equals' if same else 'DIFFERS from'} the uninterrupted run's"
                  + ("" if same else f": {sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))}"))
            check_ok(rc2 == 0 and same, "the re-run after the kill did not exit 0 with the uninterrupted run's receipt")
        else:
            reports.mkdir()
            (reports / "s1.block").touch()
            argv = [sys.executable, str(gkd / "govkit.py"), "update", "--target", str(t), "--to", sha_b, "--write"]
            why = run_killed(argv, reports, "s1", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (reports / "s1.block").unlink()
            journal = set(read_staging_journal(t))
            print(f"update: after the kill · journal {sorted(journal)} · staged {sorted(read_staged(t))}")
            check_ok(journal and journal == read_staged(t), "the staging journal's paths do not equal the staged set")
            if plant == "kill-walk-edit":
                (t / FIXTURE_PREFIX / "demo" / "one.txt").write_text("operator edit\n", encoding="utf-8", newline="\n")
                run_fixture_git(t, "add", "tools/demo/one.txt")
            rc, out = run_govkit("update", "--target", str(t), "--to", sha_b, "--write")
            print(out, end="")
            if plant == "kill-walk-edit":
                check_ok(rc != 0 and "DIRTY: tools/demo/one.txt" in out,
                       "the re-run did not refuse the operator's different blob at a journaled path as dirty")
            else:
                rc2, _out2 = run_govkit("update", "--target", str(targets["t2"]), "--to", sha_b, "--write")
                a, b = read_target_bytes(t), read_target_bytes(targets["t2"])
                print(f"update: the re-run's bytes {'equal' if a == b else 'DIFFER from'} an uninterrupted run's"
                      + ("" if a == b else f": {sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))}"))
                check_ok(rc == 0 and "reclaimed" in out and a == b and rc2 == 0,
                       "the re-run did not reclaim the lock and converge to an uninterrupted run's bytes")
        for f in fails:
            print(f"update: FAILED · {f}")
        return 1 if fails else rc


def read_reverse_walk_callers(texts: dict[str, str]) -> list[tuple[str, int, str]]:
    """(file name, line, innermost enclosing function) of each call of `run_reverse_walk`, by a bare
    name or as an attribute, in `texts`, `{file name: module text}` (TOOL-dSafePassage-4 S7). WHAT IT
    DOES NOT SEE: a call through an alias or `getattr`, which nothing in either module spells."""
    sites = []
    for name, text in texts.items():
        tree = ast.parse(text)
        fns = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        for call in (n for n in ast.walk(tree) if isinstance(n, ast.Call)):
            f = call.func
            if (f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else "") != "run_reverse_walk":
                continue
            owner = min((fn for fn in fns if fn.lineno <= call.lineno <= fn.end_lineno),
                        key=lambda fn: fn.end_lineno - fn.lineno, default=None)
            sites.append((name, call.lineno, owner.name if owner else "<module>"))
    return sites


def run_callers_probe(texts: dict[str, str]) -> int:
    """S7's probe over `texts`: 0 where `run_reverse_walk` has exactly one call, in govkit's
    `_cmd_update`, else 1 naming every call it found, or that it found none."""
    sites = read_reverse_walk_callers(texts)
    for f, line, fn in sites:
        print(f"rollback: callers · a call of run_reverse_walk at {f}:{line}, in {fn}")
    if [(f, fn) for f, _l, fn in sites] == [("govkit.py", "_cmd_update")]:
        print("rollback: callers · one caller, update's _cmd_update")
        return 0
    print(f"rollback: callers · RED · {len(sites)} call(s) of run_reverse_walk, where its one caller is "
          f"_cmd_update" + ("; the probe read nothing" if not sites else ""))
    return 1


def run_rollback_fixture(plant: str | None) -> int:
    """`fixture rollback [--plant <case>]` (TOOL-dSafePassage-4 AC1 to AC4, AC7): the `walk` family's
    scratch gov, A to C and `s1` to `s4`, and a target walked from A to C, then reverse-walked to A
    (to B under `partial-to`) through `FIXTURE_REVERSE_CHILD`. Its bytes are compared but for the
    receipt and the staging journal. The `schema-step` plants (TOOL-dSafePassage-18) put the copied
    schema step first, over a schema-3 target. An unmet expectation prints `rollback: FAILED`;
    otherwise the exit is the reverse walk's first, `down-fails`', `witness-stays`',
    `node-witness-refuses`', `schema-step-early`'s, `image-lost`'s and `kill-after-up-image-lost`'s 1
    by design; the last (TOOL-dSafePassage-40) kills the walk after s3's up, re-runs it and deletes
    s3's image, so s3's down stops naming it. `witness-only` and the
    `node-witness` plants (TOOL-dSafePassage-17) make s2's witness hold before any up, so the walk
    records it `applied` via its witness alone and writes it no before-image; `image-lost`
    (TOOL-dSafePassage-33) deletes the image s4's up wrote, so its down stops naming the image. The
    DOWN_KILLED_PLANTS (TOOL-dSafePassage-39) kill the first reverse walk in `witness-only`'s s2's
    down, the second after taking s2's row out of the receipt, and the re-run must down s2 by its exit.
    `witness-only-reup` (TOOL-dSafePassage-73) runs `witness-only`'s walk and reverse walk, then a
    second walk, which must mark s2 `via` its witness again, before the reverse walk below.
    `kill-after-down-stage` (TOOL-dSafePassage-76) commits the walk's staging, kills the reverse
    walk once s1's down restored, before its staging, and the re-run must stage both removals from
    the index's copy of the image; `-garbled` overwrites that copy first, its re-run refusing, 1."""
    if plant == "callers":
        texts = {p.name: p.read_text(encoding="utf-8") for p in (pathlib.Path(__file__).resolve(), HERE / "govkit.py")}
        rc = run_callers_probe(texts)
        planted = {**texts, "govkit.py": texts["govkit.py"] + (
            "\n\ndef planted_caller():\n    upgrade_steps.run_reverse_walk(None, None, None, {}, [])\n")}
        print("rollback: callers · over a govkit.py planted with a second caller:")
        if run_callers_probe(planted) != 1:
            print("rollback: FAILED · callers · a planted second caller does not read red")
            return 1
        return rc
    with tempfile.TemporaryDirectory(prefix="gk-rb-", ignore_cleanup_errors=True) as td:
        tmp = pathlib.Path(td)
        gov, sha = build_walk_gov(tmp, plant)
        env = build_fixture_env()
        t = build_walk_target(tmp, sha["A"], "t", schema3=plant in ROLLBACK_SCHEMA_PLANTS)
        fx = t.with_name("t.fx")
        fx.mkdir()
        rp = t / ".governance" / "install.json"
        skip = {".governance/install.json", load_govkit().STAGING_JOURNAL_REL}
        fails: list[str] = []

        def check_ok(ok: bool, what: str) -> None:
            if not ok:
                fails.append(what)

        def read_tracked() -> dict[str, bytes]:
            return {k: v for k, v in read_target_bytes(t).items() if k not in skip}

        def read_downs() -> list[str]:
            return sorted(p.name for p in fx.glob("*.down"))

        def read_rows() -> dict[str, tuple]:
            return {r["id"]: (r["state"], r.get("failure")) for r in read_receipt_steps(t)}

        def run_reverse() -> tuple[int, list[str], str]:
            rc, out = run_fixture_child(FIXTURE_REVERSE_CHILD, gov, t, sha["B" if plant == "partial-to" else "A"], env,
                                        *(("fx/s2",) if plant == "rolled-back-witness-holds" else ()))
            print(f"rollback: rows {read_rows()}")
            return rc, [ln for ln in out.splitlines() if ln.startswith("step fx/")], out

        def render_rolled(*slugs: str) -> list[str]:
            return [f"step fx/{s} · rolled-back" for s in slugs]

        before = read_tracked()
        if plant == "after-kill":
            (fx / "s3.block-after").touch()
            why = run_killed([sys.executable, "-c", FIXTURE_WALK_CHILD, str(HERE / "upgrade_steps.py"), str(gov),
                              str(t), sha["C"]], fx, "s3", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (fx / "s3.block-after").unlink()
            s3 = read_rows().get("fx/s3", (None, None))
            print(f"rollback: after the kill · fx/s3 {s3[0]} · s3.txt {'present' if (t / 's3.txt').is_file() else 'absent'}")
            check_ok(s3[0] == "failed" and (t / "s3.txt").is_file(), "the kill did not leave s3 failed with its first file written")
        elif plant == "kill-after-up-image-lost":
            # TOOL-dSafePassage-40 AC2: the walk family's `kill-after-up`, its re-run, then s3's
            # unstaged image lost.
            (fx / "s3.witness-block").touch()
            why = run_killed([sys.executable, "-c", FIXTURE_WALK_CHILD, str(HERE / "upgrade_steps.py"), str(gov),
                              str(t), sha["C"]], fx, "s3", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (fx / "s3.witness-block").unlink()
            rc_w, _out = run_fixture_child(FIXTURE_WALK_CHILD, gov, t, sha["C"], env)
            s3 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s3"), {})
            image = derive_image_path(t, "fx/s3")
            print(f"rollback: the re-run · fx/s3 {s3.get('state')} · via {s3.get('via')} · image "
                  f"{'present' if image.is_file() else 'absent'} before the plant deletes it")
            check_ok(rc_w == 0 and s3.get("state") == "applied" and "via" not in s3 and image.is_file(),
                   "the re-run did not record s3 applied with no `via`, its image on disk")
            image.unlink(missing_ok=True)
        else:
            if plant == "after-fail":
                (fx / "s3.fail").touch()
            elif plant in ("witness-only", "witness-only-reup") + DOWN_KILLED_PLANTS:
                (fx / "s2.witness-absent").touch()
            elif plant in NODE_WITNESS_PLANTS:
                (fx / "s2.witness-always").touch()
            rc_w, _out = run_fixture_child(FIXTURE_WALK_CHILD, gov, t, sha["C"], env)
            check_ok(rc_w == (1 if plant == "after-fail" else 0), f"the walk exited {rc_w}")
            if plant in ("witness-only", "witness-only-reup") + NODE_WITNESS_PLANTS + DOWN_KILLED_PLANTS:
                bare = (read_rows().get("fx/s2", ("",))[0] == "applied" and not (fx / "s2.up").exists()
                        and not derive_image_path(t, "fx/s2").exists())
                print("rollback: fx/s2 " + ("applied by witness alone, no before-image" if bare
                                            else "NOT applied by witness alone"))
                check_ok(bare, "s2 is not recorded applied by witness alone with no before-image")
                via = next((r.get("via") for r in read_receipt_steps(t) if r["id"] == "fx/s2"), None)
                print(f"rollback: fx/s2 recorded via {via}")
                check_ok(via == "witness", "s2 is not recorded `via` `witness` (TOOL-dSafePassage-33)")
        print(f"rollback: down canaries before the reverse walk: {read_downs() or 'none'}")
        check_ok(not read_downs(), "a down ran before the reverse walk was called")
        if plant == "unrecorded":
            receipt = json.loads(rp.read_text(encoding="utf-8"))
            receipt["steps"] = [r for r in receipt["steps"] if r["id"] != "fx/s2"]
            rp.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
            check_ok((t / "s2.txt").is_file(), "s2's file is not present for the unrecorded plant")
        elif plant in ("kill-after-down-stage", "kill-after-down-stage-garbled"):
            # TOOL-dSafePassage-76 AC3: the walk's staging committed, as an adopter commits an update,
            # then the reverse walk killed once s1's down restored, before its staging; the reverse()
            # below is the re-run. `-garbled` overwrites the index's image with bytes that are no JSON.
            run_fixture_git(t, "commit", "-qm", "at C")
            (fx / "s1.down-block-after").touch()
            why = run_killed([sys.executable, "-c", FIXTURE_REVERSE_CHILD, str(HERE / "upgrade_steps.py"),
                              str(gov), str(t), sha["A"]], fx, "s1", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (fx / "s1.down-block-after").unlink()
            image = derive_image_path(pathlib.Path("."), "fx/s1").as_posix()
            s1 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s1"), {})
            gone = not (t / "s1.txt").exists() and not (t / image).exists()
            indexed = run_fixture_git(t, "ls-files", "--", "s1.txt", image).splitlines()
            print(f"rollback: after the kill · fx/s1 {s1.get('state')} · {s1.get('failure')} · s1.txt and its image "
                  f"{'restored away' if gone else 'NOT both gone'} · the index holds {indexed}")
            check_ok(s1.get("state") == "applied" and str(s1.get("failure", "")).startswith(DOWN_STOP_PREFIXES[0])
                   and gone and sorted(indexed) == sorted(["s1.txt", image]),
                   "the kill did not land after s1's down restored and before its staging")
            if plant.endswith("-garbled"):
                oid = subprocess.run(["git", "-C", str(t), "hash-object", "-w", "--stdin"], input=b"not json\n",
                                     capture_output=True, env=env).stdout.decode("ascii").strip()
                run_fixture_git(t, "update-index", "--cacheinfo", f"100644,{oid},{image}")
        elif plant == "witness-only-reup":
            # TOOL-dSafePassage-73 S5: down to A and up to C again; s2, recorded rolled-back as the
            # second walk begins, its witness holding with no up and no image, keeps its mark.
            rc_r, got_r, _o = run_reverse()
            check_ok(rc_r == 0 and got_r == render_rolled("s4", "s3", "s2", "s1"), f"the first reverse walk exited {rc_r}")
            rc_w, _out = run_fixture_child(FIXTURE_WALK_CHILD, gov, t, sha["C"], env)
            via = next((r.get("via") for r in read_receipt_steps(t) if r["id"] == "fx/s2"), None)
            print(f"rollback: fx/s2 recorded via {via} after a rollback")
            check_ok(rc_w == 0 and via == "witness", f"the second walk exited {rc_w}, or s2 is not recorded `via` `witness`")
        elif plant == "image-lost":
            # TOOL-dSafePassage-33 AC2: s4's up wrote s4.txt and its image; the image is then lost.
            s4 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s4"), {})
            image = derive_image_path(t, "fx/s4")
            ready = s4.get("state") == "applied" and "via" not in s4 and image.is_file() and (t / "s4.txt").is_file()
            print(f"rollback: fx/s4 {s4.get('state')} · via {s4.get('via')} · image "
                  f"{'present' if image.is_file() else 'absent'} before the plant deletes it")
            check_ok(ready, "s4 is not recorded applied by its up, no `via`, with its file and image")
            image.unlink(missing_ok=True)
        elif plant == "down-fails":
            (fx / "s3.down-fails").touch()
        elif plant == "witness-stays":
            (fx / "s2.down-keeps").touch()
        elif plant == "node-witness-refuses":
            (fx / "s2.down-fails").touch()
        elif plant == "schema-step-early":
            (fx / "s2.down-lowers").touch()
        elif plant == "schema-step-kill":
            # TOOL-dSafePassage-18 AC2: killed during the schema step's down, after its temporary
            # file and before its rename; the reverse() below is the re-run.
            (fx / "schema.block").touch()
            why = run_killed([sys.executable, "-c", FIXTURE_REVERSE_CHILD, str(HERE / "upgrade_steps.py"),
                              str(gov), str(t), sha["A"]], fx, "schema", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (fx / "schema.block").unlink()
            try:
                rec = json.loads(rp.read_text(encoding="utf-8"))
            except ValueError:
                rec = {}
            srow = next((r for r in rec.get("steps") or [] if r.get("id") == "govkit/receipt-schema-4"), {})
            whole = ((rec.get("schema") == 3 and "steps" not in rec)
                     or (rec.get("schema") == 4 and str(srow.get("failure", "")).startswith(DOWN_STOP_PREFIXES[0])))
            print(f"rollback: after the kill · the receipt reads schema {rec.get('schema')}"
                  + (" whole" if whole else ", NOT WHOLE"))
            check_ok(whole, "the kill left neither schema 4 with the schema step's `down interrupted:` nor schema 3 without `steps`")
        elif plant in DOWN_KILLED_PLANTS:
            # TOOL-dSafePassage-39 AC1, AC3: killed in s2's down, after move 3 and before its verdict;
            # the reverse() below is the re-run, which must still judge s2 by its down's exit.
            if plant == "unrecorded-witness-down-killed":
                receipt = json.loads(rp.read_text(encoding="utf-8"))
                receipt["steps"] = [r for r in receipt["steps"] if r["id"] != "fx/s2"]
                rp.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
                check_ok(not derive_image_path(t, "fx/s2").exists(), "s2 has a before-image for the unrecorded plant")
            (fx / "s2.down-block").touch()
            why = run_killed([sys.executable, "-c", FIXTURE_REVERSE_CHILD, str(HERE / "upgrade_steps.py"),
                              str(gov), str(t), sha["A"]], fx, "s2", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (fx / "s2.down-block").unlink()
            s2 = next((r for r in read_receipt_steps(t) if r["id"] == "fx/s2"), {})
            held = (s2.get("state") == "applied" and s2.get("via") == "witness"
                    and str(s2.get("failure", "")).startswith(DOWN_STOP_PREFIXES[0]))
            print(f"rollback: after the kill · fx/s2 {s2.get('state')} · via {s2.get('via')} · "
                  f"{'down interrupted' if held else 'NOT down interrupted via its witness'}")
            check_ok(held, "the kill did not leave s2 applied `via` `witness` with its `down interrupted:` failure")
        rc, got, out = run_reverse()
        state = read_rows()
        if plant in (None, "unrecorded", "after-kill", "after-fail", "witness-only", "node-witness",
                     "rolled-back-witness-holds", "witness-only-reup"):
            want = (render_rolled("s4", "s3", "s2", "s1") if plant not in ("after-kill", "after-fail")
                    else ["step fx/s4 · skipped (nothing applied)"] + render_rolled("s3", "s2", "s1"))
            if plant == "rolled-back-witness-holds":
                # TOOL-dSafePassage-49 S5, AC3: s2, recorded rolled-back once derived, its witness
                # holding, is downed by move 3's `applied` record and ends rolled-back, no failure.
                check_ok("', 'fx/s2', " in out and "· then fx/s2 recorded rolled-back" in out,
                       "s2 was not recorded rolled-back after the rows were derived, s2 among them")
                check_ok(state.get("fx/s2") == ("rolled-back", None) and "Refusal" not in out and "Traceback" not in out,
                       "s2 does not end rolled-back with no failure, or a Refusal or traceback printed")
            same = read_tracked() == before
            print(f"rollback: the target's bytes {'equal' if same else 'DIFFER from'} their bytes before the walk")
            check_ok(got == want, f"the reverse walk's lines are not {want}")
            check_ok(all(state.get(f"fx/{s}", ("",))[0] == "rolled-back" for s in ("s1", "s2", "s3")),
                   "s1 to s3 do not each read rolled-back")
            check_ok(same and rc == 0, f"the bytes differ from before the walk, or the reverse walk exited {rc}")
            if plant == "unrecorded":
                check_ok("s2.down" in read_downs(), "the unrecorded s2's down did not run")
        elif plant in DOWN_KILLED_PLANTS:
            same = read_tracked() == before
            print(f"rollback: the re-run · fx/s2 {state.get('fx/s2', ('',))[0]} · bytes "
                  f"{'equal' if same else 'DIFFER from'} their bytes before the walk")
            check_ok(got == render_rolled("s2", "s1"), f"the re-run's lines are not {render_rolled('s2', 's1')}")
            check_ok(all(state.get(f"fx/{s}", ("",))[0] == "rolled-back" for s in ("s1", "s2", "s3", "s4")),
                   "s1 to s4 do not each read rolled-back")
            check_ok(same and rc == 0, f"the bytes differ from before the walk, or the re-run exited {rc}")
        elif plant in ("image-lost", "kill-after-up-image-lost"):
            n = 4 if plant == "image-lost" else 3
            text = f"{DOWN_STOP_PREFIXES[2]}; before-image .governance/steps/fx/s{n}.before.json absent"
            kept = (t / f"s{n}.txt").is_file()
            print(f"rollback: fx/s{n} {state.get(f'fx/s{n}')} · s{n}.txt {'in place' if kept else 'GONE'}")
            check_ok(got == render_rolled(*(["s4"] if n == 3 else [])) + [f"step fx/s{n} · STOPPED · {text}"],
                   f"the reverse walk did not stop at fx/s{n} naming `{text}`")
            check_ok(state.get(f"fx/s{n}") == ("applied", text) and kept,
                   f"s{n} is not kept applied with the stop, its file in place")
            check_ok(f"s{n - 1}.down" not in read_downs() and rc == 1 and "Traceback" not in out,
                   f"the reverse walk went on past the stop, or exited {rc}, or printed a traceback")
        elif plant == "partial-to":
            print(f"rollback: s1.txt and s2.txt {'present' if (t / 's1.txt').is_file() and (t / 's2.txt').is_file() else 'GONE'}")
            check_ok(got == render_rolled("s4", "s3") and read_downs() == ["s3.down", "s4.down"], "the reverse walk to B does not down only s4 and s3")
            check_ok(state.get("fx/s1", ("",))[0] == "applied" and (t / "s1.txt").is_file() and (t / "s2.txt").is_file()
                   and rc == 0, "a step introduced at or before B was downed")
        elif plant in ("down-fails", "witness-stays", "node-witness-refuses"):
            # TOOL-dSafePassage-49 S13, S16: the stop texts built from the constant, and compared
            # through the row rule, the module's one test of an opening.
            sid, text = {"down-fails": ("fx/s3", f"{DOWN_STOP_PREFIXES[1]}1: fx: s3 down fails by its plant"),
                         "node-witness-refuses": ("fx/s2", f"{DOWN_STOP_PREFIXES[1]}1: fx: s2 down fails by its plant")}.get(
                plant, ("fx/s2", DOWN_STOP_PREFIXES[2]))
            stops = [state[sid][1]] if state.get(sid, ("", None))[1] else []

            def test_stop_admitted(s: str) -> bool:
                try:
                    test_step_row(sid, "applied", s)
                    return True
                except Refusal:
                    return False
            opens = all(test_stop_admitted(s) for s in stops)
            print(f"rollback: {sid} {state.get(sid)} · stop text opens with an entry of DOWN_STOP_PREFIXES: "
                  f"{'yes' if stops and opens else 'NO'}")
            check_ok(got == (render_rolled("s4") if plant == "down-fails" else render_rolled("s4", "s3")) + [f"step {sid} · STOPPED · {text}"],
                   "the reverse walk did not stop at its failed down with the stop line")
            check_ok(state.get(sid) == ("applied", text) and stops and opens, f"{sid} does not keep applied with `{text}`")
            check_ok("s1.down" not in read_downs() and (plant != "down-fails" or "s2.down" not in read_downs()),
                   "the reverse walk went on past the stop")
            check_ok(rc == 1 and "Traceback" not in out, f"the reverse walk exited {rc}, or printed a traceback")
            if plant == "down-fails":
                (fx / "s3.down-fails").unlink()
                rc2, got2, _out2 = run_reverse()
                s4_downs = (fx / "s4.down").read_text(encoding="utf-8").split()
                print(f"rollback: the re-run · s4 downed {len(s4_downs)} time(s) in all · "
                      f"bytes {'equal' if read_tracked() == before else 'DIFFER from'} their bytes before the walk")
                check_ok(got2 == render_rolled("s3", "s2", "s1") and len(s4_downs) == 1 and rc2 == 0,
                       "the re-run did not resume at s3")
                check_ok(read_tracked() == before, "the re-run did not return the target's bytes")
        elif plant in ("schema-step", "schema-step-kill"):
            # TOOL-dSafePassage-18 AC1, AC2: the schema step's down writes no row, its verdict
            # `rolled-back` last; the killed run's re-run converges on an uninterrupted run's receipt.
            rec = json.loads(rp.read_text(encoding="utf-8"))
            verdicts = next((ln for ln in out.splitlines() if ln.startswith("rollback: verdicts ")), "")
            last = "('govkit/receipt-schema-4', 'rolled-back')"
            lowered = rec.get("schema") == 3 and "steps" not in rec
            print(f"rollback: the receipt reads schema {rec.get('schema')}"
                  + (" without steps" if lowered else " WITH steps" if "steps" in rec else "")
                  + f" · last verdict {last if verdicts.endswith(last + ']') else 'NOT the schema step rolled-back'}")
            check_ok(lowered and verdicts.endswith(last + "]"), "the receipt is not schema 3 without `steps`, or the "
                   "verdict list does not name the schema step rolled-back last")
            check_ok(got == (render_rolled("s4", "s3", "s2", "s1") if plant == "schema-step" else []),
                   "the reverse walk's fx lines are not the ones this plant downs")
            check_ok(read_tracked() == before and rc == 0 and "Traceback" not in out,
                   f"the bytes differ from before the walk, or the reverse walk exited {rc}")
            if plant == "schema-step-kill":
                t2 = build_walk_target(tmp, sha["A"], "t2", schema3=True)
                rc_w2, _o = run_fixture_child(FIXTURE_WALK_CHILD, gov, t2, sha["C"], env)
                rc2, _o = run_fixture_child(FIXTURE_REVERSE_CHILD, gov, t2, sha["A"], env)
                same = (t2 / ".governance" / "install.json").read_bytes() == rp.read_bytes()
                print(f"rollback: the re-run's receipt {'equals' if same else 'DIFFERS from'} an uninterrupted rollback's")
                check_ok(same and rc_w2 == 0 and rc2 == 0, "the re-run's receipt is not an uninterrupted rollback's")
        elif plant == "kill-after-down-stage":
            image = derive_image_path(pathlib.Path("."), "fx/s1").as_posix()
            status = run_fixture_git(t, "diff", "--cached", "--name-status").splitlines()
            deleted = {ln.split("\t", 1)[1] for ln in status if ln.startswith("D\t")}
            print(f"rollback: the re-run · git diff --cached --name-status lists D s1.txt "
                  f"{'yes' if 's1.txt' in deleted else 'NO'} · D {image} {'yes' if image in deleted else 'NO'}"
                  f" · fx/s1 {state.get('fx/s1', ('',))[0]}")
            check_ok({"s1.txt", image} <= deleted, "the re-run did not stage the removal of s1.txt and of its before-image")
            check_ok(got == render_rolled("s1") and state.get("fx/s1", ("",))[0] == "rolled-back" and rc == 0
                   and "Traceback" not in out, f"the re-run did not record fx/s1 rolled-back, or exited {rc}")
        elif plant == "kill-after-down-stage-garbled":
            image = derive_image_path(pathlib.Path("."), "fx/s1").as_posix()
            refusal = next((ln for ln in out.splitlines() if ln.startswith("rollback: refused · ")), "")
            named = image in refusal and "stage the restored paths" in refusal and "by hand" in refusal
            print(f"rollback: the re-run's refusal names the image and the restored paths to stage by hand: "
                  f"{'yes' if named else 'NO'}")
            check_ok(named and rc == 1 and "Traceback" not in out,
                   f"the re-run did not refuse naming the garbled image, or exited {rc}, or printed a traceback")
        elif plant == "schema-step-early":
            # TOOL-dSafePassage-18 AC3: s2's down lowers the receipt before the last row, so the
            # walk stops there and downs nothing it could not record.
            check_ok(got == render_rolled("s4", "s3") + [f"step fx/s2 · STOPPED · {LOWERED_STOP}"],
                   f"the reverse walk did not stop at fx/s2 naming `{LOWERED_STOP}`")
            check_ok("s1.down" not in read_downs() and rc == 1 and "Traceback" not in out,
                   f"the walk downed s1 after the lowered receipt, or exited {rc}, or printed a traceback")
        for f in fails:
            print(f"rollback: FAILED · {f}")
        return 1 if fails else rc


def run_rollback_update_fixture(plant: str | None) -> int:
    """`fixture rollback-update [--plant <case>]` (TOOL-dSafePassage-4 AC5, AC6): `build_update_gov`'s
    scratch gov with the one step `fx/s1` at B, a target updated from A to B with `s1` applied and
    committed, then `update --rollback --to A`; the refusing plants run `update` as each names. An
    unmet expectation prints `rollback-update: FAILED`; otherwise the exit is `update`'s, and 1 for
    a refusing plant whose refusal held. `retired-step` (TOOL-dSafePassage-76) lands `fx/s2` at B,
    retires it at C, and rolls back to B, which passes, then to A, which refuses."""
    with tempfile.TemporaryDirectory(prefix="gk-rbu-", ignore_cleanup_errors=True) as td:
        tmp = pathlib.Path(td)
        fails: list[str] = []
        schema = plant in ROLLBACK_UPDATE_SCHEMA_PLANTS
        killed = plant in ("schema-step-kill-before-stamp", "schema-step-kill-shipped-rows")
        shipped = plant == "schema-step-kill-shipped-rows"  # TOOL-dSafePassage-70 S2: the floor row's shape
        gov, targets, sha_a, sha_b, env = build_update_gov(
            tmp, ("t", "t2") if killed else ("t",), ("s1", "s2") if shipped or plant == "retired-step" else ("s1",), fails,
            schema3=schema or plant == "schema-up-kill", down_exit=("s2",) if shipped else ())
        t = targets["t"]
        reports, rp = t.with_name("t.fx"), t / ".governance" / "install.json"

        def check_ok(ok: bool, what: str) -> None:
            if not ok:
                fails.append(what)

        def run_govkit(*args: str) -> tuple[int, str]:
            rc, out = run_fixture_govkit(gov, env, "update", "--target", str(t), *args)
            print(out, end="")
            return rc, out

        def load_receipt() -> dict:
            return json.loads(rp.read_text(encoding="utf-8"))

        def read_spawns() -> dict[str, str]:
            return {p.name: p.read_text(encoding="utf-8") for p in reports.iterdir()} if reports.is_dir() else {}

        def load_receipt_of(tt: pathlib.Path) -> dict:
            return json.loads((tt / ".governance" / "install.json").read_text(encoding="utf-8"))

        def read_record_of(tt: pathlib.Path) -> list[str]:
            rec = tt / ".governance" / "outbox" / f"update-reverted-{sha_b[:8]}-{sha_a[:8]}.md"
            return rec.read_text(encoding="utf-8").splitlines() if rec.is_file() else []

        for tt in targets.values() if not fails and plant not in ("descendant", "schema-up-kill") else ():
            if shipped:
                # s1 applied by its witness alone, no before-image; s2's witness holds whatever the
                # target holds, as the floor row's reads the node.
                fx = tt.with_name(tt.name + ".fx")
                fx.mkdir(exist_ok=True)
                (fx / "s1.witness-absent").touch()
                (fx / "s2.witness-always").touch()
            rc0, out0 = run_fixture_govkit(gov, env, "update", "--target", str(tt), "--to", sha_b, "--write")
            got0 = {r["id"]: r["state"] for r in load_receipt_of(tt).get("steps") or []}
            check_ok(rc0 == 0 and load_receipt_of(tt).get("gov_commit") == sha_b and got0.get("fx/s1") == "applied"
                   and (not schema or got0.get("govkit/receipt-schema-4") == "applied"),
                   f"the update from A to B did not apply s1 ({rc0}): {out0[-600:]}")
            if plant == "no-base":
                rec = load_receipt()
                rec.pop("gov_commit", None)
                rp.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
            run_fixture_git(tt, "add", "-A")
            run_fixture_git(tt, "commit", "-qm", "at B")
        rc = 0
        if fails:
            pass
        elif plant == "schema-up-kill":
            # TOOL-dSafePassage-62 AC1, AC2: `update --to B --write` over the schema-3 target at A,
            # killed once the schema step's up has renamed schema 4 into place, so the walk persisted
            # no step record; the receipt written before the walk must name B's bytes for every row
            # the write loop moved, and the rollback to A from that state must return them.
            reports.mkdir(exist_ok=True)
            (reports / "schema.block-after").touch()
            why = run_killed([sys.executable, str(gov / FIXTURE_PREFIX / HERE.name / "govkit.py"), "update", "--target",
                              str(t), "--to", sha_b, "--write"], reports, "schema", env)
            check_ok(why is None, f"the kill was not staged: {why}")
            (reports / "schema.block-after").unlink(missing_ok=True)
            rec = load_receipt()
            row = next((f for f in rec.get("files") or [] if f.get("path") == "tools/demo/one.txt"), {})
            names = {sha_a: "A", sha_b: "B"}
            print(f"rollback-update: after the kill · gov_commit {names.get(rec.get('gov_commit'), rec.get('gov_commit'))} · "
                  f"tools/demo/one.txt row at {names.get(row.get('commit'), row.get('commit'))}")
            check_ok(rec.get("gov_commit") == sha_a and row.get("commit") == sha_b,
                   "the killed receipt does not name gov_commit A with the one.txt row at B's vintage")
            rc, out = run_govkit("--rollback", "--to", sha_a, "--write")
            rec, one = load_receipt(), (t / FIXTURE_PREFIX / "demo" / "one.txt").read_bytes()
            print(f"rollback-update: the rollback exits {rc} · tools/demo/one.txt {one!r} · schema {rec.get('schema')} · "
                  f"{'WITH' if 'steps' in rec else 'no'} steps · gov_commit {names.get(rec.get('gov_commit'), rec.get('gov_commit'))}")
            check_ok(rc == 0 and one == b"v1\n" and rec.get("schema") == 3 and "steps" not in rec
                   and rec.get("gov_commit") == sha_a,
                   "the rollback did not exit 0 with one.txt at v1, schema 3, no `steps` and gov_commit A")
        elif schema:
            # TOOL-dSafePassage-19 AC1: a rollback past the schema step, over a target updated from a
            # schema-3 receipt through it, stamps schema 3 with no `steps` and finishes its record.
            twin = targets["t2" if killed else "t"]
            rc_t, _o = run_fixture_govkit(gov, env, "update", "--target", str(twin), "--rollback", "--to", sha_a, "--write")
            print(_o, end="")
            rec, text = load_receipt_of(twin), read_record_of(twin)
            print(f"rollback-update: {twin.name} exits {rc_t} · schema {rec.get('schema')} · "
                  f"{'WITH' if 'steps' in rec else 'no'} steps · gov_commit "
                  f"{'A' if rec.get('gov_commit') == sha_a else rec.get('gov_commit')}")
            print("".join(f"rollback-update: record · {ln}\n" for ln in text), end="")
            check_ok(rc_t == 0 and rec.get("schema") == 3 and "steps" not in rec and rec.get("gov_commit") == sha_a,
                   "the rollback did not exit 0 with schema 3, no `steps` and gov_commit A")
            check_ok("down govkit/receipt-schema-4: rolled-back" in text and f"gov_commit: moved to {sha_a[:8]}" in text
                   and not any(ln.endswith("not finished") for ln in text),
                   "the record does not name the schema step rolled-back and the stamp moved, finished")
            rc = rc_t
            if killed:
                # AC2: `t` killed once the schema step's down has renamed schema 3 into place, before
                # the write loop moves a file row; its re-run is compared with the twin above.
                reports.mkdir(exist_ok=True)
                (reports / "schema.block-after").touch()
                why = run_killed([sys.executable, str(gov / FIXTURE_PREFIX / HERE.name / "govkit.py"), "update", "--target",
                                  str(t), "--rollback", "--to", sha_a, "--write"], reports, "schema", env)
                check_ok(why is None, f"the kill was not staged: {why}")
                (reports / "schema.block-after").unlink()
                rec, text = load_receipt(), read_record_of(t)
                print(f"rollback-update: after the kill · schema {rec.get('schema')} · "
                      f"{'WITH' if 'steps' in rec else 'no'} steps · gov_commit "
                      f"{'B' if rec.get('gov_commit') == sha_b else rec.get('gov_commit')} · record "
                      f"{'not finished' if any(ln.endswith('not finished') for ln in text) else 'FINISHED'} with "
                      f"{sum(ln.startswith('down ') for ln in text)} down line(s)")
                check_ok(rec.get("schema") == 3 and "steps" not in rec and rec.get("gov_commit") == sha_b,
                       "the killed receipt is not schema 3 with no `steps` and gov_commit unmoved")
                check_ok(any(ln.endswith("not finished") for ln in text) and not any(ln.startswith("down ") for ln in text),
                       "the killed run's record is not `not finished` with no down line")
                rc, out = run_govkit("--rollback", "--to", sha_a, "--write")
                text, twin_text = read_record_of(t), read_record_of(twin)

                def read_outside(tt: pathlib.Path) -> dict[str, bytes]:
                    got = {k: v for k, v in read_target_bytes(tt).items() if not k.startswith(".governance/outbox/")}
                    got[":index"] = b"\n".join(ln for ln in got[":index"].split(b"\n") if b"\t.governance/outbox/" not in ln)
                    return got

                a, b = read_outside(t), read_outside(twin)
                same_receipt = rp.read_bytes() == (twin / ".governance" / "install.json").read_bytes()
                files = [ln for ln in text if ln.startswith("files: ")]
                shape = (any(" · finished " in ln for ln in text) and not any(ln.endswith("not finished") for ln in text)
                         and files and files == [ln for ln in twin_text if ln.startswith("files: ")]
                         and f"gov_commit: moved to {sha_a[:8]}" in text)
                downs = [ln for ln in text if ln.startswith("down ")]
                print(f"rollback-update: the re-run exits {rc} · its receipt's bytes "
                      f"{'equal' if same_receipt else 'DIFFER from'} the twin's · the target's bytes "
                      f"{'equal' if a == b else 'DIFFER from'} the twin's"
                      + ("" if a == b else f": {sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))}")
                      + f" · the record {'has' if shape else 'LACKS'} the twin's finished shape")
                print("".join(f"rollback-update: re-run record · {ln}\n" for ln in text), end="")
                check_ok(rc == 0 and same_receipt and a == b and shape,
                       "the re-run did not exit 0 matching the twin's receipt, target bytes and finished record")
                if not shipped:
                    check_ok(downs == ["down fx/s1: skipped (nothing applied)",
                                     "down govkit/receipt-schema-4: skipped (nothing applied)"],
                           "the re-run's down lines are not the two `skipped (nothing applied)` lines")
                else:
                    # TOOL-dSafePassage-70 AC1: every line but `started` and the schema step's equals the
                    # twin's, and each fx down ran twice on `t`, the second writing nothing.
                    schema_line = "down govkit/receipt-schema-4: "
                    differ = [(x, y) for x, y in zip(text, twin_text) if x != y and not
                              (x.startswith("started ") and y.startswith("started "))]
                    same_but_schema = (len(text) == len(twin_text) and differ == [
                        (schema_line + "skipped (nothing applied)", schema_line + "rolled-back")])
                    ran = {s: len((reports / f"{s}.down").read_text(encoding="utf-8").splitlines())
                           if (reports / f"{s}.down").is_file() else 0 for s in ("s2", "s1")}
                    print(f"rollback-update: the re-run's record equals the twin's line for line "
                          f"{'except started and the schema step' if same_but_schema else f'NOT, differing in {differ}'}")
                    print(f"rollback-update: on t fx/s2's down ran {ran['s2']} time(s) · fx/s1's down ran {ran['s1']} time(s)")
                    check_ok(same_but_schema and downs == ["down fx/s2: rolled-back", "down fx/s1: rolled-back",
                                                         schema_line + "skipped (nothing applied)"],
                           "the re-run's record does not equal the twin's but for started and the schema step's line")
                    check_ok(ran == {"s2": 2, "s1": 2}, "fx/s2's and fx/s1's downs did not each run twice on t")
        elif plant is None:
            # First a rollback whose down fails: it stops before any file row moves, the stamp held.
            reports.mkdir(exist_ok=True)
            (reports / "s1.down-fails").touch()
            rc1, out1 = run_govkit("--rollback", "--to", sha_a, "--write")
            (reports / "s1.down-fails").unlink()
            record = t / ".governance" / "outbox" / f"update-reverted-{sha_b[:8]}-{sha_a[:8]}.md"
            text = record.read_text(encoding="utf-8").splitlines() if record.is_file() else []
            held = (t / FIXTURE_PREFIX / "demo" / "one.txt").read_bytes() == b"v2\n" and load_receipt().get("gov_commit") == sha_b
            print(f"rollback-update: the stopped run exits {rc1} · file rows and gov_commit "
                  f"{'held at B' if held else 'MOVED'} · record {text[-1:] or 'absent'}")
            check_ok(rc1 == 1 and held and "the rollback's reverse walk stopped at fx/s1" in out1
                   and "gov_commit: not moved, the reverse walk stopped at fx/s1" in text,
                   "a stopped reverse walk did not end the run with the rows and the stamp held, recorded")
            rc, out = run_govkit("--rollback", "--to", sha_a, "--write")
            # The down's own view of the tree: B's `one.txt` there means no file row had moved yet.
            saw = reports / "s1.down-saw"
            v2 = f"tools/demo/one.txt {hashlib.sha256(b'v2\n').hexdigest()}"
            early = saw.is_file() and v2 in saw.read_text(encoding="utf-8").splitlines()
            record = t / ".governance" / "outbox" / f"update-reverted-{sha_b[:8]}-{sha_a[:8]}.md"
            text = record.read_text(encoding="utf-8").splitlines() if record.is_file() else []
            rec, one = load_receipt(), (t / FIXTURE_PREFIX / "demo" / "one.txt").read_bytes()
            print(f"rollback-update: s1's down found tools/demo/one.txt at "
                  f"{'B, before the write loop moved it' if early else 'NOT B: a file row moved first, or no down ran'}")
            print(f"rollback-update: tools/demo/one.txt {one!r} · gov_commit "
                  f"{'A' if rec.get('gov_commit') == sha_a else rec.get('gov_commit')} · schema {rec.get('schema')} · "
                  f"record {record.name if record.is_file() else 'absent'}")
            print("".join(f"rollback-update: record · {ln}\n" for ln in text), end="")
            check_ok(early, "s1's down did not run before the write loop moved the file rows")
            check_ok(one == b"v1\n", "the file rows did not return to A's bytes")
            check_ok(rec.get("gov_commit") == sha_a and rec.get("schema") == 4,
                   "the stamp is not gov_commit A with the schema the downs left")
            check_ok("down fx/s1: rolled-back" in text and f"gov_commit: moved to {sha_a[:8]}" in text
                   and not any(ln.endswith("not finished") for ln in text), "the record does not name s1 rolled-back and the stamp moved")
            check_ok(rc == 0, f"update exited {rc}")
        elif plant == "retired-step":
            # TOOL-dSafePassage-76 AC4: C takes fx/s2 out of the steps file and names it in a
            # `[[retired]]` row; the target, updated to C, still records it applied. Introduced at B,
            # it owes no down to B and owes one to A, which no row declares.
            gkd = gov / FIXTURE_PREFIX / HERE.name
            (gkd / STEPS_FILE).write_text(render_fixture_row("s1"), encoding="utf-8", newline="\n")
            with (gkd / REGISTRY_FILE).open("a", encoding="utf-8", newline="\n") as f:
                f.write('\n[[retired]]\nid = "fx/s2"\nsuccessor = "none"\nsurfaces = []\n')
            run_fixture_git(gov, "add", "-A")
            run_fixture_git(gov, "commit", "-qm", "C")
            sha_c = run_fixture_git(gov, "rev-parse", "HEAD")
            rc_c, _o = run_govkit("--to", sha_c, "--write")
            run_fixture_git(t, "add", "-A")
            run_fixture_git(t, "commit", "-qm", "at C")
            s2 = next((r for r in load_receipt().get("steps") or [] if r.get("id") == "fx/s2"), {})
            print(f"rollback-update: updated to C · exits {rc_c} · fx/s2 {s2.get('state')}")
            check_ok(rc_c == 0 and s2.get("state") == "applied", "the update to C did not keep fx/s2 recorded applied")
            rc_b, out_b = run_govkit("--rollback", "--to", sha_b, "--write")
            run_fixture_git(t, "add", "-A")
            run_fixture_git(t, "commit", "-qm", "at B")
            rc_a, out_a = run_govkit("--rollback", "--to", sha_a, "--write")
            named = all(n in out_a for n in ("fx/s2", "[[retired]] row", "its down is owed"))
            print(f"rollback-update: update --rollback --to B --write exits {rc_b} · update --rollback --to A "
                  f"--write exits {rc_a}, naming fx/s2, its [[retired]] row and that its down is owed: "
                  f"{'yes' if named else 'NO'}")
            check_ok(rc_b == 0, f"the rollback to B, which owes fx/s2 no down, exited {rc_b}")
            check_ok(rc_a == 2 and named, f"the rollback to A, which owes fx/s2 a down, exited {rc_a} or did not say so")
            rc = 1
        elif plant == "read-only":
            before = read_spawns()
            rc, out = run_govkit("--rollback", "--to", sha_a)
            same = read_spawns() == before
            print(f"rollback-update: step spawns during the read-only run: {'none' if same else 'SOME'}")
            check_ok([ln for ln in out.splitlines() if "would roll back" in ln] == ["govkit update —   would roll back fx/s1"],
                   "the read-only run does not print `would roll back` for s1 alone")
            check_ok(same and rc == 0, "a step spawned on the read-only run, or it failed")
        else:
            args, needle = {"refused": (("--to", sha_a, "--write"), "update --rollback --to"),
                            "descendant": (("--rollback", "--to", sha_b, "--write"), "is not an ancestor of"),
                            "scoped": (("--rollback", "--kits", "demo", "--to", sha_a, "--write"), "--kits"),
                            "no-base": (("--rollback", "--to", sha_a, "--write"), "no gov_commit")}[plant]
            before, held = read_spawns(), rp.read_bytes()
            rc_g, out = run_govkit(*args)
            print(f"rollback-update: {plant} · update exits {rc_g} · receipt "
                  f"{'unchanged' if rp.read_bytes() == held else 'CHANGED'} · step spawns {'none' if read_spawns() == before else 'SOME'}")
            check_ok(rc_g == 2 and needle in out, f"update did not refuse naming `{needle}`")
            check_ok(rp.read_bytes() == held and read_spawns() == before, "a refused run changed the receipt or spawned a step")
            rc = 1
        for f in fails:
            print(f"rollback-update: FAILED · {f}")
        return 1 if fails else rc


def main(argv: list[str]) -> int:
    root = next((p for p in HERE.parents if (p / ".git").exists()), HERE.parent.parent)
    try:
        if argv and argv[0] == "list" and argv[1:] in ([], ["--window"]):
            return cmd_list(root, argv[1:] == ["--window"])
        if argv and argv[0] == "frozen" and (argv[1:] == [] or (len(argv) == 3 and argv[1] == "--base")):
            return cmd_frozen(root, argv[2] if len(argv) == 3 else None)
        if argv[:2] == ["fixture", "isolation"] and (
                len(argv) == 2 or (len(argv) == 4 and argv[2] == "--plant" and argv[3] in FIXTURE_PLANTS)):
            return run_isolation_fixture(argv[3] if len(argv) == 4 else None)
        for family, plants, run, bare in (("walk", WALK_PLANTS, run_walk_fixture, True),
                                          ("lock", LOCK_PLANTS, run_lock_fixture, False),
                                          ("update", UPDATE_PLANTS, run_update_fixture, True),
                                          ("rollback", ROLLBACK_PLANTS, run_rollback_fixture, True),
                                          ("rollback-update", ROLLBACK_UPDATE_PLANTS, run_rollback_update_fixture, True)):
            if argv[:2] == ["fixture", family] and ((bare and len(argv) == 2) or (
                    len(argv) == 4 and argv[2] == "--plant" and argv[3] in plants)):
                return run(argv[3] if len(argv) == 4 else None)
        sys.stderr.write(f"usage: python upgrade_steps.py list [--window] | frozen [--base <rev>] | "
                         f"fixture isolation [--plant {'|'.join(FIXTURE_PLANTS)}] | "
                         f"fixture walk [--plant {'|'.join(WALK_PLANTS)}] | "
                         f"fixture lock --plant {'|'.join(LOCK_PLANTS)} | "
                         f"fixture update [--plant {'|'.join(UPDATE_PLANTS)}] | "
                         f"fixture rollback [--plant {'|'.join(ROLLBACK_PLANTS)}] | "
                         f"fixture rollback-update [--plant {'|'.join(ROLLBACK_UPDATE_PLANTS)}]\n")
        return 2
    except Refusal as e:
        sys.stderr.write(f"upgrade-steps: {e}\n")
        return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
