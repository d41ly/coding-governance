#!/usr/bin/env python3
"""govkit — the mechanical deployer.

Contract: the deployer unit's spec under memory/builds/aSealedCaravan/spec/

WHAT THIS FILE DOES TODAY, AND WHAT IT DOES NOT. The verbs are `selfcheck`, the read-only `plan`,
`check`, `update` and `adopt`, the writing `apply` / `apply --resume`, and `intake`. THE COUNT IS
NOT SPELLED HERE and the list is not a second source: `USAGE` and `main`'s dispatch tuple own it
between them, a selftest arm joins the two, and the sentence that used to say "all five" was wrong
from the commit that landed the sixth. What it does NOT do is stated on every run
rather than left to be discovered — see the two SKIPPED lines `apply` prints. A subcommand that
parses and does nothing is indistinguishable, from the outside, from one that works, and this unit
exists because that class of silence ships broken installs.

`apply` lands the roles it can honour and REFUSES the ones it cannot, by name. Two steps of S5's hard
order have no implementation anywhere in this repo — writing a gov-owned region into a target-owned
file, and emitting a leg into the target's own gate runner — and both are REPORTED on every run
rather than skipped quietly. A deployer that says nothing about what it did not do is the failure
this unit was built to end.

`selfcheck` is the ratchet. Its most load-bearing arm is the SURFACE predicate (spec S12): every
tracked path in the declared surface is an entry, a member of exactly one entry's file rules, or an
exemption with a reason. The spec states no population count anywhere on purpose — it stated two
across its life and both were true when measured and false when read — so this is where a count is
allowed to exist, derived, once, at the moment it is checked.

EVERY REFUSAL PRINTS ITS OWN MESSAGE AND IS COUNTED. Exit 0 clean, 1 findings, 2 misconfigured.
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import time

KIT_GOVKIT_VERSION = "1.9"  # gov:kit govkit@1.9 — kit identity; set HERE, never from a conf

RECEIPT_SCHEMA = 3  # bumped by any unit that adds a per-role row field; readers accept 1, 2 and 3

# The hard order's step ids, RESERVED here in one ordered tuple — including the steps this engine
# does not perform yet. A step id is data, not a print: the ordering criterion is an assertion about
# ORDER, and before this there was nothing stable to order. Later units FILL steps and may never
# rename one. The owning unit per id is a table in this build's spec set; no count of
# them is written anywhere, because a count in prose is what this build spends a unit removing.
STEP_BASELINE = "BASELINE"
STEP_ATTRIBUTES = "ATTRIBUTES"
STEP_LAND = "LAND"
STEP_STAGE = "STAGE"
STEP_HOOKPROBE = "HOOKPROBE"
STEP_CONFIGURE = "CONFIGURE"
STEP_OBSERVE = "OBSERVE"
STEP_RENORMALIZE = "RENORMALIZE"
STEP_LEGS = "LEGS"
STEP_AFTER = "AFTER"
STEP_RECEIPT = "RECEIPT"
STEPS = (STEP_BASELINE, STEP_ATTRIBUTES, STEP_LAND, STEP_STAGE, STEP_HOOKPROBE, STEP_CONFIGURE,
         STEP_OBSERVE, STEP_RENORMALIZE, STEP_LEGS, STEP_AFTER, STEP_RECEIPT)


def step(name: str, detail: str = "") -> None:
    """Print one phase line carrying its step id. Refuses an id outside the reserved tuple."""
    if name not in STEPS:
        raise Refusal(f"'{name}' is not a reserved step id; the tuple is the vocabulary")
    print(f"govkit apply — [{STEPS.index(name) + 1}/{name}]" + (f" {detail}" if detail else ""))

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - the message is the product on an old interpreter
    sys.stderr.write(
        "govkit: this tool needs tomllib (CPython 3.11+). The descriptors are TOML and there is no\n"
        "govkit: vendored parser: a second TOML dialect is a second source of truth about the same\n"
        "govkit: files, which is the defect class this unit exists to close.\n"
    )
    raise SystemExit(2)


class Refusal(RuntimeError):
    """A condition that stops govkit before it reads or writes anything further."""


# ---------------------------------------------------------------------------- repo + git plumbing
def repo_root() -> pathlib.Path:
    """The gov checkout this file lives in.

    Walk UP for the registry rather than asking git. Two reasons, both measured in this repo. A
    `git -C <dir> rev-parse --show-toplevel` returns <dir> itself when an absolute GIT_DIR is
    inherited — which is what git exports to a merge driver in a linked worktree, and it is exactly
    how the row-keyed merge driver was found to be inert here. And a fixed number of `parents[]` is
    correct only at one install prefix. The walk is correct at any prefix and inherits nothing.
    """
    here = pathlib.Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "tools" / "govkit" / "registry.toml").is_file():
            return parent
    raise Refusal(
        f"no tools/govkit/registry.toml above {here.as_posix()} — govkit reads its population from "
        f"the registry and has no directory-listing fallback, by design"
    )


def git(root: pathlib.Path, *args: str) -> str:
    out = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True, check=False
    )
    if out.returncode != 0:
        raise Refusal(f"git {' '.join(args)} failed in {root.as_posix()}: {out.stderr.strip()}")
    return out.stdout


def tracked(root: pathlib.Path) -> list[str]:
    return [p for p in git(root, "ls-files", "-z").split("\0") if p]


# ------------------------------------------------------------------------------------- the model
def load_toml(path: pathlib.Path) -> dict:
    try:
        with path.open("rb") as fh:
            return tomllib.load(fh)
    except FileNotFoundError as e:
        raise Refusal(f"no such descriptor: {path.as_posix()}") from e
    except tomllib.TOMLDecodeError as e:
        raise Refusal(f"{path.as_posix()} is not valid TOML: {e}") from e


def surface_paths(root: pathlib.Path, globs: list[str]) -> set[str]:
    """Tracked paths inside the declared surface, as repo-relative posix strings.

    `tools/*` means depth-1 entries under tools/ — a FILE at depth 1, or the directory a deeper
    tracked path sits in. Quantifying over directories alone is precisely the predicate this
    replaces: it left every single-file deployable the runbook prescribes in no population at all.
    """
    out: set[str] = set()
    files = tracked(root)
    for g in globs:
        if g.endswith("/*"):
            prefix = g[:-2] + "/"
            for f in files:
                if not f.startswith(prefix):
                    continue
                rest = f[len(prefix):]
                out.add(prefix + rest.split("/", 1)[0])
        elif g.endswith("/**"):
            prefix = g[:-3] + "/"
            out.update(f for f in files if f.startswith(prefix))
        else:
            rx = re.compile("^" + re.escape(g).replace(r"\*", "[^/]*") + "$")
            out.update(f for f in files if rx.match(f))
    return out


def rule_sources(desc: dict, rule: dict) -> list[str]:
    """The repo-relative source paths a file rule names, globs excluded.

    `root_relative` exists because one entry's bytes straddle two trees: the lander lives under the
    install prefix and its hook lives at a verbatim repo-root path with no prefix at all. Resolving
    every include against `home` put that hook under `tools/`, where it does not exist — caught by
    this gate's own first run, which is the point of running a new predicate over the real tree
    before trusting it.
    """
    home = (desc.get("home") or "").rstrip("/")
    inc = rule.get("include")
    srcs = inc if isinstance(inc, list) else ([inc] if inc else [])
    out = []
    for s in srcs:
        if not s or any(ch in s for ch in "*?["):
            continue
        out.append(s if rule.get("root_relative") or not home else f"{home}/{s}")
    return out


def rule_relpath(desc: dict, rule: dict, src: str) -> str:
    """`{relpath}` — the source relative to the RULE'S BASE, which is not always its basename.

    The base is the repo root for a `root_relative` rule and the entry's `home` otherwise. Resolving
    it through the basename instead is a measured defect: push-main's hook rule declares
    `to = "{relpath}"` over `.githooks/pre-push`, so the destination resolved to a bare `pre-push` at
    the target ROOT while the same rule's own `claims` spelled `.githooks/pre-push` — two spellings of
    one destination inside one rule, and the wrong one is the one that would have been written.
    """
    home = (desc.get("home") or "").rstrip("/")
    if rule.get("root_relative") or not home:
        return src
    if src.startswith(home + "/"):
        return src[len(home) + 1:]
    return pathlib.PurePosixPath(src).name


def destinations_for(desc: dict, rule: dict, src: str) -> list[str]:
    """The destination template(s) ONE source reaches under this rule. Tokens unresolved.

    An explicit `to` WINS for every role; the kit-relative form is the default only where the rule
    declared no destination. Defaulting regardless is how a flat entry — one with no kit directory at
    all — silently lands under a directory it does not have.
    """
    to = rule.get("to")
    rel = rule_relpath(desc, rule, src)
    if not to:
        return ["{kit}/" + rel]
    dests = to if isinstance(to, list) else [to]
    return [d.replace("{relpath}", rel) for d in dests]


def rule_destinations(desc: dict, rule: dict) -> list[str]:
    """Every destination template a rule writes, over the sources it names literally.

    `to` is a LIST because one source can reach two places — the hook that must exist both as a kit
    copy and as a wired copy, whose parity arm fails outright when the wired one is absent. A rule
    naming no literal source still declares its destination: a delegated rule has no gov bytes and is
    written by an adopter, and returning nothing for it would hide the destination from every
    consumer that reasons about what a kit puts in a target.
    """
    to = rule.get("to")
    if not to:
        return []
    srcs = rule_sources(desc, rule)
    if not srcs:
        dests = to if isinstance(to, list) else [to]
        return [d for d in dests if "{relpath}" not in d]
    out: list[str] = []
    for s in srcs:
        out.extend(destinations_for(desc, rule, s))
    return list(dict.fromkeys(out))


# ------------------------------------------------------------------------------------ the resolver
# Roles `apply` can land. `project-owned` is deliberately NOT here: it is a SOURCE-level carve-out,
# not a writer, and after the playbook entry was retagged `seed` no rule in the tree needs
# write-if-absent semantics. Adding the branch would be a widening nothing exercises.
LANDABLE_ROLES = ("engine", "seed")

# Why a role does not land, and WHO produces it instead. Every unlanded rule prints one of these.
# There is no path out of the land loop that says nothing: the silent skip this replaces swallowed
# thirteen rules across the shipped descriptors, and a role dropped without a word is
# indistinguishable from a role that landed.
UNLANDED_REASON = {
    "project-owned": "the target authors it — gov supplies no bytes for this source, ever",
    "generated": "produced in the target by its own tooling, never carried across",
    "rendered": "written by this kit's own adopter; a second renderer would race the real one",
    "merged": "a gov-owned region inside a target-owned file — no writer exists yet",
    # DEPL-dCarriedReceipt-10 S3. gov's copy is a DERIVATIVE of the target's, so gov's bytes are
    # wrong for that target BY CONSTRUCTION and are wrong there whether or not the target's own copy
    # is absent. This line is what makes `selfcheck` arm 7g demand an `UPDATE_ROLE` row for the role
    # without that demand being written a second time: 7g's `known_roles` is built from this table.
    "forked": "gov's copy is a derivative of the target's — gov keeps these bytes for itself and "
              "has no right to send them; reported in both directions, written in neither",
}


def expand_rules(root: pathlib.Path, desc: dict, ctx: dict[str, str]) -> list[dict]:
    """Every (rule index, source, destination template, role) the descriptor names, BEFORE precedence.

    A `**` include enumerates the tracked files under `home`; everything else is literal. A rule that
    names no source at all still contributes its declared destinations, because a delegated rule has
    no gov bytes and its destination must still be visible to `plan` and to the receipt.
    """
    home = (desc.get("home") or "").rstrip("/")
    out: list[dict] = []
    for i, rule in enumerate(desc.get("files", [])):
        role = rule.get("role", "engine")
        # THE SAME POOL `plan` AND the write loop use. This function used to carry its own glob
        # expansion; another node landed `resolve_rule_pool` for the same reason on the same file,
        # and two expanders for one question is the class this repo keeps a record about. Theirs is
        # landed and recorded, so this defers to it — and their pool already excludes a source whose
        # DESTINATION another rule claims, which is the same protection this function's carve-out
        # provides and measurably reaches further.
        for src in resolve_rule_pool(root, desc, rule, ctx, home):
            for dest, miss in resolve_dests(desc, rule, src, ctx, home):
                out.append({"rule": i, "src": src, "dest": dest, "role": role, "miss": miss})
        if not resolve_rule_pool(root, desc, rule, ctx, home):
            for dest in rule_destinations(desc, rule):
                out.append({"rule": i, "src": None, "dest": dest, "role": role, "miss": []})
    return out


def resolve_entry(root: pathlib.Path, desc: dict, ctx: dict[str, str]) -> dict:
    """Apply precedence. TWO operations, TWO keys — the distinction the whole unit turns on.

    A `project-owned` rule is a SOURCE-level carve-out: it removes its sources from every EARLIER
    rule's contribution, and gov supplies no bytes for them ever. Among what survives, the WRITER of
    each destination is the LAST landable rule reaching it.

    Reducing by destination alone elects the seed template over the carve-out and makes the carve-out
    unobservable; reducing by source alone cannot express one source legitimately reaching two
    destinations under two roles, which two shipped descriptors do. Worked: codebase-map's `**` glob,
    its `map_extractors.py` carve-out and its template seed all touch one destination — the carve-out
    stops gov's own FILLED module travelling, and the seed elects the template as that destination's
    writer. Before this, gov's filled module landed byte-identical in the target and the receipt
    called it `engine`.

    Returns writes (resolved destination -> row), unlanded rows with their reasons, the carved source
    set, and the census of destinations whose winner is not the first rule that matched them.
    """
    rows = expand_rules(root, desc, ctx)

    carve_at: dict[str, int] = {}
    for r in rows:
        if r["role"] == "project-owned" and r["src"]:
            carve_at.setdefault(r["src"], r["rule"])
    survivors = [r for r in rows
                 if not (r["src"] in carve_at and r["rule"] < carve_at[r["src"]])]

    writes: dict[str, dict] = {}
    first: dict[str, dict] = {}
    unlanded: list[dict] = []
    missing: list[str] = []
    for r in survivors:
        dest, miss = r["dest"], r.get("miss", [])
        row = dict(r, dest=dest, missing=miss)
        missing += miss
        if r["role"] in LANDABLE_ROLES:
            first.setdefault(dest, row)
            writes[dest] = row          # later wins
        else:
            unlanded.append(row)

    census = [d for d, w in writes.items() if first[d]["rule"] != w["rule"]]
    return {"writes": writes, "unlanded": unlanded, "carved": set(carve_at),
            "census": census, "missing": sorted(set(missing)), "survivors": survivors}


def canonical_ctx(eid: str) -> dict[str, str]:
    """A ctx for reasoning about a descriptor with no target in hand — `selfcheck`'s only need."""
    return {"prefix": "tools", "kit_id": eid, "kit": f"tools/{eid}", "memory_root": "memory"}


def entry_version(root: pathlib.Path, desc: dict) -> str:
    """The kit's version constant AS RESOLVED NOW, for the receipt.

    A declared absence resolves to a marker rather than to a null, because a null is a value the next
    reader has to interpret and every reader will interpret it differently.
    """
    vf = desc.get("version_from")
    if not vf or "none" in vf:
        return "(none declared)"
    home = (desc.get("home") or "").rstrip("/")
    f, pat = vf.get("file"), vf.get("pattern")
    if not f or not pat:
        return "(unresolvable)"
    target = root / (f"{home}/{f}" if home else f)
    if not target.is_file():
        return "(unresolvable)"
    rx = re.compile(pat)
    for ln in target.read_text(encoding="utf-8", errors="replace").splitlines():
        if rx.search(ln):
            return ln.strip()
    return "(unresolvable)"


def entry_members(root: pathlib.Path, entry_id: str, desc: dict, desc_path: str) -> set[str]:
    """Every surface path this entry claims.

    A directory-shaped entry claims its own directory; a flat entry claims the paths its file rules
    name. Both are read from the descriptor, never inferred from the id.
    """
    claimed: set[str] = set()
    home = desc.get("home")
    if home and desc.get("kind") != "flat":
        claimed.add(home.rstrip("/"))
    for rule in desc.get("files", []):
        claimed.update(rule_sources(desc, rule))
        claimed.update(rule.get("claims", []))
    return claimed


# ------------------------------------------------------------------------------- selection + tokens
# The DEFAULT set is DECLARED IN THE REGISTRY, not here. It began as a constant in this file, and a
# scratch fixture caught what that meant: the engine named five kits by hand while the registry named
# the population, so any registry but gov's own reported five entries missing. Two answers to one
# question, inside the tool whose whole thesis is that there should be one. `--all` was already
# derived; the default set now comes from the same single source.
def default_kits(reg: dict) -> tuple[str, ...]:
    return tuple((reg.get("selection") or {}).get("default") or ())


def all_kits(descs: dict[str, tuple[dict, str]]) -> list[str]:
    """Every non-conditional entry. Derived; never a literal list."""
    return sorted(e for e, (d, _) in descs.items() if d.get("selectable") != "conditional")


def derive_install_order(ids: list[str], descs: dict[str, tuple[dict, str]]) -> list[str]:
    """Order a selection so a kit follows everything it `requires`. Alphabetical within a tier.

    `requires` was DECLARED by `memory-recall` and read by nothing: every mode of
    `resolve_selection` returned `sorted(...)`, so CONFIGURE ran adopters alphabetically and
    `memory-recall` ran BEFORE `memory-tree` had seeded `.memory-tree.conf`. Its adopter exited 1,
    govkit could not classify that code, and the default-selection apply arm failed on every node.
    Running the same adopter by hand a moment later exited 0 — the ordering was the whole defect.

    A dependency OUTSIDE the selection is not an error: `--kits drift-audit` is a legal install and
    orders one entry. Only the edges among the selected ids constrain the order.

    Kahn with an alphabetical ready-queue, so the result is deterministic and reduces to today's
    alphabetical order whenever no edge applies. A cycle REFUSES rather than falling back to
    alphabetical: an install order nobody can satisfy is not an order, and silently picking one is
    how this class returns.
    """
    want = set(ids)
    deps = {i: sorted({d for d in (descs[i][0].get("requires") or []) if d in want and d != i})
            for i in ids}
    out, placed = [], set()
    while len(out) < len(ids):
        ready = sorted(i for i in ids
                       if i not in placed and all(d in placed for d in deps[i]))
        if not ready:
            stuck = sorted(i for i in ids if i not in placed)
            raise Refusal(
                f"`requires` has a cycle among {', '.join(stuck)} — refusing to invent an install "
                f"order. Break the cycle in the descriptors; an order nobody can satisfy is not one"
            )
        out.extend(ready)
        placed.update(ready)
    return out


def resolve_selection(reg: dict, descs: dict[str, tuple[dict, str]], mode: str,
                      kits: list[str]) -> list[str]:
    if mode == "all":
        return derive_install_order(all_kits(descs), descs)
    if mode == "kits":
        unknown = [k for k in kits if k not in descs]
        if unknown:
            raise Refusal(
                f"--kits names {', '.join(unknown)}, which {'is' if len(unknown) == 1 else 'are'} "
                f"not a registry entry; the population is the registry, never a directory listing"
            )
        return derive_install_order(sorted(kits), descs)
    dk = default_kits(reg)
    if not dk:
        raise Refusal("registry.toml declares no [selection] default set, and this tool will not "
                      "invent one: a default nobody declared is a decision nobody made")
    missing = [k for k in dk if k not in descs]
    if missing:
        raise Refusal(f"the default set names {', '.join(missing)}, absent from the registry")
    return derive_install_order(sorted(dk), descs)


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
    tools/lib/resolve-python.sh documents for the Microsoft Store python3 stub.

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


def target_context(target: pathlib.Path, deploy: dict, eid: str, desc: dict) -> dict[str, str]:
    """The token values for one entry, from the target descriptor's answers."""
    prefix = (deploy.get("prefix") or "tools").strip("/")
    ctx: dict[str, str] = {
        "prefix": prefix,
        "kit_id": eid,
        "kit": f"{prefix}/{eid}",
    }
    for k, v in (deploy.get("answers") or {}).items():
        if isinstance(v, str):
            ctx[k] = v
    for k, v in ((deploy.get("kit") or {}).get(eid) or {}).items():
        if isinstance(v, str):
            ctx[k] = v
    ctx.setdefault("memory_root", "memory")
    return ctx


def load_deploy(target: pathlib.Path) -> dict:
    p = target / ".governance" / "deploy.toml"
    if not p.is_file():
        raise Refusal(
            f"no target descriptor at {p.as_posix()} — `intake` writes it and `apply --unattended` "
            f"reads every answer from it. Refusing to guess: an answer this tool invents is one the "
            f"operator never made and cannot audit"
        )
    return load_toml(p)


# ----------------------------------------------------------------------------------- the findings
class Report:
    def __init__(self) -> None:
        self.problems: list[str] = []
        self.notes: list[str] = []

    def fail(self, msg: str) -> None:
        self.problems.append(msg)

    def note(self, msg: str) -> None:
        self.notes.append(msg)

    def emit(self) -> int:
        for n in self.notes:
            print(f"govkit: {n}")
        for p in self.problems:
            print(f"govkit: {p}")
        if self.problems:
            print(f"govkit: {len(self.problems)} problem(s)")
            return 1
        return 0


# ------------------------------------------------------------------------------------- selfcheck
def selfcheck(root: pathlib.Path, write: bool = False) -> int:
    r = Report()
    reg_path = root / "tools" / "govkit" / "registry.toml"
    reg = load_toml(reg_path)

    entries = reg.get("entry", [])
    exempts = reg.get("exempt", [])
    if not entries:
        r.fail("registry.toml declares no entries — an empty population makes every assertion "
               "keyed on it vacuously true, which is the failure this file exists to prevent")
        return r.emit()

    # ---- 1: every entry names a descriptor, and the descriptor exists and parses. ONE reader,
    #         shared with plan and check — a second copy of this loop would be the very class the
    #         version cross-check below exists to catch, committed inside the tool that catches it.
    descs = read_descriptors(root, reg, r)

    # ---- 2: the descriptor's own id agrees with the registry's. Two spellings of one fact.
    for eid, (d, dpath) in descs.items():
        if d.get("id") != eid:
            r.fail(f"descriptor {dpath} declares id '{d.get('id')}' but the registry calls it "
                   f"'{eid}' — a descriptor and its registry row are two spellings of one fact")

    # ---- 3: every file a descriptor declares as a literal source actually exists.
    for eid, (d, _dpath) in descs.items():
        for rule in d.get("files", []):
            for src in rule_sources(d, rule):
                if not (root / src).exists():
                    r.fail(f"entry '{eid}' declares a source that does not exist: {src}")

    # ---- 3b: every role a descriptor SPELLS is a key of ROLE_KINDS. Caught here rather than at
    #          install time, because a role the table does not carry has no defined outcome in
    #          either verb — and the fallback that would let it through is `write`, the one kind
    #          that promises a file. An ABSENT role still defaults to `engine`; this is about a
    #          role spelled and unrecognised.
    for eid, (d, _dpath) in descs.items():
        for rule in d.get("files", []):
            role = rule.get("role")
            if role is not None and role not in ROLE_KINDS:
                r.fail(f"entry '{eid}' declares role '{role}', which is not in ROLE_KINDS "
                       f"({', '.join(sorted(ROLE_KINDS))}) — `plan` and `apply` both read that "
                       f"table, so an unlisted role has no defined outcome in either verb")

    # ---- 3c: a `forked` rule declares BOTH of `FORK_RULE_KEYS`, and `direction` is drawn from the
    #          closed enum. DEPL-dCarriedReceipt-10 S5.
    #
    #          THE DEMAND IS ON THE DESCRIPTOR AND NOWHERE ELSE. A receipt row is READ by `update`'s
    #          report printer and is never validated by it, because that printer keys on the
    #          RECEIPT's role and therefore meets rows this unit never wrote. Required on write,
    #          tolerated on read — the refusal lives where an operator can fix it, which is the rule
    #          file, not somebody else's installed target.
    #
    #          Neither key defaults. An unstated direction is the same silence `version_from`
    #          already refuses, and a fork with no ratifying record is a fork nobody agreed to.
    #          `direction` is a LABEL on a report: nothing in either verb branches on its value, and
    #          the enum exists so two descriptors cannot spell one answer two ways for the human who
    #          reads it.
    #
    #          WHAT THIS DOES NOT CHECK: whether the file IS a fork. That is a claim about
    #          provenance which no predicate over a descriptor can settle — this arm grades whether
    #          the claim is stated completely, never whether it is true.
    for eid, (d, _dpath) in descs.items():
        for rule in d.get("files", []):
            if rule.get("role") != "forked":
                continue
            direction = rule.get("direction")
            if not direction:
                r.fail(f"entry '{eid}' declares a `forked` rule with no `direction` — a fork that "
                       f"does not say which way the derivation runs tells the next reader nothing "
                       f"about whose bytes are authoritative. Declare one of "
                       f"{', '.join(FORK_DIRECTIONS)}")
            elif direction not in FORK_DIRECTIONS:
                r.fail(f"entry '{eid}' declares a `forked` rule with direction '{direction}', which "
                       f"is outside the closed set {', '.join(FORK_DIRECTIONS)} — a free-form "
                       f"direction is a field two descriptors spell two ways, and this one is read "
                       f"by a person deciding whether to touch the file")
            if not str(rule.get("record") or "").strip():
                r.fail(f"entry '{eid}' declares a `forked` rule with no `record` — name the id that "
                       f"ratified the fork. A fork nobody agreed to is a local edit wearing a role")

    # ---- 3d: a kit source whose HEAD declares `FORKED from` is claimed by a `forked` rule.
    #          DEPL-dCarriedReceipt-10 S6. The header is the author's own statement that gov's
    #          copy is a derivative of somebody else's file; this arm makes that statement bind a
    #          role, so the class is gated rather than the three instances fixed. Landing it
    #          without S7 would red gov's own registry on the first run, which is why the spec
    #          requires the same commit.
    #
    #          KEYED ON `rule_sources`, NOT REPO-WIDE, and the difference is measured: a repo-wide
    #          grep returns FOUR files, and the fourth is gov's own `.claude/hooks/recall-opened.js`,
    #          which NO descriptor claims as a destination. A repo-wide predicate would demand a
    #          `forked` declaration from an entry that does not own the path and red gov for its
    #          own hand-wired hook.
    #
    #          THE HEAD IS BOUNDED. A `FORKED from` deep inside a file is prose about something
    #          else -- this repo's own specs and records discuss the header constantly -- and an
    #          unbounded scan would grade them. The declaration is a header or it is not one.
    FORK_HEADER_BYTES = 800
    for eid, (d, _dpath) in descs.items():
        _fctx = canonical_ctx(eid)
        _fhome = (d.get('home') or '').rstrip('/')
        for rule in d.get('files', []):
            # THE EXPANDED POOL, not `rule_sources`. `rule_sources` skips any include carrying a glob
            # character, and the rule that would swallow an undeclared fork is exactly the `**` one --
            # so an arm keyed on it grades only literal includes and cannot fail on the case it exists
            # for. Observed: undeclaring `extract.py` left selfcheck GREEN.
            for src in resolve_rule_pool(root, d, rule, _fctx, _fhome):
                sp = root / src
                if not sp.is_file():
                    continue
                try:
                    head = sp.read_bytes()[:FORK_HEADER_BYTES].decode('utf-8', 'replace')
                except OSError:
                    continue
                if 'FORKED from' not in head:
                    continue
                if rule.get('role') != 'forked':
                    r.fail(f"'{src}' declares `FORKED from` in its head but entry '{eid}' claims "
                           f"it with role '{rule.get('role')}' — a forked source landed as an "
                           f"engine row is overwritten by gov's copy on the next update, and the "
                           f"target's own divergence is destroyed. Declare the rule `forked`")

    # ---- 4: no two file rules across the whole registry write the SAME destination.
    #         One source reaching two destinations is legal; two sources contending for one is not.
    dest_owner: dict[str, str] = {}
    for eid, (d, _dpath) in descs.items():
        for rule in d.get("files", []):
            for dest in rule_destinations(d, rule):
                if dest in dest_owner and dest_owner[dest] != eid:
                    r.fail(f"two entries write the same destination '{dest}': "
                           f"'{dest_owner[dest]}' and '{eid}'")
                dest_owner[dest] = eid

    # ---- 4b: a rule declaring BOTH `to` and `claims` resolves `to` INTO its own claims.
    #          DEPL-dCarriedReceipt-1 S4. The unit's defect was `{relpath}` resolving to a basename
    #          in the seam that writes while `destinations_for` resolved it through `rule_relpath`,
    #          so push-main's hook rule landed a bare `pre-push` at the target ROOT while the same
    #          rule's `claims` spelled `.githooks/pre-push`. Two spellings of one destination inside
    #          one rule. This arm gates the CLASS: fixing the instance and scanning only the instance
    #          certifies coverage that does not exist, and the next token to go wrong is not
    #          necessarily `{relpath}`.
    #
    #          Scoped to rules declaring BOTH keys, because `claims` is what makes the disagreement
    #          decidable -- a rule declaring no claims states no second opinion to contradict. A
    #          destination still carrying an unresolved `{...}` token is SKIPPED rather than failed:
    #          those are answer keys a target supplies, `claims` are written without them, and
    #          comparing the two spellings would red every templated rule in the registry.
    for eid, (d, _dpath) in descs.items():
        for rule in d.get("files", []):
            claims = rule.get("claims")
            if not rule.get("to") or not claims:
                continue
            # THROUGH `resolve_dests`, which is what `plan`, the write loop and the wildcard
            # exclusion all call. The first draft of this arm asked `rule_destinations`, which
            # routes through `destinations_for` -- the resolver that was already correct -- so
            # staging the defect back in left selfcheck GREEN. An arm that reads a different value
            # from the one the writer uses cannot fail on the writer's bug.
            _ctx = canonical_ctx(eid)
            _home = (d.get("home") or "").rstrip("/")
            _dests: list[str] = []
            for _s in rule_sources(d, rule):
                _dests.extend(dest for dest, _m in resolve_dests(d, rule, _s, _ctx, _home))
            for dest in _dests:
                if "{" in dest:
                    continue
                if dest not in claims:
                    r.fail(f"entry '{eid}' declares a rule whose destination '{dest}' is not among "
                           f"its own claims ({', '.join(sorted(claims))}) — one rule spelling one "
                           f"destination two ways, which is the shape that landed a bare basename "
                           f"at a target root while the claims named the real path")

    # ---- 5: version_from resolves to EXACTLY one line, or declares an explicit `none` with a reason.
    for eid, (d, _dpath) in descs.items():
        vf = d.get("version_from")
        if vf is None:
            r.fail(f"entry '{eid}' declares no version_from — declare the constant, or declare "
                   f"`version_from = {{ none = \"<reason>\" }}`; silence is not a third option")
            continue
        if "none" in vf:
            if not str(vf.get("none")).strip():
                r.fail(f"entry '{eid}' declares version_from.none with an empty reason")
            continue
        home = (d.get("home") or "").rstrip("/")
        f, pat = vf.get("file"), vf.get("pattern")
        if not f or not pat:
            r.fail(f"entry '{eid}' version_from needs both `file` and `pattern`")
            continue
        target = root / (f"{home}/{f}" if home else f)
        if not target.is_file():
            r.fail(f"entry '{eid}' version_from names a file that does not exist: {f}")
            continue
        rx = re.compile(pat)
        hits = [ln for ln in target.read_text(encoding="utf-8", errors="replace").splitlines()
                if rx.search(ln)]
        if len(hits) != 1:
            r.fail(f"entry '{eid}' version_from pattern matches {len(hits)} lines in {f}, not "
                   f"exactly one — a pattern matching none is unfillable and one matching several "
                   f"cannot say which is the version")

    # ---- 5b: the version claims cross-checked against the repo's OWN version gate, BOTH directions.
    #
    # This arm exists because without it the registry is a SECOND POPULATION describing the same
    # fact as `check-kit-versions.sh`'s `need` list, and nothing would assert they agree — which is
    # exactly the defect class this unit was built to close, reproduced inside the unit. It is not a
    # tautology: the two sides are authored independently, in different languages, by different
    # units. A disagreement is REPORTED rather than repaired; repairing gov's own version bookkeeping
    # is a stated non-goal of this unit and is filed as its own backlog row.
    gate = root / "tools" / "check-kit-versions.sh"
    if gate.is_file():
        gate_txt = gate.read_text(encoding="utf-8", errors="replace")
        gate_files = set(re.findall(r'^need\s+"[^"]*"\s+(\S+)', gate_txt, re.M))
        reg_files: dict[str, str] = {}
        for eid, (d, _dpath) in descs.items():
            vf = d.get("version_from") or {}
            if "none" in vf or not vf.get("file"):
                continue
            home = (d.get("home") or "").rstrip("/")
            reg_files[f"{home}/{vf['file']}" if home else vf["file"]] = eid
        for f, eid in sorted(reg_files.items()):
            if f not in gate_files:
                r.note(f"entry '{eid}' declares a version constant in '{f}' that "
                       f"tools/check-kit-versions.sh does not assert — reported, not repaired")
        for f in sorted(gate_files - set(reg_files)):
            r.note(f"tools/check-kit-versions.sh asserts a constant in '{f}' that no registry entry "
                   f"claims — reported, not repaired")

    # ---- 6: every declared hole carries a discharge probe. A hole observed by NEITHER flag is the
    #         majority case measured across the shipped kits, and there the probe is the only
    #         evidence the hole exists at all.
    for eid, (d, _dpath) in descs.items():
        for h in d.get("hole", []):
            hid = h.get("id", "<unnamed>")
            if not h.get("discharge"):
                r.fail(f"entry '{eid}' hole '{hid}' carries no discharge probe — 'discharged' is "
                       f"then undefined, and check has no evaluator for it")
            if not str(h.get("why", "")).strip():
                r.fail(f"entry '{eid}' hole '{hid}' carries no reason")

    # ---- 7: a requires_if condition names keys that resolve in the named kit's config lists, and
    #         names a kit that is a registry entry.
    key_lists = ("required_keys_gate", "required_keys_render", "optional_keys", "conditional_keys")
    for eid, (d, _dpath) in descs.items():
        for edge in d.get("requires_if", []):
            other = edge.get("kit")
            if other and other not in descs:
                r.fail(f"entry '{eid}' requires_if names '{other}', which is not a registry entry")
            declared: set[str] = set()
            cfg = d.get("config", {})
            for kl in key_lists:
                declared.update(cfg.get(kl, []))
            for k in edge.get("when_any_key_set", []):
                if k not in declared:
                    r.fail(f"entry '{eid}' requires_if names condition key '{k}', which appears in "
                           f"none of its own config key lists — selfcheck then has no key to resolve")

    # ---- 7b: the selections are DERIVED, and every default-set member is a real entry. `--all` is
    #          computed from the registry rather than listed anywhere, so an entry cannot exist that
    #          no selection reaches — the state the unattended kit was found in.
    derived_all = all_kits(descs)
    for k in default_kits(reg):
        if k not in descs:
            r.fail(f"the default set names '{k}', which is not a registry entry")
    unreachable = [e for e in descs if e not in derived_all
                   and descs[e][0].get("selectable") != "conditional"]
    for e in unreachable:
        r.fail(f"entry '{e}' is reached by no selection and is not marked conditional")

    # ---- 7c: every guard pathspec in gov's OWN manifest falls into exactly ONE declared class.
    #          A class table that does not partition its input is how the emitter gets a rule for the
    #          majority and no rule for the rest — which is what happened when the hooks directory
    #          and the kickoff tree were classed "cannot exist in a target" while the same revision
    #          deployed both.
    legs_path = root / "tools" / "gate-legs.json"
    if legs_path.is_file():
        kit_dirs = {f"tools/{e}/" for e in descs} | {"tools/"}
        exempt_prefixes = {x.get("path", "").rstrip("/") + "/" for x in exempts if x.get("path")}
        verbatim = (".githooks/", ".claude/")
        renamed = ("skills/session-kickoff/",)
        for leg in json.loads(legs_path.read_text(encoding="utf-8")):
            for g in leg.get("guard", []) or []:
                classes = []
                if g.startswith("memory/"):
                    classes.append("memory-root-relative")
                if any(g.startswith(v) for v in verbatim):
                    classes.append("verbatim-repo-root")
                if any(g.startswith(v) for v in renamed):
                    classes.append("renamed")
                if any(g == p.rstrip("/") or g.startswith(p) for p in exempt_prefixes):
                    classes.append("exempt")
                if any(g == k or g.startswith(k) for k in kit_dirs) and "exempt" not in classes:
                    classes.append("kit-relative")
                if len(classes) != 1:
                    r.fail(f"guard pathspec '{g}' (leg '{leg.get('name')}') falls into "
                           f"{len(classes)} declared classes {classes or '[]'}, not exactly one — "
                           f"a taxonomy that does not partition its own input gives the emitter no "
                           f"rule for the remainder")

    # ---- 7d: `mutates_index` is DERIVED, never trusted as a declared value. A `git add` string
    #          inside an `echo` is not a staging call, and mistaking one for the other is how this
    #          unit's own spec published a measured claim that was three times the truth.
    for eid, (d, _dpath) in descs.items():
        adopt = d.get("adopt") or {}
        declared = adopt.get("mutates_index")
        if declared is None:
            continue
        argv = adopt.get("argv") or []
        script = next((a for a in argv if a.endswith(".sh")), None)
        if not script:
            continue
        home = (d.get("home") or "").rstrip("/")
        cand = root / (f"{home}/{pathlib.PurePosixPath(script).name}" if home
                       else pathlib.PurePosixPath(script).name)
        if not cand.is_file():
            continue
        actual = any(re.match(r"^[ \t]*git add ", ln)
                     for ln in cand.read_text(encoding="utf-8", errors="replace").splitlines())
        if bool(declared) != actual:
            r.fail(f"entry '{eid}' declares mutates_index = {str(declared).lower()} but its adopter "
                   f"{'does' if actual else 'does not'} execute `git add` — the declared value is "
                   f"not the measured one")

    # ---- 7e: the step-id vocabulary is a TUPLE, and `step()` is its only printer. Deriving the
    #          ordinal from the tuple is what makes the ordering criterion an assertion about order
    #          rather than about a substring; a hand-numbered print would drift from the tuple the
    #          first time a step was inserted.
    for i, name in enumerate(STEPS):
        if not name.isupper() or not name.isalpha():
            r.fail(f"step id '{name}' is not an upper-case word — the vocabulary is compared by "
                   f"exact string and a decorated id cannot be matched")
    if len(set(STEPS)) != len(STEPS):
        r.fail("the step-id tuple repeats an id, so an ordinal does not identify a step")

    # ---- 7f: PRECEDENCE, both halves, over gov's own descriptors.
    #          The census is a NOTE: an overlap is legal and is how a carve-out is spelled. What
    #          FAILS is a source a carve-out excluded that is nonetheless written — A1 as a predicate.
    later_wins = carves = carves_that_change = 0
    for eid, (d, _dpath) in descs.items():
        try:
            res = resolve_entry(root, d, canonical_ctx(eid))
        except Refusal as e:
            r.fail(f"entry '{eid}' does not resolve: {e}")
            continue
        later_wins += len(res["census"])
        carves += len(res["carved"])
        written_srcs = {w["src"] for w in res["writes"].values() if w["src"]}
        for s in sorted(res["carved"] & written_srcs):
            r.fail(f"entry '{eid}' carves out '{s}' as project-owned and writes it anyway — gov "
                   f"must supply no bytes for a carved source, and this is the shape that landed "
                   f"gov's own filled extractors in a target")
        # Does the carve-out change any WRITE, or is it redundant with destination last-wins? Both
        # figures are reported, and a zero on the second does NOT red. Measured on gov today it IS
        # zero: both shipped carve-outs sit in front of a seed rule that already wins the same
        # destination. Reporting only the first figure would hide that; reddening on the second would
        # red a true state, which is how a gate teaches its operator to waive it.
        if res["carved"]:
            bare = dict(d, files=[x for x in d.get("files", [])
                                  if x.get("role") != "project-owned"])
            try:
                alt = resolve_entry(root, bare, canonical_ctx(eid))
            except Refusal:
                continue
            a = {k: (v["src"], v["role"]) for k, v in res["writes"].items()}
            b = {k: (v["src"], v["role"]) for k, v in alt["writes"].items()}
            if a != b:
                carves_that_change += 1
    r.note(f"precedence: {later_wins} destination(s) won by a later rule than the first match · "
           f"{carves} carve-out source(s) declared, of which {carves_that_change} change a write")

    # ---- 7g: `update`'s dispatch is COMPLETE over BOTH enumerations. Two arms, because the role arm
    #          structurally cannot see a missing GRID cell — which is how the grid shipped with no
    #          answer for a file deleted on both sides, and the verdict routed to a restore of a blob
    #          that does not exist. A refusal counts as a row; silence does not.
    known_roles = set(UNLANDED_REASON) | set(LANDABLE_ROLES) | {"attributes", "gate-leg", "ci"}
    for role in sorted(known_roles):
        if role not in UPDATE_ROLE:
            r.fail(f"role '{role}' has no row in `update`'s dispatch — a role a later unit adds and "
                   f"leaves out of the table is one `update` will meet and cannot classify")
    for o in OURS_STATES:
        for t in THEIRS_STATES:
            if (o, t) not in VERDICT_GRID:
                r.fail(f"the verdict grid has no cell for (ours={o}, theirs={t}) — every pair must "
                       f"name a verdict, including the one where both sides are gone")

    # ---- 7i: DEPL-dCarriedReceipt-8 S4/AC5. THE NO-CLOBBER GUARANTEE, asserted STRUCTURALLY over
    #          the grid rather than behaviourally over the one row that exposed it. `differs` on the
    #          OURS axis means the target's index blob is not gov's blob at this row's `commit` — an
    #          adopter's edit, or a carried copy `-9` proves a rung for. A cell that routed such a
    #          row to a verdict in `RAW_WRITE_VERDICTS` would hand it to the arm that overwrites
    #          with gov's raw bytes, which is precisely the destruction `-8` closed. Both sets are
    #          READ from the module, so widening the write arm or repointing a cell reds HERE rather
    #          than shipping.
    #
    #          WHAT THIS DOES NOT CHECK, because a structural check reads as a semantic one.
    #          Not whether the delta predicate itself is right — that is `classify_row`'s
    #          `gov_oid` comparison, graded behaviourally. Not whether the merge branch stamps
    #          the right identity — S1, likewise behavioural. And nothing at all about the
    #          `absent` OURS row: a carried row the target DELETED reaches `missing`
    #          legitimately, and that cell is `-9` S11's rather than this arm's.
    for o, t, v in raw_write_cells(VERDICT_GRID):
        r.fail(f"the verdict grid maps (ours={o}, theirs={t}) to '{v}', which `update`'s write "
               f"loop RAW-WRITES with gov's bytes. An OURS axis of `differs` says the target holds "
               f"something gov did not ship, so that cell silently destroys it — the defect "
               f"DEPL-dCarriedReceipt-8 closed. A delta row routes to the three-way merge, always")

    # ---- 7h: LEG correspondence, BOTH directions. The descriptors and
    #          gov's own leg manifest are two spellings of one fact, and before this nothing asserted
    #          they agree — the deployer's whole thesis, unapplied to the deployer. An exemption is
    #          the escape, on the same reason-and-staleness rule as the path exemptions, and S6
    #          refuses a leg that is BOTH claimed and exempted.
    legs_path = root / "tools" / "gate-legs.json"
    if legs_path.is_file():
        _legs_json = json.loads(legs_path.read_text(encoding="utf-8"))
        manifest = {leg.get("name") for leg in _legs_json}
        manifest_subject = {leg.get("name"): leg.get("subject") for leg in _legs_json}
        claimed_legs: dict[str, str] = {}
        for eid, (d, _dpath) in descs.items():
            for leg in d.get("gate_leg", []):
                nm = leg.get("name")
                if not nm:
                    r.fail(f"entry '{eid}' declares a gate leg with no name")
                    continue
                if nm in claimed_legs:
                    r.fail(f"leg '{nm}' is claimed by both '{claimed_legs[nm]}' and '{eid}'")
                claimed_legs[nm] = eid
                if nm not in manifest:
                    r.fail(f"entry '{eid}' declares gate leg '{nm}', which is in no leg of "
                           f"tools/gate-legs.json — a descriptor and the manifest are two spellings "
                           f"of one fact and this is the direction that deploys a leg a target's "
                           f"runner will never match")
                else:
                    # AND THEY MUST AGREE ABOUT SUBJECT. The name check above proves the leg exists
                    # in both; it says nothing about whether they agree on which side of the bar it
                    # sits. A descriptor saying `kit` against a manifest saying `repo` deploys a leg
                    # that is held in the target and run here, or the reverse — two spellings of one
                    # fact, drifting exactly where nobody is reading. TOOL-dUnstalledConvoy-26.
                    d_sub = leg.get("subject")
                    m_sub = manifest_subject.get(nm)
                    if d_sub is None:
                        r.fail(f"entry '{eid}' declares gate leg '{nm}' with no `subject` — a leg "
                               f"that does not say whose subject it is cannot be held or run "
                               f"deliberately, and defaulting it here would hide the omission. "
                               f"The criterion is stated once, at the `subject` field declaration "
                               f"in tools/run-gates/run-gates.sh: ask what a FAILURE of this leg "
                               f"MEANS, not what it tests")
                    elif d_sub not in ("kit", "repo"):
                        r.fail(f"entry '{eid}' declares gate leg '{nm}' with subject '{d_sub}', "
                               f"which is outside the closed set kit|repo — an unrecognised value "
                               f"would be defaulted by every reader to whichever side it assumed")
                    elif m_sub is None:
                        # THE ONE CASE THE FIRST DRAFT EXEMPTED, and it is the case that drifts
                        # SILENTLY and then permanently. Guarding the comparison on
                        # `m_sub is not None` meant a manifest row with no key never disagreed with
                        # anything — while the runner defaults it to `repo` and the emitter ships
                        # the DESCRIPTOR's value to every adopter. Reproduced end to end: gov runs
                        # the leg on every bar and every adopter holds it forever, with this check
                        # green. Worse, -29's ratchet reds once and its own remediation
                        # (`selfcheck --write`) then pins the DERIVED default and the disagreement
                        # is green for good. The sibling exempt-leg path already refused exactly
                        # this; the two paths agree now.
                        r.fail(f"entry '{eid}' declares gate leg '{nm}' as subject '{d_sub}' and "
                               f"tools/gate-legs.json declares none — every reader defaults a "
                               f"missing key to 'repo', so an omission here is a silent "
                               f"disagreement that the subject pin will then make permanent")
                    elif d_sub != m_sub:
                        r.fail(f"entry '{eid}' declares gate leg '{nm}' as subject '{d_sub}' while "
                               f"tools/gate-legs.json says '{m_sub}' — the descriptor and the "
                               f"manifest disagree about whether this leg runs by default")
                # AC1b: a name that travels. A digit inside a parenthetical is a COUNT, and a count
                # in a leg name goes stale exactly where nobody is reading — in somebody else's repo.
                if re.search(r"\([^)]*\d[^)]*\)", nm):
                    r.fail(f"entry '{eid}' declares leg name '{nm}', which carries a digit-bearing "
                           f"parenthetical; the emitter writes this name into a target, where a "
                           f"count nobody maintains is worse than no name at all")

        exempt_legs: dict[str, str] = {}
        for x in reg.get("exempt_leg", []):
            nm, why = x.get("name"), str(x.get("why", "")).strip()
            if not nm:
                r.fail(f"an exempt_leg row carries no name: {x!r}")
                continue
            if not why:
                r.fail(f"exempt_leg '{nm}' carries an empty reason — an exemption without one is an "
                       f"omission wearing a label")
            if nm not in manifest:
                r.fail(f"exempt_leg '{nm}' names a leg that is no longer in the manifest — a stale "
                       f"exemption silently widens the surface it was written to narrow")
            if nm in claimed_legs:
                r.fail(f"leg '{nm}' is exempted AND claimed by entry '{claimed_legs[nm]}' — an "
                       f"exemption and a claim for one fact is the two-spellings class arriving "
                       f"through the escape hatch built to prevent it")
            # AND ITS SUBJECT IS READ HERE, because this is the only path that reaches it.
            # An exempted leg is claimed by no descriptor, so every subject arm above — presence,
            # closed set, descriptor-vs-manifest agreement — quantifies over a population these
            # rows are not in. Without this the check silently covers less than its name claims,
            # which is the exact wording TOOL-dUnstalledConvoy-26 S8 used and the exact item its
            # build left unfinished. Read from the MANIFEST, since that is where an exempt leg's
            # subject is written and where the runner reads it from.
            _x_sub = manifest_subject.get(nm)
            if _x_sub is None:
                r.fail(f"exempt_leg '{nm}' is a leg in tools/gate-legs.json that declares no "
                       f"`subject` — an exempted leg is reachable by no descriptor, so this is the "
                       f"only check that can see it, and a defaulted subject is a side of the bar "
                       f"nobody chose")
            elif _x_sub not in ("kit", "repo"):
                r.fail(f"exempt_leg '{nm}' declares subject '{_x_sub}', outside the closed set "
                       f"kit|repo — an unrecognised value is defaulted by every reader to whichever "
                       f"side it assumed")
            exempt_legs[nm] = why
        for nm in sorted(manifest - set(claimed_legs) - set(exempt_legs)):
            r.fail(f"gate leg '{nm}' is claimed by no descriptor and carried by no [[exempt_leg]] — "
                   f"a new leg must red until a declaration says whether an adopter receives it")
        r.note(f"legs: {len(manifest)} in the manifest · {len(claimed_legs)} claimed · "
               f"{len(exempt_legs)} exempt")

        # ---- 7h2: THE SUBJECT RATCHET. TOOL-dUnstalledConvoy-29.
        #
        # WHAT THIS DOES NOT CHECK, said here because a check named for subjects sitting green on a
        # bar reads to everybody who did not write it as evidence the subjects are RIGHT. It is not.
        # Deciding whether a leg belongs on the automatic bar means knowing what its failure MEANS,
        # which no predicate over a descriptor can see. This grades CHANGE and nothing else: a
        # subject cannot move without the move appearing in a diff somebody reviews. A green row here
        # is evidence that nobody flipped a value quietly, never that the value is correct.
        #
        # PINNED OVER THE MANIFEST, not over the descriptors. 7h above already asserts the two agree
        # in both directions, so pinning the manifest pins every descriptor leg transitively AND
        # covers the [[exempt_leg]] rows, which no descriptor claims and a descriptor-derived pin
        # would therefore leave free to move. The spec asked for the descriptors; this is the amended
        # answer and -29 rev-2 records why.
        pin_path = root / "tools" / "govkit" / "subject-pins.tsv"
        live = {nm: (manifest_subject.get(nm) or "repo") for nm in manifest if nm}
        bad_name = sorted(nm for nm in live if "\t" in nm)
        for nm in bad_name:
            r.fail(f"gate leg '{nm}' carries a TAB in its name, which is this pin file's field "
                   f"separator — a name that cannot be recorded cannot be ratcheted")
        body = "".join(f"{nm}\t{live[nm]}\n" for nm in sorted(live) if nm not in bad_name)
        header = (
            "# subject-pins.tsv — GENERATED. Regenerate with `python tools/govkit/govkit.py "
            "selfcheck --write`.\n"
            "#\n"
            "# One row per gate leg in tools/gate-legs.json: <name>\\t<subject>. `kit` legs are HELD "
            "off the\n"
            "# automatic bar and run only under GATE_SELFTESTS=1; `repo` legs run on every bar.\n"
            "#\n"
            "# THIS FILE GRADES CHANGE, NOT CORRECTNESS. It exists so a subject cannot move without\n"
            "# the move appearing in a diff. Whether any given value is RIGHT is a review judgement\n"
            "# — the criterion is stated once, at the `subject` field declaration in\n"
            "# tools/run-gates/run-gates.sh: ask what a FAILURE of the leg MEANS.\n")
        want = header + body
        if write:
            pin_path.parent.mkdir(parents=True, exist_ok=True)
            pin_path.write_text(want, encoding="utf-8", newline="\n")
            subprocess.run(["git", "-C", str(root), "add", "--", "tools/govkit/subject-pins.tsv"],
                           capture_output=True, check=False)
            print(f"govkit selfcheck — wrote {len(live)} subject pin(s) to "
                  f"tools/govkit/subject-pins.tsv")
        elif not pin_path.is_file():
            r.fail("tools/govkit/subject-pins.tsv is missing — the subject ratchet has no pin to "
                   "compare against, so every leg could leave the automatic bar unobserved. "
                   "Regenerate with `python tools/govkit/govkit.py selfcheck --write`")
        else:
            pinned: dict[str, str] = {}
            for ln in pin_path.read_text(encoding="utf-8").split("\n"):
                if not ln.strip() or ln.lstrip().startswith("#"):
                    continue
                nm, _tab, sv = ln.partition("\t")
                if not _tab:
                    r.fail(f"tools/govkit/subject-pins.tsv has a row with no tab: {ln!r}")
                    continue
                pinned[nm] = sv.strip()
            for nm in sorted(set(live) - set(pinned)):
                r.fail(f"gate leg '{nm}' has no row in tools/govkit/subject-pins.tsv — a NEW leg "
                       f"reds until its subject is on the record, because an unpinned leg is one "
                       f"whose side of the bar nobody chose. Regenerate with "
                       f"`python tools/govkit/govkit.py selfcheck --write`")
            for nm in sorted(set(pinned) - set(live)):
                r.fail(f"tools/govkit/subject-pins.tsv pins '{nm}', which is in no leg of "
                       f"tools/gate-legs.json — a stale pin row is a pin for nothing, and it hides "
                       f"the next leg that arrives under that name")
            for nm in sorted(set(live) & set(pinned)):
                if live[nm] != pinned[nm]:
                    moved = ("OFF the automatic bar: it will run only under GATE_SELFTESTS=1"
                             if live[nm] == "kit" else
                             "ON to the automatic bar: it will run on every gate run")
                    r.fail(f"gate leg '{nm}' is subject '{live[nm]}' and pinned '{pinned[nm]}' — "
                           f"this moves the leg {moved}. If that is intended, move the pin in the "
                           f"SAME commit with `python tools/govkit/govkit.py selfcheck --write`; "
                           f"this check grades the CHANGE and never whether the value is right")
            r.note(f"subject pins: {len(pinned)} pinned · "
                   f"{sum(1 for v in live.values() if v == 'kit')} held")

    # ---- 7h3: A REPO-LOCAL POLICY MAY NOT RIDE OUT IN A KIT'S PAYLOAD. TOOL-dUnstalledConvoy-28.
    #
    # `.githooks/pre-push` ships VERBATIM to every push-main adopter, so a `GATE_SELFTESTS`
    # assignment written into it is a choice every adopter inherits without making it — and it would
    # turn the kit self-tests back on for exactly the repositories TOOL-dUnstalledConvoy-26 exists to
    # spare, at exactly the boundary it was measured for. The mechanism may travel; the choice may
    # not. This is the assertion that keeps that true after everyone has forgotten why it was chosen.
    #
    # WHAT IT DOES NOT CHECK: whether the policy is the RIGHT one, or whether the file that carries
    # it is wired to anything. It answers one question — is a file that DECIDES this also a file a
    # kit COPIES — and the shipped set is derived through the same descriptors `apply` writes from,
    # never listed, because a second list of what a kit ships is the two-spellings class this build
    # has already paid for twice.
    #
    # THE PREDICATE IS A BARE ASSIGNMENT, deliberately: `GATE_SELFTESTS=1 bash ...` is an INVOCATION
    # and appears in docs, arms and refusal strings all over this tree, while a line that is nothing
    # but the assignment is a policy. Run over the tracked tree before wiring: 0 hits and 54
    # near-misses, none of them a policy. Records under the memory root are excluded — a decision
    # log quoting a policy line is not executing one.
    # TWO EVASIONS the first spelling admitted, both of them things a person writes without
    # thinking: a trailing comment (`export GATE_SELFTESTS=1  # gov only`) and the shell default
    # form (`: ${GATE_SELFTESTS:=1}`), which assigns exactly as hard as `=`. Re-run over the tracked
    # tree after widening: still one hit, still no invocation matched.
    policy_re = re.compile(
        r"^[ \t]*(?::[ \t]+)?(?:export[ \t]+)?"
        r"(?:GATE_SELFTESTS=\S*|\$\{GATE_SELFTESTS:?=[^}]*\})"
        r"[ \t]*(?:#.*)?$")
    # THE SHIPPED SET, resolved the way `apply` resolves it. `claims` covers only 13 of 58 file
    # rules in this tree, so deriving from that key alone would have quantified over a third of the
    # payload and reported a confident zero over the rest — the could-not-fail shape, arriving as an
    # under-derived population rather than as a wrong predicate. `**` is expanded against the
    # entry's home exactly as check 7i expands it.
    _all_tracked = tracked(root)
    shipped_owner: dict[str, str] = {}
    for eid, (d, _dpath) in descs.items():
        _home = (d.get("home") or "").rstrip("/")
        for rule in d.get("files", []):
            _inc = rule.get("include")
            _srcs = _inc if isinstance(_inc, list) else ([_inc] if _inc else [])
            if any(s == "**" for s in _srcs) and _home:
                _paths = [f for f in _all_tracked if f.startswith(_home + "/")]
            else:
                _paths = rule_sources(d, rule)
            for _c in list(_paths) + [str(c) for c in (rule.get("claims") or [])]:
                shipped_owner.setdefault(_c, eid)
    policy_files = []
    for f in _all_tracked:
        if not f or f.startswith("memory/") or f.endswith(".md"):
            continue
        try:
            txt = (root / f).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if any(policy_re.match(ln) for ln in txt.split("\n")):
            policy_files.append(f)
    for f in sorted(set(policy_files) & set(shipped_owner)):
        owner = shipped_owner[f]
        r.fail(f"'{f}' carries a bare GATE_SELFTESTS assignment AND is shipped by kit '{owner}' — "
               f"a repo-local gate policy written into a file a kit copies is a policy every adopter "
               f"inherits without choosing it. Move the assignment to a path no kit claims; the "
               f"mechanism that reads it may travel, the choice may not")
    r.note(f"gate policy: {len(policy_files)} file(s) assign GATE_SELFTESTS · "
           f"{len(shipped_owner)} shipped path(s) derived from the descriptors")

    # ---- 7i: per-file claim inside a NON-FLAT entry's home. Scoped deliberately: five `kind="flat"`
    #          entries declare `home = "tools"` as a source-resolution base, and quantifying over
    #          that home would red on every tracked file under it — hundreds — rather than on the one
    #          real exposure. A flat entry's home resolves sources; it is not an ownership boundary.
    exempt_paths_pre = {x.get("path") for x in exempts if x.get("path")}
    files_all = tracked(root)
    unclaimed_in_home = 0
    for eid, (d, _dpath) in descs.items():
        home = (d.get("home") or "").rstrip("/")
        if not home or d.get("kind") == "flat":
            continue
        named = set()
        for rule in d.get("files", []):
            inc = rule.get("include")
            srcs = inc if isinstance(inc, list) else ([inc] if inc else [])
            if any(s == "**" for s in srcs):
                named.update(f for f in files_all if f.startswith(home + "/"))
            else:
                named.update(rule_sources(d, rule))
        for f in files_all:
            if f.startswith(home + "/") and f not in named and f not in exempt_paths_pre:
                unclaimed_in_home += 1
                r.fail(f"entry '{eid}' has '{f}' under its home and no file rule claims it — a file "
                       f"added inside a kit whose includes are a literal list is otherwise invisible "
                       f"to the surface predicate, which is depth-1")
    r.note(f"per-file claim: {unclaimed_in_home} unclaimed file(s) under a non-flat home")

    # ---- 7j: `--check` WIRING PARITY, derived in BOTH directions like `mutates_index`. A shipped
    #          script that accepts the arm and is wired by no descriptor is a verifier nobody runs; a
    #          `[check].argv` naming a script with no such arm is a claim the engine cannot honour.
    #          The scan is scoped to the NAMED script, which is what excludes the false positives a
    #          repo-wide grep would collect.
    n_scanned = 0
    for eid, (d, _dpath) in descs.items():
        chk = d.get("check") or {}
        wired, declared_none = bool(chk.get("argv")), "none" in chk
        home = (d.get("home") or "").rstrip("/")

        # The population is every ADOPTER-shaped script this entry ships, not only the ones an argv
        # names — the two entries this arm exists for name their script in no argv at all, and an
        # argv-only scan cannot see them.
        cands: list[pathlib.Path] = []
        for av in ((d.get("adopt") or {}).get("argv") or [], chk.get("argv") or []):
            for a in av:
                if a.endswith(".sh"):
                    cands.append(root / (f"{home}/{pathlib.PurePosixPath(a).name}" if home
                                         else pathlib.PurePosixPath(a).name))
        for rule in d.get("files", []):
            for s in rule_sources(d, rule):
                if s.endswith(".sh") and not s.endswith(".test.sh"):
                    cands.append(root / s)

        for cand in dict.fromkeys(cands):
            if not cand.is_file():
                continue
            n_scanned += 1
            body = [ln for ln in cand.read_text(encoding="utf-8", errors="replace").splitlines()
                    if not ln.lstrip().startswith("#")]
            accepts = any("--check" in ln for ln in body)
            # A DECLARED absence is the legal escape, exactly as it is for a version constant: an
            # entry may say `[check] = { none = "<reason>" }` and may not say nothing.
            if accepts and not wired and not declared_none:
                r.fail(f"entry '{eid}': {cand.name} accepts `--check`, no `[check].argv` wires it, "
                       f"and no reason is declared — a verifier the kit ships and nothing runs")
            if wired and not accepts and cand.name in "".join(chk.get("argv") or []):
                r.fail(f"entry '{eid}': `[check].argv` names {cand.name}, which has no `--check` arm")
    r.note(f"check wiring: {n_scanned} shipped script(s) read")

    # ---- 7k: entry-level `scope` is DERIVED and asserted against the declared value. Every
    #          descriptor declares one and the engine read only the rule-level spelling, so the
    #          contract's machine-scoped criterion had no referent at all.
    n_scope = 0
    for eid, (d, _dpath) in descs.items():
        if "scope" not in d:
            continue
        n_scope += 1
        rules = d.get("files", [])
        derived = "machine" if rules and all(
            rr.get("scope") == "machine" or rr.get("link") for rr in rules) else "repo"
        if d["scope"] != derived:
            r.fail(f"entry '{eid}' declares scope '{d['scope']}' and its rules derive '{derived}' — "
                   f"an entry is machine-scoped only when every one of its rules is")
    r.note(f"entry scope: {n_scope} declaration(s) checked against their derived value")

    # ---- 8: the SURFACE predicate, both directions (spec S12). This is the arm that stops a
    #         population claim going stale, and the one place a count is derived rather than spelled.
    globs = reg.get("surface", {}).get("globs", [])
    if not globs:
        r.fail("registry.toml declares no surface globs — the completeness assertion would then "
               "quantify over nothing and pass vacuously")
        return r.emit()

    surface = surface_paths(root, globs)
    claimed: dict[str, str] = {}
    for eid, (d, dpath) in descs.items():
        for m in entry_members(root, eid, d, dpath):
            claimed.setdefault(m, eid)

    exempt_paths: dict[str, str] = {}
    for x in exempts:
        p, why = x.get("path"), str(x.get("why", "")).strip()
        if not p:
            r.fail(f"an exemption row carries no path: {x!r}")
            continue
        if not why:
            r.fail(f"exemption '{p}' carries an empty reason — an exemption without one is an "
                   f"omission wearing a label")
        if not (root / p).exists():
            r.fail(f"exemption '{p}' names a path that no longer exists — a stale exemption "
                   f"silently widens the surface it was written to narrow")
        exempt_paths[p] = why

    unowned = sorted(s for s in surface if s not in claimed and s not in exempt_paths)
    for u in unowned:
        r.fail(f"tracked path '{u}' is in the declared surface but is neither an entry member nor "
               f"an exemption — a new moving part must red until a declaration claims it")

    stale_claims = sorted(c for c in claimed if c not in surface and not (root / c).exists())
    for c in stale_claims:
        r.fail(f"entry '{claimed[c]}' claims '{c}', which is not tracked")

    r.note(f"surface {len(surface)} tracked path(s) · {len(descs)} entr(y|ies) · "
           f"{len(exempt_paths)} exemption(s) · {len(unowned)} unclaimed")
    return r.emit()


# ------------------------------------------------------------------------------ roles → outcomes
# THE ONE TABLE. `plan` classifies with it, `apply` derives its write condition from it, and
# `selfcheck` asserts the declared role population is a subset of its keys. TWO FUNCTIONS DECIDING
# INDEPENDENTLY WHAT `apply` WILL DO IS THE DEFECT THIS TABLE DELETES — the same class as the
# `resolve_dests`/`resolve_rule_pool` seam one level down, and the same class the repo records at
# memory/gotchas/two-answers-to-one-question.md.
#
# `merged` maps to `blocked` rather than to a write because writing a gov-owned region into a file
# the target owns is the one shape with no seam anywhere in this repo — measured, nothing here writes
# a `.gitattributes` block or performs the renormalize that follows it — and `cmd_apply` refuses the
# whole install over one. `rendered`/`generated` map to `side-effect` because a step `apply` runs
# produces them; whether such a step EXISTS is a per-entry question and `derive_rule_kind` asks it.
# `forked` maps to a kind of its OWN — DEPL-dCarriedReceipt-10 S1 — and reusing `blocked` was
# rejected on two measured grounds rather than on taste. `planned_writes` previews a `blocked` rule
# from `rule_destinations` alone and never from the source pool, so a forked rule derived from a `**`
# include with no `to` would preview NOTHING; and `SKIP_REASONS["blocked"]` is a sentence about
# gov-owned regions inside target-owned files, which is `merged`'s situation and is false of a fork.
# The forked kind previews from the pool like every non-blocked role, prints its own mark, and
# carries its own reason.
#
# WHAT `forked` IS, because the name invites the wrong reading: it is a claim the DESCRIPTOR RULE
# makes about a file's PROVENANCE — gov's copy is derived from the target's — and it is re-read from
# that rule on every run. It is never inferred from what an attribution walk found, and no
# measurement of bytes can promote a row to it or demote a row out of it.
ROLE_KINDS = {
    "engine": "write",
    "seed": "write",
    "rendered": "side-effect",
    "generated": "side-effect",
    "project-owned": "order",
    "merged": "blocked",
    "forked": "forked",
}

#: The closed enum a `forked` rule's `direction` is drawn from (DEPL-dCarriedReceipt-10 §8 F1). A
#: free string is a field two descriptors spell two ways, and the value is read by a human deciding
#: whether to touch the file. It is a LABEL on a report and never an instruction: nothing in either
#: verb branches on it.
FORK_DIRECTIONS = ("gov-from-target", "target-from-gov", "both")

#: The keys a `forked` rule must declare. REQUIRED ON THE DESCRIPTOR, TOLERATED ON A RECEIPT ROW —
#: one rule, two call sites. `selfcheck` refuses a descriptor that omits either, because that is
#: where an operator can fix it; `update`'s printer keys on the RECEIPT's role and therefore meets
#: rows this unit never wrote (one stamped before the role existed, one whose descriptor has since
#: changed its keys), and a printer that raised on a missing key would convert a report into a crash
#: on the single path that exists to avoid acting.
FORK_RULE_KEYS = ("direction", "record")

#: DERIVED, never declared beside the table. A role added with any kind other than `write` is
#: automatically not landable and a role added as `write` is automatically landed, in BOTH verbs,
#: from one edit — which is what makes the single-table rule mechanical rather than remembered.
LANDABLE_ROLES = tuple(k for k, v in ROLE_KINDS.items() if v == "write")

#: The plan marks, in the order `cmd_plan` prints them. Kept beside the table so a new kind cannot
#: reach the printer without a mark.
KIND_MARKS = {"write": "write ", "order": "ORDER ", "side-effect": "SIDE  ",
              "covered": "COVER ", "blocked": "BLOCK ", "forked": "FORK  "}


def check_entry_producer(desc: dict) -> bool:
    """Does `apply` run anything for this entry that could produce a `rendered`/`generated` file?

    MEASURED, not assumed. CONFIGURE is `argv = d.get("adopt", {}).get("argv") or []` followed by
    `if not argv: continue`, so an entry with an empty adopter runs NOTHING — and two entries
    carrying a `rendered`/`generated` rule declare exactly that in writing: `review-harness`
    ("the render is performed by the parity gate's own --render mode rather than by a separate
    adopter") and `check-install-prefix` ("seeded empty rather than copied"). Previewing those two as
    a side-effect would be the same over-promise this unit deletes, moved one mark over.

    A `blocks_adopt` hole makes CONFIGURE skip too. No descriptor here declares one today, so that
    half is correct and unexercised by the shipped tree; `selftest.py` arms it with a FIXTURE, which
    is the difference between a guard and a claim.
    """
    if not ((desc.get("adopt") or {}).get("argv") or []):
        return False
    return not any(h.get("blocks_adopt") for h in desc.get("hole", []))


def scan_produced_destinations(desc: dict, ctx: dict) -> set[str]:
    """Destinations some rule in this descriptor declares as a `side_effects` product."""
    out: set[str] = set()
    for rule in desc.get("files", []):
        for sfx in rule.get("side_effects", []):
            out.add(resolve_tokens(sfx, ctx)[0])
    return out


def scan_written_destinations(root: pathlib.Path, desc: dict, ctx: dict, home: str) -> set[str]:
    """Every destination a LANDABLE rule in this descriptor actually writes.

    Exists because a role does not determine an outcome on its own. In 2 of this tree's 4
    `project-owned` rules a sibling `seed` rule lands that exact path in the SAME apply —
    `map_extractors.py` beside `map_extractors.template.py`, and `drift_signals.py` beside its
    template. Classifying on the role alone printed two contradictory verbs for one path.
    """
    out: set[str] = set()
    for rule in desc.get("files", []):
        if ROLE_KINDS.get(rule.get("role", "engine")) != "write":
            continue
        if rule.get("scope") == "machine" or rule.get("link"):
            continue
        for src in resolve_rule_pool(root, desc, rule, ctx, home):
            out.update(d for d, _m in resolve_dests(desc, rule, src, ctx, home))
    return out


#: What `apply` prints when it declines a rule, keyed by the kind the PREVIEW gave that rule — so
#: the two verbs cannot describe one skip two ways.
SKIP_REASONS = {
    "side-effect": "a step this apply runs produces it; govkit does not copy it",
    "order": "nothing in this install produces it — the target or its operator must supply it",
    "covered": "a sibling rule in this entry writes that same path in this run",
    "blocked": "no verb here can write a gov-owned region into a target-owned file",
    "forked": "gov's copy is a derivative of this target's file — its bytes are wrong here by "
              "construction, and that stays true when the target's own copy is absent",
}


def _resolve_skip_destinations(root: pathlib.Path, desc: dict, rule: dict, ctx: dict,
                       home: str) -> list[tuple[str, list[str]]]:
    """The destinations a SKIPPED rule would have had, for reporting only.

    Machine-scoped and link rules never resolve a source pool, so they answer from
    `rule_destinations` the way `planned_writes` does for them.
    """
    if rule.get("scope") == "machine" or rule.get("link") \
            or ROLE_KINDS.get(rule.get("role", "engine")) == "blocked":
        return [resolve_tokens(x, ctx) for x in rule_destinations(desc, rule)]
    return [p for src in resolve_rule_pool(root, desc, rule, ctx, home)
            for p in resolve_dests(desc, rule, src, ctx, home)]


def derive_rule_kind(eid: str, desc: dict, rule: dict, dest: str, written: set[str],
                  produced: set[str], r: "Report") -> str | None:
    """What `apply` will do at ONE resolved destination. `None` means the role is unknown and `r`
    now carries the refusal.

    An unknown role does NOT fall back to `write`. Defaulting an unrecognised role to the one kind
    that promises a file is how this defect would be reintroduced by the next role someone adds; an
    ABSENT role still defaults to `engine`, which is the documented existing behaviour.
    """
    role = rule.get("role", "engine")
    if rule.get("scope") == "machine" or rule.get("link"):
        return "order"          # an act on the machine, not on the tree — role does not enter
    kind = ROLE_KINDS.get(role)
    if kind is None:
        r.fail(f"entry '{eid}' declares role '{role}', which is not in ROLE_KINDS "
               f"({', '.join(sorted(ROLE_KINDS))}) — refusing rather than guessing whether "
               f"`apply` writes it. Add the role to the table with the kind it deserves")
        return None
    if kind == "side-effect" and not (check_entry_producer(desc) or dest in produced):
        return "order"          # nothing in this install produces it; someone else must
    if kind == "order" and dest in written:
        return "covered"        # a sibling rule writes this same path in this same apply
    return kind


# ----------------------------------------------------------------------------------------- plan
def planned_writes(root: pathlib.Path, target: pathlib.Path, deploy: dict,
                   descs: dict[str, tuple[dict, str]], selection: list[str],
                   r: Report) -> list[dict]:
    """What `apply` would DO, one row per resolved destination. WRITES NOTHING.

    A row's `kind` comes from `derive_rule_kind()` — the ONE table `apply` derives its write condition
    from. Every non-`write` kind is a promise this tool does NOT make: `order` (someone else supplies
    it), `side-effect` (a step `apply` runs produces it), `covered` (a sibling rule writes that same
    path), `blocked` (`apply` refuses the install over it).

    THIS FUNCTION USED TO STAMP `write` ON EVERY ROLE. `apply` writes only `LANDABLE_ROLES`, so a
    preview of the `playbook` entry — in the DEFAULT selection — promised two files and `apply`
    landed zero and exited 0. Four of the six declared roles were previewed as writes and never
    written.
    """
    commit = git(root, "rev-parse", "HEAD").strip()
    out: list[dict] = []
    for eid in selection:
        d, _dpath = descs[eid]
        ctx = target_context(target, deploy, eid, d)
        home = (d.get("home") or "").rstrip("/")
        # Computed ONCE per entry: which destinations a landable rule in this descriptor writes, so
        # a `project-owned` row that shares a path with a sibling `seed` is not previewed as an
        # ORDER for a file this same run creates.
        written = scan_written_destinations(root, d, ctx, home)
        produced = scan_produced_destinations(d, ctx)
        for rule in d.get("files", []):
            role = rule.get("role", "engine")
            srcs = rule_sources(d, rule)
            if ROLE_KINDS.get(role) == "blocked":
                # PREVIEWED FROM `to`, NOT FROM A SOURCE POOL. `cmd_apply` refuses the whole install
                # on a `merged` rule regardless of what it includes, so a preview that reads the pool
                # shows NOTHING for a merged rule declaring `include = []` — measured on
                # `settings-merge`, where plan listed one write and one side-effect while apply
                # refused. The refusal is the most important thing a preview can carry.
                for dest in rule_destinations(d, rule):
                    resolved, missing = resolve_tokens(dest, ctx)
                    out.append({"kit": eid, "role": role, "kind": "blocked",
                                "dest": resolved, "missing": missing, "src": ", ".join(srcs) or "(no source)",
                                "commit": commit})
                continue
            # THE SAME POOL `apply` WILL USE. This used to read `rule_destinations()`, which resolves
            # sources through `rule_sources()` and therefore skips every glob — so a `**` rule
            # produced no rows at all and the operator approved a plan describing a fraction of the
            # write. Measured on the lexicon kit before this changed: plan 3, apply 12.
            for src in resolve_rule_pool(root, d, rule, ctx, home):
                for resolved, missing in resolve_dests(d, rule, src, ctx, home):
                    for k in missing:
                        r.fail(f"entry '{eid}' needs answer '{k}' to resolve a destination for "
                               f"'{src}', and the target descriptor supplies none — refusing before "
                               f"any write, and naming the key rather than inventing a value")
                    kind = derive_rule_kind(eid, d, rule, resolved, written, produced, r)
                    if kind is None:
                        continue
                    out.append({"kit": eid, "role": role, "kind": kind,
                                "dest": resolved, "missing": missing, "src": src,
                                "commit": commit})
        # The attributes destination and ONE row per declared PIN PATTERN. Never the resolved path
        # list: that population is git's answer about which paths the block governs, and at plan
        # time the block is unwritten, so git resolves nothing. The resolved list is asserted
        # receipt-versus-post-condition instead, which is why it is not a plan row.
        for pin in d.get("lf_pin", []):
            pat, miss = resolve_tokens(pin.get("pattern", ""), ctx)
            out.append({"kit": eid, "role": "attributes", "kind": "order",
                        "dest": ".gitattributes:" + pat, "missing": miss, "src": "",
                        "why": "a line-ending pin, emitted into one govkit-owned block"})

    return out


def coverage_rows(root: pathlib.Path, target: pathlib.Path, deploy: dict,
                  descs: dict[str, tuple[dict, str]], selection: list[str],
                  r: Report, rows: list[dict] | None = None) -> list[dict]:
    """PARTIAL adoption: which files gov would write that this target does not hold
    (DEPL-dCarriedReceipt-4 S1).

    THE ONLY PARTIAL-ADOPTION SIGNAL THIS ENGINE HAD WAS WHOLE-KIT — `update`'s
    `available (not installed)` line, which needs a receipt. So a target that took 80 files of a kit
    and left 20 read exactly like one that took all 100. This is the read-only join that needs no
    receipt, writes nothing, and returns a number for a real adopter today.

    THE POPULATION IS `kind == "write"` AND NOTHING ELSE (S2). `order`, `side-effect`, `covered` and
    `blocked` are each a promise gov does NOT make, so counting one as a gap reports a target for a
    file gov never ships. The predicate is written against the kind rather than the role, over the
    whole `ROLE_KINDS` table, because a role added tomorrow gets its kind from that table and this
    join inherits the answer.

    A ROW WITH AN UNRESOLVED TOKEN IS NOT A COVERAGE ROW (S3). `planned_writes` has already turned
    that into an `r.fail`, and a destination still carrying a brace is not a path — reporting it as
    absent would say the target is missing a file whose name nobody knows.

    THE INDEX ANSWERS, NEVER THE WORKTREE. An untracked file sitting at the destination is not a
    file the target HOLDS, and this engine already decided that once, where a leg guard drops on
    tracked-ness rather than existence. Two answers to "does the target have this" is the class this
    file spends most of its comments on.

    ROWS, NEVER UNIQUE DESTINATIONS (S4). Two rules resolving to one `dest` are two triage items,
    and a destination-keyed tally is exactly what hid the one collision measured at NicoCares.

    `rows` IS AN OPTIONAL ALREADY-COMPUTED PLAN, and it exists so the spec's own perf line stays
    true. That line promises ONE `git ls-files` on top of the walk `planned_writes` already
    performs; the only caller is `cmd_plan`, which has just walked the descriptors for its own
    output, so without this the coverage flag would silently double the run's dominant cost on a
    181-row target. Called without it, this function is self-contained and does the walk itself —
    which is what any future caller gets, and what the arms exercise.
    """
    if rows is None:
        rows = planned_writes(root, target, deploy, descs, selection, r)
    have = set(tracked(target))
    return [{"kit": row["kit"], "dest": row["dest"], "src": row["src"]}
            for row in rows
            if row["kind"] == "write" and not row["missing"] and row["dest"] not in have]


def cmd_plan(root: pathlib.Path, target: pathlib.Path, mode: str, kits: list[str],
             coverage: bool = False, emit_declines: bool = False) -> int:
    r = Report()
    reg = load_toml(root / "tools" / "govkit" / "registry.toml")
    descs = read_descriptors(root, reg, r)
    deploy = load_deploy(target)
    selection = resolve_selection(reg, descs, mode, kits)
    rows = planned_writes(root, target, deploy, descs, selection, r)

    print(f"govkit plan — target {target.as_posix()} · selection: {', '.join(selection)}")
    print(f"govkit plan — source commit {git(root, 'rev-parse', '--short', 'HEAD').strip()} "
          f"(bytes are taken from the git index at this commit, never from the working tree)")
    # THE LEGEND IS PART OF THE PROMISE. Only `write` says govkit puts bytes at that path; every
    # other mark says something else does, or nothing does. Printed before the rows because a mark
    # an operator has to infer is a mark that gets read as a write.
    print("govkit plan — marks: write = govkit writes it · SIDE = a step apply runs produces it · "
          "ORDER = something outside apply must supply it · COVER = a sibling rule writes that same "
          "path · BLOCK = apply refuses the install over it · FORK = gov's copy is a derivative of "
          "the target's, reported and never written · UNRES. = unresolved token, not a path")
    for row in rows:
        # A destination still carrying a brace is NOT a path, and printing it under `write` would
        # promise a write this tool cannot perform — the row is marked UNRESOLVED so the plan never
        # reads as a file set anyone can rely on.
        mark = "UNRES." if row["missing"] else KIND_MARKS.get(row["kind"], "?????")
        print(f"  {mark} [{row['role']:<13}] {row['dest']}   <- {row['kit']}")
    holes = [(eid, h.get("id")) for eid in selection for h in descs[eid][0].get("hole", [])]
    for eid, hid in holes:
        print(f"  ORDER  [hole         ] .governance/outbox/{hid}.md   <- {eid}")
    # `n` is derived from KIND_MARKS and the summary HAND-NAMES its kinds, so a kind added to the
    # table alone is counted here and never printed — measured, and DEPL-dCarriedReceipt-10 S2 is
    # the unit that met it. The clause below is derived from the same table for that reason: every
    # kind KIND_MARKS carries reaches the line, and a kind added tomorrow reaches it too.
    n = {k: sum(1 for x in rows if x["kind"] == k) for k in KIND_MARKS}
    named = {"write": "write(s)", "side-effect": "side-effect(s)", "order": "order(s)",
             "covered": "covered", "blocked": "blocked", "forked": "forked"}
    counts = {k: n[k] + (len(holes) if k == "order" else 0) for k in KIND_MARKS}
    print("govkit plan — "
          + ", ".join(f"{counts[k]} {named.get(k, k)}" for k in KIND_MARKS)
          + ". NOTHING was written.")

    # ---- DEPL-dCarriedReceipt-4 S4. ADDITIVE (§8 F2): the plan rows above are what a reader needs
    # ---- to interpret a gap row, and a mode that hid them would make the operator run the verb
    # ---- twice. REPORT-ONLY (§8 F1): a gap is a state of the world, not a fault in the run, and a
    # ---- first honest run that exits 1 reads as a broken tool.
    # `--emit-declines` IMPLIES `--coverage` rather than refusing without it. The skeletons are one
    # per GAP row, so without the join there is no gap set — and a flag that printed nothing in that
    # case is the skip-that-looks-like-a-pass shape this whole unit is written against. Implying it
    # is also why this adds no refusal branch, which is what §7 promises about `BRANCH_PIN`.
    if coverage or emit_declines:
        gaps = coverage_rows(root, target, deploy, descs, selection, r, rows)
        for g in gaps:
            print(f"  GAP    [{g['kit']:<13}] {g['dest']}   <- {g['src']}")
        per_kit = {k: sum(1 for g in gaps if g["kit"] == k) for k in selection}
        # `gap 0` PRINTS. A clean run that printed nothing is indistinguishable from a coverage
        # check that never ran, and this whole unit exists because an absent signal read as a
        # present one for two live targets.
        print(f"govkit plan — coverage: gap {len(gaps)} of {counts['write']} write row(s)"
              + (" · " + ", ".join(f"{k} {v}" for k, v in per_kit.items() if v) if gaps else "")
              + ". Coverage answers PRESENCE only: a present-but-hand-edited file reads as covered.")
        if emit_declines:
            # STDOUT, never the target's own file (§3). A deployer that edits the document carrying
            # the owner's decisions has made one for them. This is paste-ready text and nothing else.
            for g in gaps:
                print(f'\n[[decline]]\nkit = "{g["kit"]}"\ndest = "{g["dest"]}"\nwhy = ""')
    return r.emit()


# ---------------------------------------------------------------------------------------- check
def run_kit_check(eid: str, desc: dict, ctx: dict[str, str], target: pathlib.Path,
                  r: "Report | None" = None) -> tuple[str, str, int | None]:
    """RUN one kit's own declared `[check]` and report the state it MEASURED (`-14` S1).

    ONE runner, and this is the whole of it: `check` calls it per claimed kit, and `update` calls it
    twice per TOUCHED kit — once before the first byte moves and once after the write loop. A second
    implementation is the duplicate-answer class this build spends units removing, and a verifier
    that graded a write by a different predicate than `check` uses would disagree with `check` the
    first time either one changed.

    RETURNS `(state, detail, rc)`. `state` is one of the three states a check that RAN can produce —
    `adopted`, `landed-but-inert`, `landed-unmeasured` — and NOTHING here returns `not-run`: a kit
    nothing executed has no check result, and that state is owned by the caller that decided not to
    call. `rc` is the exit code, or None wherever no subprocess ran, which is every
    `landed-unmeasured` spelling.

    `r` IS THE FINDING CHANNEL AND IT IS OPTIONAL, deliberately. `check` passes its own report and
    keeps every message it printed before this extraction, byte for byte. `update` passes None and
    owns its own disposition, because `-14` S6 turns on a distinction no single run can make: a kit
    red at BOTH runs is pre-existing red and must NOT `r.fail`, and a runner that reported for the
    caller would decide that question here, one call too early.
    """
    chk = (desc.get("check") or {})
    if chk.get("argv"):
        pairs = [resolve_tokens(a, ctx) for a in chk["argv"]]
        if any(m for _a, m in pairs):
            if r is not None:
                r.fail(f"kit '{eid}' check argv carries an unresolved token")
            return "landed-unmeasured", " (its check argv does not resolve)", None
        try:
            rc = subprocess.run(resolve_shell_argv([a for a, _m in pairs]), cwd=str(target),
                                capture_output=True, text=True).returncode
        except OSError as e:
            # A check that cannot LAUNCH is red, never unmeasured and never a traceback. The hole
            # loop below has had this shape since it was written; the check arm had not, so a
            # descriptor naming a binary the target does not have took `update` down mid-write
            # rather than reporting the kit. `landed-but-inert` is the honest state: something was
            # asked and it did not work.
            if r is not None:
                r.fail(f"kit '{eid}': its own adopter check arm could not run: {e}")
            return "landed-but-inert", f" (its check arm could not run: {e})", None
        if rc != 0 and r is not None:
            r.fail(f"kit '{eid}': its own adopter check arm exits {rc}, so the kit is landed "
                   f"but not working — surfaced rather than swallowed")
        return ("adopted" if rc == 0 else "landed-but-inert"), "", rc
    if "none" in chk:
        reason = str(chk.get("none", "")).strip()
        if not reason and r is not None:
            r.fail(f"kit '{eid}' declares `[check] = {{ none }}` with an empty reason")
        return "landed-unmeasured", (f" — {reason}" if reason else ""), None
    if r is not None:
        r.fail(f"kit '{eid}' declares neither `[check].argv` nor `[check] = {{ none = \"…\" }}`, "
               f"so nothing measured it and nothing said why — declare the absence with a "
               f"reason; silence is not a third option")
    return "landed-unmeasured", "", None


def check_argv_of(desc: dict, ctx: dict[str, str]) -> str:
    """The kit's check argv as the operator would type it, for an order to name (`-14` S7).

    Resolved through the same `resolve_tokens` the runner uses, so an order cannot name a different
    command than the one that ran. Unresolved tokens are left standing — an order about a check that
    could not resolve should show the brace that stopped it.
    """
    argv = (desc.get("check") or {}).get("argv") or []
    return " ".join(resolve_tokens(a, ctx)[0] for a in argv)


def cmd_check(root: pathlib.Path, target: pathlib.Path) -> int:
    """Read-only verification of an installed target, over one owned state vocabulary.

    Every state is a MEASUREMENT and none is a placeholder. `not-landed` is a kit the receipt claims
    with zero rows for it while its descriptor declares a landable rule. `landed-unmeasured` is legal
    only where the descriptor DECLARES `[check] = { none = "<reason>" }` — an undeclared absence reds,
    because before this the engine printed one byte-identical string for "nothing was measured" and
    for "measured and broken", and exited 0 either way. `landed-but-inert` is reserved for a MEASURED
    failure. `adopted` is a check arm that ran and passed.

    A hole that is undischarged reds regardless of what the kit's adopter exited with, because exit 0
    from an adopter means "the adopter ran", never "the kit works".
    """
    r = Report()
    reg = load_toml(root / "tools" / "govkit" / "registry.toml")
    descs = read_descriptors(root, reg, r)

    receipt_path = target / ".governance" / "install.json"
    if not receipt_path.is_file():
        print(f"govkit check — {target.as_posix()}: NOT LANDED (no .governance/install.json)")
        r.fail("no receipt, so nothing here was installed by govkit. That is a state, not an error "
               "in the target — but `check` cannot verify an install that left no record")
        return r.emit()

    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    deploy = load_deploy(target)
    selection = receipt.get("kits") or []

    # ---- EVIDENCE, role-scoped. Before this, `check` contained ONE
    # ---- filesystem test — on the receipt's own path — and never opened the file list, never read
    # ---- the sidecar it writes, and called no hash function. Measured: a target whose landed files
    # ---- were all deleted, whose every recorded commit was rewritten to zeros and whose every hash
    # ---- was rewritten to nonsense, exited 0.
    rows = receipt.get("files") or []
    n_engine = n_ok = n_prov = n_prov_ok = 0
    for row in rows:
        role, path = row.get("role", "engine"), row.get("path")
        dp = target / path
        if role in ("engine", "seed", "project-owned", "generated") and not dp.exists():
            if row.get("written") is False and role in ("project-owned", "generated"):
                continue          # gov never wrote it; its absence is the target's business
            r.fail(f"'{path}' is in the receipt and not on disk")
            continue
        if role != "engine":
            # A `seed` carries an EXISTENCE claim only: the role's whole contract is that the target
            # owns the file after one copy, so hashing it would red every target that did what the
            # role exists to permit. That scoping is the contract's own unscoped-quantifier mistake,
            # not repeated here.
            continue
        n_engine += 1
        want = row.get("sha256")
        if want and _sha(dp.read_bytes()) != want:
            r.fail(f"'{path}' does not match the receipt: expected {want[:12]}, "
                   f"found {_sha(dp.read_bytes())[:12]}")
        else:
            n_ok += 1
        src, commit = row.get("source"), row.get("commit")
        if src and commit:
            n_prov += 1
            blob = blob_at(root, commit, src)
            # DEPL-dCarriedReceipt-8 S6. THE PROVENANCE QUESTION IS "did gov ship these bytes at
            # this commit", and `gov_oid` is the field that answers it — the only one that does.
            # This loop used to read `sha256`, which is a hash of the bytes that LANDED, and the two
            # coincide only where the target holds gov's file untouched. On a merged row they never
            # do: the file legitimately holds gov's bytes plus the adopter's edit, and this loop
            # called that receipt corruption. Measured immediately after a successful three-way,
            # `provenance: 1/2 resolved` plus a named hash mismatch, on a target nothing was wrong
            # with. `sha256` still answers the INTEGRITY question above, unchanged; one field was
            # being asked two questions and this is the reader that had the wrong one.
            gov_oid = row.get("gov_oid")
            if blob is None:
                r.fail(f"'{path}': its recorded source '{src}' does not resolve at commit "
                       f"{commit[:12]} in the gov checkout at {root.as_posix()} — either this is a "
                       f"different clone than the receipt recorded, or that commit is not fetched here")
            elif gov_oid:
                if blob_oid(blob) != gov_oid:
                    r.fail(f"'{path}': the receipt's gov_oid does not name gov's own blob "
                           f"at {commit[:12]} — recorded {gov_oid[:12]}, gov has "
                           f"{blob_oid(blob)[:12]}. `gov_oid` is STORED, so this is a "
                           f"receipt that no longer matches its own evidence rather than a "
                           f"target that drifted")
                else:
                    n_prov_ok += 1
            elif want and _sha(blob) != want:
                # A receipt below schema 3 carries no `gov_oid` at all, and `check` does not migrate
                # — `update` does, once, from this same evidence. `sha256` is the only identity such
                # a row has, so the legacy comparison is what is available rather than what is
                # right, and it keeps its old message. A merged row in a schema-2 receipt therefore
                # still reds here, truthfully: nothing in it distinguishes gov's bytes from the
                # merge result until the migration runs.
                r.fail(f"'{path}': the receipt's hash does not match gov's own bytes at "
                       f"{commit[:12]} — recorded {want[:12]}, gov has {_sha(blob)[:12]}")
            else:
                n_prov_ok += 1

    # A DERIVED count, and a zero over a population the DESCRIPTORS say is non-empty is itself a
    # finding — a receipt that lost its rows and a target that is clean are otherwise the same output.
    r.note(f"integrity: {n_ok}/{n_engine} engine row(s) verified · "
           f"provenance: {n_prov_ok}/{n_prov} resolved")
    if n_prov and n_prov_ok == 0:
        r.fail("DEAD PROBE: every engine row failed to resolve in this gov checkout, so the "
               "provenance loop measured nothing — a probe that cannot move is not a green one")

    # The sidecar and the receipt are asserted against EACH OTHER. They are two spellings written
    # from one list, and the sidecar — the artifact a target verifies with bash alone — is read by
    # nothing in this repo. Verifying one and trusting the other leaves it unasserted forever.
    sums_path = target / ".governance" / "install.sums"
    if sums_path.is_file():
        sums = set()
        for ln in sums_path.read_text(encoding="utf-8").splitlines():
            if ln.strip():
                h, _, pth = ln.partition("  ")
                sums.add((h.strip(), pth.strip()))
        want_pairs = {(f["sha256"], f["path"]) for f in rows if "sha256" in f}
        for extra in sorted(sums - want_pairs):
            r.fail(f"install.sums carries {extra[1]} ({extra[0][:12]}) which the receipt does not")
        for missing in sorted(want_pairs - sums):
            r.fail(f"the receipt carries {missing[1]} ({missing[0][:12]}) which install.sums does not")
        r.note(f"sidecar: {len(sums)} line(s) compared against {len(want_pairs)} hashed row(s)")

    # ---- MERGED-BLOCK DRIFT. The receipt hashes the BLOCK, never the file, so an edit OUTSIDE the
    # ---- block is invisible here BY CONSTRUCTION — the extractor only ever reads the marked lines.
    # ---- That is both of the contract's clauses satisfied by one mechanism rather than two.
    n_blocks = n_blocks_ok = 0
    for row in rows:
        if row.get("role") != "merged" or row.get("marker_style") == "json-pointer":
            continue
        n_blocks += 1
        dp = target / row["path"]
        if not dp.is_file():
            r.fail(f"the file carrying gov block '{row.get('block_id')}' is GONE: {row['path']}")
            continue
        om, cm = marker_pair(row.get("marker_style"), row["block_id"])
        try:
            span = find_block(dp.read_text(encoding="utf-8", errors="replace"), om, cm)
        except Refusal as e:
            r.fail(f"{row['path']}: {e}")
            continue
        if span is None:
            r.fail(f"gov block '{row['block_id']}' has been REMOVED from {row['path']}")
            continue
        i, j = span
        got = "\n".join(dp.read_text(encoding="utf-8", errors="replace").split("\n")[i:j + 1])
        h = hashlib.sha256(got.replace(CR, "").encode("utf-8")).hexdigest()
        if h != row.get("block_sha256"):
            r.fail(f"DRIFT: gov block '{row['block_id']}' in {row['path']} was edited "
                   f"(expected {str(row.get('block_sha256'))[:8]}, found {h[:8]})")
        else:
            n_blocks_ok += 1
    if n_blocks:
        r.note(f"merged blocks: {n_blocks_ok}/{n_blocks} intact")

    # ---- THE OUTBOX. The contract names it as an arm and the verb never opened it. Every order the
    # ---- receipt records must exist; an order for a hole no selected kit declares is stale.
    declared_holes = {h.get("id") for eid in selection if eid in descs
                      for h in descs[eid][0].get("hole", [])}
    n_orders = 0
    for order in receipt.get("orders") or []:
        n_orders += 1
        op = target / order["path"]
        if not op.is_file():
            r.fail(f"the receipt records order '{order['path']}' and it is not on disk")
        if order.get("kind") == "hole" and order.get("id") not in declared_holes:
            r.fail(f"order '{order['path']}' is for hole '{order.get('id')}', which no selected kit "
                   f"declares — a stale order is an instruction nobody owns")
        if order.get("kind") == "machine":
            # NOT `landed-but-inert` and NOT a missing-file finding. The destination is outside the
            # repository, so a check running inside it cannot answer the question — the ORDER is the
            # only observable artifact, and its absence is what reds.
            print(f"govkit check — {order.get('kit')}: undischargeable — "
                  f"{order.get('destination')} is outside this repository")
    if n_orders:
        r.note(f"outbox: {n_orders} order(s) recorded")

    for eid in selection:
        if eid not in descs:
            r.fail(f"the receipt claims kit '{eid}', which is not a registry entry")
            continue
        d, _ = descs[eid]
        ctx = target_context(target, deploy, eid, d)

        # `not-landed` is decided per KIT against the receipt's own rows. The whole-target verdict it
        # replaces early-returned on an ABSENT receipt, so a kit whose files were all gone still
        # printed a landed state.
        landable = any(rule.get("role", "engine") in LANDABLE_ROLES
                       for rule in d.get("files", []))
        if landable and not [f for f in (receipt.get("files") or []) if f.get("kit") == eid]:
            print(f"govkit check — {eid}: not-landed")
            r.fail(f"kit '{eid}' is claimed by the receipt and has no rows in it, while its "
                   f"descriptor declares at least one landable rule")
            continue

        state, detail, _rc = run_kit_check(eid, d, ctx, target, r)
        print(f"govkit check — {eid}: {state}{detail}")

        for h in d.get("hole", []):
            hid = h.get("id")
            cmd = (h.get("discharge") or {}).get("command")
            if not cmd:
                r.fail(f"kit '{eid}' hole '{hid}' has no discharge probe, so 'discharged' is "
                       f"undefined for it and this check cannot answer the question")
                continue
            resolved = []
            unresolved: list[str] = []
            for a in cmd:
                s, miss = resolve_tokens(a, ctx)
                resolved.append(s)
                unresolved += miss
            if unresolved:
                r.fail(f"kit '{eid}' hole '{hid}' probe needs answer(s) "
                       f"{', '.join(sorted(set(unresolved)))}, which the target descriptor lacks")
                continue
            try:
                rc = subprocess.run(resolve_shell_argv(resolved), cwd=str(target), capture_output=True,
                                    text=True).returncode
            except OSError as e:
                r.fail(f"kit '{eid}' hole '{hid}' probe could not run: {e}")
                continue
            if rc != 0:
                r.fail(f"kit '{eid}' hole '{hid}' is UNDISCHARGED (probe exit {rc}) — "
                       f"{h.get('why', '').splitlines()[0] if h.get('why') else 'no reason declared'}")
    return r.emit()


# ----------------------------------------------------------------------------------------- apply
# `LANDABLE_ROLES` used to be a hand-written `("engine", "seed")` HERE, beside the write loop, while
# `planned_writes` decided the same question with a different predicate. It is now DERIVED from
# `ROLE_KINDS` at the top of the roles section, so there is one table and one answer.
# LANDABLE_ROLES and UNLANDED_REASON live with the resolver, above: which roles land is a property of
# the resolution, not of the apply verb, and spelling it twice is the defect this file exists to end.


# ------------------------------------------------------------------------ the merged-region writer
CR = "\r"


def marker_pair(style: str, block_id: str) -> tuple[str, str]:
    """The ONE function that knows what a marker pair looks like.

    Neither merged SOURCE carries the markers its rule names — measured — so the pair cannot be
    found, only SYNTHESIZED, and the writer and the checker must synthesize the identical pair.
    Spelling it in two places is this repo's named defect class, so it is spelled here and nowhere.
    """
    if style != "hash-comment":
        raise Refusal(f"marker_style '{style}' has no synthesizer; the value is refused rather than "
                      f"defaulted, because a block written under a grammar the checker cannot "
                      f"reproduce is a block gov wrote and can never find again")
    return f"# {block_id}", f"# /{block_id}"


def find_block(text: str, open_m: str, close_m: str) -> tuple[int, int] | None:
    """Locate a marked region. REPRODUCES the shipped splice's refusal table, deliberately.

    Column 0, exact equality after stripping exactly ONE trailing CR; exactly one open and one
    close; close after open. It is REPRODUCED and not imported: the marker contract's own harness
    names a cross-kit edge as the forbidden shape and says the deliverable is agreement, proven.

    The ONE divergence: zero opens AND zero closes returns None rather than raising, because that is
    the first-apply case the shipped splice has no reason to support and this writer must.
    """
    lines = text.split("\n")

    def _is(line: str, mark: str) -> bool:
        # ONE trailing CR, not all of them — `rstrip("\r")` would accept a line ending in two CRs
        # that the other readers refuse. Asserted at SOURCE by the contract harness, because on an
        # MSYS node the runtime strips CR before a fixture can observe it.
        return (line[:-1] if line.endswith(CR) else line) == mark

    opens = [i for i, l in enumerate(lines) if _is(l, open_m)]
    closes = [i for i, l in enumerate(lines) if _is(l, close_m)]
    if not opens and not closes:
        return None
    if len(opens) != 1 or len(closes) != 1:
        raise Refusal(f"expected exactly one marker pair, found {len(opens)} open and "
                      f"{len(closes)} close")
    if closes[0] < opens[0]:
        raise Refusal("the closing marker precedes the opening one")
    return opens[0], closes[0]


def write_block(text: str | None, open_m: str, close_m: str, block: str,
                insert: str) -> tuple[str, str]:
    """Splice, append or create. Returns (new text, mode).

    The APPEND never joins two lines. MEASURED: appending to a file whose last line lacks a trailing
    newline produces a concatenated line that destroys the target's own final rule, makes git report
    an invalid attribute name on every attribute query in that repository, and leaves the block's
    open marker off column 0 — so every later apply refuses forever while the receipt claims a block
    that can never be found again.
    """
    if text is None:
        return block + "\n", "created"
    span = find_block(text, open_m, close_m)
    if span is not None:
        lines = text.split("\n")
        i, j = span
        return "\n".join(lines[:i] + block.split("\n") + lines[j + 1:]), "spliced"
    if insert == "refuse":
        raise Refusal("the destination exists and carries no marker pair, and this rule declares "
                      "insert = \"refuse\": its position is SEMANTIC, and guessing one in a file the "
                      "target owns is a behavioural change to their tooling")
    sep = "" if (not text or text.endswith("\n")) else "\n"
    return text + sep + block + "\n", "appended"


def fnmatchcase_path(path: str, pattern: str) -> bool:
    """Does a gitattributes-shaped pattern cover this path? Used ONLY to report a pin that governs
    nothing — never to decide what the renormalize touches, which is git's own answer."""
    import fnmatch
    if pattern.startswith("**/"):
        pattern = pattern[3:]
    pat = pattern.replace("/**/", "/*/")
    return (fnmatch.fnmatchcase(path, pattern) or fnmatch.fnmatchcase(path, pat)
            or fnmatch.fnmatchcase(pathlib.PurePosixPath(path).name, pattern))


GA_BLOCK_ID = "govkit:lf-pins"


def lf_pin_block(pins: list[tuple[str, str, str]]) -> tuple[str, str, str]:
    """(open-marker, close-marker, block text) for a resolved pin set.

    DEPL-dCarriedReceipt-2 S2. `apply` WRITES this block and `update` RECOMPUTES it to decide
    whether gov's pins have moved, so the construction lives in one place. Two copies would drift
    and the comparison would fail open -- reporting `pins-moved` forever, or `current` forever, and
    neither is distinguishable from a correct answer without reading both copies.
    """
    om, cm = marker_pair("hash-comment", GA_BLOCK_ID)
    body = [om, "# GENERATED by govkit apply. Edit the kits' descriptors, not this block."]
    for pat, claimant, why in pins:
        body.append(f"# {claimant}" + (f" — {why}" if why else ""))
        body.append(f"{pat} text eol=lf")
    body.append(cm)
    return om, cm, "\n".join(body)


def eol_population(target: pathlib.Path) -> dict[str, str]:
    """Ask GIT which tracked paths resolve to which `eol` value. Never a pattern match.

    An attributes PATTERN and a git PATHSPEC are different languages, and feeding one string to both
    is wrong in BOTH directions on the exact patterns this seeds: `memory/**/*.md` as an attribute
    matches a file at depth 1, as a pathspec it does not; `memory/*.md` as a pathspec crosses a
    directory separator, as an attribute it does not. So the population is git's own answer, and the
    literal paths it returns are what the renormalize touches and what the post-condition re-reads.
    """
    files = subprocess.run(["git", "-C", str(target), "ls-files", "-z"],
                           capture_output=True, text=True).stdout.split("\0")
    files = [f for f in files if f]
    if not files:
        return {}
    out = subprocess.run(["git", "-C", str(target), "check-attr", "--stdin", "-z", "eol"],
                         input="\0".join(files), capture_output=True, text=True)
    fields, res = out.stdout.split("\0"), {}
    for i in range(0, len(fields) - 2, 3):
        path, _attr, value = fields[i], fields[i + 1], fields[i + 2]
        if value not in ("unspecified", "unset", ""):
            res[path] = value
    return res


def lf_pins(descs: dict, selection: list[str], ctx_of) -> list[tuple[str, str, str]]:
    """(pattern, claimant, why-first-line) for the selection, deduped and sorted.

    Sorted so the block's bytes are stable at any selection order — otherwise the same install
    produces different bytes depending on the order kits were named.

    The registry's `[[gov_only_pin]]` rows are DELIBERATELY not here. They exist so every eol pin in
    gov's own attributes file is accounted for by something — the same completeness claim the path
    exemptions make — and emitting them would put gov-internal rules about gov's own shell scripts
    and its own deployer into a target that receives neither.
    """
    seen: dict[str, tuple[str, str]] = {}
    for eid in selection:
        d = descs[eid][0]
        for pin in d.get("lf_pin", []):
            pat, miss = resolve_tokens(pin.get("pattern", ""), ctx_of(eid, d))
            if miss or not pat:
                raise Refusal(f"entry '{eid}' declares an lf_pin whose pattern needs answer "
                              f"'{miss[0] if miss else '?'}' — a literal brace written into "
                              f"somebody's .gitattributes matches nothing, forever")
            seen.setdefault(pat, (eid, str(pin.get("why", "")).strip().split("\n")[0]))
    return sorted((p, c, w) for p, (c, w) in seen.items())


# ------------------------------------------------------------------- the gate runner declaration
# ONE vocabulary, owned here. `make`, `npm` and `shell` are REFUSED BY NAME: refusing three and doing
# one well beats half-writing four, because a splice into a Makefile that half-works ships a target a
# leg that never runs while this tool exits 0 — the silent-green direction.
GR_KINDS = ("none", "manifest")

# THE OBSERVED-STATE TABLE, and it is the ONE spelling of it. Three copies existed: the reader's
# state tuple, the validator's string-check tuple, and the seed writer's hardcoded key list — and
# they disagreed. `observed_reused` was declared by the run-gates kit, read by nobody and emitted by
# nobody, so the kit.toml comment claiming it made the reused outcome reachable was describing a
# path that did not exist. `observed_held` then arrived with TOOL-dUnstalledConvoy-26 and reached
# none of the three, which made every upgrading adopter's `apply` report its held legs as VANISHED.
#
# ORDER IS SEMANTIC. `read_gate_verdicts` scans in this order and `setdefault` keeps the FIRST
# state a line matches, so a more specific verb must never sit behind a prefix of itself.
OBSERVED_STATES = (
    ("green", "observed_ran"),
    ("red", "observed_failed"),
    ("skipped", "observed_skipped"),
    ("reused", "observed_reused"),
    ("held", "observed_held"),
)
OBSERVED_KEYS = tuple(k for _s, k in OBSERVED_STATES)
# A state that means the leg DID NOT EXECUTE. Neither is a failure and neither is evidence of a
# pass; the dead-probe refusal below rests on exactly this distinction.
NOT_EXECUTED = ("skipped", "held")
GR_REQUIRED = ("file", "grammar", "dedupe_key", "command", "run_all_env",
               "observed_ran", "observed_failed")


def validate_gate_runner(deploy: dict, r: Report) -> dict:
    """Validate the declaration in the PRE-WRITE pass. Legs are emitted last, so a bad declaration
    discovered at emission time would refuse after everything else had landed."""
    gr = deploy.get("gate_runner") or {}
    if not gr:
        return {"kind": "absent"}
    kind = gr.get("kind")
    if kind in ("make", "npm", "shell"):
        r.fail(f"[gate_runner].kind = '{kind}' — this unit implements ONE grammar and refuses the "
               f"others by name rather than half-writing them; a splice that half-works ships a leg "
               f"that never runs while this tool exits 0")
        return gr
    if kind not in GR_KINDS:
        r.fail(f"[gate_runner].kind = '{kind}' is outside the vocabulary {GR_KINDS}")
        return gr
    if "anchor" in gr:
        r.fail("[gate_runner].anchor is refused: it is meaningful only for a line grammar this unit "
               "does not implement, and a key that parses and is ignored looks exactly like one "
               "that works")
    if kind == "none":
        return gr
    missing = [k for k in GR_REQUIRED if not gr.get(k)]
    if missing:
        r.fail(f"[gate_runner] declares kind = 'manifest' and is a PARTIAL promotion: "
               f"{', '.join(missing)} absent. A complete promotion supplies {', '.join(GR_REQUIRED)}")
    if gr.get("grammar") not in (None, "json-array"):
        r.fail(f"[gate_runner].grammar = '{gr.get('grammar')}' — only 'json-array' is implemented")
    if gr.get("dedupe_key") not in (None, "name"):
        r.fail(f"[gate_runner].dedupe_key = '{gr.get('dedupe_key')}' — only 'name' is implemented")
    # The observation templates are ITERATED by `read_gate_verdicts`, so a scalar is not a
    # near-miss — it is walked character by character and silently classifies every line green.
    # Refused BY NAME here rather than left to the reader, because the reader's failure is silent
    # and this one is not. The assertion is what stops the next kit repeating it.
    for _obs in OBSERVED_KEYS:
        if isinstance(gr.get(_obs), str):
            r.fail(f"[gate_runner].{_obs} is a STRING; it must be an array of templates. Its only "
                   f"consumer iterates it, so a string is walked character by character: the head "
                   f"becomes one character, no leg name is ever recovered, and every line is "
                   f"classified by whichever state is scanned first")
    if isinstance(gr.get("command"), str):
        r.fail("[gate_runner].command is a STRING; it must be an argv array. Splitting a shell "
               "string is a guess about quoting this tool has no way to check, so it refuses "
               "rather than splits")
    ci = gr.get("ci") or {}
    if ci and ci.get("system") != "github-actions":
        r.fail(f"[gate_runner.ci].system = '{ci.get('system')}' — the only CI grammar this repo has "
               f"ever measured is github-actions")
    return gr


# The run-gates version at which `subject` entered the manifest's pinned key set. Below it, the
# target's own canary refuses the key. TOOL-dUnstalledConvoy-26.
SUBJECT_FLOOR_RUN_GATES = (1, 1)


def check_target_reads_subject(target: pathlib.Path, deploy: dict) -> bool:
    """Can this target's installed run-gates parse a `subject` key without redding its own canary?

    Read from the TARGET, never assumed and never taken from gov's own tree: the question is what
    THEY have installed. A tree with no run-gates at all gets the key — there is no canary to red,
    and withholding it would silently deny them the feature. An unreadable version is treated as
    BELOW the floor, because the direction that costs a feature is recoverable and the direction
    that reds somebody else's bar is not.
    """
    prefix = (deploy.get("prefix") or "tools").strip("/")
    runner = target / prefix / "run-gates" / "run-gates.sh"
    if not runner.is_file():
        return True
    try:
        txt = runner.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    m = re.search(r"^KIT_RUN_GATES_VERSION=([0-9]+(?:\.[0-9]+)*)", txt, re.M)
    if not m:
        return False
    try:
        got = tuple(int(x) for x in m.group(1).split("."))
    except ValueError:
        return False
    return got >= SUBJECT_FLOOR_RUN_GATES


def read_gate_verdicts(target: pathlib.Path, gr: dict) -> dict[str, str]:
    """Parse the target's runner output into leg name -> green|red|skipped.

    Run WITHOUT the run-everything escape, deliberately. Running both reads with it doubles the
    target's whole bar AND makes the dead-probe check unreachable, because with every guard
    overridden no leg can report skipped — a liveness half the regime forbids is not one.
    """
    cmd = gr.get("command") or []
    if not cmd:
        return {}
    # THROUGH THE RESOLVER, like every other leg argv. A [[hole]] discharge command is authored in a
    # kit descriptor and the shipped ones are `["bash", "-c", ...]` — the exact bare name that sends
    # this call to the WSL launcher on a Windows python, which is a different filesystem and a
    # different interpreter. Two sessions fixed this class independently and this was the one site
    # neither pass wired on its own: main resolved four, the merged branch found the fifth.
    out = subprocess.run(resolve_shell_argv(list(cmd)), cwd=str(target), capture_output=True, text=True)
    verdicts: dict[str, str] = {}
    for state, key in OBSERVED_STATES:
        for tmpl in (gr.get(key) or []):
            head = tmpl.split("{name}")[0]
            for line in (out.stdout + out.stderr).splitlines():
                # Line-anchored PREFIX, never whole-line equality: the runner's failure and skip
                # lines carry a variable tail — an exit code, a branch name — so a whole-line
                # literal matches NOTHING and every liveness half that rests on it is unreachable.
                if line.startswith(head) and len(line) > len(head):
                    verdicts.setdefault(line[len(head):].strip().split("  ")[0].strip(), state)
    return verdicts


def exempt_leg(descs: dict, selection: list[str], target: pathlib.Path, name: str,
               configure_skipped: set[str]) -> bool:
    """Is a leg that is red AFTER the install exempt? Two ways, and nothing else.

    The exemption is granted by RUNNING the hole's discharge probe, never by reading its flag. The
    measured defect next door is exactly that: `blocks_adopt` is read statically, so a kit is
    reported inert while its own hole's probe exits 0 in the landed tree.

    `red_after_land` is a WINDOW, scoped in BOTH consumers: it exempts only while that kit's
    configure phase was skipped THIS RUN. Unscoped it is a permanent exemption, under which an
    all-kits install can land a kit with its legs red forever and every criterion still pass.
    """
    for eid in selection:
        d, _p = descs[eid]
        for leg in d.get("gate_leg", []):
            if leg.get("name") != name:
                continue
            for h in d.get("hole", []):
                if not h.get("blocks_gate"):
                    continue
                cmd = (h.get("discharge") or {}).get("command")
                if not cmd:
                    continue
                ctx = {"kit": f"tools/{eid}", "prefix": "tools", "kit_id": eid,
                       "memory_root": "memory"}
                resolved = [resolve_tokens(a, ctx)[0] for a in cmd]
                try:
                    if subprocess.run(resolve_shell_argv(resolved), cwd=str(target),
                                      capture_output=True).returncode != 0:
                        return True          # the hole is genuinely undischarged, right now
                except OSError:
                    return False
            if leg.get("red_after_land") and eid in configure_skipped:
                return True
    return False


def hook_probe(target: pathlib.Path) -> tuple[str, str]:
    """Would the OPERATOR's landing commit be refused? Answered without creating a commit.

    Three-valued because two states share an exit code: git's hook runner exits non-zero BOTH when
    the hook refuses and when no hook exists. `--ignore-missing` is refused — it maps missing onto
    the same code as PASS, trading a visible collision for the dangerous one.
    """
    ver = subprocess.run(["git", "-C", str(target), "version"], capture_output=True, text=True)
    m = re.search(r"(\d+)\.(\d+)", ver.stdout or "")
    if m and (int(m.group(1)), int(m.group(2))) < (2, 36):
        return "unsupported", "git predates `git hook run`; nothing was probed"
    p = subprocess.run(["git", "-C", str(target), "rev-parse", "--git-path", "hooks/pre-commit"],
                       capture_output=True, text=True)
    hp = (target / p.stdout.strip()) if p.returncode == 0 else None
    if not hp or not hp.exists():
        return "no-hook", "the target has no pre-commit hook"
    out = subprocess.run(["git", "-C", str(target), "hook", "run", "pre-commit"],
                         capture_output=True, text=True)
    if out.returncode == 0:
        return "pass", ""
    return "block", (out.stdout + out.stderr).strip()


def classify_outcome(target: pathlib.Path, desc: dict, ctx: dict[str, str], rc: int) -> dict | None:
    """The DECLARED meaning of an adopter's exit code, decided by a filesystem PROBE.

    The exit-code collision is per BRANCH, not per kit: one shipped adopter exits 1 for six unrelated
    outcomes, so a code-to-meaning table cannot tell them apart and parsing stdout is fragile. Each
    `[[outcome]]` therefore declares what must and must not exist, and this RUNS that probe. Six
    descriptors declared these blocks and nothing read them, so an integer was the whole report.

    Returns the matching BLOCK, or None when none matches — reported as unclassified, never
    invented. The block rather than its `means` string, because the caller needs `ok` too: a
    descriptor declares whether a classified outcome is an ACCEPTED STOP or a failure, and reducing
    it to a name here would throw that away.
    """
    for oc in desc.get("outcome", []):
        if oc.get("code") != rc:
            continue
        probe = oc.get("probe") or {}
        ok = True
        for key, want in (("must_exist", True), ("must_not_exist", False)):
            spec = probe.get(key)
            if not spec:
                continue
            for p in (spec if isinstance(spec, list) else [spec]):
                resolved, miss = resolve_tokens(p, ctx)
                if miss:
                    ok = False
                    break
                if (target / resolved).exists() is not want:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return oc
    return None


def resolve_dests(desc: dict, rule: dict, src: str, ctx: dict, home: str) -> list[tuple[str, list[str]]]:
    """Where one source lands under a rule, as `(destination, unresolved-answer-keys)` pairs.

    ONE spelling, called by `plan`, by the write loop, and by the wildcard exclusion — each has to
    ask the same question the writer will answer, and two computations of one thing is the class this
    repo keeps a record about. DEPL-dCarriedReceipt-1: that claim was false for `{relpath}`, which
    this function resolved as a BASENAME while `destinations_for` resolved it through
    `rule_relpath`. push-main's hook rule declares `to = "{relpath}"` over `.githooks/pre-push`, so
    the writer landed a bare `pre-push` at the target ROOT while the same rule's own `claims` spelled
    `.githooks/pre-push`. Both now call `rule_relpath`, and `selfcheck` asserts the CLASS: every
    rule declaring both `to` and `claims` must resolve into its own claims.

    THE `missing` LIST IS RETURNED, not dropped. An earlier cut called `resolve_tokens(...)[0]` and
    discarded it, so `apply --kits kickoff-manifest` with no `manifest_path` answer wrote a file
    named literally `{manifest_path}` and exited 0, while `plan` exited 1 refusing the same install.
    A destination with an unresolved token is not a destination.

    An explicit `to` WINS for every role. Defaulting engine files to the kit-relative form regardless
    is how a flat entry — one with no kit directory at all — silently lands under a directory it does
    not have. The default applies only where the rule declared no destination.
    """
    if rule.get("to"):
        rel = rule_relpath(desc, rule, src)
        return [resolve_tokens(x.replace("{relpath}", rel), ctx)
                for x in (rule["to"] if isinstance(rule["to"], list) else [rule["to"]])]
    rel = src[len(home) + 1:] if home and src.startswith(home + "/") else \
        pathlib.PurePosixPath(src).name
    return [(f"{ctx['kit']}/{rel}", [])]


def resolve_rule_pool(root: pathlib.Path, desc: dict, rule: dict, ctx: dict, home: str) -> list[str]:
    """The source paths a rule actually lands. ONE spelling for `plan` AND `apply`.

    THIS SEAM EXISTS BECAUSE THE TWO DISAGREED. `plan` resolved sources through `rule_sources()`,
    which skips any include containing a glob character — so a `**` rule produced ZERO plan rows
    while `apply` pooled every tracked file under `home`. Measured on the lexicon kit: plan printed
    3 writes, apply landed 12. Ten of this repo's nineteen descriptors carry a `**` engine rule, so
    an operator approving a plan was approving a fraction of what would be written — and the files
    that went unlisted are exactly the ones a re-apply overwrites.

    A deployer whose preview disagrees with its action is worse than one that simply does the wrong
    thing, because the wrong thing is at least visible.
    """
    inc = rule.get("include")
    srcs = inc if isinstance(inc, list) else ([inc] if inc else [])
    if any(s == "**" for s in srcs):
        claimed = scan_claimed_paths(desc, rule, ctx, home)
        return [f for f in tracked(root)
                if home and f.startswith(home + "/")
                and not ({d for d, _m in resolve_dests(desc, rule, f, ctx, home)} & claimed)]
    return rule_sources(desc, rule)


def scan_claimed_paths(desc: dict, wildcard_rule: dict, ctx: dict, home: str) -> set[str]:
    """Every DESTINATION some other rule in this descriptor already owns.

    A `**` include means "everything not otherwise claimed" — which is how every descriptor author
    has read it, and what the engine did NOT implement. It pooled every tracked file under `home` and
    wrote each one unconditionally, so a rule declared LATER never got the chance to protect its own
    file. Measured against `drift-audit`: an adopter's edit to the `project-owned` `drift_signals.py`
    was destroyed by every re-apply, silently, with the descriptor reading exactly as intended.

    CLAIMED BY DESTINATION, NOT BY SOURCE, and the distinction was measured rather than reasoned.
    Excluding claimed SOURCES too is the obvious first cut and it UNDER-LANDS: `drift_signals.template.py`
    is the seed rule's source, its `**` destination is `{kit}/drift_signals.template.py`, and nothing
    else claims that path — so a source-based exclusion silently stopped shipping the adopter the
    template their own re-seed depends on. Measured: 8 files landed before, 6 after, and the two
    missing were not the two being protected.

    A destination claim covers both real cases. `project-owned` names `drift_signals.py`, which
    resolves to `{kit}/drift_signals.py` — the path it owns and, being non-landable, could not
    otherwise defend. `seed` names a different source but lands ON that same path, so its "copied
    ONCE, then the target owns it" guard is protected by the same test.
    """
    claimed: set[str] = set()
    for other in desc.get("files", []):
        if other is wildcard_rule:
            continue
        inc = other.get("include")
        srcs = inc if isinstance(inc, list) else ([inc] if inc else [])
        if any(s == "**" for s in srcs):
            continue  # two wildcards claim nothing FROM each other; neither is more specific
        for s in rule_sources(desc, other):
            claimed.update(d for d, _m in resolve_dests(desc, other, s, ctx, home))
    return claimed


def blob_at(root: pathlib.Path, commit: str, path: str) -> bytes | None:
    """Bytes from the gov git INDEX at a recorded commit — never from the working tree.

    This is the receipt's whole provenance claim. Reading the working tree would make the receipt
    say "these bytes came from <commit>" about bytes that came from whatever the operator had
    checked out and half-edited at the time.
    """
    out = subprocess.run(["git", "-C", str(root), "show", f"{commit}:{path}"],
                         capture_output=True, check=False)
    return out.stdout if out.returncode == 0 else None


# ---------------------------------------------------------------- the two identities (DEPL-dCarriedReceipt-7)
# `gov_oid` is the git blob GOV shipped at a row's `commit`. `oid` is the git blob the TARGET holds,
# read from its INDEX. One receipt field was being asked to be both: `classify_row` compared `sha256`
# against the target's WORKTREE bytes while `check` compared the same field against gov's blob, and
# both claims hold only where the target's worktree is byte-identical to what gov shipped — false for
# any adopter whose clone applies a line-ending filter. Measured on a `core.autocrlf=true` clone of a
# memory-tree install: 23 of 24 engine rows read `patched` with nothing edited.
def blob_oid(data: bytes) -> str:
    """Git's object name for these bytes — the string `git hash-object --stdin` would print.

    Computed rather than spawned, because both callers already hold the bytes: `apply` has gov's
    blob in hand and `update` has just read it through `blob_at`. The rule is git's own and not a
    hash of this tool's choosing — the header is `blob <byte-length>` and a NUL.

    WHAT THIS DOES NOT COVER, stated because a structural check reads as a semantic one: a
    repository on the sha256 object format names the same bytes differently, and gov is sha1 like
    every repo this deployer has met. A target on the other format would read every identity as
    DIFFERING, which is the safe direction — `differs` reaches only `patched` and `diverged`, and no
    raw write sits on either.
    """
    return hashlib.sha1(b"blob %d\0" % len(data) + data,  # noqa: S324 - git's object name, not a MAC
                        usedforsecurity=False).hexdigest()


def index_read(target: pathlib.Path, paths: list[str]) -> tuple[dict[str, tuple[str, str]], set[str]]:
    """The TARGET's index, batched: `(path -> (mode, oid))` at STAGE 0, and every path at ANY stage.

    ONE `ls-files -s -z` over the receipt's whole path list rather than one read per row (§8 F2).
    Chunked, because a receipt can outgrow a command line and this one is measured in the hundreds
    on a live adopter.

    TWO return values because two questions need different populations. The map answers "what blob
    does the target hold", and only a stage-0 entry answers it: an unmerged path carries stages 1-3
    and no stage 0, and reading a merge stage as the target's blob answers a question nobody asked.
    The SET is every path with any entry at all, so `-7` S4's absent-from-the-index refusal does not
    fire on a path that is merely unmerged — that state is `-12` S3's refusal, one step earlier, and
    two units refusing one state hand the operator two different messages for it.
    """
    at_stage0: dict[str, tuple[str, str]] = {}
    present: set[str] = set()
    for i in range(0, len(paths), 400):
        chunk = paths[i:i + 400]
        if not chunk:
            continue
        out = subprocess.run(["git", "-C", str(target), "ls-files", "-s", "-z", "--", *chunk],
                             capture_output=True, text=True, check=False)
        for rec in out.stdout.split("\0"):
            if not rec.strip():
                continue
            meta, _tab, pth = rec.partition("\t")
            bits = meta.split()
            if len(bits) < 3 or not pth:
                continue
            mode, oid, stage = bits[0], bits[1], bits[2]
            present.add(pth)
            if stage == "0":
                at_stage0[pth] = (mode, oid)
    return at_stage0, present


def index_blob(target: pathlib.Path, oid: str) -> bytes | None:
    """The bytes behind an index entry, from the target's object database and never from its disk.

    Called ONLY where the bytes themselves are needed — the three-way merge, the order it writes on
    a conflict, and DEPL-dCarriedReceipt-9's rung ladder. Every VERDICT is still decided from the OID
    alone, and a byte-identical row still costs nothing; what the rungs added is one spawn per row
    whose index blob is NOT gov's own, because `eol` and `relocate` are questions about bytes and no
    oid comparison can answer either. The spec's perf line claimed "no new subprocess" and that is
    wrong on this arm — stated here rather than left for the next reader to discover.
    """
    out = subprocess.run(["git", "-C", str(target), "cat-file", "blob", oid],
                         capture_output=True, check=False)
    return out.stdout if out.returncode == 0 else None


def gov_tree_mode(root: pathlib.Path, commit: str, path: str) -> str | None:
    """The file mode gov's own tree records for a path at a commit.

    §8 F1: a row with no existing index entry in the target takes THIS mode rather than a literal
    `100644`. A hook that lands non-executable is a hook that does not run.
    """
    out = subprocess.run(["git", "-C", str(root), "ls-tree", commit, "--", path],
                         capture_output=True, text=True, check=False)
    if out.returncode != 0 or not out.stdout.strip():
        return None
    mode = out.stdout.split()[0]
    return mode if mode in ("100644", "100755", "120000") else None


def foreign_kit_present(target: pathlib.Path, descs: dict[str, tuple[dict, str]],
                        receipt: dict | None) -> list[str]:
    """Registry entries resolvable in the target that THIS target's receipt does not claim.

    The unqualified form of this predicate refuses every re-run the unit designs for: after the
    first apply, a version constant resolves AND a receipt exists, so idempotency, `--resume` and
    a re-apply all become unreachable. The carve-out is the receipt: a kit this target's own receipt
    claims is the authorized path and proceeds.
    """
    claimed = set((receipt or {}).get("kits") or [])
    found = []
    for eid, (d, _p) in descs.items():
        if eid in claimed:
            continue
        # Probe the entry's DECLARED destinations, at both the canonical and the root prefix. An
        # earlier form guessed a kit-relative path from the entry id, which missed every FLAT entry
        # — the ones with no kit directory at all — so a target already carrying one of those was
        # not detected as kitted. Caught by this file's own arm.
        probes: list[str] = []
        vf = d.get("version_from") or {}
        vf_name = pathlib.PurePosixPath(vf["file"]).name if vf.get("file") else None
        for prefix in ("tools", ""):
            ctx = {"prefix": prefix, "kit_id": eid,
                   "kit": f"{prefix}/{eid}" if prefix else eid, "memory_root": "memory"}
            for rule in d.get("files", []):
                # A `merged` destination is a file the TARGET owns and gov writes a region of, so its
                # existing is the normal case and not evidence of a foreign kit. Probing it made the
                # git hooks directory — which almost every repo has — read as a kit already
                # installed, and refused the install before writing anything.
                if rule.get("role") == "merged":
                    continue
                for dest in rule_destinations(d, rule):
                    resolved, missing = resolve_tokens(dest, ctx)
                    if missing:
                        continue
                    if vf_name is None or pathlib.PurePosixPath(resolved).name == vf_name:
                        probes.append(resolved)
            if vf_name:
                probes.append(f"{prefix}/{eid}/{vf_name}" if prefix else f"{eid}/{vf_name}")
        if d.get("sentinel"):
            probes.append(d["sentinel"])
        for pr in dict.fromkeys(probes):
            if pr and (target / pr).exists():
                found.append(f"{eid} (at {pr})")
                break
    return found


# ------------------------------------------------ write preconditions and the outbox write lock
# DEPL-dCarriedReceipt-12. The FIRST gate a write passes, and it is SHARED because both writing
# verbs have the same exposure: `apply` lands bytes and rewrites `.gitattributes`, `update` lands
# bytes and re-stamps the receipt, and only one of them shipped a guard — a guard that was dead in
# the linked-worktree layout adopters are told to use. Every refusal here names the condition, the
# marker or path that tripped it, and what to do about it; there is deliberately no `--force`.

IN_PROGRESS_MARKERS = ("MERGE_HEAD", "REBASE_HEAD", "CHERRY_PICK_HEAD")

# One spelling of where the lock lives. Both verbs take it and the refusal prints it, so a second
# literal would be a second answer to the same question.
WRITE_LOCK_REL = ".governance/outbox/.update.lock"

# The lock THIS process created, and nothing else. A run that REFUSED on somebody else's lock must
# never unlink the file it just refused over, which is the one way a lock becomes an amplifier.
_HELD_LOCK: pathlib.Path | None = None


def git_path(target: pathlib.Path, name: str) -> pathlib.Path:
    """Where git ACTUALLY keeps <name> for this working tree.

    Never `target/.git/<name>`. In a LINKED WORKTREE `.git` is a file and the per-worktree state
    lives under the host repo's `.git/worktrees/<id>/`, so the path stat resolves to nothing and
    every probe built on it reports a clean tree in the middle of a merge — reproduced live before
    this was written. `--git-path` is the form `hook_probe` already uses; this is that same answer
    rather than a second one. It returns a working-tree-relative path in a normal repo and an
    ABSOLUTE one in a linked worktree, and joining an absolute right-hand side yields it unchanged.
    """
    out = subprocess.run(["git", "-C", str(target), "rev-parse", "--git-path", name],
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise Refusal(
            f"git could not resolve --git-path {name} in {target.as_posix()}: "
            f"{out.stderr.strip()} — refusing rather than falling back to .git/{name}, which is "
            f"the guess that is wrong in every linked worktree")
    return target / out.stdout.strip()


def demand_no_operation_in_progress(target: pathlib.Path, verb: str) -> None:
    """S1 + S2. Asked of BOTH verbs and conditioned on NOTHING.

    It used to sit inside `if pins:`, so a target declaring no `lf_pin` was unguarded even in the
    layout where the old path form happened to work.
    """
    for marker in IN_PROGRESS_MARKERS:
        p = git_path(target, marker)
        if p.exists():
            raise Refusal(
                f"the target has {marker} at {p.as_posix()} — a merge, rebase or cherry-pick is in "
                f"progress. `{verb}` writes gov-owned paths and STAGES them, and a `git add` over a "
                f"path carrying conflict stages collapses all three of them: both sides of your "
                f"merge become unrecoverable, and renormalizing mid-conflict rewrites index stages "
                f"nobody can reconstruct. Finish or abort that operation in the target, then re-run")


def demand_index_resolved(target: pathlib.Path, verb: str) -> None:
    """S3. `ls-files -u` asks the question directly — which paths carry more than one index stage."""
    out = subprocess.run(["git", "-C", str(target), "ls-files", "-u", "-z"],
                         capture_output=True, text=True)
    paths = sorted({row.split("\t", 1)[1] for row in out.stdout.split("\0") if "\t" in row})
    if paths:
        raise Refusal(
            f"{len(paths)} path(s) in the target's index carry unresolved merge stages: "
            + ", ".join(paths) +
            f" — `{verb}` stages what it writes, and one `git add` over such a path collapses its "
            f"three stages to one, with both sides of the merge unrecoverable afterwards. Resolve "
            f"them in the target (or `git merge --abort`), then re-run")


def dirty_claimed_paths(target: pathlib.Path, claimed: list[str]) -> list[str]:
    """S4, and the DEFINITION of dirty for this whole build, implemented in one place.

    A claimed path is dirty when it differs index-versus-HEAD or worktree-versus-index — `git diff
    --cached` and `git diff` over that path, and deliberately NOT `git status --porcelain`, which
    also flags `??`. Two carve-outs, and each of them is a state another unit owns:

    - Absent from BOTH the index and the worktree: dirty when HEAD still carries it, because that
      is a STAGED deletion and a staged deletion is an operator decision. NOT dirty when HEAD has
      no copy either — that is the COMMITTED deletion `-9` restores, and there is nothing left to
      diff.
    - An untracked file SHADOWING a claimed path that is absent from the index is NOT dirty here.
      That state is `-7` S4's refusal, which names the path and the risk, and two units refusing
      one tree would give the operator two different messages for it.

    Four git calls over the whole population rather than four per path: a hundred-row receipt would
    otherwise pay four hundred process creations, and on the node that measured it every exec costs
    about 22 ms whatever it does.
    """
    claimed = [c for c in dict.fromkeys(claimed) if c]
    if not claimed:
        return []

    def _names(*args: str) -> set[str]:
        out = subprocess.run(["git", "-C", str(target), *args, "--", *claimed],
                             capture_output=True, text=True)
        return {n for n in out.stdout.split("\0") if n}

    in_index = _names("ls-files", "-z")
    has_head = subprocess.run(["git", "-C", str(target), "rev-parse", "--verify", "-q", "HEAD"],
                              capture_output=True).returncode == 0
    in_head = _names("ls-tree", "-r", "--name-only", "-z", "HEAD") if has_head else set()
    # index-versus-HEAD is unanswerable before the first commit, and calling every staged path an
    # addition there would report a fresh repository as entirely dirty. The worktree-versus-index
    # half still answers, so that is the half that runs.
    staged = _names("diff", "--cached", "--name-only", "-z", "HEAD") if has_head else set()
    unstaged = _names("diff", "--name-only", "-z")

    dirty: list[str] = []
    for path in claimed:
        if path not in in_index:
            if (target / path).exists():
                continue                        # carve-out 2 — `-7` S4 owns this tree
            if path in in_head:
                dirty.append(f"{path} (deleted from the index, still in HEAD)")
            continue                            # carve-out 1 — a committed deletion is not dirty
        if path in staged or path in unstaged:
            dirty.append(path)
    return dirty


def demand_claimed_paths_clean(target: pathlib.Path, verb: str, receipt: dict | None) -> None:
    """S4's refusal, scoped to the receipt's own population.

    A deployer that refuses over an unrelated edit in a repository it does not own is a deployer
    people learn to work around, so a dirty path outside the receipt does not block.
    """
    dirty = dirty_claimed_paths(
        target, [row.get("path") for row in ((receipt or {}).get("files") or [])])
    if dirty:
        raise Refusal(
            f"{len(dirty)} path(s) this target's receipt claims are DIRTY: " + ", ".join(dirty)
            + f" — `{verb}` overwrites gov-owned paths, and a write onto an uncommitted local "
            f"change is indistinguishable afterwards from a change you made. Commit or stash those "
            f"paths in the target, then re-run. A dirty path OUTSIDE the receipt does not block")


def describe_write_lock(lock: pathlib.Path) -> str:
    """Who holds the lock and for how long — or the fact that the file cannot say.

    An unreadable lock is reported as unreadable rather than described as anonymous: a stale lock
    an operator cannot diagnose is indistinguishable from a live run they must wait for.
    """
    try:
        held = json.loads(lock.read_text(encoding="utf-8"))
        age = int(max(0.0, time.time() - float(held.get("started") or 0.0)))
        return (f"pid {held.get('pid', '?')} running `{held.get('verb', '?')}`, started "
                f"{held.get('started_utc', '?')}, {age}s ago")
    except (OSError, ValueError, TypeError):
        return "its lock file records no readable pid or start time, so it is almost certainly stale"


def take_write_lock(target: pathlib.Path, verb: str) -> None:
    """S5. `O_EXCL`, so the CREATION is the acquisition rather than a check followed by a create.

    Per TARGET, not per (target, verb): `apply` and `update` both write the receipt, so letting the
    two interleave is the case this exists for. The file records who holds it and since when,
    because a lock that refuses without saying who holds it is a mystery rather than an error.
    """
    global _HELD_LOCK
    lock = target.joinpath(*WRITE_LOCK_REL.split("/"))
    lock.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise Refusal(
            f"another govkit write holds {lock.as_posix()} — {describe_write_lock(lock)}. Two "
            f"writing runs against one target interleave on the receipt, which is exactly what "
            f"this lock exists to prevent, so `{verb}` is refusing rather than joining in. Wait "
            f"for that run to finish; if that process is gone the lock is STALE and `rm "
            f"{lock.as_posix()}` clears it") from None
    with os.fdopen(fd, "w", newline="\n") as fh:
        fh.write(json.dumps({"pid": os.getpid(), "verb": verb, "started": time.time(),
                             "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())},
                            indent=2) + "\n")
    _HELD_LOCK = lock


def release_write_lock() -> None:
    """Run by every exit path of both writing verbs, refusals included — it is a `finally`, never a
    line at the bottom of a success branch. A lock only a clean run releases is a lock that survives
    the first refusal and then blocks every run after it."""
    global _HELD_LOCK
    if _HELD_LOCK is None:
        return
    try:
        _HELD_LOCK.unlink()
    except OSError:
        pass
    _HELD_LOCK = None


def demand_writable_target(target: pathlib.Path, verb: str, receipt: dict | None) -> None:
    """Steps 1 and 2 of the build's precondition order, in that order, for a run that WILL write.

    A read-only run does not come here, on purpose: taking the lock creates `.governance/outbox/`
    and a file inside it, and a read-only verb that leaves a byte behind is the whole risk
    `update`'s default guards against. There is nothing for these preconditions to protect on a run
    that writes nothing.
    """
    demand_no_operation_in_progress(target, verb)
    demand_index_resolved(target, verb)
    demand_claimed_paths_clean(target, verb, receipt)
    take_write_lock(target, verb)


def demand_forward_vintage(root: pathlib.Path, base_commit: str | None, to_commit: str) -> None:
    """S7. `--to` must be a DESCENDANT of the vintage the receipt records.

    `--is-ancestor` holds reflexively, so a re-run at the same vintage stays legal, and a receipt
    carrying no `gov_commit` skips the question entirely — the same carve-out the resolve-check
    beside this one already makes. Asked of git rather than modelled here: a second model of the
    commit graph inside govkit is a second answer to a question git already owns.
    """
    if not base_commit:
        return
    ok = subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor",
                         base_commit, to_commit], capture_output=True).returncode == 0
    if not ok:
        raise Refusal(
            f"--to resolves to {to_commit} and this target's receipt records {base_commit}, which "
            f"is not an ancestor of it. A DOWNGRADE IS NOT AN UPDATE: every clean row takes the raw "
            f"arm rather than the three-way, so it would be rewound to the older bytes, and the "
            f"receipt would be re-stamped backwards so that nothing afterwards records it happened. "
            f"Pass a --to that descends from {base_commit}, or re-install deliberately if a "
            f"rollback is really what you want")


def demand_published_vintage(root: pathlib.Path, to_commit: str) -> None:
    """S8. `--to` must be reachable from SOME ref in the gov checkout.

    `rev-parse --verify` accepts any object that EXISTS — a dangling commit, a fetched-but-unmerged
    tip — which is how a branch nobody shipped becomes an adopter's new baseline. It is the same
    class the read side refuses by declining `git log --all`, and refusing it on the write side too
    keeps one answer to the question of what vintage an adopter may be moved to.
    """
    out = subprocess.run(["git", "-C", str(root), "for-each-ref", "--contains", to_commit,
                          "--count=1"], capture_output=True, text=True)
    if out.returncode != 0 or not out.stdout.strip():
        raise Refusal(
            f"--to resolves to {to_commit}, which this gov checkout can reach from NO ref — a "
            f"dangling commit, a deleted branch tip, or something fetched and never merged. The "
            f"object existing is not the same as it having been shipped, and an adopter may only "
            f"be moved to a vintage some ref names. Point --to at a branch or tag containing it")


def cmd_apply(root: pathlib.Path, target: pathlib.Path, mode: str, kits: list[str],
              resume: bool) -> int:
    """The verb. Its BODY is `_cmd_apply`, and the split exists for the lock's release path.

    S5 wants the lock released on EVERY exit — the clean return, each report emit, and every
    refusal — and a `finally` around the whole body is the only shape that also covers a
    Refusal raised out of a helper three frames down. A release line at the bottom of the
    success branch is the shape that leaves a stale lock behind after the first refusal.
    """
    try:
        return _cmd_apply(root, target, mode, kits, resume)
    finally:
        release_write_lock()


def _cmd_apply(root: pathlib.Path, target: pathlib.Path, mode: str, kits: list[str],
               resume: bool) -> int:
    r = Report()
    reg = load_toml(root / "tools" / "govkit" / "registry.toml")
    descs = read_descriptors(root, reg, r)
    if r.problems:
        return r.emit()
    # Target IDENTITY first, before anything is read out of it. A refusal about WHICH repository
    # this is must not queue behind a complaint about that repository's contents.
    if pathlib.Path(root).resolve() == target.resolve():
        raise Refusal("--target resolves to the gov checkout itself; deploying into this repo is a "
                      "stated non-goal and would be indistinguishable from a self-overwrite")

    deploy = load_deploy(target)
    selection = resolve_selection(reg, descs, mode, kits)
    commit = git(root, "rev-parse", "HEAD").strip()

    receipt_path = target / ".governance" / "install.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.is_file() else None
    if resume and receipt is None:
        raise Refusal("--resume needs an existing receipt; there is no install here to resume")

    # ---- AC8: refuse a FOREIGN kit before writing anything. A kit this target's own receipt claims
    # ---- is the authorized re-run and proceeds.
    foreign = foreign_kit_present(target, descs, receipt)
    if foreign and not resume:
        raise Refusal(
            "the target already carries " + ", ".join(sorted(foreign)) + " and this target's "
            "receipt does not claim it. Converging a repo that already has kits is a stated "
            "non-goal; refusing before writing anything"
        )

    # ---- THE WRITE PRECONDITIONS (DEPL-dCarriedReceipt-12), steps 1 and 2 of the build's
    # ---- declared order: is the target mid-operation, does its index carry unresolved merge
    # ---- stages, is any receipt-claimed path dirty, and can the lock be taken. All of it
    # ---- BEFORE the descriptor validation below, because a refusal about the state of the
    # ---- repository must not queue behind a complaint about a kit descriptor.
    demand_writable_target(target, "apply", receipt)

    # ---- validate every merged rule BEFORE writing. A source that cannot yield exactly one pair,
    # ---- or a marker style with no synthesizer, is a refusal — a block gov writes and can never
    # ---- find again is worse than one it never wrote.
    for eid in selection:
        d0 = descs[eid][0]
        for rule in d0.get("files", []):
            if rule.get("role", "engine") != "merged":
                continue
            style, bid = rule.get("marker_style"), rule.get("block_id")
            if not bid:
                r.fail(f"entry '{eid}' declares a merged rule with no block_id")
                continue
            if style == "json-pointer":
                if not (d0.get("adopt") or {}).get("argv"):
                    r.fail(f"entry '{eid}' declares a json-pointer merged rule and no adopter to "
                           f"delegate to — govkit does not write that document itself")
                continue
            try:
                om, cm = marker_pair(style, bid)
            except Refusal as e:
                r.fail(f"entry '{eid}': {e}")
                continue
            for src in rule_sources(d0, rule):
                blob = blob_at(root, commit, src)
                if blob is None:
                    continue
                try:
                    if find_block(blob.decode("utf-8", "replace"), om, cm) is None:
                        r.fail(f"entry '{eid}': its merged SOURCE {src} carries no '{bid}' marker "
                               f"pair, so there is no block to take — refusing rather than splicing "
                               f"the whole file into somebody's hook")
                except Refusal as e:
                    r.fail(f"entry '{eid}': merged source {src}: {e}")
    if r.problems:
        return r.emit()

    gr = validate_gate_runner(deploy, r)
    if r.problems:
        return r.emit()

    # ---- BASELINE. The target's OWN runner, read before any write. It EXECUTES target-authored
    # ---- code: the command comes from a file committed in the target repo, so anyone with commit
    # ---- access there chooses what runs on the operator's machine. The argv and the descriptor it
    # ---- came from are printed and recorded, and a CHANGE to either re-prompts.
    before_map: dict[str, str] = {}
    baseline = {"kind": gr.get("kind", "absent")}
    if gr.get("kind") == "manifest":
        print(f"govkit apply — the baseline will RUN, from this target's own .governance/deploy.toml:"
              f"\n                 {' '.join(gr.get('command') or [])}")
        step(STEP_BASELINE, "reading the target's own runner")
        before_map = read_gate_verdicts(target, gr)
        baseline["legs"] = before_map
        # A map with nothing green or red carries no information — every leg after the install
        # would land in the row that carries the exemptions. `held` joins `skipped` here by being
        # absent from the green/red test, which is what makes an all-held baseline refuse rather
        # than sail through on an empty map. TOOL-dUnstalledConvoy-26.
        if before_map and not any(v in ("green", "red") for v in before_map.values()):
            raise Refusal(
                "DEAD PROBE: the baseline read parsed legs but not one of them is green or red — a "
                "map that is entirely skipped carries no information, and every leg after the "
                "install would land in the row that carries the exemptions. Refusing rather than "
                "rerouting the whole install into its most forgiving branch")
        reds = [n for n, v in before_map.items() if v == "red"]
        if reds and (deploy.get("policy") or {}).get("on_baseline_red") == "refuse":
            raise Refusal(f"on_baseline_red = refuse and these legs are already red before this "
                          f"install: {', '.join(sorted(reds))}")
        if reds:
            print(f"govkit apply — {len(reds)} leg(s) were ALREADY red before this install: "
                  f"{', '.join(sorted(reds))} — reported, not fatal")
    else:
        step(STEP_BASELINE, "no runner declared" if gr.get("kind") == "none"
             else "this target's descriptor declares no [gate_runner] at all")

    rows: list[dict] = []       # every file gov is responsible for — the receipt, schema 3
    staged: list[str] = []      # only what this run actually wrote

    # ---- ATTRIBUTES. The pin block is written EARLY — before any content — because it is what the
    # ---- renormalize and every later checkout read. The PROBE and the renormalize are NOT here:
    # ---- they run last, after configure, because on a first install the pinned population does not
    # ---- exist yet (the memory tree is scaffolded by an adopter, the confs are adopter outputs, the
    # ---- rendered artifacts appear at configure). One phase would either refuse every first install
    # ---- or report success over nothing.
    # The UNION of this selection and whatever the receipt already claims. A narrower later apply
    # must not un-pin files whose kit is still installed — that would be invisible until somebody
    # re-checked-out on a foreign platform and a byte-comparing gate went red for reasons nothing
    # records.
    pins = lf_pins(descs, sorted(set(selection) | set((receipt or {}).get("kits") or [])),
                   lambda e, dd: target_context(target, deploy, e, dd))
    ga_path = target / ".gitattributes"
    if pins:
        # The mid-operation probe that used to stand HERE moved to the preamble
        # (DEPL-dCarriedReceipt-12 S1/S2). It was twice unreachable: conditioned on this very
        # `if pins:`, so a target declaring no `lf_pin` was unguarded, and stat'ing
        # `target/.git/<marker>`, which resolves to nothing in a linked worktree. WHY it
        # existed is unchanged and still worth writing down: cleanliness must be established
        # before this block is written, because `git add --renormalize` rewrites a
        # DELIBERATELY STAGED blob, and a tracked path deleted in the worktree makes it abort
        # entirely — staging nothing, after gov's block is already in the file.
        om, cm, block_text = lf_pin_block(pins)
        cur = ga_path.read_text(encoding="utf-8", errors="replace") if ga_path.is_file() else None
        new, mode = write_block(cur, om, cm, block_text, "append")
        ga_path.write_text(new, encoding="utf-8", newline="\n")
        subprocess.run(["git", "-C", str(target), "add", "--", ".gitattributes"],
                       capture_output=True, check=False)
        rows.append({"path": ".gitattributes", "role": "attributes", "kit": "(govkit)",
                     "version": "(synthesized)", "block_id": GA_BLOCK_ID,
                     "marker_style": "hash-comment", "mode": mode, "normalized": "lf",
                     "block_sha256": hashlib.sha256(
                         block_text.encode("utf-8")).hexdigest(),
                     "patterns": [p for p, _c, _w in pins], "written": True})
        step(STEP_ATTRIBUTES, f"{len(pins)} pin(s) [{mode}]")
    else:
        step(STEP_ATTRIBUTES, f"0 pin(s) declared by {', '.join(selection)} — nothing to write")

    # ---- LAND. Kit content from the index at `commit`, through the ONE resolver `plan` also calls.
    step(STEP_LAND, f"from {commit[:8]} into {target.as_posix()}")
    for eid in selection:
        d, _p = descs[eid]
        ctx = target_context(target, deploy, eid, d)
        home = (d.get("home") or "").rstrip("/")
        written_here = scan_written_destinations(root, d, ctx, home)
        produced_here = scan_produced_destinations(d, ctx)
        for rule in d.get("files", []):
            role = rule.get("role", "engine")
            if role not in LANDABLE_ROLES or rule.get("scope") == "machine" or rule.get("link"):
                # A SKIP IS AN OUTCOME, NOT HOUSEKEEPING. This used to be a bare `continue`, so a
                # `plan` promising two playbook files was followed by `landed 0 file(s)` and exit 0
                # with neither skip named on either side. One line per rule, with the same kind the
                # preview printed, so the two verbs are legible against each other.
                for dest, _miss in _resolve_skip_destinations(root, d, rule, ctx, home):
                    kind = derive_rule_kind(eid, d, rule, dest, written_here, produced_here, r)
                    print(f"govkit apply — SKIPPED [{role:<13}] {dest} <- {eid}: "
                          f"{SKIP_REASONS.get(kind, 'not a role this verb lands')}")
        res = resolve_entry(root, d, ctx)
        vers = entry_version(root, d)

        # Every rule that does NOT land says so, by role, naming who does produce it. The silent
        # skip this replaces swallowed thirteen rules across the shipped descriptors.
        # ---- MERGED. A gov-owned region inside a file the target owns. The block is taken from the
        # ---- SOURCE's own pair and written through the one region writer; an edit OUTSIDE it
        # ---- survives by construction, because replacement is by line index and never a regex.
        for rule in d.get("files", []):
            if rule.get("role", "engine") != "merged":
                continue
            style = rule.get("marker_style")
            if style == "json-pointer":
                continue          # delegated at CONFIGURE, below
            om, cm = marker_pair(style, rule["block_id"])
            for src in rule_sources(d, rule):
                blob = blob_at(root, commit, src)
                if blob is None:
                    continue
                st = blob.decode("utf-8", "replace")
                i, j = find_block(st, om, cm)
                block = "\n".join(st.split("\n")[i:j + 1])
                for dest_t in (rule.get("to") if isinstance(rule.get("to"), list)
                               else [rule.get("to")]):
                    dest, miss = resolve_tokens(dest_t, ctx)
                    if miss:
                        r.fail(f"entry '{eid}' merged destination needs answer '{miss[0]}'")
                        continue
                    dp = target / dest
                    cur = dp.read_text(encoding="utf-8", errors="replace") if dp.is_file() else None
                    try:
                        new, mode = write_block(cur, om, cm, block, rule.get("insert", "append"))
                    except Refusal as e:
                        r.fail(f"entry '{eid}' -> {dest}: {e}")
                        continue
                    dp.parent.mkdir(parents=True, exist_ok=True)
                    dp.write_text(new, encoding="utf-8", newline="\n")
                    staged.append(dest)
                    rows.append({"path": dest, "role": "merged", "kit": eid, "version": vers,
                                 "block_id": rule["block_id"], "marker_style": style,
                                 # The BLOCK's hash, never the file's, and normalized so a
                                 # re-checkout on another platform does not read as drift.
                                 "block_sha256": hashlib.sha256(
                                     block.replace(CR, "").encode("utf-8")).hexdigest(),
                                 "normalized": "lf", "mode": mode, "source": src,
                                 "commit": commit, "written": True})
                    print(f"govkit apply — merged [{mode}] {dest} <- block '{rule['block_id']}'")

        for u in res["unlanded"]:
            if u["role"] == "merged":
                continue          # written above, or delegated at configure
            why = UNLANDED_REASON.get(u["role"])
            if why is None:
                r.fail(f"entry '{eid}' declares role '{u['role']}', which is not in the role enum — "
                       f"refusing rather than skipping a rule this engine cannot classify")
                continue
            # THE ROW, NOT A SECOND PRINT. Schema 2 needs a receipt row for every file gov is
            # responsible for, which is what this loop is for. The announcement is already made
            # once, by the SKIPPED line the write path emits with the same role, destination, kit
            # and reason — printing it again here was two answers to one question in the output of
            # the verb built to end silent partial installs.
            _row = {"path": u["dest"], "role": u["role"], "kit": eid,
                    "version": vers, "written": False, "source": u["src"], "why": why}
            # DEPL-dCarriedReceipt-10 S4/S5. A forked row COPIES its two keys from the RULE that
            # produced it — the rule `resolve_entry` returned — and never from any measurement of
            # bytes. `forked` is a claim about provenance the descriptor makes, so the receipt
            # records what was declared and `update` re-reads the declaration on every run rather
            # than trusting this copy. Copied with `.get` because arm 3c is the thing that demands
            # them, and `apply` must not become a second, quieter place the same demand is written.
            if u["role"] == "forked":
                _rules = d.get("files", [])
                _i = u.get("rule")
                _rule = _rules[_i] if isinstance(_i, int) and 0 <= _i < len(_rules) else {}
                for _k in FORK_RULE_KEYS:
                    if _rule.get(_k):
                        _row[_k] = _rule[_k]
            rows.append(_row)

        for dest, w in sorted(res["writes"].items()):
            if w["missing"]:
                r.fail(f"entry '{eid}' needs answer '{w['missing'][0]}' to resolve destination "
                       f"'{w['dest']}' — refusing before the write, naming the key")
                continue
            if w.get("scope") == "machine":
                continue
            rule = d.get("files", [])[w["rule"]]
            if rule.get("scope") == "machine" or rule.get("link"):
                continue
            data = blob_at(root, commit, w["src"]) if w["src"] else None
            if data is None:
                r.fail(f"entry '{eid}': {w['src']} does not resolve at {commit[:8]}")
                continue
            dp = target / dest
            # BOTH IDENTITIES, on this channel only (S1, S7). `gov_oid` is the blob gov shipped at
            # `commit` and means that forever; `oid` is the blob the TARGET's index holds and is
            # filled after the stage below, because it does not exist until this run stages it. The
            # other three producers — the `merged` row, the `attributes` row and the `unlanded`
            # rows — take NEITHER, and each for its own stated reason: there is no whole-file gov
            # blob at those destinations to name.
            row = {"path": dest, "role": w["role"], "kit": eid, "version": vers,
                   "sha256": hashlib.sha256(data).hexdigest(), "gov_oid": blob_oid(data),
                   "source": w["src"], "commit": commit}
            if w["role"] == "seed" and dp.exists():
                # seed: copied ONCE, then the target owns it. The ROW is recorded either way —
                # serializing the receipt from the write log alone is what made it shrink from one
                # apply to the next, taking every later evidence loop with it.
                row["written"] = False
                rows.append(row)
                continue
            dp.parent.mkdir(parents=True, exist_ok=True)
            dp.write_bytes(data)
            row["written"] = True
            rows.append(row)
            staged.append(dest)
    print(f"govkit apply — landed {len(staged)} file(s), {len(rows)} row(s) in the receipt")

    # ---- STAGE. Not housekeeping: every gate in this suite reads the INDEX, so an unstaged install
    # ---- is invisible to the verification that follows it.
    if staged:
        subprocess.run(["git", "-C", str(target), "add", "--"] + staged,
                       capture_output=True, check=False)
    # S7's second half: `oid` is read from each row's INDEX ENTRY, once the stage above has made one.
    # ONE batched read over the writes channel's paths, per row and not per stage — that one `git
    # add` covers every channel, and a seed the target already owned was never staged by this run at
    # all. A row whose path the target does not track gets no `oid`, which is a true statement about
    # a target that holds no index entry for it.
    _landed = [w["path"] for w in rows if w.get("role") in LANDABLE_ROLES]
    _idx, _ = index_read(target, _landed) if _landed else ({}, set())
    for w in rows:
        if w.get("role") in LANDABLE_ROLES and w["path"] in _idx:
            w["oid"] = _idx[w["path"]][1]
    step(STEP_STAGE, f"{len(staged)} path(s)")

    # ---- HOOK PROBE. After the stage, because the question is whether the OPERATOR's landing commit
    # ---- is refused, and a staged-scope hook leg sees nothing until the install is staged.
    hook_state, hook_out = hook_probe(target)
    step(STEP_HOOKPROBE, hook_state)
    if hook_state == "block":
        (target / ".governance" / "outbox").mkdir(parents=True, exist_ok=True)
        (target / ".governance" / "outbox" / "hook-block.md").write_text(
            "# the target's pre-commit hook would refuse the landing commit\n\n"
            "`apply` never commits, so no hook fired during the install itself. This is a warning "
            "about the commit YOU are about to make, captured so you meet it here rather than by "
            "hand.\n\n```\n" + hook_out + "\n```\n", encoding="utf-8", newline="\n")
        if (deploy.get("policy") or {}).get("on_hook_block") == "refuse":
            r.fail("on_hook_block = refuse and the target's pre-commit hook refuses; the install is "
                   "on disk and staged, and nothing was rolled back")

    # ---- CONFIGURE. A kit with a blocks_adopt hole lands and is NOT configured.
    outbox = target / ".governance" / "outbox"
    outbox.mkdir(parents=True, exist_ok=True)
    orders: list[dict] = []
    configure_skipped: set[str] = set()
    stopped_ok: set[str] = set()   # kits whose adopter stopped at a DECLARED, accepted outcome
    for eid in selection:
        d, _p = descs[eid]
        ctx = target_context(target, deploy, eid, d)
        blocked = [h for h in d.get("hole", []) if h.get("blocks_adopt")]
        for h in d.get("hole", []):
            (outbox / f"{h.get('id')}.md").write_text(
                f"# {h.get('id')} — {eid}\n\n{h.get('why', '').strip()}\n\n"
                f"Discharge is decided by RUNNING this hole's probe, never by deleting this file.\n",
                encoding="utf-8", newline="\n")
            orders.append({"kind": "hole", "id": h.get("id"),
                           "path": f".governance/outbox/{h.get('id')}.md"})

        # A machine-scoped RULE gets an ORDER, never a write. The population is the RULE and not the
        # entry: every descriptor declares an entry-level scope of `repo` and exactly one rule in the
        # tree is machine-scoped, so an entry-keyed state would have no instance while apply writes
        # per rule — the two sides would quantify over different populations and the state would be
        # permanently unreachable. The order's own name is `<entry>-<slug>.md`, because a rule has no
        # hole id and the outbox's other names are hole ids.
        for rule in d.get("files", []):
            if not (rule.get("scope") == "machine" or rule.get("link")):
                continue
            for dest in rule_destinations(d, rule):
                resolved, miss = resolve_tokens(dest, ctx)
                if miss:
                    continue
                slug = re.sub(r"[^A-Za-z0-9]+", "-", resolved).strip("-").lower()[:60]
                name = f"{eid}-{slug}.md"
                link = (f"mklink /J \"{resolved}\" \"<gov>/{'/'.join(rule_sources(d, rule)[:1])}\""
                        if os.name == "nt" else
                        f"ln -s \"<gov>/{'/'.join(rule_sources(d, rule)[:1])}\" \"{resolved}\"")
                other = (f"ln -s \"<gov>/…\" \"{resolved}\"" if os.name == "nt"
                         else f"mklink /J \"{resolved}\" \"<gov>/…\"")
                (outbox / name).write_text(
                    f"# {eid} — a MACHINE-scoped destination\n\n"
                    f"destination: {resolved}\n\n"
                    f"This lives OUTSIDE the repository, so `apply` writes nothing for it and "
                    f"`check` reports it undischargeable rather than missing — a check running "
                    f"inside the repo cannot answer a question about a path outside it.\n\n"
                    f"On this host:\n    {link}\n\nOn the other platform:\n    {other}\n",
                    encoding="utf-8", newline="\n")
                orders.append({"kind": "machine", "id": name[:-3], "path":
                               f".governance/outbox/{name}", "destination": resolved, "kit": eid})
        if blocked and not resume:
            print(f"govkit apply — CONFIGURE {eid}: skipped, blocked by hole "
                  f"'{blocked[0].get('id')}' — landed but inert")
            configure_skipped.add(eid)
            continue
        argv = d.get("adopt", {}).get("argv") or []
        if not argv:
            continue
        resolved = [resolve_tokens(a, ctx)[0] for a in argv]
        rc = subprocess.run(resolve_shell_argv(resolved), cwd=str(target), capture_output=True, text=True).returncode
        outcome = classify_outcome(target, d, ctx, rc)
        means = outcome.get("means") if outcome else None
        accepted = bool(outcome and outcome.get("ok"))
        if accepted:
            stopped_ok.add(eid)
        print(f"govkit apply — CONFIGURE {eid}: adopter exit {rc}"
              + (f" — {means}" if means else "")
              + (" [accepted stop]" if accepted and rc != 0 else ""))
        if rc != 0 and accepted:
            # A DECLARED, ACCEPTED terminal state. `memory-tree` seeds `.memory-tree.conf` and stops
            # by design so a person edits it before anything renders; that is a correct first
            # install, and calling it a failure made `apply` exit non-zero on every one of them.
            # The arm asserting a default-selection apply returns 0 was therefore unsatisfiable, and
            # it landed red rather than being read as the contradiction it was.
            pass
        elif rc != 0 and means:
            # The `[[outcome]]` blocks were declared by six descriptors and read by ZERO code, so an
            # exit code shared by six unrelated branches was reported as an integer. A declared
            # meaning lets a fixture assert a MEANING, which is what the acceptance layer needs.
            r.fail(f"kit '{eid}': its adopter exited {rc} — {means}")
        elif rc != 0:
            # A non-zero adopter exit is a FINDING, not a printed integer. Measured before this:
            # `apply --resume` printed 'adopter exit 1' and exited 0, so an install whose configure
            # phase failed was indistinguishable from one that worked. WHICH failure it is needs the
            # `[[outcome]]` evaluator, which is a later unit's; until then it is unclassified and
            # says so rather than being interpreted.
            r.fail(f"kit '{eid}': its adopter exited {rc} — unclassified, because no `[[outcome]]` "
                   f"evaluator exists yet to say WHICH declared outcome that code means")

    # ---- OBSERVE. apply does NOT render — the adopters do, and a second renderer would race the
    # ---- real one. What it does is look at what they produced, so `update` and `check` have
    # ---- something to reason about. A rendered destination that is ABSENT after configure is a
    # ---- FINDING: before this, every non-landable role vanished with no message at all.
    step(STEP_OBSERVE, "rendered destinations")
    n_rendered = 0
    for row in rows:
        if row.get("role") != "rendered":
            continue
        n_rendered += 1
        dp = target / row["path"]
        if not dp.is_file():
            if row.get("kit") in stopped_ok:
                # Its adopter stopped at a DECLARED, accepted outcome, so it never reached the render.
                # Reporting the absence here would be reporting the accepted stop a second time,
                # under a name that reads like a defect.
                print(f"govkit apply — OBSERVE {row['path']}: not rendered — "
                      f"'{row['kit']}' stopped at an accepted outcome")
                continue
            r.fail(f"'{row['path']}' is declared `rendered` by kit '{row['kit']}' and is absent "
                   f"after its adopter ran — the adopter owns those bytes and did not write them")
            continue
        row["output_sha256"] = hashlib.sha256(dp.read_bytes()).hexdigest()
        row["template"] = row.get("source")
        conf = (descs[row["kit"]][0].get("config") or {}).get("file")
        if conf and (target / conf).is_file():
            row["inputs"] = [{"path": conf,
                              "sha256": hashlib.sha256((target / conf).read_bytes()).hexdigest()}]
    print(f"govkit apply — observed {n_rendered} rendered destination(s)")

    # ---- RENORMALIZE, after CONFIGURE and not beside the block. This DEPARTS from the contract's
    # ---- stated order, deliberately and for a measured reason: before the adopters have run, the
    # ---- pinned population is empty.
    if pins:
        want = eol_population(target)
        lf_paths = sorted(p for p, v in want.items() if v == "lf")
        if lf_paths:
            # GOV'S OWN WRITES ARE NOT "SOMEBODY'S WORK-IN-PROGRESS". `git diff HEAD` covers the
            # index, and STAGE has already `git add`-ed everything this run landed — so on a normal
            # first install every pinned path gov just wrote came back dirty and the renormalize
            # refused itself. `staged` is the paths this run actually wrote; what remains after
            # subtracting them is a change gov did not make, which is the only thing this guard is
            # for. Measured: without this, a clean fixture target failed here on the DEFAULT
            # selection, naming two files gov had itself just landed.
            ours = set(staged)
            dirty = [p for p in subprocess.run(
                ["git", "-C", str(target), "diff", "--name-only", "HEAD", "--"] + lf_paths,
                capture_output=True, text=True).stdout.split() if p not in ours]
            missing_wt = [p for p in lf_paths if not (target / p).exists()]
            if dirty or missing_wt:
                r.fail(f"the pinned population is not clean relative to HEAD "
                       f"({', '.join(sorted(set(dirty + missing_wt))[:4])}) — refusing the "
                       f"renormalize rather than folding somebody's work-in-progress into an index "
                       f"gov does not own")
            else:
                subprocess.run(["git", "-C", str(target), "add", "--renormalize", "--"] + lf_paths,
                               capture_output=True, check=False)
        after = eol_population(target)
        idx = subprocess.run(["git", "-C", str(target), "ls-files", "--eol", "--"] + lf_paths,
                             capture_output=True, text=True).stdout if lf_paths else ""
        bad = [ln.split("\t")[-1] for ln in idx.splitlines() if ln and "i/lf" not in ln.split()[0]]
        for b in bad:
            r.fail(f"'{b}' is pinned eol=lf and its INDEX blob is not LF after the renormalize")
        covers_nothing = [p for p, _c, _w in pins
                          if not any(fnmatchcase_path(f, p) for f in after)]
        for p in covers_nothing:
            claim = next(c for pp, c, _w in pins if pp == p)
            r.note(f"pin '{p}' (declared by {claim}) resolves to no tracked path in this target")
        step(STEP_RENORMALIZE, f"{len(lf_paths)} path(s) governed, {len(bad)} not LF in the index")
        for row in rows:
            if row.get("role") == "attributes":
                row["renormalized"] = lf_paths

    # ---- LEGS. The last CONTENT step of the hard order. Guards are RENDERED against the target's
    # ---- own prefix and memory root, and a guard is DROPPED on tracked-ness rather than existence:
    # ---- the runner's predicate is a diff over a pathspec, and a pathspec matching nothing diffs
    # ---- clean, so a guard naming an existing-but-UNTRACKED path skips its leg forever at exit 0.
    emitted: list[dict] = []
    step(STEP_LEGS, gr.get("kind", "absent"))
    if gr.get("kind") == "manifest":
        rf = target / gr["file"]
        try:
            existing = json.loads(rf.read_text(encoding="utf-8")) if rf.is_file() else []
        except json.JSONDecodeError:
            raise Refusal(f"the declared runner file {gr['file']} is not valid JSON")
        if not isinstance(existing, list):
            raise Refusal(f"the declared runner file {gr['file']} is not a JSON list")
        owned = {e["name"] for e in ((receipt or {}).get("gate_runner") or {}).get("emitted", [])}
        by_name = {e.get("name"): i for i, e in enumerate(existing)}
        tracked_target = set(subprocess.run(["git", "-C", str(target), "ls-files"],
                                            capture_output=True, text=True).stdout.split("\n"))
        for eid in selection:
            d, _p = descs[eid]
            ctx = target_context(target, deploy, eid, d)
            for leg in d.get("gate_leg", []):
                nm = leg.get("name")
                argv, miss = [], []
                for a in leg.get("argv", []):
                    s, m = resolve_tokens(a, ctx)
                    argv.append(s)
                    miss += m
                if miss:
                    r.fail(f"leg '{nm}' argv still carries {miss[0]} after rendering — a leg wired "
                           f"to an unresolved token is broken forever; a dropped GUARD only costs "
                           f"an unnecessary run, which is why the two are not symmetric")
                    continue
                guards, dropped = [], []
                for g in leg.get("guard", []) or []:
                    s, m = resolve_tokens(g, ctx)
                    if m:
                        dropped.append((g, f"unresolved token '{m[0]}'"))
                    elif not any(t == s.rstrip("/") or t.startswith(s.rstrip("/") + "/")
                                 for t in tracked_target if t):
                        dropped.append((s, "matches no tracked path in the target"))
                    else:
                        guards.append(s)
                if nm in by_name and nm not in owned:
                    raise Refusal(f"the target's runner already has a leg named '{nm}' and this "
                                  f"target's receipt does not claim it — overwriting a leg the "
                                  f"target wrote silently deletes their own coverage")
                # SUBJECT TRAVELS. Without this the field never reaches an adopter and the whole
                # mechanism stops at this repo's edge — a target would receive every kit self-test as
                # an ordinary bar leg, which is the defect the unit exists to remove.
                # Defaulted to `repo`, because an undeclared leg belongs ON the bar: the other
                # default silently removes a leg the descriptor never spoke about.
                # SUBJECT IS EMITTED ONLY WHERE THE TARGET CAN READ IT. `tools/gate-legs.json`
                # has a PINNED key set, asserted by the `run-gates canary` leg that the run-gates
                # kit ships and that runs on every adopter's bar — and that pin did not carry
                # `subject` before this build. Writing the key into a tree whose run-gates predates
                # it reds their canary as a side effect of a routine `apply --kits memory-tree`,
                # which is the deployer breaking a target's gate while installing something else.
                # The floor is read from the TARGET's installed runner, not assumed.
                row = {"name": nm, "argv": argv}
                if check_target_reads_subject(target, deploy):
                    row["subject"] = leg.get("subject") or "repo"
                if guards:
                    row["guard"] = guards      # OMITTED, never `[]`, when everything dropped
                if nm in by_name:
                    prev = next((e for e in owned and
                                 ((receipt or {}).get("gate_runner") or {}).get("emitted", [])
                                 if e["name"] == nm), None)
                    if prev and (prev.get("argv") != argv or prev.get("guard", []) != guards):
                        r.fail(f"leg '{nm}' in the target differs from what the receipt recorded — "
                               f"reporting drift rather than replacing it; ownership of the NAME is "
                               f"not ownership of the ROW")
                        continue
                    existing[by_name[nm]] = row
                else:
                    existing.append(row)
                # THE RECEIPT CARRIES SUBJECT TOO, and not only so the summary below can count it.
                # The receipt is what a later apply reads to decide what this deployer owns; a
                # field that reaches the target's manifest but not the receipt is a field no drift
                # check can ever see move. The first draft omitted it and the summary silently
                # counted zero — an `if n_kit:` that is never true prints nothing and reads exactly
                # like a kit with no self-tests. TOOL-dUnstalledConvoy-26.
                emitted.append({"name": nm, "kit": eid, "argv": argv, "guard": guards,
                                "subject": row["subject"],
                                "guard_dropped": [{"spec": a, "why": b} for a, b in dropped],
                                "history_depth": leg.get("history_depth")})
                if dropped and not guards:
                    print(f"govkit apply — gate leg '{nm}': UNGUARDED "
                          f"({len(dropped)} guard(s) dropped: {dropped[0][1]})")
        if not r.problems:
            rf.parent.mkdir(parents=True, exist_ok=True)
            rf.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8", newline="\n")
            subprocess.run(["git", "-C", str(target), "add", "--", gr["file"]],
                           capture_output=True, check=False)
            print(f"govkit apply — gate legs: emitted {len(emitted)} into {gr['file']}")
            # THE KIT-SUBJECT LEGS ARE HELD, and an adopter has to be told twice: once here, where
            # they can run them for the first time against the kit they just installed, and once as
            # the standing way to ask. Without this line the legs are simply absent from their bar
            # and nothing says they exist. TOOL-dUnstalledConvoy-26.
            n_kit = sum(1 for e in emitted if (e.get("subject") or "repo") == "kit")
            if n_kit:
                print(f"govkit apply — {n_kit} of those are kit SELF-TESTS and are HELD by default: "
                      f"they test the kit's own source, which does not change in a repo that "
                      f"copy-installs it. Run them once now to verify this install, and afterwards "
                      f"whenever you edit a kit:")
                # THE TARGET'S OWN RUNNER COMMAND, not this repo's path. An adopter told to run a
                # script that does not exist in their tree has been told nothing, and `command` is
                # the declaration govkit already validated and already echoed at BASELINE.
                _cmd = " ".join(gr.get("command") or []) or "your gate runner"
                print(f"govkit apply —   GATE_SELFTESTS=1 {_cmd}")
                print(f"govkit apply — GATE_FULL=1 does NOT run them: it ignores every guard, and a "
                      f"kit's own tests are not a guard. A green bar without that variable says "
                      f"nothing about the kits themselves.")
    else:
        (target / ".governance" / "outbox").mkdir(parents=True, exist_ok=True)
        lines = ["# gate legs — ORDERED, not emitted", ""]
        for eid in selection:
            d, _p = descs[eid]
            ctx = target_context(target, deploy, eid, d)
            for leg in d.get("gate_leg", []):
                lines.append(f"- {leg.get('name')}: "
                             f"{' '.join(resolve_tokens(a, ctx)[0] for a in leg.get('argv', []))}")
        lines += ["", "Nothing in this target runs these yet."]
        (target / ".governance" / "outbox" / "gate-legs.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        orders.append({"kind": "gate-legs", "id": "gate-legs",
                       "path": ".governance/outbox/gate-legs.md"})
        print("govkit apply — gate legs: ORDERED, not emitted — "
              + ("[gate_runner] declares kind = \"none\"" if gr.get("kind") == "none"
                 else "this target's deploy.toml declares no [gate_runner]")
              + " (see .governance/outbox/gate-legs.md)")

    # ---- AFTER. The same function, the same regime, so the two maps are comparable.
    after_map: dict[str, str] = {}
    if gr.get("kind") == "manifest":
        step(STEP_AFTER, "re-reading the target's runner")
        after_map = read_gate_verdicts(target, gr)
        for nm in sorted(set(before_map) | set(after_map)):
            b, a2 = before_map.get(nm), after_map.get(nm)
            if b == "green" and a2 == "red":
                r.fail(f"leg '{nm}' was green before this install and is red after")
            elif b == "green" and a2 == "held":
                # NOT A FAILURE, and this is the whole point of the state. A leg whose subject this
                # install set to `kit` is HELD afterwards BY DESIGN — that is what an adopter is
                # buying. Silent would be wrong too: the leg stops running and nothing else says so.
                print(f"govkit apply — leg '{nm}' ran before this install and is HELD after: it is "
                      f"a kit self-test now, and runs under GATE_SELFTESTS=1")
            elif b == "green" and a2 == "reused":
                print(f"govkit apply — leg '{nm}' was REUSED after this install rather than "
                      f"re-executed; its verdict is carried, not earned")
            elif b == "green" and a2 == "skipped":
                r.fail(f"leg '{nm}' was green before and did not execute after — the install broke "
                       f"its guard")
            elif b == "green" and a2 is None:
                r.fail(f"leg '{nm}' was green before this install and is gone after — a leg that "
                       f"vanished is not a leg that passed")
            elif b is None and a2 == "red" and not exempt_leg(descs, selection, target, nm,
                                                              configure_skipped):
                r.fail(f"leg '{nm}' did not exist before this install and is red after")

    # ---- RECEIPT. Tool-written only, plus the flat sidecar a target verifies with bash alone.
    (target / ".governance").mkdir(exist_ok=True)
    receipt_path.write_text(json.dumps(
        {"schema": RECEIPT_SCHEMA, "gov_source": str(root), "gov_commit": commit,
         "prefix": (deploy.get("prefix") or "tools"), "kits": selection, "files": rows,
         "orders": orders, "baseline": baseline, "after": after_map,
         "hook_block": {"state": hook_state},
         "gate_runner": {"kind": gr.get("kind", "absent"), "file": gr.get("file"),
                         "emitted": emitted}},
        indent=2) + "\n", encoding="utf-8", newline="\n")
    (target / ".governance" / "install.sums").write_text(
        "".join(f"{w['sha256']}  {w['path']}\n" for w in rows if "sha256" in w),
        encoding="utf-8", newline="\n")
    step(STEP_RECEIPT, f"{len(rows)} row(s), {len(selection)} kit(s), schema {RECEIPT_SCHEMA}")
    return r.emit()


# ---------------------------------------------------------------------------------------- update
# The verdict GRID, as data so `selfcheck` can assert it is complete. Keyed
# (ours-vs-receipt, theirs-vs-base); `absent` on the THEIRS axis is evaluated as its own value across
# every OURS state, which is the correction the spec audit bought: as a value on the `equal` row only,
# an edited-and-withdrawn file routed to `diverged` and a file deleted on both sides routed to
# `missing` — a restore of a blob that does not exist.
OURS_STATES = ("equal", "differs", "absent")
THEIRS_STATES = ("equal", "differs", "absent")
VERDICT_GRID = {
    ("equal", "equal"): "current",
    ("equal", "differs"): "stale",
    ("equal", "absent"): "withdrawn",
    ("differs", "equal"): "patched",
    ("differs", "differs"): "diverged",
    ("differs", "absent"): "patched",
    ("absent", "equal"): "missing",
    ("absent", "differs"): "missing",
    ("absent", "absent"): "converged",
}

# DEPL-dCarriedReceipt-8 S4. The verdicts whose write arm takes GOV'S RAW BYTES, over whatever the
# target holds. Named HERE rather than spelled at the `if` in `_cmd_update`, because `selfcheck`
# asserts that no grid cell on the `differs` OURS row reaches one of these — and an assertion that
# retypes the set it grades stops grading it on the edit that widens the arm. One spelling, two
# readers. A row whose OURS axis says `differs` carries something the target changed, so a raw write
# over it destroys that change; the guarantee is STRUCTURAL — the cells simply do not map there —
# rather than a guard in front of the write, because a guard reading the field the bug corrupts is
# disabled by the bug it exists to catch.
RAW_WRITE_VERDICTS = ("stale", "missing")

# DEPL-dCarriedReceipt-14 S2 + S4. THE TOUCHED SET, decided from the CLASSIFICATION and therefore
# known before the first byte moves — which is the only place it can be decided, because the
# pre-write snapshot depends on the same fact. Every verdict the write loop acts on under
# `how == "table"` is here: the two raw-write words, `-11`'s `renamed`, and `diverged`, whose arm
# is the three-way that motivates this whole unit. `withdrawn` joins it only under
# `--write-withdrawals`, because without that flag its arm deletes nothing and writes only an order.
#
# WHAT THIS IS NOT, stated because a structural predicate reads as a semantic one to everybody who
# did not write it: it is what the loop will act on, not what the loop DID. A row that reaches its
# arm and is refused there — a conflicting three-way, an occupied rename destination — leaves its
# kit in this set, so that kit is checked twice and snapshotted for a byte that never moved. The
# restore is keyed on the snapshot, so rolling one of those back re-writes the entry it already
# has; the cost is a wasted check and the alternative is a post-hoc population the snapshot could
# not have been taken from.
TOUCHING_VERDICTS = tuple(RAW_WRITE_VERDICTS) + ("diverged", "renamed")

# DEPL-dCarriedReceipt-14 S3. The six fields `-11` S4 rewrites AS A SET, snapshotted together and
# restored together. `path` and `source` are in it because a rolled-back rename that kept its
# post-rename spelling beside pre-rename identities is exactly the split `-7` S9 refuses the whole
# next run on; `sha256` and `oid` because a row stamped forward over reverted bytes re-creates `-8`.
ROLLBACK_FIELDS = ("path", "source", "sha256", "commit", "gov_oid", "oid")


def raw_write_cells(grid: dict) -> list[tuple[str, str, str]]:
    """Every cell of a verdict grid that would hand a DELTA row to the raw-write arm.

    A function rather than a loop inside `selfcheck` so the harness can drive it over a hand-edited
    COPY of the grid and watch it SPEAK. A structural assertion nobody has ever seen fire is an
    assertion about nothing, and re-implementing the rule in the test to make it fire would leave
    two spellings of it — the class this whole file is about.
    """
    return sorted((o, t, v) for (o, t), v in grid.items()
                  if o == "differs" and v in RAW_WRITE_VERDICTS)


# What `update` does per ROLE. A role whose row is a refusal is still a ROW: silence is what lets a
# later unit add a role and leave it behind, and `selfcheck` asserts this covers the role enum.
UPDATE_ROLE = {
    "engine": "table",          # the full verdict table
    "seed": "report-reseed",    # never written; a moved template is reported
    "project-owned": "skip",    # gov supplied no bytes, so there is no base to compare
    "generated": "skip",
    "rendered": "adopter",      # re-run the adopter, compare, CAP at report
    "merged": "block",          # compare the BLOCK hash; never a three-way
    "attributes": "pins",       # DEPL-dCarriedReceipt-2: recompute, compare, report; never write
    "gate-leg": "report",       # DEPL-dCarriedReceipt-2: one row each, tallied, no r.fail
    "ci": "report",             # DEPL-dCarriedReceipt-2: ditto -- `-6` owns emitting them
    # DEPL-dCarriedReceipt-10 S4, the `report` disposition's SECOND consumer. A forked row prints
    # one counted line and is written in NEITHER direction: gov's copy is a derivative of the
    # target's, so sending gov's bytes over the target's is the destruction this role exists to
    # stop, and `direction` is a LABEL on that report rather than an instruction to anything.
    # NOT `refuse`, which `-2` exists to remove: one forked row would make every future `update` on
    # that target exit non-zero and never re-stamp its receipt.
    "forked": "report",
}


def _sha(b: bytes | None) -> str | None:
    return hashlib.sha256(b).hexdigest() if b is not None else None


# ------------------------------------------------------------ the carry rungs (DEPL-dCarriedReceipt-9)
# A row whose two identities differ is NOT automatically a local delta. The difference may be a
# CARRY — a transformation gov already knows about — and there are exactly three rungs: `verbatim`
# (there is nothing to explain), `eol` (the target's checkout committed CRLF where gov ships LF), and
# `relocate` (the adopter installed at a different `prefix`, so every file that SPELLS a path differs
# on every line that spells one). The motivating measurement is NOT this tree's and cannot be
# reproduced from it, so it is attributed rather than asserted: DEPL-dCarriedReceipt-9 §4 records
# that on inCMS at 2cff5855, of the 52 rows whose recorded gov commit resolves, 21 are byte-identical,
# 6 differ only in line endings and 5 differ only by the prefix relocation. Eleven rows carrying no
# local edit at all, and the two-identity predicate on its own calls every one of them a local delta —
# so the raw-write arm is closed to all of them forever and each is handed to a three-way whose
# `base` still spells gov's prefix where the target's own copy does not.
#
# THE RUNG IS RECOMPUTED BY PROOF ON EVERY RUN AND IS NEVER READ BACK OFF THE RECEIPT (S2). A stored
# rung is a claim about bytes that have moved since; the whole point of the two identities is that no
# stored boolean stands between this tool and the blobs. `carry` is written into the row for
# REPORTING, and the print loop is its only reader — asserted by an arm over this file's source
# rather than left to discipline.
#
# WHAT A PROVEN RUNG DOES NOT BUY, stated here because a structural guarantee reads as a semantic one
# to everybody who did not write it: it does NOT move `o_state`, does NOT touch `VERDICT_GRID`, and
# CANNOT put a row on the raw-write arm. What it buys is the MERGE path — applied to `base` and to
# `theirs` it cancels in the base-to-theirs diff, `git merge-file` sees only gov's semantic change,
# and the row reconciles to the CARRIED bytes with no operator turn.
CARRY_RUNGS = ("verbatim", "eol", "relocate")


def derive_lf(data: bytes) -> bytes:
    """CRLF to LF — the `eol` rung's whole transformation, spelled once because two spellings of one
    rule is the class this file spends most of its comments on."""
    return data.replace(b"\r\n", b"\n")


def derive_carry_map(pairs) -> tuple[dict[str, str], dict[str, str], list[tuple[str, list[str]]]]:
    """The needle map, DERIVED from a sequence of `(gov source, target destination)` pairs.

    A SEQUENCE OF PAIRS rather than a receipt, because the derivation has two callers and only one
    of them has a receipt to read. `cmd_update` feeds it the receipt's rows — the record of where
    the target actually TOOK each file, which is what `update`'s whole job is to move. `adopt`
    (DEPL-dCarriedReceipt-13 S4a) feeds it the planned `(src, dest)` pairs of its own run, because at
    bootstrap there is no receipt yet.

    THERE IS NO AUTHORED FORM AND NO OVERRIDE KEY. A hand-written map is a second answer to a
    question the caller's own pairs already answer.

    NOT re-resolved from the descriptors, and that is the reuse RESULT rather than an oversight.
    `resolve_dests` and `rule_relpath` already know how a source maps to a destination and calling
    them here would look like reuse — but they answer for the descriptor as it reads TODAY, while
    this map must answer for what the target actually installed, possibly at a different gov commit
    and a different `prefix`. Reusing them would make the map drift the moment a descriptor's `to`
    changes, which is the two-spellings-of-one-fact class `-1` exists to close, re-created one layer
    down.

    THE LIFT IS ONE DIRNAME PAIR PER ROW. Stripping EQUAL TRAILING SEGMENTS was measured and is
    wrong: it collapses `tools/unattended` into the bare gov directory `tools`, which then collides
    with the hooks kit's `tools` and is dropped as ambiguous — taking the whole unattended kit's
    relocation with it. The comparison is the spec's, over a population this tree does not hold, and
    is cited rather than restated: DEPL-dCarriedReceipt-9 §4 measured both lifts against each other
    and the dirname one yields strictly more surviving pairs. What THIS file's arms grade is the lift
    itself, over a fixture they build.

    A gov directory that yields two DIFFERENT target directories names no single destination and
    cannot be a needle, so it is DROPPED and returned BY NAME (§8 F1 — drop loudly). Refusing would
    make a perfectly installable target unupdatable over a map entry it never asked for, and a silent
    drop is indistinguishable from a target that relocated nothing.

    Needles emit in BOTH the `/` form and the `~` form, because gov flattens paths into fixture
    filenames: `tools/unattended/check-playbook.test.sh` spells `tools~` while an adopter's own
    fixture records are named `scripts~unattended~…`. The two forms COINCIDE for a directory with no
    slash and the map then holds one of them, so the needle count is not two per pair and is not
    written down anywhere — the caller prints what this returns.

    WHAT THIS DOES NOT COVER: a gov directory whose own NAME contains a literal `~` can flatten onto
    another directory's `~` form. The map is built in sorted order so the later one wins
    deterministically. No arm exercises it, because nothing in this tree names a directory that way
    and an arm nobody has ever seen fail is an assertion about nothing.

    Returns `(needles, pairs, dropped)` — the substitution map, the surviving directory pairs, and
    `(gov directory, [destinations])` for every one dropped.
    """
    lifted: dict[str, set[str]] = {}
    for src, dest in pairs:
        if not src or not dest:
            continue                       # a row with no `source` contributes no pair, and is not
        gd = str(src).rsplit("/", 1)[0] if "/" in str(src) else ""   # a reason to refuse the run
        td = str(dest).rsplit("/", 1)[0] if "/" in str(dest) else ""
        if not gd or not td:
            continue                       # a root-level file lifts to the EMPTY needle, which would
        lifted.setdefault(gd, set()).add(td)                    # match at every position in a file
    dropped = [(gd, sorted(ds)) for gd, ds in sorted(lifted.items()) if len(ds) > 1]
    pairs_out: dict[str, str] = {gd: next(iter(ds)) for gd, ds in sorted(lifted.items())
                                 if len(ds) == 1}
    needles: dict[str, str] = {}
    for gd, td in pairs_out.items():
        needles[gd] = td
        needles[gd.replace("/", "~")] = td.replace("/", "~")
    return needles, pairs_out, dropped


def derive_carried(data: bytes, needles: dict[str, str]) -> bytes:
    """Gov's bytes rewritten through the needle map — ONE left-to-right pass, longest needle first.

    THE OUTPUT IS NEVER RESCANNED, and that is the property that keeps this a function of its input.
    Rescanning, or matching longest-anywhere rather than leftmost, lets one substitution feed
    another, so rewriting `tools` inside a path already rewritten to `scripts` becomes reachable.
    `re.sub` over an alternation sorted longest-first is exactly the required pass: the alternation
    is ORDERED, so the longest needle wins at each position, and `sub` takes the leftmost match and
    resumes AFTER the replacement it just wrote.

    A PROOF INSTRUMENT, NOT A WRITE-TIME TRANSFORM (§3). It is applied to gov's bytes to COMPARE
    them, never to produce bytes landed on the strength of the map alone. Measured on
    `tools/unattended/adopt-unattended.test.sh` at ce5dca99, landing the rewritten form corrupts six
    lines: four `bash tools/land.sh` occurrences at lines 34, 63, 83 and 91, which name no prefix at
    all, and lines 132-133, where the fixture builds a directory literally named
    `my tools/unattended` and the bare needle turns it into `my scripts`. Under the proof gate that
    row simply matches no rung, and none of those six lines is ever written. The ONE bounded
    exception is the `missing` restore (S11), where the target holds no bytes to prove anything
    against and the alternative is writing gov's prefix into a target that does not use it.

    A blob that is not valid UTF-8 comes back UNCHANGED rather than being mangled into a false rung.
    """
    if not needles:
        return data
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data
    pat = "|".join(re.escape(n) for n in sorted(needles, key=lambda n: (-len(n), n)))
    return re.sub(pat, lambda m: needles[m.group(0)], text).encode("utf-8")


def derive_carry_rung(base: bytes, needles: dict[str, str], read_ours,
                      known_equal: bool = False) -> str | None:
    """THE LADDER: `verbatim`, `eol`, `relocate`, tried in that order, and the first proof wins (S1).

    A LADDER AND NOT A LATTICE (§8 F2). The rungs do not compose, so `relocate` is proved on RAW
    bytes and never on eol-normalised ones. The spec's grounds, attributed: on the live target every
    `relocate` row proves on raw bytes and none needs the composition, so composing buys nothing today
    and adds a fourth rung's worth of surface. The cost is stated rather than hidden: an adopter whose
    checkout is CRLF and whose prefix is ALSO non-default falls to local delta on those rows and gets
    the three-way instead of a raw write.

    WHOLE-FILE EQUALITY DECIDES A RUNG (S5). One residual byte and the rung does not match, the row
    keeps exactly the verdict it would have had, and nothing is written. The residual risk runs the
    other way and is accepted by design: a row like `adopt-unattended.test.sh` will never take an
    automatic write, and that is the correct outcome rather than a gap.

    `read_ours` is a THUNK, and that is a perf shape rather than a style. `verbatim` is settled from
    the OIDs the caller already holds, so a byte-identical row never pays a blob read at all — and on
    a real adopter that is most of the receipt. `known_equal` says the caller has already proved that
    `ours` and `base` name the
    same git blob — in which case `base` IS `ours`, byte for byte. The fall-through still re-proves
    equality ON BYTES, so a target whose object format is not gov's (where no oid ever matches) still
    reaches `verbatim` rather than being mislabelled `eol` by the rung below it.
    """
    ours = base if known_equal else read_ours()
    if ours is None:
        return None
    if ours == base:
        return "verbatim"
    if derive_lf(ours) == derive_lf(base):
        return "eol"
    if ours == derive_carried(base, needles):
        return "relocate"
    return None


def derive_carried_by_rung(rung: str | None, data: bytes, needles: dict[str, str]) -> bytes:
    """The rung's own transformation, for S6: applied to BOTH `base` and `theirs` before the
    three-way, so it CANCELS in the base-to-theirs diff and `git merge-file` sees only gov's semantic
    change — which is how a carried row reconciles to the carried bytes with no operator turn.

    WHAT EACH RUNG ACTUALLY DOES HERE, because two of the three are no-ops and a reader is owed that
    rather than left to infer it. `relocate` is the load-bearing one. `eol` normalises GOV's own
    bytes, which is a no-op wherever gov ships LF — it is written for the rung rather than for the
    one rung that needs it, and an `eol` row's merge is therefore exactly what it would be with no
    rung at all. `verbatim` is identity by construction and never reaches a three-way in any case:
    `ours == base` means `o_state` is `equal`, which the grid routes to `current`, `stale` or
    `withdrawn` and never to `diverged`.
    """
    if rung == "relocate":
        return derive_carried(data, needles)
    if rung == "eol":
        return derive_lf(data)
    return data


# ------------------------------------------------ rename detection (DEPL-dCarriedReceipt-11 S1/S7)
# THE SIMILARITY THRESHOLD, DECLARED. git's own default is 50% and this is that number — named here
# rather than left implicit at the call site, because an undeclared default is a value nobody can
# review, and this one decides whether an adopter's file is MOVED or REPORTED WITHDRAWN. Below it
# there is no `R` pair, the verdict stays `withdrawn`, and nothing is invented (S7): a low-similarity
# pair landed anyway would be attribution by guess — the new file has no receipt row, so its
# `gov_oid` would be invented, which is the inversion DEPL-dCarriedReceipt-13 refuses.
RENAME_SIMILARITY_PERCENT = 50


def derive_rename_map(root: pathlib.Path, base_commit: str | None, to_commit: str) -> dict[str, str]:
    """Gov's own renames between two vintages, as `old source -> new source`. ONE diff per run.

    UNSCOPED, and that is the whole design rather than an omission. Pathspec-limiting the diff to the
    receipt's own sources hides the DESTINATION half of every rename pair: git needs both sides in
    the same diff to pair a deletion with an addition at all, so a scoped diff sees the delete and
    reports it as a delete. Measured on this unit's own fixture, where gov moves a claimed file to
    `docs/gone.txt` — outside the kit's `home` entirely, and invisible to any scope the receipt could
    supply.

    `-z` because a rename pair is three NUL-separated fields and the non-`-z` form QUOTES a path
    containing a space or a quote — a quoted spelling matches no receipt row, so the rename silently
    degrades to a withdrawal for exactly the paths hardest to notice.

    ONLY the `R` rows. A `C` (copy) row means gov still ships the old source, so the row's `theirs`
    resolves and there is nothing here to reconcile; taking one would move a file gov did not move.
    A receipt carrying no `gov_commit` gets an empty map rather than a diff against a guessed base.
    """
    if not base_commit:
        return {}
    out = git(root, "diff", f"--find-renames={RENAME_SIMILARITY_PERCENT}%", "--name-status", "-z",
              base_commit, to_commit)
    fields = out.split("\0")
    renames: dict[str, str] = {}
    i = 0
    while i < len(fields):
        st = fields[i]
        if not st:
            i += 1
            continue
        if st[0] in ("R", "C") and i + 2 < len(fields):
            if st[0] == "R":
                renames[fields[i + 1]] = fields[i + 2]
            i += 3
            continue
        i += 2
    return renames


def classify_row(root: pathlib.Path, target: pathlib.Path, row: dict, to_commit: str,
                 index: dict[str, tuple[str, str]],
                 needles: dict[str, str] | None = None,
                 rename=None) -> dict:
    """One receipt row's verdict, from three identities. TWO of them are git blob OIDs.

    OURS is the blob the TARGET's index holds, compared to the row's STORED `gov_oid` — the blob gov
    shipped at this row's `commit`. Not to `sha256`, and not to the target's WORKTREE: `sha256` is a
    hash of bytes at write time, the worktree is whatever that target's own filters produced from
    the blob, and asking either of them "did the operator change this file" answers a different
    question. On a `core.autocrlf=true` clone the worktree read called 23 of 24 untouched engine
    rows `patched`.

    Both fields are STORED and only the COMPARISON is live: `gov_oid` is read back off the receipt
    and never recomputed here — S9's preamble asserts it instead — while the target's oid is read
    fresh on every run. No boolean anywhere stores the answer.

    A row carrying no `gov_oid` cannot be called equal to anything, so a present index entry reads
    `differs`. That is the SAFE direction by construction: `differs` reaches only `patched` and
    `diverged`, and `diverged` additionally needs a THEIRS that moved, which needs the `source` and
    `commit` such a row does not have. No raw write sits on this state.

    `ours` BYTES are fetched only where they are actually consumed — the three-way merge, the order
    it writes on a conflict, and DEPL-dCarriedReceipt-9's rung ladder. That last one moves the cost:
    a row whose index blob is not gov's own now pays one `cat-file` to find out WHY, which the
    verdict alone could never answer. A byte-identical row still pays nothing, because `verbatim` is
    settled from the two oids.

    `carry` (DEPL-dCarriedReceipt-9 S1) is computed here and is OUTPUT: it explains the difference
    the verdict reports, and it changes neither `o_state` nor the verdict nor which arm the row takes
    (S9). It is recomputed by PROOF on every run and a stored one is never read.

    `renamed` (DEPL-dCarriedReceipt-11 S2) is the one verdict that does NOT come from the grid, and
    it is decided before the grid is consulted rather than after — a row gov MOVED must never take
    the `withdrawn` cell, whose write arm exists to remove files. `renamed_to` carries the new gov
    source and the destination the caller resolved for it, and `theirs_new` gov's blob there; all
    three are `None` on every other verdict.
    """
    src, base_commit = row.get("source"), row.get("commit")
    theirs = blob_at(root, to_commit, src) if src else None
    base = blob_at(root, base_commit, src) if (src and base_commit) else None
    entry = index.get(row["path"])
    ours_oid = entry[1] if entry else None
    gov_oid = row.get("gov_oid")

    t_state = "absent" if theirs is None else ("equal" if _sha(theirs) == _sha(base) else "differs")
    if ours_oid is None:
        o_state = "absent"
    elif gov_oid and ours_oid == gov_oid:
        o_state = "equal"
    else:
        o_state = "differs"

    # ---- DEPL-dCarriedReceipt-9 S1. The rung, over the SAME two blobs the verdict came from, and
    # ---- it is computed here so there is one classifier rather than a second one beside it. The
    # ---- fetch is memoised because two readers want the same bytes: the ladder, and the three-way
    # ---- on a `diverged` row. A row with no `base` — no `source`, no `commit`, or gov holding no
    # ---- blob there — can prove nothing, and gets no rung rather than a guessed one.
    fetched: list[bytes | None] = []

    def read_ours() -> bytes | None:
        if not fetched:
            fetched.append(index_blob(target, ours_oid))
        return fetched[0]

    carry = None
    if base is not None and ours_oid is not None:
        carry = derive_carry_rung(base, needles or {}, read_ours,
                                  known_equal=(ours_oid == blob_oid(base)))

    # ---- DEPL-dCarriedReceipt-11 S2. THE RENAME, DECIDED BEFORE THE GRID IS CONSULTED, so the
    # ---- `("equal","absent")` cell never sees a row gov MOVED and answers `withdrawn` for it — the
    # ---- cell whose write arm unlinked the adopter's file, `git rm`-ed it and dropped its row, at
    # ---- exit 0, with the replacement never landed.
    #
    # THREE CONDITIONS, and each is load-bearing rather than defensive. `t_state == "absent"` is what
    # a rename LOOKS like from a receipt row — gov holds no blob at the old source any more — and
    # asking it keeps a stale map from stealing a row whose source still resolves. `o_state !=
    # "absent"` is the target's half: it deleted its copy, so there is nothing to move, and both
    # `absent` cells already grid to a verdict this verb acts on (`missing`, `converged`) rather than
    # to a `git mv` of a file that is not there. And the CALLER's resolver has to name exactly one
    # destination for the new source — a rename OUT of the kit's claimed surface is a withdrawal from
    # the target's point of view, not a move, and inventing a destination for it is the class
    # DEPL-dCarriedReceipt-1 closed.
    #
    # `rename` is a THUNK for the reason `read_ours` is one: the destination costs a full
    # `resolve_entry` over the descriptor, and asking it per row for rows that did not move would pay
    # that on every run. It is also where the descriptor knowledge lives — this classifier has no
    # registry and no target descriptor, and giving it one would make it a second resolver.
    moved = rename(row) if (rename is not None and src
                            and t_state == "absent" and o_state != "absent") else None
    theirs_new = blob_at(root, to_commit, moved[0]) if moved else None
    if moved and theirs_new is None:
        moved = None          # git named the pair and gov's tree has no blob there: not actionable
    if moved and carry != "verbatim" and read_ours() is None:
        # The one input the move's byte decision cannot be taken without. `verbatim` is settled from
        # the two oids and needs no read; every other outcome is a three-way, and merging against a
        # `b""` this verb could not obtain would drop the operator's whole side. Degrading to the
        # grid leaves `withdrawn`, which after S8 is a report and an order — it deletes nothing.
        #
        # THIS IS ALSO WHAT MAKES THE WRITE ARM'S `ours` NON-NONE, and it is stated here because
        # the guarantee is STRUCTURAL rather than a guard in front of the merge: a row that says
        # `renamed` has either proved `verbatim` — which never reaches `three_way` — or read its
        # bytes back successfully on this line. The `diverged` arm below carries an explicit
        # `ours is None` refusal instead, because nothing degrades ITS verdict: the two are the
        # same question answered at the two different places it can be answered.
        moved = None
    verdict = "renamed" if moved else VERDICT_GRID[(o_state, t_state)]

    if ours_oid and verdict == "diverged":
        read_ours()
    ours = fetched[0] if fetched else None
    return {"verdict": verdict, "ours": ours, "ours_oid": ours_oid, "theirs": theirs,
            "base": base, "o_state": o_state, "t_state": t_state, "carry": carry,
            "renamed_to": moved, "theirs_new": theirs_new if moved else None}


def land_through_index(root: pathlib.Path, target: pathlib.Path, path: str, src: str | None,
                       data: bytes, to_commit: str,
                       index: dict[str, tuple[str, str]]) -> tuple[str | None, str | None]:
    """Put bytes into the target THROUGH ITS OWN INDEX, and let its filters decide the worktree (S5).

    Three plumbing calls, in this order and for this reason. `hash-object -w --stdin` puts the blob
    in the TARGET's object database unchanged — no clean filter runs, so what lands is what gov
    shipped, byte for byte. `update-index --cacheinfo` names it at the row's path. `checkout-index
    -f` materialises the worktree file, which is the ONLY step that runs the target's smudge filter.

    The replaced `write_bytes` had this exactly backwards: it decided the WORKTREE bytes from here
    and left the index to catch up, so on a clone with a line-ending filter every file gov landed was
    immediately `modified` in the target's own `git status`.

    MODE from the row's existing index entry, and from gov's tree entry at `commit` for a row with
    none (§8 F1) — a hook that lands non-executable is a hook that does not run.

    Returns `(oid, None)` on success and `(None, why)` on failure. A failure LEAVES the index entry
    rather than half-writing; rolling one back is `-14`'s.
    """
    out = subprocess.run(["git", "-C", str(target), "hash-object", "-w", "--stdin"],
                         input=data, capture_output=True, check=False)
    if out.returncode != 0:
        return None, f"git hash-object refused the bytes: {out.stderr.decode('utf-8', 'replace').strip()}"
    oid = out.stdout.decode("utf-8", "replace").strip()
    entry = index.get(path)
    mode = entry[0] if entry else ((gov_tree_mode(root, to_commit, src) if src else None) or "100644")
    up = subprocess.run(["git", "-C", str(target), "update-index", "--add", "--cacheinfo",
                         f"{mode},{oid},{path}"], capture_output=True, text=True, check=False)
    if up.returncode != 0:
        return None, f"git update-index refused {mode},{oid[:12]},{path}: {up.stderr.strip()}"
    (target / path).parent.mkdir(parents=True, exist_ok=True)
    co = subprocess.run(["git", "-C", str(target), "checkout-index", "-f", "--", path],
                        capture_output=True, text=True, check=False)
    if co.returncode != 0:
        return None, (f"the index now names {oid[:12]} at '{path}' and `git checkout-index` could "
                      f"not write the worktree file: {co.stderr.strip()}")
    return oid, None


def three_way(ours: bytes, base: bytes, theirs: bytes) -> tuple[bytes | None, str]:
    """Delegate to `git merge-file`, which is this repo's structural merge primitive.

    The row-keyed merge driver already hands its structure lines to exactly this call. A wrong
    argument order does NOT error here — it emits a plausible file with one side silently dropped —
    which is why every arm asserts merged CONTENT and never the exit code.
    """
    import tempfile as _tf
    with _tf.TemporaryDirectory() as td:
        d = pathlib.Path(td)
        (d / "ours").write_bytes(ours)
        (d / "base").write_bytes(base)
        (d / "theirs").write_bytes(theirs)
        out = subprocess.run(["git", "merge-file", "-p",
                              str(d / "ours"), str(d / "base"), str(d / "theirs")],
                             capture_output=True, check=False)
        if out.returncode == 0:
            return out.stdout, "merged"
        return None, "conflict"


def cmd_update(root: pathlib.Path, target: pathlib.Path, to_rev: str, write: bool,
               write_withdrawals: bool = False) -> int:
    """The verb. Its BODY is `_cmd_update`; see `cmd_apply` for why the split exists."""
    try:
        return _cmd_update(root, target, to_rev, write, write_withdrawals)
    finally:
        release_write_lock()


def _cmd_update(root: pathlib.Path, target: pathlib.Path, to_rev: str, write: bool,
                write_withdrawals: bool = False) -> int:
    """Move an installed target forward to a newer gov commit. READ-ONLY unless `--write`.

    The default is read-only because this verb's failure mode is silent data loss in a repository the
    operator owns and gov does not, and the muscle-memory invocation must not be the destructive one.
    """
    r = Report()
    reg = load_toml(root / "tools" / "govkit" / "registry.toml")
    descs = read_descriptors(root, reg, r)
    if r.problems:
        return r.emit()
    if pathlib.Path(root).resolve() == target.resolve():
        raise Refusal("--target resolves to the gov checkout itself")

    receipt_path = target / ".governance" / "install.json"
    if not receipt_path.is_file():
        raise Refusal(f"no receipt at {receipt_path.as_posix()} — `update` moves an install forward "
                      f"and there is no record of one here")
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    schema = receipt.get("schema", 1)
    base_commit = receipt.get("gov_commit")

    out = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", f"{to_rev}^{{commit}}"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise Refusal(f"--to '{to_rev}' does not resolve in this gov checkout")
    to_commit = out.stdout.strip()

    if base_commit:
        chk = subprocess.run(["git", "-C", str(root), "cat-file", "-e", f"{base_commit}^{{commit}}"],
                             capture_output=True)
        if chk.returncode != 0:
            raise Refusal(
                f"the receipt records gov commit {base_commit}, which does not resolve in this "
                f"checkout. REFUSING rather than treating the target as a fresh install: that "
                f"fallback classifies every file as missing and overwrites every local edit in a "
                f"repository gov does not own"
            )

    # ---- THE WRITE PRECONDITIONS (DEPL-dCarriedReceipt-12), in the build's declared order.
    # Steps 1 and 2 — mid-operation, unresolved index, dirty claimed paths, the lock — guard a
    # WRITE, so a read-only run does not pay them and does not create the lock file. Step 3,
    # the two vintage questions, runs on EVERY run: it grades the ARGUMENT rather than the
    # tree, it sits beside the two resolve-checks it completes, and a read-only preview of a
    # downgrade is a preview of something that will never be allowed to happen.
    if write:
        demand_writable_target(target, "update", receipt)
    demand_forward_vintage(root, base_commit, to_commit)
    demand_published_vintage(root, to_commit)

    claimed = receipt.get("kits") or []
    for eid in claimed:
        if eid not in descs:
            raise Refusal(f"the receipt claims kit '{eid}', which is no longer a registry entry — "
                          f"refusing rather than dropping it, which would leave its files owned by "
                          f"nobody")
    available = [e for e in all_kits(descs) if e not in claimed]

    # ---- THE PRECONDITIONS THIS UNIT ADDS (DEPL-dCarriedReceipt-7), steps 4 and 5 of the build's
    # ---- declared preamble order: after `-12`'s three and before any row is classified.
    # THE WHOLE LIST, unfiltered. A row with no `path` key is malformed and has always raised out of
    # the classification loop; filtering it out here would turn that into a silent drop, which is a
    # skip that looks like a pass — one row of a receipt quietly ungraded and nothing saying so.
    rows_all = receipt.get("files", [])

    # ---- SCHEMA MIGRATION, and it runs before S9 because S9's third arm grades a field this fills.
    # A receipt written before schema 3 carries no `gov_oid` at all, so every engine row in one would
    # read as S9's half-populated pair. Fill it ONCE, from EVIDENCE — gov's own blob at the row's
    # recorded `commit` — and never from `sha256`, which hashes the bytes that landed and is not an
    # object name. SCOPED TO `schema < RECEIPT_SCHEMA`: a schema-3 receipt is NEVER back-filled,
    # because a schema-3 row carrying `commit` and no `gov_oid` is exactly the corruption S9 exists
    # to catch, and filling it in is how a text-merged receipt gets laundered into a plausible one.
    # Scoped to LANDABLE_ROLES for S1's reason: those are the only rows whose destination holds a
    # whole-file gov blob. A `merged` row's gov bytes are a BLOCK inside a file the target owns and
    # an `attributes` row's are a block `lf_pins` composes — neither has a blob to name, and neither
    # gets one invented for it here.
    if schema < RECEIPT_SCHEMA:
        for row in rows_all:
            if row.get("role", "engine") not in LANDABLE_ROLES or row.get("gov_oid"):
                continue
            if not (row.get("source") and row.get("commit")):
                continue
            was = blob_at(root, row["commit"], row["source"])
            if was is not None:
                row["gov_oid"] = blob_oid(was)

    # ---- S9. THE RECEIPT'S OWN INTEGRITY, over EVERY row, before any of them is classified.
    # `gov_oid` is a STORED field and this is what a stored field costs. `install.json` is committed,
    # `-11` rewrites `path`, `source`, `commit` and `gov_oid` together on a rename, and a TEXT merge
    # of that file can pair `commit` from one side with `gov_oid` from the other. A stale `gov_oid`
    # that happens to equal the target's live index blob reads the delta predicate FALSE and opens
    # the raw-write arm on a row carrying a local edit.
    # SCOPED BY FIELD PRESENCE, in three arms, plus ONE exemption by ROLE.
    for row in rows_all:
        # §8 F4, RATIFIED. A row whose `role` is `merged` is passed over BY ROLE, whatever `commit`
        # it carries: that commit names the vintage the BLOCK was taken from, `UPDATE_ROLE['merged']`
        # is its reader, and S9 has no whole-file gov blob to assert against. The arm reads `role`
        # rather than `evidence` deliberately — `role` is on every row `apply` and `adopt` write, so
        # it needs no later precondition to have run. Without it the FIRST update against any target
        # that ever applied a hash-comment merged rule refuses everything: measured on a `push-main`
        # receipt, whose merged row carries `commit`, `source` and `block_sha256` and NEITHER
        # identity — which is the exactly-one shape two arms below.
        if row.get("role") == "merged":
            continue
        has_commit, has_gov = bool(row.get("commit")), bool(row.get("gov_oid"))
        if not has_commit and not has_gov:
            # Nothing to compare, so this is not a failed integrity check. NOTE WHAT THIS ROW IS
            # NOT: it is not necessarily `-13` S7's `evidence: "unattributed"` state. Every row
            # `apply` writes through the `unlanded` channel carries neither field, and so does the
            # synthesized `attributes` row. What happens to it next is its ROLE's business, in the
            # classification loop, not this preamble's.
            continue
        if has_commit and has_gov:
            was = blob_at(root, row["commit"], row["source"]) if row.get("source") else None
            now = blob_oid(was) if was is not None else None
            if now != row["gov_oid"]:
                raise Refusal(
                    f"receipt row '{row['path']}' records gov_oid {row['gov_oid']} for "
                    f"'{row.get('source')}' at {str(row.get('commit'))[:12]}, and gov's blob there "
                    f"is {now or '(no such blob)'}. REFUSING the whole run rather than classifying "
                    f"this row against an identity the file no longer earns: `gov_oid` is stored, "
                    f"and a stored identity that disagrees with its own evidence is how a "
                    f"text-merged receipt opens the raw-write arm on a locally edited file"
                )
            continue
        raise Refusal(
            f"receipt row '{row['path']}' carries "
            + ("`commit` and no `gov_oid`" if has_commit else "`gov_oid` and no `commit`")
            + ". The two are written together and are meaningless apart, so this pairing is the "
              "corruption shape a text merge of `install.json` produces — REFUSING the whole run "
              "rather than acting on half of it. A receipt below schema "
            + f"{RECEIPT_SCHEMA} has `gov_oid` filled from gov's blob at the row's own `commit` "
              "before this check, so a row that still lacks it either could not be upgraded — gov "
              "has no blob for that source at that commit — or was written at schema "
            + f"{RECEIPT_SCHEMA} and has since been split"
        )

    # ---- S4. A claimed path PRESENT IN THE WORKTREE and ABSENT FROM THE INDEX, over the same
    # ---- batched read S2 classifies from. Without this, the index read's own `absent` routes to
    # ---- `missing` and then to the write arm, which would overwrite whatever untracked file the
    # ---- operator has there. Evaluated HERE, in the preamble: it is a whole-run refusal and must
    # ---- not depend on which rows the loop has already reached.
    index0, index_present = index_read(target, [w["path"] for w in rows_all])
    shadowed = sorted(w["path"] for w in rows_all
                      if w["path"] not in index_present and (target / w["path"]).is_file())
    if shadowed:
        raise Refusal(
            "these receipt-claimed path(s) are present in the target's WORKTREE and absent from its "
            "INDEX: " + ", ".join(shadowed) + ". `update` reads ours from the index, so an untracked "
            "file there classifies as `missing` and the write arm would overwrite it with gov's "
            "bytes. REFUSING: track it (`git add`) if it is meant to be gov's, or move it aside if "
            "it is yours"
        )

    print(f"govkit update — {target.as_posix()}")
    print(f"govkit update — {base_commit[:8] if base_commit else '(none)'} -> {to_commit[:8]} · "
          f"receipt schema {schema} · {'WRITE' if write else 'read-only'}")

    # ---- DEPL-dCarriedReceipt-9 S3 + S7. The needle map, DERIVED from the receipt's own
    # ---- (source, path) pairs, and PRINTED before the first row is classified. A map that silently
    # ---- collapsed is indistinguishable from a target that genuinely relocated nothing, and that is
    # ---- the failure mode that would waste the most time. Neither number is written down anywhere:
    # ---- both come off the derivation, on this run, over this receipt.
    needles, carry_pairs, carry_dropped = derive_carry_map(
        [(w.get("source"), w.get("path")) for w in rows_all])
    for _gd, _dests in carry_dropped:
        print(f"govkit update — carry map DROPPED the ambiguous gov directory '{_gd}': this receipt "
              f"puts it at {', '.join(_dests)}, so it names no single destination and cannot be a "
              f"needle")
    print(f"govkit update — carry map: {len(carry_pairs)} directory pair(s), "
          f"{len(needles)} needle(s)")

    deploy = load_deploy(target)

    # ---- DEPL-dCarriedReceipt-11 S1 + S3. GOV'S OWN RENAMES, once per run, and the resolver that
    # ---- turns one into a destination. PRINTED before the first row is classified, for the reason
    # ---- the carry map above is: a run that silently found nothing is indistinguishable from a gov
    # ---- that renamed nothing, and the difference is whether an adopter's files are about to move.
    renames = derive_rename_map(root, base_commit, to_commit)
    print(f"govkit update — rename map: {len(renames)} gov source(s) moved between these two "
          f"vintages, at >= {RENAME_SIMILARITY_PERCENT}% similarity")
    rename_dests: dict[str, dict[str, list[str]]] = {}

    def resolve_renamed(row: dict) -> tuple[str, str] | None:
        """gov's new source for this row, and the ONE destination the descriptor puts it at.

        S3: the destination is RECOMPUTED through `resolve_entry`, never derived by string-editing
        the old one. A rename that crosses a rule boundary changes the descriptor's answer — gov's
        own fixture moves a file from a `**` engine pool into a rule with an explicit `to` — and a
        string edit would land it where the descriptor does not declare it. `resolve_entry` is the
        answer `apply` uses, and DEPL-dCarriedReceipt-1 exists because this file already paid once
        for a second spelling of it.

        DROPS LOUDLY, in the shape DEPL-dCarriedReceipt-9's carry map drops an ambiguous directory.
        Every `return None` here degrades the row to `withdrawn`, which after S8 deletes nothing —
        so the cost of dropping is a report, and the cost of guessing is a file in the wrong place.
        Both `writes` and `unlanded` are searched: a `rendered` or `forked` source is never written
        by this verb, but its row still gets a verdict, and a role's disposition decides what happens
        NEXT rather than whether the row moved.

        WHAT IT DOES NOT ANSWER, because a structural check reads as a semantic one to everybody
        who did not write it: it resolves the descriptor as it stands in THIS CHECKOUT, not as it
        stood at `to_commit`. That is the same approximation `apply` makes — `read_descriptors`
        reads the working tree — and it fails in the safe direction here: a new source this
        checkout's descriptor does not claim resolves to nothing, the row degrades to `withdrawn`,
        and after S8 a `withdrawn` row is a report and an order rather than a deletion.
        """
        old, eid = row.get("source"), row.get("kit")
        new = renames.get(old or "")
        if not new:
            return None
        if eid not in descs:
            print(f"  rename NOT taken  {row['path']}: gov moved '{old}' to '{new}', and this row "
                  f"names kit '{eid}', which no registry entry claims")
            return None
        if eid not in rename_dests:
            d, _p = descs[eid]
            res = resolve_entry(root, d, target_context(target, deploy, eid, d))
            by_src: dict[str, list[str]] = {}
            for _dest, _w in res["writes"].items():
                if _w.get("src"):
                    by_src.setdefault(_w["src"], []).append(_dest)
            for _u in res["unlanded"]:
                if _u.get("src"):
                    by_src.setdefault(_u["src"], []).append(_u["dest"])
            rename_dests[eid] = {k: sorted(set(v)) for k, v in by_src.items()}
        dests = rename_dests[eid].get(new) or []
        if len(dests) != 1:
            print(f"  rename NOT taken  {row['path']}: gov moved '{old}' to '{new}', which kit "
                  f"'{eid}' now resolves to "
                  + (f"{len(dests)} destinations ({', '.join(dests)}) — one row cannot move to "
                     f"several, and picking one would be a guess"
                     if dests else "no destination at all: it has left this kit's claimed surface, "
                                   "which from this receipt's side is a withdrawal and not a move"))
            return None
        return new, dests[0]

    tally: dict[str, int] = {}
    acted: list[dict] = []
    # S2's order, collected in the loop and written in the write phase below, where `outbox` exists.
    pins_order: str | None = None
    for row in rows_all:
        role = row.get("role", "engine")
        how = UPDATE_ROLE.get(role)
        if how is None:
            r.fail(f"receipt row '{row['path']}' carries role '{role}', which has no row in the "
                   f"update dispatch — refusing rather than classifying it from an absent field")
            continue

        # A schema-1 receipt's ROLE is untrusted: unit 1 measured that such a receipt stamps
        # `engine` on a file its descriptor declares project-owned. Re-resolve and refuse a
        # disagreement rather than acting on either answer.
        if schema < 2 and row.get("kit") in descs:
            d, _ = descs[row["kit"]]
            ctx = target_context(target, deploy, row["kit"], d)
            res = resolve_entry(root, d, ctx)
            w = res["writes"].get(row["path"])
            now = w["role"] if w else next(
                (u["role"] for u in res["unlanded"] if u["dest"] == row["path"]), None)
            if now and now != role:
                r.fail(f"row '{row['path']}' is recorded as '{role}' and its descriptor now resolves "
                       f"it as '{now}' — refusing this row rather than acting on a role a schema-1 "
                       f"receipt cannot be trusted about")
                continue

        if how == "block":
            # The block's own hash, not the file's. `check` owns the drift verdict; `update` reports
            # whether gov's block MOVED, and never merges: a gov-owned region has an owner.
            src2 = row.get("source")
            theirs2 = blob_at(root, to_commit, src2) if src2 else None
            base2 = blob_at(root, row.get("commit"), src2) if (src2 and row.get("commit")) else None
            v = "current" if _sha(theirs2) == _sha(base2) else "block-moved"
            tally[v] = tally.get(v, 0) + 1
            print(f"  {v:<18} [{role:<13}] {row['path']}")
            continue
        if how in ("skip",):
            tally[role + ":skipped"] = tally.get(role + ":skipped", 0) + 1
            continue
        if how == "refuse":
            r.fail(f"row '{row['path']}' has role '{role}', which no unit has taught `update` to "
                   f"move yet — refusing by name rather than guessing")
            continue

        # DEPL-dCarriedReceipt-2 S3. REPORT, never refuse: these roles have no writer yet, but a
        # role without a writer is not a reason to strand the whole receipt. `r.fail` here set
        # `r.problems`, which permanently skips the re-stamp at the end of this function, so one
        # such row froze a target's `gov_commit` forever.
        if how == "report":
            tally[role + ":reported"] = tally.get(role + ":reported", 0) + 1
            # DEPL-dCarriedReceipt-10 S4. `direction` is an OPTIONAL TRAILING FIELD on the one
            # printed row, never a second line and never a second row — the `report` disposition's
            # shape is `-2`'s and is not re-specified here. READ WITH `.get`, deliberately: `how` is
            # resolved from the RECEIPT's role a few lines above, so this printer meets rows this
            # unit never wrote — one stamped before the role existed, one whose descriptor has since
            # changed its keys — and `row["direction"]` would raise `KeyError` on exactly those,
            # turning the report disposition into a traceback on the one path that exists to avoid
            # acting. The missing-key refusal is selfcheck arm 3c's, and it fires on DESCRIPTORS.
            _dir = row.get("direction")
            print(f"  {'report':<18} [{role:<13}] {row['path']}"
                  + (f" · direction {_dir}" if _dir else ""))
            continue

        # DEPL-dCarriedReceipt-2 S2. The pins row is SYNTHESIZED by `apply`, not shipped by a kit,
        # so it has no gov blob and `classify_row` has nothing to compare. Recompute what `apply`
        # would write now, and compare it against the block the target actually holds. This arm
        # never merges and never edits `.gitattributes`: that destination belongs to `apply`.
        if how == "pins":
            _pins = lf_pins(descs, [e for e in claimed if e in descs],
                            lambda e, dd: target_context(target, deploy, e, dd))
            _om, _cm, _text = lf_pin_block(_pins) if _pins else ("", "", "")
            _ga = target / row["path"]
            _cur = _ga.read_text(encoding="utf-8", errors="replace") if _ga.is_file() else ""
            # LINE indices, inclusive of both markers -- not character offsets. Slicing the string
            # with them silently produced a prefix that never matched, so the `current` arm could
            # not fire and every target read `pins-moved` forever. Caught by observing the arm on a
            # target whose block was known to be correct.
            _span = find_block(_cur, _om, _cm) if _pins else None
            _held = "\n".join(
                _cur.split("\n")[_span[0]:_span[1] + 1]) if _span else None
            v = "current" if (_held is not None and _held.strip() == _text.strip()) else "pins-moved"
            tally[v] = tally.get(v, 0) + 1
            print(f"  {v:<18} [{role:<13}] {row['path']}")
            if v == "pins-moved":
                pins_order = _text
            continue

        # DEPL-dCarriedReceipt-13 S7. A BOOTSTRAPPED row that matched no gov vintage has no base,
        # and every writing disposition needs one — so it is printed, counted and skipped HERE:
        # after `how` resolves, before the verdict table it would otherwise feed. Written in
        # neither direction until an operator supplies a base with `adopt --pin`.
        #
        # SCOPED TWO WAYS, and both halves are load-bearing rather than defensive. The predicate is
        # `evidence == "unattributed"` and NEVER field-absence: every row `apply` writes through the
        # unlanded channel carries neither `commit` nor `gov_oid`, and so does the synthesized
        # `attributes` row, so a field-absence reading would swallow all of them ahead of the
        # dispatch and silently delete four dispositions that exist for exactly those roles. And it
        # is scoped to `table`, the ONLY disposition that can put bytes on disk: `seed` still
        # reaches its reseed override and `attributes` still reaches `-2`'s pins arm, each of which
        # reports against a `base` of `None` rather than needing one. AC14 grades both halves.
        # THE ROW SHAPE IS `-2`'s AND ENDS AT THE PATH. The remedy sentence goes in the tally line
        # below, once, rather than onto every row: the printed row is PARSED by name elsewhere —
        # `-7`'s AC9 arm reads the verdict off a line whose last field is the path — and a trailing
        # clause here made that arm read "(no row)" for a row this branch had just printed.
        if how == "table" and row.get("evidence") == "unattributed":
            tally["unattributed"] = tally.get("unattributed", 0) + 1
            print(f"  {'unattributed':<18} [{role:<13}] {row['path']}")
            continue

        c = classify_row(root, target, row, to_commit, index0, needles, resolve_renamed)

        # DEPL-dCarriedReceipt-9 S2. `carry` is OUTPUT. It was recomputed from the blobs one line
        # above and is written back for REPORTING; a stale one left by an older run is DROPPED
        # rather than believed, so the field can never be a claim about bytes that have moved since.
        # No branch in either verb reads it back — asserted over this file's SOURCE by an arm,
        # because "nobody will read it" is a discipline and this is a gate.
        if c["carry"]:
            row["carry"] = c["carry"]
        else:
            row.pop("carry", None)

        v = c["verdict"]
        if how == "seed" or how == "report-reseed":
            if c["t_state"] == "differs":
                v = "reseed-available"
            elif v not in ("missing", "renamed"):
                # DEPL-dCarriedReceipt-11 S0c. `renamed` IS EXEMPT FROM THIS OVERRIDE, beside
                # `missing`, and the exemption is the sharpest thing in that unit. This line rewrites
                # any surviving verdict on a seed row to `current`/`patched` — which for a row whose
                # gov SOURCE gov renamed means printing `current` over a source that no longer
                # exists. Measured at 9ddcc5c9 on this unit's own fixture: the seed row read
                # `t_state = "absent"`, gridded to `withdrawn`, and came out of this line as
                # `current` while the file behind it had moved. That is a silent-green of exactly
                # the kind the comment at the reported-only branch below records an incident for.
                v = "current" if c["o_state"] == "equal" else "patched"
        if how == "adopter" and v in ("diverged", "stale"):
            v = "re-rendered"          # CAP at report; the adopter owns these bytes
        if v == "patched" and c["carry"] in ("eol", "relocate"):
            # DEPL-dCarriedReceipt-9 S10. `("differs","equal")` grids to `patched`, which is a LIE
            # for a carried row: the target edited NOTHING, it installed at a different prefix or
            # committed different line endings. Sourced from `carry` and from nothing else, and the
            # tally counts it under the label it printed rather than under the one it replaced.
            v = f"carried ({c['carry']})"
        tally[v] = tally.get(v, 0) + 1
        print(f"  {v:<18} [{role:<13}] {row['path']}")
        acted.append({"row": row, "c": c, "verdict": v, "how": how})

    for line in (f"  available (not installed): {e}" for e in available):
        print(line)
    if available:
        print("govkit update — the entries above are registry entries this receipt does not claim. "
              "`update` does not install them: widening a target's governance surface is an owner "
              "decision, and `--add-kits` is the flag that would")
    print("govkit update — " + " · ".join(f"{k} {v}" for k, v in sorted(tally.items())))
    # DEPL-dCarriedReceipt-13 S7's remedy, said ONCE and only when it applies. An operator who sees
    # `unattributed` rows and no next step concludes the tool is broken; one who sees the sentence
    # repeated per row learns to scroll past the whole block.
    if tally.get("unattributed"):
        print(f"govkit update — {tally['unattributed']} row(s) matched no gov vintage at adoption, "
              f"so there is no base to write against and none was written. `govkit adopt --pin "
              f"<path>=<rev>` supplies one")

    if not write:
        print("govkit update — read-only. NOTHING was written; re-run with --write to perform it.")
        return r.emit()

    outbox = target / ".governance" / "outbox"
    outbox.mkdir(parents=True, exist_ok=True)
    changed, deleted, conflicts = [], [], 0
    # DEPL-dCarriedReceipt-11 S6. BOTH SPELLINGS of every performed rename, in the shape `changed`
    # and `deleted` already take. `git mv` stages both ends, so this is not a second `git add` and
    # nothing below re-adds it: it exists because DEPL-dCarriedReceipt-14's pre-write snapshot and
    # its touched-kit predicate read these lists, and a renamed row is invisible to both through
    # `changed` and `deleted` alone.
    renamed: list[str] = []
    withheld = 0
    # DEPL-dCarriedReceipt-2 S2: an ORDER, not a write. `.gitattributes` is `apply`'s destination
    # and DEPL-dSettledRoster-1 is an open ask about how it writes them, so this verb states what
    # moved and stops. Written under `--write` only, matching every other order this verb emits.
    if pins_order is not None:
        (outbox / "update-pins.md").write_text(
            "# gov's LF pins have moved\n\n"
            "The govkit-owned block in this target's `.gitattributes` no longer matches what the\n"
            "claimed kits declare at the requested vintage. `update` does NOT write that file:\n"
            "the destination is `apply`'s. Re-run `govkit apply` to move the block.\n\n"
            "The block gov would write now:\n\n```\n" + pins_order + "\n```\n",
            encoding="utf-8", newline="\n")
    # ---- DEPL-dCarriedReceipt-14 S2 + S3 + S4. THE PRE-WRITE SNAPSHOT AND THE BASELINE, in that
    # ---- order and BEFORE the first byte of any kit path moves. Everything below this block is a
    # ---- write; everything in it is a read.
    #
    # THE SNAPSHOT IS KEYED ON THE ROW, never on a path string. A `renamed` row occupies TWO
    # spellings — the old one it is about to leave and the new one it is about to land at — and the
    # new one's pre-write index state is `absent`, which under a path key sits behind a key the old
    # spelling never reaches. So a path-keyed snapshot cannot restore a rename at all: it would put
    # the old path back and leave gov's bytes staged at the new one, which is both halves of the
    # rename standing at once.
    _touching = set(TOUCHING_VERDICTS) | ({"withdrawn"} if write_withdrawals else set())
    snap_rows: list[dict] = []
    for a in acted:
        if a["how"] != "table" or a["verdict"] not in _touching:
            continue
        _paths = [a["row"]["path"]]
        if a["verdict"] == "renamed" and a["c"].get("renamed_to"):
            _paths.append(a["c"]["renamed_to"][1])
        snap_rows.append({"kit": a["row"].get("kit"), "row": a["row"], "paths": _paths,
                          "fields": {k: a["row"][k] for k in ROLLBACK_FIELDS if k in a["row"]}})

    # THE INDEX SIDE IS `-7`'s READER, not a second one. `index0` is the batched read the preamble
    # already took over every receipt path; a rename DESTINATION is by definition not one of those,
    # so the only paths that need a second call are those, and they go through the same
    # `index_read`. A path with no entry is stored as None — the marker `absent` — and that is a
    # DIFFERENT fact from "not looked up", which is why the lookup is materialised per row here
    # rather than deferred to a `.get` at restore time.
    _receipt_paths = {w["path"] for w in rows_all}
    _extra = sorted({p for s in snap_rows for p in s["paths"] if p not in _receipt_paths})
    _index_extra: dict[str, tuple[str, str]] = {}
    if _extra:
        _index_extra, _ = index_read(target, _extra)
    for s in snap_rows:
        s["index"] = {p: (index0.get(p) if p in _receipt_paths else _index_extra.get(p))
                      for p in s["paths"]}

    # S4's POPULATION, and the reason the baseline is affordable: exactly the kits this run is about
    # to write to, which is exactly the set the after-pass will check. Baselining every CLAIMED kit
    # would run checks for kits the run never touches, which is the whole-bar behaviour §3 refuses.
    touched_kits = [e for e in claimed if any(s["kit"] == e for s in snap_rows)]
    orphan_kits = sorted({(s["kit"] or "(no kit)") for s in snap_rows if s["kit"] not in claimed})
    baseline: dict[str, tuple[str, str, int | None]] = {}
    for _eid in touched_kits:
        _d, _ = descs[_eid]
        baseline[_eid] = run_kit_check(_eid, _d, target_context(target, deploy, _eid, _d), target)

    withdrawn_rows: list[dict] = []
    for a in acted:
        row, c, v = a["row"], a["c"], a["verdict"]

        # A receipt path is TARGET-SUPPLIED data. Joining it onto the target root and writing is a
        # traversal away from the repository the operator named, which is the one boundary this whole
        # tool is built around. Resolve and contain before any write.
        dp = (target / row["path"]).resolve()
        try:
            dp.relative_to(target.resolve())
        except ValueError:
            r.fail(f"receipt row '{row['path']}' resolves outside the target repository — refusing "
                   f"it: a path that escapes the tree the operator named is not a path this verb "
                   f"may write, whatever the verdict says")
            continue

        # THE ROLE DECIDES, not the verdict. `how` is what the role dispatch computed; branching on
        # the verdict alone writes gov's RAW bytes for a role declared never-written — measured, a
        # `rendered` row on a `missing` verdict landed an unrendered template, placeholders and all,
        # into an adopter tree at exit 0, and a `seed` the target had deleted was silently restored
        # from gov rather than left to the target that owns it.
        if a["how"] != "table":
            # DEPL-dCarriedReceipt-11 S0b. `renamed` joins this tuple, and it has to: a verdict word
            # absent from it falls through to the bare `continue` below, so a `rendered` or `seed`
            # row whose gov source MOVED would get its verdict line and then nothing at all from the
            # verb that just decided not to write it. The line is a SECOND line rather than the only
            # one — every row in `acted` already printed its verdict above — and what it adds is the
            # disposition: this role is reported, never moved.
            if v in ("missing", "stale", "withdrawn", "diverged", "renamed"):
                print(f"  reported only   [{row.get('role')}] {row['path']} — {v}; this role is "
                      f"never written by `update`")
            continue

        if v in RAW_WRITE_VERDICTS:
            data = c["theirs"]
            # ---- DEPL-dCarriedReceipt-9 S11. THE `missing` RESTORE CARRIES TOO, and it is the ONE
            # ---- arm in this verb that writes bytes gov does not hold WITHOUT a bytes-proof —
            # ---- because there are no `ours` bytes to prove a rung against: the target DELETED the
            # ---- file. `classify_row` returns `o_state = "absent"`, both `absent` cells grid to
            # ---- `missing`, and `missing` shares the raw arm right here, so without this a
            # ---- rung-carrying row the target deleted comes back in gov's un-carried spelling.
            # ---- Bounded twice over: it fires only on `missing`, and it applies the row's OWN
            # ---- (dirname(source), dirname(path)) pair rather than the derived map — which needs
            # ---- no bytes and is exactly S3's derivation over one pair — so a literal inside the
            # ---- restored file can only be rewritten by that one row's own relocation. That
            # ---- residual is accepted: the alternative on this arm is writing gov's prefix into a
            # ---- target that demonstrably does not use it.
            restored_carry = None
            if v == "missing" and row.get("source"):
                _one, _, _ = derive_carry_map([(row["source"], row["path"])])
                _carried = derive_carried(data, _one)
                if _carried != data:
                    data, restored_carry = _carried, "relocate"
            oid, why = land_through_index(root, target, row["path"], row.get("source"),
                                          data, to_commit, index0)
            if oid is None:
                r.fail(f"'{row['path']}' could not be landed: {why}")
                continue
            # DEPL-dCarriedReceipt-9 S12, which NARROWS one cell of `-8`'s write table rather than
            # contradicting it. ONE stamping rule: `oid` records the blob ACTUALLY WRITTEN, and
            # `gov_oid` keeps the meaning `-8` gives it — gov's blob at the row's `commit`, which
            # this write advances to `to_commit` two lines below.
            #
            # On the UN-CARRIED raw arm the two agree BY CONSTRUCTION, which is `-8`'s stamp
            # unchanged: gov's blob went into the target's object database untouched, so the name the
            # target gave it is the name gov's tree gives it. On a CARRIED restore they DIFFER, and
            # that is the point — `oid != gov_oid` afterwards reads "this row carries a rung", not
            # "local delta", because `carry` is re-proved from the blobs on the next run and
            # re-explains the difference. Taking the un-narrowed stamp there is the corrupt pairing:
            # two identities recorded EQUAL over bytes gov never shipped, which the next run reads as
            # a clean gov-owned row and raw-overwrites straight back to gov's prefix.
            #
            # `sha256` follows the bytes that LANDED, because that is what `install.sums` lists and
            # what a target verifies with bash alone. It decides nothing here.
            row["gov_oid"] = blob_oid(c["theirs"])
            row["oid"] = oid
            row["sha256"] = _sha(data)
            row["commit"] = to_commit
            if restored_carry:
                row["carry"] = restored_carry
            changed.append(row["path"])
        elif v == "renamed":
            # ---- DEPL-dCarriedReceipt-11 S4 / S5 / S11. GOV MOVED THIS FILE, so the target's copy
            # ---- moves with it. Everything that decides bytes happens BEFORE the move, and that
            # ---- ordering is the unit rather than a style: `git mv` moves bytes unchanged, so a
            # ---- post-move comparison would ask "does the target's copy match gov's blob at the new
            # ---- source" of a file nobody has written yet, answer no, and freeze it at pre-rename
            # ---- content while printing `patched` — the grid's word for an adopter edit that never
            # ---- happened. Deciding first also means a conflict leaves the row EXACTLY as it was,
            # ---- rather than half-applied at a new path.
            new_src, new_dest = c["renamed_to"]
            ndp = (target / new_dest).resolve()
            try:
                ndp.relative_to(target.resolve())
            except ValueError:
                r.fail(f"gov moved '{row.get('source')}' to '{new_src}', which this target's own "
                       f"descriptor resolves to '{new_dest}' — a path OUTSIDE the repository the "
                       f"operator named. Refusing the move: the destination is composed from that "
                       f"target's answers, so a `prefix` that climbs out of the tree is a write "
                       f"this verb may not perform whatever the verdict says")
                continue
            # ASKED OF THE INDEX AND OF THE DISK, both. The preamble's batched read covers the
            # RECEIPT's paths and a rename destination is by definition not one of them, so a
            # tracked file there whose worktree copy the operator removed is invisible to `exists()`
            # — and `git mv` would take its index entry without a word.
            _, _at_dest = index_read(target, [new_dest])
            if new_dest in _at_dest or ndp.exists():
                r.fail(f"gov moved '{row.get('source')}' to '{new_src}', which resolves to "
                       f"'{new_dest}' — and this target ALREADY holds a file there. Refusing rather "
                       f"than overwriting it: `update` moves one row and would be destroying "
                       f"another file's bytes to do it. Move or remove '{new_dest}' and re-run")
                continue

            # THE BYTES, decided here and written after the move. `carry == "verbatim"` IS S4's
            # no-delta question — the ladder proves it on BYTES, which is the same question the
            # spec asks of the pre-move `oid` and strictly better than an oid comparison on a target
            # whose object format is not gov's. No delta means gov's blob at the NEW source, raw,
            # with `commit` and `gov_oid` advancing together beneath it.
            #
            # EVERYTHING ELSE TAKES THE THREE-WAY, and that includes a row DEPL-dCarriedReceipt-9
            # proved a rung for (S11): a carried row's bytes never equal gov's blob at the old
            # source, so it lands here by construction, and a proven rung must never open the raw
            # arm or the target's own spelling is replaced by gov's at the new path. The rung is
            # applied to BOTH sides exactly as the `diverged` arm below applies it, at the two
            # vintages and the two sources this unit names: the OLD source at the row's own
            # `commit`, and the NEW source at `to_commit`. It cancels in the base-to-theirs diff,
            # so `git merge-file` sees only gov's semantic change.
            byte_arm = "gov" if c["carry"] == "verbatim" else "merged"
            if c["carry"] == "verbatim":
                data = c["theirs_new"]
            else:
                merged, _how = three_way(
                    c["ours"],
                    derive_carried_by_rung(c["carry"], c["base"] or b"", needles),
                    derive_carried_by_rung(c["carry"], c["theirs_new"], needles))
                if merged is None:
                    conflicts += 1
                    (outbox / f"update-conflict-{pathlib.PurePosixPath(row['path']).name}.md"
                     ).write_text(
                        f"# update conflict — {row['path']} (gov RENAMED this file)\n\n"
                        f"gov moved  {row.get('source')} -> {new_src}\n"
                        f"carry  {c['carry'] or '(none — the difference is a local delta)'}\n"
                        f"base   {row.get('commit')} sha {_sha(c['base'])}\n"
                        f"ours   target index  sha {_sha(c['ours'])} oid {c['ours_oid']}\n"
                        f"theirs {to_commit} sha {_sha(c['theirs_new'])}\n\n"
                        f"NOTHING was moved and the file was left BYTE-IDENTICAL at its old path.\n"
                        f"Resolve by hand, then re-run `update`.\n",
                        encoding="utf-8", newline="\n")
                    r.fail(f"'{row['path']}' was renamed by gov to '{new_src}' and the three-way "
                           f"conflicts — left untouched at its old path, order written")
                    continue
                data = merged

            # THE MOVE. The parent is created here because `git mv` does NOT create one — measured:
            # a rename into a new subdirectory fails with `destination directory does not exist`,
            # which would make every into-a-subdir rename a reported failure. Both failure modes are
            # ONE report: the row is left exactly as it was, and nothing about it is rewritten.
            old_path = row["path"]
            mv_err: str | None = None
            try:
                ndp.parent.mkdir(parents=True, exist_ok=True)
                mv = subprocess.run(["git", "-C", str(target), "mv", "--", old_path, new_dest],
                                    capture_output=True, text=True, check=False)
                if mv.returncode != 0:
                    mv_err = mv.stderr.strip() or f"git mv exited {mv.returncode}"
            except OSError as e:
                mv_err = str(e)
            if mv_err:
                r.fail(f"'{row['path']}' could not be moved to '{new_dest}': {mv_err} — the row is "
                       f"left exactly as it was, at its old path and its old vintage")
                continue

            oid, why = land_through_index(root, target, new_dest, new_src, data, to_commit, index0)
            if oid is None:
                # NO ARM REACHES THIS, and the skip announces itself rather than passing for
                # coverage. `land_through_index` fails only when the TARGET's own git refuses —
                # a rejected blob write, a mode `update-index` will not take, a worktree file
                # `checkout-index` cannot replace — and this suite manufactures none of those; the
                # two older call sites above are in exactly the same position. What it leaves is a
                # moved file whose bytes are still the pre-move ones, reported and not re-stamped.
                r.fail(f"'{row['path']}' was moved to '{new_dest}' and the bytes could not be "
                       f"landed: {why}. The move is staged and the row is NOT advanced, so a re-run "
                       f"sees the file at its new path with its old vintage")
                continue
            # THE FOUR FIELDS, REWRITTEN TOGETHER. `path` and `source` carry the new spelling, which
            # is what makes the NEXT run's classification correct; `commit` advances to `to_commit`
            # and `gov_oid` becomes gov's blob at the NEW source there, because those two are
            # meaningless apart and DEPL-dCarriedReceipt-7's preamble refuses a receipt that pairs
            # one vintage's `commit` with another's `gov_oid`. `oid` records what the target now
            # holds — equal to `gov_oid` on the raw arm by construction, and deliberately different
            # on the merge arm, where it reads "this row carries something gov did not ship".
            row["path"], row["source"] = new_dest, new_src
            row["gov_oid"] = blob_oid(c["theirs_new"])
            row["oid"] = oid
            row["sha256"] = _sha(data)
            row["commit"] = to_commit
            renamed.extend([old_path, new_dest])
            # The DESTINATION line. The verdict row above names the old path, which is the only
            # spelling the receipt had when it was printed; where the file went is the other half,
            # and it ends in the byte arm rather than in a path so that nothing parsing this output
            # for a row's verdict can mistake this line for one.
            print(f"  moved            [{row.get('role')}] {old_path} -> {new_dest} · "
                  f"bytes {byte_arm}")
        elif v == "withdrawn":
            # ---- DEPL-dCarriedReceipt-11 S8 + S9. THE ENGINE'S ONLY UNGUARDED DELETE, CLOSED. What
            # ---- stood here removed a tracked file from a repository gov does not own — unlinked
            # ---- it, `git rm`-ed it and dropped its row — with no flag, no order and no way for
            # ---- anything downstream to notice, and it did so on the same verdict a gov RENAME
            # ---- produces, which is how the replacement was never landed either.
            #
            # The report and the ORDER are unconditional under `--write`; the DELETION needs
            # `--write-withdrawals`, which defaults OFF. That flag is a SCOPE flag and not a
            # `--force`: it enables a narrower class of action and overrides no refusal. The order is
            # written either way, because a deletion that happened and a deletion that was withheld
            # are both things the operator has to be able to read afterwards.
            _why = ("It WAS deleted: this run carried --write-withdrawals."
                    if write_withdrawals else
                    "NOTHING was deleted. `update` no longer removes a tracked file from a "
                    "repository gov does not own on the strength of a verdict alone. Re-run with "
                    "--write-withdrawals if this file really should go.")
            (outbox / f"update-withdrawn-{pathlib.PurePosixPath(row['path']).name}.md").write_text(
                f"# gov no longer ships {row['path']}\n\n"
                f"source {row.get('source')}\n"
                f"last gov commit {row.get('commit')}\n"
                f"vintage asked for {to_commit}\n\n"
                f"gov's tree holds no blob for that source at the requested vintage, and no rename "
                f"pair at >= {RENAME_SIMILARITY_PERCENT}% similarity names a replacement for it.\n\n"
                f"{_why}\n",
                encoding="utf-8", newline="\n")
            if not write_withdrawals:
                withheld += 1
                continue
            if dp.is_file():
                dp.unlink()
            deleted.append(row["path"])
            # And DROP the row. Keeping it leaves the receipt and the sidecar claiming a file gov no
            # longer ships and the target no longer has, which unit 5's integrity loop then reports
            # forever — every updated target permanently red, from a successful update.
            withdrawn_rows.append(row)
        elif v == "diverged":
            if c["ours"] is None:
                # OURS is now read from the target's object database rather than off its disk, so
                # this is the one new way it can be missing: the index names a blob the odb does not
                # hold. NO ARM REACHES THIS, and the skip announces itself rather than passing for
                # coverage — manufacturing a corrupt object database is not something this suite
                # does, and merging against a silent `b""` would drop the operator's whole side.
                r.fail(f"'{row['path']}' is diverged and its index blob {str(c['ours_oid'])[:12]} "
                       f"does not read back from the target's object database — refusing to merge "
                       f"against bytes this verb could not obtain")
                continue
            # DEPL-dCarriedReceipt-9 S6. A row that PROVED a rung and has since diverged is
            # reconciled rather than raw-written, and what makes that work is WHAT THE THREE-WAY IS
            # HANDED: the rung applied to BOTH `base` and `theirs`, so it cancels in the
            # base-to-theirs diff and `git merge-file` sees only gov's semantic change. `ours` is
            # left alone — it is already in the target's own spelling, which is the spelling the
            # merged result must come out in. Without this, a `relocate` row hands the merge a base
            # that spells gov's prefix where the target's copy does not, so every line naming a path
            # reads as an operator edit and the whole file conflicts.
            merged, how = three_way(
                c["ours"],
                derive_carried_by_rung(c["carry"], c["base"] or b"", needles),
                derive_carried_by_rung(c["carry"], c["theirs"], needles))
            if merged is None:
                conflicts += 1
                (outbox / f"update-conflict-{pathlib.PurePosixPath(row['path']).name}.md").write_text(
                    f"# update conflict — {row['path']}\n\n"
                    f"carry  {c['carry'] or '(none — the difference is a local delta)'}\n"
                    f"base   {base_commit} sha {_sha(c['base'])}\n"
                    f"ours   target index  sha {_sha(c['ours'])} oid {c['ours_oid']}\n"
                    f"theirs {to_commit} sha {_sha(c['theirs'])}\n\n"
                    f"The file was left BYTE-IDENTICAL. Resolve by hand, then re-run `update`.\n",
                    encoding="utf-8", newline="\n")
                r.fail(f"'{row['path']}' diverged and the three-way conflicts — left untouched, "
                       f"order written")
            else:
                oid, why = land_through_index(root, target, row["path"], row.get("source"),
                                              merged, to_commit, index0)
                if oid is None:
                    r.fail(f"'{row['path']}' merged cleanly and could not be landed: {why}")
                    continue
                # DEPL-dCarriedReceipt-8 S1. THE TWO IDENTITIES SPLIT HERE, and this is the one
                # branch where they must. `gov_oid` is GOV's blob at the row's `commit`, and
                # `commit` advances to `to_commit` two lines below, so the only bytes that can name
                # it are gov's own at that vintage — `c["theirs"]`, which `classify_row` already
                # read through `blob_at`. `oid` is what the TARGET now holds, which is the merge
                # result. Nothing the target produced may reach `gov_oid`, ever.
                #
                # WHY THIS IS THE WHOLE UNIT. Stamping the merge result into gov's identity made the
                # NEXT run read `ours == gov_oid` — the target does hold the merged bytes — so
                # `o_state` came back `equal`, the grid's `("equal", "differs")` cell said `stale`,
                # and the raw arm above overwrote the adopter's edit and reported it as a clean
                # write with zero conflicts. Reproduced end to end at 9ddcc5c9: local line count 1
                # after the merge, 0 after the update that followed it, rc 0 and no finding printed.
                # After `-7` the same stamp instead disagrees with its own evidence, so S9's
                # preamble refuses the WHOLE run for good and the target can never be updated
                # again — a different symptom of one defect, measured on `-7`'s tip before this.
                #
                # The permanence falls out rather than being flagged: these two now differ, so the
                # row's OURS axis reads `differs` on every later run, and `differs` reaches only
                # `patched` and `diverged` — neither of which is in `RAW_WRITE_VERDICTS`. An adopter
                # who later reverts the edit by hand puts the index blob back to `gov_oid` and the
                # row rejoins the raw arm on its own — what a stored boolean would get wrong.
                #
                # DEPL-dCarriedReceipt-9 S12, on the other arm that writes bytes gov does not hold.
                # `c["theirs"]` here is gov's UN-CARRIED blob — S6 rewrote only what was handed to
                # `three_way`, never the row's evidence — so `gov_oid` still names a blob gov's own
                # tree holds at `to_commit`, and a carried row's `oid != gov_oid` afterwards reads
                # "carries a rung" for the same reason the restore arm's does.
                row["gov_oid"] = blob_oid(c["theirs"])
                row["oid"] = oid
                row["sha256"] = _sha(merged)
                row["commit"] = to_commit
                changed.append(row["path"])

    # NO `git add` OVER `changed`. S5 already staged every one of those paths from gov's own bytes;
    # re-adding them would re-CLEAN what the smudge filter just produced, and a filter pair that does
    # not round-trip exactly would replace gov's blob with a near-miss nobody asked for. The staging
    # this verb owes is done, and it is done from the blob rather than from the disk.
    if deleted:
        subprocess.run(["git", "-C", str(target), "rm", "-q", "--ignore-unmatch", "--"] + deleted,
                       capture_output=True, check=False)

    # ======================= DEPL-dCarriedReceipt-14 S4..S8 — POST-WRITE VERIFICATION ============
    # Every byte this run was going to move has moved. Now ask each TOUCHED kit the one question it
    # already knows how to answer about itself — its own `[check].argv`, the same declaration
    # `cmd_check` runs — and compare that answer against the BASELINE taken before the write.
    #
    # THE ROLLBACK KEYS ON THE TRANSITION, never on the after-state alone, and that is the whole
    # difference between a verifier and a wedge. On the after-state alone, an adopter carrying ONE
    # unrelated local red in a touched kit reverts every correct write on EVERY run, forever: the
    # `r.fail` below reaches the `if r.problems` arm, `gov_commit` never advances, and §3 refuses
    # the `--force` that would otherwise be the way out. Red-before-and-red-after is reported as
    # pre-existing and left alone. What that trade costs is narrower and is stated rather than
    # implied: a kit already red keeps its writes, so a genuinely broken merge inside THAT kit lands
    # unobserved, because a binary check cannot tell "still broken" from "newly broken".
    #
    # IT RUNS UNCONDITIONALLY UNDER `--write`. There is no flag, in any spelling, because an opt-in
    # verifier verifies the runs that were already careful.

    # WHAT THE WRITE LOOP ACTUALLY DID, frozen before any rollback edits these lists. The snapshot's
    # population is what the loop was GOING to act on; this is what it reached. A row refused at its
    # own arm — a conflicting three-way, a rename destination the target already holds — is in the
    # first and not the second, and rolling one of those back is not merely wasted: the occupied
    # rename destination is an UNTRACKED operator file whose snapshot entry is `absent`, so the
    # `absent` arm below would unlink bytes this run never wrote and the refusal exists to protect.
    written_paths = set(changed) | set(renamed) | set(deleted)
    n_verified = n_unverified = n_rolled = n_preexisting = 0
    for eid in touched_kits:
        d, _ = descs[eid]
        ctx_v = target_context(target, deploy, eid, d)
        was, _was_detail, was_rc = baseline[eid]
        now, now_detail, now_rc = run_kit_check(eid, d, ctx_v, target)
        exits = f"exit {'no-launch' if was_rc is None else was_rc} -> " \
                f"{'no-launch' if now_rc is None else now_rc}"

        # S8. THE SKIP ANNOUNCES ITSELF. A `[check] = { none = "…" }` and an argv carrying an
        # unresolved token both land here, and a check that could not run is not a pass — so it is
        # counted apart from verified rather than swelling it.
        if now == "landed-unmeasured":
            n_unverified += 1
            print(f"govkit update — verify {eid}: {was} -> {now}{now_detail} · UNVERIFIED: nothing "
                  f"measured this kit's writes, which is not the same as measuring them green")
            continue

        # S6. PRE-EXISTING RED, the only escape from the wedge. Its writes stand, nothing is rolled
        # back, and no `r.fail` — so the run completes and the receipt re-stamps.
        if was == "landed-but-inert" and now == "landed-but-inert":
            n_preexisting += 1
            (outbox / f"update-preexisting-red-{eid}.md").write_text(
                f"# {eid} was already red before this update\n\n"
                f"check  {check_argv_of(d, ctx_v) or '(the kit declares no argv)'}\n"
                f"{exits}\n"
                f"vintage {base_commit} -> {to_commit}\n\n"
                f"This kit's own check failed BEFORE this run wrote anything and failed again "
                f"after, so this run did not break it and nothing was rolled back. Its writes "
                f"stand and the receipt re-stamps.\n\n"
                f"WHAT THIS DOES NOT SAY: a binary check cannot tell `still broken` from `newly "
                f"broken`, so a bad merge inside THIS kit would land unobserved. Fix the standing "
                f"red, then re-run `update` to get this kit verified again.\n",
                encoding="utf-8", newline="\n")
            print(f"govkit update — verify {eid}: {was} -> {now} · {exits} · PRE-EXISTING RED: not "
                  f"rolled back, and this run is not what broke it")
            continue

        # S5. GREEN BEFORE, RED AFTER: this run broke it, and only this kit is undone.
        if was == "adopted" and now == "landed-but-inert":
            n_rolled += 1
            # NO ARM REACHES THE THREE PLUMBING FAILURES BELOW, and the skip announces itself
            # rather than passing for coverage. Each fires only when the TARGET's own git refuses a
            # call — an entry `update-index` will not take, a worktree file `checkout-index` cannot
            # replace, an index `git rm --cached` will not touch — and this suite manufactures none
            # of those modes; `land_through_index`'s post-`git mv` failure is in exactly the same
            # position and says so where it stands. What each of them leaves is a PART-restored
            # target, and each says that in its own message, because a silent partial restore is
            # worse than the write it was undoing.
            restored: list[str] = []
            untouched: list[str] = []
            for s in [x for x in snap_rows if x["kit"] == eid]:
                for p in s["paths"]:
                    if p not in written_paths:
                        untouched.append(p)
                        continue
                    entry = s["index"].get(p)
                    if entry is None:
                        # `absent` before the write. The bytes at this path are ones this run put
                        # there — a rename destination, or a `missing` restore — so unstaging and
                        # unlinking returns the target to what it had, which was nothing.
                        rmv = subprocess.run(
                            ["git", "-C", str(target), "rm", "-q", "--cached", "--ignore-unmatch",
                             "--", p], capture_output=True, text=True, check=False)
                        if rmv.returncode != 0:
                            r.fail(f"rolling back kit '{eid}': '{p}' was absent from the index "
                                   f"before this run and `git rm --cached` would not unstage it: "
                                   f"{rmv.stderr.strip()}. The target is now PART restored — say so "
                                   f"rather than reporting a rollback that did not happen")
                            continue
                        if (target / p).is_file():
                            (target / p).unlink()
                        restored.append(p)
                        continue
                    mode, oid = entry
                    upx = subprocess.run(
                        ["git", "-C", str(target), "update-index", "--add", "--cacheinfo",
                         f"{mode},{oid},{p}"], capture_output=True, text=True, check=False)
                    if upx.returncode != 0:
                        r.fail(f"rolling back kit '{eid}': `git update-index` would not restore "
                               f"{mode},{oid[:12]},{p}: {upx.stderr.strip()}. The target is now "
                               f"PART restored")
                        continue
                    (target / p).parent.mkdir(parents=True, exist_ok=True)
                    cox = subprocess.run(
                        ["git", "-C", str(target), "checkout-index", "-f", "--", p],
                        capture_output=True, text=True, check=False)
                    if cox.returncode != 0:
                        r.fail(f"rolling back kit '{eid}': the index now names {oid[:12]} at '{p}' "
                               f"and `git checkout-index` could not write the worktree file: "
                               f"{cox.stderr.strip()}. The target is now PART restored — a silent "
                               f"partial restore is worse than the write it was undoing")
                        continue
                    restored.append(p)

                # S3 + S5. THE ROW'S OWN FIELDS, restored TOGETHER. Restoring bytes and leaving the
                # row stamped forward re-creates `-8` exactly — the next run reads the row as
                # `equal` against bytes that were reverted — and restoring only some of the six is
                # the split `-7` S9 refuses the whole next run on.
                for k in ROLLBACK_FIELDS:
                    if k in s["fields"]:
                        s["row"][k] = s["fields"][k]
                    else:
                        s["row"].pop(k, None)
                if s["row"] in withdrawn_rows:
                    withdrawn_rows.remove(s["row"])

            # The three lists are what the closing line counts, and a rolled-back path is not a
            # write that stands. Both spellings of a restored rename leave `renamed` together, so
            # its `// 2` stays a pair count.
            for p in restored:
                for lst in (changed, deleted, renamed):
                    while p in lst:
                        lst.remove(p)

            (outbox / f"update-rollback-{eid}.md").write_text(
                f"# {eid} was rolled back — its own check reds on what this run wrote\n\n"
                f"check  {check_argv_of(d, ctx_v) or '(the kit declares no argv)'}\n"
                f"{exits}\n"
                f"vintage {base_commit} -> {to_commit}\n\n"
                f"This kit's check PASSED before this run and FAILS after it, so this run is what "
                f"broke it. Every path below was restored to the index entry it had before the "
                f"first byte moved, and this kit's receipt rows were restored with them. No other "
                f"kit was touched: a green kit's write is correct and reverting it to punish a "
                f"sibling discards a good result.\n\n"
                + "".join(f"restored  {p}\n" for p in restored)
                + ("(nothing to restore: every path this kit owns was refused before it was "
                   "written)\n" if not restored else "")
                + "".join(f"left alone {p} — this run never wrote it, so there is nothing here to "
                          f"undo\n" for p in untouched)
                + f"\nThe receipt is NOT re-stamped, so the next run re-classifies these rows from "
                  f"the vintage they are actually at. Resolve by hand — most often the clean "
                  f"three-way merge that produced this is plausible and wrong — then re-run "
                  f"`update`.\n",
                encoding="utf-8", newline="\n")
            print(f"govkit update — verify {eid}: {was} -> {now} · {exits} · ROLLED BACK · "
                  + (" ".join(restored) if restored else "(no path restored)"))
            r.fail(f"kit '{eid}' passed its own check before this run and fails it after: "
                   f"{exits}. Its writes were ROLLED BACK to their pre-run index entries and an "
                   f"order was written under .governance/outbox/")
            continue

        n_verified += 1
        print(f"govkit update — verify {eid}: {was} -> {now} · {exits} · verified")

    for eid in orphan_kits:
        print(f"govkit update — verify {eid}: NOT VERIFIED — this run moved rows the receipt "
              f"attributes to that kit and its own `kits` list does not claim it, so there is no "
              f"descriptor to ask and no check to run")

    # S4's `not-run`, bounded to CLAIMED kits. An unclaimed registry entry is NOT one of these:
    # `available (not installed)` above already printed it, and a second line about the same kit is
    # two answers to one question in the output of the verb built to end silent partial installs.
    not_run = [e for e in claimed if e not in touched_kits]
    for eid in not_run:
        print(f"govkit update — verify {eid}: not-run — this run moved no path this kit owns, so "
              f"its check was executed neither before nor after")
    # EVERY COUNT PRINTS, including the zeros. An absence is never coverage, and a silent
    # pre-existing-red tally would hide exactly the kits nothing verified.
    print(f"govkit update — verify: verified {n_verified} · unverified {n_unverified} · "
          f"not-run {len(not_run)} · rolled back {n_rolled} · pre-existing red {n_preexisting}")

    if withdrawn_rows:
        receipt["files"] = [f for f in receipt["files"] if f not in withdrawn_rows]

    # The receipt is re-stamped ONLY on a clean run. Stamping it on a run that REFUSED rows is how a
    # schema-1 receipt whose role-distrust arm fired gets promoted to schema 2 — and the next run then
    # skips that guard entirely and overwrites the project-owned file the first run refused to touch.
    # A partial update leaves the receipt describing what it did, at the commit it came from.
    if r.problems:
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
        (target / ".governance" / "install.sums").write_text(
            "".join(f"{f['sha256']}  {f['path']}\n" for f in receipt["files"] if "sha256" in f),
            encoding="utf-8", newline="\n")
        print(f"govkit update — wrote {len(changed)}, moved {len(renamed) // 2}, "
              f"deleted {len(deleted)}, withheld {withheld}, "
              f"{conflicts} conflict(s). The receipt is NOT re-stamped: this run had findings, and a "
              f"stamp would tell the next run that guards which fired here have already been passed")
        return r.emit()

    receipt["schema"] = RECEIPT_SCHEMA
    receipt["gov_commit"] = to_commit
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
    (target / ".governance" / "install.sums").write_text(
        "".join(f"{f['sha256']}  {f['path']}\n" for f in receipt["files"] if "sha256" in f),
        encoding="utf-8", newline="\n")
    print(f"govkit update — wrote {len(changed)}, moved {len(renamed) // 2}, "
          f"deleted {len(deleted)}, withheld {withheld}, "
          f"{conflicts} conflict(s); receipt re-stamped at {to_commit[:8]}")
    return r.emit()



# ----------------------------------------------------------------- adopt (DEPL-dCarriedReceipt-13)
# THE BOOTSTRAP. Every other verb here moves an install forward; this one writes the receipt an
# already-installed tree never had, by MEASURING that tree against gov's own history. It is the first
# documented path onto the engine for a repository somebody vendored kits into by hand, and the
# audit that motivated it measured zero auto-syncable rows in either live target for exactly one
# reason: `cmd_update` refuses without `.governance/install.json`, and neither target has one.
#
# `evidence` IS THIS UNIT'S FIELD, and it exists because a base an ENGINE INFERRED must never be
# indistinguishable from one a write produced. `apply` stamps `"apply"`; this verb stamps
# `"vintage-match"` for a row whose bytes it proved against a gov commit, `"pinned"` for one an
# operator asserted, and `"unattributed"` for one that matched no vintage at all. The fifth state is
# ABSENCE, on S11's two synthesized classes, and it is NOT a synonym for `"unattributed"` — S7's skip
# keys on the string, so widening it to field-absence would swallow every unlanded row and silently
# delete four dispositions. That reading was in an earlier rev of the spec and was destructive.
EVIDENCE_STATES = ("apply", "vintage-match", "pinned", "unattributed")


def carry_matches(rung: str, ours: bytes, base: bytes, needles: dict[str, str]) -> bool:
    """Does ONE named rung explain the difference between the target's bytes and gov's?

    `derive_carry_rung` asks the ladder question — WHICH rung, first proof wins — over ONE base.
    `adopt` asks the transposed one: hold the rung, walk the bases (S4). Both are the same three
    proofs and they are spelled ONCE, here, with the ladder calling this rather than repeating it.

    `eol` normalises BOTH sides and that is why this is not `derive_carried_by_rung`: that function
    is the WRITE-path transform, applied to gov's bytes alone so the rung cancels in a three-way
    diff. Normalising one side is the right answer there and the wrong answer to this question — a
    CRLF target compared against an LF-normalised gov blob still differs on every line.
    """
    if rung == "verbatim":
        return ours == base
    if rung == "eol":
        return derive_lf(ours) == derive_lf(base)
    return ours == derive_carried(base, needles)


def derive_attribution(root: pathlib.Path, src: str, ours: bytes, to_commit: str,
                       needles: dict[str, str]) -> tuple[str, str, str] | None:
    """S3 + S4. The vintage the target's bytes came from, as `(commit, gov_oid, rung)`, or `None`.

    RUNG-MAJOR, NOT RECENCY-MAJOR, and it is load-bearing rather than a preference. Every commit is
    tested at `verbatim` first, then `eol`, then `relocate`, and the NEWEST commit inside the FIRST
    rung that matches wins. Preferring a newer commit at a lossier rung selects a base whose delta
    was never applied to this target, and the three-way then re-applies work the adopter already
    has. The inverse is in the spec's rejected alternatives for that reason.

    `git log <to-rev> -- <src>` and NEVER `--all`. Measured at 9ddcc5c9: gov carries eight commits
    reachable from a ref and not from `HEAD`, several on in-flight branches, and a walk that reaches
    them attributes an adopter to a vintage nobody ever shipped.

    ONE BLOB READ PER COMMIT, cached across all three rungs. The walk is this verb's dominant cost on
    a real adopter — 143 planned writes on the target section 5 names — and re-reading the same blob
    three times would triple it for nothing.
    """
    out = subprocess.run(
        ["git", "-C", str(root), "log", "--format=%H", to_commit, "--", src],
        capture_output=True, text=True, check=False)
    commits = [c for c in out.stdout.split() if c]
    cache: dict[str, bytes | None] = {}

    def base_at(c: str) -> bytes | None:
        if c not in cache:
            cache[c] = blob_at(root, c, src)
        return cache[c]

    for rung in CARRY_RUNGS:
        for c in commits:                      # `git log` emits newest-first, so this IS recency
            base = base_at(c)
            if base is None:
                continue
            if carry_matches(rung, ours, base, needles):
                return c, blob_oid(base), rung
    return None


def demand_adopt_index_clean(target: pathlib.Path) -> None:
    """S8's third refusal, and section 8 F1 decides its WIDTH: the index, never the worktree.

    `adopt` reads every identity it records out of the index, so an index that disagrees with HEAD
    means the receipt would record blobs no commit in the target carries. An UNSTAGED edit is a
    different thing entirely — the operator's own work in a repository gov does not own — and
    refusing over one is the shape adopters learn to route around. `-12` owns the worktree
    preconditions, on the verbs that write bytes into the target; this verb writes one file under
    `.governance/` and nothing else.
    """
    has_head = subprocess.run(["git", "-C", str(target), "rev-parse", "--verify", "-q", "HEAD"],
                              capture_output=True).returncode == 0
    if not has_head:
        return          # index-versus-HEAD is unanswerable before the first commit
    out = subprocess.run(["git", "-C", str(target), "diff", "--cached", "--name-only", "-z", "HEAD"],
                         capture_output=True, text=True, check=False)
    staged = sorted({n for n in out.stdout.split("\0") if n})
    if staged:
        raise Refusal(
            f"{len(staged)} path(s) in the target's index differ from HEAD: " + ", ".join(staged)
            + " — `adopt` records each row's identity from the INDEX, so a staged-but-uncommitted "
            "tree would be written into the receipt as the vintage this target holds, and no commit "
            "here carries those blobs. Commit or reset them, then re-run. An UNSTAGED edit does not "
            "block: this verb writes one file under `.governance/` and never touches your worktree"
        )


def cmd_adopt(root: pathlib.Path, target: pathlib.Path, to_rev: str,
              pins: dict[str, str], re_adopt: bool, write: bool) -> int:
    """Write the receipt an already-installed tree never had, by measuring it against gov history.

    READ-ONLY WITHOUT `--write`, matching `update` and for the same reason: the muscle-memory
    invocation must not be the one that writes.
    """
    r = Report()
    reg = load_toml(root / "tools" / "govkit" / "registry.toml")
    descs = read_descriptors(root, reg, r)
    if r.problems:
        return r.emit()

    # ---- S8, the three refusals. Target IDENTITY first, before anything is read out of the tree:
    # ---- a refusal about WHICH repository this is must not queue behind one about its contents.
    if pathlib.Path(root).resolve() == target.resolve():
        raise Refusal("--target resolves to the gov checkout itself; adopting this repo into itself "
                      "is a stated non-goal and would be indistinguishable from a self-overwrite")
    receipt_path = target / ".governance" / "install.json"
    if receipt_path.is_file() and not re_adopt:
        raise Refusal(
            f"the target already carries a receipt at {receipt_path.as_posix()} — `adopt` writes one "
            f"where there was none. Re-run with `--re-adopt` to re-measure from scratch. That flag "
            f"is deliberately a second explicit invocation rather than a default: a receipt is a "
            f"decision artefact, and `intake` refuses to silently rewrite the descriptor for the "
            f"same reason"
        )
    demand_adopt_index_clean(target)

    deploy = load_deploy(target)
    selection = resolve_selection(reg, descs, "kits" if deploy.get("kits") else "default",
                                  list(deploy.get("kits") or []))
    out = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", to_rev + "^{commit}"],
                         capture_output=True, text=True, check=False)
    if out.returncode != 0:
        raise Refusal(f"--to '{to_rev}' does not resolve in this gov checkout")
    commit = out.stdout.strip()

    print(f"govkit adopt — target {target.as_posix()} · selection: {', '.join(selection)}")
    print(f"govkit adopt — measuring against gov {commit[:8]} "
          f"({'--write' if write else 'READ-ONLY: pass --write to record the receipt'})")

    # ---- THE DESTINATION SET (S2). BOTH of `resolve_entry`'s channels, because a `forked` rule's
    # ---- rows arrive in the second one and a set built from `writes` alone leaves the receipt
    # ---- silent about exactly the files that most need saying. `merged` entries are skipped on
    # ---- this channel and re-synthesized in `apply`'s own shape by S11, exactly as `apply` skips
    # ---- them in its own unlanded loop; the stripped unlanded shape is the one row `cmd_check`
    # ---- cannot read.
    plan: list[dict] = []                      # one entry per planned destination, in landing order
    merged_rules: list[tuple[str, str, dict, dict]] = []      # (eid, version, descriptor, rule)
    for eid in selection:
        d, _p = descs[eid]
        ctx = target_context(target, deploy, eid, d)
        vers = entry_version(root, d)
        res = resolve_entry(root, d, ctx)
        for dest, w in sorted(res["writes"].items()):
            if w["missing"] or w.get("scope") == "machine":
                continue
            rule = d.get("files", [])[w["rule"]]
            if rule.get("scope") == "machine" or rule.get("link"):
                continue
            plan.append({"dest": dest, "role": w["role"], "kit": eid, "version": vers,
                         "src": w["src"], "landable": True, "rule": rule})
        for u in res["unlanded"]:
            if u["role"] == "merged" or u.get("missing"):
                continue                       # S11 writes the real merged row below
            _rules = d.get("files", [])
            _i = u.get("rule")
            plan.append({"dest": u["dest"], "role": u["role"], "kit": eid, "version": vers,
                         "src": u["src"], "landable": False,
                         "rule": _rules[_i] if isinstance(_i, int) and 0 <= _i < len(_rules) else {}})
        for rule in d.get("files", []):
            if rule.get("role", "engine") == "merged" and rule.get("marker_style") != "json-pointer":
                merged_rules.append((eid, vers, d, rule))

    # ---- S4a. THE NEEDLE MAP, at bootstrap. `-9` F3's derivation reads a RECEIPT, and there is no
    # ---- receipt yet — so the same function is fed this run's planned `(src, dest)` pairs, which
    # ---- are the only record of where a file would land. Without it the `relocate` rung has no
    # ---- map, the ladder collapses to `verbatim`/`eol`, and every relocated row bootstraps
    # ---- `unattributed` and is skipped by S7 forever.
    needles, dpairs, dropped = derive_carry_map([(p["src"], p["dest"]) for p in plan if p["src"]])
    for gd, ds in dropped:
        print(f"govkit adopt — dropped ambiguous gov directory '{gd}': it names "
              f"{len(ds)} target directories ({', '.join(ds)}), so it is no single needle")
    print(f"govkit adopt — needle map: {len(dpairs)} directory pair(s), {len(needles)} needle(s)")

    # ---- THE INDEX, ONE batched read over every planned destination. A destination the target does
    # ---- not track has no identity to record and gets no row at all.
    idx, _present = index_read(target, [p["dest"] for p in plan]) if plan else ({}, set())

    rows: list[dict] = []
    tally: dict[str, int] = {}
    for p in plan:
        dest = p["dest"]
        if dest not in idx:
            tally["not-installed"] = tally.get("not-installed", 0) + 1
            print(f"  {'not-installed':<15} [{p['role']:<13}] {dest}")
            continue
        ours = index_blob(target, idx[dest][1])
        # THE ROW's `role` IS THE RULE'S, NEVER THE WALK'S (S5). A fork has a common ancestor BY
        # CONSTRUCTION, so the walk attributes it at its pre-fork vintage and matches `verbatim`
        # there; taking the role from that outcome adopts it as `engine` with the two identities
        # AGREEING, which opens the raw-write arm and lets the first `update --write` land gov's
        # fork over the target's working program. That is the measured landmine `-10` exists for,
        # re-manufactured by the bootstrap written to record it.
        row: dict = {"path": dest, "role": p["role"], "kit": p["kit"], "version": p["version"],
                     "source": p["src"]}
        if not p["landable"]:
            row["written"] = False
            why = UNLANDED_REASON.get(p["role"])
            if why is not None:
                row["why"] = why
        if p["role"] == "forked":
            for _k in FORK_RULE_KEYS:
                if p["rule"].get(_k):
                    row[_k] = p["rule"][_k]
        # F5: `sha256` hashes the TARGET's own bytes at the moment the receipt is written, not gov's
        # at `commit`. The two coincide only while every row is `verbatim`, and this is the first
        # verb whose whole job is the rows where they do not. It is what `install.sums` lists, so
        # `sha256sum -c` stays honest on a tree this verb did not touch.
        if ours is not None:
            row["sha256"] = hashlib.sha256(ours).hexdigest()
            row["oid"] = idx[dest][1]

        # THE RUNG IS A LOCAL, and never read back off the row it was just written to. `-9` S2 says
        # no branch anywhere reads a stored `carry`, and an arm over this file's SOURCE enforces it
        # by NAME: reading `row["carry"]` five lines after writing it is indistinguishable, to that
        # arm and to a reader, from trusting one an older run left behind.
        rung: str | None = None
        pin = pins.get(dest)
        if pin is not None:
            pc = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify",
                                 pin + "^{commit}"], capture_output=True, text=True, check=False)
            if pc.returncode != 0:
                raise Refusal(f"--pin {dest}={pin} does not resolve in this gov checkout")
            pinned = pc.stdout.strip()
            was = blob_at(root, pinned, p["src"]) if p["src"] else None
            if was is None:
                raise Refusal(f"--pin {dest}={pin}: gov holds no blob for '{p['src']}' at "
                              f"{pinned[:12]}, so the assertion names a base that does not exist")
            row["commit"] = pinned
            row["gov_oid"] = blob_oid(was)
            # RECOMPUTED, never asserted. `--pin` fixes the BASE; the rung stays a proof, so an
            # operator who pins the wrong vintage gets a row with no rung rather than a claim.
            row["evidence"] = "pinned"
            rung = derive_carry_rung(was, needles, lambda: ours) if ours is not None else None
            if rung:
                row["carry"] = rung
        else:
            hit = derive_attribution(root, p["src"], ours, commit, needles) if (
                p["src"] and ours is not None) else None
            if hit is None:
                # S7. Its OWN state, and NOT `forked`: that role is a claim the DESCRIPTOR makes,
                # and the walk does not get to make it on the descriptor's behalf. No `commit`, no
                # `gov_oid`, `role` untouched.
                row["evidence"] = "unattributed"
            else:
                row["commit"], row["gov_oid"], rung = hit
                row["carry"] = rung
                row["evidence"] = "vintage-match"

        ev = row["evidence"]
        key = "forked" if p["role"] == "forked" else (rung or ev)
        tally[key] = tally.get(key, 0) + 1
        print(f"  {key:<15} [{p['role']:<13}] {dest}"
              + (f" <- {row['commit'][:8]}" if row.get("commit") else ""))
        rows.append(row)

    # ---- S11. THE TWO CLASSES `resolve_entry` DOES NOT PRODUCE, in `apply`'s own shapes rather
    # ---- than in a second one. Without them `-2`'s `pins` arm never dispatches and `cmd_check`'s
    # ---- merged loop raises `KeyError` on `row['block_id']`. NEITHER carries `evidence`, `gov_oid`
    # ---- or `oid`: both are measured from the target's own bytes rather than attributed to a gov
    # ---- vintage, and `merged`'s exemption from `-7` S9's integrity preamble is by ROLE, which
    # ---- this row inherits by being the same row `apply` writes.
    pins_declared = lf_pins(descs, selection, lambda e, dd: target_context(target, deploy, e, dd))
    if pins_declared:
        _om, _cm, _text = lf_pin_block(pins_declared)
        _ga = target / ".gitattributes"
        _cur = _ga.read_text(encoding="utf-8", errors="replace") if _ga.is_file() else ""
        _span = find_block(_cur, _om, _cm)
        _held = "\n".join(_cur.split("\n")[_span[0]:_span[1] + 1]) if _span else None
        rows.append({"path": ".gitattributes", "role": "attributes", "kit": "(govkit)",
                     "version": "(synthesized)", "block_id": GA_BLOCK_ID,
                     "marker_style": "hash-comment", "mode": "append", "normalized": "lf",
                     # The block the TARGET holds where it holds one, so `update`'s pins arm
                     # compares against what is really there; gov's recomputed block otherwise,
                     # which is the honest reading of a target that never had one.
                     "block_sha256": hashlib.sha256(
                         (_held if _held is not None else _text).encode("utf-8")).hexdigest(),
                     "patterns": [p for p, _c, _w in pins_declared], "written": False})
        tally["attributes"] = tally.get("attributes", 0) + 1

    for eid, vers, d, rule in merged_rules:
        ctx = target_context(target, deploy, eid, d)
        om, cm = marker_pair(rule.get("marker_style"), rule["block_id"])
        for src in rule_sources(d, rule):
            if blob_at(root, commit, src) is None:
                continue
            for dest_t in (rule.get("to") if isinstance(rule.get("to"), list) else [rule.get("to")]):
                dest, miss = resolve_tokens(dest_t, ctx)
                if miss:
                    continue
                dp = target / dest
                if not dp.is_file():
                    continue
                text = dp.read_text(encoding="utf-8", errors="replace")
                held = find_block(text, om, cm)
                if held is None:
                    continue
                block = "\n".join(text.split("\n")[held[0]:held[1] + 1])
                rows.append({"path": dest, "role": "merged", "kit": eid, "version": vers,
                             "block_id": rule["block_id"],
                             "marker_style": rule.get("marker_style"),
                             "block_sha256": hashlib.sha256(
                                 block.replace(CR, "").encode("utf-8")).hexdigest(),
                             "normalized": "lf", "mode": "append", "source": src,
                             "commit": commit, "written": False})
                tally["merged"] = tally.get("merged", 0) + 1

    print("govkit adopt — " + (", ".join(f"{k} {v}" for k, v in sorted(tally.items())) or "0 rows"))
    if not write:
        print(f"govkit adopt — READ-ONLY: {len(rows)} row(s) would be recorded. "
              f"Nothing was written; re-run with --write")
        return r.emit()

    # ---- S10. THE ENVELOPE, not just the rows. Three units read fields OUTSIDE `files`, and
    # ---- omitting them degrades each of them SILENTLY: `-12` S7's vintage guard fails open by its
    # ---- own words with no `gov_commit`, `-11`'s rename diff has no base and the unit is inert,
    # ---- and `-2`'s pins arm reads an empty `kits` so every registry entry prints as "available
    # ---- (not installed)". `orders`, `baseline`, `after`, `hook_block` and `gate_runner` are NOT
    # ---- written: each records what an install DID, and this verb installs nothing.
    (target / ".governance").mkdir(exist_ok=True)
    receipt_path.write_text(json.dumps(
        {"schema": RECEIPT_SCHEMA, "gov_source": str(root), "gov_commit": commit,
         "prefix": (deploy.get("prefix") or "tools"), "kits": selection, "files": rows},
        indent=2) + "\n", encoding="utf-8", newline="\n")
    (target / ".governance" / "install.sums").write_text(
        "".join(f"{w['sha256']}  {w['path']}\n" for w in rows if "sha256" in w),
        encoding="utf-8", newline="\n")
    print(f"govkit adopt — receipt written: {len(rows)} row(s), {len(selection)} kit(s), "
          f"schema {RECEIPT_SCHEMA}, gov_commit {commit[:8]}")
    return r.emit()


# ---------------------------------------------------------------------------------------- intake
def needed_answers(descs: dict[str, tuple[dict, str]], selection: list[str]) -> list[str]:
    """Every token a selected kit's destinations and probes need that is not derived.

    Derived from the descriptors, never listed: a hand-kept question list is how `intake` stops
    asking for something a kit started needing.
    """
    derived = {"prefix", "kit", "kit_id", "relpath", "memory_root"}
    want: set[str] = set()
    for eid in selection:
        d, _p = descs[eid]
        blobs: list[str] = []
        for rule in d.get("files", []):
            to = rule.get("to")
            blobs += (to if isinstance(to, list) else [to]) if to else []
        for h in d.get("hole", []):
            blobs += (h.get("discharge") or {}).get("command") or []
        # Every place a token can appear, not just the two obvious ones. A gate leg's argv carries
        # `{gate_file}` for one shipped kit, and scanning only destinations and hole probes meant
        # `intake` never asked for it — so `apply` would land, and the leg it wired would name a
        # path nobody supplied. Found by running intake over the default set.
        for leg in d.get("gate_leg", []):
            blobs += leg.get("argv") or []
            blobs += leg.get("guard") or []
        blobs += (d.get("adopt") or {}).get("argv") or []
        blobs += (d.get("check") or {}).get("argv") or []
        cfg = d.get("config") or {}
        if cfg.get("seeded_from"):
            blobs.append(cfg["seeded_from"])
        for b in blobs:
            want.update(k for k in TOKEN_RX.findall(b or "") if k not in derived)
    return sorted(want)


def cmd_intake(root: pathlib.Path, target: pathlib.Path, mode: str, kits: list[str],
               answers: dict[str, str]) -> int:
    """Write the target descriptor ONCE, from answers supplied non-interactively.

    AC12's shape: given a prepared answer stream, `intake` writes a `deploy.toml` that
    `apply` accepts with no further prompting. It refuses to invent an answer, and it refuses to
    overwrite a descriptor that already exists — that file is the standing authorization for an
    unattended re-run, and silently rewriting it would replace a decision the operator made.
    """
    r = Report()
    reg = load_toml(root / "tools" / "govkit" / "registry.toml")
    descs = read_descriptors(root, reg, r)
    if r.problems:
        return r.emit()
    selection = resolve_selection(reg, descs, mode, kits)
    out = target / ".governance" / "deploy.toml"
    if out.is_file():
        raise Refusal(
            f"{out.as_posix()} already exists. It is the standing authorization for an unattended "
            f"re-run, so this verb will not silently rewrite a decision the operator already made; "
            f"edit it, or remove it deliberately"
        )
    need = needed_answers(descs, selection)
    missing = [k for k in need if k not in answers]
    if missing:
        raise Refusal(
            "the selected kits need answer(s) " + ", ".join(missing) +
            " and none was supplied. Refusing to invent one: an answer this tool guesses is one the "
            "operator never made and cannot audit. Supply them as --answer key=value"
        )
    # DEPL-dCarriedReceipt-3 S1: resolved ONCE, and every spelling below reads this. `or` rather
    # than a presence test, so `--answer prefix=` with an empty value takes the default instead of
    # emitting an empty prefix that would resolve every destination to a bare relative path.
    pfx = answers.get("prefix") or "tools"
    body = ['# deploy.toml — written once by `govkit intake`. Committed, it is the standing',
            '# authorization for an unattended re-run: it carries every owner decision, so a later',
            '# `apply` reads answers rather than asking for them again.',
            '',
            f'gov_source = "{root.as_posix()}"',
            f'gov_commit = "{git(root, "rev-parse", "HEAD").strip()}"',
            f'prefix = "{pfx}"',
            'kits = [' + ", ".join(f'"{k}"' for k in selection) + ']',
            '',
            '[answers]']
    body += [f'{k} = "{answers[k]}"' for k in need]
    # the run-gates promotion spec's S9: emit the target's [gate_runner] declaration from the selected
    # entry's [gate_runner_seed]. A declaration written at CONFIGURE time cannot reach the same run's
    # leg-emission step, so leaving it to the operator means the first `apply` after adopting a
    # runner silently takes the "ORDERED, not emitted" branch and exits 0 — the silent-green
    # direction this deployer refuses by name everywhere else.
    #
    # PATH TOKENS ONLY. `{prefix}` and `{kit}` are the deployer's to resolve; the runner's own
    # `{name}` placeholder passes through VERBATIM, because that substitution belongs to the runner
    # at report time and resolving it here would write a declaration matching one leg's line.
    seeds = [(k, descs[k][0].get("gate_runner_seed")) for k in selection
             if isinstance(descs.get(k), tuple) and descs[k][0].get("gate_runner_seed")]
    if len(seeds) > 1:
        raise Refusal(
            "the selection carries more than one [gate_runner_seed] (" +
            ", ".join(k for k, _ in seeds) + "). A target has ONE [gate_runner]; emitting two would "
            "silently keep whichever the writer wrote last. Select one runner kit"
        )
    if seeds:
        eid, seed = seeds[0]
        gctx = {"prefix": pfx, "kit_id": eid, "kit": f"{pfx}/{eid}"}

        def resolve_seed_value(v):
            if isinstance(v, str):
                out, missing = resolve_tokens(v, gctx)
                # `{name}` is the RUNNER's, not ours: it is expected to survive.
                unresolved = [m for m in missing if m != "name"]
                if unresolved:
                    raise Refusal(
                        f"[gate_runner_seed] in entry '{eid}' leaves {', '.join(unresolved)} "
                        f"unresolved in {v!r}; a path with a brace still in it is not a path"
                    )
                return out
            if isinstance(v, list):
                return [resolve_seed_value(x) for x in v]
            return v

        body += ['', '# [gate_runner] — emitted from the ' + eid + " kit's [gate_runner_seed] (S9).",
                 "# The runner's own {name} placeholder is deliberately intact: it is substituted by",
                 '# the runner at report time, not by this deployer.',
                 '[gate_runner]']
        # A LIST is emitted as a TOML ARRAY; only a scalar is quoted. Quoting every value turned the
        # seed's observation templates into strings, and `read_gate_verdicts` iterates them — so it
        # walked each one character by character and could never report a red leg. The emitter and
        # the reader had never met, because every arm on the bar hand-writes the array form.
        # DERIVED from OBSERVED_KEYS rather than re-typed. The hand-written list here dropped
        # `observed_reused` from every emitted deploy.toml, so a template the kit declared never
        # reached a single target — the emitter and the reader had never met.
        for k in ("kind", "grammar", "file", "dedupe_key", "run_all_env") + OBSERVED_KEYS + ("command",):
            if k not in seed:
                continue
            v = resolve_seed_value(seed[k])
            if isinstance(v, list):
                body.append(f'{k} = [' + ", ".join(f'"{x}"' for x in v) + ']')
            else:
                body.append(f'{k} = "{v}"')

    body += ['', '[policy]',
             '# on_baseline_red: proceed | refuse — a target leg already red BEFORE the install',
             'on_baseline_red = "proceed"',
             '# on_hook_block: report | refuse — apply never commits, so no pre-commit hook fires',
             '# during an install; this exists so a target whose hooks WILL refuse the operator\'s',
             '# own landing commit is told before they discover it by hand.',
             'on_hook_block = "report"', '']
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(body), encoding="utf-8", newline="\n")
    print(f"govkit intake — wrote {out.as_posix()} for {len(selection)} kit(s); "
          f"{len(need)} answer(s) recorded; "
          f'prefix "{pfx}" ({"from --answer" if answers.get("prefix") else "default"})')
    return r.emit()


def read_descriptors(root: pathlib.Path, reg: dict, r: Report) -> dict[str, tuple[dict, str]]:
    """Shared by every verb: the registry's entries, parsed. A missing one is a refusal, not a skip."""
    descs: dict[str, tuple[dict, str]] = {}
    for e in reg.get("entry", []):
        eid, dpath = e.get("id"), e.get("descriptor")
        if not eid or not dpath:
            r.fail(f"a registry entry is missing an id or a descriptor path: {e!r}")
            continue
        p = root / dpath
        if not p.is_file():
            r.fail(f"entry '{eid}' names a descriptor that does not exist: {dpath}")
            continue
        descs[eid] = (load_toml(p), dpath)
    return descs


# ------------------------------------------------------------------------------------------- main
USAGE = """usage:
  govkit.py selfcheck
  govkit.py plan  --target <path> [--kits a,b | --all] [--coverage] [--emit-declines]
  govkit.py check --target <path>
  govkit.py apply --target <path> [--kits a,b | --all] [--resume]
  govkit.py update --target <path> [--to <rev>] [--write] [--write-withdrawals]
  govkit.py adopt  --target <path> [--to <rev>] [--pin <path>=<rev> ...] [--re-adopt] [--write]
  govkit.py intake --target <path> [--kits a,b | --all] [--answer key=value ...]

`plan`, `check`, `update` and `adopt` are READ-ONLY and none writes a byte; `update --write` performs
what `update` printed. `adopt` is the BOOTSTRAP: it writes the receipt an already-installed tree
never had, by measuring that tree against gov's own history, and `--write` is what records it. It
puts no byte into the target's working tree ever — one file under `.governance/` and nothing else —
and it refuses over an existing receipt unless `--re-adopt` says to re-measure from scratch. `--write-withdrawals` is the ONLY way `update` deletes anything: without it a file
gov has stopped shipping is REPORTED and an order is written under `.governance/outbox/`, and the
adopter's copy stays exactly where it is. It defaults off and it is a scope flag rather than a
`--force` — it enables a narrower class of action and overrides no refusal. A file gov RENAMED is
not a withdrawal at all: `update --write` moves the target's copy to the new destination its own
descriptor resolves, carrying any local edit through a three-way merge. The default is read-only because that verb's failure mode is silent data loss in a
repository the operator owns and gov does not, and the muscle-memory invocation must not be the
destructive one. `intake` writes the target descriptor
ONCE and refuses to overwrite one that exists — a subcommand that parses and does
nothing looks exactly like one that works, from the outside, and this unit exists because that class
of silence ships broken installs.
"""


def parse_args(argv: list[str]) -> tuple:
    verb = argv[0]
    target: pathlib.Path | None = None
    mode, kits = "default", []
    resume = False
    write = False
    write_withdrawals = False
    to_rev = "HEAD"
    answers: dict[str, str] = {}
    # DEPL-dCarriedReceipt-13 S1. Both widen this function, which used to return a fixed 8-tuple.
    # `--pin` is REPEATABLE and keyed by destination: one assertion per row, never a mode.
    pins: dict[str, str] = {}
    re_adopt = False
    # DEPL-dCarriedReceipt-4 S6. `--emit-declines` implies `--coverage` in `cmd_plan`, so the two
    # are parsed independently and joined there rather than here: a parser that silently switched
    # another flag on would make `parse_args`'s return the second place the rule is written.
    coverage = False
    emit_declines = False
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--target" and i + 1 < len(argv):
            target = pathlib.Path(argv[i + 1]).resolve()
            i += 2
        elif a == "--answer" and i + 1 < len(argv):
            k, _, v = argv[i + 1].partition("=")
            if not _:
                raise Refusal(f"--answer needs key=value, got: {argv[i + 1]}")
            answers[k.strip()] = v
            i += 2
        elif a == "--resume":
            resume = True
            i += 1
        elif a == "--write":
            write = True
            i += 1
        elif a == "--write-withdrawals":
            # DEPL-dCarriedReceipt-11 S9. Its OWN flag rather than a value on `--write`, and NOT a
            # `deploy.toml` field: a descriptor field is a STANDING authorization, and the whole
            # reason this flag exists is that a deletion used to happen without anyone deciding it
            # once, let alone standing (§8 F1). It does nothing without `--write`, because the
            # deletion it scopes lives in the write loop.
            write_withdrawals = True
            i += 1
        elif a == "--pin" and i + 1 < len(argv):
            # DEPL-dCarriedReceipt-13 S6. `<path>=<rev>`, and the SAME key=value refusal `--answer`
            # already makes: a `--pin` with no `=` is an operator naming a path and no vintage, and
            # accepting it would silently pin nothing.
            k, _eq, v = argv[i + 1].partition("=")
            if not _eq:
                raise Refusal(f"--pin needs <path>=<rev>, got: {argv[i + 1]}")
            pins[k.strip()] = v.strip()
            i += 2
        elif a == "--re-adopt":
            re_adopt = True
            i += 1
        elif a == "--coverage":
            coverage = True
            i += 1
        elif a == "--emit-declines":
            emit_declines = True
            i += 1
        elif a == "--to" and i + 1 < len(argv):
            to_rev = argv[i + 1]
            i += 2
        elif a == "--all":
            mode = "all"
            i += 1
        elif a == "--kits" and i + 1 < len(argv):
            mode, kits = "kits", [k.strip() for k in argv[i + 1].split(",") if k.strip()]
            i += 2
        else:
            raise Refusal(f"unknown or incomplete argument: {a}")
    return (verb, target, mode, kits, resume, answers, write, to_rev, write_withdrawals,
            pins, re_adopt, coverage, emit_declines)


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        sys.stderr.write(USAGE)
        return 0 if argv else 2
    try:
        (verb, target, mode, kits, RESUME, ANSWERS, WRITE, TO_REV, WRITE_WD,
         PINS, RE_ADOPT, COVERAGE, EMIT_DECLINES) = parse_args(argv)
        root = repo_root()
        if verb == "selfcheck":
            # `--write` is the ONLY argument, and it regenerates the subject pin. Kept narrow on
            # purpose: `selfcheck` is the verb a gate leg runs, and a verb that writes by default
            # would let the bar repair the very record it is supposed to be grading.
            if len(argv) > 2 or (len(argv) == 2 and argv[1] != "--write"):
                raise Refusal("selfcheck takes no arguments except --write")
            return selfcheck(root, write=(len(argv) == 2))
        if verb in ("plan", "check", "apply", "intake", "update", "adopt"):
            if target is None:
                raise Refusal(
                    f"{verb} needs an explicit --target. Refusing to default it to the process cwd: "
                    f"that is how a tool writes into, or reports on, a repository nobody named"
                )
            if not (target / ".git").exists():
                raise Refusal(f"--target {target.as_posix()} is not a git repository")
            if verb == "plan":
                return cmd_plan(root, target, mode, kits, coverage=COVERAGE,
                                emit_declines=EMIT_DECLINES)
            if verb == "check":
                return cmd_check(root, target)
            if verb == "intake":
                return cmd_intake(root, target, mode, kits, ANSWERS)
            if verb == "update":
                return cmd_update(root, target, TO_REV, write=WRITE,
                                  write_withdrawals=WRITE_WD)
            if verb == "adopt":
                return cmd_adopt(root, target, TO_REV, PINS, RE_ADOPT, write=WRITE)
            return cmd_apply(root, target, mode, kits, resume=RESUME)
        sys.stderr.write(f"govkit: unknown subcommand '{verb}'\n\n{USAGE}")
        return 2
    except Refusal as e:
        sys.stderr.write(f"govkit: {e}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
