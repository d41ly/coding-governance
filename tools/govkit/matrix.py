#!/usr/bin/env python3
"""The acceptance matrix — the deployer driven against repo SHAPES, not against kits.

WHAT THIS IS NOT. `selftest.py` grades MECHANISMS, one fixture per behaviour, and unit 3's
deployability leg grades every registry ENTRY. This grades the four repo shapes the contract names,
and it CITES those two rather than re-asserting what they already assert: plan-equals-apply and
apply-twice stay with the deployability leg, and the per-mechanism arms stay in the selftest.

EVERY ARM'S EXPECTED OUTCOME IS STATED HERE, in the table below, rather than read off the
implementation. An arm with no stated expectation is a test written after the fact against itself,
which is the shape the contract refuses by name. Each asserts a MESSAGE or an on-disk effect and
never an exit code alone — an exit code shared by six unrelated outcomes is the ambiguity the
descriptors' outcome probes exist to resolve.
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
GOVKIT = HERE / "govkit.py"
NL = chr(10)
FAILURES: list[str] = []


def check(label: str, cond: bool, detail: str = "") -> None:
    if cond:
        print(f"ok   {label}")
    else:
        FAILURES.append(label)
        print(f"FAIL {label}" + (f" — {detail[:400]}" if detail else ""))


def git(cwd: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(GOVKIT), *args], capture_output=True, text=True)


DEPLOY = ('gov_source = "l"' + NL + 'prefix = "tools"' + NL + 'kits = ["check-wiring"]' + NL
          + "[answers]" + NL + 'memory_root = "memory"' + NL)


def shape(tmp: pathlib.Path, name: str, *, lang: str = "none", hook: str | None = None,
          policy: str = "") -> pathlib.Path:
    g = tmp / name
    g.mkdir(parents=True, exist_ok=True)
    (g / ".governance").mkdir(exist_ok=True)
    (g / ".governance" / "deploy.toml").write_text(DEPLOY + policy, encoding="utf-8", newline=NL)
    (g / "README.md").write_text("t" + NL, encoding="utf-8", newline=NL)
    if lang == "python":
        (g / "app.py").write_text("x = 1" + NL, encoding="utf-8", newline=NL)
    git(g, "init", "-q", "-b", "main")
    git(g, "config", "user.email", "t@e")
    git(g, "config", "user.name", "t")
    if hook is not None:
        hd = g / ".githooks"
        hd.mkdir(exist_ok=True)
        (hd / "pre-commit").write_text(hook, encoding="utf-8", newline=NL)
        (hd / "pre-commit").chmod(0o755)
        git(g, "config", "core.hooksPath", ".githooks")
    git(g, "add", "-A")
    git(g, "commit", "-qm", "base")
    return g


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        shapes = 0

        # SHAPE 1 — a fresh, empty repository.
        # EXPECTED: the install COMPLETES and the receipt exists. This is the base case and every
        # other shape is measured as a departure from it.
        shapes += 1
        g = shape(tmp, "empty")
        p = run("apply", "--target", str(g), "--kits", "check-wiring")
        check("empty repo: the install completes", p.returncode == 0, p.stdout + p.stderr)
        check("empty repo: a receipt exists",
              (g / ".governance" / "install.json").is_file(), "")
        check("empty repo: the landed file is on disk, not merely recorded",
              (g / "tools" / "check-wiring.sh").is_file(), "")

        # SHAPE 2 — a repository with no Python of its own.
        # EXPECTED: the DEPLOYER runs on the deployer's interpreter regardless; the target having no
        # Python is irrelevant to landing. Stated because the opposite is the natural assumption.
        shapes += 1
        g = shape(tmp, "nopython", lang="none")
        p = run("apply", "--target", str(g), "--kits", "check-wiring")
        check("no-python repo: the deployer runs on ITS OWN interpreter and lands anyway",
              p.returncode == 0 and (g / "tools" / "check-wiring.sh").is_file(),
              p.stdout + p.stderr)

        # SHAPE 3 — a repository whose pre-commit hook REFUSES.
        # EXPECTED: the install COMPLETES and the receipt exists, because `apply` never commits and
        # therefore no hook fires during the install itself; and an ORDER carries the hook's own
        # output, so the operator meets the refusal here rather than when they try to land.
        shapes += 1
        g = shape(tmp, "hookblock", hook="#!/usr/bin/env bash" + NL + "echo NOPE >&2" + NL +
                  "exit 1" + NL)
        p = run("apply", "--target", str(g), "--kits", "check-wiring")
        check("blocking-hook repo: the install COMPLETES anyway — apply never commits",
              (g / ".governance" / "install.json").is_file(), p.stdout + p.stderr)
        ob = g / ".governance" / "outbox" / "hook-block.md"
        check("blocking-hook repo: an order carries the hook's OWN output",
              ob.is_file() and "NOPE" in ob.read_text(encoding="utf-8"),
              ob.read_text(encoding="utf-8") if ob.is_file() else "absent")
        check("blocking-hook repo: the probe records the state by NAME, not by an exit code",
              json.loads((g / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("hook_block", {}).get("state") == "block", "")
        # And the NEGATIVE half, which is what makes the three-valued probe worth having: with NO
        # hook the probe must record `no-hook`, NOT `pass` — measured, git's hook runner exits
        # non-zero for both, so an exit-code reading would collapse them.
        g2 = shape(tmp, "nohook")
        run("apply", "--target", str(g2), "--kits", "check-wiring")
        check("no-hook repo: recorded as no-hook, a state distinct from a refusing hook",
              json.loads((g2 / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("hook_block", {}).get("state") == "no-hook", "")

        # SHAPE 4 — a repository carrying a gate leg of its own that is ALREADY red.
        # EXPECTED with the default policy: the install COMPLETES, the pre-existing red leg is
        # REPORTED and does not fail it. With the policy flipped to refuse: apply exits non-zero
        # and leaves NO receipt, because the refusal happens at the baseline, before any write.
        shapes += 1
        runner = ("import json, subprocess" + NL +
                  "legs = json.load(open('tools/legs.json'))" + NL +
                  "for l in legs:" + NL +
                  "    c = subprocess.run(l['argv'], capture_output=True).returncode" + NL +
                  "    print(('GATE ok    ' if c == 0 else 'GATE FAIL  ') + l['name'])" + NL)
        decl = (NL + "[gate_runner]" + NL + 'kind = "manifest"' + NL +
                'file = "tools/legs.json"' + NL + 'grammar = "json-array"' + NL +
                'dedupe_key = "name"' + NL +
                'command = ["%s", "tools/runner.py"]' % sys.executable.replace(chr(92), "/") + NL +
                'run_all_env = { GATE_FULL = "1" }' + NL +
                'observed_ran = ["GATE ok    {name}"]' + NL +
                'observed_failed = ["GATE FAIL  {name}"]' + NL)

        for policy_val, label in (("proceed", "default"), ("refuse", "refuse")):
            g = tmp / ("prered-" + policy_val)
            (g / "tools").mkdir(parents=True, exist_ok=True)
            (g / "tools" / "runner.py").write_text(runner, encoding="utf-8", newline=NL)
            (g / "tools" / "legs.json").write_text(
                json.dumps([{"name": "theirs", "argv": ["false"]}], indent=2) + NL,
                encoding="utf-8", newline=NL)
            (g / ".governance").mkdir(exist_ok=True)
            (g / ".governance" / "deploy.toml").write_text(
                DEPLOY + NL + "[policy]" + NL + 'on_baseline_red = "%s"' % policy_val + NL + decl,
                encoding="utf-8", newline=NL)
            git(g, "init", "-q", "-b", "main"); git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t"); git(g, "add", "-A"); git(g, "commit", "-qm", "b")
            p = run("apply", "--target", str(g), "--kits", "check-wiring")
            if policy_val == "proceed":
                check("pre-existing-red repo: the install completes and REPORTS the red leg",
                      (g / ".governance" / "install.json").is_file()
                      and "ALREADY red" in p.stdout, p.stdout + p.stderr)
            else:
                check("pre-existing-red repo, policy=refuse: apply refuses NAMING the leg",
                      "theirs" in p.stderr, p.stdout + p.stderr)
                check("pre-existing-red repo, policy=refuse: and leaves NO receipt — the refusal "
                      "is at the baseline, before any write",
                      not (g / ".governance" / "install.json").exists(), "")

        print(f"govkit-matrix: {shapes} repo shape(s) exercised")
        if shapes == 0:
            print("govkit-matrix: NO shape ran — a matrix over nothing is not a matrix")
            return 1
    if FAILURES:
        print(f"govkit-matrix: {len(FAILURES)} FAILED — " + "; ".join(FAILURES[:3]))
        return 1
    print("govkit-matrix: all arms held")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
