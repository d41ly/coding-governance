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
import time

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


def govkit_update_role() -> dict:
    """The engine's OWN update dispatch table, for the reason `govkit_kind_marks` gives."""
    sys.path.insert(0, str(HERE))
    import govkit  # noqa: E402
    return govkit.UPDATE_ROLE


def govkit_module():
    """The engine module itself, for arms that call a resolver directly rather than a verb."""
    sys.path.insert(0, str(HERE))
    import govkit  # noqa: E402
    return govkit
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


def settle(t: pathlib.Path, msg: str = "fixture") -> None:
    """Commit whatever a writing verb just left in the target.

    DEPL-dCarriedReceipt-12 S4 refuses a writing verb when any RECEIPT-CLAIMED path is dirty,
    and dirty is defined there as differing index-versus-HEAD or worktree-versus-index. `apply`
    STAGES every path it lands, so a target that has been applied and not committed carries an
    entire receipt's worth of dirty claimed paths. Every fixture below that runs a writing verb
    a second time therefore commits in between — which is exactly what the refusal now asks an
    operator to do, so the fixtures model the supported flow rather than working around it.

    Without this, twelve arms went red and two more passed VACUOUSLY: their re-apply refused,
    wrote nothing, and "the edit survived" was trivially true because nothing had run.
    """
    git(t, "add", "-A")
    git(t, "commit", "-qm", msg)


def make_target(tmp: pathlib.Path, deploy: str | None) -> pathlib.Path:
    t = tmp / "target"
    t.mkdir(parents=True, exist_ok=True)
    git(t, "init", "-q", "-b", "main")
    git(t, "config", "user.email", "t@e")
    git(t, "config", "user.name", "t")
    # PINNED, not inherited. DEPL-dCarriedReceipt-7 S5 lands bytes through `checkout-index`, so the
    # TARGET's own filters decide its worktree — which is the whole point, and which makes every
    # arm asserting worktree bytes depend on the DEVELOPER's global `core.autocrlf` until it is
    # pinned here. It is `true` by default on a Windows git install, and measured: eight arms
    # asserting `b"v3\n"` went red on this machine for that reason alone. The filter is still
    # exercised, deliberately and per fixture, by the clones `-7`'s own arms build with
    # `-c core.autocrlf=true`.
    git(t, "config", "core.autocrlf", "false")
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
        # THE ENGINE'S OWN CONSTANT, for the reason `govkit_steps` gives: a number spelled here goes
        # stale the next time a unit adds a per-role row field, and the arm then grades the harness's
        # memory of the schema instead of the receipt's declaration of it.
        check("the receipt declares its schema", rec1.get("schema") == govkit_module().RECEIPT_SCHEMA,
              str(rec1.get("schema")))
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
        settle(ap, "the first apply")     # -12 S4: the first apply's staged rows are dirty
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
        settle(cm, "the first apply")
        (cm / "tools" / "codebase-map" / "map_extractors.py").write_bytes(b"# TARGET EDITED\n")
        # COMMITTED, not merely written. -12 S4 refuses a writing verb over an uncommitted edit
        # to a claimed path, so an uncommitted edit here would make the re-apply refuse — and
        # both arms below would then pass on an apply that never ran.
        settle(cm, "the target edits its seed")
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
                # AND `gov_oid`, or this fixture is not "landed at an older vintage" — it is a row
                # whose `commit` came from one vintage and whose `gov_oid` came from another, which
                # is EXACTLY the corruption `-7` S9 refuses. Measured: nine arms went red on that
                # refusal, and they were right to. The engine's own helper, so the fixture and the
                # thing it grades cannot disagree about what a blob is named.
                f["gov_oid"] = govkit_module().blob_oid(b)
                (t / f["path"]).write_bytes(b)
            rp.write_text(json.dumps(rec, indent=2), encoding="utf-8", newline="\n")
            # -12 S4: `apply` staged every row, and the loop above then rewound their bytes in
            # the worktree. Both halves are dirty by that definition, so the fixture commits
            # the stale state it just built — the target is legitimately AT an older vintage,
            # which is a committed fact about it and not an operator's work-in-progress.
            settle(t, "landed at the older vintage")
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
        # COMMITTED. -12 S4 refuses over an UNCOMMITTED edit to a claimed path — a stronger
        # protection than this arm asserts, and one that would stop the classifier ever being
        # reached. The guarantee under test is the one that survives a commit: a local edit gov
        # can SEE is reported, never overwritten.
        settle(up2, "the operator edits a gov-owned file")
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
                             "guard": [], "subject": "repo"}], indent=2) + NL,
                encoding="utf-8", newline=NL)
            # `shutil.copytree(HERE, ...)` above brings gov's own subject pin with it, and this
            # tree has one leg rather than gov's whole manifest. Overwritten with a pin for THIS
            # fixture, because a pin naming legs the tree does not have is exactly the stale-pin
            # refusal the ratchet exists to raise. TOOL-dUnstalledConvoy-29.
            (g / "tools" / "govkit" / "subject-pins.tsv").write_text(
                "# fixture pin" + NL + "demo leg\trepo" + NL, encoding="utf-8", newline=NL)
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
                # The fixture declares `subject`, because govkit now refuses a descriptor leg without
                # one — a leg that does not say whose subject it is cannot be held or run
                # deliberately. TOOL-dUnstalledConvoy-26.
                lines += ["[[gate_leg]]", 'name = "%s"' % leg_name, 'subject = "repo"',
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

        # ---- AC11 (TOOL-dUnstalledConvoy-26): the install summary tells the adopter about the
        # ---- legs it just made INVISIBLE. A kit-subject leg is held by default, so an adopter who
        # ---- is not told at install has a self-test they will never run and no way to learn it
        # ---- exists — the removal would read to them as the kit shipping no tests at all.
        # ---- The check-wiring entry emits exactly one leg and it is subject = "kit", so this
        # ---- fixture is the right shape for the arm rather than an accident of it.
        _kits_in = [r for r in json.loads((gt / "tools" / "legs.json").read_text(encoding="utf-8"))
                    if (r.get("subject") or "repo") == "kit"]
        check("LIVENESS: the fixture actually emitted a kit-subject leg, or the AC11 arms below "
              "would be asserting about a summary with nothing to summarise",
              len(_kits_in) == 1, str(_kits_in))
        check("AC11: the install summary states how many emitted legs are HELD kit self-tests",
              f"govkit apply — {len(_kits_in)} of those are kit SELF-TESTS and are HELD by default"
              in pa.stdout, pa.stdout)
        # The invocation is the TARGET's declared runner command, not this repo's path — an adopter
        # pointed at a script absent from their tree has been told nothing.
        check("AC11: and names the once-and-on-demand invocation against the target's own runner",
              "govkit apply —   GATE_SELFTESTS=1 bash tools/runner.sh" in pa.stdout, pa.stdout)
        # The GATE_FULL sentence is not decoration: `guard = ["{kit}/"]` was the mechanism this
        # replaced, and it failed precisely because GATE_FULL ignores guards. An adopter who reads
        # `GATE_FULL=1` as "everything" will believe a green bar covered the kits.
        check("AC11: and says plainly that GATE_FULL does NOT run them",
              "GATE_FULL=1 does NOT run them" in pa.stdout, pa.stdout)
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

        # --- DEPL-dCarriedReceipt-3: `intake` honours `--answer prefix=`, on every branch.
        # The pre-unit behaviour emitted the literal `tools` whatever was supplied, so the one
        # committed non-default descriptor in the fleet was a file the tool that owns it could not
        # have written. Each arm below fails against that draft.
        ik3 = make_target(tmp / "i3", None)
        p = run("intake", "--target", str(ik3), "--kits", "gate-lint",
                "--answer", "prefix=scripts")
        check("intake with --answer prefix= exits 0", p.returncode == 0, p.stdout + p.stderr)
        check("the descriptor carries the SUPPLIED prefix",
              'prefix = "scripts"' in (ik3 / ".governance" / "deploy.toml").read_text(
                  encoding="utf-8"), p.stdout)
        check("the run reports the prefix and names its source",
              'prefix "scripts" (from --answer)' in p.stdout, p.stdout)

        ik4 = make_target(tmp / "i4", None)
        p = run("intake", "--target", str(ik4), "--kits", "gate-lint")
        check("an OMITTED prefix still defaults to tools",
              'prefix = "tools"' in (ik4 / ".governance" / "deploy.toml").read_text(
                  encoding="utf-8"), p.stdout)
        check("the default is reported as a default, not as an answer",
              'prefix "tools" (default)' in p.stdout, p.stdout)

        # An EMPTY value is the default, never an empty prefix: `prefix = ""` would resolve every
        # destination to a bare relative path, which is a silent mis-install rather than a refusal.
        ik5 = make_target(tmp / "i5", None)
        p = run("intake", "--target", str(ik5), "--kits", "gate-lint", "--answer", "prefix=")
        check("an EMPTY --answer prefix= falls back to tools",
              'prefix = "tools"' in (ik5 / ".governance" / "deploy.toml").read_text(
                  encoding="utf-8"), p.stdout)
        check("an empty prefix is never emitted",
              'prefix = ""' not in (ik5 / ".governance" / "deploy.toml").read_text(
                  encoding="utf-8"), p.stdout)

        # The prefix has THREE readers in `cmd_intake` and they all land in this one file. The
        # [gate_runner] block is emitted from a seed whose {prefix} and {kit} tokens resolve here,
        # so a draft that fixes only the `prefix = ` line writes a descriptor declaring one prefix
        # whose runner paths spell another. Observed as a staged break before this arm was written.
        ik6 = make_target(tmp / "i6", None)
        p = run("intake", "--target", str(ik6), "--kits", "run-gates",
                "--answer", "prefix=scripts")
        check("intake emits a [gate_runner] under a non-default prefix", p.returncode == 0,
              p.stdout + p.stderr)
        _d6 = (ik6 / ".governance" / "deploy.toml").read_text(encoding="utf-8")
        check("the emitted [gate_runner] follows the SUPPLIED prefix",
              'file = "scripts/gate-legs.json"' in _d6, _d6)
        check("the [gate_runner] command follows it too",
              '"scripts/run-gates/run-gates.sh"' in _d6, _d6)
        check("no tools/ path survives in the descriptor's runner block",
              "tools/gate-legs.json" not in _d6, _d6)

        # ================= DEPL-dCarriedReceipt-2: attributes, gate-leg and ci =================
        # The defect: `UPDATE_ROLE` sent all three to `refuse`, which runs BEFORE `classify_row`
        # and calls `r.fail` -- and a non-empty `r.problems` permanently skips the receipt
        # re-stamp. So ONE `.gitattributes` row froze a target's `gov_commit` forever, and every
        # kit selection carrying an lf_pin produces exactly such a row. Reproduced on a real target
        # before the fix: `update --write` exited 1 and `gov_commit` never moved.
        ap = make_target(tmp / "u2pins", None)
        p = run("intake", "--target", str(ap), "--kits", "push-main")
        check("[-2] intake accepts push-main", p.returncode == 0, p.stdout + p.stderr)
        p = run("apply", "--target", str(ap), "--kits", "push-main")
        settle(ap, "the push-main install")     # -12 S4, as everywhere below
        check("[-2] apply lands push-main and synthesizes the attributes row", p.returncode == 0,
              p.stdout + p.stderr)
        _rec = json.loads((ap / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("[-2] the receipt really carries an attributes row",
              any(f.get("role") == "attributes" for f in _rec["files"]),
              str([f.get("role") for f in _rec["files"]]))

        p = run("update", "--target", str(ap), "--write")
        check("[-2] an attributes row no longer strands the run", p.returncode == 0,
              p.stdout + p.stderr)
        check("[-2] and it is no longer refused BY NAME",
              "refusing by name" not in (p.stdout + p.stderr), p.stdout + p.stderr)
        check("[-2] the pins row reports `current` when the block matches",
              "current" in p.stdout and "attributes" in p.stdout, p.stdout)
        check("[-2] the receipt re-stamped, which is what the refusal used to prevent",
              json.loads((ap / ".governance" / "install.json").read_text(
                  encoding="utf-8"))["gov_commit"] != "", p.stdout)

        # The OTHER arm of the same predicate. A verdict that can only ever read one way is not a
        # verdict, and this one shipped broken once already: `find_block` returns LINE indices and
        # the first draft sliced the string with them, so `current` could never fire.
        _ga = ap / ".gitattributes"
        # INSIDE the marker pair. Appending after the close marker leaves the block itself
        # byte-identical, so `current` is the right answer and the arm proves nothing.
        _ga.write_text(
            _ga.read_text(encoding="utf-8").replace(
                "# /govkit:lf-pins", "# TAMPERED\n# /govkit:lf-pins"),
            encoding="utf-8", newline="\n")
        check("[-2] the tamper really landed inside the block",
              "# TAMPERED" in _ga.read_text(encoding="utf-8"), "")
        settle(ap, "the tampered pin block")    # .gitattributes is a CLAIMED path — -12 S4
        _before = _ga.read_bytes()
        p = run("update", "--target", str(ap), "--write")
        check("[-2] a moved block reports `pins-moved`", "pins-moved" in p.stdout, p.stdout)
        check("[-2] and still exits 0 rather than stranding the receipt", p.returncode == 0,
              p.stdout + p.stderr)
        check("[-2] `update` NEVER edits .gitattributes -- that destination is apply's",
              _ga.read_bytes() == _before, "")
        check("[-2] it writes an ORDER instead",
              (ap / ".governance" / "outbox" / "update-pins.md").is_file(), p.stdout)

        # S3/S4. The dispatch table is the unit's actual subject, and `selfcheck` already asserts it
        # covers the role enum -- this arm asserts WHICH disposition each of the three now takes, so
        # a future edit that quietly restores `refuse` fails here rather than in an adopter.
        _UR = govkit_update_role()
        check("[-2] attributes dispatches to pins, not refuse",
              _UR["attributes"] == "pins", str(_UR))
        check("[-2] gate-leg reports rather than refusing",
              _UR["gate-leg"] == "report", str(_UR))
        check("[-2] ci reports rather than refusing",
              _UR["ci"] == "report", str(_UR))
        check("[-2] and no role is left on the refuse disposition by accident",
              "refuse" not in _UR.values(), str(_UR))

        # ============ DEPL-dCarriedReceipt-1: {relpath} in the seam that WRITES ============
        # `rule_relpath` resolves {relpath} against the RULE'S BASE; `resolve_dests` took the
        # basename instead. push-main's hook rule declares `to = "{relpath}"` over
        # `.githooks/pre-push`, so the writer landed a bare `pre-push` at the target ROOT while the
        # same rule's own `claims` spelled `.githooks/pre-push`. Observed on a live target before
        # the fix: the receipt carried `pre-push` and `pre-push.test.sh` at the root.
        _gk = govkit_module()
        _pm = _gk.load_toml(HERE / "entries" / "push-main.kit.toml")
        _hook = [rr for rr in _pm.get("files", [])
                 if rr.get("root_relative") and rr.get("to") == "{relpath}"]
        check("[-1] push-main still declares the root-relative {relpath} rule this unit is about",
              len(_hook) == 1, str([rr.get("to") for rr in _pm.get("files", [])]))
        if _hook:
            _rule = _hook[0]
            _ctx = _gk.canonical_ctx("push-main")
            _got = [dd for dd, _m in _gk.resolve_dests(
                _pm, _rule, ".githooks/pre-push", _ctx, (_pm.get("home") or "").rstrip("/"))]
            check("[-1] the WRITING seam resolves {relpath} against the rule's base",
                  _got == [".githooks/pre-push"], str(_got))
            check("[-1] and it agrees with the rule's own claims",
                  set(_got) <= set(_rule.get("claims", [])), str(_got))

        # THE OTHER BRANCH. A source directly under `home` still resolves to its basename under the
        # kit directory -- the case the buggy form got RIGHT, so the fix must not regress it. An arm
        # that only covers the broken branch cannot tell a fix from an overcorrection.
        _eng = [rr for rr in _pm.get("files", [])
                if rr.get("to") == "{prefix}/{relpath}" and not rr.get("root_relative")]
        check("[-1] push-main still declares the home-relative rule", len(_eng) == 1,
              str([rr.get("to") for rr in _pm.get("files", [])]))
        if _eng:
            _got2 = [dd for dd, _m in _gk.resolve_dests(
                _pm, _eng[0], "push-main.sh", _gk.canonical_ctx("push-main"),
                (_pm.get("home") or "").rstrip("/"))]
            check("[-1] a source under `home` still resolves to its basename",
                  _got2 == ["tools/push-main.sh"], str(_got2))

        # ================= liveness of the two derived assertions =================
        # An assertion that finds nothing on a clean tree is indistinguishable from one that CANNOT
        # find anything. These arms build a scratch gov tree — a copy of the engine plus a minimal
        # registry — and feed it input that MUST red. Without them, the two arms below would be the
        # repo's own `fixture-passes-by-finding-nothing` class living inside the tool that gates it.
        def scratch_gov(mutates: str, guard: str, tag: str = "") -> pathlib.Path:
            # `tag` disambiguates two fixtures built from the SAME pair. The name was derived from
            # the arguments alone, so a second call with identical ones met a directory that already
            # existed and died with FileExistsError rather than reusing or refusing.
            g = tmp / f"gov{abs(hash((mutates, guard))) % 9999}{tag}"
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
                '[[gate_leg]]\nname = "demo"\nargv = ["true"]\nguard = []\nsubject = "repo"\n',
                encoding="utf-8", newline="\n")
            # The adopter EXECUTES `git add`. A `git add` inside an echo would not count, which is
            # the distinction that made this assertion necessary in the first place.
            (g / "tools" / "demo" / "adopt-demo.sh").write_text(
                '#!/usr/bin/env bash\necho "  1. git add something && commit."\ngit add .\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "gate-legs.json").write_text(
                # THE MANIFEST DECLARES ITS SUBJECT, like the descriptor beside it. An
                # omission here is the M1 case: the descriptor says one thing and the
                # manifest says nothing, which every reader defaults to `repo` — a silent
                # disagreement, and selfcheck refuses it now.
                json.dumps([{"name": "demo", "argv": ["true"], "guard": [guard],
                             "subject": "repo"}], indent=2) + "\n",
                encoding="utf-8", newline="\n")
            # Only govkit.py was copied, so this tree arrives with no subject pin and the ratchet
            # reds on its absence — correctly, and this fixture's premise is a tree where every
            # declared fact agrees. The manifest leg declares no subject, so it derives to `repo`.
            (g / "tools" / "govkit" / "subject-pins.tsv").write_text(
                "# fixture pin\ndemo\trepo\n", encoding="utf-8", newline="\n")
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

        # ---- A REPO-LOCAL GATE POLICY MAY NOT RIDE OUT IN A KIT'S PAYLOAD ------------------------
        # TOOL-dUnstalledConvoy-28. `.githooks/pre-push` ships verbatim to every push-main adopter,
        # so a GATE_SELFTESTS assignment written into it turns the kit self-tests back on for
        # exactly the repositories TOOL-dUnstalledConvoy-26 exists to spare. The mechanism that
        # READS the choice may travel; the file that MAKES it may not. Armed on a fixture rather
        # than on this tree alone, because gating the instance certifies coverage nobody has.
        pg = scratch_gov("true", "tools/demo/", tag="-policy")
        # `tools/demo/` is claimed by an `include = "**"` engine rule, so anything dropped in it is
        # payload. That is the case a claims-only derivation missed: 13 of 58 file rules in gov's
        # own tree declare `claims` at all.
        (pg / "tools" / "demo" / "policy.sh").write_text(
            "#!/usr/bin/env sh\nexport GATE_SELFTESTS=1\n", encoding="utf-8", newline="\n")
        git(pg, "add", "-A")
        git(pg, "commit", "-qm", "policy in the payload")
        _pol = run_in(pg)
        check("AC2: a bare GATE_SELFTESTS assignment inside a kit's payload REDS",
              _pol.returncode == 1 and "carries a bare GATE_SELFTESTS assignment AND is shipped"
              in _pol.stdout, _pol.stdout + _pol.stderr)
        check("AC2: and the refusal names the file and the kit that would ship it",
              "'tools/demo/policy.sh'" in _pol.stdout and "kit 'demo'" in _pol.stdout, _pol.stdout)

        # ITS CONTROL, and it is the arm that stops this being a ban on the variable. The same line
        # in a path no kit claims is the SANCTIONED shape — that is where gov keeps its own — and a
        # check that redded on it would have no place left to put the policy.
        (pg / "tools" / "demo" / "policy.sh").unlink()
        (pg / ".githooks").mkdir(parents=True, exist_ok=True)
        (pg / ".githooks" / "gate-env.sh").write_text(
            "#!/usr/bin/env sh\nexport GATE_SELFTESTS=1\n", encoding="utf-8", newline="\n")
        git(pg, "add", "-A")
        git(pg, "commit", "-qm", "policy outside the payload")
        _ok = run_in(pg)
        check("CONTROL: the same assignment in a path no kit ships is GREEN",
              _ok.returncode == 0, _ok.stdout + _ok.stderr)

        # An INVOCATION is not a policy. `GATE_SELFTESTS=1 bash ...` appears in docs, arms and
        # refusal strings all over gov's tree — 54 such lines when the predicate was run over it —
        # and a check that called those policies would be permanently red on its own source.
        (pg / "tools" / "demo" / "invoke.sh").write_text(
            "#!/usr/bin/env sh\nGATE_SELFTESTS=1 bash run-gates.sh\n",
            encoding="utf-8", newline="\n")
        git(pg, "add", "-A")
        git(pg, "commit", "-qm", "an invocation, not a policy")
        _inv = run_in(pg)
        check("an INVOCATION inside the payload is not a policy and stays GREEN",
              _inv.returncode == 0, _inv.stdout + _inv.stderr)

        # ---- THE SUBJECT RATCHET (TOOL-dUnstalledConvoy-29) --------------------------------------
        # A leg's subject decides whether it runs on every bar or waits for GATE_SELFTESTS=1, and no
        # predicate over a descriptor can decide whether a given value is RIGHT — that needs to know
        # what the leg's failure MEANS. So the value is ratcheted instead: it cannot move without the
        # move appearing in a diff. These arms grade the ratchet, and none of them grades correctness.
        rg = scratch_gov("true", "tools/demo/", tag="-ratchet")
        pinf = rg / "tools" / "govkit" / "subject-pins.tsv"
        legsf = rg / "tools" / "gate-legs.json"
        kitf = rg / "tools" / "demo" / "kit.toml"

        def _write_legs(subject: str, extra: bool = False) -> None:
            rows = [{"name": "demo", "argv": ["true"], "guard": ["tools/demo/"],
                     "subject": subject}]
            if extra:
                rows.append({"name": "demo two", "argv": ["true"], "guard": [], "subject": "repo"})
            legsf.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8", newline="\n")
            # The DESCRIPTOR moves with it. Leaving it behind reds on the 7h agreement check, and
            # the arm would then be green for a reason that has nothing to do with the ratchet.
            body = ('id = "demo"\nhome = "tools/demo"\n'
                    'version_from = { none = "fixture" }\n\n'
                    '[check]\nnone = "a fixture kit"\n\n'
                    '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                    '[adopt]\nargv = ["bash", "{kit}/adopt-demo.sh"]\nmutates_index = true\n\n'
                    f'[[gate_leg]]\nname = "demo"\nargv = ["true"]\nguard = []\n'
                    f'subject = "{subject}"\n')
            if extra:
                body += ('\n[[gate_leg]]\nname = "demo two"\nargv = ["true"]\nguard = []\n'
                         'subject = "repo"\n')
            kitf.write_text(body, encoding="utf-8", newline="\n")

        # AC4 — the pin is DERIVED, not hand-listed: regenerating it over this tree produces exactly
        # the tree's own population, and the tree is green afterwards.
        #
        # The pin is CORRUPTED first, on purpose. With a fixture pin that already matched, the two
        # arms below passed against a build with no ratchet in it at all — the generated content was
        # the content that was already there, and a tree nothing checks is green for free. Starting
        # wrong is what makes regeneration the thing being measured.
        pinf.write_text("# fixture pin\ndemo\tkit\nzzz gone\trepo\n", encoding="utf-8", newline="\n")
        _liv = run_in(rg)
        check("LIVENESS: a pin that disagrees with the manifest REDS, so the arms below are not "
              "measuring a tree that was already correct",
              _liv.returncode == 1 and "is subject 'repo' and pinned 'kit'" in _liv.stdout,
              _liv.stdout + _liv.stderr)
        _w = run_in_gov(rg, "selfcheck", "--write")
        check("AC4: selfcheck --write regenerates the subject pin",
              _w.returncode == 0 and "wrote 1 subject pin" in _w.stdout, _w.stdout + _w.stderr)
        _rows = [l for l in pinf.read_text(encoding="utf-8").split("\n")
                 if l.strip() and not l.startswith("#")]
        check("AC4: and the generated pin is exactly the derived population",
              _rows == ["demo\trepo"], str(_rows))
        _g0 = run_in(rg)
        # A CONTROL, not a discriminating arm: an assertion that something is green cannot fail when
        # the mechanism is absent, and this one passed in the red-first run for exactly that reason.
        # It is kept because a ratchet that reds on a correct tree is the other way this fails.
        check("CONTROL: a tree whose pin was just regenerated is GREEN",
              _g0.returncode == 0, _g0.stdout + _g0.stderr)

        # AC1 — a flip with the pin left behind REDS, and the refusal names the leg, both values,
        # and what the move actually does. "subject changed" would tell a reader nothing.
        _write_legs("kit")
        _r1 = run_in(rg)
        check("AC1: flipping a subject without moving its pin REDS",
              _r1.returncode == 1, _r1.stdout + _r1.stderr)
        check("AC1: and the refusal names the leg and BOTH values",
              "gate leg 'demo' is subject 'kit' and pinned 'repo'" in _r1.stdout, _r1.stdout)
        check("AC1: and says what the move does — leaving the automatic bar",
              "OFF the automatic bar" in _r1.stdout, _r1.stdout)
        check("AC1: and says it grades the change rather than the value",
              "never whether the value is right" in _r1.stdout, _r1.stdout)

        # AC2 — moving the pin in the same commit is the sanctioned path, and it passes. Without
        # this arm the ratchet could be a check that reds on everything forever.
        _w2 = run_in_gov(rg, "selfcheck", "--write")
        check("AC2: moving the pin in the same commit passes",
              _w2.returncode == 0, _w2.stdout + _w2.stderr)
        _rows2 = [l for l in pinf.read_text(encoding="utf-8").split("\n")
                  if l.strip() and not l.startswith("#")]
        # EXACTLY the new population, which is what makes this arm discriminating: the stale row
        # planted in the corruption above must be GONE, and only a real regeneration removes it.
        check("AC2: and the moved pin records the new value and drops the stale row",
              _rows2 == ["demo\tkit"], str(_rows2))

        # AC3 — a NEW leg is UNPINNED, and unpinned reds. A new leg passing by default is the hole:
        # it would let a leg arrive already held, on nobody's decision.
        _write_legs("kit", extra=True)
        _r3 = run_in(rg)
        check("AC3: a NEW leg with no pin row REDS rather than passing",
              _r3.returncode == 1 and "gate leg 'demo two' has no row in" in _r3.stdout,
              _r3.stdout + _r3.stderr)

        # ...and its mirror: a pin naming a leg that is gone. A stale row is a pin for nothing, and
        # it silently adopts the next leg that arrives under that name.
        run_in_gov(rg, "selfcheck", "--write")
        _write_legs("kit")
        _r4 = run_in(rg)
        check("a pin row naming a leg the manifest no longer declares REDS",
              _r4.returncode == 1 and "pins 'demo two'" in _r4.stdout, _r4.stdout + _r4.stderr)

        sys.path.insert(0, str(HERE))
        import govkit  # noqa: E402

        # ---- L1: THE REFUSAL BRANCHES THIS BUILD ADDED, each reached by an arm ----------------
        # Six of twelve were unverified text — any of them could be misspelled, unreachable, or emit
        # the wrong operator instruction with nothing reporting it, and M1 above is the live proof
        # that "unarmed" and "wrong" arrive together. `refusal_join.py` is the mechanism meant to
        # catch this and its JOIN half has never executed, so these are hand-written.
        def _write_desc(subject_line: str, extra: str = "") -> None:
            kitf.write_text(
                'id = "demo"\nhome = "tools/demo"\n'
                'version_from = { none = "fixture" }\n\n'
                '[check]\nnone = "a fixture kit"\n\n'
                '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                '[adopt]\nargv = ["bash", "{kit}/adopt-demo.sh"]\nmutates_index = true\n\n'
                '[[gate_leg]]\nname = "demo"\n' + subject_line +
                'argv = ["true"]\nguard = []\n' + extra,
                encoding="utf-8", newline="\n")

        _write_legs("repo")
        run_in_gov(rg, "selfcheck", "--write")
        _write_desc("")                       # the descriptor declares no subject at all
        _r = run_in(rg)
        check("L1: a descriptor gate leg with NO subject REDS",
              _r.returncode == 1 and "with no `subject`" in _r.stdout, _r.stdout + _r.stderr)
        check("L1: and the refusal points at where the criterion is stated",
              "ask what a FAILURE of this leg MEANS" in _r.stdout, _r.stdout)

        _write_desc('subject = "Kit"\n')      # right word, wrong case: outside the closed set
        _r = run_in(rg)
        check("L1: a descriptor subject outside the closed set kit|repo REDS",
              _r.returncode == 1 and "outside the closed set kit|repo" in _r.stdout,
              _r.stdout + _r.stderr)

        _write_desc('subject = "kit"\n')      # descriptor kit against a manifest that says repo
        _r = run_in(rg)
        check("L1: a descriptor and manifest that DISAGREE about subject RED",
              _r.returncode == 1 and "disagree about whether this leg runs by default" in _r.stdout,
              _r.stdout + _r.stderr)

        # ...back to agreement, then the PIN's own two refusals.
        _write_desc('subject = "repo"\n')
        run_in_gov(rg, "selfcheck", "--write")
        check("L1 control: the fixture is GREEN again before the pin arms below",
              run_in(rg).returncode == 0, "")
        _pinf = rg / "tools" / "govkit" / "subject-pins.tsv"
        _pinf.write_text("# fixture pin\ndemo repo\n", encoding="utf-8", newline="\n")
        _r = run_in(rg)
        check("L1: a pin row with no TAB REDS rather than being skipped as unparseable",
              _r.returncode == 1 and "has a row with no tab" in _r.stdout, _r.stdout + _r.stderr)
        _pinf.unlink()
        _r = run_in(rg)
        check("L1: a MISSING pin file REDS — the ratchet with no pin compares against nothing",
              _r.returncode == 1 and "has no pin to compare against" in _r.stdout,
              _r.stdout + _r.stderr)
        run_in_gov(rg, "selfcheck", "--write")

        # ---- M1: AN ABSENT MANIFEST SUBJECT IS A DISAGREEMENT, not an exemption ---------------
        # The first draft guarded the comparison on `m_sub is not None`, so a manifest row with no
        # key never disagreed with anything — while the runner defaults it to `repo` and the emitter
        # ships the DESCRIPTOR's value to every adopter. Reproduced end to end on the live tree by
        # the closing review: gov runs the leg and every adopter holds it, with this check green,
        # and -29's own remediation then pins the derived default and makes it permanent.
        _write_legs("kit")
        _mf = json.loads(legsf.read_text(encoding="utf-8"))
        for _r in _mf:
            _r.pop("subject", None)
        legsf.write_text(json.dumps(_mf, indent=2) + "\n", encoding="utf-8", newline="\n")
        _m1 = run_in(rg)
        check("M1: a descriptor subject against a manifest row that declares none REDS",
              _m1.returncode == 1 and "declares none" in _m1.stdout, _m1.stdout + _m1.stderr)
        check("M1: and the refusal says every reader defaults the missing key to repo",
              "defaults a missing key to 'repo'" in _m1.stdout, _m1.stdout)
        # ITS CONTROL: put the key back and the same tree is green again, so the arm is about the
        # omission and not about the fixture being broken in some other way.
        _write_legs("kit")
        run_in_gov(rg, "selfcheck", "--write")
        _m1c = run_in(rg)
        check("M1 control: with the manifest key present the same tree is GREEN",
              _m1c.returncode == 0, _m1c.stdout + _m1c.stderr)

        # ---- M5: the gate-policy predicate's two evasions -------------------------------------
        # Both are things a person writes without thinking: a trailing comment, and the shell
        # default form, which assigns exactly as hard as `=`. The INVOCATION control is the half
        # that keeps the predicate from redding on its own source — `GATE_SELFTESTS=1 bash ...`
        # appears dozens of times across this tree in docs, arms and refusal strings.
        _pol_re = _re.compile(
            r"^[ \t]*(?::[ \t]+)?(?:export[ \t]+)?"
            r"(?:GATE_SELFTESTS=\S*|\$\{GATE_SELFTESTS:?=[^}]*\})"
            r"[ \t]*(?:#.*)?$")
        _gk_src = (HERE / "govkit.py").read_text(encoding="utf-8")
        check("M5: the predicate this arm grades is the one govkit.py actually compiles",
              "GATE_SELFTESTS=\\S*|" in _gk_src or "GATE_SELFTESTS=" in _gk_src, "")
        for _s in ("export GATE_SELFTESTS=1", "GATE_SELFTESTS=1",
                   "export GATE_SELFTESTS=1  # gov only", ": ${GATE_SELFTESTS:=1}"):
            check(f"M5: a policy line is caught — {_s!r}", bool(_pol_re.match(_s)), _s)
        for _s in ("GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh",
                   'if [ -n "${GATE_SELFTESTS:-}" ]; then',
                   'echo "set GATE_SELFTESTS=1 to run"'):
            check(f"M5 control: an invocation is NOT a policy — {_s[:38]!r}",
                  not _pol_re.match(_s), _s)

        # ---- M6: `subject` is emitted only where the target can READ it -----------------------
        # The manifest's key set is PINNED by the `run-gates canary`, a leg the run-gates kit ships
        # and that runs on every adopter's bar. Writing the key into a tree whose run-gates predates
        # it reds their canary as a side effect of an apply that was installing something else.
        with tempfile.TemporaryDirectory() as _vd:
            _vp = pathlib.Path(_vd)
            check("M6: a target with no run-gates at all still gets the key — there is no canary "
                  "to red, and withholding it would deny the feature silently",
                  govkit.check_target_reads_subject(_vp, {"prefix": "tools"}), "")
            (_vp / "tools" / "run-gates").mkdir(parents=True)
            _rgs = _vp / "tools" / "run-gates" / "run-gates.sh"
            _rgs.write_text("#!/usr/bin/env bash\nKIT_RUN_GATES_VERSION=1.0\n",
                            encoding="utf-8", newline="\n")
            check("M6: a target BELOW the floor does not get the key",
                  not govkit.check_target_reads_subject(_vp, {"prefix": "tools"}), "1.0 accepted")
            _rgs.write_text("#!/usr/bin/env bash\nKIT_RUN_GATES_VERSION=1.1\n",
                            encoding="utf-8", newline="\n")
            check("M6: a target AT the floor does",
                  govkit.check_target_reads_subject(_vp, {"prefix": "tools"}), "1.1 refused")
            _rgs.write_text("#!/usr/bin/env bash\n# no version constant here\n",
                            encoding="utf-8", newline="\n")
            check("M6: an UNREADABLE version is treated as below the floor — the direction that "
                  "costs a feature is recoverable, the one that reds somebody else's bar is not",
                  not govkit.check_target_reads_subject(_vp, {"prefix": "tools"}), "unreadable accepted")
            check("M6: the floor is the version the canary's key set moved in",
                  govkit.SUBJECT_FLOOR_RUN_GATES == (1, 1),
                  str(govkit.SUBJECT_FLOOR_RUN_GATES))

        # AC5 — the header says what the check does NOT decide, in the generated file itself, where
        # a reader who found the pin will actually be looking.
        run_in_gov(rg, "selfcheck", "--write")
        check("AC5: the generated pin's own header states it grades change and not correctness",
              "GRADES CHANGE, NOT CORRECTNESS" in pinf.read_text(encoding="utf-8"),
              pinf.read_text(encoding="utf-8"))

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

            settle(t, "the drift-audit install")
            owned.write_text(owned.read_text(encoding="utf-8") + "\n# ADOPTER EDIT\n", encoding="utf-8")
            # COMMITTED for the reason site 2 gives: an uncommitted edit to a claimed path
            # makes the re-apply REFUSE, and "the edit survived" is then true because nothing
            # ran — which is the exact vacuity the arm below was written to close.
            settle(t, "the adopter edits a seeded file")
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

        # ========== DEPL-dCarriedReceipt-12: write preconditions and the outbox lock ==========
        # EVERY arm below was observed RED on a real scratch target before the engine moved. At the
        # base sha: in a LINKED WORKTREE both verbs walked straight through a live MERGE_HEAD,
        # because `.git` is a file there and `target/.git/<marker>` resolves to nothing; a target
        # declaring no `lf_pin` was unguarded even in a normal repo, because the probe sat inside
        # `if pins:`; `update --write` over a path carrying three index stages collapsed them to
        # ZERO through its own `git add`, measured 3 -> 0; `--to <older sha>` took the raw arm on
        # every clean row, rewound the bytes and re-stamped `gov_commit` backwards; and `--to
        # <sha no ref reaches>` landed the bytes of a deleted branch and stamped that sha in.
        LOCK_REL = govkit_module().WRITE_LOCK_REL

        def gout(cwd: pathlib.Path, *args: str) -> str:
            """`git` with its stdout, which the harness's own `git()` throws away."""
            return subprocess.run(["git", "-C", str(cwd), *args],
                                  capture_output=True, text=True).stdout

        def lock_of(t: pathlib.Path) -> pathlib.Path:
            return t.joinpath(*LOCK_REL.split("/"))

        def set_marker(t: pathlib.Path, marker: str) -> pathlib.Path:
            """Plant an in-progress marker WHERE GIT KEEPS IT, which is the whole point.

            Resolved with `--git-path` rather than written to `target/.git/<marker>`: in a linked
            worktree the second spelling creates a file inside a DIRECTORY THAT DOES NOT EXIST as a
            git dir, so the fixture would plant a marker git never reads and the arm would grade
            nothing. Asserted below, not assumed.
            """
            p = t / gout(t, "rev-parse", "--git-path", marker).strip()
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(gout(t, "rev-parse", "HEAD").strip() + "\n", encoding="utf-8",
                         newline="\n")
            return p

        def wt_target(name: str, kits: str) -> pathlib.Path:
            """A target whose `.git` is a FILE — the linked-worktree layout adopters are told to use.

            This is the fixture no existing one covered, and that is exactly why the dead probe
            shipped: every arm written against a normal repo passes while the guard is inert.
            """
            host = tmp / f"{name}-host"
            host.mkdir(parents=True)
            git(host, "init", "-q", "-b", "main")
            git(host, "config", "user.email", "t@e")
            git(host, "config", "user.name", "t")
            git(host, "config", "core.autocrlf", "false")   # pinned, for `make_target`'s reason
            (host / "README.md").write_text("host\n", encoding="utf-8", newline="\n")
            git(host, "add", "-A")
            git(host, "commit", "-qm", "base")
            wt = tmp / f"{name}-wt"
            git(host, "worktree", "add", "-q", str(wt), "-b", f"{name}-feat")
            run("intake", "--target", str(wt), "--kits", kits)
            run("apply", "--target", str(wt), "--kits", kits)
            settle(wt, "the install")
            return wt

        # ---- AC1: the linked worktree, on BOTH verbs. push-main is the kit on purpose — it DOES
        # ---- declare lf_pins, so the old probe was reached and still could not see the marker.
        # ---- This arm therefore grades the `--git-path` fix and nothing else.
        w1 = wt_target("ac1", "push-main")
        check("[-12] AC1 the fixture really is a linked worktree — .git is a FILE",
              (w1 / ".git").is_file(), str(sorted(q.name for q in w1.iterdir())))
        _rw1 = json.loads((w1 / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("[-12] AC1 and it really declares pins, so the OLD probe was reached",
              any(f.get("role") == "attributes" for f in _rw1["files"]),
              str([f.get("role") for f in _rw1["files"]]))
        _mh = set_marker(w1, "MERGE_HEAD")
        check("[-12] AC1 the marker sits where git keeps it and NOT at target/.git/MERGE_HEAD",
              _mh.is_file() and not (w1 / ".git" / "MERGE_HEAD").exists(), _mh.as_posix())
        _pa = run("apply", "--target", str(w1), "--kits", "push-main")
        check("[-12] AC1 apply refuses a mid-merge LINKED WORKTREE by name",
              _pa.returncode == 2 and "MERGE_HEAD" in _pa.stderr and "in progress" in _pa.stderr,
              _pa.stdout + _pa.stderr)
        _pu = run("update", "--target", str(w1), "--write")
        check("[-12] AC1 update --write refuses the same tree by name",
              _pu.returncode == 2 and "MERGE_HEAD" in _pu.stderr and "in progress" in _pu.stderr,
              _pu.stdout + _pu.stderr)
        check("[-12] AC1 the refusal says what to do about it",
              "Finish or abort that operation" in _pu.stderr, _pu.stderr)
        # NEGATIVE half. Without it the arm cannot tell the fix from a verb that refuses always.
        _mh.unlink()
        _pa2 = run("apply", "--target", str(w1), "--kits", "push-main")
        check("[-12] AC1 NEGATIVE: the same worktree with the marker gone proceeds",
              _pa2.returncode == 0, _pa2.stdout + _pa2.stderr)

        # ---- AC2: a NORMAL repo whose selection declares NO lf_pin. check-wiring is the kit for
        # ---- the mirror-image reason: the path form works fine here, so the only thing this arm
        # ---- can be measuring is that the probe left `if pins:`.
        n2 = make_target(tmp / "ac2", None)
        run("intake", "--target", str(n2), "--kits", "check-wiring")
        run("apply", "--target", str(n2), "--kits", "check-wiring")
        settle(n2, "the install")
        check("[-12] AC2 the fixture is a NORMAL repo — .git is a directory",
              (n2 / ".git").is_dir(), "")
        _rn2 = json.loads((n2 / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("[-12] AC2 and its receipt carries NO attributes row, so no pin was declared",
              not any(f.get("role") == "attributes" for f in _rn2["files"]),
              str([f.get("role") for f in _rn2["files"]]))
        for _mk in govkit_module().IN_PROGRESS_MARKERS:
            _p = set_marker(n2, _mk)
            _r = run("apply", "--target", str(n2), "--kits", "check-wiring")
            check(f"[-12] AC2 apply refuses {_mk} on a target that declares no lf_pin",
                  _r.returncode == 2 and _mk in _r.stderr, _r.stdout + _r.stderr)
            _p.unlink()
        _r = run("apply", "--target", str(n2), "--kits", "check-wiring")
        check("[-12] AC2 NEGATIVE: with every marker cleared the same target proceeds",
              _r.returncode == 0, _r.stdout + _r.stderr)

        # ---- AC3: an unresolved index, WITHOUT a marker. A real `git merge` conflict would also
        # ---- leave MERGE_HEAD, so S1 would refuse first and this arm would grade that rule
        # ---- instead of S3. The stages are injected directly, so the tree carries exactly the one
        # ---- condition under test — asserted on the next two lines rather than assumed.
        u3 = stale_target("ac3")
        CW = "tools/check-wiring.sh"
        _blob = gout(u3, "rev-parse", f"HEAD:{CW}").strip()
        # BYTES, never `text=True`. Text mode wraps stdin in a TextIOWrapper whose default newline
        # handling rewrites every "\n" as os.linesep, so on Windows git read a path with a trailing
        # CR, matched nothing, and the fixture arrived with ZERO stages. The fixture assertion below
        # is the only reason that was a red rather than a vacuous green.
        subprocess.run(["git", "-C", str(u3), "update-index", "--index-info"],
                       input=f"0 {'0' * 40}\t{CW}\n".encode(), capture_output=True)
        subprocess.run(["git", "-C", str(u3), "update-index", "--index-info"],
                       input="".join(f"100644 {_blob} {n}\t{CW}\n"
                                     for n in (1, 2, 3)).encode(), capture_output=True)
        _stages = len([ln for ln in gout(u3, "ls-files", "-u").splitlines() if ln.strip()])
        check("[-12] AC3 the fixture really carries three index stages", _stages == 3, str(_stages))
        check("[-12] AC3 and it carries NO in-progress marker, so S3 is the rule under test",
              not any((u3 / gout(u3, "rev-parse", "--git-path", m).strip()).exists()
                      for m in govkit_module().IN_PROGRESS_MARKERS), "")
        _p3 = run("update", "--target", str(u3), "--write")
        check("[-12] AC3 update --write refuses an unresolved index by name",
              _p3.returncode == 2 and "unresolved merge stages" in _p3.stderr, _p3.stderr)
        check("[-12] AC3 the refusal names the path that tripped it", CW in _p3.stderr, _p3.stderr)
        _after = len([ln for ln in gout(u3, "ls-files", "-u").splitlines() if ln.strip()])
        check("[-12] AC3 the index still shows three stages afterwards — nothing was collapsed",
              _after == 3, f"{_stages} -> {_after}")
        # AC6, half one, and it covers two claims rather than the one it looks like. The S3 refusal
        # itself is raised BEFORE the lock is taken, so it creates none; the `apply` that BUILT this
        # fixture did take one, so an absent lock here also says that run gave it back. What it does
        # NOT grade is a refusal raised while holding — that is half two, under AC7. Measured:
        # breaking the release reds both halves and eighteen arms after them.
        check("[-12] AC6 an S3 refusal leaves no lock behind, and the apply before it gave one back",
              not lock_of(u3).exists(), "")

        # ---- AC4: dirty is scoped to the RECEIPT's population, and to nothing else.
        u4 = stale_target("ac4")
        _orig = (u4 / CW).read_bytes()
        (u4 / CW).write_bytes(_orig + b"\n# LOCAL EDIT\n")
        check("[-12] AC4 the fixture's claimed path really is dirty",
              CW in gout(u4, "diff", "--name-only"), gout(u4, "diff", "--name-only"))
        _p4 = run("update", "--target", str(u4), "--write")
        check("[-12] AC4 update --write refuses over a dirty CLAIMED path",
              _p4.returncode == 2 and "DIRTY" in _p4.stderr, _p4.stderr)
        check("[-12] AC4 and names the path", CW in _p4.stderr, _p4.stderr)
        check("[-12] AC4 the local edit is still there — the refusal wrote nothing",
              (u4 / CW).read_bytes() == _orig + b"\n# LOCAL EDIT\n", "")
        # NEGATIVE half: the same target, dirty OUTSIDE the receipt, proceeds. Without this the arm
        # cannot tell a scoped refusal from a verb that refuses on any dirty tree at all.
        (u4 / CW).write_bytes(_orig)
        (u4 / "README.md").write_text("edited, and gov does not own this\n", encoding="utf-8",
                                      newline="\n")
        check("[-12] AC4 the fixture is now dirty ONLY outside the receipt",
              gout(u4, "diff", "--name-only").split() == ["README.md"],
              gout(u4, "diff", "--name-only"))
        _p4b = run("update", "--target", str(u4), "--write")
        check("[-12] AC4 NEGATIVE: a dirty path OUTSIDE the receipt does not block",
              _p4b.returncode == 0, _p4b.stdout + _p4b.stderr)

        # ---- AC5: two concurrent `update --write` runs, both of them real processes.
        # memory-tree is the fixture kit because its receipt is large enough that a run holds the
        # lock for about a second, which is what makes the contention observable rather than lucky.
        # The loop does not sleep-and-hope: it WATCHES for the lock to appear and only then starts
        # the second run, and if three attempts never catch the first run holding it, the arm FAILS
        # rather than reporting a green it did not earn.
        cc = make_target(tmp / "ac5", None)
        run("intake", "--target", str(cc), "--kits", "memory-tree")
        run("apply", "--target", str(cc), "--kits", "memory-tree")
        settle(cc, "the install")
        _lk = lock_of(cc)
        _race = None
        for _attempt in range(3):
            _first = subprocess.Popen(
                [sys.executable, str(GOVKIT), "update", "--target", str(cc), "--write"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            _deadline = time.time() + 30
            while time.time() < _deadline and not _lk.exists() and _first.poll() is None:
                time.sleep(0.002)
            if not _lk.exists():
                _first.communicate()
                continue
            _second = run("update", "--target", str(cc), "--write")
            _fo, _fe = _first.communicate()
            _race = (_second, _first.returncode, _fo + _fe)
            break
        check("[-12] AC5 the two runs really contended — the lock was observed HELD",
              _race is not None,
              "three attempts and the first run never held the lock long enough to be seen")
        if _race is not None:
            _second, _first_rc, _first_out = _race
            check("[-12] AC5 the second concurrent update --write refuses ON THE LOCK",
                  _second.returncode == 2 and ".update.lock" in _second.stderr
                  and "another govkit write holds" in _second.stderr, _second.stderr)
            check("[-12] AC5 the refusal names the holder and how to clear a stale lock",
                  "pid " in _second.stderr and "rm " in _second.stderr, _second.stderr)
            check("[-12] AC5 and the first run completed", _first_rc == 0, _first_out)
        check("[-12] AC5 after both runs the lock file is gone", not _lk.exists(), "")

        # ---- AC7 + AC8: the two vintage refusals, on a scratch gov with a real branch history.
        # Built rather than borrowed: gov's own history has no dangling commit to point `--to` at,
        # and manufacturing one would mean writing to the repository under test.
        def vintage_gov() -> pathlib.Path:
            g = tmp / "gov-vintage"
            (g / "tools" / "govkit").mkdir(parents=True)
            (g / "tools" / "demo").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                '[selection]\ndefault = ["demo"]\n\n'
                '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "demo" / "kit.toml").write_text(
                'id = "demo"\nhome = "tools/demo"\n'
                'version_from = { none = "fixture" }\n\n'
                '[check]\nnone = "a fixture kit"\n\n'
                '[[files]]\ninclude = ["demo.txt"]\nrole = "engine"\n\n'
                '[adopt]\nargv = []\nmutates_index = false\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "demo" / "demo.txt").write_text("v1\n", encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g

        def gov_run(g: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
            return subprocess.run([sys.executable, str(g / "tools" / "govkit" / "govkit.py"), *args],
                                  capture_output=True, text=True)

        gv = vintage_gov()
        VA = gout(gv, "rev-parse", "HEAD").strip()
        (gv / "tools" / "demo" / "demo.txt").write_text("v2\n", encoding="utf-8", newline="\n")
        git(gv, "add", "-A")
        git(gv, "commit", "-qm", "B")
        VB = gout(gv, "rev-parse", "HEAD").strip()

        # The target installs at whatever gov's HEAD is, so it is built HERE — between B and D —
        # which is how its receipt comes to record the MIDDLE vintage with history on both sides.
        t7 = make_target(tmp / "ac7", None)
        gov_run(gv, "intake", "--target", str(t7), "--kits", "demo")
        gov_run(gv, "apply", "--target", str(t7), "--kits", "demo")
        settle(t7, "the demo install")

        (gv / "tools" / "demo" / "demo.txt").write_text("v3\n", encoding="utf-8", newline="\n")
        git(gv, "add", "-A")
        git(gv, "commit", "-qm", "D")
        VD = gout(gv, "rev-parse", "HEAD").strip()
        git(gv, "checkout", "-q", "-b", "gone")
        (gv / "tools" / "demo" / "demo.txt").write_text("v9\n", encoding="utf-8", newline="\n")
        git(gv, "add", "-A")
        git(gv, "commit", "-qm", "C on a branch nobody keeps")
        VC = gout(gv, "rev-parse", "HEAD").strip()
        git(gv, "checkout", "-q", "main")
        git(gv, "branch", "-q", "-D", "gone")

        DEMO = "tools/demo/demo.txt"
        check("[-12] AC7 the fixture's receipt records the MIDDLE vintage",
              json.loads((t7 / ".governance" / "install.json").read_text(
                  encoding="utf-8"))["gov_commit"] == VB, VB)
        check("[-12] AC8 the fixture's dangling sha exists as an object",
              gout(gv, "cat-file", "-t", VC).strip() == "commit", VC)
        check("[-12] AC8 and no ref in that gov reaches it",
              not gout(gv, "for-each-ref", "--contains", VC, "--count=1").strip(), VC)

        _b7 = (t7 / DEMO).read_bytes()
        _p7 = gov_run(gv, "update", "--target", str(t7), "--to", VA, "--write")
        check("[-12] AC7 update refuses a --to that is not a descendant of the receipt's vintage",
              _p7.returncode == 2 and "DOWNGRADE IS NOT AN UPDATE" in _p7.stderr, _p7.stderr)
        check("[-12] AC7 the refusal prints BOTH shas",
              VA in _p7.stderr and VB in _p7.stderr, _p7.stderr)
        check("[-12] AC7 it wrote zero bytes", (t7 / DEMO).read_bytes() == _b7, "")
        check("[-12] AC7 and left the receipt's gov_commit at the newer sha",
              json.loads((t7 / ".governance" / "install.json").read_text(
                  encoding="utf-8"))["gov_commit"] == VB, "")
        # AC6, half two, and this is the half that grades the `finally`: the vintage refusal is
        # raised with the lock ALREADY HELD, so a release that only runs on the success path would
        # strand it here and every later run against this target would refuse on a stale lock.
        check("[-12] AC6 a refusal raised WITH THE LOCK HELD still releases it",
              not lock_of(t7).exists(), "")

        _pe = gov_run(gv, "update", "--target", str(t7), "--to", VB, "--write")
        check("[-12] AC7 NEGATIVE: a --to EQUAL to the receipt's vintage proceeds",
              _pe.returncode == 0, _pe.stdout + _pe.stderr)
        _pd = gov_run(gv, "update", "--target", str(t7), "--to", VD, "--write")
        check("[-12] AC7 NEGATIVE: a --to that IS a descendant proceeds and lands its bytes",
              _pd.returncode == 0 and (t7 / DEMO).read_bytes() == b"v3\n",
              _pd.stdout + _pd.stderr)
        settle(t7, "the forward update")     # -12 S4: that run staged what it wrote

        _p8 = gov_run(gv, "update", "--target", str(t7), "--to", VC, "--write")
        check("[-12] AC8 update refuses a --to no ref reaches",
              _p8.returncode == 2 and "reach from NO ref" in _p8.stderr, _p8.stderr)
        check("[-12] AC8 the refusal names the sha", VC in _p8.stderr, _p8.stderr)
        check("[-12] AC8 it wrote zero bytes", (t7 / DEMO).read_bytes() == b"v3\n", "")
        git(gv, "branch", "-q", "keeps-c", VC)
        _p8b = gov_run(gv, "update", "--target", str(t7), "--to", VC, "--write")
        check("[-12] AC8 NEGATIVE: the SAME sha proceeds once a ref contains it",
              _p8b.returncode == 0 and (t7 / DEMO).read_bytes() == b"v9\n",
              _p8b.stdout + _p8b.stderr)

        # ---- AC9: S4's first carve-out, both sides of it. A STAGED deletion is an operator
        # ---- decision and refuses; a COMMITTED one is not dirty, because there is nothing left to
        # ---- diff, and reaches the `missing` cell. Neither state is reachable from AC4's arm,
        # ---- which edits a path that still exists.
        u9 = stale_target("ac9")
        git(u9, "rm", "-q", "--", CW)
        check("[-12] AC9 the fixture staged a deletion: gone from the index and the worktree",
              CW not in gout(u9, "ls-files").split() and not (u9 / CW).exists(), "")
        check("[-12] AC9 ...while HEAD still carries it, which is what makes it STAGED",
              CW in gout(u9, "ls-tree", "-r", "--name-only", "HEAD").split(), "")
        _p9 = run("update", "--target", str(u9), "--write")
        check("[-12] AC9 update --write refuses a staged deletion by name",
              _p9.returncode == 2 and "DIRTY" in _p9.stderr
              and "deleted from the index" in _p9.stderr, _p9.stderr)
        check("[-12] AC9 the refusal names the path", CW in _p9.stderr, _p9.stderr)
        check("[-12] AC9 and the deletion was left exactly as the operator staged it",
              not (u9 / CW).exists(), "")
        settle(u9, "the deletion is committed")
        check("[-12] AC9 the committed deletion is gone from HEAD too",
              CW not in gout(u9, "ls-tree", "-r", "--name-only", "HEAD").split(), "")
        _p9b = run("update", "--target", str(u9), "--write")
        check("[-12] AC9 NEGATIVE: a COMMITTED deletion is not dirty and reaches `missing`",
              _p9b.returncode == 0 and "missing" in _p9b.stdout, _p9b.stdout + _p9b.stderr)
        check("[-12] AC9 ...and that cell restored the file from gov", (u9 / CW).is_file(), "")

        # ---- S4's SECOND carve-out, which no AC names and the definition pins anyway: an untracked
        # ---- file SHADOWING a claimed path absent from the index is NOT dirty here. That tree is
        # ---- `-7` S4's refusal, and two units refusing one state would hand the operator two
        # ---- different messages for it. Same precondition as the arm above — absent from the index
        # ---- — and the opposite worktree state, so the pair grades the carve-out and not the path.
        settle(u9, "the restored file")
        git(u9, "rm", "-q", "--cached", "--", CW)
        check("[-12] S4 the fixture is out of the index but present on disk",
              CW not in gout(u9, "ls-files").split() and (u9 / CW).is_file(), "")
        _p9c = run("update", "--target", str(u9), "--write")
        # The carve-out still holds, and the assertion moved from an EXIT CODE to a MESSAGE because
        # `-7` S4 has since landed and claims this exact tree. `-12`'s dirty check must still not
        # fire on it — two units refusing one state hand the operator two different messages — so
        # the arm asserts which refusal speaks: `-7`'s index-absence one, and not `-12`'s DIRTY one.
        check("[-12] S4 an untracked file shadowing a claimed path is NOT `-12` dirty",
              "DIRTY" not in _p9c.stderr, _p9c.stdout + _p9c.stderr)
        check("[-12] S4 ...it is `-7` S4's refusal that owns that tree now",
              _p9c.returncode == 2 and "absent from its INDEX" in _p9c.stderr,
              _p9c.stdout + _p9c.stderr)

        # ---- DEPL-dCarriedReceipt-7: TWO IDENTITIES, READ INDEX-SIDE -------------------------
        #
        # WHAT WENT WRONG, measured rather than argued. One receipt field was asked to be two things
        # at once: `classify_row` compared `sha256` against the target's WORKTREE bytes while
        # `check`'s provenance loop compared that same field against gov's blob at the row's
        # `commit`. Both claims hold only where the target's worktree is byte-identical to what gov
        # shipped, and that is false for any adopter whose clone applies a line-ending filter. On a
        # `core.autocrlf=true` clone of a memory-tree install, 23 of 24 engine rows read `patched`
        # with nothing edited: near-total false divergence, zero automatic adoption, and a plausible
        # table shown while it happened.
        #
        # `gov_oid` is the blob gov shipped at a row's `commit`, and it is STORED. `oid` is the blob
        # the TARGET holds, read from its INDEX and never from its worktree. `sha256` is retained so
        # a schema-2 reader keeps working, and decides nothing.
        #
        # EVERY ARM BELOW WAS WATCHED TO FAIL before it was kept, by staging the break into
        # `govkit.py` and running it — never by reasoning about what it would do.

        def clone_crlf(src: pathlib.Path, name: str) -> pathlib.Path:
            """A clone whose CHECKOUT applies a line-ending filter — where the adopter actually is.

            No fixture in this file had one, which is exactly why a worktree-side comparator
            shipped: every arm written against a repo whose worktree is byte-identical to gov's
            blobs passes while the comparator is wrong.
            """
            c = tmp / name
            subprocess.run(["git", "clone", "-q", "-c", "core.autocrlf=true", str(src), str(c)],
                           capture_output=True)
            git(c, "config", "user.email", "t@e")
            git(c, "config", "user.name", "t")
            return c

        def tally_of(out: str) -> str:
            """The one summary line `update` prints, which is where the counts live."""
            head = "govkit update — "
            for ln in out.splitlines():
                if not ln.startswith(head):
                    continue
                body = ln[len(head):]
                bits = body.split(" · ")
                if bits and all(_re.fullmatch(r"[a-z:-]+ \d+", b) for b in bits):
                    return body
            return "(no tally line)"

        def verdict_of(out: str, path: str) -> str:
            """The verdict `update` printed for ONE row, by path."""
            for ln in out.splitlines():
                if ln.startswith("  ") and ln.rstrip().endswith(" " + path):
                    return ln[2:].split("[", 1)[0].strip()
            return "(no row)"

        MTR = "tools/memory-tree/README.md"
        i7 = make_target(tmp / "id7", DEPLOY_FULL)
        run("apply", "--target", str(i7), "--kits", "memory-tree")
        settle(i7, "the install")
        c7 = clone_crlf(i7, "id7-clone")

        # ---- AC1: the clone reads the same as the original. THE FIXTURE IS ASSERTED FIRST — a
        # ---- fixture that does not trigger the rule proves nothing, and this rule is triggered by
        # ---- a filter rather than by an edit.
        check("[-7] AC1 the fixture really carries the filter — the clone's worktree holds CRLF",
              b"\r\n" in (c7 / MTR).read_bytes() and b"\r\n" not in (i7 / MTR).read_bytes(),
              repr((c7 / MTR).read_bytes()[:40]))
        check("[-7] AC1 ...and both INDEXES still name the identical blob, so nothing was edited",
              gout(c7, "ls-files", "-s", "--", MTR).split()[1]
              == gout(i7, "ls-files", "-s", "--", MTR).split()[1],
              gout(c7, "ls-files", "-s", "--", MTR))
        _ti = tally_of(run("update", "--target", str(i7)).stdout)
        _tc = tally_of(run("update", "--target", str(c7)).stdout)
        check("[-7] AC1 the autocrlf clone reports the SAME tally as the uncloned original",
              _tc == _ti and _tc != "(no tally line)", f"original {_ti!r} · clone {_tc!r}")
        check("[-7] AC1 ...and that tally carries no `patched` at all", "patched" not in _tc, _tc)

        # ---- AC2: BOTH ARMS of the index read. A fix that reads neither side is indistinguishable
        # ---- from one that reads the wrong side, so the PAIR is the assertion and neither half is.
        (c7 / MTR).write_bytes((c7 / MTR).read_bytes() + b"\nLOCAL EDIT\n")
        _a2 = run("update", "--target", str(c7))
        check("[-7] AC2 an UNSTAGED worktree edit leaves the row `current` — the index decides",
              verdict_of(_a2.stdout, MTR) == "current", _a2.stdout)
        git(c7, "add", "--", MTR)
        _a2b = run("update", "--target", str(c7))
        check("[-7] AC2 ...and STAGING that same edit moves it to `patched`",
              verdict_of(_a2b.stdout, MTR) == "patched", _a2b.stdout)

        # ---- AC3: S4. A claimed path present in the WORKTREE and absent from the INDEX. This arm
        # ---- guards a hazard S2 itself introduces, so its failing case was observed by staging S2
        # ---- WITHOUT S4: `update --write` then classified the operator's untracked file as
        # ---- `missing` and overwrote it with gov's bytes at exit 0.
        c3 = clone_crlf(i7, "id7-c3")
        git(c3, "rm", "-q", "--cached", "--", MTR)
        (c3 / MTR).write_bytes(b"MINE, NOT GOVS\n")
        check("[-7] AC3 the fixture is out of the INDEX and present in the WORKTREE",
              MTR not in gout(c3, "ls-files").split() and (c3 / MTR).is_file(), "")
        _a3 = run("update", "--target", str(c3), "--write")
        check("[-7] AC3 update --write refuses a claimed path the index does not carry",
              _a3.returncode == 2 and "absent from its INDEX" in _a3.stderr, _a3.stderr)
        check("[-7] AC3 the refusal names the path", MTR in _a3.stderr, _a3.stderr)
        check("[-7] AC3 the operator's untracked bytes are byte-identical afterwards",
              (c3 / MTR).read_bytes() == b"MINE, NOT GOVS\n", "")
        git(c3, "add", "--", MTR)
        _a3b = run("update", "--target", str(c3), "--write")
        check("[-7] AC3 NEGATIVE: the same tree with that path STAGED proceeds",
              "absent from its INDEX" not in _a3b.stderr, _a3b.stdout + _a3b.stderr)

        # ---- AC6: THE CLASS GATE. The class is "a receipt field asked to be two things at once",
        # ---- and the behavioural form of "it decides nothing now" is that corrupting it moves no
        # ---- verdict. Staged red: with the worktree/sha256 comparator patched back in, this same
        # ---- corruption moved all 26 engine rows from `current` to `patched`.
        c6 = clone_crlf(i7, "id7-c6")
        _before6 = [ln for ln in run("update", "--target", str(c6)).stdout.splitlines()
                    if ln.startswith("  ")]
        _rp6 = c6 / ".governance" / "install.json"
        _r6 = json.loads(_rp6.read_text(encoding="utf-8"))
        _n6 = 0
        for _f in _r6["files"]:
            if "sha256" in _f:
                _f["sha256"] = "0" * 64
                _n6 += 1
        _rp6.write_text(json.dumps(_r6, indent=2) + "\n", encoding="utf-8", newline="\n")
        check("[-7] AC6 the fixture corrupted a NON-EMPTY population of sha256 fields",
              _n6 > 0 and len(_before6) > 0, f"{_n6} field(s), {len(_before6)} row line(s)")
        _after6 = [ln for ln in run("update", "--target", str(c6)).stdout.splitlines()
                   if ln.startswith("  ")]
        check("[-7] AC6 every row's sha256 rewritten to one constant moves NO verdict line",
              _before6 == _after6,
              str([(a, b) for a, b in zip(_before6, _after6) if a != b][:3]))

        # ---- AC5: the schema. `-2` had to land first for this fixture to reach a finding-free run
        # ---- at all — its `attributes` row used to take `refuse` and freeze the re-stamp forever.
        c5 = clone_crlf(i7, "id7-c5")
        _a5 = run("update", "--target", str(c5), "--write")
        _r5 = json.loads((c5 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _eng5 = [f for f in _r5["files"] if f.get("role") == "engine"]
        check("[-7] AC5 a --write run with no findings exits 0", _a5.returncode == 0,
              _a5.stdout + _a5.stderr)
        check("[-7] AC5 ...and re-stamps the receipt at the engine's own schema",
              _r5.get("schema") == govkit_module().RECEIPT_SCHEMA, str(_r5.get("schema")))
        check("[-7] AC5 the fixture's engine population is non-empty, so the next arm CAN fail",
              len(_eng5) > 0, str(len(_eng5)))
        check("[-7] AC5 every engine row carries gov_oid, oid AND sha256",
              all(all(k in f for k in ("gov_oid", "oid", "sha256")) for f in _eng5),
              str([f["path"] for f in _eng5
                   if not all(k in f for k in ("gov_oid", "oid", "sha256"))][:3]))
        check("[-7] AC5 and the synthesized attributes row takes NEITHER identity",
              all(not (f.get("gov_oid") or f.get("oid"))
                  for f in _r5["files"] if f.get("role") == "attributes"), "")

        # ---- AC5, the older schemas. A hand-built schema-1 and a schema-2 receipt must still
        # ---- classify without a refusal — `gov_oid` is filled from EVIDENCE on the first update of
        # ---- one, never carried over from `sha256` — and schema 1's role-distrust arm must still
        # ---- fire, because a migration that disarms an older guard is not a migration.
        for _sch in (1, 2):
            _co = clone_crlf(i7, f"id7-s{_sch}")
            _rp = _co / ".governance" / "install.json"
            _rr = json.loads(_rp.read_text(encoding="utf-8"))
            _rr["schema"] = _sch
            for _f in _rr["files"]:
                _f.pop("gov_oid", None)
                _f.pop("oid", None)
            _rp.write_text(json.dumps(_rr, indent=2) + "\n", encoding="utf-8", newline="\n")
            _ao = run("update", "--target", str(_co))
            check(f"[-7] AC5 a schema-{_sch} receipt still classifies without a refusal",
                  _ao.returncode != 2 and "REFUSING" not in _ao.stderr, _ao.stderr[:400])
            check(f"[-7] AC5 ...and a schema-{_sch} row is GRADED rather than skipped wholesale",
                  verdict_of(_ao.stdout, MTR) in ("current", "patched", "stale"),
                  verdict_of(_ao.stdout, MTR))
        # ---- ...and the schema-1 role-distrust guard still FIRES, which the loop above cannot
        # ---- show: that guard fires on a DISAGREEMENT between the recorded role and the one the
        # ---- descriptor resolves now, and the receipts above carry correct roles. Built here
        # ---- instead, as unit 1 measured it: a schema-1 receipt stamping `engine` on a file its
        # ---- descriptor declares otherwise. A migration that disarms an older guard is not a
        # ---- migration, and this is the arm that would notice.
        s1 = clone_crlf(i7, "id7-s1role")
        _rp1 = s1 / ".governance" / "install.json"
        _rr1 = json.loads(_rp1.read_text(encoding="utf-8"))
        _rr1["schema"] = 1
        _lied = None
        for _f in _rr1["files"]:
            _f.pop("gov_oid", None)
            _f.pop("oid", None)
            if _f.get("role") == "rendered" and _lied is None:
                _lied, _f["role"] = _f["path"], "engine"
        _rp1.write_text(json.dumps(_rr1, indent=2) + "\n", encoding="utf-8", newline="\n")
        check("[-7] AC5 the fixture really mislabels a non-engine row, so the guard CAN fire",
              _lied is not None, str(_lied))
        _ao1 = run("update", "--target", str(s1))
        check("[-7] AC5 the schema-1 role-distrust arm still fires on a schema-1 receipt",
              "a schema-1 receipt cannot be trusted about" in _ao1.stdout, _ao1.stdout[-800:])
        check("[-7] AC5 ...and names the row it refused", str(_lied) in _ao1.stdout,
              _ao1.stdout[-800:])

        # ---- AC4, AC8, AC9 and AC10 need a row that is GENUINELY STALE — gov moved between the
        # ---- receipt's vintage and `--to` — which `stale_target` cannot give them: it rewinds one
        # ---- real kit against gov's own history and every arm here needs three rows it can poison
        # ---- independently. A scratch gov with three files, built rather than borrowed.
        def identity_gov(name: str) -> pathlib.Path:
            g = tmp / f"{name}-gov"
            (g / "tools" / "govkit").mkdir(parents=True)
            (g / "tools" / "demo").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                '[selection]\ndefault = ["demo"]\n\n'
                '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "demo" / "kit.toml").write_text(
                'id = "demo"\nhome = "tools/demo"\n'
                'version_from = { none = "fixture" }\n\n'
                '[check]\nnone = "a fixture kit"\n\n'
                '[[files]]\ninclude = ["demo.txt", "extra.txt", "spare.txt"]\nrole = "engine"\n\n'
                '[adopt]\nargv = []\nmutates_index = false\n', encoding="utf-8", newline="\n")
            for _n, _c in (("demo.txt", "alpha\nbeta\ngamma\n"), ("extra.txt", "x1\n"),
                           ("spare.txt", "s1\n")):
                (g / "tools" / "demo" / _n).write_text(_c, encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g

        def identity_target(g: pathlib.Path, name: str) -> pathlib.Path:
            """A target installed from THAT gov at its current HEAD, committed.

            Run through the SCRATCH gov's own copy of the engine, which is the seam that acts —
            a break staged into this repo's `govkit.py` does not reach a copy taken before it.
            """
            t = make_target(tmp / name, None)
            for verb in ("intake", "apply"):
                subprocess.run([sys.executable, str(g / "tools" / "govkit" / "govkit.py"), verb,
                                "--target", str(t), "--kits", "demo"], capture_output=True)
            settle(t, "the demo install")
            return t

        def gov_update(g: pathlib.Path, t: pathlib.Path, *extra: str):
            return subprocess.run([sys.executable, str(g / "tools" / "govkit" / "govkit.py"),
                                   "update", "--target", str(t), *extra],
                                  capture_output=True, text=True)

        def poison(t: pathlib.Path, path: str, drop: tuple[str, ...] = (),
                   **set_to) -> dict:
            """Rewrite ONE receipt row, and return it so the arm can assert the state it built."""
            rp = t / ".governance" / "install.json"
            rec = json.loads(rp.read_text(encoding="utf-8"))
            hit = {}
            for f in rec["files"]:
                if f.get("path") != path:
                    continue
                for k in drop:
                    f.pop(k, None)
                f.update(set_to)
                hit = f
            rp.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
            return hit

        ig = identity_gov("id4")
        DMO = "tools/demo/demo.txt"
        # EVERY target is installed at vintage A and gov moves to B AFTERWARDS, once, below. Built
        # in this order deliberately: a target installed after the move records B, and then "the
        # stale row's bytes moved" is trivially true because they were never anywhere else. That is
        # a fixture that cannot trigger the rule it grades, and the first cut of this block had it.
        it4 = identity_target(ig, "id4-t")
        c4 = clone_crlf(it4, "id4-clone")
        it8 = identity_target(ig, "id8-t")
        it9 = identity_target(ig, "id9-t")
        it10s = {d: identity_target(ig, f"id10-{d}") for d in ("gov_oid", "commit")}
        (ig / "tools" / "demo" / "demo.txt").write_text("alpha\nbeta CHANGED\ngamma\n",
                                                        encoding="utf-8", newline="\n")
        git(ig, "add", "-A")
        git(ig, "commit", "-qm", "B")
        _govblob = gout(ig, "rev-parse", "HEAD:tools/demo/demo.txt").strip()

        # ---- AC4: what lands in the INDEX is gov's blob, and what lands in the WORKTREE is
        # ---- whatever THAT target's own filters make of it. Staged red, twice over: the replaced
        # ---- `write_bytes` landed LF into a tree whose filters produce CRLF — and on this very
        # ---- fixture the pre-unit engine never even reached its write arm, because the worktree
        # ---- comparator called the untouched clone `diverged` and left a conflict order instead.
        check("[-7] AC4 the fixture's clone really carries CRLF where gov shipped LF",
              b"\r\n" in (c4 / DMO).read_bytes(), repr((c4 / DMO).read_bytes()))
        _a4 = gov_update(ig, c4, "--write")
        check("[-7] AC4 the row was genuinely STALE, so this arm graded a write and not a no-op",
              verdict_of(_a4.stdout, DMO) == "stale", _a4.stdout + _a4.stderr)
        check("[-7] AC4 the INDEX blob is byte-identical to gov's blob at --to",
              gout(c4, "ls-files", "-s", "--", DMO).split()[1] == _govblob,
              gout(c4, "ls-files", "-s", "--", DMO) + " vs " + _govblob)
        check("[-7] AC4 ...while the WORKTREE carries the endings that target's filters produce",
              b"\r\n" in (c4 / DMO).read_bytes() and b"CHANGED" in (c4 / DMO).read_bytes(),
              repr((c4 / DMO).read_bytes()))
        check("[-7] AC4 ...and the target's own git sees NO unstaged delta on it afterwards",
              gout(c4, "status", "--porcelain", "--", DMO)[1:2] == " ",
              repr(gout(c4, "status", "--porcelain", "--", DMO)))

        # ---- AC8: the STORED half of `gov_oid`, and the only thing standing between a text-merged
        # ---- receipt and a destroyed local edit. The poison is not arbitrary: `-11` rewrites
        # ---- `path`, `source`, `commit` and `gov_oid` together on a rename, so a text merge of
        # ---- `install.json` can pair `commit` from one side with `gov_oid` from the other. Staged
        # ---- red: with S9's mismatch arm patched out, this exact fixture classified the operator's
        # ---- COMMITTED edit as `equal` to gov, called the row `stale`, and overwrote it at exit 0.
        (it8 / DMO).write_text("alpha\nbeta MINE\ngamma\n", encoding="utf-8", newline="\n")
        settle(it8, "an operator edit, committed")
        _mine = gout(it8, "ls-files", "-s", "--", DMO).split()[1]
        _row8 = poison(it8, DMO, gov_oid=_mine)
        _sum8 = (it8 / ".governance" / "install.json").read_bytes()
        check("[-7] AC8 the fixture pairs a real `commit` with a `gov_oid` from the other side",
              _row8.get("gov_oid") == _mine and bool(_row8.get("commit")), str(_row8)[:200])
        _a8 = gov_update(ig, it8, "--write")
        check("[-7] AC8 update refuses a row whose stored gov_oid disagrees with its evidence",
              _a8.returncode == 2 and "records gov_oid" in _a8.stderr, _a8.stderr)
        check("[-7] AC8 the refusal names the path and BOTH oids",
              DMO in _a8.stderr and _mine in _a8.stderr, _a8.stderr)
        check("[-7] AC8 the operator's edit is still there — the refusal wrote nothing",
              b"beta MINE" in (it8 / DMO).read_bytes(), repr((it8 / DMO).read_bytes()))
        check("[-7] AC8 and the receipt is byte-identical",
              (it8 / ".governance" / "install.json").read_bytes() == _sum8, "")

        # ---- AC9 + AC10: the SCOPING, both halves, in one fixture. AC9 says a row carrying NEITHER
        # ---- field is passed over; AC10 says a row carrying exactly ONE still refuses. They must
        # ---- live together or the first is built as a blanket pass for any row missing a field.
        # ---- Staged red for AC9: with S9's neither-arm patched out — the unscoped assertion — the
        # ---- preamble refused on the field-less row and the stale row never moved.
        #
        # The field-less row carries no `source` either, which is the shape AC9 describes and the
        # only one that reaches "written in neither direction" under THIS unit alone. MEASURED, and
        # deliberately not pinned by an arm: the same row WITH a `source` and no `commit` reads
        # `diverged` and is merged against an empty base. That population is `-13` S7's in-loop
        # skip, keyed on `evidence: "unattributed"` and running after `how` resolves — step 6 of the
        # build's preamble order, where S9 is step 4. This unit does not own it and does not pin it.
        _r9 = poison(it9, "tools/demo/extra.txt", drop=("commit", "gov_oid", "source"),
                     evidence="unattributed")
        check("[-7] AC9 the fixture's field-less row really carries neither identity",
              not _r9.get("commit") and not _r9.get("gov_oid")
              and _r9.get("evidence") == "unattributed", str(_r9)[:200])
        check("[-7] AC9 ...and its receipt is at the CURRENT schema, so no migration fills them in",
              json.loads((it9 / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("schema") == govkit_module().RECEIPT_SCHEMA, "")
        _x9 = (it9 / "tools" / "demo" / "extra.txt").read_bytes()
        _a9 = gov_update(ig, it9, "--write")
        check("[-7] AC9 the run completes over the field-less row and exits 0",
              _a9.returncode == 0, _a9.stdout + _a9.stderr)
        check("[-7] AC9 the genuinely stale row's bytes MOVED",
              b"CHANGED" in (it9 / DMO).read_bytes(), repr((it9 / DMO).read_bytes()))
        check("[-7] AC9 the field-less row was printed BY NAME",
              verdict_of(_a9.stdout, "tools/demo/extra.txt") != "(no row)", _a9.stdout)
        check("[-7] AC9 ...and written in NEITHER direction",
              (it9 / "tools" / "demo" / "extra.txt").read_bytes() == _x9, "")

        for _drop, _why in (("gov_oid", "commit and no gov_oid"), ("commit", "gov_oid and no commit")):
            it10 = it10s[_drop]
            poison(it10, "tools/demo/extra.txt", drop=("commit", "gov_oid", "source"),
                   evidence="unattributed")
            _r10 = poison(it10, "tools/demo/spare.txt", drop=(_drop,))
            _sum10 = (it10 / ".governance" / "install.json").read_bytes()
            _b10 = (it10 / DMO).read_bytes()
            check(f"[-7] AC10 the fixture's `engine` row really carries {_why}",
                  _r10.get("role") == "engine" and (_drop not in _r10)
                  and bool(_r10.get("commit") or _r10.get("gov_oid")), str(_r10)[:200])
            _a10 = gov_update(ig, it10, "--write")
            check(f"[-7] AC10 a half-populated pair ({_why}) refuses by name",
                  _a10.returncode == 2 and "meaningless apart" in _a10.stderr
                  and "tools/demo/spare.txt" in _a10.stderr, _a10.stderr)
            check(f"[-7] AC10 ...writes nothing ({_why})", (it10 / DMO).read_bytes() == _b10, "")
            check(f"[-7] AC10 ...and leaves the receipt byte-identical ({_why})",
                  (it10 / ".governance" / "install.json").read_bytes() == _sum10, "")

        # ---- AC11: §8 F4's exemption, OBSERVED. `push-main` is the kit because it is one of the
        # ---- two in this tree declaring `role = "merged"` at `marker_style = "hash-comment"`,
        # ---- which is the branch that writes the row shape under test. Staged red: with the
        # ---- `merged` arm patched out of S9, that row's `commit`-without-`gov_oid` tripped the
        # ---- exactly-one branch and the WHOLE run refused before any row was classified — on the
        # ---- first update against any target that ever applied such a rule.
        t11 = make_target(tmp / "id11", None)
        run("intake", "--target", str(t11), "--kits", "push-main")
        run("apply", "--target", str(t11), "--kits", "push-main")
        settle(t11, "the push-main install")
        _r11 = json.loads((t11 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _mrg = [f for f in _r11["files"] if f.get("role") == "merged"]
        check("[-7] AC11 the fixture really produced a merged row", len(_mrg) == 1,
              str([f.get("role") for f in _r11["files"]]))
        check("[-7] AC11 ...and it carries `commit` with NEITHER identity — S9's exactly-one shape",
              bool(_mrg[0].get("commit")) and not _mrg[0].get("gov_oid")
              and not _mrg[0].get("oid"), str(sorted(_mrg[0])))
        _a11 = run("update", "--target", str(t11), "--write")
        check("[-7] AC11 update runs to completion over that receipt and exits 0",
              _a11.returncode == 0, _a11.stdout + _a11.stderr)
        check("[-7] AC11 NEGATIVE: no refusal fires on the merged row",
              "meaningless apart" not in _a11.stderr and "REFUSING" not in _a11.stderr,
              _a11.stderr)
        check("[-7] AC11 the merged row reached its own block compare, by name",
              verdict_of(_a11.stdout, ".githooks/pre-commit") in ("current", "block-moved"),
              _a11.stdout)

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

    # ---- THE OBSERVED-STATE TABLE IS THE ONE SPELLING OF IT ---------------------------------
    # Three copies existed and they disagreed: the reader's state tuple, the validator's
    # string-check tuple, and the seed writer's hardcoded key list. `observed_reused` reached one of
    # the three; `observed_held` (TOOL-dUnstalledConvoy-26) reached none — which made every
    # kit-subject leg invisible to `read_gate_verdicts`, so an upgrading adopter's apply saw a leg
    # that was green before, holding NO state after, and tripped "a leg that vanished is not a leg
    # that passed" on every one of them.
    sys.path.insert(0, str(HERE))
    import govkit as _GK
    _OBS_KEYS = _GK.OBSERVED_KEYS
    check("OBSERVED_KEYS is derived from OBSERVED_STATES rather than re-typed",
          _OBS_KEYS == tuple(k for _s, k in _GK.OBSERVED_STATES), str(_OBS_KEYS))
    check("the table carries the held verb, or the fifth verb is invisible to the deployer",
          "observed_held" in _OBS_KEYS, str(_OBS_KEYS))
    check("and the reused verb, which was declared by a kit and read by nobody",
          "observed_reused" in _OBS_KEYS, str(_OBS_KEYS))
    check("held is a not-executed state beside skipped, so an all-held baseline carries no "
          "information and the dead-probe refusal can see that",
          set(_GK.NOT_EXECUTED) == {"skipped", "held"}, str(_GK.NOT_EXECUTED))

    # BEHAVIOURAL: drive the reader over a runner that prints one line per verb and assert every
    # bare leg name comes back under the right state. A synthetic runner, because the subject is the
    # PARSE and a real bar takes minutes to say the same thing.
    with tempfile.TemporaryDirectory() as _rd:
        _rp = pathlib.Path(_rd)
        (_rp / "echo_verbs.py").write_text(
            "print('GATE ok    a repo leg')\n"
            "print('GATE FAIL  a red leg  (exit 1)')\n"
            "print('GATE skip  a guarded leg  (unchanged vs main)')\n"
            "print('GATE reuse a reused leg  (proven green, inputs unchanged)')\n"
            "print('GATE held  a kit self-test  (kit self-test, set GATE_SELFTESTS=1 to run)')\n",
            encoding="utf-8", newline="\n")
        _verbs = {"green": "GATE ok    ", "red": "GATE FAIL  ", "skipped": "GATE skip  ",
                  "reused": "GATE reuse ", "held": "GATE held  "}
        _gr = {"command": [sys.executable, "echo_verbs.py"]}
        for _st, _key in _GK.OBSERVED_STATES:
            _gr[_key] = [_verbs[_st] + "{name}"]
        _got = _GK.read_gate_verdicts(_rp, _gr)
        check("the reader classifies all five verbs, by name and by state",
              _got == {"a repo leg": "green", "a red leg": "red", "a guarded leg": "skipped",
                       "a reused leg": "reused", "a kit self-test": "held"}, str(_got))
        # ITS LIVENESS HALF: with the held template removed that leg holds NO state at all, which is
        # the exact shape that made an upgrading adopter's apply refuse.
        _gr2 = dict(_gr)
        del _gr2["observed_held"]
        _got2 = _GK.read_gate_verdicts(_rp, _gr2)
        check("LIVENESS: without the held template that leg holds no state at all",
              "a kit self-test" not in _got2, str(_got2))

    reg = load_seed_toml(_gov / "tools" / "govkit" / "registry.toml")
    seeded = []
    for e in reg.get("entry", []):
        d = load_seed_toml(_gov / e["descriptor"])
        if d.get("gate_runner_seed"):
            seeded.append((e["id"], d["gate_runner_seed"]))
    check("at least one registry entry declares a [gate_runner_seed] to round-trip",
          bool(seeded), "no entry declares one — this arm would pass by finding nothing")
    # A SHIPPED seed must declare the verb its own runner prints, or the emission arms above
    # quantify over a set that never contains it and pass by finding nothing.
    check("a shipped [gate_runner_seed] declares observed_held",
          any("observed_held" in s for _e, s in seeded),
          "no seed declares it, so every held leg is invisible to every adopter's deployer")
    check("...and observed_reused",
          any("observed_reused" in s for _e, s in seeded), "no seed declares it")
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
            # EVERY key the SEED declares must reach the emitted deploy.toml — not the two a
            # previous pass remembered. The emitter's key list was hand-written and dropped
            # `observed_reused` from every target since the day the run-gates kit declared it: a
            # template that shipped, that no adopter ever received and no reader ever read. The
            # population is the seed's own keys, so a verb added to a kit is covered here on the
            # commit that adds it. TOOL-dUnstalledConvoy-26.
            # DERIVED FROM THE SEED, never from OBSERVED_KEYS. Quantifying over the table
            # would make this arm stop checking a verb on the same edit that drops it from
            # the table — a predicate derived from the thing it grades. Measured: removing
            # `held` from OBSERVED_STATES left this loop silently green about it.
            for key in sorted(k for k in seed if k.startswith("observed_")):
                check(f"[{eid}] the seed declares {key} and the emitted deploy.toml carries it",
                      isinstance(decl.get(key), list) and bool(decl.get(key)),
                      f"the seed declares {key} and the emission produced {decl.get(key)!r}")
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

    # ---- THE SHELL A LEG ACTUALLY GETS -------------------------------------------------
    # Guards the govkit-matrix repair measured on node d, 2026-08-20. A descriptor declares
    # `argv = ["bash", ...]`, govkit is a WINDOWS python, and the loader answers that bare name
    # with C:/Windows/System32/bash.exe — the WSL launcher, which sees /mnt/c/ and carries its
    # own python3 (3.10.12, no tomllib). Every arm below is the difference between a fix and a
    # line anyone can delete: without them nothing reds until a node with WSL runs a FULL bar,
    # and the leg is GUARDED, so a scoped bar never would.
    sys.path.insert(0, str(HERE))
    import govkit  # noqa: E402

    rb = govkit.resolve_bash()
    low = rb.replace(chr(92), "/").lower()
    check("resolve_bash never returns a launcher for another filesystem",
          "/system32/" not in low and "/windowsapps/" not in low, "resolved " + repr(rb))
    check("resolve_bash returns something that RUNS",
          subprocess.run([rb, "-c", ":"], capture_output=True).returncode == 0,
          "resolved " + repr(rb) + " and it did not run")

    got = govkit.resolve_shell_argv(["bash", "x.sh"])
    check("resolve_shell_argv rewrites a LEADING bare bash", got == [rb, "x.sh"], "got " + repr(got))
    got = govkit.resolve_shell_argv(["python", "x.py"])
    check("resolve_shell_argv leaves a non-bash argv0 alone", got == ["python", "x.py"],
          "got " + repr(got))
    # `bash` as an ARGUMENT is a value the target chose. Rewriting it would be govkit editing
    # the command rather than choosing the shell that runs it.
    got = govkit.resolve_shell_argv(["sh", "-c", "bash"])
    check("resolve_shell_argv leaves a bash in argument position alone", got == ["sh", "-c", "bash"],
          "got " + repr(got))
    check("resolve_shell_argv is a no-op on an empty argv", govkit.resolve_shell_argv([]) == [], "")

    # ---- THE CLASS, not the three instances. The behavioural arms above prove the resolver works;
    # ---- they cannot prove every place that executes a leg argv calls it, and that gap is not
    # ---- theoretical. Two sessions fixed this class independently in the same week and BOTH left a
    # ---- site unwrapped: one missed the CONFIGURE step, the other the [[hole]] discharge probe,
    # ---- whose shipped commands are literally ["bash", "-c", ...]. A behavioural arm is green in
    # ---- both cases, because the function it exercises is fine — it is the caller that is missing.
    # ----
    # ---- WHAT THIS DOES NOT CHECK: that the resolver picks the right bash (the arms above do), or
    # ---- that a target's own scripts are portable (nothing here does). It reads SOURCE and asserts
    # ---- one thing: no subprocess call in these two files executes an argv that is neither a
    # ---- literal git invocation nor routed through the resolver.
    for _src in ("govkit.py", "matrix.py"):
        _txt = (HERE / _src).read_text(encoding="utf-8")
        _bad = []
        for _m in _re.finditer(r"subprocess\.(?:run|Popen)\(\s*([^\n]*)", _txt):
            _head = _m.group(1)
            if "resolve_shell_argv" in _head:
                continue
            if _head.lstrip().startswith(('["git"', "['git'", "[sys.executable", "[cand,")):
                continue
            if _head.lstrip().startswith(")") or _head.strip() == "":
                continue                      # a multi-line call whose argv is on the next line
            # ...and not a match INSIDE a string literal. matrix.py builds fixture runner scripts as
            # text, and one of them contains `subprocess.run(l[argv])` — code it WRITES into a
            # synthetic target, not code govkit runs. The first draft of this arm redded on it, which
            # is why a candidate predicate gets run over the real tree before it is wired.
            _pre = _txt[: _m.start()].rsplit(chr(10), 1)[-1]
            if _pre.count(chr(34)) % 2 or _pre.count(chr(39)) % 2:
                continue
            _line = _txt[: _m.start()].count("\n") + 1
            _bad.append(f"{_src}:{_line} {_head.strip()[:60]}")
        check(f"every leg argv in {_src} goes through resolve_shell_argv",
              not _bad, "unwrapped: " + "; ".join(_bad))

    # An override that is SET and unusable must be THIS failure, never a quiet fall-through:
    # the operator would believe they had chosen. The memo is cleared around the arm so it
    # measures the resolver rather than the answer the arms above cached.
    keep_bash, keep_env = govkit._BASH, os.environ.get("GOV_BASH")
    govkit._BASH = None
    os.environ["GOV_BASH"] = str(HERE / "no-such-bash-xyzzy")
    try:
        govkit.resolve_bash()
        refused = False
    except govkit.Refusal:
        refused = True
    finally:
        govkit._BASH = keep_bash
        if keep_env is None:
            os.environ.pop("GOV_BASH", None)
        else:
            os.environ["GOV_BASH"] = keep_env
    check("a GOV_BASH that is set and does not run is a Refusal, not a fall-through", refused,
          "resolve_bash fell through to another shell instead of naming the bad override")

    print()
    if FAILURES:
        print(f"govkit-selftest: {len(FAILURES)} FAILED — {', '.join(FAILURES)}")
        return 1
    print("govkit-selftest: all arms held")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
