#!/usr/bin/env python3
"""upgrade_steps — the upgrade-step kind: the step row, the succession row, their one reader, the
frozen-row check, and the two helpers a step program writes through (TOOL-dSafePassage-1).

    python <prefix>/govkit/upgrade_steps.py list               # every row, ordered, with its commit
    python <prefix>/govkit/upgrade_steps.py list --window      # each translation-window member
    python <prefix>/govkit/upgrade_steps.py frozen [--base <rev>]   # the `step-rows-frozen` leg
    python <prefix>/govkit/upgrade_steps.py fixture isolation [--plant <case>]   # the contract, observed

THE ROWS. A kit descriptor's `[[upgrade]]` rows, rows of the same grammar in
`<prefix>/govkit/steps.toml` for surfaces no descriptor owns, and the registry's `[[retired]]`
succession rows. `read_steps` and `read_retired` parse, validate and order every one of them, at a
revision or in the working tree; govkit calls them and parses no row itself. This reader is the rows'
write boundary, so it DENIES BY DEFAULT and a refusal names the file, the row and the key: an
unknown key; an authored `introduced` or `retired`; a placeholder other than `{gov}`, `{target}` and
`{prefix}`; an interpreter other than python and bash; a `{gov}/` program git does not track at the
revision read; a duplicate id; a descriptor row whose `<entry>` is not that descriptor's own id, or
a steps-file row whose `<entry>` IS a registry entry; a `surfaces` item that is not
`<class>:<name>`; and a succession row whose id is still live or whose successor is not.

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
edited `up`, `down`, `witness`, `resume` or `surfaces` reds; an edited byte of a program a landed
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
discarded silently; then it removes the image. A step program imports this file by its own path,
because the runner's `-I` drops the script directory from `sys.path`.

THE RECEIPT'S `steps` (TOOL-dSafePassage-3). A schema-4 receipt records each step's progress as
`{"id", "introduced", "state"}` rows, `state` applied, failed (adding `failure`) or rolled-back.
`set_step_state` is the only code that mutates the field and `read_step_states` the only code that
parses it; the writer persists nothing.

WHAT A STEP CAN REACH (TOOL-dSafePassage-7). `run_step_isolated` is the one spawn of a step argv:
from gov's checkout root, under an environment built from the `STEP_ENV_KEEP` allowlist and never
from a copy of the parent's, home and temp in a fresh scratch, git's system and global config
unread, `core.hooksPath` an empty directory and `credential.helper` empty through
`GIT_CONFIG_COUNT`, and a leading `python` run `-I`. A row declaring `needs-target = true` is
`attended` and spawns nothing. `check_needs_target` runs a row beside planted target hooks and
modules and reads `isolated`, `breach`, `needs-target` or `attended`; `fixture isolation` observes
all of it, a `-stub` plant swapping one half of the contract inside the fixture process only.

Exit 0 clean, 1 a frozen-row finding or no base to compare against, 2 a refused row, an unreadable
revision or a usage error. `fixture isolation` exits 0 green and 1 on a red, a `-stub` plant's,
`needs-target`'s, `breach`'s and `token`'s by design.
"""

from __future__ import annotations

import ast
import base64
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from typing import NamedTuple

HERE = pathlib.Path(__file__).resolve().parent
# Run as a program, this module is `__main__`; registering it under its own name means govkit,
# loaded later by `load_govkit`, imports THIS module rather than a second copy, so there is one
# `Refusal` class and every catcher of it catches what this file raises.
if __name__ == "__main__":
    sys.modules.setdefault("upgrade_steps", sys.modules[__name__])

INTERPRETERS = ("python", "bash")
PLACEHOLDER_RE = re.compile(r"\{(?:gov|target|prefix)\}")
STEP_KEYS = ("id", "up", "down", "witness", "resume", "surfaces", "needs-target")
RETIRED_KEYS = ("id", "successor", "surfaces")
FROZEN_FIELDS = ("up", "down", "witness", "resume", "surfaces")
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
SHA_RE = re.compile(r"[0-9a-f]{40}")
# THE ISOLATION CONTRACT's allowlist (TOOL-dSafePassage-7): the names process creation and Python's
# start-up need, none carrying a credential. Every other name, `GIT_ENV_LEAKS` and every token
# variable included, falls out because nothing copies it in; a name joins by a reviewed edit.
STEP_ENV_KEEP = ("PATH", "PATHEXT", "SYSTEMROOT", "SYSTEMDRIVE", "WINDIR", "COMSPEC", "OS",
                 "PROCESSOR_ARCHITECTURE", "NUMBER_OF_PROCESSORS", "LANG", "LC_ALL", "TZ")
STEP_PHASES = ("up", "down", "witness", "resume")
# Where `check_needs_target` gathers canaries: inside the scratch tree it is handed, so a target
# module planted beside the plants can name its own canary by its own path.
CANARY_DIR = ".gk-canaries"
# Every client-side hook name git runs; a name git adds later is unplanted until it is listed here.
CLIENT_HOOKS = ("applypatch-msg", "pre-applypatch", "post-applypatch", "pre-commit",
                "pre-merge-commit", "prepare-commit-msg", "commit-msg", "post-commit", "pre-rebase",
                "post-checkout", "post-merge", "pre-push", "pre-auto-gc", "post-rewrite",
                "sendemail-validate", "fsmonitor-watchman", "p4-changelist", "p4-prepare-changelist",
                "p4-post-changelist", "p4-pre-submit", "post-index-change", "reference-transaction")
FIXTURE_PLANTS = ("hook", "hook-stub", "module", "module-stub", "credential", "credential-stub",
                  "needs-target", "breach", "token", "callers")


class Refusal(RuntimeError):
    """A condition that stops govkit before it reads or writes anything further."""


class StepRow(NamedTuple):
    """One `[[upgrade]]` row, validated. `introduced` is a commit, `unlanded`, or None where the
    caller asked for no derivation; `file` is repo-relative and `row` 1-based within that file."""
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
    entries = []
    for e in parse_table_rows(text, rel, "entry", where):
        if isinstance(e.get("id"), str) and isinstance(e.get("descriptor"), str):
            entries.append((e["id"], gk.resolve_prefix_token(e["descriptor"], tr)))
    return tr, rel, parse_table_rows(text, rel, "retired", where), entries


def check_argv(value, at: str, tr: str, where: str, read_tracked) -> list:
    """`value` as a validated argv, else a refusal naming `at` (file, row and key): non-empty
    strings, `argv[0]` an interpreter the runner resolves, only the three placeholders, and every
    `{gov}/` program a file `read_tracked()` names, git's tracked set at the revision read."""
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
    None and the order is declaration order."""
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
                check_argv(d[k], f"{at} key {k}", tr, where, read_tracked)
            resume = d.get("resume")
            if resume is not None and resume != "atomic":
                check_argv(resume, f"{at} key resume", tr, where, read_tracked)
            if "surfaces" not in d:
                raise Refusal(f"{at} key surfaces: required, possibly empty, so an absence is declared")
            check_surfaces(d["surfaces"], f"{at} key surfaces")
            if not isinstance(d.get("needs-target"), bool):
                raise Refusal(f"{at} key needs-target: required, true or false")
            rows.append(StepRow(sid, d["up"], d["down"], d["witness"], resume, d["surfaces"],
                                d["needs-target"], rel, n, None))
    if landed_ref is None:
        return rows
    hit = derive_introduced(root, landed_ref, [rel for rel, _e in files], "upgrade", [r.id for r in rows])
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
                      ids: list[str]) -> dict[str, tuple[str, int]]:
    """{id: (commit, first-parent position)} for each of `ids` a `[[<table>]]` row of `files` holds on
    `landed_ref`'s first-parent line: the oldest commit whose change against its first parent left a
    holding blob. One `git log` names the changed blobs oldest first, one `cat-file --batch` reads
    them, a blob is parsed only where it spells a wanted id, and the walk stops at the last hit."""
    want, found = set(ids), {}
    if not (landed_ref and want and files):
        return found
    log = run_git(root, "log", "--first-parent", "--reverse", "--diff-merges=first-parent", "--raw",
                  "--no-abbrev", "--no-renames", "--format=%x00%H", landed_ref, "--", *files)
    if log is None:
        raise Refusal(f"git log over {landed_ref} failed in {pathlib.Path(root).as_posix()}")
    cat = subprocess.Popen(["git", "-C", str(root), "cat-file", "--batch"],
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        for pos, chunk in enumerate(log.decode("utf-8", "replace").split("\0")[1:]):
            lines = chunk.strip("\n").split("\n")
            for ln in lines[1:]:
                if not ln.startswith(":"):
                    continue
                blob = ln.split("\t", 1)[0].split()[3]
                if not blob.strip("0"):
                    continue  # a deletion leaves no blob to hold a row
                cat.stdin.write(blob.encode("ascii") + b"\n")
                cat.stdin.flush()
                head = cat.stdout.readline().split()
                if len(head) < 3:
                    continue
                text = cat.stdout.read(int(head[2]) + 1)[:-1].decode("utf-8", "replace")
                hits = [i for i in want if f'"{i}"' in text]
                if not hits:
                    continue
                try:
                    held = {r.get("id") for r in tomllib.loads(text.removeprefix("\ufeff")).get(table) or []
                            if isinstance(r, dict)}
                except (tomllib.TOMLDecodeError, AttributeError):
                    continue  # an unparsable vintage holds no row
                for i in hits:
                    if i in held:
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
        for argv in (row.up, row.down, row.witness, row.resume if isinstance(row.resume, list) else []):
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
    return pathlib.Path(target) / IMAGE_DIR / m[1] / f"{m[2]}.before.json"


def check_contained(target, rel: str) -> pathlib.Path:
    """`target`/`rel`, refused where `rel` is absolute or climbs out of the target."""
    pp = pathlib.PurePosixPath(rel)
    if pp.is_absolute() or ".." in pp.parts or ":" in rel:
        raise Refusal(f"'{rel}' is not a path inside the target, so no step may write it")
    return pathlib.Path(target) / rel


def write_before_image(target, step_id: str, derive_after) -> dict[str, bytes | None]:
    """The after-state `{path: bytes, or None for removed}` of `step_id`'s up at `target`, with its
    before-image written first.

    With no image, `derive_after(None)` runs the step's pre-write reads against the working tree and
    names every path it will write or remove; the image then records each path's working-tree bytes
    and the sha256 of what the up leaves. An image already there is never overwritten:
    `derive_after` is handed its before bytes instead, and its answer must hash to the image's
    after-hashes, so a re-run over a killed up converges on the first image or refuses."""
    image = derive_image_path(target, step_id)
    if image.is_file():
        held = json.loads(image.read_text(encoding="utf-8"))["paths"]
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
    image.write_text(json.dumps({"step": step_id, "paths": paths}, indent=2, sort_keys=True) + "\n",
                     encoding="utf-8", newline="\n")
    return after


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
    a list of `{"id", "introduced", "state"}` objects, `state` one of STEP_STATES, a `failed` row
    adding a non-empty `failure`, an `applied` row a down stopped on adding one that opens with an
    entry of DOWN_STOP_PREFIXES (TOOL-dSafePassage-43), a `rolled-back` row carrying none,
    `introduced` a 40-hex commit or null. Anything else is a refusal naming the row, and nothing
    is repaired."""
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
        stopped = state == "applied" and "failure" in row
        want = {"id", "introduced", "state"} | ({"failure"} if state == "failed" or stopped else set())
        if set(row) != want:
            raise Refusal(f"{at} carries the keys {sorted(row)}, where a {state!r} row carries {sorted(want)}")
        if not isinstance(row["id"], str) or not row["id"]:
            raise Refusal(f"{at}: `id` is not a non-empty string")
        if state not in STEP_STATES:
            raise Refusal(f"{at}: `state` {state!r} is not one of {', '.join(STEP_STATES)}")
        fail = row.get("failure")
        if (state == "failed" or stopped) and not (
                isinstance(fail, str) and fail and (not stopped or fail.startswith(DOWN_STOP_PREFIXES))):
            raise Refusal(f"{at}: an applied row's `failure` {fail!r} opens with none of the down stops "
                          f"{', '.join(map(repr, DOWN_STOP_PREFIXES))}, and an applied row carries only "
                          f"a stopped down's" if stopped else f"{at}: a failed row's `failure` is a non-empty string")
        intro = row["introduced"]
        if intro is not None and not (isinstance(intro, str) and SHA_RE.fullmatch(intro)):
            raise Refusal(f"{at}: `introduced` {intro!r} is neither a 40-hex commit nor null")
    return steps


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


def set_step_state(receipt: dict, step_id, introduced, state, failure=None) -> dict:
    """Record `step_id` at `state` in the receipt's `steps`: the field's one writer (S3).

    The row moves to the end, so the last `applied` row is the last completed step; a known
    `introduced` survives a call passing None. It refuses a receipt `test_steps_recordable`
    rejects and any row `read_step_states` would refuse, mutates `receipt` and persists nothing:
    the caller writes it.

    The bootstrap: before schema 4 no step row is persisted, so a step's failure or interruption
    on such a receipt goes to `update`'s output and findings only; the `govkit/receipt-schema-4`
    row is written after that step's post-spawn re-read shows schema 4, through this writer, like
    any other row (TOOL-dSafePassage-16).

    `introduced` is the reader's value as `read_steps` returns it: `resolve_recorded_introduced`
    maps it first, so the reader's `unlanded` records null (TOOL-dSafePassage-20)."""
    introduced = resolve_recorded_introduced(introduced)
    schema = receipt.get("schema", 1)
    if not test_steps_recordable(receipt):
        raise Refusal(f"a receipt at schema {schema!r} has no `steps` to record '{step_id}' in: a "
                      f"step row is recorded only where `schema` is a number of 4 or more and "
                      f"`steps` is a list; the step govkit/receipt-schema-4 takes it to schema 4 first")
    row = {"id": step_id, "introduced": introduced, "state": state}
    if failure is not None:
        row["failure"] = failure
    rows = read_step_states(receipt)
    old = next((r for r in rows if r["id"] == step_id), None)
    if introduced is None and old is not None:
        row["introduced"] = old["introduced"]
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


def build_step_env(scratch) -> dict[str, str]:
    """The environment a step runs under (TOOL-dSafePassage-7, S1): a NEW dict of the
    `STEP_ENV_KEEP` names present in the parent, plus the contract's own. Home and temp point into
    `scratch`; git reads no system or global config and prompts for nothing, and through
    `GIT_CONFIG_COUNT`, which outranks the target's own config, runs hooks from the empty
    `<scratch>/hooks` and holds the empty credential helper."""
    scratch = pathlib.Path(scratch)
    env = {k: os.environ[k] for k in STEP_ENV_KEEP if k in os.environ}
    env.update(dict.fromkeys(("HOME", "USERPROFILE", "APPDATA", "LOCALAPPDATA", "XDG_CONFIG_HOME"),
                             str(scratch / "home")))
    env.update(dict.fromkeys(("TMP", "TEMP", "TMPDIR"), str(scratch / "tmp")))
    env.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull, "GIT_TERMINAL_PROMPT": "0",
                "GCM_INTERACTIVE": "never", "GIT_CONFIG_COUNT": "2",
                "GIT_CONFIG_KEY_0": "core.hooksPath", "GIT_CONFIG_VALUE_0": str(scratch / "hooks"),
                "GIT_CONFIG_KEY_1": "credential.helper", "GIT_CONFIG_VALUE_1": ""})
    return env


def resolve_step_argv(argv, ctx: dict[str, str], step_id: str = "a step") -> list[str]:
    """`argv` resolved for the contract (S2): `{gov}`, `{target}` and `{prefix}` from `ctx` through
    govkit's `resolve_tokens`, a leading `python` as govkit's own interpreter and `-I`, a leading
    `bash` through `resolve_shell_argv`. A token `ctx` does not answer is a refusal naming the step
    and the token, before any spawn."""
    gk, out = load_govkit(), []
    for tok in argv:
        got, missing = gk.resolve_tokens(tok, ctx)
        if missing:
            raise Refusal(f"{step_id}: '{tok}' holds {', '.join('{' + m + '}' for m in missing)}, which "
                          f"this run does not answer, so nothing was spawned")
        out.append(got)
    if out and out[0] == "python":
        return [sys.executable, "-I", *out[1:]]
    return gk.resolve_shell_argv(out)


def derive_step_mode(row: StepRow) -> str:
    """`attended` for a row declaring `needs-target = true`, which no runner spawns, else
    `isolated`: the row runs under the contract."""
    return "attended" if row.needs_target else "isolated"


def run_step_isolated(row: StepRow, phase: str, target, gov_root) -> dict:
    """Run `phase` of `row` under the contract: the step kind's ONE spawn of a step argv (S3), so the
    walk, the reverse walk, gov first and the leg inherit the contract by calling it.

    From gov's checkout root, with `build_step_env` over a scratch made for the call and cleared
    after it, and `resolve_step_argv`'s argv; output decoded as `run_target_argv` decodes it.
    Returns `{"verdict": "ok" | "failed" | "attended", "rc", "tail"}`, `tail` stderr's last 20
    lines. A row that needs target code is `attended` and spawns nothing; a spawn error is
    `failed` with `rc` None; a phase with no argv is a refusal."""
    if derive_step_mode(row) == "attended":
        return {"verdict": "attended", "rc": None, "tail": ""}
    if phase not in STEP_PHASES or not isinstance(getattr(row, phase), list):
        raise Refusal(f"{row.id}: no `{phase}` argv to run; a step runs one of {', '.join(STEP_PHASES)}")
    gk = load_govkit()
    target, gov_root = pathlib.Path(target).resolve(), pathlib.Path(gov_root).resolve()
    tr = gk.derive_tool_root(gov_root)
    ctx = {"gov": (gov_root / tr if tr else gov_root).as_posix(), "target": target.as_posix()}
    if (target / ".governance" / "deploy.toml").is_file():
        ctx["prefix"] = gk.target_context(target, gk.load_deploy(target), row.id.split("/", 1)[0], {})["prefix"]
    with tempfile.TemporaryDirectory(prefix="gk-step-", ignore_cleanup_errors=True) as td:
        for d in ("home", "tmp", "hooks"):
            (pathlib.Path(td) / d).mkdir()
        try:
            p = subprocess.run(resolve_step_argv(getattr(row, phase), ctx, row.id), cwd=str(gov_root),
                               env=build_step_env(td), stdin=subprocess.DEVNULL, capture_output=True,
                               text=True, encoding="utf-8", errors="replace")
        except OSError as e:
            return {"verdict": "failed", "rc": None, "tail": f"{row.id} {phase}: could not spawn: {e}"}
    return {"verdict": "ok" if p.returncode == 0 else "failed", "rc": p.returncode,
            "tail": "\n".join(p.stderr.splitlines()[-20:])}


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


def load_govkit():
    """The deployer beside this file: the running module where it is the program, else imported by
    its path. Only the CLI asks for it — the remote ladder and the push base are govkit's."""
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


def cmd_list(root, window: bool) -> int:
    """`list [--window]`: every row in order with its introducing commit and declaring file, the
    succession rows after them; or, under `--window`, each home a step row's `surfaces` declares,
    `open` or `closed by <step id>`. The landed ref is the remote ladder's default branch."""
    gk = load_govkit()
    remote, branch, _observed, refusal = gk.resolve_remote(root)
    if refusal:
        raise Refusal(refusal)
    branch = branch or "main"
    landed = next((ref for ref in ((f"{remote}/{branch}", branch) if remote else (branch,))
                   if run_git(root, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")), None)
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
    sha, _boundary, why = load_govkit().derive_push_base(root, base)
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
    def reads_phase(n) -> bool:
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
            if argv is None or not any(reads_phase(n) for n in ast.walk(argv)):
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
        "cred = subprocess.run(['git', 'credential', 'fill'], capture_output=True, timeout=60,\n"
        "                      input=b'protocol=https\\nhost=gk-step.invalid\\n\\n')\n"
        "helpers = subprocess.run(['git', '-C', target, 'config', '--get-all', 'credential.helper'],\n"
        "                         capture_output=True, text=True)\n"
        "hooks = os.environ.get('GIT_CONFIG_VALUE_0', '')\n"
        "with open(os.path.join(reports, 'clean.json'), 'w', encoding='utf-8') as f:\n"
        "    json.dump({'env': sorted(os.environ), 'count': os.environ.get('GIT_CONFIG_COUNT'),\n"
        "               'key0': os.environ.get('GIT_CONFIG_KEY_0'),\n"
        "               'hooks': sorted(os.listdir(hooks)) if os.path.isdir(hooks) else None,\n"
        "               'isolated': sys.flags.isolated, 'cwd': os.getcwd(), 'prefix': prefix,\n"
        "               'add': add.returncode, 'cred': cred.returncode,\n"
        "               'helpers': helpers.stdout.splitlines()}, f)\n"),
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
    saved = {k: g[k] for k in ("build_step_env", "resolve_step_argv")}
    for k in [k for k in os.environ if k.upper().startswith("GIT_")]:
        del os.environ[k]  # a calling hook's GIT_DIR would point every fixture git call elsewhere
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
    (gov / "tools" / "steps").mkdir(parents=True)
    (gov / "tools" / HERE.name).mkdir()
    (gov / "tools" / HERE.name / REGISTRY_FILE).write_text("", encoding="utf-8")
    for name, text in FIXTURE_STEPS.items():
        (gov / "tools" / "steps" / name).write_text(text, encoding="utf-8", newline="\n")
    reports.mkdir()
    quiet = build_tree_git_env()
    subprocess.run(["git", "init", "-q", str(target)], env=quiet, capture_output=True, check=True)
    (target / ".governance").mkdir()
    (target / ".governance" / "deploy.toml").write_text('prefix = "tools"\n', encoding="utf-8")
    (target / "adopter_only.py").write_text(FIXTURE_ADOPTER_ONLY, encoding="utf-8", newline="\n")
    witness = ["python", "-c", "import os, sys; sys.exit(not os.path.isfile(sys.argv[1]))", "{target}/stepped.txt"]

    def row(slug: str, up: list, needs: bool = False) -> StepRow:
        return StepRow(f"fixture/{slug}", up, ["python", "-c", "pass"], witness, "atomic", [], needs,
                       "fixture", 1, None)

    clean = row("clean", ["python", "{gov}/steps/clean.py", "{target}", "{prefix}", reports.as_posix()])
    report = reports / "clean.json"
    fails: list[str] = []

    def expect(ok: bool, what: str) -> None:
        if not ok:
            fails.append(what)

    def run_clean() -> dict:
        r = run_step_isolated(clean, "up", target, gov)
        print(f"isolation: {clean.id} · up · {r['verdict']}" + (f" · rc {r['rc']}: {r['tail']}" if r["verdict"] != "ok" else ""))
        try:
            return json.loads(report.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}  # no report, or one a shadowed `json` left empty: read as nothing reported

    def drop_pair(env: dict, key: str) -> dict:
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
        # The contract's own names are what the builder returns over an EMPTY parent: a builder
        # that copies the parent adds nothing there, so the oracle is not the code under test.
        held = dict(os.environ)
        os.environ.clear()
        try:
            allowed = set(STEP_ENV_KEEP) | set(contract_env(tmp))
        finally:
            os.environ.update(held)
        extra = sorted(set(rep.get("env", [])) - allowed)
        print(f"isolation: {clean.id} · env names outside the allowlist and the contract: {extra or 'none'}")
        print(f"isolation: {clean.id} · GIT_CONFIG_COUNT {rep.get('count')} · {rep.get('key0')} holds "
              f"{rep.get('hooks')} · sys.flags.isolated {rep.get('isolated')} · cwd {rep.get('cwd')}")
        expect(bool(rep) and rep.get("add") == 0, "clean's report is missing, or its git add failed")
        expect(not extra, f"names outside the allowlist reached the step: {extra}")
        expect(rep.get("count") == "2" and rep.get("key0") == "core.hooksPath" and rep.get("hooks") == [],
               "GIT_CONFIG_COUNT is not 2 with core.hooksPath naming an empty directory")
        expect(rep.get("isolated") == 1, "the leading python ran without -I")
        expect(bool(rep) and pathlib.Path(rep["cwd"]).resolve() == gov.resolve(), "the working directory is not gov's root")
        expect(rep.get("prefix") == "tools", "{prefix} did not resolve to the target's install prefix")
        expect(check_needs_target(clean, target, gov) == "isolated", "clean does not read isolated")
    elif plant in ("hook", "hook-stub"):
        subprocess.run(["git", "-C", str(target), "config", "core.hooksPath", ".githooks"], env=quiet, check=True)
        planted = write_target_plants(target, canaries)
        expect(all(any(p.endswith(f".githooks/{h}") for p in planted) for h in ("post-index-change", "pre-commit")),
               "no post-index-change and pre-commit planted under the target's own core.hooksPath")
        if plant == "hook-stub":
            g["build_step_env"] = lambda scratch: drop_pair(saved_build(scratch), "core.hooksPath")
        rep = run_clean()
        expect(rep.get("add") == 0, "clean's git add did not run")
        hit = [c for c in read_plant_canaries(canaries) if c.startswith("hook-")]
        print(f"isolation: hook canary: {'present · ' + ', '.join(hit) if hit else 'absent'}")
        rc = 1 if hit else 0
    elif plant in ("module", "module-stub"):
        write_target_plants(target, canaries)
        os.environ["PYTHONPATH"] = str(target)
        if plant == "module-stub":
            saved_argv = g["resolve_step_argv"]
            g["build_step_env"] = lambda scratch: dict(os.environ)
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
            g["build_step_env"] = lambda scratch: {**drop_pair(saved_build(scratch), "credential.helper"),
                                                   "GIT_CONFIG_GLOBAL": os.environ["GIT_CONFIG_GLOBAL"],
                                                   "GH_TOKEN": os.environ["GH_TOKEN"]}
        rep = run_clean()
        hit = read_plant_canaries(canaries)
        token = "GH_TOKEN" in rep.get("env", [])
        print(f"isolation: credential canary: {'present · ' + ', '.join(hit) if hit else 'absent'}")
        print(f"isolation: token: {'present · GH_TOKEN reached the step' if token else 'absent'}")
        print(f"isolation: git credential fill exits {rep.get('cred')} · credential.helper reads {rep.get('helpers')}")
        expect(bool(rep) and rep.get("cred") != 0, "git credential fill did not exit non-zero")
        if plant == "credential":
            expect(rep.get("helpers") == [""], "credential.helper does not read only the empty value")
        rc = 1 if hit or token else 0
    elif plant == "needs-target":
        ran = reports / "ran-reaches-attended"
        reaches = row("reaches", ["python", "{gov}/steps/reaches.py", (reports / "ran-reaches").as_posix()])
        attended = row("reaches-attended", ["python", "{gov}/steps/reaches.py", ran.as_posix()], True)
        expect(check_needs_target(reaches, target, gov) == "needs-target", "reaches does not read needs-target")
        expect((reports / "ran-reaches").is_file(), "reaches never ran, so its needs-target reads nothing")
        expect(check_needs_target(attended, target, gov) == "attended", "the declaring copy does not read attended")
        print(f"isolation: {attended.id} · own canary {'present: it spawned' if ran.exists() else 'absent'}")
        expect(not ran.exists(), "an attended row spawned")
        rc = 1
    elif plant == "breach":
        opens = row("opens", ["python", "{gov}/steps/opens.py", "{target}"])
        expect(check_needs_target(opens, target, gov) == "breach", "opens does not read breach")
        rc = 1
    elif plant == "token":
        tok = row("token", ["python", "{gov}/steps/clean.py", "{unknown}", "{prefix}", reports.as_posix()])
        try:
            run_step_isolated(tok, "up", target, gov)
            expect(False, "a row holding {unknown} was not refused")
        except Refusal as e:
            print(f"isolation: {tok.id} · refused · {e}")
        expect(not report.exists(), "the row holding {unknown} spawned")
        rc = 1
    for f in fails:
        print(f"isolation: FAILED · {f}")
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
        sys.stderr.write(f"usage: python upgrade_steps.py list [--window] | frozen [--base <rev>] | "
                         f"fixture isolation [--plant {'|'.join(FIXTURE_PLANTS)}]\n")
        return 2
    except Refusal as e:
        sys.stderr.write(f"upgrade-steps: {e}\n")
        return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
