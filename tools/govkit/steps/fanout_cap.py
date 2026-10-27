#!/usr/bin/env python3
"""fanout_cap.py — the upgrade step `agent-cap/fanout-cap-to-agents-in-flight` (TOOL-dSafePassage-1, S6).

    python <prefix>/govkit/steps/fanout_cap.py up|down|witness <target>

Its row is the agent-cap descriptor's `[[upgrade]]`. The UP moves `.agent-cap.conf`'s `FANOUT_CAP`
into the policy key `runtime.agents-in-flight` and takes the line out, so the limit reads the same
on either side of it; the DOWN restores both files byte-identical; the WITNESS exits 0 when no
`FANOUT_CAP` assignment is left in the file, or there is no file, which is the step applied.

THE UP, in order. No `.agent-cap.conf`: exit 0, nothing written. Otherwise the file's working-tree
bytes, the whole of which the before-image keeps, are read in the policy reader's legacy grammar,
`read_legacy_fanout`'s (TOOL-dSafePassage-26 S30): `FANOUT_CAP=<n>` or `FANOUT_CAP="<n>"`, a BOM and a
trailing CR tolerated, the last such line winning, and every other line — another key, a blank, a
comment — legal and ignored. The up exits 1 WRITING NOTHING on a value that is not an integer of at
least 1, or where the conf or the policy file differs from its blob at HEAD — the policy reader
reads committed revisions only, so an uncommitted edit is one it would not see. It takes out only
the `FANOUT_CAP` lines, and removes the file only where blanks and comments alone remain. Where gov's
`policy.py get runtime.agents-in-flight --rev HEAD --explain`, run in the target, gives the reason
`lowered to <n> by FANOUT_CAP`, the key is set to `<n>` through `render_policy_text`; otherwise the
file lowers nothing and the policy file is left byte-identical, restating no default. The conf is
rewritten or removed LAST, so the witness changes last. The pre-write reads run only while no before-image
exists: a re-run over a killed up recomputes from the first image and converges.

Exit 0 done, 1 refused naming the file (nothing written), 2 a usage error.
"""

import importlib.util
import pathlib
import re
import subprocess
import sys

STEP_ID = "agent-cap/fanout-cap-to-agents-in-flight"
CONF = ".agent-cap.conf"
POLICY = ".governance/policy.toml"
FANOUT_LINE = re.compile(r"^\s*FANOUT_CAP\s*=(.*)$")
LOWERED_RE = re.compile(r"lowered to (\d+) by FANOUT_CAP")
GOV = pathlib.Path(__file__).resolve().parents[2]  # `{gov}`: the tool root this step ships in


def load_steps():
    """The step reader beside this file's directory, imported by its path: the runner's `-I` drops
    this file's own directory from `sys.path`, and the before-image helpers live there."""
    path = pathlib.Path(__file__).resolve().parents[1] / "upgrade_steps.py"
    mod = sys.modules.get("upgrade_steps")
    if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
        return mod
    spec = importlib.util.spec_from_file_location("upgrade_steps", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["upgrade_steps"] = mod
    spec.loader.exec_module(mod)
    return mod


STEPS = load_steps()
Refusal = STEPS.Refusal


# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the canonical
# copy named on its marker line and gated by the resolve-python self-test: the policy kit's reader
# is found through it, never through a typed kit path.
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


def parse_conf(data: bytes):
    """The `FANOUT_CAP` value `.agent-cap.conf`'s bytes carry, None where no line sets it; a value
    that is not an integer of at least 1 is a refusal at its line. Any other line is legal."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise Refusal(f"{CONF}: not UTF-8 ({e}), so its FANOUT_CAP cannot be read") from None
    found = None
    for n, ln in enumerate(text.removeprefix("\ufeff").split("\n"), 1):
        ln = ln.rstrip("\r")
        m = FANOUT_LINE.match(ln)
        if m:
            found = (m[1].strip(), n)
    if found is None:
        return None
    raw, n = found
    value = raw[1:-1] if len(raw) >= 2 and raw[0] == raw[-1] == '"' else raw
    if not re.fullmatch(r"[0-9]+", value) or int(value) < 1:
        raise Refusal(f"{CONF}:{n}: FANOUT_CAP must be an integer of at least 1")
    return int(value)


def render_conf_rest(data: bytes) -> bytes | None:
    """`.agent-cap.conf`'s bytes with every `FANOUT_CAP` line taken out, each other line byte for
    byte; None where only blanks and comments remain, the file then removed."""
    lines = data.decode("utf-8").splitlines(keepends=True)
    rest = [ln for ln in lines if not FANOUT_LINE.match(ln.removeprefix("\ufeff").rstrip("\r\n"))]
    left = [ln.removeprefix("\ufeff").strip() for ln in rest]
    return None if all(not ln or ln.startswith("#") for ln in left) else "".join(rest).encode("utf-8")


def check_committed(target: pathlib.Path, rel: str) -> bool:
    """True where the working-tree `rel` is its blob at HEAD, read through the target's own filters,
    or is absent in both."""
    head = subprocess.run(["git", "-C", str(target), "rev-parse", "--verify", "--quiet", f"HEAD:{rel}"],
                          capture_output=True, encoding="utf-8")
    if not (target / rel).is_file():
        return head.returncode != 0
    now = subprocess.run(["git", "-C", str(target), "hash-object", f"--path={rel}", "--", rel],
                         capture_output=True, encoding="utf-8")
    return head.returncode == 0 and now.returncode == 0 and head.stdout.strip() == now.stdout.strip()


def render_policy_bytes(before: bytes | None, n: int) -> bytes:
    """The policy file's bytes with `runtime.agents-in-flight` set to `n`, through the one writer."""
    text = None if before is None else before.decode("utf-8")
    return STEPS.render_policy_text(text, "runtime", "agents-in-flight", n).encode("utf-8")


def cmd_up(target: pathlib.Path) -> int:
    conf = target / CONF
    if not conf.is_file():
        print(f"fanout-cap: up · no {CONF} at {target.as_posix()}, so there is nothing to move")
        return 0
    policy_py = resolve_kit_dir("policy", "policy.py", GOV) / "policy.py"

    def derive_after(before):
        if before is not None:
            n = parse_conf(before[CONF])
            after = {CONF: render_conf_rest(before[CONF])}
            if POLICY in before:
                after[POLICY] = render_policy_bytes(before[POLICY], n)
            return after
        data = conf.read_bytes()
        n = parse_conf(data)
        for rel in (CONF, POLICY):
            if not check_committed(target, rel):
                raise Refusal(f"{rel}: differs from its blob at HEAD, and the policy reader reads "
                              f"committed revisions only; commit it, then re-run the step")
        after = {CONF: render_conf_rest(data)}
        if n is None:
            return after
        got = subprocess.run([sys.executable, str(policy_py), "get", "runtime.agents-in-flight",
                              "--rev", "HEAD", "--explain"],
                             cwd=str(target), capture_output=True, encoding="utf-8")
        if got.returncode != 0:
            raise Refusal(f"{POLICY}: policy.py get runtime.agents-in-flight refused at HEAD: "
                          f"{got.stderr.strip()}")
        m = LOWERED_RE.search(got.stderr)
        if m:
            pol = target / POLICY
            after[POLICY] = render_policy_bytes(pol.read_bytes() if pol.is_file() else None, int(m[1]))
        return after

    after = STEPS.write_before_image(target, STEP_ID, derive_after)
    if after.get(POLICY) is not None:
        (target / POLICY).parent.mkdir(parents=True, exist_ok=True)
        (target / POLICY).write_bytes(after[POLICY])
    if after[CONF] is None:  # LAST: the witness reads the line's absence
        conf.unlink()
    else:
        conf.write_bytes(after[CONF])
    print(f"fanout-cap: up · {CONF} " + ("retired" if after[CONF] is None else "kept, its FANOUT_CAP taken out")
          + (" · runtime.agents-in-flight set in " + POLICY if POLICY in after else
             f" · it lowered nothing, so {POLICY} is unchanged"))
    return 0


def cmd_down(target: pathlib.Path) -> int:
    restored = STEPS.write_from_before_image(target, STEP_ID)
    print(f"fanout-cap: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path) -> int:
    conf = target / CONF
    text = conf.read_bytes().decode("utf-8", "replace") if conf.is_file() else ""
    held = any(FANOUT_LINE.match(ln.removeprefix("\ufeff").rstrip("\r")) for ln in text.split("\n"))
    print(f"fanout-cap: witness · {CONF} " + ("assigns FANOUT_CAP: not applied" if held else
                                             "assigns no FANOUT_CAP, or is absent: applied"))
    return 1 if held else 0


def main(argv: list[str]) -> int:
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 2 or argv[0] not in verbs:
        sys.stderr.write("usage: python fanout_cap.py up|down|witness <target>\n")
        return 2
    try:
        return verbs[argv[0]](pathlib.Path(argv[1]).resolve())
    except Refusal as e:
        sys.stderr.write(f"fanout-cap: {argv[0]} refused · {e}\n")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
