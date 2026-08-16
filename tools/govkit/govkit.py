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

KIT_GOVKIT_VERSION = "1.2"  # gov:kit govkit@1.2 — kit identity; set HERE, never from a conf

RECEIPT_SCHEMA = 2  # bumped by any unit that adds a per-role row field; readers accept 1 and 2

# The hard order's step ids, RESERVED here in one ordered tuple — including the steps this engine
# does not perform yet. A step id is data, not a print: the ordering criterion is an assertion about
# ORDER, and before this there was nothing stable to order. Later units FILL steps and may never
# rename one. The owning unit per id is the table in DEPL-aTetheredConvoy-1 section 4; no count of
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
}


def expand_rules(root: pathlib.Path, desc: dict) -> list[dict]:
    """Every (rule index, source, destination template, role) the descriptor names, BEFORE precedence.

    A `**` include enumerates the tracked files under `home`; everything else is literal. A rule that
    names no source at all still contributes its declared destinations, because a delegated rule has
    no gov bytes and its destination must still be visible to `plan` and to the receipt.
    """
    home = (desc.get("home") or "").rstrip("/")
    pool_all: list[str] | None = None
    out: list[dict] = []
    for i, rule in enumerate(desc.get("files", [])):
        role = rule.get("role", "engine")
        inc = rule.get("include")
        srcs = inc if isinstance(inc, list) else ([inc] if inc else [])
        if any(s == "**" for s in srcs):
            if pool_all is None:
                pool_all = tracked(root)
            pool = [f for f in pool_all if home and f.startswith(home + "/")]
        else:
            pool = rule_sources(desc, rule)
        for src in pool:
            for dest in destinations_for(desc, rule, src):
                out.append({"rule": i, "src": src, "dest": dest, "role": role})
        if not pool:
            for dest in rule_destinations(desc, rule):
                out.append({"rule": i, "src": None, "dest": dest, "role": role})
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
    rows = expand_rules(root, desc)

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
        dest, miss = resolve_tokens(r["dest"], ctx)
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

    # ---- 7f: PRECEDENCE, both halves, over gov's own descriptors (DEPL-aTetheredConvoy-1 S1).
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

    # ---- 7h: LEG correspondence, BOTH directions (DEPL-aTetheredConvoy-3 S1). The descriptors and
    #          gov's own leg manifest are two spellings of one fact, and before this nothing asserted
    #          they agree — the deployer's whole thesis, unapplied to the deployer. An exemption is
    #          the escape, on the same reason-and-staleness rule as the path exemptions, and S6
    #          refuses a leg that is BOTH claimed and exempted.
    legs_path = root / "tools" / "gate-legs.json"
    if legs_path.is_file():
        manifest = {leg.get("name") for leg in json.loads(legs_path.read_text(encoding="utf-8"))}
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
            exempt_legs[nm] = why
        for nm in sorted(manifest - set(claimed_legs) - set(exempt_legs)):
            r.fail(f"gate leg '{nm}' is claimed by no descriptor and carried by no [[exempt_leg]] — "
                   f"a new leg must red until a declaration says whether an adopter receives it")
        r.note(f"legs: {len(manifest)} in the manifest · {len(claimed_legs)} claimed · "
               f"{len(exempt_legs)} exempt")

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
        res = resolve_entry(root, d, ctx)
        rules = d.get("files", [])

        # ONE expansion, shared with apply. Before this, the planner emitted a row per RULE while the
        # writer expanded the same rule over tracked files, and the planner applied no role filter at
        # all — so it printed `write` for three destinations apply refuses and for every role apply
        # cannot land. The two verbs were two implementations of one question.
        for dest, w in sorted(res["writes"].items()):
            rule = rules[w["rule"]]
            if rule.get("scope") == "machine" or rule.get("link"):
                out.append({"kit": eid, "role": w["role"], "kind": "order", "dest": dest,
                            "missing": w["missing"], "src": w["src"] or ""})
                continue
            for k in w["missing"]:
                r.fail(f"entry '{eid}' needs answer '{k}' to resolve destination '{w['dest']}', and "
                       f"the target descriptor supplies none — refusing before any write, and "
                       f"naming the key rather than inventing a value")
            out.append({"kit": eid, "role": w["role"], "kind": "write", "dest": dest,
                        "missing": w["missing"], "src": w["src"] or "", "commit": commit})

        for u in res["unlanded"]:
            out.append({"kit": eid, "role": u["role"], "kind": "skip", "dest": u["dest"],
                        "missing": u["missing"], "src": u["src"] or "",
                        "why": UNLANDED_REASON.get(u["role"], "role outside the enum")})

        seen_sfx: set[str] = set()
        for rule in rules:
            for sfx in rule.get("side_effects", []):
                resolved, _ = resolve_tokens(sfx, ctx)
                if resolved in seen_sfx:
                    continue
                seen_sfx.add(resolved)
                out.append({"kit": eid, "role": rule.get("role", "engine"), "kind": "side-effect",
                            "dest": resolved, "missing": [],
                            "src": "(produced by the adopter or the merge)", "commit": commit})
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
        elif row["kind"] == "skip":
            mark = "SKIP  "
        else:
            mark = "write "
        tail = f"   ({row['why']})" if row.get("why") else ""
        print(f"  {mark} [{row['role']:<13}] {row['dest']}   <- {row['kit']}{tail}")
    holes = [(eid, h.get("id")) for eid in selection for h in descs[eid][0].get("hole", [])]
    for eid, hid in holes:
        print(f"  ORDER  [hole         ] .governance/outbox/{hid}.md   <- {eid}")
    print(f"govkit plan — {sum(1 for x in rows if x['kind'] == 'write')} write(s), "
          f"{sum(1 for x in rows if x['kind'] == 'side-effect')} side-effect(s), "
          f"{sum(1 for x in rows if x['kind'] == 'order') + len(holes)} order(s). NOTHING was written.")
    return r.emit()


# ---------------------------------------------------------------------------------------- check
def cmd_check(root: pathlib.Path, target: pathlib.Path) -> int:
    """Read-only verification of an installed target, over the state vocabulary DEPL-aTetheredConvoy-1
    owns.

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

        chk = (d.get("check") or {})
        state, detail = None, ""
        if chk.get("argv"):
            pairs = [resolve_tokens(a, ctx) for a in chk["argv"]]
            if any(m for _a, m in pairs):
                r.fail(f"kit '{eid}' check argv carries an unresolved token")
                state = "landed-unmeasured"
                detail = " (its check argv does not resolve)"
            else:
                rc = subprocess.run([a for a, _m in pairs], cwd=str(target),
                                    capture_output=True, text=True).returncode
                state = "adopted" if rc == 0 else "landed-but-inert"
                if rc != 0:
                    r.fail(f"kit '{eid}': its own adopter check arm exits {rc}, so the kit is landed "
                           f"but not working — surfaced rather than swallowed")
        elif "none" in chk:
            reason = str(chk.get("none", "")).strip()
            if not reason:
                r.fail(f"kit '{eid}' declares `[check] = {{ none }}` with an empty reason")
            state, detail = "landed-unmeasured", f" — {reason}" if reason else ""
        else:
            state = "landed-unmeasured"
            r.fail(f"kit '{eid}' declares neither `[check].argv` nor `[check] = {{ none = \"…\" }}`, "
                   f"so nothing measured it and nothing said why — declare the absence with a "
                   f"reason; silence is not a third option")
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
# LANDABLE_ROLES and UNLANDED_REASON live with the resolver, above: which roles land is a property of
# the resolution, not of the apply verb, and spelling it twice is the defect this file exists to end.


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

    rows: list[dict] = []       # every file gov is responsible for — the receipt, schema 2
    staged: list[str] = []      # only what this run actually wrote
    # ---- LAND. Kit content from the index at `commit`, through the ONE resolver `plan` also calls.
    step(STEP_LAND, f"from {commit[:8]} into {target.as_posix()}")
    for eid in selection:
        d, _p = descs[eid]
        ctx = target_context(target, deploy, eid, d)
        res = resolve_entry(root, d, ctx)
        vers = entry_version(root, d)

        # Every rule that does NOT land says so, by role, naming who does produce it. The silent
        # skip this replaces swallowed thirteen rules across the shipped descriptors.
        for u in res["unlanded"]:
            why = UNLANDED_REASON.get(u["role"])
            if why is None:
                r.fail(f"entry '{eid}' declares role '{u['role']}', which is not in the role enum — "
                       f"refusing rather than skipping a rule this engine cannot classify")
                continue
            rows.append({"path": u["dest"], "role": u["role"], "kit": eid,
                         "version": vers, "written": False, "source": u["src"]})
            print(f"govkit apply — not landed [{u['role']}] {u['dest']} — {why}")

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
            row = {"path": dest, "role": w["role"], "kit": eid, "version": vers,
                   "sha256": hashlib.sha256(data).hexdigest(),
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
    step(STEP_STAGE, f"{len(staged)} path(s)")
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
        if rc != 0:
            # A non-zero adopter exit is a FINDING, not a printed integer. Measured before this:
            # `apply --resume` printed 'adopter exit 1' and exited 0, so an install whose configure
            # phase failed was indistinguishable from one that worked. WHICH failure it is needs the
            # `[[outcome]]` evaluator, which is a later unit's; until then it is unclassified and
            # says so rather than being interpreted.
            r.fail(f"kit '{eid}': its adopter exited {rc} — unclassified, because no `[[outcome]]` "
                   f"evaluator exists yet to say WHICH declared outcome that code means")

    # ---- RECEIPT. Tool-written only, plus the flat sidecar a target verifies with bash alone.
    (target / ".governance").mkdir(exist_ok=True)
    receipt_path.write_text(json.dumps(
        {"schema": RECEIPT_SCHEMA, "gov_source": str(root), "gov_commit": commit,
         "prefix": (deploy.get("prefix") or "tools"), "kits": selection, "files": rows},
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

# What `update` does per ROLE. A role whose row is a refusal is still a ROW: silence is what lets a
# later unit add a role and leave it behind, and `selfcheck` asserts this covers the role enum.
UPDATE_ROLE = {
    "engine": "table",          # the full verdict table
    "seed": "report-reseed",    # never written; a moved template is reported
    "project-owned": "skip",    # gov supplied no bytes, so there is no base to compare
    "generated": "skip",
    "rendered": "adopter",      # re-run the adopter, compare, CAP at report
    "merged": "refuse",         # unit 6 fills this
    "attributes": "refuse",     # unit 6
    "gate-leg": "refuse",       # unit 4
    "ci": "refuse",             # unit 4
}


def _sha(b: bytes | None) -> str | None:
    return hashlib.sha256(b).hexdigest() if b is not None else None


def classify_row(root: pathlib.Path, target: pathlib.Path, row: dict, to_commit: str) -> dict:
    """One receipt row's verdict, from three blobs. `ours` is compared to the RECEIPT's hash.

    Not to `base`: for a rendered row those differ by construction, and for every row the receipt's
    hash is what gov actually wrote.
    """
    src, base_commit = row.get("source"), row.get("commit")
    theirs = blob_at(root, to_commit, src) if src else None
    base = blob_at(root, base_commit, src) if (src and base_commit) else None
    dp = target / row["path"]
    ours = dp.read_bytes() if dp.is_file() else None

    t_state = "absent" if theirs is None else ("equal" if _sha(theirs) == _sha(base) else "differs")
    if ours is None:
        o_state = "absent"
    elif _sha(ours) == row.get("sha256"):
        o_state = "equal"
    else:
        o_state = "differs"
    return {"verdict": VERDICT_GRID[(o_state, t_state)], "ours": ours, "theirs": theirs,
            "base": base, "o_state": o_state, "t_state": t_state}


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


def cmd_update(root: pathlib.Path, target: pathlib.Path, to_rev: str, write: bool) -> int:
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

    claimed = receipt.get("kits") or []
    for eid in claimed:
        if eid not in descs:
            raise Refusal(f"the receipt claims kit '{eid}', which is no longer a registry entry — "
                          f"refusing rather than dropping it, which would leave its files owned by "
                          f"nobody")
    available = [e for e in all_kits(descs) if e not in claimed]

    print(f"govkit update — {target.as_posix()}")
    print(f"govkit update — {base_commit[:8] if base_commit else '(none)'} -> {to_commit[:8]} · "
          f"receipt schema {schema} · {'WRITE' if write else 'read-only'}")

    deploy = load_deploy(target)
    tally: dict[str, int] = {}
    acted: list[dict] = []
    for row in receipt.get("files", []):
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

        if how in ("skip",):
            tally[role + ":skipped"] = tally.get(role + ":skipped", 0) + 1
            continue
        if how == "refuse":
            r.fail(f"row '{row['path']}' has role '{role}', which no unit has taught `update` to "
                   f"move yet — refusing by name rather than guessing")
            continue

        c = classify_row(root, target, row, to_commit)
        v = c["verdict"]
        if how == "seed" or how == "report-reseed":
            if c["t_state"] == "differs":
                v = "reseed-available"
            elif v not in ("missing",):
                v = "current" if c["o_state"] == "equal" else "patched"
        if how == "adopter" and v in ("diverged", "stale"):
            v = "re-rendered"          # CAP at report; the adopter owns these bytes
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

    if not write:
        print("govkit update — read-only. NOTHING was written; re-run with --write to perform it.")
        return r.emit()

    outbox = target / ".governance" / "outbox"
    outbox.mkdir(parents=True, exist_ok=True)
    changed, deleted, conflicts = [], [], 0
    for a in acted:
        row, c, v = a["row"], a["c"], a["verdict"]
        dp = target / row["path"]
        if v == "stale" or v == "missing":
            dp.parent.mkdir(parents=True, exist_ok=True)
            dp.write_bytes(c["theirs"])
            row["sha256"] = _sha(c["theirs"])
            row["commit"] = to_commit
            changed.append(row["path"])
        elif v == "withdrawn":
            if dp.is_file():
                dp.unlink()
            deleted.append(row["path"])
        elif v == "diverged":
            merged, how = three_way(c["ours"], c["base"] or b"", c["theirs"])
            if merged is None:
                conflicts += 1
                (outbox / f"update-conflict-{pathlib.PurePosixPath(row['path']).name}.md").write_text(
                    f"# update conflict — {row['path']}\n\n"
                    f"base   {base_commit} sha {_sha(c['base'])}\n"
                    f"ours   on disk       sha {_sha(c['ours'])}\n"
                    f"theirs {to_commit} sha {_sha(c['theirs'])}\n\n"
                    f"The file was left BYTE-IDENTICAL. Resolve by hand, then re-run `update`.\n",
                    encoding="utf-8", newline="\n")
                r.fail(f"'{row['path']}' diverged and the three-way conflicts — left untouched, "
                       f"order written")
            else:
                dp.write_bytes(merged)
                row["sha256"] = _sha(merged)
                row["commit"] = to_commit
                changed.append(row["path"])

    if changed:
        subprocess.run(["git", "-C", str(target), "add", "--"] + changed,
                       capture_output=True, check=False)
    if deleted:
        subprocess.run(["git", "-C", str(target), "rm", "-q", "--ignore-unmatch", "--"] + deleted,
                       capture_output=True, check=False)
    receipt["schema"] = RECEIPT_SCHEMA
    receipt["gov_commit"] = to_commit
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
    (target / ".governance" / "install.sums").write_text(
        "".join(f"{f['sha256']}  {f['path']}\n" for f in receipt["files"] if "sha256" in f),
        encoding="utf-8", newline="\n")
    print(f"govkit update — wrote {len(changed)}, deleted {len(deleted)}, "
          f"{conflicts} conflict(s); receipt re-stamped at {to_commit[:8]}")
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
  govkit.py update --target <path> [--to <rev>] [--write]
  govkit.py intake --target <path> [--kits a,b | --all] [--answer key=value ...]

`plan`, `check` and `update` are READ-ONLY and none writes a byte; `update --write` performs what
`update` printed. The default is read-only because that verb's failure mode is silent data loss in a
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
    to_rev = "HEAD"
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
        elif a == "--write":
            write = True
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
    return verb, target, mode, kits, resume, answers, write, to_rev


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        sys.stderr.write(USAGE)
        return 0 if argv else 2
    try:
        verb, target, mode, kits, RESUME, ANSWERS, WRITE, TO_REV = parse_args(argv)
        root = repo_root()
        if verb == "selfcheck":
            if len(argv) != 1:
                raise Refusal("selfcheck takes no arguments")
            return selfcheck(root)
        if verb in ("plan", "check", "apply", "intake", "update"):
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
            if verb == "update":
                return cmd_update(root, target, TO_REV, write=WRITE)
            return cmd_apply(root, target, mode, kits, resume=RESUME)
        sys.stderr.write(f"govkit: unknown subcommand '{verb}'\n\n{USAGE}")
        return 2
    except Refusal as e:
        sys.stderr.write(f"govkit: {e}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
