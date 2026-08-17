#!/usr/bin/env python3
"""govkit — the mechanical deployer.

Contract: the deployer unit's spec under memory/builds/aSealedCaravan/spec/

WHAT THIS FILE DOES TODAY, AND WHAT IT DOES NOT. All five verbs: `selfcheck`, the read-only `plan`
and `check`, `apply` / `apply --resume`, and `intake`. What it does NOT do is stated on every run
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
import pathlib
import re
import subprocess
import sys

KIT_GOVKIT_VERSION = "1.1"  # gov:kit govkit@1.1 — kit identity; set HERE, never from a conf

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


def resolve_selection(reg: dict, descs: dict[str, tuple[dict, str]], mode: str,
                      kits: list[str]) -> list[str]:
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
    dk = default_kits(reg)
    if not dk:
        raise Refusal("registry.toml declares no [selection] default set, and this tool will not "
                      "invent one: a default nobody declared is a decision nobody made")
    missing = [k for k in dk if k not in descs]
    if missing:
        raise Refusal(f"the default set names {', '.join(missing)}, absent from the registry")
    return sorted(dk)


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
ROLE_KINDS = {
    "engine": "write",
    "seed": "write",
    "rendered": "side-effect",
    "generated": "side-effect",
    "project-owned": "order",
    "merged": "blocked",
}

#: DERIVED, never declared beside the table. A role added with any kind other than `write` is
#: automatically not landable and a role added as `write` is automatically landed, in BOTH verbs,
#: from one edit — which is what makes the single-table rule mechanical rather than remembered.
LANDABLE_ROLES = tuple(k for k, v in ROLE_KINDS.items() if v == "write")

#: The plan marks, in the order `cmd_plan` prints them. Kept beside the table so a new kind cannot
#: reach the printer without a mark.
KIND_MARKS = {"write": "write ", "order": "ORDER ", "side-effect": "SIDE  ",
              "covered": "COVER ", "blocked": "BLOCK "}


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
            if rule.get("scope") == "machine" or rule.get("link"):
                for dest in rule_destinations(d, rule):
                    resolved, missing = resolve_tokens(dest, ctx)
                    out.append({"kit": eid, "role": role, "kind": "order",
                                "dest": resolved, "missing": missing, "src": ", ".join(srcs)})
                continue
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
          "path · BLOCK = apply refuses the install over it · UNRES. = unresolved token, not a path")
    for row in rows:
        # A destination still carrying a brace is NOT a path, and printing it under `write` would
        # promise a write this tool cannot perform — the row is marked UNRESOLVED so the plan never
        # reads as a file set anyone can rely on.
        mark = "UNRES." if row["missing"] else KIND_MARKS.get(row["kind"], "?????")
        print(f"  {mark} [{row['role']:<13}] {row['dest']}   <- {row['kit']}")
    holes = [(eid, h.get("id")) for eid in selection for h in descs[eid][0].get("hole", [])]
    for eid, hid in holes:
        print(f"  ORDER  [hole         ] .governance/outbox/{hid}.md   <- {eid}")
    n = {k: sum(1 for x in rows if x["kind"] == k) for k in KIND_MARKS}
    print(f"govkit plan — {n['write']} write(s), {n['side-effect']} side-effect(s), "
          f"{n['order'] + len(holes)} order(s), {n['covered']} covered, {n['blocked']} blocked. "
          f"NOTHING was written.")
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


# ----------------------------------------------------------------------------------------- apply
# `LANDABLE_ROLES` used to be a hand-written `("engine", "seed")` HERE, beside the write loop, while
# `planned_writes` decided the same question with a different predicate. It is now DERIVED from
# `ROLE_KINDS` at the top of the roles section, so there is one table and one answer.


def resolve_dests(desc: dict, rule: dict, src: str, ctx: dict, home: str) -> list[tuple[str, list[str]]]:
    """Where one source lands under a rule, as `(destination, unresolved-answer-keys)` pairs.

    ONE spelling, called by `plan`, by the write loop, and by the wildcard exclusion — each has to
    ask the same question the writer will answer, and two computations of one thing is the class this
    repo keeps a record about.

    THE `missing` LIST IS RETURNED, not dropped. An earlier cut called `resolve_tokens(...)[0]` and
    discarded it, so `apply --kits kickoff-manifest` with no `manifest_path` answer wrote a file
    named literally `{manifest_path}` and exited 0, while `plan` exited 1 refusing the same install.
    A destination with an unresolved token is not a destination.

    An explicit `to` WINS for every role. Defaulting engine files to the kit-relative form regardless
    is how a flat entry — one with no kit directory at all — silently lands under a directory it does
    not have. The default applies only where the rule declared no destination.
    """
    if rule.get("to"):
        return [resolve_tokens(x.replace("{relpath}", pathlib.PurePosixPath(src).name), ctx)
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


def cmd_apply(root: pathlib.Path, target: pathlib.Path, mode: str, kits: list[str],
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

    # ---- refuse a role this commit cannot honour, BEFORE writing. Naming it beats half-landing it.
    for eid in selection:
        for rule in descs[eid][0].get("files", []):
            role = rule.get("role", "engine")
            if role == "merged":
                r.fail(f"entry '{eid}' declares a `merged` rule, and no verb here can write a "
                       f"gov-owned region into a target-owned file yet — nothing in this repo does "
                       f"it, so there is no seam to extend. Refusing rather than half-landing it")
    if r.problems:
        return r.emit()

    written: list[dict] = []
    # ---- LAND. Kit content from the index at `commit`, in the hard order S5 states. The
    # ---- `.gitattributes` block and the gate-runner wiring are the two steps this commit cannot
    # ---- perform; both are reported so the order is honest about what it skipped.
    print(f"govkit apply — LAND from {commit[:8]} into {target.as_posix()}")
    print("govkit apply — .gitattributes blocks: SKIPPED (no writer exists yet; reported, not silent)")
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
                continue
            pool = resolve_rule_pool(root, d, rule, ctx, home)
            for src in pool:
                pairs = resolve_dests(d, rule, src, ctx, home)
                unresolved = sorted({k for _dst, miss in pairs for k in miss})
                if unresolved:
                    r.fail(f"entry '{eid}': {src} has no resolvable destination — the target "
                           f"descriptor supplies no answer for {', '.join(unresolved)}. Refusing "
                           f"rather than writing a path with the token still in it")
                    continue
                dests = [dst for dst, _miss in pairs]
                data = blob_at(root, commit, src)
                if data is None:
                    r.fail(f"entry '{eid}': {src} does not resolve at {commit[:8]}")
                    continue
                for dest in dests:
                    dp = target / dest
                    if role == "seed" and dp.exists():
                        continue  # seed: copied ONCE, then the target owns it
                    dp.parent.mkdir(parents=True, exist_ok=True)
                    dp.write_bytes(data)
                    written.append({"path": dest, "role": role, "kit": eid,
                                    "sha256": hashlib.sha256(data).hexdigest(),
                                    "source": src, "commit": commit})
    print(f"govkit apply — landed {len(written)} file(s)")

    # ---- STAGE. Not housekeeping: every gate in this suite reads the INDEX, so an unstaged install
    # ---- is invisible to the verification that follows it.
    if written:
        subprocess.run(["git", "-C", str(target), "add", "--"] + [w["path"] for w in written],
                       capture_output=True, check=False)
    print("govkit apply — staged everything written")
    print("govkit apply — gate-runner and CI legs: SKIPPED (no emitter yet; reported, not silent)")

    # ---- CONFIGURE. A kit with a blocks_adopt hole lands and is NOT configured.
    outbox = target / ".governance" / "outbox"
    outbox.mkdir(parents=True, exist_ok=True)
    for eid in selection:
        d, _p = descs[eid]
        ctx = target_context(target, deploy, eid, d)
        blocked = [h for h in d.get("hole", []) if h.get("blocks_adopt")]
        for h in d.get("hole", []):
            (outbox / f"{h.get('id')}.md").write_text(
                f"# {h.get('id')} — {eid}\n\n{h.get('why', '').strip()}\n\n"
                f"Discharge is decided by RUNNING this hole's probe, never by deleting this file.\n",
                encoding="utf-8", newline="\n")
        if blocked and not resume:
            print(f"govkit apply — CONFIGURE {eid}: skipped, blocked by hole "
                  f"'{blocked[0].get('id')}' — landed but inert")
            continue
        argv = d.get("adopt", {}).get("argv") or []
        if not argv:
            continue
        resolved = [resolve_tokens(a, ctx)[0] for a in argv]
        rc = subprocess.run(resolved, cwd=str(target), capture_output=True, text=True).returncode
        print(f"govkit apply — CONFIGURE {eid}: adopter exit {rc}")

    # ---- RECEIPT. Tool-written only, plus the flat sidecar a target verifies with bash alone.
    (target / ".governance").mkdir(exist_ok=True)
    receipt_path.write_text(json.dumps(
        {"gov_source": str(root), "gov_commit": commit,
         "prefix": (deploy.get("prefix") or "tools"), "kits": selection, "files": written},
        indent=2) + "\n", encoding="utf-8", newline="\n")
    (target / ".governance" / "install.sums").write_text(
        "".join(f"{w['sha256']}  {w['path']}\n" for w in written), encoding="utf-8", newline="\n")
    print(f"govkit apply — receipt written: {len(written)} file(s), {len(selection)} kit(s)")
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
    body = ['# deploy.toml — written once by `govkit intake`. Committed, it is the standing',
            '# authorization for an unattended re-run: it carries every owner decision, so a later',
            '# `apply` reads answers rather than asking for them again.',
            '',
            f'gov_source = "{root.as_posix()}"',
            f'gov_commit = "{git(root, "rev-parse", "HEAD").strip()}"',
            'prefix = "tools"',
            'kits = [' + ", ".join(f'"{k}"' for k in selection) + ']',
            '',
            '[answers]']
    body += [f'{k} = "{answers[k]}"' for k in need]
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
          f"{len(need)} answer(s) recorded")
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
  govkit.py apply --target <path> [--kits a,b | --all] [--resume]
  govkit.py intake --target <path> [--kits a,b | --all] [--answer key=value ...]

`plan` and `check` are READ-ONLY and neither writes a byte. `intake` writes the target descriptor
ONCE and refuses to overwrite one that exists — a subcommand that parses and does
nothing looks exactly like one that works, from the outside, and this unit exists because that class
of silence ships broken installs.
"""


def parse_args(argv: list[str]) -> tuple[str, pathlib.Path | None, str, list[str], bool, dict[str, str]]:
    verb = argv[0]
    target: pathlib.Path | None = None
    mode, kits = "default", []
    resume = False
    answers: dict[str, str] = {}
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
        elif a == "--all":
            mode = "all"
            i += 1
        elif a == "--kits" and i + 1 < len(argv):
            mode, kits = "kits", [k.strip() for k in argv[i + 1].split(",") if k.strip()]
            i += 2
        else:
            raise Refusal(f"unknown or incomplete argument: {a}")
    return verb, target, mode, kits, resume, answers


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        sys.stderr.write(USAGE)
        return 0 if argv else 2
    try:
        verb, target, mode, kits, RESUME, ANSWERS = parse_args(argv)
        root = repo_root()
        if verb == "selfcheck":
            if len(argv) != 1:
                raise Refusal("selfcheck takes no arguments")
            return selfcheck(root)
        if verb in ("plan", "check", "apply", "intake"):
            if target is None:
                raise Refusal(
                    f"{verb} needs an explicit --target. Refusing to default it to the process cwd: "
                    f"that is how a tool writes into, or reports on, a repository nobody named"
                )
            if not (target / ".git").exists():
                raise Refusal(f"--target {target.as_posix()} is not a git repository")
            if verb == "plan":
                return cmd_plan(root, target, mode, kits)
            if verb == "check":
                return cmd_check(root, target)
            if verb == "intake":
                return cmd_intake(root, target, mode, kits, ANSWERS)
            return cmd_apply(root, target, mode, kits, resume=RESUME)
        sys.stderr.write(f"govkit: unknown subcommand '{verb}'\n\n{USAGE}")
        return 2
    except Refusal as e:
        sys.stderr.write(f"govkit: {e}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
