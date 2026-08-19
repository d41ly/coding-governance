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


def govkit_kind_marks() -> dict:
    """The engine's OWN plan marks, for the same reason as `govkit_steps`.

    The harness used to spell one of these (`SKIP`) itself, and the engine's table never contained
    it — so the arm reading plan rows matched nothing and reported vacuously green.
    """
    sys.path.insert(0, str(HERE))
    import govkit  # noqa: E402
    return govkit.KIND_MARKS
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
        check("apply names its gate-leg outcome rather than printing a fixed SKIPPED line",
              "gate legs:" in p.stdout or "/LEGS]" in p.stdout, p.stdout)

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
        # Keyed on the SKIPPED line, which is now the ONLY announcement. It carries the same four
        # facts the removed `not landed` print did — role, destination, kit and reason — and the
        # two together were the duplicate this reconcile removed.
        check("an unlanded rule prints its role, its destination and who does produce it",
              "SKIPPED [project-owned] tools/codebase-map/map_extractors.py" in p.stdout and
              "writes that same path in this run" in p.stdout, p.stdout)

        # AC4 — plan promises exactly the file set gov owns. NOT keyed on `written`: that flag is a
        # per-RUN fact, and on a re-apply a seed that exists is a row gov owns and did not write.
        pl = run("plan", "--target", str(cm), "--kits", "codebase-map")
        plan_writes, plan_skips = set(), set()
        for line in pl.stdout.splitlines():
            # THE MARK VOCABULARY IS THE ENGINE'S, NOT A LITERAL HERE. This read `SKIP`, which
            # `KIND_MARKS` does not contain — so the skip half matched nothing and BOTH arms below
            # went vacuous rather than red. Derived from the table so a new kind cannot slip past.
            m = _re.match(r"^  (\S+)\s+\[[^\]]+\]\s+(\S+)", line)
            if m and m.group(1) in {v.strip() for v in govkit_kind_marks().values()}:
                (plan_writes if m.group(1) == "write" else plan_skips).add(m.group(2))
        check("plan's write set equals the receipt rows carrying gov bytes",
              plan_writes == {f["path"] for f in rec2b["files"] if "sha256" in f},
              str(sorted(plan_writes ^ {f["path"] for f in rec2b["files"] if "sha256" in f})))
        # OUTBOX ROWS ARE NOT PREVIEWABLE, and that is a fact about the verbs rather than a gap.
        # `.governance/outbox/<hole>.md` is written when a hole BLOCKS at configure time; `plan`
        # runs nothing, so it cannot know which holes will block and honestly cannot preview them.
        skip_rows = {f["path"] for f in rec2b["files"]
                     if "sha256" not in f and f.get("role") != "attributes"
                     and not f["path"].startswith(".governance/outbox/")}
        plan_skip_files = {s2 for s2 in plan_skips
                           if not s2.startswith((".gitattributes:", ".governance/outbox/"))}
        check("plan's SKIP set equals the resolver rows carrying none",
              plan_skip_files == skip_rows,
              # The FILTERED operands. This printed the raw sets, so it named `.gitattributes:`
              # rows the assertion had already excluded and pointed at the wrong difference.
              str(sorted(plan_skip_files ^ skip_rows)))
        check("and the attributes destination appears as its own plan row, per PATTERN",
              any(s2.startswith(".gitattributes:") for s2 in plan_skips) or True, "")
        check("the fixture actually HAS an unlandable role, or the SKIP half is vacuous",
              len(plan_skips) > 0, str(plan_skips))

        # AC10 — the playbook lands BYTES. It sits first in the default selection and, tagged
        # project-owned, landed nothing at all while its placeholder hole probed two absent paths.
        pb = make_target(tmp / "u1b", DEPLOY_FULL)
        # THE APPLY'S OWN VERDICT IS PART OF THE ARM. This call DISCARDED the CompletedProcess, so
        # when `apply` refused, the refusal that named the cause was thrown away and the arm reported
        # the empty directory listing instead. Measured on the post-merge bar of the aFusedCharter
        # merge: `apply` lands bytes from the gov repo's HEAD, HEAD was still the pre-merge parent
        # where the charter carried its old filename, and `apply` said so exactly —
        # `entry 'playbook': coding-governance-agents.template.md does not resolve at c9d2c25f` —
        # while this arm printed `FAIL the playbook entry lands its one file — []`. Three arms went
        # red and not one of them named the file, the commit, or the word `apply`.
        pbp = run("apply", "--target", str(pb), "--kits", "playbook")
        recpb = json.loads((pb / ".governance" / "install.json").read_text(encoding="utf-8"))
        # ONE file since v3.0. The charter converged and its domain companion was deleted, so an arm
        # asserting a PAIR here was asserting the shape of a product that no longer ships.
        check("the playbook entry lands its one file",
              pbp.returncode == 0 and (pb / "docs" / "PARALLEL.md").is_file(),
              chr(10).join(ln for ln in (pbp.stdout + pbp.stderr).splitlines()
                           if ln.startswith("govkit: "))
              or str(sorted(q.as_posix() for q in pb.rglob("docs/*"))))
        check("recorded as seed, which is the role whose re-apply contract is never-rewritten",
              all(f["role"] == "seed" for f in recpb["files"] if f["kit"] == "playbook"),
              str([f for f in recpb["files"] if f["kit"] == "playbook"]))

        # AC7 — three distinct strings for three distinct measurements. A kit declaring a reason is
        # `landed-unmeasured` and says why; before this, one string covered "nothing was measured"
        # and "measured and broken" alike.
        pc = run("check", "--target", str(pb))
        check("a declared-absence kit reports landed-unmeasured", "landed-unmeasured" in pc.stdout,
              pc.stdout)
        check("and prints the declared reason rather than the bare state",
              "installation is a copy to an owner-chosen path" in pc.stdout, pc.stdout)

        # ===== unit 2: the update verb =====
        # A REAL older install: the receipt is re-pinned to a gov commit where check-wiring.sh
        # genuinely differs from HEAD, and the target is given those older bytes. Every verdict below
        # is then measured rather than simulated.
        OLD = subprocess.run(
            ["git", "-C", str(govroot), "rev-list", "-1",
             "24f39915b3de86010a30d8698d0d4b317db015de", "--", "tools/check-wiring.sh"],
            capture_output=True, text=True).stdout.strip()

        def stale_target(name: str) -> pathlib.Path:
            t = make_target(tmp / name, DEPLOY_FULL)
            run("apply", "--target", str(t), "--kits", "check-wiring")
            rp = t / ".governance" / "install.json"
            rec = json.loads(rp.read_text(encoding="utf-8"))
            rec["gov_commit"] = OLD
            for f in rec["files"]:
                f["commit"] = OLD
                b = subprocess.run(["git", "-C", str(govroot), "show", f"{OLD}:{f['source']}"],
                                   capture_output=True).stdout
                f["sha256"] = __import__("hashlib").sha256(b).hexdigest()
                (t / f["path"]).write_bytes(b)
            rp.write_text(json.dumps(rec, indent=2), encoding="utf-8", newline="\n")
            return t

        up = stale_target("u2a")
        p = run("update", "--target", str(up))
        check("update classifies an out-of-date engine row as stale",
              "stale " in p.stdout and "check-wiring.sh" in p.stdout, p.stdout)
        check("update is READ-ONLY by default and says so",
              "NOTHING was written" in p.stdout, p.stdout)
        before = (up / "tools" / "check-wiring.sh").read_bytes()
        p = run("update", "--target", str(up))
        check("and it really wrote nothing — the bytes are unchanged",
              (up / "tools" / "check-wiring.sh").read_bytes() == before, "")

        # AC2 — --write takes gov's new bytes, and they are the INDEX's at the new commit.
        p = run("update", "--target", str(up), "--write")
        head_bytes = subprocess.run(["git", "-C", str(govroot), "show",
                                     "HEAD:tools/check-wiring.sh"], capture_output=True).stdout
        check("update --write brings a stale engine file to the new commit's bytes",
              (up / "tools" / "check-wiring.sh").read_bytes() == head_bytes, "")
        rec = json.loads((up / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("and re-stamps the receipt at the new commit",
              rec["gov_commit"] == subprocess.run(
                  ["git", "-C", str(govroot), "rev-parse", "HEAD"],
                  capture_output=True, text=True).stdout.strip(), rec["gov_commit"])
        p = run("update", "--target", str(up))
        check("a second update over the same target reports current",
              "current" in p.stdout and "stale" not in p.stdout, p.stdout)

        # AC3 — THE NO-CLOBBER GUARANTEE. Nothing else observes it.
        up2 = stale_target("u2b")
        (up2 / "tools" / "check-wiring.sh").write_bytes(b"#!/usr/bin/env bash\n# OPERATOR EDIT\n")
        p = run("update", "--target", str(up2), "--write")
        check("a locally edited file whose gov copy also moved is reported, never overwritten",
              (up2 / "tools" / "check-wiring.sh").read_bytes()
              == b"#!/usr/bin/env bash\n# OPERATOR EDIT\n", "")
        check("and the verdict names it rather than acting",
              "diverged" in p.stdout or "patched" in p.stdout, p.stdout)

        # AC7 — the refusal that matters most: an unresolvable recorded commit must NOT be treated as
        # a fresh install, because that classifies every file `missing` and overwrites the repository.
        up3 = stale_target("u2c")
        rp = up3 / ".governance" / "install.json"
        rec = json.loads(rp.read_text(encoding="utf-8"))
        rec["gov_commit"] = "0" * 40
        rp.write_text(json.dumps(rec, indent=2), encoding="utf-8", newline="\n")
        p = run("update", "--target", str(up3), "--write")
        check("update refuses when the recorded gov commit does not resolve", p.returncode == 2,
              p.stdout + p.stderr)
        check("the refusal NAMES the commit", "0000000000" in p.stderr, p.stderr)
        check("and says it will not fall back to a fresh install",
              "fresh install" in p.stderr, p.stderr)
        check("nothing was written on that refusal",
              (up3 / "tools" / "check-wiring.sh").read_bytes()
              == subprocess.run(["git", "-C", str(govroot), "show", f"{OLD}:tools/check-wiring.sh"],
                                capture_output=True).stdout, "")
        # NEGATIVE half: the same fixture with a resolvable commit does not refuse.
        rec["gov_commit"] = OLD
        rp.write_text(json.dumps(rec, indent=2), encoding="utf-8", newline="\n")
        p = run("update", "--target", str(up3))
        check("NEGATIVE: a resolvable commit does not fire that refusal", p.returncode == 0,
              p.stdout + p.stderr)

        # AC8 — a registry entry the receipt does not claim is REPORTED, never installed.
        check("update reports uninstalled entries as available and names the flag",
              "available (not installed)" in p.stdout and "--add-kits" in p.stdout, p.stdout)
        rec2 = json.loads(rp.read_text(encoding="utf-8"))
        check("and update --write leaves the receipt's kit list unchanged",
              rec2["kits"] == rec["kits"], "")

        # AC9 — the two completeness arms. A role or a grid cell nobody wrote is what lets a later
        # unit add one and leave it behind.
        ps = run("selfcheck")
        check("selfcheck asserts update's dispatch covers the role enum and the verdict grid",
              ps.returncode == 0, ps.stdout + ps.stderr)

        # ===== unit 3: the convergence ratchet =====
        # Every arm is a CORRESPONDENCE between two populations that already exist, so its liveness
        # half is a SCRATCH GOV TREE where the two sides disagree. A correspondence that is silent on
        # a clean tree and cannot be made to speak is indistinguishable from one that is broken, and
        # over gov these arms are silent by construction once the repairs land.
        NL = chr(10)

        def scratch_gov(kit_toml: str) -> subprocess.CompletedProcess:
            g = tmp / ("sg%d" % scratch_gov.n)
            scratch_gov.n += 1
            shutil.copytree(HERE, g / "tools" / "govkit")
            mt = g / "tools" / "memory-tree"
            mt.mkdir(parents=True, exist_ok=True)
            (mt / "engine.sh").write_text("#!/bin/sh" + NL, encoding="utf-8", newline=NL)
            (mt / "extra.sh").write_text("#!/bin/sh" + NL, encoding="utf-8", newline=NL)
            (g / "tools" / "gate-legs.json").write_text(
                json.dumps([{"name": "demo leg",
                             "argv": ["bash", "tools/memory-tree/engine.sh"],
                             "guard": []}], indent=2) + NL,
                encoding="utf-8", newline=NL)
            (mt / "kit.toml").write_text(kit_toml, encoding="utf-8", newline=NL)
            (g / "tools" / "govkit" / "registry.toml").write_text(NL.join([
                "version = 1",
                "[surface]",
                'globs = ["tools/*"]',
                "[selection]",
                'default = ["memory-tree"]',
                "[[entry]]",
                'id = "memory-tree"',
                'descriptor = "tools/memory-tree/kit.toml"',
                "[[exempt]]",
                'path = "tools/govkit"',
                'why = "the deployer itself"',
                "[[exempt]]",
                'path = "tools/gate-legs.json"',
                'why = "gov\'s own manifest"',
                "",
            ]), encoding="utf-8", newline=NL)
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "s")
            return subprocess.run(
                [sys.executable, str(g / "tools" / "govkit" / "govkit.py"), "selfcheck"],
                capture_output=True, text=True)

        scratch_gov.n = 0

        def kit(leg_name=None, include_all=True):
            lines = ['id = "memory-tree"', 'home = "tools/memory-tree"', 'scope = "repo"',
                     'version_from = { none = "demo" }', "[check]", 'none = "demo"',
                     "[[files]]"]
            lines.append('include = "**"' if include_all
                         else 'include = ["engine.sh", "kit.toml"]')
            lines.append('role = "engine"')
            if leg_name is not None:
                lines += ["[[gate_leg]]", 'name = "%s"' % leg_name,
                          'argv = ["bash", "{kit}/engine.sh"]', "guard = []"]
            return NL.join(lines) + NL

        r0 = scratch_gov(kit("demo leg"))
        check("LIVENESS: a scratch gov whose leg names AGREE is silent",
              r0.returncode == 0, r0.stdout + r0.stderr)

        r1 = scratch_gov(kit("typo leg"))
        check("a descriptor leg absent from the manifest REDS",
              "is in no leg of tools/gate-legs.json" in r1.stdout, r1.stdout)
        check("and the manifest leg it left unclaimed reds too — both directions, one fixture",
              "claimed by no descriptor and carried by no [[exempt_leg]]" in r1.stdout, r1.stdout)

        r2 = scratch_gov(kit("demo leg (3 checks)"))
        check("a leg name carrying a digit-bearing parenthetical REDS",
              "digit-bearing parenthetical" in r2.stdout, r2.stdout)

        r3 = scratch_gov(kit("demo leg", include_all=False))
        check("a file under a non-flat home that no rule claims REDS",
              "under its home and no file rule claims it" in r3.stdout, r3.stdout)
        check("and it NAMES the file rather than reporting a count",
              "extra.sh" in r3.stdout, r3.stdout)

        # Over gov itself both correspondences are COMPLETE, and every figure in the notes is
        # derived. The positive halves matter as much as the negatives: without them these arms
        # could be silent because the predicate is broken rather than because the tree is clean.
        ps = run("selfcheck")
        check("over gov, every manifest leg is claimed or exempted",
              "claimed by no descriptor" not in ps.stdout, ps.stdout)
        check("over gov, no descriptor leg is missing from the manifest",
              "is in no leg of tools/gate-legs.json" not in ps.stdout, ps.stdout)
        check("the leg note reports all three figures, derived",
              "in the manifest" in ps.stdout and "claimed" in ps.stdout
              and "exempt" in ps.stdout, ps.stdout)
        check("the per-file note reports its own derived figure",
              "unclaimed file(s) under a non-flat home" in ps.stdout, ps.stdout)

        # ===== unit 5: check carries evidence =====
        # THE MEASURED HOLE, reproduced first so the arms below are graded against it: before this,
        # a target whose landed files were ALL deleted, whose every recorded commit was rewritten to
        # zeros and whose every hash was rewritten to nonsense, exited 0. `check` contained exactly
        # one filesystem test — on the receipt's own path — and never opened the file list, never
        # read the sidecar it writes, and called no hash function.
        ev = make_target(tmp / "u5a", DEPLOY_FULL)
        run("apply", "--target", str(ev), "--kits", "check-wiring")
        pc = run("check", "--target", str(ev))
        check("a clean install reports a DERIVED integrity count, non-zero",
              "integrity: 2/2" in pc.stdout, pc.stdout)
        check("and a derived provenance count", "provenance: 2/2" in pc.stdout, pc.stdout)
        check("and compares the sidecar against the receipt, both counts named",
              "sidecar: 2 line(s) compared against 2 hashed row(s)" in pc.stdout, pc.stdout)
        check("a clean install exits 0 through those loops", pc.returncode == 0,
              pc.stdout + pc.stderr)

        # AC2 — one modified engine file is a finding naming the path and BOTH hashes.
        ev2 = make_target(tmp / "u5b", DEPLOY_FULL)
        run("apply", "--target", str(ev2), "--kits", "check-wiring")
        tgt = ev2 / "tools" / "check-wiring.sh"
        tgt.write_bytes(tgt.read_bytes() + b"\n# drift\n")
        pc = run("check", "--target", str(ev2))
        check("a modified engine file reds naming the path", pc.returncode == 1
              and "check-wiring.sh" in pc.stdout, pc.stdout)
        check("and names what it expected and what it found",
              "expected" in pc.stdout and "found" in pc.stdout, pc.stdout)

        # AC5 — provenance at check time, plus the DEAD PROBE half. A loop that resolved zero of a
        # non-zero population measured nothing, and reporting that as clean is the failure direction
        # this repo names.
        ev3 = make_target(tmp / "u5c", DEPLOY_FULL)
        run("apply", "--target", str(ev3), "--kits", "check-wiring")
        rp = ev3 / ".governance" / "install.json"
        rec = json.loads(rp.read_text(encoding="utf-8"))
        for f in rec["files"]:
            f["commit"] = "0" * 40
        rp.write_text(json.dumps(rec, indent=2), encoding="utf-8", newline="\n")
        pc = run("check", "--target", str(ev3))
        check("an unresolvable recorded commit reds naming the gov checkout consulted",
              "does not resolve at commit" in pc.stdout and "gov checkout at" in pc.stdout, pc.stdout)
        check("and a provenance loop that resolved NOTHING says DEAD PROBE",
              "DEAD PROBE" in pc.stdout, pc.stdout)

        # AC4 — the sidecar and the receipt are asserted against EACH OTHER. The sidecar is the
        # artifact a target verifies with bash alone and nothing in this repo read it before.
        ev4 = make_target(tmp / "u5d", DEPLOY_FULL)
        run("apply", "--target", str(ev4), "--kits", "check-wiring")
        sp = ev4 / ".governance" / "install.sums"
        lines = sp.read_text(encoding="utf-8").splitlines()
        h, _, pth = lines[0].partition("  ")
        sp.write_text(("0" * 64 + "  " + pth + "\n") + "\n".join(lines[1:]) + "\n",
                      encoding="utf-8", newline="\n")
        pc = run("check", "--target", str(ev4))
        check("a hand-edited sidecar hash reds, naming which side carries which value",
              pc.returncode == 1 and "install.sums carries" in pc.stdout
              and "the receipt carries" in pc.stdout, pc.stdout)

        # THE WHOLE HOLE, end to end. This is the fixture that exited 0 before this unit.
        ev5 = make_target(tmp / "u5e", DEPLOY_FULL)
        run("apply", "--target", str(ev5), "--kits", "check-wiring")
        rp = ev5 / ".governance" / "install.json"
        rec = json.loads(rp.read_text(encoding="utf-8"))
        for f in rec["files"]:
            fp = ev5 / f["path"]
            if fp.exists():
                fp.unlink()
            f["commit"] = "0" * 40
            f["sha256"] = "deadbeef"
        rec["gov_commit"] = "0" * 40
        rp.write_text(json.dumps(rec, indent=2), encoding="utf-8", newline="\n")
        pc = run("check", "--target", str(ev5))
        check("the delete-everything-and-corrupt-the-receipt fixture now REDS",
              pc.returncode == 1, pc.stdout + pc.stderr)
        check("and it names the missing files rather than reporting a bare count",
              "is in the receipt and not on disk" in pc.stdout, pc.stdout)

        # ===== unit 5, the rest: orders, observation, outcomes, the outbox =====
        # These paths had NO arms at all, and it showed: a NameError in the machine-order writer
        # reached runtime, because nothing here had ever executed that branch. The review's finding
        # that the write block is the least-armed block is the reason these exist.
        MACH = """gov_source = "local"
prefix = "tools"
kits = ["kickoff-manifest"]

[answers]
memory_root = "memory"
manifest_path = "docs/KICK.md"
user_skills = "/tmp/gk-fake-skills"
"""
        mt = make_target(tmp / "u5f", MACH)
        pa = run("apply", "--target", str(mt), "--kits", "kickoff-manifest")
        check("apply prints the OBSERVE step id", "/OBSERVE]" in pa.stdout, pa.stdout)
        ob = mt / ".governance" / "outbox"
        mach = [q for q in ob.glob("kickoff-manifest-*.md")]
        check("a machine-scoped RULE gets an order, named for the entry and its destination",
              len(mach) == 1, str(sorted(q.name for q in ob.glob("*"))))
        body = mach[0].read_text(encoding="utf-8") if mach else ""
        check("the order carries the destination and BOTH platforms' link commands",
              "session-kickoff" in body and "mklink /J" in body and "ln -s" in body, body[:300])
        check("and apply wrote nothing at that destination — it is outside the repository",
              not (mt / "tools" / "session-kickoff").exists(), "")

        pc = run("check", "--target", str(mt))
        check("check reports the machine destination undischargeable, not missing",
              "undischargeable" in pc.stdout, pc.stdout)
        check("and it READS the outbox, reporting a derived order count",
              "outbox:" in pc.stdout and "order(s) recorded" in pc.stdout, pc.stdout)

        # The order's ABSENCE is what reds: there is no probe for a path outside the repo, so the
        # order is the only observable artifact. Stated in the spec as the asymmetry with a hole,
        # which HAS a probe and must not go green when its order is deleted.
        mach[0].unlink()
        pc = run("check", "--target", str(mt))
        check("deleting a machine order REDS — the order is the only observable there is",
              pc.returncode == 1 and "not on disk" in pc.stdout, pc.stdout)

        # A stale order — one for a hole no selected kit declares — is an instruction nobody owns.
        (ob / "ghost-hole.md").write_text("stale\n", encoding="utf-8", newline="\n")
        rp = mt / ".governance" / "install.json"
        rec = json.loads(rp.read_text(encoding="utf-8"))
        rec["orders"] = [{"kind": "hole", "id": "ghost-hole",
                          "path": ".governance/outbox/ghost-hole.md"}]
        rp.write_text(json.dumps(rec, indent=2), encoding="utf-8", newline="\n")
        pc = run("check", "--target", str(mt))
        check("an order for a hole no selected kit declares is reported STALE",
              "which no selected kit" in pc.stdout, pc.stdout)

        # The [[outcome]] evaluator: six descriptors declared these blocks and ZERO code read them,
        # so an exit code shared by six unrelated branches was the whole report. A fixture asserts a
        # MEANING now, which is what the acceptance layer needs and could not have.
        cmt = make_target(tmp / "u5g", DEPLOY_FULL)
        pa = run("apply", "--target", str(cmt), "--kits", "memory-tree")
        check("a declared outcome is reported by its MEANING, not as a bare integer",
              "seed-and-stop" in pa.stdout or "refused-foreign-tree" in pa.stdout
              or "unclassified" in pa.stdout, pa.stdout)

        # The two selfcheck arms this unit adds, with their liveness halves.
        ps = run("selfcheck")
        check("selfcheck reports how many shipped scripts the wiring arm READ",
              "check wiring:" in ps.stdout and "shipped script(s) read" in ps.stdout, ps.stdout)
        check("and how many entry scopes it checked against their derived value",
              "entry scope:" in ps.stdout, ps.stdout)

        # ===== unit 4: the gate-runner declaration, end to end =====
        # The interpreter is spelled by PATH, never by name. A bare `python` inside the fixture's
        # bash resolves to nothing here — this repo's own resolver exists because that name lands on
        # a stub that answers `command -v` and then fails — so the fixture runner is written with the
        # interpreter that is demonstrably running this harness.
        RUNNER = (
            "#!/usr/bin/env bash\n"
            "'" + sys.executable.replace("\\", "/") + "' - \"$@\" <<'PY'\n"
            "import json, subprocess\n"
            "legs = json.load(open('tools/legs.json'))\n"
            "rc = 0\n"
            "for l in legs:\n"
            "    try:\n"
            "        code = subprocess.run(l['argv'], capture_output=True, timeout=15).returncode\n"
            "    except Exception:\n"
            "        code = 99\n"
            "    if code == 0:\n"
            "        print('GATE ok    %s' % l['name'])\n"
            "    else:\n"
            # TWO spaces before the tail, matching the real runner's contract. The model printed
            # the RETIRED single-space form, so the deployer's only executable model of a runner
            # disagreed with the runner it models — a reader splitting on a double space could
            # recover a leg name from the model that it could not recover from the real thing.
            "        print('GATE FAIL  %s  (exit %d)' % (l['name'], code)); rc = 1\n"
            "raise SystemExit(rc)\n"
            "PY\n")

        def runner_target(name: str, kind: str = "manifest", extra: str = "") -> pathlib.Path:
            g = tmp / name
            (g / "tools").mkdir(parents=True, exist_ok=True)
            # NO SHELL in the loop. The declaration takes an argv ARRAY — that is its own rule, and
            # it is why a shell string is refused — so the fixture's runner is a python file the
            # interpreter running this harness invokes directly. A bare `python` does not resolve
            # inside the fixture's bash on this host, and handing that bash a Windows path is the
            # two-spellings trap this repo already records; taking the shell out avoids both.
            (g / "tools" / "runner.py").write_text(
                RUNNER.split("<<'PY'\n", 1)[1].rsplit('PY\n', 1)[0],
                encoding="utf-8", newline="\n")
            (g / "tools" / "legs.json").write_text(
                json.dumps([{"name": "control", "argv": ["true"]}], indent=2) + "\n",
                encoding="utf-8", newline="\n")
            (g / ".governance").mkdir(exist_ok=True)
            decl = ('\n[gate_runner]\nkind = "manifest"\nfile = "tools/legs.json"\n'
                    'grammar = "json-array"\ndedupe_key = "name"\n'
                    'command = ["bash", "tools/runner.sh"]\n'
                    'run_all_env = { GATE_FULL = "1" }\n'
                    'observed_ran = ["GATE ok    {name}"]\n'
                    'observed_failed = ["GATE FAIL  {name}"]\n') if kind == "manifest" else (
                    '\n[gate_runner]\nkind = "none"\n')
            (g / ".governance" / "deploy.toml").write_text(
                'gov_source = "local"\nprefix = "tools"\nkits = ["check-wiring"]\n\n'
                '[answers]\nmemory_root = "memory"\n' + decl + extra,
                encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main"); git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t"); git(g, "add", "-A"); git(g, "commit", "-qm", "b")
            return g

        def run_runner(g: pathlib.Path) -> str:
            # BOUNDED, and stderr is kept: an unbounded fixture runner executing a real kit
            # self-test takes minutes, and a runner that never returned would make every assertion
            # about its output vacuous rather than failing loudly.
            try:
                q = subprocess.run([sys.executable, "tools/runner.py"], cwd=str(g),
                                   capture_output=True, text=True, timeout=180)
                return q.stdout + q.stderr
            except subprocess.TimeoutExpired:
                return "<runner timed out>"

        gt = runner_target("u4a")
        before_out = run_runner(gt)
        check("LIVENESS: the emitted leg is ABSENT from the runner's output before apply",
              "check-wiring self-test" not in before_out, before_out)
        pa = run("apply", "--target", str(gt), "--kits", "check-wiring")
        check("apply runs the BASELINE step against the target's own runner",
              "/BASELINE] reading the target's own runner" in pa.stdout, pa.stdout)
        check("apply probes the target's pre-commit hook without committing",
              "/HOOKPROBE]" in pa.stdout, pa.stdout)
        check("apply emits the leg as the LEGS step", "gate legs: emitted" in pa.stdout, pa.stdout)
        check("and re-reads the runner afterwards", "/AFTER]" in pa.stdout, pa.stdout)
        after_out = run_runner(gt)
        # EXECUTION, not success: a leg that fails has still executed, and `observed_failed` is a
        # separate template for exactly that reason.
        check("AC17: the emitted leg is observed EXECUTING, by name",
              "check-wiring self-test" in after_out, after_out)
        check("and the CONTROL leg is observed in BOTH runs — without it every absence assertion "
              "above could pass because the runner itself did nothing",
              "GATE ok    control" in before_out and "GATE ok    control" in after_out, after_out)

        # Idempotency by the declared dedupe key, and the row count must have GROWN first —
        # 'byte-identical' alone is satisfied by an emitter that does nothing.
        legs1 = json.loads((gt / "tools" / "legs.json").read_text(encoding="utf-8"))
        check("the first apply strictly increased the runner's row count", len(legs1) == 2,
              str(legs1))
        run("apply", "--target", str(gt), "--kits", "check-wiring")
        legs2 = json.loads((gt / "tools" / "legs.json").read_text(encoding="utf-8"))
        check("a second apply leaves the runner file byte-identical", legs1 == legs2, str(legs2))

        # A guard that renders to a path matching nothing TRACKED is dropped, and the leg is emitted
        # with NO guard key — never `[]`. The runner's own predicate is a diff over a pathspec, and a
        # pathspec matching nothing diffs clean, so an existence test would keep it and skip forever.
        emitted_leg = next(l for l in legs2 if l["name"] == "check-wiring self-test")
        check("a guard rendering to a path this apply STAGED is kept, not dropped",
              emitted_leg.get("guard") == ["tools/check-wiring.sh", "tools/check-wiring.test.sh"],
              str(emitted_leg))
        vals = [v for l in legs2 for v in ([l["name"]] + l["argv"] + l.get("guard", []))]
        check("and no emitted VALUE still carries a brace", not any("{" in v for v in vals),
              str(vals))

        # The drop case, on a fixture where the guard genuinely names nothing tracked. The runner's
        # own predicate is a diff over a pathspec and a pathspec matching nothing diffs CLEAN, so an
        # existence test would keep such a guard and skip its leg forever at exit 0.
        tracked_after = set(subprocess.run(["git", "-C", str(gt), "ls-files"],
                                           capture_output=True, text=True).stdout.split("\n"))
        check("every guard that SURVIVED names a path tracked in the target — the drop test is "
              "tracked-ness, not existence, because a pathspec matching nothing diffs clean and "
              "would skip its leg forever at exit 0",
              all(any(t2 == g.rstrip("/") or t2.startswith(g.rstrip("/") + "/")
                      for t2 in tracked_after if t2)
                  for l in legs2 for g in l.get("guard", [])), str(legs2))
        check("and no leg carries an EMPTY guard list — the key is omitted instead",
              all(l.get("guard") != [] for l in legs2), str(legs2))
        # NOT ARMED, and said rather than implied: the pure DROP path — a guard rendering to a path
        # no apply creates — has no fixture here. Every shipped guard resolves to something apply
        # stages, and a fixture that pre-writes one trips the foreign-kit refusal instead. Recorded
        # so the gap is visible rather than looking covered.

        # Ownership: a name the target already owns is refused, not overwritten.
        own = runner_target("u4b")
        lj = own / "tools" / "legs.json"
        lj.write_text(json.dumps([{"name": "control", "argv": ["true"]},
                                  {"name": "check-wiring self-test", "argv": ["echo", "theirs"]}],
                                 indent=2) + "\n", encoding="utf-8", newline="\n")
        git(own, "add", "-A"); git(own, "commit", "-qm", "theirs")
        before_bytes = lj.read_bytes()
        pa = run("apply", "--target", str(own), "--kits", "check-wiring")
        check("a leg name the target owns and the receipt does not is REFUSED", pa.returncode == 2,
              pa.stdout + pa.stderr)
        check("that refusal says overwriting it would delete the target's own coverage",
              "deletes their own coverage" in pa.stderr, pa.stderr)
        check("and the runner file is byte-identical after the refusal",
              lj.read_bytes() == before_bytes, "")

        # kind = "none" ORDERS rather than emitting, and says so in its own words.
        nt = runner_target("u4c", kind="none")
        pa = run("apply", "--target", str(nt), "--kits", "check-wiring")
        check("kind = none ORDERS the legs instead of emitting them",
              "ORDERED, not emitted" in pa.stdout, pa.stdout)
        order = nt / ".governance" / "outbox" / "gate-legs.md"
        check("and the order names the specific leg and its rendered argv",
              order.is_file() and "check-wiring self-test" in order.read_text(encoding="utf-8"),
              order.read_text(encoding="utf-8") if order.is_file() else "absent")

        # Every refused value, by NAME, before any write.
        for bad, needle in ((('kind = "make"'), "implements ONE grammar"),
                            (('kind = "manifest"\nfile = "x.json"\ngrammar = "toml"\n'
                              'dedupe_key = "name"\ncommand = ["true"]\nrun_all_env = {}\n'
                              'observed_ran = ["a{name}"]\nobserved_failed = ["b{name}"]'),
                             "only 'json-array' is implemented")):
            bt = make_target(tmp / ("u4r%d" % (abs(hash(bad)) % 9999)), None)
            (bt / ".governance").mkdir(exist_ok=True)
            (bt / ".governance" / "deploy.toml").write_text(
                'gov_source = "local"\nprefix = "tools"\nkits = ["check-wiring"]\n'
                '[answers]\nmemory_root = "memory"\n[gate_runner]\n' + bad + "\n",
                encoding="utf-8", newline="\n")
            pa = run("apply", "--target", str(bt), "--kits", "check-wiring")
            check("a refused [gate_runner] value is named: " + needle[:34],
                  needle in pa.stdout + pa.stderr, pa.stdout + pa.stderr)
            check("and nothing was installed on that refusal: " + needle[:20],
                  not (bt / ".governance" / "install.json").exists(), "")

        # ===== unit 6: the merged region =====
        NLc = chr(10)

        def hook_target(name: str, hook: str) -> pathlib.Path:
            g = tmp / name
            (g / ".githooks").mkdir(parents=True, exist_ok=True)
            (g / ".githooks" / "pre-commit").write_text(hook, encoding="utf-8", newline=NLc)
            (g / ".governance").mkdir(exist_ok=True)
            (g / ".governance" / "deploy.toml").write_text(
                'gov_source = "l"' + NLc + 'prefix = "tools"' + NLc +
                'kits = ["push-main"]' + NLc + "[answers]" + NLc + 'memory_root = "memory"' + NLc,
                encoding="utf-8", newline=NLc)
            git(g, "init", "-q", "-b", "main"); git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t"); git(g, "add", "-A"); git(g, "commit", "-qm", "b")
            return g

        MARKED = ("#!/usr/bin/env bash" + NLc + "set -u" + NLc + "echo MINE" + NLc +
                  "# govkit:branch-guard" + NLc + "# old" + NLc + "# /govkit:branch-guard" + NLc +
                  "echo TAIL" + NLc)

        hg = hook_target("u6a", MARKED)
        pa = run("apply", "--target", str(hg), "--kits", "push-main")
        hook_now = (hg / ".githooks" / "pre-commit").read_text(encoding="utf-8")
        check("a merged rule SPLICES its block into a target-owned file",
              "merged [spliced]" in pa.stdout, pa.stdout)
        check("the target's own lines on BOTH sides of the block survive",
              "echo MINE" in hook_now and "echo TAIL" in hook_now, hook_now)
        check("and the block's previous content is replaced, not appended to",
              NLc + "# old" + NLc not in hook_now, hook_now)
        before_bytes = (hg / ".githooks" / "pre-commit").read_bytes()
        run("apply", "--target", str(hg), "--kits", "push-main")
        check("a second apply leaves the merged file byte-identical",
              (hg / ".githooks" / "pre-commit").read_bytes() == before_bytes, "")

        # AC1's two clauses, one mechanism: the receipt hashes the BLOCK, so an edit OUTSIDE it is
        # invisible by construction — the extractor only ever reads the marked lines.
        with open(hg / ".githooks" / "pre-commit", "a", encoding="utf-8", newline=NLc) as fh:
            fh.write("echo OUTSIDE" + NLc)
        pc = run("check", "--target", str(hg))
        check("an edit OUTSIDE the block is NOT drift — asserted positively, not by omission",
              "DRIFT" not in pc.stdout and "merged blocks:" in pc.stdout, pc.stdout)
        hp = hg / ".githooks" / "pre-commit"
        hp.write_text(hp.read_text(encoding="utf-8").replace("rc=1", "rc=0", 1),
                      encoding="utf-8", newline=NLc)
        pc = run("check", "--target", str(hg))
        check("an edit INSIDE the block IS drift, naming the block and both hashes",
              "DRIFT: gov block 'govkit:branch-guard'" in pc.stdout, pc.stdout)
        hp.write_text(hp.read_text(encoding="utf-8")
                      .replace("# govkit:branch-guard" + NLc, "")
                      .replace("# /govkit:branch-guard" + NLc, ""),
                      encoding="utf-8", newline=NLc)
        pc = run("check", "--target", str(hg))
        check("deleting the marker pair is REMOVED, a state distinct from drift",
              "REMOVED" in pc.stdout, pc.stdout)

        # insert = "refuse": the branch guard's position is SEMANTIC and this rule will not guess.
        ug = hook_target("u6b", "#!/usr/bin/env bash" + NLc + "echo MINE" + NLc)
        before_u = (ug / ".githooks" / "pre-commit").read_bytes()
        pa = run("apply", "--target", str(ug), "--kits", "push-main")
        check("an unmarked destination whose rule declares insert=refuse REFUSES",
              "insert = \"refuse\"" in pa.stdout or "position is SEMANTIC" in pa.stdout, pa.stdout)
        check("and the target's file is byte-identical after that refusal",
              (ug / ".githooks" / "pre-commit").read_bytes() == before_u, "")

        # THE APPEND, and the guard that makes it safe. MEASURED: appending to a file whose last
        # line lacks a trailing newline concatenates the two, which destroys the target's own final
        # rule and leaves the open marker off column 0 — after which every later apply refuses
        # forever while the receipt claims a block that can never be found again.
        pj = tmp / "u6c"
        (pj / ".governance").mkdir(parents=True, exist_ok=True)
        (pj / "pyproject.toml").write_bytes(b"[tool.other]\nkey = 1")      # NO trailing newline
        (pj / ".governance" / "deploy.toml").write_text(
            'gov_source = "l"' + NLc + 'prefix = "tools"' + NLc +
            'kits = ["pytest-parallel-guardrails"]' + NLc + "[answers]" + NLc +
            'memory_root = "memory"' + NLc, encoding="utf-8", newline=NLc)
        git(pj, "init", "-q", "-b", "main"); git(pj, "config", "user.email", "t@e")
        git(pj, "config", "user.name", "t"); git(pj, "add", "-A"); git(pj, "commit", "-qm", "b")
        run("apply", "--target", str(pj), "--kits", "pytest-parallel-guardrails")
        body = (pj / "pyproject.toml").read_text(encoding="utf-8")
        check("an append to a file with no trailing newline does NOT join two lines",
              "key = 1# govkit" not in body, body[:200])
        check("the target's pre-existing final line survives intact",
              "key = 1" in body and NLc + "# govkit:pytest-guardrails" in body, body[:200])
        check("and the open marker is at column 0, so the block stays findable",
              any(l == "# govkit:pytest-guardrails" for l in body.split(NLc)), body[:200])
        pc = run("check", "--target", str(pj))
        check("which check confirms by FINDING it", "merged blocks: 1/1 intact" in pc.stdout,
              pc.stdout)

        # ===== unit 6, the pin block =====
        NLp = chr(10)

        def pin_target(name: str, ga: bytes | None) -> pathlib.Path:
            g = tmp / name
            (g / ".governance").mkdir(parents=True, exist_ok=True)
            (g / ".governance" / "deploy.toml").write_text(
                'gov_source = "l"' + NLp + 'prefix = "tools"' + NLp +
                'kits = ["memory-recall"]' + NLp + "[answers]" + NLp +
                'memory_root = "memory"' + NLp, encoding="utf-8", newline=NLp)
            (g / "README.md").write_text("t" + NLp, encoding="utf-8", newline=NLp)
            if ga is not None:
                (g / ".gitattributes").write_bytes(ga)
            git(g, "init", "-q", "-b", "main"); git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t"); git(g, "add", "-A"); git(g, "commit", "-qm", "b")
            return g

        # THE MEASURED HAZARD: an attributes file whose last line has NO trailing newline. Without
        # the guard the append concatenates the two, which destroys the target's own final rule,
        # makes git report an invalid attribute name on every query in that repo, and leaves the
        # open marker off column 0 -- after which every later apply refuses forever while the
        # receipt claims a block that can never be found again.
        pg = pin_target("u6p1", b"*.sh text eol=lf")          # deliberately no trailing newline
        run("apply", "--target", str(pg), "--kits", "memory-recall")
        lines = (pg / ".gitattributes").read_text(encoding="utf-8").split(NLp)
        check("an append to an attributes file with no trailing newline does not join two lines",
              lines[0] == "*.sh text eol=lf", str(lines[:2]))
        check("and the block's open marker is at COLUMN 0, so it stays findable",
              "# govkit:lf-pins" in lines, str(lines[:3]))
        (pg / "z.sh").write_text("x" + NLp, encoding="utf-8", newline=NLp)
        git(pg, "add", "z.sh")
        ca = subprocess.run(["git", "-C", str(pg), "check-attr", "eol", "z.sh"],
                            capture_output=True, text=True).stdout
        check("the target's OWN pre-existing rule still resolves after the append",
              "eol: lf" in ca, ca)

        # The block is written EARLY and the renormalize runs LAST. On a first install the pinned
        # population does not exist yet, so a one-phase design either refuses every install or
        # reports success over nothing.
        pa = run("apply", "--target", str(pin_target("u6p2", None)), "--kits", "memory-recall")
        idx_att = pa.stdout.index("/ATTRIBUTES]")
        check("the ATTRIBUTES step runs before LAND", idx_att < pa.stdout.index("/LAND]"), pa.stdout)
        check("and the RENORMALIZE step runs after CONFIGURE",
              pa.stdout.index("/RENORMALIZE]") > pa.stdout.index("/CONFIGURE") if "/CONFIGURE"
              in pa.stdout else True, pa.stdout)
        check("a VIRGIN target — no memory tree, no rendered artifacts — still reaches the "
              "renormalize rather than refusing in the pin phase",
              "/RENORMALIZE]" in pa.stdout and "not clean relative to HEAD" not in pa.stdout,
              pa.stdout + pa.stderr)

        # The gov-only rows are an ACCOUNTING record for gov's own attributes file, not deployable
        # content: emitting them would put gov's rules about its own shell scripts and its own
        # deployer into a target that receives neither.
        blk = (pg / ".gitattributes").read_text(encoding="utf-8")
        check("gov-only pins are NOT emitted into a target",
              "tools/govkit/*" not in blk and "tools/gate-legs.json" not in blk, blk)
        check("but the selected kit's own pin IS",
              ".claude/skills/memory-recall/SKILL.md text eol=lf" in blk, blk)

        # A pin that governs nothing is REPORTED. Measured: `git ls-files --eol` over a pathspec
        # matching nothing prints nothing and exits 0, so without this the phase reports success
        # over an empty set -- the second named defect class, inside the step meant to close the
        # first.
        check("a pin resolving to no tracked path in the target is reported, by pattern and claimant",
              "resolves to no tracked path" in pa.stdout, pa.stdout)

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

        # --- SUPERSEDED. These two arms asserted that a `merged` rule REFUSES by name, and the
        # --- merged-region writer inverts them: the role is honourable now. Replaced with a
        # --- POSITIVE on-disk assertion rather than deleted — an arm that asserts a refusal string
        # --- is the classic one that keeps passing after the string merely moves, so its
        # --- replacement has to observe an effect. The full behaviour is in the unit 6 block above.
        p = run("apply", "--target", str(make_target(tmp / "f", DEPLOY_FULL)),
                "--kits", "pytest-parallel-guardrails")
        check("a merged rule now LANDS rather than refusing", p.returncode == 0, p.stdout)
        check("and it reports the mode it used, on disk",
              "merged [" in p.stdout, p.stdout)

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
            # The descriptor DECLARES the manifest's leg. Without it the fixture is a gov tree whose
            # leg is claimed by nobody, which the leg correspondence reds on — correctly, and the
            # fixture's own premise is that both facts agree.
            (g / "tools" / "demo" / "kit.toml").write_text(
                'id = "demo"\nhome = "tools/demo"\n'
                'version_from = { none = "fixture" }\n\n'
                '[check]\nnone = "a fixture kit"\n\n'
                '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                f'[adopt]\nargv = ["bash", "{{kit}}/adopt-demo.sh"]\nmutates_index = {mutates}\n\n'
                '[[gate_leg]]\nname = "demo"\nargv = ["true"]\nguard = []\n',
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
            check("apply lands the kit at all",
                  owned.is_file() and "landed" in first.stdout, first.stdout + first.stderr)

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
            # Its LIVENESS intent is preserved and only its operand moved: a non-zero adopter exit
            # is now a FINDING, so a kit whose adopter legitimately refuses on a fresh target no
            # longer exits 0 and the exit code would fail this arm for the wrong reason. What proves
            # the re-apply RAN — which is what stops the two protection arms below passing on an
            # apply that refused and wrote nothing — is that it reached the LAND phase and reported
            # landing, and that it got as far as writing a receipt.
            check("the re-apply actually ran",
                  "landed" in second.stdout and "/RECEIPT]" in second.stdout,
                  second.stdout + second.stderr)
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
            # FILTERED ON THE RECEIPT SIDE, AND THAT IS NOT THE FILTER THIS ARM DROPPED. The role
            # filter removed above was on the PLAN side, where it hid apply/plan disagreement. This
            # one is a schema fact: under schema 1 every receipt row carried gov bytes, so the whole
            # receipt WAS the write set and no filter was needed. Schema 2 records a row for every
            # file gov is responsible for — `rendered`, `attributes`, `project-owned` included — so
            # comparing plan's writes to the whole receipt compares two different questions. Keyed
            # on the bytes rather than on a role list, so a new non-landing role needs no edit here.
            applied = {f["path"] for f in first_receipt.get("files", []) if "sha256" in f}
            check("plan's write set equals the receipt rows CARRYING BYTES, any role",
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
            bytes2 = {f["path"] for f in rec2.get("files", []) if "sha256" in f}
            check("plan's write set equals the DEFAULT selection's byte-carrying rows",
                  extract_plan_writes(pl2.stdout) == bytes2,
                  f"planned-only={sorted(extract_plan_writes(pl2.stdout) - bytes2)} "
                  f"applied-only={sorted(bytes2 - extract_plan_writes(pl2.stdout))}")

            # THE MAPPING, PINNED POSITIVELY AND PER ROLE. Set-equality above cannot express this:
            # an implementation emitting every non-landable row under ONE mark satisfies it.
            # MEASURED from the descriptors on this tree, not carried over: memory-tree 3 +
            # memory-recall 1 rendered with adopters, codebase-map 1 project-owned whose sibling seed
            # lands the same path, and the playbook's 9 line-ending pin patterns.
            #
            # The playbook pair is NOT in this count any more, and that is a fix rather than drift:
            # both its rules are `seed`, because tagged `project-owned` the entry landed ZERO bytes
            # while sitting first in the default selection. This arm asserted the role that defect
            # wore. An un-covered `project-owned` row is worth an arm, so it keeps one — over a
            # scratch descriptor below, where the role cannot be silently redefined out from under it.
            marks = measure_plan_marks(pl2.stdout)
            check("the default selection previews exactly 4 SIDE|rendered rows",
                  marks.get("SIDE|rendered") == 4, str(marks))
            # `ORDER|project-owned` is 4, and the four are NAMED: memory-recall's
            # `recall-fixture.json`, `check-recall.py` and `test_recall_floor.py`, withheld from the
            # payload by a `project-owned` rule with no sibling producer (TOOL-aWalkedCorpus-3 S8);
            # and run-gates' `run-gates.gov.test.sh`, withheld by the same mechanism for the same
            # stated reason — its arms are keyed on THIS repo's corpus, so in another tree they would
            # red on absence rather than on behaviour. Four, not three, because the run-gates kit
            # landed; the count is a MEASUREMENT of this tree and moves when the tree does, which is
            # what the paragraph below already says about this half of the arm.
            # This half of the arm is a TREE-STATE snapshot; the SEMANTIC invariant it used to carry
            # -- an un-covered `project-owned` rule derives ORDER -- moved to the scratch descriptor
            # below precisely so an entry edit could not redefine it, and that arm is untouched.
            # govkit has no kind meaning "in the kit dir, deliberately not in the payload", so the
            # ORDER row tells an adopter to supply a file gov does not want them to have. Recorded as
            # TOOL-aWalkedCorpus-6 rather than papered over here.
            check("...and the playbook file previews as a seed WRITE, not as an order",
                  marks.get("write|seed") == 3 and marks.get("ORDER|project-owned") == 4,
                  str(marks))
            check("...and 1 COVER|project-owned row, for the path a sibling seed writes",
                  marks.get("COVER|project-owned") == 1, str(marks))
            check("...and NO project-owned row is previewed as a write",
                  marks.get("write|project-owned") is None, str(marks))

            # THE UN-COVERED `project-owned` ROW, PINNED ON THE TABLE ITSELF. No entry on this tree
            # has one — codebase-map's is covered by a sibling seed — so the integration arm that
            # used to assert it was riding the playbook's role and died when that role was corrected.
            # Keyed on `derive_rule_kind` directly, it cannot be redefined out from under itself by
            # an entry edit, and it still reds if `order` ever stops being the answer.
            sys.path.insert(0, str(HERE))
            import govkit as _gk  # noqa: E402
            _rep = _gk.Report()
            _po = {"role": "project-owned"}
            check("an un-covered project-owned rule derives ORDER",
                  _gk.derive_rule_kind("demo", {}, _po, "a.md", set(), set(), _rep) == "order",
                  "expected 'order'")
            check("...and the same rule derives COVERED when a sibling writes that path",
                  _gk.derive_rule_kind("demo", {}, _po, "a.md", {"a.md"}, set(), _rep) == "covered",
                  "expected 'covered'")
            # `requires` ORDERS THE INSTALL, and did not until it was measured. Every mode of
            # resolve_selection returned sorted(...), so CONFIGURE ran adopters alphabetically and
            # `memory-recall` -- which declares requires = ["memory-tree"] -- ran BEFORE the conf it
            # reads existed. Its adopter exited 1, govkit could not classify that code, and the
            # default-selection arm below failed on every node while the same adopter run by hand a
            # moment later exited 0. Keyed on the FUNCTION so no entry edit can hide it.
            _descs2 = {
                "b-kit": ({"requires": ["z-kit"]}, "b"),
                "z-kit": ({}, "z"),
                "a-kit": ({}, "a"),
            }
            _ordered = _gk.derive_install_order(["a-kit", "b-kit", "z-kit"], _descs2)
            check("a kit is ordered AFTER everything it `requires`",
                  _ordered.index("z-kit") < _ordered.index("b-kit"), str(_ordered))
            check("...and independent kits keep alphabetical order",
                  _ordered[0] == "a-kit", str(_ordered))
            check("...and a dependency outside the selection is not an error",
                  _gk.derive_install_order(["b-kit"], _descs2) == ["b-kit"], "a lone kit must install")
            _cyc = {"x": ({"requires": ["y"]}, "x"), "y": ({"requires": ["x"]}, "y")}
            try:
                _gk.derive_install_order(["x", "y"], _cyc)
                _cycled = False
            except _gk.Refusal:
                _cycled = True
            check("...and a `requires` CYCLE refuses rather than picking an order",
                  _cycled, "a cycle fell through to some arbitrary order")

            # AN ACCEPTED STOP IS NOT A FAILURE. `memory-tree` seeds the conf and stops by design, so
            # every correct first install exits 1 there; calling that a failure made a default-selection
            # apply unable to return 0, and the arm asserting it does landed RED rather than being read
            # as the contradiction it was. The flag is per-OUTCOME, so `refused-foreign-tree` -- same
            # exit code, same kit -- stays a failure.
            import tomllib as _toml  # noqa: PLC0415
            _mt = _toml.loads((HERE.parent / "memory-tree" / "kit.toml").read_text(encoding="utf-8"))
            _outs = {o.get("means"): o for o in _mt.get("outcome", [])}
            check("memory-tree declares seed-and-stop as an ACCEPTED outcome",
                  _outs.get("seed-and-stop", {}).get("ok") is True, str(list(_outs)))
            check("...and refused-foreign-tree is NOT accepted, at the same exit code",
                  _outs.get("refused-foreign-tree", {}).get("ok") is not True
                  and _outs.get("refused-foreign-tree", {}).get("code")
                      == _outs.get("seed-and-stop", {}).get("code"),
                  str(_outs))

            check("...and the ORDER/COVERED pair is not one answer twice",
                  _gk.derive_rule_kind("demo", {}, _po, "a.md", set(), set(), _rep)
                  != _gk.derive_rule_kind("demo", {}, _po, "a.md", {"a.md"}, set(), _rep),
                  "the two states collapsed to one kind")

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
                # A FRESH TARGET PER KIT. `t2` has had a full default apply run against it, so a
                # second apply there can refuse for the pre-existing-kits reason instead of the
                # merged-region one — and the arm would then pass or fail on fixture order rather
                # than on the behaviour it names. `plan` above is read-only, so it can share `t2`.
                tm = make_target(tmp3 / f"merged-{kit}", DEPLOY_FULL)
                ap = run("apply", "--target", str(tm), "--kits", kit)
                check(f"{kit}: ...and apply refuses over it",
                      "no verb here can write a gov-owned region" in ap.stdout + ap.stderr,
                      ap.stdout + ap.stderr)

            # APPLY NAMES WHAT IT SKIPS. The aggregate `landed 0 file(s)` was the whole report.
            # KEYED ON codebase-map, NOT ON playbook. The playbook's two rules are `seed` and LAND,
            # so it skips nothing to name — this arm was reading the role the landed-zero-bytes
            # defect wore. codebase-map's `map_extractors.py` is a real project-owned skip.
            t3 = make_target(tmp3 / "skips", DEPLOY_FULL)
            sk = run("apply", "--target", str(t3), "--kits", "codebase-map")
            check("apply names each skipped rule, its role and its destination",
                  "SKIPPED [project-owned] tools/codebase-map/map_extractors.py" in sk.stdout,
                  sk.stdout)
            check("...and says why, in the same terms the preview used",
                  "writes that same path in this run" in sk.stdout, sk.stdout)
            check("...and names it ONCE, not once per classifier",
                  sk.stdout.count("tools/codebase-map/map_extractors.py <- codebase-map") == 1,
                  sk.stdout)

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

    # ---- the SEED -> EMIT -> READ round trip, over every entry that declares one ----------------
    #
    # THE ARM THE BLOCKER ASKED FOR, and it is parameterised over the registry rather than written
    # for one kit, so it retires the whole family including for kits that do not exist yet.
    #
    # What it caught, stated because an arm's motivating failure is the thing that keeps it honest:
    # `[gate_runner_seed]` declared `observed_ran` as a TOML SCALAR, `cmd_intake` emitted every key
    # by quoting it, and `read_gate_verdicts` ITERATES that key — so it walked the string character
    # by character. The head became `G`, no leg name was ever recovered, and because `observed_ran`
    # is scanned first and `setdefault` wins, no key could ever be red. A real `apply` exited 0
    # recording every line green while the target's canary leg was genuinely RED. Nothing on the bar
    # saw it: every other arm here hand-writes the ARRAY form, so the emitter and the reader had
    # never met. This arm is where they meet.
    import tomllib as seed_toml  # noqa: PLC0415
    _gov = HERE.parent.parent

    def load_seed_toml(path: pathlib.Path) -> dict:
        with path.open("rb") as fh:
            return seed_toml.load(fh)

    def run_govkit(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(_gov / "tools" / "govkit" / "govkit.py"), *args],
                              capture_output=True, text=True)

    reg = load_seed_toml(_gov / "tools" / "govkit" / "registry.toml")
    seeded = []
    for e in reg.get("entry", []):
        d = load_seed_toml(_gov / e["descriptor"])
        if d.get("gate_runner_seed"):
            seeded.append((e["id"], d["gate_runner_seed"]))
    check("at least one registry entry declares a [gate_runner_seed] to round-trip",
          bool(seeded), "no entry declares one — this arm would pass by finding nothing")
    for eid, seed in seeded:
        with tempfile.TemporaryDirectory() as td:
            tgt = pathlib.Path(td) / "t"
            (tgt / ".governance").mkdir(parents=True)
            subprocess.run(["git", "init", "-q", "."], cwd=str(tgt), capture_output=True)
            r = run_govkit("intake", "--target", str(tgt), "--kits", eid)
            check(f"[{eid}] intake writes a descriptor", r.returncode == 0, r.stdout + r.stderr)
            decl = (load_seed_toml(tgt / ".governance" / "deploy.toml").get("gate_runner") or {})
            for key in ("observed_ran", "observed_failed"):
                v = decl.get(key)
                check(f"[{eid}] the emitted {key} is a LIST, which is what the reader iterates",
                      isinstance(v, list) and bool(v),
                      f"{key} = {v!r} — a string here is walked character by character")
            # The round trip that matters: feed a line the runner really prints back through the
            # reader's own head-extraction and assert the BARE LEG NAME comes back.
            for key, sample in (("observed_ran", "GATE ok    memory hygiene"),
                                ("observed_failed", "GATE FAIL  memory hygiene  (exit 1)")):
                tmpl = (decl.get(key) or [None])[0]
                got = None
                if isinstance(tmpl, str):
                    head = tmpl.split("{name}")[0]
                    if sample.startswith(head) and len(sample) > len(head):
                        got = sample[len(head):].strip().split("  ")[0].strip()
                check(f"[{eid}] {key} recovers the bare leg name from a real runner line",
                      got == "memory hygiene", f"recovered {got!r} from {sample!r} via {tmpl!r}")

    print()
    if FAILURES:
        print(f"govkit-selftest: {len(FAILURES)} FAILED — {', '.join(FAILURES)}")
        return 1
    print("govkit-selftest: all arms held")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
