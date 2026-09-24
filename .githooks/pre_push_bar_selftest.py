#!/usr/bin/env python3
"""Does .githooks/pre-push refuse a merge bar it cannot vouch for? TOOL-aRepatriatedFork-5.

Ported from NicoCares' `scripts/pre_push_bar_selftest.py` (PKG-dCandidLodestar-5), which carried
the guard this hook now ships. Its cases and its three-arm mutation are kept; the port renames its
functions to this repository's verb table, names every text encoding, and reads the run-log `bar`
key the hook's END line gained here.

WHY THIS IS ITS OWN LEG, BESIDE .githooks/pre-push.test.sh. That suite covers the hook's
classification and carries the guard's arms 25-29b. This file covers the narrower and sharper
question, WHICH COMMAND ACTUALLY RUNS, and it is the only control that re-disables the guard's
arms on every run (the owner's F2 ruling on the unit's spec).

THE DEFECT LINEAGE, each step measured rather than argued:

  rev-1  guarded the LAST path-shaped token.   `bash /tmp/evil.sh <tracked>` landed.
  rev-2  guarded EVERY path-shaped token.      `gatepayload <tracked>` landed: the payload is a
                                               PATH command, so it holds no '/' and does not end
                                               '.sh', and no arm ever looked at it.
                                               `bash -c gatepayload <tracked>` landed the same way.
                                               `bash <tracked>` with <tracked> rewritten in the
                                               working tree landed too: the blob is what the check
                                               reads, the working copy is what runs.
  rev-3  constrains the FIRST WORD (a tracked script, or bash/sh with no option word before the
         script) and requires each tracked token's working copy to hash to its blob.
         `bash gatepayload <tracked>` still landed (closing review round 1 B1): the payload
         sat BETWEEN the interpreter and the script, where no arm looked.
  rev-4  constrains the EXECUTED word by POSITION, word 1 or word 2 after bash/sh, and requires
         it path-shaped, which routes it through the tracked and working-copy arms. And the
         whole value must be the kit's own runner or the GATE_CMD `.unattended.conf` declares
         at the pushed sha (M1): every tracked script that exits 0 passed rev-3.

Each of those landings was observed at rc 0 with the bar stubbed RED and the remote MOVED, which is
why this file drives real `git push` calls against a scratch remote rather than asserting on the
hook's text.

THE MUTATION RUNS EVERY TIME. A guard whose failing case was observed once, by hand, on the day it
landed, is a guard nobody will ever see fail again. Every run re-disables the program, option,
working-copy and declared arms in a COPY of the hook and asserts the five hostile values LAND, so if the arms are ever removed,
weakened or short-circuited, this file stops being able to prove its own mutation and says so.

WHAT THIS DOES NOT CHECK. `--no-verify`, a `core.hooksPath` pointed elsewhere, and `BASH_ENV`, each
of which bypasses the hook as a whole (the unit's spec, section 3). The run-log line's other fields,
which `.githooks/pre-push.runlog.test.sh` grades. The lander marker push-main withholds under the
escape, which `push-main.test.sh` grades.

Usage:
    python .githooks/pre_push_bar_selftest.py [-v]
Exit 0 = every case ok, and at least FLOOR_ASSERTIONS of them ran.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOK = os.path.join(ROOT, ".githooks", "pre-push")

# The anchor the mutation splices after. It is the end of the tokenising loop inside the hook's
# `check_bar_command`, so everything the rev-3 arms read is already computed and can be overwritten
# wholesale.
ANCHOR = "  set +f\n"
# Neutralises exactly the rev-4 arms and nothing else: the executed-word check (its value set to a
# path shape), the option check, the working-copy hash check and the declared-value check. The
# every-token tracked check (rev-2) keeps working, which is what makes the mutation a test of THESE
# arms rather than of the whole block. `_tree_dirty` is the
# hook's dirty-tree refusal (TOOL-aRepatriatedFork-8 S3), measured before this point and refused
# after it: it catches M3's rewritten bar one layer out, so it is cleared too or M3 could not land.
NEUTER = ('  _bar_prog=neutered.sh; _bar_opt=""; _bar_dirty=""; _bar_decl=$cmd; _tree_dirty=""'
          '   # SELFTEST MUTATION\n')

# The executed-assertion floor. A case block stranded behind an early return reads as fewer
# assertions, never as a pass.
FLOOR_ASSERTIONS = 22

FAILURES: list[str] = []
COUNT = [0]
VERBOSE = "-v" in sys.argv or "--verbose" in sys.argv


def print_ok(msg: str) -> None:
    COUNT[0] += 1
    print(f"  ok   — {msg}")


def print_fail(msg: str) -> None:
    COUNT[0] += 1
    print(f"  FAIL — {msg}")
    FAILURES.append(msg)


def run(args: list[str], cwd: str, env: dict | None = None) -> tuple[int, str]:
    e = dict(os.environ)
    for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GOV_GATE_CMD", "GOV_GATE_CMD_TEST",
              "GATE_SELFTESTS", "GOV_RUNLOG"):
        e.pop(k, None)
    if env:
        e.update(env)
    p = subprocess.run(args, cwd=cwd, env=e, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def write(path: str, text: str, executable: bool = False) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    if executable:
        os.chmod(path, 0o755)


class Fixture:
    """A scratch repo + bare remote with the hook under test installed."""

    def __init__(self, tmp: str, hook_text: str) -> None:
        self.tmp = tmp
        self.work = os.path.join(tmp, "work")
        self.remote = os.path.join(tmp, "remote.git")
        self.hooks = os.path.join(tmp, "hooks")
        os.makedirs(self.hooks)
        write(os.path.join(self.hooks, "pre-push"), hook_text, executable=True)

        run(["git", "init", "-q", "--bare", self.remote], cwd=tmp)
        run(["git", "init", "-q", self.work], cwd=tmp)
        for cfg in (["user.email", "t@t.test"], ["user.name", "t"], ["core.autocrlf", "false"],
                    ["commit.gpgsign", "false"],
                    ["core.hooksPath", self.hooks.replace("\\", "/")]):
            run(["git", "config"] + cfg, cwd=self.work)
        os.makedirs(os.path.join(self.work, "scripts", "run-gates"))
        # The DEFAULT bar, stubbed RED. Every accept case below has to get past this, so a case that
        # reports "accepted" is reporting that the named bar ran, not that no bar did.
        write(os.path.join(self.work, "scripts", "run-gates", "run-gates.sh"),
              '#!/usr/bin/env bash\necho "DEFAULT BAR RAN - RED"; exit 1\n')
        # A tracked bar, GREEN, so an accept case is visible by the bar's own text.
        write(os.path.join(self.work, "scripts", "unattended-bar.sh"),
              '#!/usr/bin/env bash\necho "TRACKED BAR RAN - GREEN"; exit 0\n')
        # A second tracked bar, GREEN and clean but NOT declared: the M1 shape, any cheap tracked
        # script that exits 0.
        write(os.path.join(self.work, "scripts", "other-bar.sh"),
              '#!/usr/bin/env bash\necho "OTHER BAR RAN"; exit 0\n')
        # THE DECLARATION the hook reads at the pushed sha (M1), in the unattended driver's own file.
        write(os.path.join(self.work, ".unattended.conf"), 'GATE_CMD="bash scripts/unattended-bar.sh"\n')
        write(os.path.join(self.work, "f.txt"), "hi\n")
        run(["git", "add", "-A"], cwd=self.work)
        run(["git", "commit", "-qm", "init"], cwd=self.work)
        run(["git", "branch", "-M", "main"], cwd=self.work)
        run(["git", "remote", "add", "origin", self.remote.replace("\\", "/")], cwd=self.work)
        # An untracked stub, by construction outside the repo: the shape every hook harness uses.
        self.untracked = os.path.join(tmp, "stub.sh").replace("\\", "/")
        write(self.untracked, '#!/usr/bin/env bash\necho "UNTRACKED STUB RAN"; exit 0\n')
        # A PATH command whose name is neither path-shaped nor *.sh. This is the rev-2 evasion.
        self.bindir = os.path.join(tmp, "bin")
        os.makedirs(self.bindir)
        # `x.pyc` is B1's second shape: a word an ignore rule would hide, sat after `sh`.
        for name in ("gatepayload", "x.pyc"):
            write(os.path.join(self.bindir, name),
                  '#!/usr/bin/env bash\necho "PAYLOAD RAN"; exit 0\n', executable=True)

    def read_tip(self) -> str:
        rc, out = run(["git", "--git-dir", self.remote, "rev-parse", "main"], cwd=self.tmp)
        return out.strip() if rc == 0 else ""

    def read_end(self) -> dict[str, str]:
        """The last END line of the push journal, as a key -> value map; empty when there is none."""
        path = os.path.join(self.work, ".git", "runlog", "pushes.log")
        if not os.path.isfile(path):
            return {}
        with open(path, encoding="utf-8", errors="replace") as fh:
            ends = [ln.rstrip("\n") for ln in fh if "\tev=end\t" in ln]
        if not ends:
            return {}
        return dict(part.partition("=")[::2] for part in ends[-1].split("\t"))

    def run_push(self, value: str | None, escape: bool = False) -> tuple[int, str, bool]:
        """One push. Returns (rc, combined output, did the remote move)."""
        run(["git", "commit", "-q", "--allow-empty", "-m", "c"], cwd=self.work)
        before = self.read_tip()
        rc, gd = run(["git", "rev-parse", "--git-dir"], cwd=self.work)
        marker = os.path.join(self.work, gd.strip(), "push-main-active")
        write(marker, "")
        env = {
            "GOV_DEFAULT_BRANCH": "main",
            "PATH": self.bindir + os.pathsep + os.environ.get("PATH", ""),
            "GOV_GATE_CMD": "" if value is None else value,
        }
        if escape:
            env["GOV_GATE_CMD_TEST"] = "1"
        rc, out = run(["git", "push", "origin", "HEAD:refs/heads/main"], cwd=self.work, env=env)
        moved = self.read_tip() != before
        if VERBOSE:
            print(f"    [{value!r} escape={escape}] rc={rc} moved={moved}\n"
                  + "\n".join("      " + ln for ln in out.splitlines()))
        return rc, out, moved


def check_refused(fx: Fixture, value: str, needle: str, label: str, forbid: str = "") -> None:
    rc, out, moved = fx.run_push(value)
    if moved or rc == 0:
        print_fail(f"{label} — the push LANDED over a bar the hook cannot vouch for")
        return
    if needle not in out:
        print_fail(f"{label} — refused, but not for the stated reason; wanted {needle!r}")
        return
    if forbid and forbid in out:
        print_fail(f"{label} — refused, but {forbid!r} still ran before the refusal")
        return
    print_ok(label)


def check_landed(fx: Fixture, value: str | None, needle: str, label: str,
                 escape: bool = False) -> None:
    rc, out, moved = fx.run_push(value, escape=escape)
    if not moved:
        print_fail(f"{label} — a legitimate bar was REFUSED, so every refusal case proves only "
                   f"that the hook refuses everything: {out.strip()[:300]}")
        return
    if needle not in out:
        print_fail(f"{label} — landed, but the evidence line did not carry {needle!r}")
        return
    print_ok(label)


def check_end(fx: Fixture, key: str, want: str, label: str) -> None:
    got = fx.read_end().get(key, "<absent>")
    if got == want:
        print_ok(label)
    else:
        print_fail(f"{label} — the last run-log END carries {key}={got}, wanted {want}")


def check_positional_and_declared(fx: Fixture) -> None:
    """Closing review round 1 B1 and M1: what sits after the interpreter, and which value is declared."""
    # 9 — B1: a bare word BETWEEN the interpreter and the tracked script is what bash runs, off PATH.
    check_refused(fx, "bash gatepayload scripts/unattended-bar.sh", "would RUN 'gatepayload'",
                  "9 a PATH command after the interpreter is refused", forbid="PAYLOAD RAN")
    # 10 — B1's second shape, under `sh`.
    check_refused(fx, "sh x.pyc scripts/unattended-bar.sh", "would RUN 'x.pyc'",
                  "10 a bare word after `sh` is refused", forbid="PAYLOAD RAN")
    # 11 — M1: tracked, clean, green and undeclared. Every rev-3 arm passed it.
    check_refused(fx, "bash scripts/other-bar.sh", "neither this kit's own runner",
                  "11 a tracked bar that .unattended.conf does not declare is refused",
                  forbid="OTHER BAR RAN")


def main() -> int:
    if not os.path.isfile(HOOK):
        print(f"pre-push-bar selftest: {HOOK} is missing")
        return 2
    with open(HOOK, encoding="utf-8") as fh:
        hook_text = fh.read()

    untracked_reason = "does not track"
    print("pre-push-bar selftest — the hook as tracked:")
    tmp = tempfile.mkdtemp()
    try:
        fx = Fixture(tmp, hook_text)
        # 0 — THE NON-VACUITY CONTROL FIRST. With no GOV_GATE_CMD the default bar runs and it is
        #     RED, so the fixture is one where a real bar decides the push.
        rc, out, moved = fx.run_push(None)
        if moved or "DEFAULT BAR RAN - RED" not in out:
            print_fail("0 control — the default RED bar did not decide this fixture's pushes, so "
                       f"every case below is about something else: {out.strip()[:300]}")
        else:
            print_ok("0 control — the default bar runs and a RED one blocks the push")
        check_end(fx, "bar", "default", "0b the run log records the default bar as `bar=default`")
        # 1 — a tracked bar, no escape, is ACCEPTED. Without this the rest is an outage, not a gate.
        check_landed(fx, "bash scripts/unattended-bar.sh",
                     "bar: bash scripts/unattended-bar.sh",
                     "1 control — a TRACKED, unmodified bar is accepted and named in the decision line")
        check_end(fx, "bar", "tracked", "1b the run log records a vetted bar as `bar=tracked`")
        check_end(fx, "bar_path", "scripts/unattended-bar.sh",
                  "1c and names the script it vetted as `bar_path`")
        # 2 — a value naming no script at all.
        check_refused(fx, "true", "names no script at all",
                      "2 'true' is refused — a no-op bar names nothing")
        check_end(fx, "decision", "refuse-bar", "2b the refusal is recorded as `decision=refuse-bar`")
        # 3 — an untracked script (rev-1's defect).
        check_refused(fx, f"bash {fx.untracked}", untracked_reason,
                      "3 an UNTRACKED bar is refused", forbid="UNTRACKED STUB RAN")
        # 4 — a tracked name TRAILING an untracked one (rev-2's fix, kept honest).
        check_refused(fx, f"bash {fx.untracked} scripts/unattended-bar.sh", untracked_reason,
                      "4 an untracked token is refused even when a tracked one follows it",
                      forbid="UNTRACKED STUB RAN")
        # 5 — rev-3: a PATH command prepended to a tracked name. rev-2 LANDED this.
        check_refused(fx, "gatepayload scripts/unattended-bar.sh", "would RUN 'gatepayload'",
                      "5 a PATH command prepended to a tracked bar is refused", forbid="PAYLOAD RAN")
        # 6 — rev-3: the same evasion through the interpreter's own -c.
        check_refused(fx, "bash -c gatepayload scripts/unattended-bar.sh", "passes '-c'",
                      "6 an interpreter option before the script is refused", forbid="PAYLOAD RAN")
        # 7 — rev-3: tracked by NAME, rewritten in the working tree. rev-2 LANDED this.
        write(os.path.join(fx.work, "scripts", "unattended-bar.sh"),
              '#!/usr/bin/env bash\necho "DIRTY WORKING COPY RAN"; exit 0\n')
        check_refused(fx, "bash scripts/unattended-bar.sh", "whose working copy differs",
                      "7 a tracked bar whose working copy was rewritten is refused",
                      forbid="DIRTY WORKING COPY RAN")
        # Restore by rewriting the bytes, not by asking git to: the tracked content is one literal
        # and re-writing it keeps this harness free of any working-tree-discarding git command.
        write(os.path.join(fx.work, "scripts", "unattended-bar.sh"),
              '#!/usr/bin/env bash\necho "TRACKED BAR RAN - GREEN"; exit 0\n')
        # 8 — the declared escape waives all of it AND says so. A silent waiver is the defect
        #     wearing a test's name.
        check_landed(fx, f"bash {fx.untracked}", "bar: STUB ",
                     "8 under GOV_GATE_CMD_TEST the stub is allowed and the line marks it STUB",
                     escape=True)
        check_end(fx, "bar", "stub", "8b the run log records the waived bar as `bar=stub`")
        check_positional_and_declared(fx)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # --- THE MUTATION. Disable the three rev-3 arms and require the three hostile values to LAND.
    print("pre-push-bar selftest — the same hook with the rev-3 arms disabled (observed RED):")
    if hook_text.count(ANCHOR) != 1:
        print_fail("M0 — the mutation anchor 'set +f' was not found exactly once in "
                   ".githooks/pre-push, so this harness cannot disable the arms it claims to test. "
                   "That is a refusal, not a skip: an unmutatable guard is one whose failing case "
                   "nobody has observed.")
        return print_report()
    mutated = hook_text.replace(ANCHOR, ANCHOR + NEUTER, 1)
    tmp = tempfile.mkdtemp()
    try:
        fx = Fixture(tmp, mutated)
        for value, label, evidence in (
            ("gatepayload scripts/unattended-bar.sh",
             "M1 without the first-word arm the PATH payload LANDS", "PAYLOAD RAN"),
            ("bash -c gatepayload scripts/unattended-bar.sh",
             "M2 without the option arm the -c payload LANDS", "PAYLOAD RAN"),
            ("bash gatepayload scripts/unattended-bar.sh",
             "M4 without the executed-word arm the payload after the interpreter LANDS", "PAYLOAD RAN"),
            ("bash scripts/other-bar.sh",
             "M5 without the declared arm an undeclared tracked bar LANDS", "OTHER BAR RAN"),
        ):
            rc, out, moved = fx.run_push(value)
            if moved and evidence in out:
                print_ok(label)
            else:
                print_fail(f"{label} — but it did NOT land, so cases 5, 6, 9 and 11 may be passing for "
                           f"some other reason and the arm they name is unproven: {out.strip()[:300]}")
        write(os.path.join(fx.work, "scripts", "unattended-bar.sh"),
              '#!/usr/bin/env bash\necho "DIRTY WORKING COPY RAN"; exit 0\n')
        rc, out, moved = fx.run_push("bash scripts/unattended-bar.sh")
        if moved and "DIRTY WORKING COPY RAN" in out:
            print_ok("M3 without the working-copy arm the rewritten bar LANDS")
        else:
            print_fail("M3 the rewritten working copy did not land under mutation, so case 7 is "
                       f"unproven: {out.strip()[:300]}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    return print_report()


def print_report() -> int:
    n = COUNT[0]
    if n < FLOOR_ASSERTIONS:
        FAILURES.append(f"{n} assertions ran, under the floor of {FLOOR_ASSERTIONS}")
        print(f"  FAIL — {n} assertions ran, under the floor of {FLOOR_ASSERTIONS}: a case stopped asserting")
    if FAILURES:
        print(f"pre-push-bar selftest: FAILURES ({len(FAILURES)}), {n} assertions")
        return 1
    print(f"PASS ({n} assertions)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
