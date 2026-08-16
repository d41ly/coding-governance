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

import json
import os
import pathlib
import re as _re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent


def govkit_steps() -> tuple:
    """The engine's OWN step tuple, imported rather than restated.

    A second copy of this vocabulary in the harness is the two-spellings class inside the arm that
    exists to grade it: the harness would keep passing against its own idea of the order.
    """
    sys.path.insert(0, str(HERE))
    import govkit  # noqa: E402
    return govkit.STEPS
GOVKIT = HERE / "govkit.py"
FAILURES: list[str] = []


def run(*args: str, cwd: pathlib.Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(GOVKIT), *args],
        capture_output=True, text=True, cwd=str(cwd) if cwd else None,
    )


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
        check("plan emits no path still carrying a brace",
              "{playbook_path}" not in "".join(
                  l for l in p.stdout.splitlines() if l.strip().startswith("write")),
              p.stdout)

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
        # The receipt carries a ROW, because a kit the receipt claims with NO rows is the separate
        # `not-landed` state and check reports that and stops — the hole loop is unreachable there.
        # Before unit 1 this fixture used an empty file list, so the arm graded hole behaviour on a
        # receipt shape no apply can produce.
        (full / ".governance" / "install.json").write_text(
            json.dumps({"schema": 2, "gov_source": "local", "kits": ["memory-tree"],
                        "files": [{"path": "tools/memory-tree/check-memory-hygiene.sh",
                                   "role": "engine", "kit": "memory-tree", "written": True}]},
                       indent=2),
            encoding="utf-8", newline="\n")
        (full / ".memory-tree.conf").write_text('MEMORY_ROOT=memory\n', encoding="utf-8", newline="\n")
        p = run("check", "--target", str(full))
        check("check reds on an undischarged hole", p.returncode == 1, p.stdout + p.stderr)
        check("check names the hole and calls it UNDISCHARGED",
              "measured-pins' is UNDISCHARGED" in p.stdout, p.stdout)
        check("check reports a per-kit state line",
              "govkit check — memory-tree:" in p.stdout, p.stdout)

        # --- unit 1 AC8: a kit the receipt CLAIMS with zero rows, while its descriptor declares a
        # --- landable rule, is `not-landed` — a per-KIT verdict. The whole-target verdict it replaces
        # --- early-returned on an ABSENT receipt, so this state had no way to be reported at all.
        (full / ".governance" / "install.json").write_text(
            json.dumps({"schema": 2, "gov_source": "local", "kits": ["memory-tree"], "files": []},
                       indent=2),
            encoding="utf-8", newline="\n")
        p = run("check", "--target", str(full))
        check("a claimed kit with zero receipt rows is reported not-landed",
              "memory-tree: not-landed" in p.stdout, p.stdout)
        check("and it is a finding, not a state printed at exit 0", p.returncode == 1, p.stdout)

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
              "gate-runner and CI legs: SKIPPED" in p.stdout, p.stdout)

        # --- unit 1 AC9: the phase lines carry their reserved step id, and the ids appear in TUPLE
        # --- order. The ordering claim is over the ids this run prints and NOTHING else: all four
        # --- clauses of the contract's hard-order criterion stay vacuous until the baseline, the
        # --- attributes phase and the emitter exist.

        seen = [m.group(1) for m in _re.finditer(r"— \[\d+/([A-Z]+)\]", p.stdout)]
        check("apply's phase lines carry reserved step ids", bool(seen), p.stdout)
        check("the step ids appear in the tuple's order",
              seen == sorted(seen, key=lambda s: govkit_steps().index(s)), str(seen))
        check("every printed step id is IN the reserved tuple",
              all(s in govkit_steps() for s in seen), str(seen))

        rec1 = json.loads((ap / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("the receipt declares its schema", rec1.get("schema") == 2, str(rec1.get("schema")))
        check("every receipt row carries the kit version resolved at install",
              all("version" in f for f in rec1["files"]), "")

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
              {(f["path"], f.get("sha256")) for f in rec1["files"]} ==
              {(f["path"], f.get("sha256")) for f in rec2["files"]}, "")

        # ===== unit 1: the truthful core =====
        # AC1 — the carve-out. codebase-map declares a `**` engine glob, a project-owned carve-out
        # over gov's FILLED extractors, and a seed rule writing the TEMPLATE to the same destination.
        # Before precedence existed, gov's filled module landed byte-identical in the target and the
        # receipt called it `engine`. The arm asserts the BYTES, not just the role: a role that is
        # right about the wrong file is the failure this replaces.
        cm = make_target(tmp / "u1a", DEPLOY_FULL)
        p = run("apply", "--target", str(cm), "--kits", "codebase-map")
        rec = json.loads((cm / ".governance" / "install.json").read_text(encoding="utf-8"))
        govroot = HERE.parents[1]
        idx_of = lambda q: subprocess.run(["git", "-C", str(govroot), "show", f"HEAD:{q}"],
                                          capture_output=True).stdout
        landed = (cm / "tools" / "codebase-map" / "map_extractors.py").read_bytes()
        check("the carved destination carries the TEMPLATE's bytes",
              landed == idx_of("tools/codebase-map/map_extractors.template.py"), "")
        check("and NOT gov's own filled module — the measured data-loss path",
              landed != idx_of("tools/codebase-map/map_extractors.py"), "")
        rows = {f["path"]: f for f in rec["files"]}
        check("its winning row is the seed, sourced from the template",
              rows["tools/codebase-map/map_extractors.py"]["role"] == "seed" and
              rows["tools/codebase-map/map_extractors.py"]["source"].endswith("template.py"),
              str(rows.get("tools/codebase-map/map_extractors.py")))
        check("gov's filled module is recorded as project-owned and NOT written",
              any(f["role"] == "project-owned" and f.get("written") is False
                  and f["source"] == "tools/codebase-map/map_extractors.py"
                  for f in rec["files"]), "")

        # AC1b — a `seed` the target has since edited survives a re-apply, and the receipt row for it
        # is still there. The row surviving is the half that used to fail: serializing the receipt
        # from the write log dropped every seed row on the second run.
        (cm / "tools" / "codebase-map" / "map_extractors.py").write_bytes(b"# TARGET EDITED\n")
        p = run("apply", "--target", str(cm), "--kits", "codebase-map")
        check("a re-apply leaves an edited seed byte-identical",
              (cm / "tools" / "codebase-map" / "map_extractors.py").read_bytes()
              == b"# TARGET EDITED\n", "")
        rec2b = json.loads((cm / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("and its receipt row SURVIVES the re-apply",
              any(f["path"].endswith("codebase-map/map_extractors.py") and f["role"] == "seed"
                  for f in rec2b["files"]), "")
        check("the row count did not shrink between the two applies",
              len(rec["files"]) == len(rec2b["files"]),
              f"{len(rec['files'])} -> {len(rec2b['files'])}")

        # AC2b — the carve-out's own arm, on a SCRATCH descriptor. MEASURED: resolving either shipped
        # carve-out descriptor with and without its project-owned rule yields an identical writes map,
        # because destination last-wins already elects the seed template. So on gov's tree this arm
        # has no red state at all, and a fixture built from a real descriptor would pass by finding
        # nothing — inside the arm written to close the data-loss path.
        sys.path.insert(0, str(HERE))
        import govkit as _G
        _root = _G.repo_root()
        CARVED = {"id": "scratch", "home": "tools/memory-tree", "files": [
            {"include": "**", "role": "engine"},
            {"include": ["corpus_ids.py"], "role": "project-owned"},
        ]}
        with_co = _G.resolve_entry(_root, CARVED, _G.canonical_ctx("scratch"))
        bare = dict(CARVED, files=[CARVED["files"][0]])
        without = _G.resolve_entry(_root, bare, _G.canonical_ctx("scratch"))
        dest = "tools/scratch/corpus_ids.py"
        check("a carved source whose destination no later rule reaches is NOT written",
              dest not in with_co["writes"], str(sorted(with_co["writes"])[:3]))
        check("LIVENESS: without the carve-out the same destination IS written",
              dest in without["writes"], str(sorted(without["writes"])[:3]))
        check("the carve-out is recorded as an unlanded row rather than vanishing",
              any(u["dest"] == dest and u["role"] == "project-owned"
                  for u in with_co["unlanded"]), "")

        # AC2 — the precedence note reports BOTH figures. Zero carve-outs-that-change is the true
        # state of gov today and must NOT red; hiding it behind a single number is what let the first
        # fold claim a byte-level effect the resolver does not have.
        ps = run("selfcheck")
        check("selfcheck's precedence note reports carve-outs declared AND how many change a write",
              "carve-out source(s) declared, of which" in ps.stdout, ps.stdout)
        check("and reporting zero of them changing a write does not red",
              ps.returncode == 0, ps.stdout + ps.stderr)

        # AC5 — no rule leaves the land loop without a line. The silent skip this replaces swallowed
        # every rendered, project-owned and generated rule in the tree.
        check("an unlanded rule prints its role, its destination and who does produce it",
              "not landed [project-owned]" in p.stdout and
              "gov supplies no bytes for this source, ever" in p.stdout, p.stdout)

        # AC4 — plan promises exactly the file set gov owns. NOT keyed on `written`: that flag is a
        # per-RUN fact, and on a re-apply a seed that exists is a row gov owns and did not write.
        pl = run("plan", "--target", str(cm), "--kits", "codebase-map")
        plan_writes, plan_skips = set(), set()
        for line in pl.stdout.splitlines():
            m = _re.match(r"^  (write|SKIP)\s+\[[^\]]+\]\s+(\S+)", line)
            if m:
                (plan_writes if m.group(1) == "write" else plan_skips).add(m.group(2))
        check("plan's write set equals the receipt rows carrying gov bytes",
              plan_writes == {f["path"] for f in rec2b["files"] if "sha256" in f},
              str(sorted(plan_writes ^ {f["path"] for f in rec2b["files"] if "sha256" in f})))
        check("plan's SKIP set equals the rows carrying none",
              plan_skips == {f["path"] for f in rec2b["files"] if "sha256" not in f},
              str(sorted(plan_skips ^ {f["path"] for f in rec2b["files"] if "sha256" not in f})))
        check("the fixture actually HAS an unlandable role, or the SKIP half is vacuous",
              len(plan_skips) > 0, str(plan_skips))

        # AC10 — the playbook lands BYTES. It sits first in the default selection and, tagged
        # project-owned, landed nothing at all while its placeholder hole probed two absent paths.
        pb = make_target(tmp / "u1b", DEPLOY_FULL)
        run("apply", "--target", str(pb), "--kits", "playbook")
        recpb = json.loads((pb / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("the playbook entry lands its two files",
              (pb / "docs" / "PARALLEL.md").is_file()
              and (pb / "docs" / "parallel-coding-governance.domain-rules.md").is_file(),
              str(sorted(q.as_posix() for q in pb.rglob("docs/*"))))
        check("recorded as seed, which is the role whose re-apply contract is never-rewritten",
              all(f["role"] == "seed" for f in recpb["files"]), str(recpb["files"]))

        # AC7 — three distinct strings for three distinct measurements. A kit declaring a reason is
        # `landed-unmeasured` and says why; before this, one string covered "nothing was measured"
        # and "measured and broken" alike.
        pc = run("check", "--target", str(pb))
        check("a declared-absence kit reports landed-unmeasured", "landed-unmeasured" in pc.stdout,
              pc.stdout)
        check("and prints the declared reason rather than the bare state",
              "installation is a copy to an owner-chosen path" in pc.stdout, pc.stdout)

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

    print()
    if FAILURES:
        print(f"govkit-selftest: {len(FAILURES)} FAILED — {', '.join(FAILURES)}")
        return 1
    print("govkit-selftest: all arms held")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
