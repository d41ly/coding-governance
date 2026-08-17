#!/usr/bin/env python3
"""govkit selftest — every refusal and every reported state, exercised in throwaway repos.

Contract: the deployer unit's spec under memory/builds/aSealedCaravan/spec/

WHY THIS FILE EXISTS AT ALL. `check-arms.py`'s population is tracked `*.sh`, so nothing in this repo
demands arms from a Python write path — the unit resolved that deliberately and moved the guarantee
to the test layer instead. This is that layer. Each arm asserts a SPECIFIC message or on-disk effect,
never an exit code alone: an exit code shared by six unrelated outcomes is the exact ambiguity the
descriptors' outcome probes exist to resolve, and a test that accepted one would be reproducing it.

Every fixture is a throwaway repo under `mktemp`-equivalent. Nothing is written into this repo.
"""

from __future__ import annotations

import importlib.util
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
GOVKIT = HERE / "govkit.py"
FAILURES: list[str] = []


def run(*args: str, cwd: pathlib.Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(GOVKIT), *args],
        capture_output=True, text=True, cwd=str(cwd) if cwd else None,
    )


def _extract_plan_rows(out: str) -> list[tuple[str, str]]:
    """`(mark, destination)` for every row `plan` printed. ONE parser, so an arm comparing sets and
    an arm counting marks cannot disagree about what a row is."""
    rows = []
    for ln in out.splitlines():
        if "]" not in ln or "<-" not in ln or not ln.startswith("  "):
            continue
        mark = ln[2:].split("[", 1)[0].strip()
        dest = ln.split("]", 1)[1].split("<-")[0].strip()
        rows.append((mark, dest))
    return rows


def extract_plan_writes(out: str) -> set[str]:
    """The destinations `plan` promised govkit would WRITE. No role filter — that filter existed
    only because a non-landable row used to be marked `write`."""
    return {d for m, d in _extract_plan_rows(out) if m == "write"}


def measure_plan_marks(out: str) -> dict[str, int]:
    """Rows per `MARK|role` pair.

    KEYED ON THE PAIR, not on the mark. A mark-only tally is not a per-role assertion and is not even
    STABLE: `ORDER` covers the hole rows, the machine-scoped link rule, and the `project-owned` file
    rules, so the total moves with which answers a descriptor happens to supply — the first cut of
    this helper counted 2 against a descriptor missing `user_skills` and 3 against one that had it.
    """
    n: dict[str, int] = {}
    for ln in out.splitlines():
        if "]" not in ln or "<-" not in ln or not ln.startswith("  "):
            continue
        mark = ln[2:].split("[", 1)[0].strip()
        role = ln.split("[", 1)[1].split("]", 1)[0].strip()
        n[f"{mark}|{role}"] = n.get(f"{mark}|{role}", 0) + 1
    return n


def check(label: str, cond: bool, detail: str = "") -> None:
    if cond:
        print(f"ok   {label}")
    else:
        FAILURES.append(label)
        print(f"FAIL {label}{(' — ' + detail) if detail else ''}")


def git(cwd: pathlib.Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, check=False)


def make_target(tmp: pathlib.Path, deploy: str | None) -> pathlib.Path:
    t = tmp / "target"
    t.mkdir(parents=True, exist_ok=True)
    git(t, "init", "-q", "-b", "main")
    git(t, "config", "user.email", "t@e")
    git(t, "config", "user.name", "t")
    (t / "README.md").write_text("target\n", encoding="utf-8")
    if deploy is not None:
        gov = t / ".governance"
        gov.mkdir(exist_ok=True)
        (gov / "deploy.toml").write_text(deploy, encoding="utf-8", newline="\n")
    git(t, "add", "-A")
    git(t, "commit", "-qm", "base")
    return t


DEPLOY_FULL = """gov_source = "local"
prefix = "tools"
kits = ["memory-tree"]

[answers]
memory_root = "memory"
playbook_path = "docs/PARALLEL.md"
playbook_dir = "docs"
manifest_path = "docs/SESSION-KICKOFF.md"
user_skills = "~/.claude/skills"
"""

DEPLOY_NO_ANSWERS = """gov_source = "local"
prefix = "tools"
kits = ["playbook"]
"""


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)

        # --- selfcheck runs green in this repo. The positive arm: without it, every negative arm
        # --- below could pass because the tool is broken rather than because the input is bad.
        p = run("selfcheck")
        check("selfcheck exits 0 over this repo", p.returncode == 0, p.stdout + p.stderr)
        check("selfcheck reports a derived surface count rather than a spelled one",
              "surface " in p.stdout and "unclaimed" in p.stdout, p.stdout)

        # --- plan refuses without a target, and NAMES why rather than defaulting to the cwd.
        p = run("plan")
        check("plan refuses with no --target", p.returncode == 2)
        check("plan's refusal names the cwd-defaulting hazard",
              "Refusing to default it to the process cwd" in p.stderr, p.stderr)

        # --- plan refuses a target that is not a repository.
        notrepo = tmp / "notrepo"
        notrepo.mkdir()
        p = run("plan", "--target", str(notrepo))
        check("plan refuses a non-repository target", p.returncode == 2)
        check("that refusal names the path", str(notrepo.name) in p.stderr, p.stderr)

        # --- plan refuses a target carrying no descriptor, and says who writes one.
        bare = make_target(tmp / "a", None)
        p = run("plan", "--target", str(bare))
        check("plan refuses a target with no deploy.toml", p.returncode == 2)
        check("that refusal refuses to GUESS an answer",
              "Refusing to guess" in p.stderr, p.stderr)

        # --- plan over a real descriptor lists writes and WRITES NOTHING. The on-disk effect is the
        # --- assertion: a read-only verb that leaves a byte behind is the whole risk of this verb.
        full = make_target(tmp / "b", DEPLOY_FULL)
        before = sorted(q.relative_to(full).as_posix() for q in full.rglob("*") if q.is_file())
        p = run("plan", "--target", str(full), "--kits", "memory-tree")
        after = sorted(q.relative_to(full).as_posix() for q in full.rglob("*") if q.is_file())
        check("plan exits 0 over a descriptor with the answers it needs", p.returncode == 0,
              p.stdout + p.stderr)
        check("plan wrote NOTHING into the target", before == after,
              f"{set(after) - set(before)}")
        check("plan says it wrote nothing", "NOTHING was written" in p.stdout, p.stdout)
        check("plan lists a rendered destination resolved from the answers",
              "memory/HYGIENE.md" in p.stdout, p.stdout)
        check("plan names the source commit its bytes would come from",
              "source commit" in p.stdout, p.stdout)
        check("plan lists an ORDER for every declared hole",
              ".governance/outbox/measured-pins.md" in p.stdout, p.stdout)

        # --- plan REFUSES when an answer a selected kit needs is absent, and NAMES THE KEY.
        # --- This is the arm that separates "refuses" from "refuses usefully".
        noans = make_target(tmp / "c", DEPLOY_NO_ANSWERS)
        p = run("plan", "--target", str(noans), "--kits", "playbook")
        check("plan reds when a needed answer is missing", p.returncode == 1, p.stdout)
        check("plan NAMES the missing answer key", "needs answer 'playbook_path'" in p.stdout,
              p.stdout)
        # Quantified over EVERY mark except UNRES., not over `write` alone. The `write`-only form was
        # written when a `project-owned` row was marked `write`; once those rows became ORDER it went
        # vacuously true over an empty line set — an arm that passes because its population emptied.
        check("plan emits no path still carrying a brace under any mark but UNRES.",
              not [d for m, d in _extract_plan_rows(p.stdout) if m != "UNRES." and "{" in d],
              str(_extract_plan_rows(p.stdout)))

        # --- --kits refuses an id that is not a registry entry.
        p = run("plan", "--target", str(full), "--kits", "not-a-kit")
        check("--kits refuses an unknown id", p.returncode == 2)
        check("that refusal says the population is the registry",
              "not a registry entry" in p.stderr, p.stderr)

        # --- check reports NOT LANDED rather than pretending, when no receipt exists.
        p = run("check", "--target", str(full))
        check("check on a target with no receipt exits non-zero", p.returncode != 0)
        check("check calls that state NOT LANDED by name", "NOT LANDED" in p.stdout, p.stdout)

        # --- check RUNS a hole's discharge probe and reds on an undischarged one. The fixture is
        # --- built so the probe genuinely CANNOT pass: memory-tree's measured pins are absent, which
        # --- is the state a fresh install leaves. An arm whose fixture cannot trigger the rule
        # --- passes and proves nothing, so this one is asserted on the message, not the code.
        (full / ".governance" / "install.json").write_text(
            json.dumps({"gov_source": "local", "kits": ["memory-tree"], "files": []}, indent=2),
            encoding="utf-8", newline="\n")
        (full / ".memory-tree.conf").write_text('MEMORY_ROOT=memory\n', encoding="utf-8", newline="\n")
        p = run("check", "--target", str(full))
        check("check reds on an undischarged hole", p.returncode == 1, p.stdout + p.stderr)
        check("check names the hole and calls it UNDISCHARGED",
              "measured-pins' is UNDISCHARGED" in p.stdout, p.stdout)
        check("check reports a per-kit state line",
              "govkit check — memory-tree:" in p.stdout, p.stdout)

        # --- a receipt naming a kit the registry does not carry is a refusal, not a skip.
        (full / ".governance" / "install.json").write_text(
            json.dumps({"kits": ["ghost-kit"], "files": []}, indent=2),
            encoding="utf-8", newline="\n")
        p = run("check", "--target", str(full))
        check("check reds on a receipt claiming an unknown kit", p.returncode == 1, p.stdout)
        check("that message names the kit", "claims kit 'ghost-kit'" in p.stdout, p.stdout)

        # ================= apply =================
        # `check-wiring` is the fixture kit on purpose: engine files, a flat destination, and NO
        # adopter, so these arms measure the LAND path rather than somebody else's adopter.
        ap = make_target(tmp / "d", DEPLOY_FULL)
        p = run("apply", "--target", str(ap), "--kits", "check-wiring")
        check("apply exits 0 over a clean target", p.returncode == 0, p.stdout + p.stderr)
        check("apply landed the flat destination its descriptor DECLARES, not a kit-relative default",
              (ap / "tools" / "check-wiring.sh").is_file(),
              str(sorted(q.as_posix() for q in (ap / "tools").rglob("*"))))
        check("apply wrote a receipt", (ap / ".governance" / "install.json").is_file())
        check("apply wrote the flat sums sidecar a target verifies with bash alone",
              (ap / ".governance" / "install.sums").is_file())
        check("apply STAGED what it wrote — every gate here reads the index",
              "tools/check-wiring.sh" in subprocess.run(
                  ["git", "-C", str(ap), "diff", "--cached", "--name-only"],
                  capture_output=True, text=True).stdout, "")
        check("apply reports the steps it could NOT perform rather than skipping silently",
              "SKIPPED (no writer exists yet; reported, not silent)" in p.stdout and
              "gate-runner and CI legs: SKIPPED" in p.stdout, p.stdout)

        rec1 = json.loads((ap / ".governance" / "install.json").read_text(encoding="utf-8"))

        # --- AC3 provenance: the bytes are the INDEX's at the recorded commit, not the working
        # --- tree's. Asserted by comparing against `git show`, which is the receipt's whole claim.
        f0 = rec1["files"][0]
        idx = subprocess.run(["git", "-C", str(HERE.parents[1]), "show",
                              f"{f0['commit']}:{f0['source']}"], capture_output=True).stdout
        check("a landed file's bytes equal the gov INDEX at the recorded commit",
              (ap / f0["path"]).read_bytes() == idx, f0["path"])

        # --- AC2 idempotency: path-and-hash over the receipt, not porcelain. The second run must be
        # --- ALLOWED — the unqualified refuse-a-kitted-repo predicate made this unreachable.
        p = run("apply", "--target", str(ap), "--kits", "check-wiring")
        check("a second apply is NOT refused — the receipt authorises it", p.returncode == 0,
              p.stdout + p.stderr)
        rec2 = json.loads((ap / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("apply twice changes no path and no hash",
              {(f["path"], f["sha256"]) for f in rec1["files"]} ==
              {(f["path"], f["sha256"]) for f in rec2["files"]}, "")

        # --- AC8 the POSITIVE half: a FOREIGN kit, one no receipt claims, refuses before writing.
        for_ = make_target(tmp / "e", DEPLOY_FULL)
        (for_ / "tools").mkdir(parents=True, exist_ok=True)
        (for_ / "tools" / "check-wiring.sh").write_text("KIT_CHECK_WIRING_VERSION=9.9\n",
                                                        encoding="utf-8")
        p = run("apply", "--target", str(for_), "--kits", "memory-tree")
        check("apply refuses a target already carrying a kit no receipt claims", p.returncode == 2)
        check("that refusal NAMES the kit and where it resolved",
              "check-wiring (at tools/check-wiring.sh)" in p.stderr, p.stderr)
        check("the refusal happened BEFORE any write",
              not (for_ / ".governance" / "install.json").exists(), "")

        # --- a `merged` rule refuses by name rather than half-landing.
        p = run("apply", "--target", str(make_target(tmp / "f", DEPLOY_FULL)),
                "--kits", "pytest-parallel-guardrails")
        check("apply refuses a merged rule it cannot honour", p.returncode == 1, p.stdout)
        check("that refusal says there is no seam to extend",
              "no seam to extend" in p.stdout, p.stdout)

        # --- deploying into gov itself is a stated non-goal, and is refused before anything.
        p = run("apply", "--target", str(HERE.parents[1]), "--kits", "check-wiring")
        check("apply refuses the gov checkout as its own target", p.returncode == 2)
        check("that refusal calls it a stated non-goal", "stated non-goal" in p.stderr, p.stderr)

        # --- --resume needs an install to resume.
        p = run("apply", "--target", str(make_target(tmp / "g", DEPLOY_FULL)),
                "--kits", "check-wiring", "--resume")
        check("--resume refuses with no receipt", p.returncode == 2)
        check("that refusal says there is no install to resume",
              "no install here to resume" in p.stderr, p.stderr)

        # ================= intake =================
        # AC12: given a prepared answer stream, intake writes a descriptor `apply` accepts with no
        # further prompting. The arm is the CHAIN, not the file: intake then apply, no hand editing.
        ik = make_target(tmp / "h", None)
        p = run("intake", "--target", str(ik), "--kits", "check-wiring")
        check("intake exits 0 when the selection needs no answers", p.returncode == 0,
              p.stdout + p.stderr)
        check("intake wrote the descriptor", (ik / ".governance" / "deploy.toml").is_file())
        p = run("apply", "--target", str(ik), "--kits", "check-wiring")
        check("apply accepts intake's descriptor with no further prompting", p.returncode == 0,
              p.stdout + p.stderr)

        # --- intake refuses to invent an answer, and NAMES the ones it wants.
        ik2 = make_target(tmp / "i", None)
        p = run("intake", "--target", str(ik2), "--kits", "playbook")
        check("intake refuses when an answer is missing", p.returncode == 2)
        check("intake names the missing answers", "playbook_path" in p.stderr, p.stderr)
        check("intake refuses to INVENT one", "Refusing to invent" in p.stderr, p.stderr)
        check("intake wrote nothing when it refused",
              not (ik2 / ".governance" / "deploy.toml").exists(), "")

        p = run("intake", "--target", str(ik2), "--kits", "playbook",
                "--answer", "playbook_path=docs/PARALLEL.md",
                "--answer", "playbook_dir=docs")
        check("intake accepts a prepared answer stream", p.returncode == 0, p.stdout + p.stderr)
        check("the descriptor records the answers",
              "playbook_path" in (ik2 / ".governance" / "deploy.toml").read_text(encoding="utf-8"))

        # --- intake will NOT silently rewrite a standing authorization.
        p = run("intake", "--target", str(ik2), "--kits", "playbook",
                "--answer", "playbook_path=x", "--answer", "playbook_dir=y")
        check("intake refuses to overwrite an existing descriptor", p.returncode == 2)
        check("that refusal calls it the standing authorization",
              "standing authorization" in p.stderr, p.stderr)

        # ================= liveness of the two derived assertions =================
        # An assertion that finds nothing on a clean tree is indistinguishable from one that CANNOT
        # find anything. These arms build a scratch gov tree — a copy of the engine plus a minimal
        # registry — and feed it input that MUST red. Without them, the two arms below would be the
        # repo's own `fixture-passes-by-finding-nothing` class living inside the tool that gates it.
        def scratch_gov(mutates: str, guard: str) -> pathlib.Path:
            g = tmp / f"gov{abs(hash((mutates, guard))) % 9999}"
            (g / "tools" / "govkit").mkdir(parents=True)
            (g / "tools" / "demo").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                '[selection]\ndefault = ["demo"]\n\n'
                '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n\n'
                '[[exempt]]\npath = "tools/gate-legs.json"\nwhy = "a gov-specific leg manifest"\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "demo" / "kit.toml").write_text(
                'id = "demo"\nhome = "tools/demo"\n'
                'version_from = { none = "fixture" }\n\n'
                '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                f'[adopt]\nargv = ["bash", "{{kit}}/adopt-demo.sh"]\nmutates_index = {mutates}\n',
                encoding="utf-8", newline="\n")
            # The adopter EXECUTES `git add`. A `git add` inside an echo would not count, which is
            # the distinction that made this assertion necessary in the first place.
            (g / "tools" / "demo" / "adopt-demo.sh").write_text(
                '#!/usr/bin/env bash\necho "  1. git add something && commit."\ngit add .\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "gate-legs.json").write_text(
                json.dumps([{"name": "demo", "argv": ["true"], "guard": [guard]}], indent=2) + "\n",
                encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "base")
            return g

        def run_in(g: pathlib.Path) -> subprocess.CompletedProcess:
            return subprocess.run([sys.executable, str(g / "tools" / "govkit" / "govkit.py"),
                                   "selfcheck"], capture_output=True, text=True)

        def run_in_gov(g: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
            return subprocess.run([sys.executable, str(g / "tools" / "govkit" / "govkit.py"), *args],
                                  capture_output=True, text=True)

        def build_scratch_gov_kit(tag: str, kit_toml: str) -> pathlib.Path:
            """A scratch gov tree carrying ONE `demo` entry whose descriptor the caller writes.

            The two conditions below have no exerciser in the shipped tree — no descriptor declares
            an unknown role, and none declares a `blocks_adopt` hole — so both would be branches
            asserted by nothing. A fixture is the difference between a guard and a claim.
            """
            g = tmp / f"govkit-{tag}"
            (g / "tools" / "govkit").mkdir(parents=True)
            (g / "tools" / "demo").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                '[selection]\ndefault = ["demo"]\n\n'
                '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "demo" / "kit.toml").write_text(kit_toml, encoding="utf-8", newline="\n")
            (g / "tools" / "demo" / "demo-rendered.md").write_text("x\n", encoding="utf-8",
                                                                   newline="\n")
            (g / "tools" / "demo" / "adopt-demo.sh").write_text(
                '#!/usr/bin/env bash\ntrue\n', encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "base")
            return g

        def build_scratch_gov_role(role: str) -> pathlib.Path:
            return build_scratch_gov_kit(f"role-{role}",
                                   'id = "demo"\nhome = "tools/demo"\n'
                                   'version_from = { none = "fixture" }\n\n'
                                   '[[files]]\ninclude = ["demo-rendered.md"]\n'
                                   f'role = "{role}"\n\n[adopt]\nargv = []\nmutates_index = false\n')

        def build_scratch_gov_hole() -> pathlib.Path:
            return build_scratch_gov_kit(
                "blocked-hole",
                'id = "demo"\nhome = "tools/demo"\n'
                'version_from = { none = "fixture" }\n\n'
                '[[files]]\ninclude = ["demo-rendered.md"]\nrole = "rendered"\n\n'
                '[adopt]\nargv = ["bash", "{kit}/adopt-demo.sh"]\nmutates_index = false\n\n'
                '[[hole]]\nid = "demo-hole"\nkind = "authoring"\nblocks_adopt = true\n'
                'blocks_gate = false\nwhy = "the fixture that arms the blocks_adopt branch"\n'
                'discharge = { command = ["true"] }\n')

        good = run_in(scratch_gov("true", "tools/demo/"))
        check("the scratch gov fixture is GREEN when both facts agree", good.returncode == 0,
              good.stdout + good.stderr)

        bad_m = run_in(scratch_gov("false", "tools/demo/"))
        check("mutates_index reds when the declared value is not the measured one",
              bad_m.returncode == 1 and "mutates_index" in bad_m.stdout, bad_m.stdout)
        check("that message says the declared value is not the measured one",
              "not the measured one" in bad_m.stdout, bad_m.stdout)

        bad_g = run_in(scratch_gov("true", "docs/nowhere/"))
        check("a guard in no declared class reds",
              bad_g.returncode == 1 and "declared classes" in bad_g.stdout, bad_g.stdout)
        check("that message says the taxonomy must partition its own input",
              "does not partition its own input" in bad_g.stdout, bad_g.stdout)

        # ---- a `**` rule must not claim what another rule owns (TOOL-dClosedLexicon-4) ----------
        # REPRODUCED before it was fixed: `apply` iterated file rules in order, and an
        # `include = "**"` engine rule pooled every tracked file under `home` and wrote each
        # unconditionally — so it reached a `project-owned` or `seed` path FIRST and a rule declared
        # later never got to protect its own file. An adopter's edit to `drift_signals.py` was
        # destroyed by every re-apply, silently, with the descriptor reading exactly as intended.
        with tempfile.TemporaryDirectory() as td3:
            tmp3 = pathlib.Path(td3)
            t = make_target(tmp3, None)
            run("intake", "--target", str(t), "--kits", "drift-audit")
            first = run("apply", "--target", str(t), "--kits", "drift-audit")
            owned = t / "tools" / "drift-audit" / "drift_signals.py"
            check("apply lands the kit at all", first.returncode == 0 and owned.is_file(),
                  first.stdout + first.stderr)

            # AC3 FIRST, and it is not ceremony: the cheapest way to pass the two arms below is to
            # stop landing files, so the coverage claim has to be pinned BEFORE the protection ones.
            first_receipt = json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8"))
            landed_before = sorted(p.name for p in (t / "tools" / "drift-audit").iterdir() if p.is_file())
            check("a ** rule still lands what nothing else claims — the template included",
                  "drift_signals.template.py" in landed_before and "drift_report.py" in landed_before,
                  str(landed_before))

            owned.write_text(owned.read_text(encoding="utf-8") + "\n# ADOPTER EDIT\n", encoding="utf-8")
            seeded = t / "tools" / "drift-audit" / "drift_signals.py"
            second = run("apply", "--target", str(t), "--kits", "drift-audit")
            # THE RE-APPLY MUST HAVE SUCCEEDED. Both protection arms are satisfied by an apply that
            # REFUSED and wrote nothing — "the edit survived" is trivially true when nothing ran —
            # so the exit code is asserted FIRST. Demonstrated by injecting a refusal and watching
            # the suite still print "all arms held".
            check("the re-apply actually ran", second.returncode == 0, second.stdout + second.stderr)
            check("a re-apply PRESERVES an adopter's edit to a project-owned/seeded file",
                  "ADOPTER EDIT" in seeded.read_text(encoding="utf-8"),
                  "the wildcard rule clobbered a path another rule owns")

            landed_after = sorted(p.name for p in (t / "tools" / "drift-audit").iterdir() if p.is_file())
            check("...and the re-apply still lands the same file set",
                  landed_after == landed_before, f"{landed_before} -> {landed_after}")

            # PLAN AND APPLY MUST DESCRIBE THE SAME WRITE, compared as SETS over a `**` kit.
            # `plan` used to resolve sources through `rule_sources()`, which skips every glob, so a
            # wildcard rule produced ZERO plan rows while apply landed every tracked file under
            # `home` — the operator approving a preview of a fraction of the install. Ten of this
            # repo's nineteen descriptors carry a `**` rule. A deployer whose preview disagrees with
            # its action is worse than one that simply does the wrong thing: the wrong thing is
            # visible, and this was not.
            # Compared against the FIRST receipt: a `seed` rule legitimately skips a destination the
            # target already has, so a re-apply's receipt is the wrong operand.
            # NO ROLE FILTER (TOOL-dClosedLexicon-13). This arm used to restrict itself to `engine`
            # and `seed`, because `plan` marked a non-landable row `write` while `apply` skipped it —
            # so the arm could not have been written any other way. That is now one predicate in both
            # verbs, and the filter is gone: a `write` row that apply does not land, from ANY role,
            # fails here.
            plan_out = run("plan", "--target", str(t), "--kits", "drift-audit")
            applied = {f["path"] for f in first_receipt.get("files", [])}
            check("plan's write set equals apply's receipt for a ** kit, NO role filter",
                  extract_plan_writes(plan_out.stdout) == applied,
                  f"planned-only={sorted(extract_plan_writes(plan_out.stdout) - applied)} "
                  f"applied-only={sorted(applied - extract_plan_writes(plan_out.stdout))}")

            # ...AND OVER THE DEFAULT SELECTION, which is the operand that matters to an operator who
            # types no `--kits`. The `**` kit alone cannot see a divergence that lives in the roles.
            t2 = make_target(tmp3 / "dflt", DEPLOY_FULL)
            ap2 = run("apply", "--target", str(t2))
            check("apply over the DEFAULT selection ran", ap2.returncode == 0, ap2.stdout + ap2.stderr)
            rec2 = json.loads((t2 / ".governance" / "install.json").read_text(encoding="utf-8"))
            pl2 = run("plan", "--target", str(t2))
            check("plan's write set equals apply's receipt over the DEFAULT selection",
                  extract_plan_writes(pl2.stdout) == {f["path"] for f in rec2.get("files", [])},
                  f"planned-only={sorted(extract_plan_writes(pl2.stdout) - {f['path'] for f in rec2.get('files', [])})} "
                  f"applied-only={sorted({f['path'] for f in rec2.get('files', [])} - extract_plan_writes(pl2.stdout))}")

            # THE MAPPING, PINNED POSITIVELY AND PER ROLE. Set-equality above cannot express this:
            # an implementation emitting all seven non-landable rows under ONE mark satisfies it.
            # Counted from the descriptors: memory-tree 3 + memory-recall 1 rendered with adopters,
            # playbook 2 project-owned with no sibling writer, codebase-map 1 project-owned whose
            # sibling seed lands the same path.
            marks = measure_plan_marks(pl2.stdout)
            check("the default selection previews exactly 4 SIDE|rendered rows",
                  marks.get("SIDE|rendered") == 4, str(marks))
            check("...2 ORDER|project-owned rows, the playbook pair nothing produces",
                  marks.get("ORDER|project-owned") == 2, str(marks))
            check("...and 1 COVER|project-owned row, for the path a sibling seed writes",
                  marks.get("COVER|project-owned") == 1, str(marks))
            check("...and NO project-owned row is previewed as a write",
                  marks.get("write|project-owned") is None, str(marks))

            # A ROLE WITH NO PRODUCER IS AN ORDER, NOT A SIDE-EFFECT. Both entries say so themselves:
            # `review-harness` renders through the parity gate's --render, `check-install-prefix`
            # seeds an empty file. Neither declares an adopter, so `apply`'s CONFIGURE step runs
            # nothing for them and a SIDE mark would promise a producer that does not exist.
            for kit, dest in (("review-harness", "memory/guides/REVIEW-PROTOCOL.md"),
                              ("check-install-prefix", "tools/install-prefix-waivers.txt")):
                out = run("plan", "--target", str(t2), "--kits", kit).stdout
                row = next((l for l in out.splitlines() if dest in l), "")
                check(f"{kit}: a rendered/generated rule with NO adopter is an ORDER",
                      row.strip().startswith("ORDER"), row or out)

            # A `merged` rule is previewed as BLOCK, and apply refuses over it — the same divergence
            # in the other direction. `settings-merge` is the arm that matters: its merged rule
            # declares `include = []`, so a preview reading the source pool showed NOTHING while
            # apply refused.
            for kit, dest in (("push-main", ".githooks/pre-commit"),
                              ("settings-merge", ".claude/settings.json")):
                out = run("plan", "--target", str(t2), "--kits", kit).stdout
                row = next((l for l in out.splitlines() if l.strip().endswith(f"<- {kit}")
                            and dest in l), "")
                check(f"{kit}: a merged rule previews as BLOCK", row.strip().startswith("BLOCK"),
                      row or out)
                ap = run("apply", "--target", str(t2), "--kits", kit)
                check(f"{kit}: ...and apply refuses over it",
                      "no verb here can write a gov-owned region" in ap.stdout + ap.stderr,
                      ap.stdout + ap.stderr)

            # APPLY NAMES WHAT IT SKIPS. The aggregate `landed 0 file(s)` was the whole report.
            t3 = make_target(tmp3 / "skips", DEPLOY_FULL)
            sk = run("apply", "--target", str(t3), "--kits", "playbook")
            check("apply names each skipped rule, its role and its destination",
                  "SKIPPED [project-owned] docs/PARALLEL.md" in sk.stdout, sk.stdout)
            check("...and says why, in the same terms the preview used",
                  "the target or its operator must supply it" in sk.stdout, sk.stdout)

            # LANDABLE_ROLES IS DERIVED, and pinned against a literal so a table edit that changes
            # what lands cannot pass unremarked.
            spec = importlib.util.spec_from_file_location("govkit_mod", GOVKIT)
            gk = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(gk)
            check("LANDABLE_ROLES derives to exactly ('engine', 'seed')",
                  tuple(gk.LANDABLE_ROLES) == ("engine", "seed"), str(gk.LANDABLE_ROLES))
            check("every ROLE_KINDS value has a printable mark",
                  set(gk.ROLE_KINDS.values()) <= set(gk.KIND_MARKS), str(gk.KIND_MARKS))

            # AN UNKNOWN ROLE REFUSES rather than defaulting to `write`, in BOTH the read-only verb
            # and the registry check. The `blocks_adopt` half of the producer test has no shipped
            # exerciser, so it is armed HERE, on a fixture, rather than claimed.
            gov_bad = build_scratch_gov_role("no-such-role")
            bad_r = run_in_gov(gov_bad, "selfcheck")
            check("selfcheck refuses a role that is not in ROLE_KINDS",
                  bad_r.returncode == 1 and "not in ROLE_KINDS" in bad_r.stdout, bad_r.stdout)
            gov_blk = build_scratch_gov_hole()
            blk = run_in_gov(gov_blk, "plan", "--target", str(t2), "--kits", "demo")
            row = next((l for l in blk.stdout.splitlines() if "demo-rendered.md" in l), "")
            check("a rendered rule whose entry has a blocks_adopt hole is an ORDER",
                  row.strip().startswith("ORDER"), row or blk.stdout)

    print()
    if FAILURES:
        print(f"govkit-selftest: {len(FAILURES)} FAILED — {', '.join(FAILURES)}")
        return 1
    print("govkit-selftest: all arms held")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
