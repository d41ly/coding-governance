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


# ------------------------------------------------------------------------------- selection + tokens
# The DEFAULT set, spelled once. `--all` is DERIVED from the registry rather than listed, because a
# hand-kept list is how a registry grows an entry no selection ever reaches — which is exactly the
# state the unattended kit was in when this unit's grounding found it.
DEFAULT_KITS = ("playbook", "kickoff-manifest", "memory-tree", "codebase-map", "memory-recall")


def all_kits(descs: dict[str, tuple[dict, str]]) -> list[str]:
    """Every non-conditional entry. Derived; never a literal list."""
    return sorted(e for e, (d, _) in descs.items() if d.get("selectable") != "conditional")


def resolve_selection(descs: dict[str, tuple[dict, str]], mode: str, kits: list[str]) -> list[str]:
    if mode == "all":
        return all_kits(descs)
    if mode == "kits":
        unknown = [k for k in kits if k not in descs]
        if unknown:
            raise Refusal(
                f"--kits names {', '.join(unknown)}, which {'is' if len(unknown) == 1 else 'are'} "
                f"not a registry entry; the population is the registry, never a directory listing"
            )
        return sorted(kits)
    missing = [k for k in DEFAULT_KITS if k not in descs]
    if missing:
        raise Refusal(f"the default set names {', '.join(missing)}, absent from the registry")
    return sorted(DEFAULT_KITS)


# The negative lookbehind is load-bearing and was bought by a failing arm. A discharge probe is a
# SHELL command, and shell parameter expansion is spelled `${name}` — so a bare `\{([a-z_]+)\}`
# matched the `{k}` inside `${k}` in a probe's own loop variable and reported a missing answer named
# `k`. Two syntaxes sharing a brace is the collision; refusing to match after a `$` is the fix.
TOKEN_RX = re.compile(r"(?<!\$)\{([a-z_]+)\}")


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
    for k in DEFAULT_KITS:
        if k not in descs:
            r.fail(f"the default set names '{k}', which is not a registry entry")
    unreachable = [e for e in descs if e not in derived_all
                   and descs[e][0].get("selectable") != "conditional"]
    for e in unreachable:
        r.fail(f"entry '{e}' is reached by no selection and is not marked conditional")

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


# ----------------------------------------------------------------------------------------- plan
def planned_writes(root: pathlib.Path, target: pathlib.Path, deploy: dict,
                   descs: dict[str, tuple[dict, str]], selection: list[str],
                   r: Report) -> list[dict]:
    """Every file `apply` would write, with its role and source commit. WRITES NOTHING.

    Machine-scoped rules produce an ORDER, not a write, so they are listed separately and never as
    files: `apply` writes nothing outside the repository the operator named.
    """
    commit = git(root, "rev-parse", "HEAD").strip()
    out: list[dict] = []
    for eid in selection:
        d, _dpath = descs[eid]
        ctx = target_context(target, deploy, eid, d)
        for rule in d.get("files", []):
            role = rule.get("role", "engine")
            srcs = rule_sources(d, rule)
            if rule.get("scope") == "machine" or rule.get("link"):
                for dest in rule_destinations(d, rule):
                    resolved, missing = resolve_tokens(dest, ctx)
                    out.append({"kit": eid, "role": role, "kind": "order",
                                "dest": resolved, "missing": missing, "src": ", ".join(srcs)})
                continue
            dests = rule_destinations(d, rule)
            if not dests:
                dests = [f"{{prefix}}/{{kit_id}}/{pathlib.PurePosixPath(s).name}" for s in srcs]
            for dest in dests:
                resolved, missing = resolve_tokens(dest, ctx)
                for k in missing:
                    r.fail(f"entry '{eid}' needs answer '{k}' to resolve destination '{dest}', and "
                           f"the target descriptor supplies none — refusing before any write, and "
                           f"naming the key rather than inventing a value")
                out.append({"kit": eid, "role": role, "kind": "write",
                            "dest": resolved, "missing": missing, "src": ", ".join(srcs),
                            "commit": commit})
            for sfx in rule.get("side_effects", []):
                resolved, _ = resolve_tokens(sfx, ctx)
                out.append({"kit": eid, "role": role, "kind": "side-effect", "dest": resolved,
                            "missing": [], "src": "(produced by the adopter or the merge)",
                            "commit": commit})
    return out


def cmd_plan(root: pathlib.Path, target: pathlib.Path, mode: str, kits: list[str]) -> int:
    r = Report()
    reg = load_toml(root / "tools" / "govkit" / "registry.toml")
    descs = read_descriptors(root, reg, r)
    deploy = load_deploy(target)
    selection = resolve_selection(descs, mode, kits)
    rows = planned_writes(root, target, deploy, descs, selection, r)

    print(f"govkit plan — target {target.as_posix()} · selection: {', '.join(selection)}")
    print(f"govkit plan — source commit {git(root, 'rev-parse', '--short', 'HEAD').strip()} "
          f"(bytes are taken from the git index at this commit, never from the working tree)")
    for row in rows:
        # A destination still carrying a brace is NOT a path, and printing it under `write` would
        # promise a write this tool cannot perform — the row is marked UNRESOLVED so the plan never
        # reads as a file set anyone can rely on.
        if row["missing"]:
            mark = "UNRES."
        elif row["kind"] == "order":
            mark = "ORDER "
        elif row["kind"] == "side-effect":
            mark = "SIDE  "
        else:
            mark = "write "
        print(f"  {mark} [{row['role']:<13}] {row['dest']}   <- {row['kit']}")
    holes = [(eid, h.get("id")) for eid in selection for h in descs[eid][0].get("hole", [])]
    for eid, hid in holes:
        print(f"  ORDER  [hole         ] .governance/outbox/{hid}.md   <- {eid}")
    print(f"govkit plan — {sum(1 for x in rows if x['kind'] == 'write')} write(s), "
          f"{sum(1 for x in rows if x['kind'] == 'side-effect')} side-effect(s), "
          f"{sum(1 for x in rows if x['kind'] == 'order') + len(holes)} order(s). NOTHING was written.")
    return r.emit()


# ---------------------------------------------------------------------------------------- check
def cmd_check(root: pathlib.Path, target: pathlib.Path) -> int:
    """Read-only verification of an installed target. Three states per kit.

    Exit 0 only when every selected kit is ADOPTED and every declared hole's probe passes. A hole
    that is undischarged reds regardless of what the kit's adopter exited with, because exit 0 from
    an adopter means "the adopter ran", never "the kit works".
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

    import json  # noqa: PLC0415 — only this path needs it
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    deploy = load_deploy(target)
    selection = receipt.get("kits") or []

    for eid in selection:
        if eid not in descs:
            r.fail(f"the receipt claims kit '{eid}', which is not a registry entry")
            continue
        d, _ = descs[eid]
        ctx = target_context(target, deploy, eid, d)
        state = "landed-but-inert"
        chk = d.get("check", {}).get("argv")
        if chk:
            argv, missing = zip(*(resolve_tokens(a, ctx) for a in chk)) if chk else ((), ())
            flat = [a for a in argv]
            if any(m for _a, m in ((a, resolve_tokens(a, ctx)[1]) for a in chk)):
                r.fail(f"kit '{eid}' check argv carries an unresolved token")
            else:
                rc = subprocess.run(flat, cwd=str(target), capture_output=True, text=True).returncode
                state = "adopted" if rc == 0 else "landed-but-inert"
                if rc != 0:
                    r.fail(f"kit '{eid}': its own adopter check arm exits {rc}, so the kit is landed "
                           f"but not working — surfaced rather than swallowed")
        print(f"govkit check — {eid}: {state}")

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
                rc = subprocess.run(resolved, cwd=str(target), capture_output=True,
                                    text=True).returncode
            except OSError as e:
                r.fail(f"kit '{eid}' hole '{hid}' probe could not run: {e}")
                continue
            if rc != 0:
                r.fail(f"kit '{eid}' hole '{hid}' is UNDISCHARGED (probe exit {rc}) — "
                       f"{h.get('why', '').splitlines()[0] if h.get('why') else 'no reason declared'}")
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
  govkit.py plan  --target <path> [--kits a,b | --all]
  govkit.py check --target <path>

`plan` and `check` are READ-ONLY and neither writes a byte. `apply`, `apply --resume` and `intake`
are later rollout commits and are absent rather than stubbed — a subcommand that parses and does
nothing looks exactly like one that works, from the outside, and this unit exists because that class
of silence ships broken installs.
"""


def parse_args(argv: list[str]) -> tuple[str, pathlib.Path | None, str, list[str]]:
    verb = argv[0]
    target: pathlib.Path | None = None
    mode, kits = "default", []
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--target" and i + 1 < len(argv):
            target = pathlib.Path(argv[i + 1]).resolve()
            i += 2
        elif a == "--all":
            mode = "all"
            i += 1
        elif a == "--kits" and i + 1 < len(argv):
            mode, kits = "kits", [k.strip() for k in argv[i + 1].split(",") if k.strip()]
            i += 2
        else:
            raise Refusal(f"unknown or incomplete argument: {a}")
    return verb, target, mode, kits


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        sys.stderr.write(USAGE)
        return 0 if argv else 2
    try:
        verb, target, mode, kits = parse_args(argv)
        root = repo_root()
        if verb == "selfcheck":
            if len(argv) != 1:
                raise Refusal("selfcheck takes no arguments")
            return selfcheck(root)
        if verb in ("plan", "check"):
            if target is None:
                raise Refusal(
                    f"{verb} needs an explicit --target. Refusing to default it to the process cwd: "
                    f"that is how a tool writes into, or reports on, a repository nobody named"
                )
            if not (target / ".git").exists():
                raise Refusal(f"--target {target.as_posix()} is not a git repository")
            return cmd_plan(root, target, mode, kits) if verb == "plan" else cmd_check(root, target)
        sys.stderr.write(f"govkit: unknown subcommand '{verb}'\n\n{USAGE}")
        return 2
    except Refusal as e:
        sys.stderr.write(f"govkit: {e}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
