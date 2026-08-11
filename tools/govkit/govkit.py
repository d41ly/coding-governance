#!/usr/bin/env python3
"""govkit — the mechanical deployer. Rollout commit 1: the registry and `selfcheck`.

Contract: the deployer unit's spec under memory/builds/aSealedCaravan/spec/

WHAT THIS FILE DOES TODAY, AND WHAT IT DOES NOT. Rollout commit 1 ships `registry.toml`, a
descriptor per entry, and `selfcheck`. `plan`, `check`, `apply`, `apply --resume` and `intake` are
commits 2 through 4 and are ABSENT rather than stubbed: a subcommand that parses and does nothing is
indistinguishable, from the outside, from one that works, and this unit exists because that class of
silence ships broken installs.

`selfcheck` is the ratchet. Its most load-bearing arm is the SURFACE predicate (spec S12): every
tracked path in the declared surface is an entry, a member of exactly one entry's file rules, or an
exemption with a reason. The spec states no population count anywhere on purpose — it stated two
across its life and both were true when measured and false when read — so this is where a count is
allowed to exist, derived, once, at the moment it is checked.

EVERY REFUSAL PRINTS ITS OWN MESSAGE AND IS COUNTED. Exit 0 clean, 1 findings, 2 misconfigured.
"""

from __future__ import annotations

import os
import pathlib
import re
import subprocess
import sys

KIT_GOVKIT_VERSION = "1.0"  # gov:kit govkit@1.0 — kit identity; set HERE, never from a conf

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


def rule_destinations(desc: dict, rule: dict) -> list[str]:
    """The destination(s) a rule writes, with `{relpath}` resolved per source.

    `to` is a LIST because one source can reach two places — the hook that must exist both as a kit
    copy and as a wired copy, whose parity arm fails outright when the wired one is absent. An
    unresolved `{relpath}` is a per-source template, not a destination, so it is expanded here
    rather than compared as a literal.
    """
    to = rule.get("to")
    if not to:
        return []
    dests = to if isinstance(to, list) else [to]
    out = []
    for d in dests:
        if "{relpath}" in d:
            for s in rule_sources(desc, rule):
                out.append(d.replace("{relpath}", pathlib.PurePosixPath(s).name))
        else:
            out.append(d)
    return out


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
def selfcheck(root: pathlib.Path) -> int:
    r = Report()
    reg_path = root / "tools" / "govkit" / "registry.toml"
    reg = load_toml(reg_path)

    entries = reg.get("entry", [])
    exempts = reg.get("exempt", [])
    if not entries:
        r.fail("registry.toml declares no entries — an empty population makes every assertion "
               "keyed on it vacuously true, which is the failure this file exists to prevent")
        return r.emit()

    # ---- 1: every entry names a descriptor, and the descriptor exists and parses.
    descs: dict[str, tuple[dict, str]] = {}
    for e in entries:
        eid, dpath = e.get("id"), e.get("descriptor")
        if not eid or not dpath:
            r.fail(f"a registry entry is missing an id or a descriptor path: {e!r}")
            continue
        p = root / dpath
        if not p.is_file():
            r.fail(f"entry '{eid}' names a descriptor that does not exist: {dpath}")
            continue
        try:
            descs[eid] = (load_toml(p), dpath)
        except Refusal as exc:
            r.fail(str(exc))

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


# ------------------------------------------------------------------------------------------- main
USAGE = """usage: govkit.py selfcheck

Rollout commit 1 ships `selfcheck` only. `plan`, `check`, `apply`, `apply --resume` and `intake`
are later commits and are absent rather than stubbed — a subcommand that parses and does nothing
looks exactly like one that works, from the outside.
"""


def main(argv: list[str]) -> int:
    if len(argv) != 1 or argv[0] in ("-h", "--help"):
        sys.stderr.write(USAGE)
        return 2 if argv[:1] not in (["-h"], ["--help"]) else 0
    if argv[0] != "selfcheck":
        sys.stderr.write(f"govkit: unknown subcommand '{argv[0]}'\n\n{USAGE}")
        return 2
    try:
        return selfcheck(repo_root())
    except Refusal as e:
        sys.stderr.write(f"govkit: {e}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
