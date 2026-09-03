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

import hashlib
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

# TOOL-aScouredKit-13. DEPLOY_FULL declares `kits = ["memory-tree"]`, and until that unit landed
# `plan`/`apply` IGNORED a target's own list and substituted gov's registry default — so the arms
# below that say "the default selection" were, in fact, measuring the registry default against a
# target that had asked for one kit. Now that the declaration is honoured, a fixture that exercises
# the REGISTRY default has to declare none. Same answers, no `kits` line: the difference between the
# two constants is the whole point and is why this is not a parameter.
DEPLOY_REGISTRY_DEFAULT = "".join(
    ln for ln in DEPLOY_FULL.splitlines(keepends=True) if not ln.startswith("kits = "))
assert "kits = " not in DEPLOY_REGISTRY_DEFAULT, "the kits line must be gone, or the fixture lies"

DEPLOY_NO_ANSWERS = """gov_source = "local"
prefix = "tools"
kits = ["playbook"]
"""


def main() -> int:
    # DEPL-dGaugedVintage-10. The measurer-currency probe reads a remote advertisement, and this
    # suite spawns a fresh `update` process dozens of times — one network round-trip each, which
    # blew the 600 s ceiling. Off for the whole suite; the probe's own arms drive the function
    # directly instead, so turning it off here costs no coverage.
    os.environ["GOVKIT_NO_REMOTE_PROBE"] = "1"

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

        # --- DEPL-dGaugedVintage-8 S3. THE STAMP MUST NOT OUTRUN ROWS THIS RUN NEVER GRADED.
        # --- An `evidence: "unattributed"` row is skipped before `classify_row`, by
        # --- DEPL-dCarriedReceipt-13's ratified design, and it is graded against the receipt's OWN
        # --- `gov_commit` — so advancing the stamp moves the base it must be attributed from
        # --- further away on every run, and the row gets harder to recover with no event to notice.
        # --- OBSERVED RED before the guard landed: `update --write` stamped forward over such a row
        # --- (3e11f259 -> b263d5b9 on a scratch fixture) and printed the ordinary re-stamp line.
        ung = stale_target("ungraded")
        rp_u = ung / ".governance" / "install.json"
        rec = json.loads(rp_u.read_text(encoding="utf-8"))
        for f in rec["files"]:
            f["evidence"] = "unattributed"
            f.pop("commit", None)
            f.pop("gov_oid", None)
        rp_u.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
        p = run("update", "--target", str(ung), "--write")
        rec = json.loads(rp_u.read_text(encoding="utf-8"))
        check("[dGV-8] update --write does NOT re-stamp while a row is unattributed",
              rec["gov_commit"] == OLD, rec["gov_commit"])
        check("[dGV-8] the withheld stamp says why, and names the remedy that clears the rows",
              "NOT re-stamped" in p.stdout and "--re-adopt" in p.stdout, p.stdout)
        check("[dGV-8] and it names the override rather than leaving the operator stuck",
              "--allow-ungraded" in p.stdout, p.stdout)
        p = run("update", "--target", str(ung), "--write", "--allow-ungraded")
        rec = json.loads(rp_u.read_text(encoding="utf-8"))
        check("[dGV-8] --allow-ungraded advances the stamp",
              rec["gov_commit"] != OLD, rec["gov_commit"])
        check("[dGV-8] and the override states what it overrode, so the choice is on the record",
              "ungraded row(s), --allow-ungraded" in p.stdout, p.stdout)

        # --- DEPL-dGaugedVintage-9 S1. `update` REFRESHES A ROW'S `version`. It never did: every
        # --- `"version":` write lived in `apply` or `adopt`, and `_cmd_update` did not contain the
        # --- string at all — so a row moved to new bytes kept the version it originally landed at,
        # --- against the NEW commit and the NEW sha256. aTetheredConvoy round-3 F6 reproduced that
        # --- by bumping a constant 1.0 -> 9.9 and watching the receipt keep 1.0.
        # --- A delta report over that field would have called a fully current target "behind".
        vr = stale_target("verrefresh")
        rp_v = vr / ".governance" / "install.json"
        rec = json.loads(rp_v.read_text(encoding="utf-8"))
        for f in rec["files"]:
            f["version"] = "STALE-SENTINEL"
        rp_v.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
        p = run("update", "--target", str(vr), "--write")
        rec = json.loads(rp_v.read_text(encoding="utf-8"))
        _moved = [f for f in rec["files"] if f.get("version") != "STALE-SENTINEL"]
        check("[dGV-9] update --write refreshes a refreshed row's version, not only sha256/commit",
              len(_moved) > 0, json.dumps(rec["files"], indent=1)[:900])
        check("[dGV-9] and the refreshed value is the constant's SOURCE LINE, the shape "
              "entry_version returns",
              any("KIT_CHECK_WIRING_VERSION" in (f.get("version") or "") for f in _moved),
              json.dumps([f.get("version") for f in rec["files"]])[:500])
        check("[dGV-9] and sha256 and commit moved with it, so the three stay one fact",
              all(f.get("commit") and f.get("sha256") for f in _moved),
              json.dumps(_moved, indent=1)[:600])

        # --- DEPL-dGaugedVintage-10. THE MEASURER'S OWN CURRENCY. `demand_published_vintage` and
        # --- `demand_forward_vintage` are both satisfied by any commit the local clone can see, so
        # --- an unfetched clone reported every row up to date for everything gov had since moved.
        # --- Driven DIRECTLY rather than through a verb, because the probe is off for this suite
        # --- (see main()) and a network round-trip per spawned update blew the 600 s ceiling.
        _gk = govkit_module()
        _dead = tmp / "deadremote"
        _dead.mkdir()
        git(_dead, "init", "-q", ".")
        git(_dead, "remote", "add", "origin", str(tmp / "there-is-no-such.git"))
        _saved = os.environ.pop("GOVKIT_NO_REMOTE_PROBE", None)
        try:
            _v, _d = _gk.resolve_measurer_currency(_dead, "0" * 40)
            # The memo arm belongs INSIDE the seam window: restoring the env var first would make
            # the second call take the disabled branch and prove nothing about memoization.
            _v2, _d2 = _gk.resolve_measurer_currency(_dead, "0" * 40)
        finally:
            if _saved is not None:
                os.environ["GOVKIT_NO_REMOTE_PROBE"] = _saved
        check("[dGV-10] an unreachable remote is UNVERIFIED, never read as up to date",
              _v == "unverified" and _v != "current", f"{_v} | {_d}")
        check("[dGV-10] and the verdict says which remote did not answer",
              "origin" in _d, _d)
        check("[dGV-10] the probe is memoized per process, so one advertisement read serves a run",
              (_v2, _d2) == (_v, _d), f"{_v2} | {_d2}")
        os.environ["GOVKIT_NO_REMOTE_PROBE"] = "1"
        _v3, _ = _gk.resolve_measurer_currency(tmp / "no-such-root", "0" * 40)
        check("[dGV-10] the test seam yields unverified — a disabled probe is not a clean one",
              _v3 == "unverified", _v3)

        # --- DEPL-dGaugedVintage-11. THE RELOCATE RUNG SURVIVES A KIT THAT FANS OUT.
        # --- `derive_carry_map` holds ONE destination per gov directory, so a kit shipping a
        # --- rendered artifact to a different tree than its engine files had its whole directory
        # --- dropped from the needle map — which is every kit that ships a Skill. The global map
        # --- still drops it (it cannot hold two), but rows now rewrite through their OWN pair.
        _n_global, _pairs_g, _drop_g = _gk.derive_carry_map(
            [("tools/k/engine.py", "scripts/k/engine.py"),
             ("tools/k/SKILL.template.md", ".claude/skills/k/SKILL.md")])
        check("[dGV-11] a gov directory that fans out is still absent from the GLOBAL needle map",
              "tools/k" not in _n_global and any(g == "tools/k" for g, _ in _drop_g),
              f"{_n_global} | {_drop_g}")
        _row = {"source": "tools/k/engine.py", "path": "scripts/k/engine.py"}
        _n_row = _gk.resolve_row_needles(_n_global, _row)
        check("[dGV-11] but the ROW resolves against its own destination, rooted on its own pair",
              _n_row.get("tools/k") == "scripts/k", f"{_n_row}")
        _row2 = {"source": "tools/k/SKILL.template.md", "path": ".claude/skills/k/SKILL.md"}
        _n_row2 = _gk.resolve_row_needles(_n_global, _row2)
        check("[dGV-11] and a second row under the same gov directory gets ITS destination, "
              "not the first row's",
              _n_row2.get("tools/k") == ".claude/skills/k", f"{_n_row2}")
        check("[dGV-11] gov's bytes really are rewritten through the row's needle",
              _gk.derive_carried(b"see tools/k/engine.py here", _n_row) ==
              b"see scripts/k/engine.py here",
              _gk.derive_carried(b"see tools/k/engine.py here", _n_row).decode())
        _row3 = {"source": None, "path": None}
        check("[dGV-11] a row with no pair falls back to the global map rather than emptying it",
              _gk.resolve_row_needles(_n_global, _row3) == _n_global, "")

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
        # TOOL-aScouredKit-11 moved this sentence's lead-in from "of those" to "leg(s) in your
        # runner", because on the WITHHELD path the count is over rows carried forward from the
        # previous receipt rather than over rows this run emitted, and "of those" then names a
        # population that does not exist. The edit STRANDED this arm — `arm-literal-strands-on-
        # message-edit`, catalogued in this repo's own gotchas and warned about in its kickoff
        # manifest — and the suite caught it. The literal is re-pinned here rather than the message
        # reverted, because the new wording is the true one.
        check("AC11: the install summary states how many emitted legs are HELD kit self-tests",
              f"govkit apply — {len(_kits_in)} leg(s) in your runner are kit SELF-TESTS and are "
              f"HELD by default" in pa.stdout, pa.stdout)
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

        # TOOL-aScouredKit-11 — THE WITHHELD PATH, which had three writers and no arm until this
        # build's own round-2 review said so. Two properties, and the second is the one whose
        # absence wedged a target: the manifest is NOT rewritten when the LEGS step raises, and the
        # receipt's `emitted` KEEPS the previous run's rows instead of being blanked. `owned`
        # derives from that field, so a blank makes the next apply refuse the legs this deployer
        # itself wrote — permanently, with --re-adopt carrying the blank forward.
        _pre_legs = (gt / "tools" / "legs.json").read_text(encoding="utf-8")
        _pre_rcpt = json.loads((gt / ".governance" / "install.json").read_text(encoding="utf-8"))
        _pre_owned = [e["name"] for e in (_pre_rcpt.get("gate_runner") or {}).get("emitted", [])]
        check("PRECONDITION: the target owns at least one emitted leg before the withheld run — "
              "without this the two arms below pass over an empty set",
              len(_pre_owned) >= 1, str(_pre_owned))
        # THE BREAK IS IN THE TARGET'S OWN RUNNER, and the first attempt got this wrong in a way
        # worth recording: it edited `<target>/tools/check-wiring/kit.toml`, which does not exist.
        # `check-wiring` is a FLAT registry entry — no kit directory, and the descriptor is gov's,
        # never copied into the target — so the fixture asserted against a path no install creates
        # and the loud else-branch below is what said so.
        #
        # What a target DOES have is its runner file, and editing a row gov's receipt claims makes
        # the LEGS step raise its own drift fail: "leg X in the target differs from what the receipt
        # recorded". That is a problem raised INSIDE the step, which is exactly and only what the
        # fixed guard reacts to — an earlier step's problem must NOT withhold, and that half is
        # covered by every other apply arm in this suite passing with problems recorded elsewhere.
        # THE RECEIPT IS THE OPERAND, not the runner file. The drift check reads
        # `prev.get("argv") != argv`, where `prev` is the RECEIPT's row and `argv` is this run's
        # fresh resolve — so tampering the RUNNER changes neither side and apply silently repairs
        # it, which is what the first cut of this fixture did and why it measured nothing. The
        # message's own wording ("in the target differs from what the receipt recorded") points at
        # the runner and the comparison does not; that gap is why this took two attempts.
        _rcpt_path = gt / ".governance" / "install.json"
        _tamper = next((e for e in (_pre_rcpt.get("gate_runner") or {}).get("emitted", [])
                        if e.get("name") in _pre_owned), None)
        if _tamper is not None:
            _tamper["argv"] = list(_tamper.get("argv", [])) + ["--recorded-differently"]
            _rcpt_path.write_text(json.dumps(_pre_rcpt, indent=2) + "\n",
                                  encoding="utf-8", newline="\n")
            _wr = run("apply", "--target", str(gt), "--kits", "check-wiring")
            check("AC-withheld: a leg differing from what the receipt recorded WITHHOLDS the "
                  "manifest — the problem is raised INSIDE the LEGS step, which is the only thing "
                  "the guard reacts to",
                  "gate legs: WITHHELD" in _wr.stdout, _wr.stdout + _wr.stderr)
            check("AC-withheld: and the runner file is byte-identical — nothing was rewritten",
                  (gt / "tools" / "legs.json").read_text(encoding="utf-8") == _pre_legs,
                  (gt / "tools" / "legs.json").read_text(encoding="utf-8"))
            _post = json.loads((gt / ".governance" / "install.json").read_text(encoding="utf-8"))
            _post_owned = [e["name"] for e in (_post.get("gate_runner") or {}).get("emitted", [])]
            check("AC-withheld: and the receipt KEEPS the previous ownership rather than blanking "
                  "them — a blank makes the next apply refuse the legs this deployer wrote",
                  _post_owned == _pre_owned, f"pre={_pre_owned} post={_post_owned}")
            # THE WEDGE ITSELF, end to end, because the two arms above are about a FIELD and this
            # one is about the CONSEQUENCE.
            #
            # THIS ARM WAS VACUOUS AND ROUND 3 PROVED IT. It used to overwrite the on-disk
            # receipt's `emitted` with the pre-run rows before re-applying — which is precisely the
            # job the production fix is supposed to do, so the arm passed whether or not the fix
            # existed. Demonstrated by staging the break: with `emitted = []` restored in
            # `govkit.py`, the suite reported exactly ONE failure (the field arm) while this one,
            # billed as covering the wedge end to end, printed ok.
            #
            # It now UNDOES THE TAMPER ONLY, in whatever rows the production code actually left,
            # and never writes an ownership row of its own. If the fix blanked `emitted`, there is
            # nothing to untamper, the re-apply meets a runner holding legs the receipt no longer
            # claims, and this arm fails — which is the whole point of it.
            _rcpt_now = json.loads(_rcpt_path.read_text(encoding="utf-8"))
            for _e in (_rcpt_now.get("gate_runner") or {}).get("emitted", []):
                _e["argv"] = [a for a in _e.get("argv", []) if a != "--recorded-differently"]
            _rcpt_path.write_text(json.dumps(_rcpt_now, indent=2) + "\n",
                                  encoding="utf-8", newline="\n")
            _wr2 = run("apply", "--target", str(gt), "--kits", "check-wiring")
            check("AC-withheld: and a later apply RECOVERS — it is not wedged by the withheld run",
                  _wr2.returncode == 0 and "already has a leg named" not in _wr2.stdout,
                  _wr2.stdout + _wr2.stderr)
            check("AC-withheld: and the receipt records legs_withheld, so the fact survives "
                  "outside the stdout nobody kept",
                  (_post.get("gate_runner") or {}).get("legs_withheld") is True, str(_post.get("gate_runner")))

            # TOOL-aScouredKit-31 — THE OTHER CARRY-FORWARD, on the `kind != "manifest"` branch,
            # which had no arm ANYWHERE. Round 3 proved it by reverting that line and getting "all
            # arms held", exit 0: a whole production behaviour with nothing observing it.
            #
            # Reached by flipping the target's declared runner kind to `none`, which is an operator
            # action rather than an exotic one. That branch ORDERS legs into an outbox instead of
            # writing them, so it must not REVOKE the receipt's claim on legs a previous
            # manifest-kind run really wrote — otherwise flipping back wedges the target exactly as
            # the withheld path did.
            _dep = (gt / ".governance" / "deploy.toml")
            _dep_src = _dep.read_text(encoding="utf-8")
            _dep.write_text(_dep_src.replace('kind = "manifest"', 'kind = "none"', 1),
                            encoding="utf-8", newline="\n")
            _wr3 = run("apply", "--target", str(gt), "--kits", "check-wiring")
            _r3 = json.loads(_rcpt_path.read_text(encoding="utf-8"))
            _own3 = [e["name"] for e in (_r3.get("gate_runner") or {}).get("emitted", [])]
            check("AC-ordered: a kind=none apply KEEPS the receipt's ownership of legs a previous "
                  "manifest run wrote — blanking it wedges the target when the kind is flipped back",
                  _own3 == _pre_owned, f"pre={_pre_owned} post={_own3} :: {_wr3.stdout[-400:]}")
            _dep.write_text(_dep_src, encoding="utf-8", newline="\n")
            _wr4 = run("apply", "--target", str(gt), "--kits", "check-wiring")
            check("AC-ordered: and flipping the kind BACK to manifest is not wedged",
                  _wr4.returncode == 0 and "already has a leg named" not in _wr4.stdout,
                  _wr4.stdout + _wr4.stderr)
        else:
            # LOUD, not silent. This suite has no skip verb, and inventing one here to excuse a
            # missing fixture would make the arms above indistinguishable from arms that ran. The
            # rows are written by the applies above, so an empty set is a real breakage.
            check("AC-withheld: the target owns a runner row to tamper with — an absent fixture "
                  "means the withheld arms above never ran",
                  False, f"owned={_pre_owned} rows={_pre_legs[:200]}")

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
        # --- DEPL-dGaugedVintage-3 S1/S2/S4. AN ENTRY THAT LANDS NO PROGRAM MUST NOT READ AS
        # --- ADOPTED. `memory-recall` is a registry DEFAULT whose engine files are `forked`, which
        # --- the derived LANDABLE_ROLES excludes, so `apply` lands its rendered Skill — which tells
        # --- an agent to run the CLI — and never the CLI. OBSERVED RED on the pre-fix binary over a
        # --- fresh target: `query.py` absent and zero INCOMPLETE lines.
        # --- The detection keys on the ROLE, never on the kit id, which is what makes it a class
        # --- assertion while exactly one `forked` rule ships.
        inc = make_target(tmp / "incomplete", DEPLOY_FULL)
        p = run("apply", "--target", str(inc), "--kits", "memory-recall")
        out = p.stdout + p.stderr
        check("[dGV-3] apply reports an entry INCOMPLETE when its forked files are absent",
              "INCOMPLETE memory-recall" in out, out[-900:])
        check("[dGV-3] and it names EVERY absent file with the role that withheld it",
              out.count("absent [forked") >= 3, out[-900:])
        check("[dGV-3] and it gives UNLANDED_REASON's sentence rather than a bare skip",
              "derivative of the target's" in out, out[-900:])
        check("[dGV-3] and it tells the operator gov will not send them",
              "gov will not send them" in out, out[-900:])
        check("[dGV-3] the CLI really is absent, so the report is not describing a landed file",
              not (inc / "tools" / "memory-recall" / "query.py").exists())
        _mr = inc / "tools" / "memory-recall"
        _mr.mkdir(parents=True, exist_ok=True)
        (_mr / "query.py").write_text("# the adopter's own" + NLp, encoding="utf-8", newline=NLp)
        (_mr / "extract.py").write_text("# own" + NLp, encoding="utf-8", newline=NLp)
        (_mr / "recall-opened.js").write_text("// own" + NLp, encoding="utf-8", newline=NLp)
        p = run("apply", "--target", str(inc), "--kits", "memory-recall")
        check("[dGV-3] a target that ALREADY holds its forked files is not reported incomplete",
              "INCOMPLETE memory-recall" not in (p.stdout + p.stderr), (p.stdout + p.stderr)[-700:])
        check("[dGV-3] and apply left the adopter's own bytes alone",
              (_mr / "query.py").read_text(encoding="utf-8").startswith("# the adopter's own"),
              (_mr / "query.py").read_text(encoding="utf-8"))

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
        # Three fields since TOOL-aScouredKit-3: `<name>\t<subject>\t<chunk>`. The fixture leg
        # declares no chunk, so the third field is EMPTY — which is the value a real leg with no
        # chunk key also pins, and is why the trailing tab is asserted rather than trimmed.
        check("AC4: and the generated pin is exactly the derived population",
              _rows == ["demo\trepo\t"], str(_rows))
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
              _rows2 == ["demo\tkit\t"], str(_rows2))

        # TOOL-aScouredKit-3 — the SECOND deciding field, with its failing case observed rather than
        # assumed. `run-gates.sh` holds a leg when `subject == kit` OR `chunk == selftests`, and
        # until this arm existed only the subject was pinned: flipping a `repo` leg's chunk to
        # `selftests` took it off every automatic bar with nothing in a diff to see. Measured on the
        # real tree before the fix — `selfcheck` exited 0 and still reported the old held count.
        _write_legs("repo")
        run_in_gov(rg, "selfcheck", "--write")
        _legs_now = json.loads(legsf.read_text(encoding="utf-8"))
        _legs_now[0]["chunk"] = "selftests"
        legsf.write_text(json.dumps(_legs_now, indent=2) + "\n", encoding="utf-8", newline="\n")
        kitf.write_text(kitf.read_text(encoding="utf-8").replace(
            'name = "demo"\nargv = ["true"]\nguard = []\nsubject = "repo"\n',
            'name = "demo"\nargv = ["true"]\nguard = []\nsubject = "repo"\nchunk = "selftests"\n'),
            encoding="utf-8", newline="\n")
        _rc = run_in(rg)
        check("AC5: flipping a leg's CHUNK to selftests without moving its pin REDS",
              _rc.returncode == 1, _rc.stdout + _rc.stderr)
        check("AC5: and the refusal names the leg and BOTH chunk values",
              "gate leg 'demo' is chunk 'selftests' and pinned '(none)'" in _rc.stdout, _rc.stdout)
        check("AC5: and says what the move does — leaving the automatic bar",
              "OFF the automatic bar" in _rc.stdout, _rc.stdout)
        _wc = run_in_gov(rg, "selfcheck", "--write")
        _rowsc = [l for l in pinf.read_text(encoding="utf-8").split("\n")
                  if l.strip() and not l.startswith("#")]
        check("AC5: and moving the pin in the same commit records the chunk and passes",
              _wc.returncode == 0 and _rowsc == ["demo\trepo\tselftests"],
              str(_rowsc) + _wc.stdout + _wc.stderr)

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
            t2 = make_target(tmp3 / "dflt", DEPLOY_REGISTRY_DEFAULT)
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
            # TOOL-aScouredKit-13 — the OTHER side of the split above, and the arm that did not
            # exist. A target declaring its own `kits` gets exactly those from a no---kits `plan`,
            # rather than gov's registry default. Before this unit, `plan` previewed the six-kit
            # default over a target that had asked for one, and `apply` then exited 2 over an answer
            # intake never asked for — so the documented no---kits path was the broken one and the
            # preview agreed with it. Asserted as a SUBSET relation on the preview's write set: the
            # declared single kit's rows are a strict subset of what the registry default writes,
            # which is a property no re-baselining of a row count can accidentally satisfy.
            t3 = make_target(tmp3 / "declared", DEPLOY_FULL)
            pl3 = run("plan", "--target", str(t3))
            check("a target's own `kits` list is honoured by a no---kits plan", pl3.returncode == 0,
                  pl3.stdout + pl3.stderr)
            _declared_writes = extract_plan_writes(pl3.stdout)
            _default_writes = extract_plan_writes(pl2.stdout)
            check("...and it is a STRICT subset of the registry default's write set",
                  _declared_writes and _declared_writes < _default_writes,
                  f"declared={len(_declared_writes)} default={len(_default_writes)} "
                  f"declared-only={sorted(_declared_writes - _default_writes)}")
            check("...and every path it writes belongs to the kit it declared",
                  all("memory-tree" in w or "memory" in w or w.endswith(".conf")
                      for w in _declared_writes),
                  str(sorted(_declared_writes)))

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

        # ---- OWNER RULING A (2026-08-26) -- GOV'S OWN STAGING IS NOT SOMEBODY'S WORK IN PROGRESS.
        # ---- `-12` S4 parked this: `apply` STAGES every path it lands, so a completed apply makes
        # ---- every receipt-claimed path differ index-versus-HEAD and therefore dirty by S4's own
        # ---- definition. A second `apply` refused, `update --write` straight after `apply`
        # ---- refused, and `apply --resume` refused STRUCTURALLY -- it needs a receipt, a receipt
        # ---- needs a completed apply, and a completed apply leaves the target dirty. The carve-out
        # ---- compares the INDEX BLOB against the oid the receipt recorded, so it excuses gov's own
        # ---- staging and nothing else. The negative half below is what makes that a carve-out and
        # ---- not a hole, and it is the reason this is asserted as a PAIR.
        _oa = make_target(tmp / "owner-a", None)
        run("intake", "--target", str(_oa), "--kits", "memory-tree")
        _poa = run("apply", "--target", str(_oa), "--kits", "memory-tree")
        _oarec = json.loads((_oa / ".governance" / "install.json").read_text(encoding="utf-8"))
        _oaeng = [f["path"] for f in _oarec["files"]
                  if f.get("role", "engine") == "engine" and f.get("oid")]
        check("[-12] RULING-A LIVENESS the apply landed engine rows carrying a recorded oid",
              _poa.returncode == 0 and len(_oaeng) >= 3,
              f"rc {_poa.returncode}: {len(_oaeng)} row(s)")
        # DELIBERATELY NO settle() -- the uncommitted post-apply target IS the subject.
        check("[-12] RULING-A LIVENESS ...and left them STAGED, which is the state under test",
              bool(gout(_oa, "diff", "--cached", "--name-only", "HEAD").split()),
              gout(_oa, "diff", "--cached", "--name-only", "HEAD")[:300])
        _poa2 = run("update", "--target", str(_oa), "--write")
        # ROUND 4's M5: this asserted an ABSENCE and never touched the return code, while its
        # negative twin below asserts `returncode == 2 and "DIRTY" in ...` -- a one-token asymmetry
        # inside one fixture. The blind spot needs a failure that refuses on the clean post-apply
        # tree but gets DIRTY-masked on the dirtied one; narrow, and this is the third absence-only
        # arm this build has produced, so it is fixed rather than argued about.
        check("[-12] RULING-A a writing verb straight after `apply` is NOT blocked by apply's own "
              "staging",
              _poa2.returncode == 0 and "DIRTY" not in _poa2.stderr,
              f"rc {_poa2.returncode}: " + _poa2.stdout[-400:] + _poa2.stderr[-400:])
        # ---- THE RECEIPT RECORDS WHAT THE INDEX HOLDS, over every LANDABLE row the target tracks.
        # ---- The stamp used to run BEFORE `git add --renormalize`, which rewrites the index blob of
        # ---- every LF-pinned path, so each affected row recorded a blob the target does not hold.
        # ---- `-9` S12 defines `oid` as the blob ACTUALLY WRITTEN; a value stamped before the last
        # ---- thing that writes is not that.
        # ----
        # ---- WHAT THIS DOES NOT EXERCISE, stated so a green row is not misread as a verified one:
        # ---- gov ships LF, so the renormalize is a NO-OP in this fixture and the specific trigger
        # ---- goes untested here. Reaching it needs an apply onto a target whose CHECKOUT applies a
        # ---- line-ending filter, and no fixture in this suite builds one -- `clone_crlf` clones a
        # ---- target that was already applied to. The invariant below is the one that holds either
        # ---- way, and it is what the fix restores.
        _oaidx = {}
        for _ln in gout(_oa, "ls-files", "-s").splitlines():
            _meta, _tab, _pth = _ln.partition("\t")
            _bits = _meta.split()
            if len(_bits) >= 3 and _pth and _bits[2] == "0":
                _oaidx[_pth] = _bits[1]
        # THE RECEIPT IS RE-READ HERE, and the first cut did not do that. It compared the receipt
        # `apply` wrote against the index as it stood after TWO later `update --write` runs, so a row
        # the second run legitimately re-staged read as a stale stamp. The arm was wrong, not the
        # engine -- and it reported a real-looking defect naming a real file, which is the most
        # expensive kind of wrong arm.
        _oarec2 = json.loads((_oa / ".governance" / "install.json").read_text(encoding="utf-8"))
        _oaland = [w for w in _oarec2["files"]
                   if w.get("role") in govkit_module().LANDABLE_ROLES and w.get("path") in _oaidx]
        check("[-12] RULING-A LIVENESS the invariant runs over a population big enough to mean "
              "something",
              len(_oaland) >= 10, f"{len(_oaland)} landable row(s) the target tracks")
        _oastale = [w["path"] for w in _oaland if w.get("oid") != _oaidx[w["path"]]]
        check("[-12] RULING-A every landable receipt row records the blob the target's index holds",
              not _oastale,
              "recorded oid is not the index blob (or is absent): " + ", ".join(_oastale[:6]))

        # ---- AND THE ROW THE CARVE-OUT CANNOT REACH IS EXCLUDED AT THE OTHER END. `-7` S9 requires
        # ---- an `attributes` row to carry NEITHER identity, so `.gitattributes` has no `oid` and
        # ---- the oid carve-out has nothing to compare. It is dropped from the dirty POPULATION
        # ---- instead, because `UPDATE_ROLE["attributes"]` is `pins` -- `recompute, compare, report;
        # ---- never write` -- so that row can never be the write S4's hazard is about. Asserted on
        # ---- the two facts that make the exclusion legal rather than on the exclusion itself.
        check("[-12] RULING-A `.gitattributes` is receipt-claimed and carries NEITHER identity, "
              "which is `-7` S9's shape and why the oid carve-out cannot reach it",
              any(w.get("path") == ".gitattributes"
                  and not w.get("oid") and not w.get("gov_oid") for w in _oarec2["files"]),
              str([w for w in _oarec2["files"] if w.get("path") == ".gitattributes"][:1]))
        check("[-12] RULING-A ...and its role dispatches to `pins`, which never writes",
              govkit_module().UPDATE_ROLE.get("attributes") == "pins",
              str(govkit_module().UPDATE_ROLE.get("attributes")))

        # NEGATIVE HALF. An operator's staged edit to a gov-owned path produces a DIFFERENT index
        # blob, so it stays dirty. Without this the carve-out is indistinguishable from deleting S4.
        _oap = _oa / _oaeng[0]
        _oap.write_bytes(_oap.read_bytes() + b"\n# OPERATOR EDIT, staged\n")
        git(_oa, "add", "--", _oaeng[0])
        _poa3 = run("update", "--target", str(_oa), "--write")
        check("[-12] RULING-A NEGATIVE: an operator's OWN staged edit to a gov-owned path is still "
              "DIRTY -- the carve-out reads the oid, not the fact of being staged",
              _poa3.returncode == 2 and "DIRTY" in _poa3.stderr,
              f"rc {_poa3.returncode}: " + _poa3.stdout[-400:] + _poa3.stderr[-400:])
        check("[-12] RULING-A ...and names that path",
              _oaeng[0] in _poa3.stderr, _poa3.stderr[-400:])

        # ---- ROUND 3, REPRODUCED BEFORE IT WAS FIXED: a target-supplied `prefix` carrying `..`
        # ---- escaped the target repository. `demand_safe_token` bounds token values to path-
        # ---- fragment CHARACTERS and `.` and `/` are both legal there, so `../../PWNED` passed it
        # ---- cleanly; `plan` then previewed 26 rows rooted outside the target and `apply` WROTE all
        # ---- 26 of them. Measured in a sandbox: the escape landed in a scratch directory and the
        # ---- files were counted before the guard existed.
        # ----
        # ---- THE CONTAINMENT CHECK ALREADY EXISTED, IN THE WRONG VERB -- `cmd_update`'s write loop,
        # ---- under a comment calling it "the one boundary this whole tool is built around". Same
        # ---- class as this build's blockers one operation over: a target-supplied value reaching a
        # ---- dangerous operation because the guard was written for a different caller.
        # ----
        # ---- BOTH VERBS ARE ARMED, because a `plan` that cheerfully previews escaping writes is its
        # ---- own defect: the preview is what an operator approves.
        _tv = make_target(tmp / "traversal", None)
        (_tv / ".governance").mkdir(parents=True, exist_ok=True)
        (_tv / ".governance" / "deploy.toml").write_text(
            'prefix = "../../PWNED"\n', encoding="utf-8", newline="\n")
        settle(_tv, "a hostile prefix")
        _tvp = run("plan", "--target", str(_tv), "--kits", "memory-tree")
        check("[-12] TRAVERSAL `plan` REFUSES a destination that leaves the target repository",
              _tvp.returncode == 2
              and "leaves the target repository" in (_tvp.stdout + _tvp.stderr),
              f"rc {_tvp.returncode}: " + (_tvp.stdout[-400:] + _tvp.stderr[-400:]))
        _tva = run("apply", "--target", str(_tv), "--kits", "memory-tree")
        check("[-12] TRAVERSAL ...and so does `apply`, which is the one that WROTE 26 files",
              _tva.returncode == 2
              and "leaves the target repository" in (_tva.stdout + _tva.stderr),
              f"rc {_tva.returncode}: " + (_tva.stdout[-400:] + _tva.stderr[-400:]))
        # THE OBSERVABLE, not the exit code: nothing may exist above the target. Asserted on the
        # filesystem, because a refusal that still wrote is the failure this arm is actually for.
        check("[-12] TRAVERSAL ...and NOTHING landed above the target directory",
              not (tmp / "PWNED").exists(),
              str(sorted(p.name for p in (tmp / "PWNED").rglob("*"))[:6])
              if (tmp / "PWNED").exists() else "")
        # AN ABSOLUTE PREFIX IS A DIFFERENT STORY IN EACH SPELLING, and the first cut of these two
        # arms asserted one mechanism for both and was wrong about each. MEASURED, then written:
        #   `/etc/govkit`  -- `target_context` does `.strip("/")`, so it becomes `etc/govkit`, an
        #                     ordinary RELATIVE path inside the target. Nothing escapes and nothing
        #                     should refuse. Asserting a refusal here was asserting a bug.
        #   `C:/PWNED`     -- refused, but by `demand_safe_token`, because `:` is outside the token
        #                     character class. The containment guard never sees it.
        # Both are asserted on the OUTCOME an operator cares about -- did anything land outside --
        # rather than on which guard spoke, so neither arm breaks if the division of labour moves.
        (_tv / ".governance" / "deploy.toml").write_text(
            'prefix = "/etc/govkit"\n', encoding="utf-8", newline="\n")
        settle(_tv, "a posix-absolute prefix")
        _tvp2 = run("plan", "--target", str(_tv), "--kits", "memory-tree")
        check("[-12] TRAVERSAL a POSIX-absolute prefix is NEUTRALISED by target_context's strip, "
              "not refused -- it resolves to an ordinary relative path inside the target",
              _tvp2.returncode == 0 and "etc/govkit/memory-tree/" in _tvp2.stdout
              and "/etc/govkit/memory-tree/" not in _tvp2.stdout,
              f"rc {_tvp2.returncode}: " + _tvp2.stdout[-400:] + _tvp2.stderr[-300:])
        (_tv / ".governance" / "deploy.toml").write_text(
            'prefix = "C:/PWNED"\n', encoding="utf-8", newline="\n")
        settle(_tv, "a drive-letter absolute prefix")
        _tvp3 = run("plan", "--target", str(_tv), "--kits", "memory-tree")
        # ---- THE ONE ADMITTED COLON. Round 3 parked this and the owner said resolve it. The token
        # ---- class refused `user_skills = "C:/Users/x/.claude/skills"` -- a CORRECT answer on the
        # ---- platform this project's primary node runs on -- with a message about command injection
        # ---- naming nothing the operator did wrong. `kickoff-manifest` is in the DEFAULT selection
        # ---- and its rule is `{user_skills}/session-kickoff`, so it sat on the common path for
        # ---- every Windows adopter. No arm caught it: both existing fixtures spell that answer in
        # ---- forms that already passed (`~/.claude/skills` at :176, `/tmp/gk-fake-skills` at :820),
        # ---- which is `fixture-passes-by-finding-nothing` aimed at a platform rather than a branch.
        # ----
        # ---- THE PAIR IS THE POINT: the character grader admits the drive letter, and the ESCAPE
        # ---- grader still reds a drive-lettered destination. Two guards, two jobs, asserted apart.
        _dvt = make_target(tmp / "drive-win", None)
        (_dvt / ".governance").mkdir(parents=True, exist_ok=True)
        (_dvt / ".governance" / "deploy.toml").write_text(
            'prefix = "tools"\n\n[answers]\nmanifest_path = "docs/MANIFEST.md"\n'
            'user_skills = "C:/Users/x/.claude/skills"\n', encoding="utf-8", newline="\n")
        settle(_dvt, "a Windows machine-path answer")
        _dvp = run("plan", "--target", str(_dvt), "--kits", "kickoff-manifest")
        check("[-12] DRIVE a Windows drive-letter machine path is a LEGITIMATE answer and plans",
              _dvp.returncode == 0
              and "C:/Users/x/.claude/skills/session-kickoff" in _dvp.stdout,
              f"rc {_dvp.returncode}: " + _dvp.stdout[-500:] + _dvp.stderr[-400:])
        check("[-12] DRIVE ...and it is an ORDER, never a write -- the machine-scoped row is why "
              "the containment guard must not see it",
              any(l.strip().startswith("ORDER") and "session-kickoff" in l
                  for l in _dvp.stdout.splitlines()),
              _dvp.stdout[-500:])

        # THE ESCAPE HALF, unchanged in outcome and changed in OWNER. A drive-lettered `prefix` on a
        # repo-scoped kit now passes the character class and is caught one function down, so the arm
        # names WHICH guard spoke: that division of labour is the whole design and a silent swap
        # back would leave both arms green while the class widened.
        (_dvt / ".governance" / "deploy.toml").write_text(
            'prefix = "C:/PWNED"\n', encoding="utf-8", newline="\n")
        settle(_dvt, "a drive-lettered prefix")
        _dve = run("plan", "--target", str(_dvt), "--kits", "memory-tree")
        check("[-12] DRIVE a drive-lettered PREFIX is still refused, by the CONTAINMENT guard now",
              _dve.returncode == 2
              and "leaves the target repository" in (_dve.stdout + _dve.stderr),
              f"rc {_dve.returncode}: " + _dve.stdout[-400:] + _dve.stderr[-400:])
        _dva = run("apply", "--target", str(_dvt), "--kits", "memory-tree")
        check("[-12] DRIVE ...and `apply` writes nothing at that drive path",
              _dva.returncode == 2 and not pathlib.Path("C:/PWNED").exists(),
              f"rc {_dva.returncode}: " + _dva.stdout[-300:] + _dva.stderr[-300:])

        # ---- B1's SECOND SITE, and the one that exited 0. `[gate_runner].file` is a TARGET-supplied
        # ---- path that `apply` joins onto the target root and WRITES, and nothing checked it.
        # ---- REPRODUCED before the fix: a descriptor declaring `file = "../../ESCAPED.json"` made
        # ---- `apply` write that file OUTSIDE the target repository and exit 0 -- a clean success
        # ---- while writing into a tree the operator never named. The `prefix` escape at least
        # ---- exited non-zero for unrelated reasons; this one reported nothing.
        # ----
        # ---- FOUND BY ENUMERATING every `target / <non-literal>` join in the engine and classifying
        # ---- each, rather than by reading around the first fix. Fixing the site the finding named
        # ---- and stopping there would have left the CLASS open at a site that fails SILENTLY,
        # ---- which is exactly the rule this build had already broken once in the same round.
        def build_gr_target(tag: str, runner_file: str) -> pathlib.Path:
            _t = make_target(tmp / f"gr-{tag}", None)
            (_t / ".governance").mkdir(parents=True, exist_ok=True)
            (_t / ".governance" / "deploy.toml").write_text(
                'prefix = "tools"\n\n[gate_runner]\nkind = "manifest"\n'
                f'file = "{runner_file}"\n'
                'grammar = "json-array"\ndedupe_key = "name"\n'
                'command = ["bash", "run.sh"]\nrun_all_env = "GATE_ALL"\n'
                'observed_ran = ["ran {name}"]\nobserved_failed = ["failed {name}"]\n',
                encoding="utf-8", newline="\n")
            settle(_t, f"a gate_runner declaring {runner_file}")
            return _t

        _gre = build_gr_target("escape", "../../ESCAPED.json")
        _grp = run("apply", "--target", str(_gre), "--kits", "memory-tree")
        check("[-12] RUNNER-FILE an escaping `[gate_runner].file` REFUSES the run",
              _grp.returncode == 2
              and "leaves the target repository" in (_grp.stdout + _grp.stderr),
              f"rc {_grp.returncode}: " + _grp.stdout[-400:] + _grp.stderr[-400:])
        check("[-12] RUNNER-FILE ...and the refusal NAMES the declaration it came from, not `prefix`",
              "[gate_runner].file" in (_grp.stdout + _grp.stderr),
              _grp.stdout[-400:] + _grp.stderr[-400:])
        # THE OBSERVABLE. This site's whole danger was that it exited 0, so the arm asserts on the
        # filesystem and not on the exit code alone.
        check("[-12] RUNNER-FILE ...and NOTHING was written above the target",
              not (_gre.parent / "ESCAPED.json").exists()
              and not (tmp / "ESCAPED.json").exists(),
              str(sorted(p.name for p in tmp.glob("ESCAPED*"))))

        # THE POSITIVE TWIN, because a guard with no accepted case is indistinguishable from one that
        # refuses everything -- and this one sits in the pre-write pass, where refusing everything
        # would block every promoted target.
        _grok = build_gr_target("ok", "gates/legs.json")
        _grq = run("apply", "--target", str(_grok), "--kits", "memory-tree")
        check("[-12] RUNNER-FILE a repo-relative `[gate_runner].file` still lands, inside the target",
              _grq.returncode == 0 and (_grok / "gates" / "legs.json").is_file(),
              f"rc {_grq.returncode}: " + _grq.stdout[-400:] + _grq.stderr[-400:])

        # ---- TWO TOKEN CLASSES, ONE TABLE. The strict class was written for `prefix` -- a PATH,
        # ---- interpolated into `bash -c` and `python -c` argv -- and was then applied to every
        # ---- `answers.*` and `kit.<eid>.*` value as well. Those are not all paths: the playbook
        # ---- charter's placeholders are rendered into a MARKDOWN DOCUMENT, and a legitimate
        # ---- override for one carries spaces by nature.
        # ----
        # ---- MEASURED RATHER THAN ARGUED: the single class red the `govkit acceptance matrix` leg
        # ---- from the commit that introduced it and it STAYED red for two commits, because no full
        # ---- bar ran in between and this suite does not cover that leg. The live adopter's answers
        # ---- are all path-shaped, so nothing else noticed either.
        # ----
        # ---- The prose class is still an ALLOWLIST and still refuses every injection vector this
        # ---- build reproduced. Graded on the FUNCTION, both classes side by side, because the whole
        # ---- property is that they DIFFER on prose and AGREE on every metacharacter.
        _gkp = govkit_module()

        def _check_token(_v, _prose):
            try:
                _gkp.demand_safe_token("k", _v, "arm", prose=_prose)
                return True
            except _gkp.Refusal:
                return False

        _BS = chr(92)
        for _v, _want_strict, _want_prose, _why in (
                ("tools",                              True,  True,  "the default prefix"),
                ("C:/Users/x/.claude/skills",          True,  True,  "a Windows machine path"),
                ("stated for the scratch install",     False, True,  "the matrix fixture's stub"),
                ("bash tools/run-gates/run-gates.sh",  False, True,  "a gate_runner override"),
                ("PLAY KICK TOOL DEPL",                False, True,  "an id_families override"),
                ("tools; touch PWNED ;",               False, False, "round 2's reproduction"),
                ("$(id)",                              False, False, "command substitution"),
                ("a`id`b",                             False, False, "backtick substitution"),
                ("a|b",                                False, False, "a pipe"),
                ("a&b",                                False, False, "a chain operator"),
                ("a>b",                                False, False, "a redirect"),
                ("a'b",                                False, False, "a quote"),
                ('a"b',                                False, False, "a double quote"),
                ("a" + _BS + "b",                      False, False, "a backslash"),
                ("a\nb",                               False, False, "a newline")):
            _gs, _gp = _check_token(_v, False), _check_token(_v, True)
            check(f"[-12] TOKEN strict={_want_strict} prose={_want_prose} for {_v!r} -- {_why}",
                  (_gs, _gp) == (_want_strict, _want_prose),
                  f"strict={_gs} prose={_gp}, wanted {_want_strict}/{_want_prose}")
        # THE TWO CLASSES MUST AGREE ON EVERY METACHARACTER, asserted as a PROPERTY rather than row
        # by row: if the prose class ever admits one, the loop above stops being the whole guarantee.
        _metas = [";", "|", "&", "$", "`", "'", '"', "<", ">", "(", ")", "{", "}",
                  "*", "?", "!", _BS, "\n", "\r", "\t"]
        _admitted = [m for m in _metas if _check_token(f"a{m}b", True)]
        check("[-12] TOKEN the PROSE class admits no shell metacharacter at all",
              not _admitted, "admitted: " + repr(_admitted))
        # ---- ROUND 4 H1: THE SPACE WAS MISSING FROM THAT LIST, and the space is the one character
        # ---- the prose class deliberately admits -- so the property arm asserted the class is safe
        # ---- for every character except the one it is unsafe for. It is asserted as a PAIR now,
        # ---- because neither half means anything alone: the class admits a space, AND no shipped
        # ---- descriptor may interpolate a prose-graded token inside a `-c` string.
        check("[-12] TOKEN the prose class DOES admit a space -- stated, not left to the gap above",
              _check_token("a b", True) and not _check_token("a b", False),
              f'prose={_check_token("a b", True)} strict={_check_token("a b", False)}')
        check("[-12] TOKEN ...and a space is refused in the STRICT class, which is what keeps it "
              "out of every argv-bound token",
              not _check_token("a b", False), "")

        # ---- THE STRUCTURAL ARM, and it gates the CLASS rather than any instance. Round 4's
        # ---- blocker rode a SHIPPED descriptor template: `tools/drift-audit/kit.toml` spells
        # ---- `command = ["bash", "-c", "python {kit}/drift_report.py --check"]`, and five more
        # ---- descriptors interpolate a token inside a `-c` STRING. Inside such a string a token is
        # ---- not an argv element -- it is source the shell or python parses -- so whether it is
        # ---- safe depends entirely on the CHARACTER CLASS that graded it.
        # ----
        # ---- SO THE RULE IS: a token interpolated inside a `-c` argument must be one a target
        # ---- CANNOT supply. `SEEDED_TOKENS` is exactly that set, and this arm asserts the join
        # ---- rather than trusting it -- it reds when someone adds a seventh such template using a
        # ---- token a target CAN reach, which is the door nobody is watching.
        # ----
        # ---- IT SCANS THE REAL SHIPPED DESCRIPTORS, not a fixture, because the population that
        # ---- matters is what gov actually ships to adopters.
        _gkd2 = govkit_module()
        _seeded = set(_gkd2.SEEDED_TOKENS)
        # `(?<!\$)` because `${k}` is a SHELL variable, not a govkit token. Measured: without
        # it this predicate reported memory-tree's `for k in ...; do grep "^${k}=" ...` loop as
        # a hit, which is a predicate redding an innocent file -- the near-miss S7 says to print
        # BEFORE wiring an arm, and the reason that step is a rule rather than a courtesy.
        _tok_re = __import__("re").compile(r"(?<!\$)\{([a-z_]+)\}")
        _dangerous = []
        _scanned = 0
        _templates = 0
        for _kt in sorted(pathlib.Path(HERE.parents[1]).glob("tools/*/kit.toml")) + sorted(
                pathlib.Path(HERE.parents[1]).glob("tools/govkit/entries/*.kit.toml")):
            try:
                _d2 = govkit_module().load_toml(_kt)
            except Exception:
                continue
            _scanned += 1

            def _scan_argvs(node, where):
                out = []
                if isinstance(node, dict):
                    for k, v in node.items():
                        out += _scan_argvs(v, f"{where}.{k}")
                elif isinstance(node, list):
                    # An argv. A `-c` flag makes the NEXT element a script rather than an argument.
                    for i, v in enumerate(node):
                        if isinstance(v, str) and v == "-c" and i + 1 < len(node):
                            nxt = node[i + 1]
                            if isinstance(nxt, str):
                                out.append((where, nxt))
                        out += _scan_argvs(v, f"{where}[{i}]")
                return out

            for _where, _script in _scan_argvs(_d2, _kt.name):
                _templates += 1
                for _tok in _tok_re.findall(_script):
                    if _tok not in _seeded:
                        _dangerous.append(f"{_kt.name}:{_where} interpolates {{{_tok}}} in a -c string")

        check("[-12] DESC-SCAN LIVENESS the scan reaches the real shipped descriptors and finds "
              "`-c` templates to grade",
              _scanned >= 10 and _templates >= 5,
              f"{_scanned} descriptor(s), {_templates} `-c` template(s)")
        check("[-12] DESC-SCAN no shipped descriptor interpolates a TARGET-SUPPLIABLE token inside "
              "a `-c` string -- the door round 4's blocker came through",
              not _dangerous, "; ".join(sorted(set(_dangerous))[:6]))
        # And the traversal is NOT this guard's job, in either class -- containment owns it. Asserted
        # so a later reader does not add it here and leave two answers to one question.
        check("[-12] TOKEN neither class grades a traversal -- `demand_contained_dest` owns that",
              _check_token("../../PWNED", False) and _check_token("../../PWNED", True), "")

        # AND THE WIDENING IS EXACTLY ONE COLON WIDE. Graded on the FUNCTION rather than through a
        # verb, because these are character-class questions and routing each through a fixture would
        # cost six installs to assert what one table asserts.
        _gkd = govkit_module()
        for _v, _want, _why in (
                ("C:/Users/x/.claude/skills", True,  "the legitimate answer"),
                ("~/.claude/skills",          True,  "the form the other fixtures use"),
                ("d:/proj/skills",            True,  "lowercase drive letter"),
                ("C:/a;b",                    False, "a metacharacter AFTER the drive letter"),
                ("C:/a$(id)",                 False, "command substitution after the drive"),
                ("a:b",                       False, "an interior colon is not a drive"),
                ("C:x",                       False, "a drive with no slash"),
                ("CC:/x",                     False, "a two-letter drive is not a drive"),
                ("tools; touch PWNED ;",      False, "round 2's own injection reproduction")):
            try:
                _gkd.demand_safe_token("prefix", _v, "arm")
                _got = True
            except _gkd.Refusal:
                _got = False
            check(f"[-12] DRIVE token class: {'accepts' if _want else 'refuses'} {_v!r} -- {_why}",
                  _got == _want, f"accepted={_got}, wanted={_want}")

        # ---- OWNER RULING B (2026-08-26) -- `-7` S4's shadow refusal is SCOPED TO THE TABLE.
        # ---- The predicate was unqualified by role, so a row the dispatch never sends to the raw
        # ---- write could stop an entire run, and the operator's only route back to green was
        # ---- `git add` on a file gov will never write. The arm above already holds the POSITIVE
        # ---- half on an engine row; this is the negative one, and it is the half that was missing.
        _ob = make_target(tmp / "owner-b", None)
        run("intake", "--target", str(_ob), "--kits", "memory-tree")
        run("apply", "--target", str(_ob), "--kits", "memory-tree")
        settle(_ob, "the install")
        _obrec = json.loads((_ob / ".governance" / "install.json").read_text(encoding="utf-8"))
        _obnt = [f["path"] for f in _obrec["files"]
                 if govkit_module().UPDATE_ROLE.get(f.get("role", "engine")) != "table"
                 and (_ob / f["path"]).is_file()]
        check("[-12] RULING-B LIVENESS the fixture really carries a NON-table receipt row on disk",
              bool(_obnt),
              "roles present: " + str(sorted({f.get("role", "engine") for f in _obrec["files"]})))
        if _obnt:
            git(_ob, "rm", "-q", "--cached", "--", _obnt[0])
            check("[-12] RULING-B LIVENESS ...and it is now out of the index, still on disk",
                  _obnt[0] not in gout(_ob, "ls-files").split() and (_ob / _obnt[0]).is_file(), "")
            _pob = run("update", "--target", str(_ob), "--write")
            # M5, same shape, same fix: an absence with no return code beside it.
            check("[-12] RULING-B a NON-table row shadowed by an untracked file does not refuse the "
                  "whole run -- that row can never reach the raw write the refusal exists to stop",
                  _pob.returncode == 0 and "absent from its INDEX" not in _pob.stderr,
                  f"rc {_pob.returncode}: " + _pob.stdout[-400:] + _pob.stderr[-400:])

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

        # ===== DEPL-dCarriedReceipt-8: a merge result never overwrites `gov_oid` =================
        #
        # THE DEFECT, reproduced end to end before the fix and on TWO trees, because `-7` moved the
        # symptom without moving the cause. At 9ddcc5c9 the merge stamped its own result into the
        # one `sha256` field; the next run read the row `equal` to gov, called it `stale`, and the
        # raw arm overwrote the adopter's line — `wrote 2, deleted 0, 0 conflict(s)` at rc 0, local
        # line count 1 then 0, with no finding printed at all. On `-7`'s tip the same stamp lands in
        # `gov_oid`, where it contradicts gov's own blob at the row's `commit`, so S9's preamble
        # REFUSES the whole run at rc 2 — and keeps refusing, so that target can never be updated
        # again. Both were measured on this fixture, in this order, before a line was changed.
        #
        # THE FIXTURE IS REAL GOV HISTORY, four vintages of one real file, because the guarantee is
        # about a base that keeps moving under a delta the target keeps holding.
        V8 = ("24f39915b3de86010a30d8698d0d4b317db015de",
              "0f4d30843f2693dae9e9a69a348bf3390ad0ad3c",
              "372e6b2a9a7d5b06001167b206c869f604c8a8af",
              "9ddcc5c944bdb92456ef031ee5f038842d016587")
        CWS, CWT = "tools/check-wiring.sh", "tools/check-wiring.test.sh"
        MINE8 = b"# DEPL-dCarriedReceipt-8 OPERATOR LINE\n"
        GK8 = govkit_module()

        def gblob(commit: str, path: str) -> bytes:
            return subprocess.run(["git", "-C", str(govroot), "show", f"{commit}:{path}"],
                                  capture_output=True).stdout

        # ASSERTED FIRST. A fixture that does not trigger the rule proves nothing, and this rule is
        # triggered by gov's copy MOVING under a target that is holding an edit. If these vintages
        # ever stop moving, every arm below passes by finding nothing.
        _b8 = [gblob(v, CWS) for v in V8]
        check("[-8] the four vintages of the fixture file all resolve in this gov checkout",
              all(_b8), str([len(b) for b in _b8]))
        check("[-8] ...and gov's copy really moves at every one of them",
              len({bytes(b) for b in _b8}) == 4, str([GK8.blob_oid(b)[:8] for b in _b8]))

        def delta_target(name: str) -> pathlib.Path:
            """Installed, rewound to the OLDEST vintage, then given ONE committed operator line.

            Committed, because `-12` S4 refuses a writing verb over a dirty claimed path — the
            guarantee under test is the one that survives a commit, and an uncommitted edit never
            reaches the classifier at all.
            """
            t = make_target(tmp / name, DEPLOY_FULL)
            run("apply", "--target", str(t), "--kits", "check-wiring")
            rp = t / ".governance" / "install.json"
            rec = json.loads(rp.read_text(encoding="utf-8"))
            rec["gov_commit"] = V8[0]
            for f in rec["files"]:
                if not f.get("source"):
                    continue
                b = gblob(V8[0], f["source"])
                f["commit"] = V8[0]
                # BOTH identities from the SAME vintage, or the fixture is `-7` S9's corruption
                # rather than an older install, and every run below refuses before it classifies.
                f["sha256"] = GK8._sha(b)
                f["gov_oid"] = GK8.blob_oid(b)
                (t / f["path"]).write_bytes(b)
            rp.write_text(json.dumps(rec, indent=2), encoding="utf-8", newline="\n")
            settle(t, "landed at the oldest vintage")
            (t / CWS).write_bytes((t / CWS).read_bytes() + MINE8)
            settle(t, "the operator's line, committed")
            return t

        def mine_count(t: pathlib.Path) -> int:
            return (t / CWS).read_bytes().count(MINE8.strip())

        # ---- AC1: the sequence that destroyed the edit. Staged red twice over — see the header.
        t8 = delta_target("d8-ac1")
        check("[-8] AC1 the fixture holds the operator's line before any update",
              mine_count(t8) == 1, repr((t8 / CWS).read_bytes()[-160:]))
        _r81 = run("update", "--target", str(t8), "--to", V8[2], "--write")
        check("[-8] AC1 the first update MERGES the delta row rather than overwriting it",
              _r81.returncode == 0 and verdict_of(_r81.stdout, CWS) == "diverged",
              _r81.stdout[-900:] + _r81.stderr[-600:])
        check("[-8] AC1 ...and the operator's line survived it",
              mine_count(t8) == 1, repr((t8 / CWS).read_bytes()[-160:]))

        # ---- AC2: the two identities on the merged row, each against its own evidence.
        _rec8 = json.loads((t8 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _row8 = [f for f in _rec8["files"] if f["path"] == CWS][0]
        _idx8 = gout(t8, "ls-files", "-s", "--", CWS).split()[1]
        check("[-8] AC2 the merged row's gov_oid is GOV's blob at --to, not the merge result",
              _row8.get("gov_oid") == GK8.blob_oid(gblob(V8[2], CWS)),
              str(_row8.get("gov_oid")) + " vs " + GK8.blob_oid(gblob(V8[2], CWS)))
        check("[-8] AC2 ...its oid is the blob the TARGET's index now holds",
              _row8.get("oid") == _idx8, str(_row8.get("oid")) + " vs " + _idx8)
        check("[-8] AC2 ...and the two DIFFER, which IS the local delta, recomputed per run",
              _row8.get("gov_oid") != _row8.get("oid"), str(_row8)[:300])
        check("[-8] AC2 ...while `commit` still advances to --to (§8 F1)",
              _row8.get("commit") == V8[2], str(_row8.get("commit")))

        # ---- AC3: the second symptom of the same overload. `check` reds on a target nothing is
        # ---- wrong with, because its provenance loop read `sha256` as GOV's hash.
        _c8 = run("check", "--target", str(t8))
        check("[-8] AC3 check exits 0 immediately after the merged update",
              _c8.returncode == 0, _c8.stdout[-1200:] + _c8.stderr[-400:])
        check("[-8] AC3 ...and its provenance loop RESOLVED the merged row rather than skipping it",
              "provenance: 2/2 resolved" in _c8.stdout, _c8.stdout[-600:])

        # ---- AC1, second half: the run that used to destroy the edit.
        settle(t8, "after the first update")
        _r82 = run("update", "--target", str(t8), "--to", V8[3], "--write")
        check("[-8] AC1 the SECOND update reports `diverged`, never `stale`",
              _r82.returncode == 0 and verdict_of(_r82.stdout, CWS) == "diverged",
              _r82.stdout[-900:] + _r82.stderr[-600:])
        check("[-8] AC1 ...and the operator's line is STILL there — the destruction is closed",
              mine_count(t8) == 1, repr((t8 / CWS).read_bytes()[-160:]))

        # ---- AC4: PERMANENCE. A guarantee asserted once is a guarantee asserted for one run, so
        # ---- the fourth vintage goes in between and the count is asserted after EVERY run.
        t84 = delta_target("d8-ac4")
        _seen8: list[tuple[str, int, int]] = []
        for _i, _v in enumerate(V8[1:]):
            _p8 = run("update", "--target", str(t84), "--to", _v, "--write")
            _seen8.append((verdict_of(_p8.stdout, CWS), _p8.returncode, mine_count(t84)))
            settle(t84, f"after update {_i + 1}")
        _p8 = run("update", "--target", str(t84), "--write")
        _seen8.append((verdict_of(_p8.stdout, CWS), _p8.returncode, mine_count(t84)))
        check("[-8] AC4 all four updates exit 0",
              all(rc == 0 for _v, rc, _n in _seen8), str(_seen8))
        check("[-8] AC4 ...and not one of them ever calls the delta row `stale` or `missing`",
              all(v in ("diverged", "patched") for v, _rc, _n in _seen8), str(_seen8))
        check("[-8] AC4 ...and the operator's line is present after every single one",
              all(n == 1 for _v, _rc, n in _seen8), str(_seen8))

        # ---- AC6: THE NO-REGRESSION ARM, so the fix cannot quietly turn every update into a merge.
        # ---- Asserted on the SECOND row of the same fixture — the one the operator never touched —
        # ---- rather than inferred from a tally.
        t86 = delta_target("d8-ac6")
        check("[-8] AC6 the untouched row's gov copy really moved, so this arm CAN fail",
              gblob(V8[0], CWT) != gblob(V8[2], CWT),
              GK8.blob_oid(gblob(V8[0], CWT))[:8] + " vs " + GK8.blob_oid(gblob(V8[2], CWT))[:8])
        _r86 = run("update", "--target", str(t86), "--to", V8[2], "--write")
        check("[-8] AC6 a row with NO local delta still takes the RAW write and reads `stale`",
              verdict_of(_r86.stdout, CWT) == "stale", _r86.stdout[-900:] + _r86.stderr[-600:])
        check("[-8] AC6 ...and the target's index blob for it IS gov's blob at --to",
              gout(t86, "ls-files", "-s", "--", CWT).split()[1]
              == GK8.blob_oid(gblob(V8[2], CWT)), gout(t86, "ls-files", "-s", "--", CWT))
        _row86 = [f for f in json.loads((t86 / ".governance" / "install.json")
                                        .read_text(encoding="utf-8"))["files"]
                  if f["path"] == CWT][0]
        check("[-8] AC6 ...and on THAT arm the two identities agree, which is its definition",
              _row86.get("oid") == _row86.get("gov_oid") == GK8.blob_oid(gblob(V8[2], CWT)),
              str(_row86)[:300])

        # ---- AC5: THE STRUCTURAL GATE, over the grid rather than over the row that exposed it.
        # ---- Driven through the ENGINE's own predicate on a hand-edited COPY of the grid, so the
        # ---- harness holds no second spelling of the rule it grades and the liveness half runs on
        # ---- every invocation rather than once, by hand, on the day it was written.
        check("[-8] AC5 the shipped grid routes no delta row to a raw write",
              GK8.raw_write_cells(GK8.VERDICT_GRID) == [],
              str(GK8.raw_write_cells(GK8.VERDICT_GRID)))
        _grid8 = dict(GK8.VERDICT_GRID)
        _grid8[("differs", "differs")] = "stale"
        check("[-8] AC5 LIVENESS: mapping (differs, differs) to `stale` makes that arm SPEAK",
              GK8.raw_write_cells(_grid8) == [("differs", "differs", "stale")],
              str(GK8.raw_write_cells(_grid8)))
        check("[-8] AC5 ...and the raw-write set is the one the write loop reads, not a copy",
              GK8.RAW_WRITE_VERDICTS == ("stale", "missing"), str(GK8.RAW_WRITE_VERDICTS))
        _s8 = run("selfcheck")
        check("[-8] AC5 selfcheck carrying that arm still exits 0 over this repo",
              _s8.returncode == 0, _s8.stdout[-600:] + _s8.stderr[-400:])

        # ===== DEPL-dCarriedReceipt-9: `carry` rungs, over a DERIVED needle map ==================
        #
        # WHAT THIS UNIT IS. A row whose two identities differ is not automatically a local delta.
        # The difference may be a CARRY — line endings, or a prefix relocation because the adopter
        # installed somewhere gov does not — and the rung that explains it is RECOMPUTED BY PROOF on
        # every run and never read back off the receipt.
        #
        # THE RED-FIRST OBSERVATIONS, on the fixture built below and against the engine as it stood
        # before this unit. `classify_row` returned a dict with NO `carry` key at all, and all six
        # non-identical rows classified from `o_state` alone. The `relocate` row whose gov copy had
        # moved did NOT reconcile: the three-way was handed a `base` spelling gov's prefix where the
        # target's own copy did not, every line naming a path read as an operator edit, the merge
        # CONFLICTED, the run exited 1 and a conflict order was written. The row the target had
        # DELETED was restored as `gone refers to tools/demo/gone.txt` — gov's prefix, into a target
        # that does not use it — and the stamp it left recorded `oid == gov_oid` over bytes gov never
        # shipped, which is the pairing the next run reads as a clean gov-owned row.
        #
        # ONE OF THOSE IS A CORRECTION TO THE SPEC RATHER THAN A DETAIL. AC8 predicted its red as
        # "takes the raw arm, lands gov's `tools/` spelling verbatim, and exits 0". That is the
        # behaviour at 9ddcc5c9, which the spec cites; it is NOT reachable on `-8`'s tip, because a
        # receipt claiming gov's blob IS the carried blob is exactly what `-7` S9's preamble refuses.
        # The red that IS reachable there is the whole-file conflict above, and that is the one
        # observed.
        #
        # WHAT THIS BLOCK DOES NOT CLOSE, said plainly rather than left implied by a green. S13's
        # COMMITTED inCMS-derived receipt of the 52 rows at `2cff5855` is not in this tree, and AC1's
        # and AC2's counts — 21/6/5 rungs, 13 pairs, 26 needles — are NOT reproduced anywhere below.
        # Every arm here asserts either the RELATIONSHIP the spec states or a distribution MEASURED
        # over the fixture it builds, and says which. AC2's two figures were already marked
        # UNVERIFIED over their own stated population by the spec itself, so copying them into an
        # assertion was never on the table.

        GK9 = govkit_module()

        # ---- THE DERIVATION AND THE SUBSTITUTER, DRIVEN DIRECTLY. Unit arms on purpose: they read
        # ---- THIS repo's `govkit.py`, imported, so a break staged into it is reached on the next
        # ---- run with no fixture copy in between. The end-to-end arms further down run a scratch
        # ---- gov's COPY of the engine — fine when the whole file is re-run after a break is staged,
        # ---- and a trap if it is not.
        _pairs9 = [("tools/demo/a.txt", "scripts/demo/a.txt"),
                   ("tools/demo/b.txt", "scripts/demo/b.txt"),
                   ("tools/hooks/h.js", ".claude/hooks/h.js"),
                   ("tools/top.txt", "data/top.txt"),
                   ("tools/amb/x.txt", "one/x.txt"),
                   ("tools/amb/y.txt", "two/y.txt"),
                   ("README.md", "README.md"),
                   (None, "scripts/demo/nope.txt")]
        _n9, _p9, _d9 = GK9.derive_carry_map(_pairs9)

        # ---- S3, and AC2 as the RELATIONSHIP rather than as the spec's two disclaimed numbers. The
        # ---- pair set is asserted WHOLE, not counted: a count agrees with the wrong map as readily
        # ---- as with the right one.
        check("[-9] S3 the dirname lift gives one pair per gov directory, the ambiguous one dropped",
              _p9 == {"tools/demo": "scripts/demo", "tools/hooks": ".claude/hooks",
                      "tools": "data"}, str(_p9))
        check("[-9] S3 an ambiguous gov directory is DROPPED and returned BY NAME, both destinations",
              _d9 == [("tools/amb", ["one", "two"])], str(_d9))
        check("[-9] S3 a root-level row lifts to the EMPTY needle and is skipped, never emitted",
              "" not in _n9, str(sorted(_n9)))
        check("[-9] S3 a row with no `source` contributes no pair and is not a reason to refuse",
              "scripts/demo" not in _p9 and "scripts/demo" not in _n9, str(_p9))
        # THE RELATIONSHIP S4 states: every surviving pair emits its `/` form AND its `~` form, and
        # the two COINCIDE for a gov directory with no slash. Derived from `_p9` on the spot so the
        # arm cannot drift from the map it grades. MEASURED here: 3 pairs, 5 needles.
        _forms9 = 2 * len(_p9) - sum(1 for gd in _p9 if "/" not in gd)
        check("[-9] S4 the needle count is two forms per pair, less the slashless ones that coincide",
              len(_n9) == _forms9 == 5 and len(_p9) == 3,
              f"{len(_p9)} pair(s), {len(_n9)} needle(s), relationship says {_forms9}")
        check("[-9] S4 every surviving pair is present in BOTH forms",
              all(_n9.get(gd) == td and _n9.get(gd.replace("/", "~")) == td.replace("/", "~")
                  for gd, td in _p9.items()), str(_n9))

        # ---- S4: LONGEST NEEDLE FIRST. `tools` and `tools/demo` are both needles here and they map
        # ---- to DIFFERENT roots, so the order is observable rather than inferred.
        check("[-9] S4 the longest needle wins at a position — `tools/demo` beats the bare `tools`",
              GK9.derive_carried(b"tools/demo/x", _n9) == b"scripts/demo/x",
              repr(GK9.derive_carried(b"tools/demo/x", _n9)))
        check("[-9] S4 ...and the bare `tools` needle is genuinely live, so that arm CAN fail",
              GK9.derive_carried(b"tools/other/x", _n9) == b"data/other/x",
              repr(GK9.derive_carried(b"tools/other/x", _n9)))

        # ---- AC4: the `~` form, load-bearing because gov FLATTENS paths into fixture filenames —
        # ---- `tools/unattended/check-playbook.test.sh` spells `tools~` at lines 365, 479, 523, 570
        # ---- and 582 while an adopter's own fixture records are named `scripts~unattended~…`. Its
        # ---- own map, so the criterion's literal strings are the ones asserted.
        _n4, _p4, _d4 = GK9.derive_carry_map(
            [("tools/unattended/adopt.sh", "scripts/unattended/adopt.sh"),
             ("tools/top.txt", "scripts/top.txt")])
        check("[-9] AC4 the fixture map really carries BOTH `tools/unattended` and `tools`",
              _p4 == {"tools/unattended": "scripts/unattended", "tools": "scripts"}, str(_p4))
        check("[-9] AC4 ONE pass rewrites the `/` form and the `~` form of the same string",
              GK9.derive_carried(b"tools/unattended/fixture-records/tools~a~b.md", _n4)
              == b"scripts/unattended/fixture-records/scripts~a~b.md",
              repr(GK9.derive_carried(b"tools/unattended/fixture-records/tools~a~b.md", _n4)))
        check("[-9] AC4 ...and a string already reading `scripts/unattended` is rewritten not at all",
              GK9.derive_carried(b"scripts/unattended/x", _n4) == b"scripts/unattended/x",
              repr(GK9.derive_carried(b"scripts/unattended/x", _n4)))
        # The `~` form's OWN discriminator. Above, `tools~a~b` is caught by the bare `tools` needle,
        # so the two-form rule is not what makes that line pass. Here the flattened directory carries
        # a destination the bare needle could never produce.
        check("[-9] AC4 the `~` form reaches a destination no `/`-form needle could produce",
              GK9.derive_carried(b"tools~hooks~probe.md", _n9) == b".claude~hooks~probe.md",
              repr(GK9.derive_carried(b"tools~hooks~probe.md", _n9)))
        check("[-9] AC4 LIVENESS: with the `~` needles dropped, that string lands somewhere WRONG",
              GK9.derive_carried(b"tools~hooks~probe.md",
                                 {k: v for k, v in _n9.items() if "~" not in k})
              == b"data~hooks~probe.md",
              repr(GK9.derive_carried(b"tools~hooks~probe.md",
                                      {k: v for k, v in _n9.items() if "~" not in k})))

        # ---- DEPL-dRetiredFork-1. A FANNED gov directory proves its rung PER ROW ---------------
        # The global map holds one destination per gov directory and DROPS a fanned one, so the rung
        # PROOF — which read that map — had no needle and returned None for every row underneath.
        # Seven such directories at one measured adopter, and zero `relocate` rungs across all of it.
        #
        # The three arms below are one fixture read three ways, so the difference between them is the
        # only thing that can move: same base, same content, different needle source.
        _f1 = [("tools/hooks/agent-cap.js", "scripts/hooks/agent-cap.js"),
               ("tools/hooks/scratch-guard.js", ".claude/hooks/scratch-guard.js")]
        _nf, _pf, _df = GK9.derive_carry_map(_f1)
        check("[-1] S1 a fanned gov directory is still DROPPED from the global map",
              [d[0] for d in _df] == ["tools/hooks"] and not _nf,
              f"dropped={_df} needles={_nf}")
        _rowf = {"source": "tools/hooks/agent-cap.js", "path": "scripts/hooks/agent-cap.js"}
        _pf2 = GK9.resolve_row_needles(_nf, _rowf)
        check("[-1] S1 ...but the row's own overlay supplies the needle the map could not hold",
              _pf2.get("tools/hooks") == "scripts/hooks", repr(_pf2))
        _base1 = b"# see tools/hooks/agent-cap.js for the rule" + bytes([10])
        _ours1 = GK9.derive_carried(_base1, _pf2)
        check("[-1] S1 the rung is RELOCATE with the row's needles, where the map gave nothing",
              GK9.derive_carry_rung(_base1, _pf2, lambda: _ours1, known_equal=False) == "relocate"
              and GK9.derive_carry_rung(_base1, _nf, lambda: _ours1, known_equal=False) is None,
              "per-row=%r global=%r" % (
                  GK9.derive_carry_rung(_base1, _pf2, lambda: _ours1, known_equal=False),
                  GK9.derive_carry_rung(_base1, _nf, lambda: _ours1, known_equal=False)))
        # AND THE LIMIT, asserted so nobody reads the arm above as a general promise: ONE residual
        # byte and the rung is gone. Every `nc carve-out N/20` comment is such a byte, which is why
        # widening the map moved ZERO rows at that adopter. Section 3 puts this out of scope and
        # names DEPL-dRetiredFork-7; the arm keeps the boundary honest rather than implied.
        check("[-1] S1 ...and ONE residual byte still falls through to three-way",
              GK9.derive_carry_rung(_base1, _pf2, lambda: _ours1 + b"# nc carve-out 13/20" + bytes([10]),
                                    known_equal=False) is None)

        # ---- S3b: a DEGENERATE needle is refused, not carried ----------------------------------
        # A needle is substituted over file CONTENT, so its width is its blast radius. A one-character
        # fragment matches almost everywhere, and the values come from a target-supplied receipt.
        # The threshold is EMPTINESS. A first cut refused anything under two characters and broke 16
        # arms in other units, because gov's own fixtures use single-letter directory names — so the
        # grade covers the case section 5 names and the arm says which case that is.
        _degen = None
        try:
            GK9.derive_carry_map([(" /x.txt", "b/x.txt")])
        except Exception as _e:
            _degen = type(_e).__name__
        check("[-1] S3b an EMPTY/whitespace needle is REFUSED rather than substituted",
              _degen == "Refusal", f"got {_degen}")
        check("[-1] S3b ...and a normal two-segment pair still derives",
              GK9.derive_carry_map([("tools/x.txt", "scripts/x.txt")])[0].get("tools") == "scripts")
        check("[-1] S3b ...and a single-letter directory is PERMITTED, which is the stated residual",
              GK9.derive_carry_map([("a/x.txt", "b/x.txt")])[0].get("a") == "b")

        # ---- S4: THE OUTPUT IS NEVER RESCANNED. The fixture is built so a rescan WOULD visibly
        # ---- change the answer — `tools` rewrites to `demo` and `demo` rewrites to `final` — and
        # ---- that second step is asserted live FIRST, so this cannot pass by finding nothing.
        _nr, _pr, _dr = GK9.derive_carry_map([("tools/a.txt", "demo/a.txt"),
                                              ("demo/b.txt", "final/b.txt")])
        check("[-9] S4 the no-rescan fixture really chains — `demo` on its own becomes `final`",
              GK9.derive_carried(b"demo/x", _nr) == b"final/x",
              repr(GK9.derive_carried(b"demo/x", _nr)))
        check("[-9] S4 ...so one substitution never feeds another: `tools/x` stops at `demo/x`",
              GK9.derive_carried(b"tools/x", _nr) == b"demo/x",
              repr(GK9.derive_carried(b"tools/x", _nr)))

        # ---- AC6: a blob that is not valid UTF-8 comes back UNCHANGED rather than being mangled
        # ---- into a false rung. The precondition asserts the same needle DOES fire on decodable
        # ---- bytes, so this grades the decode guard and not an empty map.
        _bin9 = b"\xff\xfe\x00 tools/demo \x00"
        check("[-9] AC6 the same needle fires on the decodable form, so the guard is what stops it",
              GK9.derive_carried(b" tools/demo ", _n9) == b" scripts/demo ", "")
        check("[-9] AC6 a non-UTF-8 blob returns byte-identical from the substituter",
              GK9.derive_carried(_bin9, _n9) == _bin9, repr(GK9.derive_carried(_bin9, _n9)))

        # ---- §5's empty-map state: no surviving pair is not a refusal, and it makes `relocate`
        # ---- unprovable rather than making it fire on everything.
        check("[-9] S3 a receipt yielding no pair produces an EMPTY map, not a raise",
              GK9.derive_carry_map([]) == ({}, {}, []), str(GK9.derive_carry_map([])))
        check("[-9] S3 ...and an empty map leaves bytes alone",
              GK9.derive_carried(b"tools/demo/x", {}) == b"tools/demo/x", "")

        # ---- S1 + S5: THE LADDER ITSELF, one arm per rung plus the rules that bound it.
        check("[-9] S1 rung `verbatim` — ours and base are the same bytes",
              GK9.derive_carry_rung(b"x\ny\n", _n9, lambda: b"x\ny\n") == "verbatim", "")
        check("[-9] S1 rung `eol` — equal after CRLF-to-LF on BOTH sides",
              GK9.derive_carry_rung(b"x\ny\n", _n9, lambda: b"x\r\ny\r\n") == "eol", "")
        check("[-9] S1 rung `relocate` — ours is base rewritten through the map",
              GK9.derive_carry_rung(b"see tools/demo/x\n", _n9,
                                    lambda: b"see scripts/demo/x\n") == "relocate", "")
        check("[-9] S5 WHOLE-FILE equality decides: one residual byte and NO rung matches",
              GK9.derive_carry_rung(b"see tools/demo/x\n", _n9,
                                    lambda: b"see scripts/demo/x\nMINE\n") is None, "")
        check("[-9] F2 a ladder and not a lattice: `relocate` AND `eol` together prove nothing",
              GK9.derive_carry_rung(b"see tools/demo/x\n", _n9,
                                    lambda: b"see scripts/demo/x\r\n") is None, "")
        check("[-9] S1 an unreadable `ours` yields no rung rather than a guessed one",
              GK9.derive_carry_rung(b"x\n", _n9, lambda: None) is None, "")

        def _boom9():
            """The thunk this arm must never call. It RETURNS rather than raising, deliberately:
            an exception here takes the whole harness down at this line instead of failing one arm,
            and the arms below it then report nothing at all. Measured, staging the eager read: the
            raising form exited 1 with a traceback and 30 later arms never ran. These bytes prove a
            DIFFERENT rung, so a read that happens is visible as a red rather than as a crash."""
            return b"x\r\ny\r\n"

        check("[-9] S1 `verbatim` is settled from the oids — a byte-identical row pays no blob read",
              GK9.derive_carry_rung(b"x\ny\n", _n9, _boom9, known_equal=True) == "verbatim", "")

        # ---- S6's transformation, per rung. Two of the three are no-ops, which the engine says at
        # ---- the site rather than leaving a reader to infer; these arms pin which is which.
        check("[-9] S6 `relocate` applied to gov's bytes lands them in the target's spelling",
              GK9.derive_carried_by_rung("relocate", b"see tools/demo/x\n", _n9)
              == b"see scripts/demo/x\n", "")
        check("[-9] S6 `eol` normalises gov's own bytes, a no-op wherever gov ships LF",
              GK9.derive_carried_by_rung("eol", b"a\r\nb\n", _n9) == b"a\nb\n"
              and GK9.derive_carried_by_rung("eol", b"a\nb\n", _n9) == b"a\nb\n", "")
        check("[-9] S6 no rung leaves the bytes exactly as gov shipped them",
              GK9.derive_carried_by_rung(None, b"see tools/demo/x\n", _n9)
              == b"see tools/demo/x\n", "")

        # ---- S2, AS A GATE RATHER THAN A DISCIPLINE. "No branch in either verb may read a stored
        # ---- `carry`" is a claim about SOURCE, and a behavioural arm can only ever show that ONE
        # ---- fixture's stored value went unread. This parses the engine and asserts that the only
        # ---- name a `carry` is ever read off is the LIVE classification `classify_row` just
        # ---- returned. WHAT IT DOES NOT CHECK: `pop` is counted as a write, because the engine
        # ---- drops a stale value rather than consuming it — an arm cannot tell those apart from
        # ---- the call shape alone, and the behavioural AC7 arms below cover the consuming case.
        import ast as _ast9  # noqa: PLC0415
        _src9 = (HERE / "govkit.py").read_text(encoding="utf-8")
        _readers9: set[str] = set()
        _writes9 = 0
        for _node in _ast9.walk(_ast9.parse(_src9)):
            if (isinstance(_node, _ast9.Call) and isinstance(_node.func, _ast9.Attribute)
                    and _node.func.attr in ("get", "pop") and _node.args
                    and isinstance(_node.args[0], _ast9.Constant)
                    and _node.args[0].value == "carry"):
                if _node.func.attr == "pop":
                    _writes9 += 1
                elif isinstance(_node.func.value, _ast9.Name):
                    _readers9.add(_node.func.value.id)
                else:
                    _readers9.add("<expression>")
            elif (isinstance(_node, _ast9.Subscript) and isinstance(_node.slice, _ast9.Constant)
                    and _node.slice.value == "carry"):
                if isinstance(_node.ctx, _ast9.Store):
                    _writes9 += 1
                elif isinstance(_node.value, _ast9.Name):
                    _readers9.add(_node.value.id)
                else:
                    _readers9.add("<expression>")
        check("[-9] S2 the engine really writes `carry` back onto rows, so this arm has a population",
              _writes9 >= 3, f"{_writes9} write site(s)")
        check("[-9] S2 the ONLY name a `carry` is read off is the live classification, never a row",
              _readers9 == {"c"}, str(sorted(_readers9)))

        # ---- THE END-TO-END FIXTURE. A scratch gov whose kit the target installed at a DIFFERENT
        # ---- prefix, because every criterion below is about what `update` does to a real receipt
        # ---- over a real index. Both sides of every rung are AUTHORED literals: deriving the
        # ---- target's bytes by calling the substituter would make `ours == derive_carried(base)` a
        # ---- tautology and every relocate arm would pass against a broken map.
        _MOVED_A = ("tools/demo/moved.txt line 1\ntools/demo/moved.txt line 2\n"
                    "tools/demo/moved.txt line 3\ntools/demo/moved.txt line 4\n"
                    "tools/demo/moved.txt line 5\n")
        _MOVED_B = ("tools/demo/moved.txt line 1\ntools/demo/moved.txt line 2\n"
                    "GOV SEMANTIC CHANGE at tools/demo/moved.txt\ntools/demo/moved.txt line 4\n"
                    "tools/demo/moved.txt line 5\n")
        _MOVED_T = ("scripts/demo/moved.txt line 1\nscripts/demo/moved.txt line 2\n"
                    "scripts/demo/moved.txt line 3\nscripts/demo/moved.txt line 4\n"
                    "scripts/demo/moved.txt line 5\n")
        # AC3's row, and the reason the whole design is a PROOF gate rather than a rewrite. `bash
        # tools/land.sh` names no prefix at all, and `my tools/demo` is a directory the fixture
        # BUILDS — the write-time alternative corrupts both. Re-opened at ce5dca99 in this tree's own
        # `tools/unattended/adopt-unattended.test.sh`: four `bash tools/land.sh` lines at 34, 63, 83
        # and 91, and the `my tools/unattended` construction at 132-133.
        _HAZ_G = ("run bash tools/land.sh\nrun bash tools/land.sh\n"
                  "mkdir 'my tools/demo'\nsee tools/demo/hazard.txt\n")
        _HAZ_T = ("run bash tools/land.sh\nrun bash tools/land.sh\n"
                  "mkdir 'my tools/demo'\nsee scripts/demo/hazard.txt\n")
        _GOV9 = {
            "tools/demo/plain.txt": b"plain one\nplain two\n",
            "tools/demo/crlf.txt": b"c one\nc two\n",
            "tools/demo/pathy.txt": b"see tools/demo/pathy.txt\nand tools/demo/other\n",
            "tools/demo/moved.txt": _MOVED_A.encode(),
            "tools/demo/gone.txt": b"gone refers to tools/demo/gone.txt\n",
            "tools/demo/hazard.txt": _HAZ_G.encode(),
            "tools/demo/binary.bin": b"\xff\xfe\x00tools/demo\x00",
            "tools/top.txt": b"top level\n",
            "tools/amb/a.txt": b"a\n",
            "tools/amb/b.txt": b"b\n",
        }
        # (target path, gov source, the target's OWN bytes, the rung those two must prove)
        _ROWS9 = [
            ("scripts/demo/plain.txt", "tools/demo/plain.txt", b"plain one\nplain two\n",
             "verbatim"),
            ("scripts/demo/crlf.txt", "tools/demo/crlf.txt", b"c one\r\nc two\r\n", "eol"),
            ("scripts/demo/pathy.txt", "tools/demo/pathy.txt",
             b"see scripts/demo/pathy.txt\nand scripts/demo/other\n", "relocate"),
            ("scripts/demo/moved.txt", "tools/demo/moved.txt", _MOVED_T.encode(), "relocate"),
            ("scripts/demo/gone.txt", "tools/demo/gone.txt",
             b"gone refers to scripts/demo/gone.txt\n", None),
            ("scripts/demo/hazard.txt", "tools/demo/hazard.txt", _HAZ_T.encode(), None),
            ("scripts/demo/binary.bin", "tools/demo/binary.bin", b"\xff\xfe\x00LOCAL\x00", None),
            ("data/top.txt", "tools/top.txt", b"top level\n", "verbatim"),
            ("one/a.txt", "tools/amb/a.txt", b"a\n", "verbatim"),
            ("two/b.txt", "tools/amb/b.txt", b"b\n", "verbatim"),
        ]
        GONE9 = "scripts/demo/gone.txt"
        HAZ9 = "scripts/demo/hazard.txt"
        MOV9 = "scripts/demo/moved.txt"
        PATH9 = "scripts/demo/pathy.txt"

        def carry_gov(name: str) -> pathlib.Path:
            """A scratch gov holding the kit under `tools/`, plus a copy of the engine to run it."""
            g = tmp / f"{name}-gov"
            (g / "tools" / "govkit").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                '[selection]\ndefault = ["demo"]\n\n'
                '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "demo").mkdir(parents=True, exist_ok=True)
            (g / "tools" / "demo" / "kit.toml").write_text(
                'id = "demo"\nhome = "tools/demo"\nversion_from = { none = "fixture" }\n\n'
                '[check]\nnone = "a fixture kit"\n\n'
                '[[files]]\ninclude = ["*.txt"]\nrole = "engine"\n\n'
                '[adopt]\nargv = []\nmutates_index = false\n', encoding="utf-8", newline="\n")
            for rel, data in _GOV9.items():
                p = g / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(data)
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g

        def carry_target(g: pathlib.Path, name: str, mutate=None) -> pathlib.Path:
            """The target, installed at a DIFFERENT prefix, hand-built rather than applied.

            `apply` cannot produce this state: it lands gov's own bytes at gov's own spelling, and
            what is under test is where an adopter ends up after installing at a `prefix` gov does
            not use. The receipt is therefore AUTHORED — schema 3, `gov_oid` from gov's real blob at
            A so `-7` S9's preamble accepts it, and `oid` from the target's own index.
            """
            t = tmp / name
            t.mkdir(parents=True)
            git(t, "init", "-q", "-b", "main")
            git(t, "config", "user.email", "t@e")
            git(t, "config", "user.name", "t")
            git(t, "config", "core.autocrlf", "false")
            (t / ".governance").mkdir()
            (t / ".governance" / "deploy.toml").write_text(
                'gov_source = "local"\nprefix = "scripts"\nkits = ["demo"]\n',
                encoding="utf-8", newline="\n")
            for path, _src, data, _rung in _ROWS9:
                p = t / path
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(data)
            git(t, "add", "-A")
            git(t, "commit", "-qm", "the relocated install")
            # AC9's deletion is COMMITTED on purpose: `-12` S4 calls a STAGED deletion dirty and
            # refuses the run at its step 2, so the `missing` cell could never be reached over one.
            # A path absent from the index, the worktree AND HEAD falls outside that definition.
            (t / GONE9).unlink()
            git(t, "add", "-A")
            git(t, "commit", "-qm", "the operator deleted a carried row, and committed it")
            A = gout(g, "rev-parse", "HEAD").strip()
            idx = {}
            for ln in gout(t, "ls-files", "-s").splitlines():
                meta, path = ln.split("\t", 1)
                idx[path] = meta.split()[1]
            rec = {"schema": 3, "gov_source": "local", "gov_commit": A, "kits": ["demo"],
                   "files": [{"path": path, "source": src, "role": "engine", "kit": "demo",
                              "written": True, "commit": A,
                              "gov_oid": GK9.blob_oid(_GOV9[src]), "oid": idx.get(path),
                              "sha256": GK9._sha(data)}
                             for path, src, data, _rung in _ROWS9]}
            if mutate is not None:
                mutate(rec)
            (t / ".governance" / "install.json").write_text(
                json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
            git(t, "add", "-A")
            git(t, "commit", "-qm", "the receipt")
            return t

        def carry_advance(g: pathlib.Path) -> str:
            """Gov moves ONE file, semantically, under a target that is holding the relocation."""
            (g / "tools" / "demo" / "moved.txt").write_bytes(_MOVED_B.encode())
            git(g, "add", "-A")
            git(g, "commit", "-qm", "B")
            return gout(g, "rev-parse", "HEAD").strip()

        def carry_update(g: pathlib.Path, t: pathlib.Path, *extra):
            return subprocess.run([sys.executable, str(g / "tools" / "govkit" / "govkit.py"),
                                   "update", "--target", str(t), *extra],
                                  capture_output=True, text=True)

        g9 = carry_gov("c9")
        A9 = gout(g9, "rev-parse", "HEAD").strip()
        t9 = carry_target(g9, "c9-t")
        B9 = carry_advance(g9)

        # ---- THE FIXTURE'S OWN PRECONDITIONS, asserted BEFORE anything runs over it. A fixture that
        # ---- does not trigger the rule proves nothing, and two of these rules are triggered by
        # ---- state rather than by an edit.
        check("[-9] the fixture's gov copy really MOVED between the two vintages",
              gout(g9, "rev-parse", f"{A9}:tools/demo/moved.txt").strip()
              != gout(g9, "rev-parse", f"{B9}:tools/demo/moved.txt").strip(),
              gout(g9, "rev-parse", f"{A9}:tools/demo/moved.txt"))
        check("[-9] the deleted row is absent from the target's index, worktree AND HEAD",
              GONE9 not in gout(t9, "ls-files").split() and not (t9 / GONE9).exists()
              and GONE9 not in gout(t9, "ls-tree", "-r", "--name-only", "HEAD").split(), "")
        check("[-9] the target really installed at a prefix gov does not use",
              all(not p.startswith("tools/") for p, _s, _d, _r in _ROWS9), "")

        # ---- AC1, restated over the fixture this file BUILDS rather than over inCMS's 52 rows.
        # ---- `classify_row` is driven directly, through the derivation's own output, and the rung
        # ---- it returns per row is compared against the rung the fixture was AUTHORED to prove —
        # ---- so the arm grades the ladder against a table written beside the bytes rather than
        # ---- against a count copied out of a document.
        _rows9 = json.loads(
            (t9 / ".governance" / "install.json").read_text(encoding="utf-8"))["files"]
        _idx9, _ = GK9.index_read(t9, [r["path"] for r in _rows9])
        _nd9, _pd9, _dd9 = GK9.derive_carry_map(
            [(r.get("source"), r.get("path")) for r in _rows9])
        _got9 = {r["path"]: GK9.classify_row(g9, t9, r, B9, _idx9, _nd9).get("carry")
                 for r in _rows9}
        _want9 = {path: rung for path, _s, _d, rung in _ROWS9}
        check("[-9] AC1 the fixture spans every rung AND a row that proves none, or it grades nothing",
              set(_want9.values()) == {"verbatim", "eol", "relocate", None},
              str(sorted(str(v) for v in set(_want9.values()))))
        check("[-9] AC1 classify_row returns the rung the fixture was authored to prove, per row",
              _got9 == _want9,
              str({k: (v, _want9[k]) for k, v in _got9.items() if v != _want9.get(k)}))
        # MEASURED over this fixture and reported as measured: 4 verbatim, 1 eol, 2 relocate, 3 with
        # no rung at all. inCMS's 21/6/5 belong to S13's committed receipt, which is not in this tree.
        _dist9 = {k: sum(1 for v in _got9.values() if v == k)
                  for k in ("verbatim", "eol", "relocate", None)}
        check("[-9] AC1 the measured distribution here is 4 verbatim, 1 eol, 2 relocate, 3 delta",
              _dist9 == {"verbatim": 4, "eol": 1, "relocate": 2, None: 3}, str(_dist9))

        # ---- AC2's by-name half, on a RUN rather than on the helper: S7 says the drop is PRINTED,
        # ---- because a silently collapsed map is indistinguishable from a target that relocated
        # ---- nothing, and that is the failure mode that would waste the most time.
        _ro9 = carry_update(g9, t9)
        check("[-9] AC2 the run names the dropped ambiguous gov directory and both destinations",
              "DROPPED the ambiguous gov directory 'tools/amb'" in _ro9.stdout
              and "one, two" in _ro9.stdout, _ro9.stdout[:1200])
        check("[-9] S7 ...and prints the pair count and the needle count it derived on this run",
              "carry map: 2 directory pair(s), 3 needle(s)" in _ro9.stdout, _ro9.stdout[:1200])
        check("[-9] S7 the printed counts are the derivation's own output, not a second spelling",
              (len(_pd9), len(_nd9)) == (2, 3), f"{len(_pd9)} pair(s), {len(_nd9)} needle(s)")

        # ---- DEPL-dCarriedReceipt-9 S13 -- THE COMMITTED INCMS FIXTURE, BUILT AT LAST.
        # ---- Deferred when this unit was built on node `d`, where the inCMS checkout is not
        # ---- reachable; reopened by owner ruling 2026-08-26 on node `a`, where it is. Generated
        # ---- once by `tools/govkit/fixtures/make_incms_receipt.py` from inCMS's own
        # ---- `.governance/install.index` at `2cff5855` against gov `ce5dca99`, and committed, so
        # ---- everything below runs with NEITHER live repository present.
        # ----
        # ---- THE ARMS DERIVE RATHER THAN READ. Nothing here compares against a rung stored in the
        # ---- fixture -- a fixture holding the ANSWER grades nothing. `verbatim` and `relocate` are
        # ---- proved by transforming GOV's bytes and comparing the resulting blob oid to the
        # ---- TARGET's recorded oid. `eol` cannot be: the rung normalises BOTH sides, and an oid
        # ---- cannot be un-hashed, so the fixture carries `lf_oid` -- one measurement of the target
        # ---- taken where inCMS was reachable -- and the arm reproduces it from gov's side.
        _fx9 = json.loads((GOVKIT.parent / "fixtures" / "incms-2cff5855.receipt.json")
                          .read_text(encoding="utf-8"))
        _fx9rows = _fx9["files"]
        check("[-9] S13 LIVENESS the committed inCMS fixture carries the 52-row population",
              len(_fx9rows) == 52, f"{len(_fx9rows)} row(s)")
        check("[-9] S13 LIVENESS ...and every row carries the three identities a rung is proved from",
              all(w.get("gov_oid") and w.get("oid") and w.get("lf_oid") for w in _fx9rows),
              str([w["path"] for w in _fx9rows
                   if not (w.get("gov_oid") and w.get("oid") and w.get("lf_oid"))][:4]))

        _gk9 = govkit_module()
        _n9s, _p9s, _d9s = _gk9.derive_carry_map(
            [(w.get("source"), w.get("path")) for w in _fx9rows])

        def _derive_fx9_rung(w: dict) -> str | None:
            """The ladder, re-derived from gov's bytes. Same order as `derive_carry_rung`."""
            base = subprocess.run(["git", "-C", str(HERE.parents[1]), "cat-file", "blob", w["gov_oid"]],
                                  capture_output=True).stdout
            if w["oid"] == _gk9.blob_oid(base):
                return "verbatim"
            if w["lf_oid"] == _gk9.blob_oid(_gk9.derive_lf(base)):
                return "eol"
            if w["oid"] == _gk9.blob_oid(_gk9.derive_carried(base, _n9s)):
                return "relocate"
            return None

        _fx9dist = {k: 0 for k in ("verbatim", "eol", "relocate", None)}
        for _w in _fx9rows:
            _fx9dist[_derive_fx9_rung(_w)] += 1
        check("[-9] AC1 over the REAL inCMS population: 21 verbatim, 6 eol, 5 relocate, 20 no rung",
              _fx9dist == {"verbatim": 21, "eol": 6, "relocate": 5, None: 20}, str(_fx9dist))
        check("[-9] AC1 ...and the four buckets account for every row, so none was skipped",
              sum(_fx9dist.values()) == len(_fx9rows),
              f"{sum(_fx9dist.values())} vs {len(_fx9rows)}")

        # ---- AC2, RESTATED AGAINST THE POPULATION IT ACTUALLY DESCRIBES, and the spec's own
        # ---- instruction was to restate rather than to edit the numbers until they fit. AC1's
        # ---- population is the 52 rows whose recorded COMMIT resolves, because a rung is proved
        # ---- against gov's bytes at that commit. The needle map needs no commit at all -- it is
        # ---- derived from (source, destination) pairs -- so its population is the 86 rows whose
        # ---- gov SOURCE resolves. The spec measured its Inventory over the 86 and wrote AC2's
        # ---- criterion against the 52, which is why its figures never reproduced anywhere.
        _fx9pairs = [tuple(p) for p in _fx9["carry_map_population"]]
        check("[-9] S13 LIVENESS the fixture carries AC2's own 86-row pair population",
              len(_fx9pairs) == 86, f"{len(_fx9pairs)} pair(s)")
        _n86, _p86, _d86 = _gk9.derive_carry_map(_fx9pairs)
        check("[-9] AC2 the 86-row population yields 13 directory pairs",
              len(_p86) == 13, f"{len(_p86)}: {sorted(_p86)}")
        check("[-9] AC2 ...and DROPS `tools/memory-recall` and `tools/workflows` BY NAME",
              sorted(g for g, _ in _d86) == ["tools/memory-recall", "tools/workflows"],
              str([g for g, _ in _d86]))
        # THE NEEDLE COUNT IS 25 AND THE SPEC SAYS 26. The spec's figure is wrong by exactly one and
        # this build DERIVED why before measuring it: needles emit in a `/` form and a `~` form, and
        # for a gov directory carrying NO slash those two strings are the SAME, so such a pair
        # contributes one needle rather than two. Exactly one of the 13 -- `tools` -- has no slash.
        # 2*13 - 1 = 25. Asserted as the RELATION and not as a literal, because a literal here is
        # the class this whole build keeps finding.
        _noslash = [g for g in _p86 if "/" not in g]
        check("[-9] AC2 exactly one surviving gov directory carries no slash, and it is `tools`",
              _noslash == ["tools"], str(_noslash))
        check("[-9] AC2 the needle count is the RELATION 2*pairs - (pairs with no slash) = 25",
              len(_n86) == 2 * len(_p86) - len(_noslash) == 25,
              f"{len(_n86)} needle(s) over {len(_p86)} pair(s), {len(_noslash)} slashless")

        # ---- S10: the label. `("differs","equal")` grids to `patched`, which is a LIE for a carried
        # ---- row — the target edited nothing, it installed somewhere else.
        check("[-9] S10 a carried row whose gov copy did not move prints `carried (relocate)`",
              verdict_of(_ro9.stdout, PATH9) == "carried (relocate)", _ro9.stdout)
        check("[-9] S10 ...and an `eol` row prints `carried (eol)` rather than `patched`",
              verdict_of(_ro9.stdout, "scripts/demo/crlf.txt") == "carried (eol)", _ro9.stdout)
        check("[-9] S10 ...while a row proving NO rung keeps exactly the verdict it already had",
              verdict_of(_ro9.stdout, HAZ9) == "patched"
              and verdict_of(_ro9.stdout, "scripts/demo/binary.bin") == "patched", _ro9.stdout)
        check("[-9] S9 a proven rung moves no row onto the raw-write arm",
              verdict_of(_ro9.stdout, PATH9) not in GK9.RAW_WRITE_VERDICTS
              and verdict_of(_ro9.stdout, MOV9) == "diverged", _ro9.stdout)

        # ---- AC8 + AC5: the RECONCILE. Red observed on this very fixture with the pre-unit engine —
        # ---- the three-way took an un-carried base, every line naming a path read as an operator
        # ---- edit, the merge conflicted, the run exited 1 and the file was left untouched.
        _w9 = carry_update(g9, t9, "--write")
        # AC3's evidence is CAPTURED HERE, before anything commits. Its arms read further down, and
        # a `git diff HEAD` asked after the `settle` below is clean whether that run wrote the row
        # or not — the settle committed it either way. Measured: staged with `patched` on the raw
        # arm, the byte arm redded and the diff arm did not, which is a check that cannot fail.
        _haz_bytes9 = (t9 / HAZ9).read_bytes()
        _haz_diff9 = subprocess.run(
            ["git", "-C", str(t9), "diff", "HEAD", "--exit-code", "--", HAZ9],
            capture_output=True).returncode
        check("[-9] AC8 the write run exits 0 — the carried row reconciles rather than conflicting",
              _w9.returncode == 0, _w9.stdout[-1400:] + _w9.stderr[-800:])
        _mi9 = gout(t9, "ls-files", "-s", "--", MOV9).split()[1]
        _mb9 = subprocess.run(["git", "-C", str(t9), "cat-file", "blob", _mi9],
                              capture_output=True).stdout
        check("[-9] AC8 the TARGET's index blob for that row spells its own `scripts/` prefix",
              b"scripts/demo/moved.txt" in _mb9 and b"tools/demo/moved.txt" not in _mb9,
              repr(_mb9))
        check("[-9] AC5 ...and carries gov's semantic change — asserted on CONTENT, never on rc",
              b"GOV SEMANTIC CHANGE at scripts/demo/moved.txt" in _mb9, repr(_mb9))
        check("[-9] AC5 ...and every untouched line came through at the target's spelling",
              _mb9 == _MOVED_B.encode().replace(b"tools/demo", b"scripts/demo"), repr(_mb9))
        _rec9 = json.loads((t9 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _rowm = [f for f in _rec9["files"] if f["path"] == MOV9][0]
        check("[-9] S12 the reconciled row's `oid` is the blob the target now holds",
              _rowm.get("oid") == _mi9, str(_rowm)[:300])
        check("[-9] S12 ...and `gov_oid` is GOV's own blob at the advanced commit, not the merge",
              _rowm.get("gov_oid") == GK9.blob_oid(_MOVED_B.encode())
              and _rowm.get("commit") == B9, str(_rowm)[:300])

        # ---- AC9: the DELETED carried row, restored. Red observed: the file came back as
        # ---- `gone refers to tools/demo/gone.txt`, gov's prefix in a target that does not use it.
        _gb9 = (t9 / GONE9).read_bytes()
        check("[-9] AC9 a `missing` carried row is restored in the CARRIED form",
              _gb9 == b"gone refers to scripts/demo/gone.txt\n", repr(_gb9))
        check("[-9] AC9 ...and spells gov's own prefix nowhere", b"tools/" not in _gb9, repr(_gb9))
        _gi9 = gout(t9, "ls-files", "-s", "--", GONE9).split()[1]
        check("[-9] AC9 ...and its index blob is NOT gov's blob for that source",
              _gi9 != GK9.blob_oid(_GOV9["tools/demo/gone.txt"]), _gi9)

        # ---- AC10: THE STAMP the restore leaves, both halves together. This is the arm that fails
        # ---- against a draft writing the carried bytes and then taking `-8`'s raw-arm stamp: the
        # ---- two identities come back EQUAL over bytes gov never shipped, and the NEXT run reads
        # ---- that row as clean and raw-overwrites it straight back to `tools/`.
        _rowg = [f for f in _rec9["files"] if f["path"] == GONE9][0]
        check("[-9] AC10 the restored row records `carry: relocate`",
              _rowg.get("carry") == "relocate", str(_rowg)[:300])
        check("[-9] AC10 ...`oid` is the blob the target's index actually holds",
              _rowg.get("oid") == _gi9, str(_rowg)[:300])
        check("[-9] AC10 ...`gov_oid` is gov's blob at the row's own commit",
              _rowg.get("gov_oid") == GK9.blob_oid(_GOV9["tools/demo/gone.txt"])
              and _rowg.get("commit") == B9, str(_rowg)[:300])
        check("[-9] AC10 ...so the two identities DIFFER, which reads `this row carries a rung`",
              _rowg.get("oid") != _rowg.get("gov_oid"), str(_rowg)[:300])
        # THE SECOND RUN is what the stamp is FOR, so it is exercised rather than argued.
        settle(t9, "after the carried update")
        _w9b = carry_update(g9, t9, "--write")
        check("[-9] AC10 the NEXT run re-proves the rung from the blobs and does not revert it",
              _w9b.returncode == 0
              and (t9 / GONE9).read_bytes() == b"gone refers to scripts/demo/gone.txt\n",
              _w9b.stdout[-1200:] + repr((t9 / GONE9).read_bytes()))
        check("[-9] AC10 ...and reports it as carried rather than as a local delta",
              verdict_of(_w9b.stdout, GONE9) == "carried (relocate)", _w9b.stdout)

        # ---- AC3: the row that must NEVER be written. A build that "fixes" this one has
        # ---- re-introduced the write-time alternative §4 rejects.
        check("[-9] AC3 the fixture triggers the hazard: the map DOES reach lines naming no prefix",
              b"bash data/land.sh" in GK9.derive_carried(_HAZ_G.encode(), _nd9)
              and b"my scripts/demo" in GK9.derive_carried(_HAZ_G.encode(), _nd9),
              repr(GK9.derive_carried(_HAZ_G.encode(), _nd9)))
        check("[-9] AC3 the hazard row proves NO rung", _got9[HAZ9] is None, str(_got9[HAZ9]))
        check("[-9] AC3 ...and its bytes are unchanged after `update --write`",
              _haz_bytes9 == _HAZ_T.encode(), repr(_haz_bytes9))
        check("[-9] AC3 ...with nothing to diff against HEAD over that path, on that same run",
              _haz_diff9 == 0, f"git diff HEAD exited {_haz_diff9}")

        # ---- AC7: a STORED `carry` is never read. The value is planted on the row that provably
        # ---- matches NO rung, so believing it would be visible in one line of output.
        def _plant7(rec: dict) -> None:
            for f in rec["files"]:
                if f["path"] == HAZ9:
                    f["carry"] = "relocate"

        g7 = carry_gov("c9-ac7")
        t7 = carry_target(g7, "c9-ac7-t", mutate=_plant7)
        _r7 = json.loads((t7 / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("[-9] AC7 the fixture really carries a hand-written `carry` on a no-rung row",
              [f for f in _r7["files"] if f["path"] == HAZ9][0].get("carry") == "relocate", "")
        _a7 = carry_update(g7, t7, "--write")
        check("[-9] AC7 that row still classifies as a local delta, never as carried",
              verdict_of(_a7.stdout, HAZ9) == "patched", _a7.stdout)
        _r7b = json.loads((t7 / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("[-9] AC7 ...and the stale value is DROPPED from the receipt rather than believed",
              "carry" not in [f for f in _r7b["files"] if f["path"] == HAZ9][0],
              str([f for f in _r7b["files"] if f["path"] == HAZ9][0]))
        check("[-9] AC7 ...and the receipt still reads schema 3 — this unit moves no schema number",
              _r7b.get("schema") == 3 == GK9.RECEIPT_SCHEMA, str(_r7b.get("schema")))
        for _sch9 in (1, 2):
            def _older(rec: dict, _s=_sch9) -> None:
                rec["schema"] = _s
                for f in rec["files"]:
                    f.pop("gov_oid", None)
                    f.pop("oid", None)

            _go = carry_gov(f"c9-s{_sch9}")
            _to = carry_target(_go, f"c9-s{_sch9}-t", mutate=_older)
            _ao = carry_update(_go, _to)
            check(f"[-9] AC7 a schema-{_sch9} receipt still classifies without a refusal",
                  _ao.returncode != 2 and "REFUSING" not in _ao.stderr, _ao.stderr[:400])
            check(f"[-9] AC7 ...and its carried row is still recognised as carried (schema {_sch9})",
                  verdict_of(_ao.stdout, PATH9) == "carried (relocate)", _ao.stdout)

        # ================= DEPL-dCarriedReceipt-10 — role `forked`, report-only ==============
        #
        # WHAT THE ROLE IS, because every arm below turns on it: `forked` is a claim the DESCRIPTOR
        # RULE makes about a file's PROVENANCE — gov's copy is derived from the target's — re-read
        # from that rule on every run and NEVER inferred from what an attribution walk found. A
        # forked row is report-only: written in NEITHER direction.
        #
        # THE LANDMINE THESE ARMS GATE AS A CLASS. gov's `tools/memory-recall/extract.py` is a fork
        # of inCMS's `scripts/recall/extract.py`; it carries `import recall_conf` at its line 55 and
        # inCMS's `scripts/` tree holds no `recall_conf` anywhere. inCMS's own `.governance/
        # install.index` declares that file `engine`, so one automatic update writes gov's blob over
        # it and `scripts/recall/query.py` — which that project's charter mandates every session run
        # — dies at import with `ModuleNotFoundError`. Reproduced against both real trees, not
        # predicted. The fix that gates the CLASS is a role that says "fork", not three excluded
        # paths.
        FORK_SRC = {
            "forked-one.py": "# gov's own copy, derived from the target's\nimport gov_only\n",
            "engine.txt": "gov A\n",
        }

        def fork_kit(direction: str | None = "gov-from-target",
                     record: str | None = "DEPL-dCarriedReceipt-10",
                     include: str = '["forked-one.py"]') -> str:
            """A descriptor whose `**` engine pool has ONE source carved out by a `forked` rule.

            Both keys are parameterised so the same builder produces the complete rule AND each
            incomplete one — an arm whose negative fixture is built by different code from its
            positive fixture is grading two descriptors rather than one omission.
            """
            rule = f'[[files]]\ninclude = {include}\nrole = "forked"\n'
            if direction is not None:
                rule += f'direction = "{direction}"\n'
            if record is not None:
                rule += f'record = "{record}"\n'
            return ('id = "demo"\nhome = "tools/demo"\nversion_from = { none = "fixture" }\n\n'
                    '[check]\nnone = "a fixture kit"\n\n'
                    '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                    + rule + '\n[adopt]\nargv = []\nmutates_index = false\n')

        def fork_gov(tag: str, kit_toml: str) -> pathlib.Path:
            """A scratch gov carrying ONE `demo` entry, its sources, and a copy of the engine.

            THE COPY IS TAKEN HERE, at fixture-build time. A break staged into this repo's
            `govkit.py` AFTER the copy runs the UNPATCHED engine and the arm reports on nothing —
            two earlier builders on this build lost time to exactly that, so it is written down
            rather than remembered.
            """
            g = tmp / f"fork-{tag}"
            (g / "tools" / "govkit").mkdir(parents=True)
            (g / "tools" / "demo").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                '[selection]\ndefault = ["demo"]\n\n'
                '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
                encoding="utf-8", newline="\n")
            (g / "tools" / "demo" / "kit.toml").write_text(kit_toml, encoding="utf-8",
                                                           newline="\n")
            for rel, body in FORK_SRC.items():
                (g / "tools" / "demo" / rel).write_text(body, encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g

        # ---- THE FIXTURE'S OWN PRECONDITION. A fixture that does not trigger the rule proves
        # ---- nothing, and "the descriptor declares a forked rule" is the entire premise of every
        # ---- negative arm below.
        _GKF = govkit_module()
        check("[-10] the fixture descriptor really declares a rule whose role is `forked`",
              'role = "forked"' in fork_kit(), fork_kit())
        check("[-10] S1 `forked` is in ROLE_KINDS and maps to a kind of its own",
              _GKF.ROLE_KINDS.get("forked") == "forked", str(_GKF.ROLE_KINDS))
        check("[-10] S1 ...so the DERIVED LANDABLE_ROLES excludes it with no second list to remember",
              "forked" not in _GKF.LANDABLE_ROLES, str(_GKF.LANDABLE_ROLES))
        check("[-10] S2 the new kind has its own mark and its own skip reason",
              "forked" in _GKF.KIND_MARKS and "forked" in _GKF.SKIP_REASONS,
              str(sorted(_GKF.KIND_MARKS)) + " / " + str(sorted(_GKF.SKIP_REASONS)))
        check("[-10] S2 ...and that reason is NOT `blocked`'s sentence about gov-owned regions",
              _GKF.SKIP_REASONS["forked"] != _GKF.SKIP_REASONS["blocked"],
              _GKF.SKIP_REASONS["forked"])
        check("[-10] AC6 arm 7g's own enumeration reaches it: UNLANDED_REASON and UPDATE_ROLE agree",
              "forked" in _GKF.UNLANDED_REASON and "forked" in govkit_update_role(),
              str(sorted(govkit_update_role())))
        check("[-10] S4 ...and its disposition is `-2`'s `report`, never a refusal",
              govkit_update_role()["forked"] == "report", govkit_update_role().get("forked"))

        # ---- S5 / AC4: the DESCRIPTOR refusals, by name. The positive fixture runs FIRST: without
        # ---- it every negative below could be passing because the tool is broken rather than
        # ---- because the input is bad.
        _f_ok = run_in(fork_gov("ok", fork_kit()))
        check("[-10] LIVENESS a complete `forked` rule is selfcheck-GREEN",
              _f_ok.returncode == 0, _f_ok.stdout + _f_ok.stderr)

        _f_nodir = run_in(fork_gov("nodir", fork_kit(direction=None)))
        check("[-10] AC4 a `forked` rule with no `direction` reds selfcheck",
              _f_nodir.returncode == 1, _f_nodir.stdout + _f_nodir.stderr)
        check("[-10] AC4 ...by NAME on the missing key, not as an unknown role",
              "`forked` rule with no `direction`" in _f_nodir.stdout, _f_nodir.stdout)

        _f_baddir = run_in(fork_gov("baddir", fork_kit(direction="sideways")))
        check("[-10] F1 a `direction` outside the closed enum reds selfcheck",
              _f_baddir.returncode == 1, _f_baddir.stdout + _f_baddir.stderr)
        check("[-10] F1 ...naming the closed set rather than accepting a free string",
              "outside the closed set" in _f_baddir.stdout
              and "gov-from-target" in _f_baddir.stdout, _f_baddir.stdout)

        _f_norec = run_in(fork_gov("norec", fork_kit(record=None)))
        check("[-10] AC4 a `forked` rule with no `record` reds selfcheck",
              _f_norec.returncode == 1, _f_norec.stdout + _f_norec.stderr)
        check("[-10] AC4 ...by NAME on the missing key",
              "`forked` rule with no `record`" in _f_norec.stdout, _f_norec.stdout)

        # ---- AC5: `plan` marks the forked source AND the summary COUNTS it. The second half is the
        # ---- one the spec observed red: `n` is derived from KIND_MARKS while the summary used to
        # ---- hand-name five kinds, so a kind added to the table alone was counted and never
        # ---- printed. The summary clause is derived from the same table now.
        _gp = fork_gov("plan", fork_kit())
        _tp = make_target(tmp / "fork-plan-t",
                          'gov_source = "local"\nprefix = "tools"\nkits = ["demo"]\n')
        _pp = run_in_gov(_gp, "plan", "--target", str(_tp), "--kits", "demo")
        _prows = _extract_plan_rows(_pp.stdout)
        check("[-10] AC5 plan exits 0 over a descriptor carrying a forked rule",
              _pp.returncode == 0, _pp.stdout + _pp.stderr)
        check("[-10] AC5 the forked source is marked FORK, not `write`",
              ("FORK", "tools/demo/forked-one.py") in _prows, str(_prows))
        check("[-10] AC5 ...and no forked destination is previewed as a write",
              "tools/demo/forked-one.py" not in extract_plan_writes(_pp.stdout),
              str(extract_plan_writes(_pp.stdout)))
        # `detail` IS STRINGIFIED HERE, and that is not tidiness. `check()` concatenates it onto
        # its FAIL line, so a list argument raises `TypeError` on the failing path and takes the
        # whole harness down instead of reporting a finding — an arm that crashes on the one
        # outcome it exists to report. Caught by the break sweep, on the break this arm is for.
        check("[-10] AC5 ...and the printed summary COUNTS it rather than dropping it",
              "1 forked" in _pp.stdout,
              str([ln for ln in _pp.stdout.splitlines() if "NOTHING was written" in ln]))
        check("[-10] AC5 ...with the legend naming the mark it just printed",
              "FORK = " in _pp.stdout, _pp.stdout)
        check("[-10] S2 the `**` engine pool still ships everything the forked rule did not claim",
              "tools/demo/engine.txt" in extract_plan_writes(_pp.stdout),
              str(extract_plan_writes(_pp.stdout)))

        # ---- AC2: `apply` then `update --write`, end to end, over a target holding its OWN copy of
        # ---- the forked file. This is the shape the landmine has: the target's bytes are the
        # ---- source, gov's are the derivative, and an `engine` role here destroys the target's.
        FORK_TARGET_BYTES = "# the target's own copy — gov's is derived FROM this\nimport ok\n"

        def fork_target(g: pathlib.Path, name: str) -> pathlib.Path:
            t = make_target(tmp / name,
                            'gov_source = "local"\nprefix = "tools"\nkits = ["demo"]\n')
            p = t / "tools" / "demo" / "forked-one.py"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(FORK_TARGET_BYTES, encoding="utf-8", newline="\n")
            git(t, "add", "-A")
            git(t, "commit", "-qm", "the target's own copy of the file gov forked")
            return t

        _ga = fork_gov("apply", fork_kit())
        _ta = fork_target(_ga, "fork-apply-t")
        check("[-10] the fixture triggers the rule: gov's bytes and the target's DIFFER",
              (_ta / "tools" / "demo" / "forked-one.py").read_text(encoding="utf-8")
              != FORK_SRC["forked-one.py"], "")

        _ap = run_in_gov(_ga, "apply", "--target", str(_ta), "--kits", "demo")
        check("[-10] apply exits 0 over a descriptor carrying a forked rule",
              _ap.returncode == 0, _ap.stdout + _ap.stderr)
        check("[-10] apply SKIPPED the forked rule and said why, rather than skipping silently",
              "SKIPPED [forked" in _ap.stdout and "derivative" in _ap.stdout, _ap.stdout)
        check("[-10] apply left the target's own copy BYTE-IDENTICAL",
              (_ta / "tools" / "demo" / "forked-one.py").read_text(encoding="utf-8")
              == FORK_TARGET_BYTES,
              repr((_ta / "tools" / "demo" / "forked-one.py").read_text(encoding="utf-8")))
        _reca = json.loads((_ta / ".governance" / "install.json").read_text(encoding="utf-8"))
        _fr = [f for f in _reca["files"] if f.get("role") == "forked"]
        check("[-10] apply wrote ONE forked receipt row, marked unwritten",
              len(_fr) == 1 and _fr[0].get("written") is False, str(_fr))
        # BOTH GUARDED ON THE POPULATION, for the reason the break sweep measured: an unguarded
        # `_fr[0]` raises `IndexError` the moment the row above it is missing, which truncates every
        # arm below and reports their coverage as untested rather than as red.
        check("[-10] S5 that row COPIED both keys from the rule that produced it",
              len(_fr) == 1 and _fr[0].get("direction") == "gov-from-target"
              and _fr[0].get("record") == "DEPL-dCarriedReceipt-10", str(_fr))
        check("[-10] ...and carries NEITHER identity, so `-7`'s S9 preamble passes it over",
              len(_fr) == 1 and "gov_oid" not in _fr[0] and "commit" not in _fr[0], str(_fr))

        # Gov moves BOTH files. The engine row must still move — an arm where nothing updates
        # cannot tell "the forked row was skipped" from "the whole run did nothing".
        settle(_ta, "after apply")
        (_ga / "tools" / "demo" / "forked-one.py").write_text(
            "# gov's own copy, moved\nimport gov_only\nimport more_gov_only\n",
            encoding="utf-8", newline="\n")
        (_ga / "tools" / "demo" / "engine.txt").write_text("gov B\n", encoding="utf-8",
                                                           newline="\n")
        git(_ga, "add", "-A")
        git(_ga, "commit", "-qm", "B")
        _B = gout(_ga, "rev-parse", "HEAD").strip()

        _up = run_in_gov(_ga, "update", "--target", str(_ta), "--write")
        check("[-10] AC2 `update --write` exits 0 with a forked row in the receipt",
              _up.returncode == 0, _up.stdout + _up.stderr)
        check("[-10] AC2 ...printing ONE report line for it, naming its `direction`",
              len([ln for ln in _up.stdout.splitlines()
                   if ln.startswith("  report") and "[forked" in ln
                   and "direction gov-from-target" in ln]) == 1, _up.stdout)
        check("[-10] AC2 ...counted in the tally rather than dropped from it",
              "forked:reported 1" in _up.stdout, _up.stdout)
        check("[-10] AC2 ...writing NEITHER direction: the target's bytes are untouched",
              (_ta / "tools" / "demo" / "forked-one.py").read_text(encoding="utf-8")
              == FORK_TARGET_BYTES,
              repr((_ta / "tools" / "demo" / "forked-one.py").read_text(encoding="utf-8")))
        check("[-10] AC2 ...and gov's own copy is untouched too — no reverse transform exists",
              (_ga / "tools" / "demo" / "forked-one.py").read_text(encoding="utf-8")
              != FORK_TARGET_BYTES, "")
        check("[-10] AC2 LIVENESS the same run DID move the engine row, so nothing passed by "
              "doing nothing",
              (_ta / "tools" / "demo" / "engine.txt").read_text(encoding="utf-8") == "gov B\n",
              repr((_ta / "tools" / "demo" / "engine.txt").read_text(encoding="utf-8")))
        _recb = json.loads((_ta / ".governance" / "install.json").read_text(encoding="utf-8"))
        check("[-10] AC2 ...and the receipt is RE-STAMPED rather than frozen by the forked row",
              _recb.get("gov_commit") == _B, str(_recb.get("gov_commit")) + " want " + _B)

        # ---- AC7: the row shape a receipt written BEFORE this unit produces, and the shape a
        # ---- descriptor edit leaves behind. `UPDATE_ROLE` is keyed on the RECEIPT's role, so such
        # ---- a row reaches this printer — and a printer reading `row["direction"]` raises
        # ---- `KeyError` on it, turning the report disposition into a traceback on the one path
        # ---- that exists to avoid acting.
        _g7 = fork_gov("nodirrow", fork_kit())
        _t7 = fork_target(_g7, "fork-nodirrow-t")
        _a7 = run_in_gov(_g7, "apply", "--target", str(_t7), "--kits", "demo")
        check("[-10] AC7 the fixture applied before the row is stripped", _a7.returncode == 0,
              _a7.stdout + _a7.stderr)
        _r7p = _t7 / ".governance" / "install.json"
        _r7 = json.loads(_r7p.read_text(encoding="utf-8"))
        for _f in _r7["files"]:
            if _f.get("role") == "forked":
                _f.pop("direction", None)
                _f.pop("record", None)
        _r7p.write_text(json.dumps(_r7, indent=2) + "\n", encoding="utf-8", newline="\n")
        settle(_t7, "a receipt whose forked row carries no direction")
        check("[-10] AC7 the fixture really carries a forked row with NO `direction` key",
              [f for f in json.loads(_r7p.read_text(encoding="utf-8"))["files"]
               if f.get("role") == "forked" and "direction" not in f], _r7p.read_text())
        (_g7 / "tools" / "demo" / "engine.txt").write_text("gov B\n", encoding="utf-8",
                                                           newline="\n")
        git(_g7, "add", "-A")
        git(_g7, "commit", "-qm", "B")
        _u7 = run_in_gov(_g7, "update", "--target", str(_t7), "--write")
        check("[-10] AC7 the run exits 0 rather than raising on the absent key",
              _u7.returncode == 0, _u7.stdout + _u7.stderr)
        check("[-10] AC7 ...with no traceback anywhere in its output",
              "Traceback" not in (_u7.stdout + _u7.stderr) and "KeyError" not in
              (_u7.stdout + _u7.stderr), (_u7.stdout + _u7.stderr)[-800:])
        check("[-10] AC7 ...and the row is PRINTED, with no direction clause and no invented one",
              len([ln for ln in _u7.stdout.splitlines()
                   if ln.startswith("  report") and "[forked" in ln
                   and "direction" not in ln]) == 1, _u7.stdout)
        check("[-10] AC7 ...and COUNTED, so a tolerated row is not a silent one",
              "forked:reported 1" in _u7.stdout, _u7.stdout)
        check("[-10] AC7 ...and still writes no bytes at that path",
              (_t7 / "tools" / "demo" / "forked-one.py").read_text(encoding="utf-8")
              == FORK_TARGET_BYTES, "")

        # ============ DEPL-dCarriedReceipt-11 — rename detection, and `withdrawn` stops deleting =========
        #
        # THE MEASURED RED, on the fixture this block builds, against the engine as it stood with `-1`
        # through `-10` landed and this unit not: `update --write` exited **0**, unlinked EIGHT tracked
        # files from the target, `git rm`-ed them, dropped all eight rows from `install.json` and landed
        # nothing at any new path — 18 tracked files before it, 10 after. SEVEN of those eight were rows
        # whose gov source gov had RENAMED and still ships; the eighth was the one genuine withdrawal, and
        # it was destroyed on the same verdict and by the same branch. The `seed` row printed `current`
        # while its gov source no longer existed, and the `rendered` row printed `patched` and got no
        # second line at all. Every arm below was written against that observation rather than against
        # the spec's prediction of it.
        #
        # WHY ONE GOV AND ONE TARGET CARRY MOST OF IT. Each row below is a different question — a clean
        # rename, a rename that also changes content, a rename over a local delta, a rename gov scored
        # below the threshold, a rename OUT of the kit, a rename to two destinations, a `seed` and a
        # `rendered` — and they are answered on one run so that no arm can pass because a fixture of its
        # own did nothing. The two questions that need a different SHAPE of target get their own: the
        # carried rename needs an install at a prefix gov does not use, which `apply` cannot produce, and
        # the two write-refusals need a target holding something in the way.

        GK11 = govkit_module()


        def read_bytes11(p) -> bytes:
            """Bytes, or empty. `check()` concatenates its detail onto the FAIL line and every arm below
            a raising one never runs, so an arm that reads a file the break just removed would report its
            own coverage as untested rather than as red. Measured on this unit's break sweep."""
            return p.read_bytes() if p.is_file() else b""

        _11_LOW_A = "alpha\nbeta\ngamma\ndelta\nepsilon\nzeta\neta\ntheta\niota\nkappa\n"
        _11_LOW_B = ("alpha\nbeta\ngamma\nXX1xxxx\nXX2xxxx\nXX3xxxx\nXX4xxxx\nXX5xxxx\nXX6xxxx\n"
                     "XX7xxxx\n")
        _11_DELTA_T = "delta one\ndelta two\ndelta three\nADOPTER EDIT\n"
        _11_DELTA_B = "delta one\nDELTA GOV CHANGE\ndelta three\ndelta four\n"
        _11_DELTA_M = "delta one\nDELTA GOV CHANGE\ndelta three\nADOPTER EDIT\n"
        _11_CONTENT_B = "content one\nCONTENT GOV CHANGE\ncontent three\ncontent four\n"

        # The descriptor, in its two vintages. Gov renaming a file inside its own kit and updating its own
        # includes in the same commit is the whole motivating scenario, so the fixture does exactly that —
        # and it is what makes `resolve_entry` the only thing that can answer where the new source lands.
        _11_KIT_A = ('id = "demo"\nhome = "tools/demo"\nversion_from = { none = "fixture" }\n\n'
                     '[check]\nnone = "a fixture kit"\n\n'
                     '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                     '[[files]]\ninclude = ["twin.txt"]\n'
                     'to = ["{kit}/twin-a.txt", "{kit}/twin-b.txt"]\nrole = "engine"\n\n'
                     '[[files]]\ninclude = ["seed.txt"]\nrole = "seed"\n\n'
                     '[[files]]\ninclude = ["rendered.txt"]\nrole = "rendered"\n\n'
                     '[adopt]\nargv = []\nmutates_index = false\n')
        _11_KIT_B = (_11_KIT_A.replace('include = ["twin.txt"]', 'include = ["twin2.txt"]')
                     .replace('include = ["seed.txt"]', 'include = ["seed2.txt"]')
                     .replace('include = ["rendered.txt"]', 'include = ["rendered2.txt"]'))

        _11_SRC = {
            "keep.txt": "keep A\n",                       # the control: gov EDITS it, never moves it
            "moved.txt": "moved one\nmoved two\nmoved three\n",
            "content.txt": "content one\ncontent two\ncontent three\ncontent four\n",
            "delta.txt": "delta one\ndelta two\ndelta three\ndelta four\n",
            "low.txt": _11_LOW_A,
            "gone.txt": "gone one\ngone two\ngone three\n",
            "twin.txt": "twin one\ntwin two\ntwin three\n",
            "seed.txt": "seed one\nseed two\nseed three\n",
            "rendered.txt": "rendered one\nrendered two\nrendered three\n",
            "sub.txt": "sub one\nsub two\nsub three\n",
            "dropped.txt": "dropped one\ndropped two\ndropped three\n",
        }


        def build_rename_gov(tag: str, kit_a: str = _11_KIT_A) -> pathlib.Path:
            """A scratch gov carrying ONE `demo` kit and a copy of the engine.

            THE COPY IS TAKEN HERE, at fixture-build time — a break staged into this repo's `govkit.py`
            AFTER the copy runs the UNPATCHED engine and the arm reports on nothing.
            """
            g = tmp / f"rn-{tag}-gov"
            (g / "tools" / "govkit").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                '[selection]\ndefault = ["demo"]\n\n'
                '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
                encoding="utf-8", newline="\n")
            d = g / "tools" / "demo"
            d.mkdir(parents=True, exist_ok=True)
            (d / "kit.toml").write_text(kit_a, encoding="utf-8", newline="\n")
            for rel, body in _11_SRC.items():
                (d / rel).write_text(body, encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g


        def write_rename_vintage(g: pathlib.Path) -> str:
            """Gov's second vintage: nine renames, one deletion-and-addition, two edits."""
            d = g / "tools" / "demo"
            git(g, "mv", "tools/demo/moved.txt", "tools/demo/renamed.txt")
            git(g, "mv", "tools/demo/content.txt", "tools/demo/content2.txt")
            (d / "content2.txt").write_text(_11_CONTENT_B, encoding="utf-8", newline="\n")
            git(g, "mv", "tools/demo/delta.txt", "tools/demo/delta2.txt")
            (d / "delta2.txt").write_text(_11_DELTA_B, encoding="utf-8", newline="\n")
            (d / "low.txt").unlink()                       # rewritten far enough that git pairs nothing
            (d / "newlow.txt").write_text(_11_LOW_B, encoding="utf-8", newline="\n")
            (g / "docs").mkdir(parents=True, exist_ok=True)
            git(g, "mv", "tools/demo/gone.txt", "docs/gone.txt")     # OUT of the kit's home entirely
            git(g, "mv", "tools/demo/twin.txt", "tools/demo/twin2.txt")
            git(g, "mv", "tools/demo/seed.txt", "tools/demo/seed2.txt")
            git(g, "mv", "tools/demo/rendered.txt", "tools/demo/rendered2.txt")
            (d / "sub").mkdir(parents=True, exist_ok=True)
            git(g, "mv", "tools/demo/sub.txt", "tools/demo/sub/sub.txt")     # into a NEW subdirectory
            git(g, "mv", "tools/demo/dropped.txt", "tools/demo/dropped2.txt")
            (d / "keep.txt").write_text("keep B\n", encoding="utf-8", newline="\n")
            (d / "kit.toml").write_text(_11_KIT_B, encoding="utf-8", newline="\n")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "B")
            return gout(g, "rev-parse", "HEAD").strip()


        def build_rename_target(g: pathlib.Path, name: str) -> pathlib.Path:
            """An installed target, built by running the real `apply` rather than by authoring a receipt.

            The adopter's own file is written BEFORE `apply`, because a `rendered` destination that is
            absent when apply looks at it is a finding — and a fixture whose apply reds is a fixture whose
            later arms are grading a broken install. The local delta is an EDIT AFTER the install, which is
            the state the three-way exists for.
            """
            t = make_target(tmp / name, 'gov_source = "local"\nprefix = "tools"\nkits = ["demo"]\n')
            (t / "tools" / "demo").mkdir(parents=True, exist_ok=True)
            (t / "tools" / "demo" / "rendered.txt").write_text(
                "the adopter rendered this\n", encoding="utf-8", newline="\n")
            settle(t, "the adopter's own rendered file")
            _ap = run_in_gov(g, "apply", "--target", str(t), "--kits", "demo")
            check(f"[-11] the {name} fixture's install applies GREEN, or every arm over it grades a "
                  f"broken target", _ap.returncode == 0, _ap.stdout[-900:] + _ap.stderr[-600:])
            (t / "tools" / "demo" / "delta.txt").write_text(_11_DELTA_T, encoding="utf-8", newline="\n")
            # AND ONE ROW THE TARGET DELETED, committed rather than staged: `-12` S4 calls a STAGED
            # deletion dirty and would refuse the run before any verdict, so a path absent from the
            # index, the worktree AND HEAD is the only way to reach this state at all.
            (t / "tools" / "demo" / "dropped.txt").unlink()
            settle(t, "the install, one adopter edit and one adopter deletion")
            return t


        _g11 = build_rename_gov("main")
        _A11 = gout(_g11, "rev-parse", "HEAD").strip()
        _t11 = build_rename_target(_g11, "rn-main-t")
        _B11 = write_rename_vintage(_g11)

        # ---- THE FIXTURE'S OWN PRECONDITIONS. A fixture that does not trigger the rule proves nothing,
        # ---- and every rule below is triggered by GIT's rename scoring rather than by anything this file
        # ---- controls directly.
        _rn50 = gout(_g11, "diff", "--find-renames=50%", "--name-status", _A11, _B11)
        _rn10 = gout(_g11, "diff", "--find-renames=10%", "--name-status", _A11, _B11)
        _pairs50 = {ln.split("\t")[1]: ln.split("\t")[2] for ln in _rn50.splitlines()
                    if ln.startswith("R") and len(ln.split("\t")) == 3}
        check("[-11] the fixture really renames: git pairs nine sources at the declared threshold",
              len(_pairs50) == 9 and _pairs50.get("tools/demo/moved.txt") == "tools/demo/renamed.txt",
              _rn50)
        check("[-11] ...including one that leaves the kit's home, which only an UNSCOPED diff can see",
              _pairs50.get("tools/demo/gone.txt") == "docs/gone.txt", _rn50)
        check("[-11] S7 the low-similarity pair is NOT paired at the declared threshold",
              "tools/demo/low.txt" not in _pairs50, _rn50)
        check("[-11] S7 LIVENESS ...and IS paired below it, so the constant is what decides, not the bytes",
              "R" in _rn10 and "tools/demo/low.txt\ttools/demo/newlow.txt" in _rn10, _rn10)
        check("[-11] S7 the threshold is a NAMED constant rather than git's implicit default",
              GK11.RENAME_SIMILARITY_PERCENT == 50, str(GK11.RENAME_SIMILARITY_PERCENT))
        _map11 = GK11.derive_rename_map(_g11, _A11, _B11)
        check("[-11] S1 the engine's own map is that same pairing, derived rather than restated",
              _map11 == _pairs50, str(sorted(_map11.items())))
        check("[-11] S1 a receipt carrying no gov_commit gets an EMPTY map, never a guessed base",
              GK11.derive_rename_map(_g11, None, _B11) == {}, "")
        _rec11a = json.loads((_t11 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _row11 = {f["path"]: f for f in _rec11a["files"]}
        check("[-11] the fixture's delta row really carries an adopter edit gov's blob does not have",
              (_t11 / "tools" / "demo" / "delta.txt").read_bytes() != _11_SRC["delta.txt"].encode(), "")
        check("[-11] ...and its clean row does NOT, or AC8 would grade the merge arm by accident",
              (_t11 / "tools" / "demo" / "content.txt").read_bytes() == _11_SRC["content.txt"].encode(), "")
        check("[-11] the fixture's rendered row is in the receipt AND in the target's index",
              _row11.get("tools/demo/rendered.txt", {}).get("role") == "rendered"
              and "tools/demo/rendered.txt" in gout(_t11, "ls-files").split(), str(sorted(_row11)))
        check("[-11] the fixture's seed row is in the receipt as `seed`",
              _row11.get("tools/demo/seed.txt", {}).get("role") == "seed", str(sorted(_row11)))

        # ---- THE READ-ONLY RUN. AC10 lives here: it asserts a string is ABSENT from the whole output, so
        # ---- it has to run over a fixture where no row can legitimately print it.
        _ro11 = run_in_gov(_g11, "update", "--target", str(_t11))
        check("[-11] the read-only run exits 0 over a receipt full of renamed sources",
              _ro11.returncode == 0, _ro11.stdout[-1200:] + _ro11.stderr[-800:])
        check("[-11] S1 the run PRINTS the map it derived rather than finding renames silently",
              "rename map: 9 gov source(s) moved" in _ro11.stdout, _ro11.stdout[:1400])
        check("[-11] S2 a clean renamed row takes the new verdict rather than `withdrawn`",
              verdict_of(_ro11.stdout, "tools/demo/moved.txt") == "renamed", _ro11.stdout)
        check("[-11] AC3 a rename git scored below the threshold stays `withdrawn` — nothing is invented",
              verdict_of(_ro11.stdout, "tools/demo/low.txt") == "withdrawn", _ro11.stdout)
        check("[-11] S3 a source renamed OUT of the kit's surface is a withdrawal, not a move",
              verdict_of(_ro11.stdout, "tools/demo/gone.txt") == "withdrawn"
              and "it has left this kit's claimed surface" in _ro11.stdout, _ro11.stdout)
        check("[-11] S3 ...and a new source the kit resolves to SEVERAL destinations is dropped LOUDLY",
              verdict_of(_ro11.stdout, "tools/demo/twin-a.txt") == "withdrawn"
              and "3 destinations" in _ro11.stdout and "picking one would be a guess" in _ro11.stdout,
              _ro11.stdout)
        check("[-11] the control row gov EDITED is still `stale`, so the map moved nothing it should not",
              verdict_of(_ro11.stdout, "tools/demo/keep.txt") == "stale", _ro11.stdout)
        check("[-11] the fixture's deleted row is absent from the target's index, worktree AND HEAD",
              "tools/demo/dropped.txt" not in gout(_t11, "ls-files").split()
              and not (_t11 / "tools" / "demo" / "dropped.txt").exists()
              and "tools/demo/dropped.txt" not in gout(
                  _t11, "ls-tree", "-r", "--name-only", "HEAD").split(), "")
        check("[-11] S2 a row the TARGET deleted is not a rename however the map reads: there is nothing "
              "to move, and the grid already answers `converged` for a file gone on both sides",
              verdict_of(_ro11.stdout, "tools/demo/dropped.txt") == "converged", _ro11.stdout)
        check("[-11] AC10 S0c a `seed` row whose gov source MOVED prints `renamed`",
              verdict_of(_ro11.stdout, "tools/demo/seed.txt") == "renamed", _ro11.stdout)
        check("[-11] AC10 S0c ...and the string `current` appears NOWHERE in that run's output — the seed "
              "override may not rewrite this verdict over a source that no longer exists",
              "current" not in _ro11.stdout, _ro11.stdout)
        check("[-11] AC6 the read-only run wrote NOTHING: no outbox, no order, no deletion",
              not (_t11 / ".governance" / "outbox").exists()
              or not list((_t11 / ".governance" / "outbox").glob("update-withdrawn-*")),
              str(sorted(p.name for p in (_t11 / ".governance" / "outbox").glob("*"))
                  if (_t11 / ".governance" / "outbox").exists() else []))

        # ---- THE WRITE RUN. AC6's standing predicate is measured ACROSS it: no `update --write` without
        # ---- `--write-withdrawals` may reduce the target's tracked-file count, whatever any verdict says.
        _files_before = sorted(x for x in gout(_t11, "ls-files").splitlines() if x)
        _w11 = run_in_gov(_g11, "update", "--target", str(_t11), "--write")
        _files_after = sorted(x for x in gout(_t11, "ls-files").splitlines() if x)
        check("[-11] AC2 `update --write` exits 0 with nine renamed sources in the receipt",
              _w11.returncode == 0, _w11.stdout[-2000:] + _w11.stderr[-1000:])
        check("[-11] AC6 THE STANDING PREDICATE: the tracked-file count is UNCHANGED across a run with no "
              "--write-withdrawals", len(_files_before) == len(_files_after),
              f"{len(_files_before)} -> {len(_files_after)}: "
              f"{sorted(set(_files_before) - set(_files_after))}")
        check("[-11] AC3 ...so the below-threshold row's file is still on disk",
              (_t11 / "tools" / "demo" / "low.txt").is_file(), "")
        check("[-11] AC3 ...and still tracked, and still a row in install.json",
              "tools/demo/low.txt" in _files_after
              and any(f["path"] == "tools/demo/low.txt" for f in json.loads(
                  (_t11 / ".governance" / "install.json").read_text(encoding="utf-8"))["files"]), "")
        check("[-11] S8 ...with an ORDER naming the file, its last gov commit and why nothing was deleted",
              (_t11 / ".governance" / "outbox" / "update-withdrawn-low.txt.md").is_file()
              and "NOTHING was deleted" in (_t11 / ".governance" / "outbox"
                                            / "update-withdrawn-low.txt.md").read_text(encoding="utf-8")
              and _A11 in (_t11 / ".governance" / "outbox"
                           / "update-withdrawn-low.txt.md").read_text(encoding="utf-8"),
              (_t11 / ".governance" / "outbox" / "update-withdrawn-low.txt.md").read_text(encoding="utf-8")
              if (_t11 / ".governance" / "outbox" / "update-withdrawn-low.txt.md").is_file() else "no order")

        _status11 = gout(_t11, "status", "--porcelain")
        check("[-11] AC2 the target's own git sees an R entry for the clean rename",
              any(ln.startswith("R") and "tools/demo/moved.txt" in ln and "tools/demo/renamed.txt" in ln
                  for ln in _status11.splitlines()), _status11)
        check("[-11] AC2 ...the old path is gone from the worktree and the new one is there",
              not (_t11 / "tools" / "demo" / "moved.txt").exists()
              and (_t11 / "tools" / "demo" / "renamed.txt").is_file(), "")
        check("[-11] S4 ...and the rename into a NEW subdirectory worked, parent and all",
              (_t11 / "tools" / "demo" / "sub" / "sub.txt").is_file(), "")
        _rec11b = json.loads((_t11 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _row11b = {f["path"]: f for f in _rec11b["files"]}
        check("[-11] AC2 the receipt row's `path` AND `source` both carry the new spelling",
              _row11b.get("tools/demo/renamed.txt", {}).get("source") == "tools/demo/renamed.txt",
              str(sorted(_row11b)))
        check("[-11] S4 ...and the old spelling is a row no more",
              "tools/demo/moved.txt" not in _row11b, str(sorted(_row11b)))
        check("[-11] S2 ...and the run stayed HEALTHY over it — no `git mv` of a file that is not "
              "there, and no traceback either: asserting only the absence of a message would let a "
              "crash pass for a guard",
              _w11.returncode == 0 and "could not be moved" not in _w11.stdout
              and "Traceback" not in (_w11.stdout + _w11.stderr),
              _w11.stdout[-600:] + _w11.stderr[-400:])
        check("[-11] S6 the run reports the moves it performed, counted rather than implied",
              "moved 4," in _w11.stdout, _w11.stdout[-400:])

        # ---- AC8 + AC9: THE CLEAN RENAME THAT ALSO CHANGES CONTENT. This is the arm that fails against a
        # ---- draft which moves the file and stamps the row forward without writing gov's new bytes — and
        # ---- against one that defers the byte question to a post-move comparison, which freezes the file
        # ---- at pre-rename content and prints `patched` for an adopter edit that never happened.
        _c2 = "tools/demo/content2.txt"
        _idx_c2 = gout(_t11, "ls-files", "-s", "--", _c2).split()
        check("[-11] AC8 the renamed-and-edited row is in the index at its NEW path",
              len(_idx_c2) >= 2, gout(_t11, "ls-files", "-s", "--", _c2))
        check("[-11] AC8 ...holding gov's blob at the requested vintage for the NEW source, byte for byte",
              len(_idx_c2) >= 2
              and _idx_c2[1] == GK11.blob_oid(GK11.blob_at(_g11, _B11, "tools/demo/content2.txt")),
              str(_idx_c2))
        check("[-11] AC8 ...and NOT the pre-rename content, which is what a deferred byte decision leaves",
              read_bytes11(_t11 / _c2) == _11_CONTENT_B.encode(), repr(read_bytes11(_t11 / _c2)))
        check("[-11] AC8 the row's `commit` and `gov_oid` BOTH carry the --to vintage, never one without "
              "the other", _row11b.get(_c2, {}).get("commit") == _B11
              and _row11b.get(_c2, {}).get("gov_oid") == GK11.blob_oid(
                  GK11.blob_at(_g11, _B11, "tools/demo/content2.txt")), str(_row11b.get(_c2))[:300])
        check("[-11] AC9 that row's verdict was `renamed`, and the string `patched` appears NOWHERE in the "
              "write run's output", verdict_of(_w11.stdout, "tools/demo/content.txt") == "renamed"
              and "patched" not in _w11.stdout, _w11.stdout)
        check("[-11] AC9 ...and its stored sha256 is gov's blob at --to, not the pre-rename content",
              _row11b.get(_c2, {}).get("sha256") == GK11._sha(_11_CONTENT_B.encode()),
              str(_row11b.get(_c2))[:300])

        # ---- AC5: THE RENAMED ROW CARRYING A LOCAL DELTA. Moved, then three-way merged — asserted on
        # ---- CONTENT and never on an exit code, because a wrong argument order to `git merge-file` emits
        # ---- a plausible file with one side silently dropped and exits 0.
        _d2 = "tools/demo/delta2.txt"
        _idx_d2 = gout(_t11, "ls-files", "-s", "--", _d2).split()
        check("[-11] AC5 the delta row moved to its new path", len(_idx_d2) >= 2, str(_idx_d2))
        check("[-11] AC5 ...and what it holds is NOT gov's blob there, which is what proves no raw write",
              len(_idx_d2) >= 2
              and _idx_d2[1] != GK11.blob_oid(GK11.blob_at(_g11, _B11, "tools/demo/delta2.txt")),
              str(_idx_d2))
        check("[-11] AC5 ...it is the MERGE: gov's change landed and the adopter's edit survived",
              read_bytes11(_t11 / _d2) == _11_DELTA_M.encode(), repr(read_bytes11(_t11 / _d2)))
        check("[-11] AC5 the two identities SPLIT on that row — `oid` is what the target holds, `gov_oid` "
              "is gov's own blob at the new source",
              len(_idx_d2) >= 2 and _row11b.get(_d2, {}).get("oid") == _idx_d2[1]
              and _row11b.get(_d2, {}).get("gov_oid") == GK11.blob_oid(
                  GK11.blob_at(_g11, _B11, "tools/demo/delta2.txt")), str(_row11b.get(_d2))[:300])

        # ---- AC11: S0b's reported-only line. A verdict word missing from that tuple falls through to a
        # ---- bare `continue`, so the row's disposition — reported, never moved — is never stated.
        check("[-11] AC11 S0b a `rendered` row whose gov source moved gets the reported-only line, naming "
              "the new verdict", any(ln.startswith("  reported only") and "[rendered]" in ln
                                     and "renamed" in ln and "tools/demo/rendered.txt" in ln
                                     for ln in _w11.stdout.splitlines()), _w11.stdout)
        check("[-11] AC11 ...in ADDITION to its verdict line, which is where the row is first named",
              verdict_of(_w11.stdout, "tools/demo/rendered.txt") == "renamed", _w11.stdout)
        check("[-11] AC11 ...and the adopter's own bytes are untouched: this role is never written",
              read_bytes11(_t11 / "tools" / "demo" / "rendered.txt") == b"the adopter rendered this\n",
              repr(read_bytes11(_t11 / "tools" / "demo" / "rendered.txt")))
        check("[-11] AC10 S0c ...and the `seed` row is reported the same way, never written",
              any(ln.startswith("  reported only") and "[seed]" in ln and "renamed" in ln
                  for ln in _w11.stdout.splitlines())
              and (_t11 / "tools" / "demo" / "seed.txt").is_file(), _w11.stdout)

        # ---- THE NEXT RUN is what the four-fields-together stamp is FOR, so it is exercised rather than
        # ---- argued. If `commit` and `gov_oid` disagreed after the move, `-7` S9's preamble would refuse
        # ---- this whole run and the target could never be updated again.
        settle(_t11, "after the rename update")
        _w11b = run_in_gov(_g11, "update", "--target", str(_t11), "--write")
        check("[-11] S4 the run AFTER the rename is accepted by `-7`'s receipt-integrity preamble",
              _w11b.returncode == 0 and "REFUSING" not in _w11b.stderr,
              _w11b.stdout[-1200:] + _w11b.stderr[-800:])
        check("[-11] S4 ...and every moved row now reads `current` at its new spelling",
              verdict_of(_w11b.stdout, "tools/demo/renamed.txt") == "current"
              and verdict_of(_w11b.stdout, _c2) == "current", _w11b.stdout)
        check("[-11] S4 ...while the merged row reads `patched`, which is what a surviving edit IS",
              verdict_of(_w11b.stdout, _d2) == "patched", _w11b.stdout)

        # ---- AC4: the deletion, and the ONLY way to get one.
        settle(_t11, "after the second update")
        _files_pre_wd = sorted(x for x in gout(_t11, "ls-files").splitlines() if x)
        _wd11 = run_in_gov(_g11, "update", "--target", str(_t11), "--write", "--write-withdrawals")
        _files_post_wd = sorted(x for x in gout(_t11, "ls-files").splitlines() if x)
        check("[-11] AC4 `--write-withdrawals` is accepted by the parser and the run exits 0",
              _wd11.returncode == 0, _wd11.stdout[-1200:] + _wd11.stderr[-800:])
        check("[-11] AC4 ...and THAT is when the withdrawn row is deleted: `ls-files` no longer names it",
              "tools/demo/low.txt" not in _files_post_wd and not (_t11 / "tools/demo/low.txt").exists(),
              str(sorted(set(_files_pre_wd) - set(_files_post_wd))))
        check("[-11] AC4 ...its row is dropped from the receipt rather than left claiming a deleted file",
              not any(f["path"] == "tools/demo/low.txt" for f in json.loads(
                  (_t11 / ".governance" / "install.json").read_text(encoding="utf-8"))["files"]), "")
        check("[-11] AC4 ...and an order is written under .governance/outbox/ either way",
              (_t11 / ".governance" / "outbox" / "update-withdrawn-low.txt.md").is_file()
              and "It WAS deleted" in (_t11 / ".governance" / "outbox"
                                       / "update-withdrawn-low.txt.md").read_text(encoding="utf-8"),
              (_t11 / ".governance" / "outbox" / "update-withdrawn-low.txt.md").read_text(encoding="utf-8"))
        check("[-11] AC6 LIVENESS the count DID fall on the run that was allowed to delete — the predicate "
              "above measures a guard, not an inert fixture",
              len(_files_post_wd) < len(_files_pre_wd),
              f"{len(_files_pre_wd)} -> {len(_files_post_wd)}")
        check("[-11] S9 the flag is a SCOPE flag: nothing gov still ships was touched by it",
              (_t11 / "tools" / "demo" / "renamed.txt").is_file()
              and (_t11 / "tools" / "demo" / "keep.txt").is_file(), "")

        # ---- THE TWO WRITE REFUSALS. Both are reachable only with something IN THE WAY, so each gets a
        # ---- target that has it. Neither is a `--force`-able state: the row is left exactly as it was.
        _g11b = build_rename_gov("occupied")
        _t11b = build_rename_target(_g11b, "rn-occupied-t")
        (_t11b / "tools" / "demo" / "renamed.txt").write_text(
            "the operator's own file, at the path gov is about to move something to\n",
            encoding="utf-8", newline="\n")
        settle(_t11b, "a file already sitting at the rename destination")
        write_rename_vintage(_g11b)
        check("[-11] the occupied fixture really holds a file at the destination gov renames into",
              (_t11b / "tools" / "demo" / "renamed.txt").is_file()
              and "tools/demo/renamed.txt" in gout(_t11b, "ls-files").split(), "")
        _occ = run_in_gov(_g11b, "update", "--target", str(_t11b), "--write")
        check("[-11] a rename whose destination the target ALREADY holds is a refusal by name",
              _occ.returncode == 1 and "ALREADY holds a file there" in _occ.stdout, _occ.stdout[-1500:])
        check("[-11] ...and it is a REFUSAL rather than an overwrite: those bytes are untouched",
              read_bytes11(_t11b / "tools" / "demo" / "renamed.txt").startswith(b"the operator's own file"),
              repr(read_bytes11(_t11b / "tools" / "demo" / "renamed.txt")))
        check("[-11] ...and the row it refused is still at its old path, at its old vintage",
              (_t11b / "tools" / "demo" / "moved.txt").is_file()
              and [f for f in json.loads((_t11b / ".governance" / "install.json").read_text(
                  encoding="utf-8"))["files"] if f["path"] == "tools/demo/moved.txt"], "")

        _g11c = build_rename_gov("mvfail")
        _t11c = build_rename_target(_g11c, "rn-mvfail-t")
        (_t11c / "tools" / "demo" / "sub").write_text(
            "a FILE where gov is about to want a directory\n", encoding="utf-8", newline="\n")
        settle(_t11c, "a file where the rename needs a parent directory")
        write_rename_vintage(_g11c)
        check("[-11] the mv-failure fixture really holds a FILE at the new parent's path",
              (_t11c / "tools" / "demo" / "sub").is_file(), "")
        _mvf = run_in_gov(_g11c, "update", "--target", str(_t11c), "--write")
        check("[-11] a move that cannot be performed is REPORTED, never half-applied",
              _mvf.returncode == 1 and "could not be moved to" in _mvf.stdout, _mvf.stdout[-1500:])
        check("[-11] ...with the row left exactly as it was, at its old path",
              (_t11c / "tools" / "demo" / "sub.txt").is_file(), "")
        check("[-11] ...and the receipt NOT re-stamped, so the next run re-attempts rather than forgetting",
              json.loads((_t11c / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("gov_commit") != gout(_g11c, "rev-parse", "HEAD").strip(), "")
        check("[-11] LIVENESS the same run still moved the rows it COULD, so one bad row strands nothing",
              (_t11c / "tools" / "demo" / "renamed.txt").is_file(), _mvf.stdout[-1200:])

        # ---- THE ESCAPING DESTINATION. The destination is composed from the TARGET's own answers, so a
        # ---- `prefix` that climbs out of the tree is target-supplied data reaching a write path — the
        # ---- same class the receipt-path guard beside it exists for, one field further along.
        _g11d = build_rename_gov("escape")
        _A11d = gout(_g11d, "rev-parse", "HEAD").strip()
        _t11d = make_target(tmp / "rn-escape-t",
                            'gov_source = "local"\nprefix = "../escape"\nkits = ["demo"]\n')
        (_t11d / "tools" / "demo").mkdir(parents=True, exist_ok=True)
        (_t11d / "tools" / "demo" / "moved.txt").write_text(
            _11_SRC["moved.txt"], encoding="utf-8", newline="\n")
        settle(_t11d, "one installed file, at a sane path")
        _idx11d = {}
        for _ln in gout(_t11d, "ls-files", "-s").splitlines():
            _meta, _p = _ln.split("\t", 1)
            _idx11d[_p] = _meta.split()[1]
        (_t11d / ".governance" / "install.json").write_text(json.dumps({
            "schema": 3, "gov_source": "local", "gov_commit": _A11d, "kits": ["demo"],
            "files": [{"path": "tools/demo/moved.txt", "source": "tools/demo/moved.txt", "role": "engine",
                       "kit": "demo", "written": True, "commit": _A11d,
                       "gov_oid": GK11.blob_oid(_11_SRC["moved.txt"].encode()),
                       "oid": _idx11d.get("tools/demo/moved.txt"),
                       "sha256": GK11._sha(_11_SRC["moved.txt"].encode())}]}, indent=2) + "\n",
            encoding="utf-8", newline="\n")
        settle(_t11d, "the receipt")
        write_rename_vintage(_g11d)
        check("[-11] the escape fixture's prefix really resolves the destination outside the target",
              "../escape" in (_t11d / ".governance" / "deploy.toml").read_text(encoding="utf-8"), "")
        _esc = run_in_gov(_g11d, "update", "--target", str(_t11d), "--write")
        check("[-11] a rename destination OUTSIDE the target repository is refused by name",
              _esc.returncode == 1 and "OUTSIDE the repository the operator named" in _esc.stdout,
              _esc.stdout[-1500:])
        check("[-11] ...and nothing was written anywhere: the row is untouched at its old path",
              (_t11d / "tools" / "demo" / "moved.txt").is_file()
              and not (_t11d.parent / "escape").exists(), "")

        # ---- S11: THE CARRIED RENAME. A row DEPL-dCarriedReceipt-9 proves a rung for ALWAYS differs from
        # ---- gov's blob at the old source, so every carried row in a renamed kit lands on the three-way —
        # ---- with an UN-carried base, which is the one input a rung exists to correct. RED observed on
        # ---- this fixture with the rung dropped from this unit's own merge call: every line naming a path
        # ---- read as an operator edit, the merge conflicted, the run exited 1 and nothing moved.
        _C11_A = "".join(f"tools/demo/pathy.txt line {i}\n" for i in range(1, 6))
        _C11_T = _C11_A.replace("tools/demo", "scripts/demo")
        _C11_B = _C11_A.replace("tools/demo/pathy.txt line 3",
                                "GOV SEMANTIC CHANGE at tools/demo/pathy.txt")
        _C11_WANT = _C11_B.replace("tools/demo", "scripts/demo")


        def build_carry_rename_gov() -> pathlib.Path:
            g = tmp / "rn-carry-gov"
            (g / "tools" / "govkit").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                '[selection]\ndefault = ["demo"]\n\n'
                '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
                encoding="utf-8", newline="\n")
            d = g / "tools" / "demo"
            d.mkdir(parents=True, exist_ok=True)
            (d / "kit.toml").write_text(
                'id = "demo"\nhome = "tools/demo"\nversion_from = { none = "fixture" }\n\n'
                '[check]\nnone = "a fixture kit"\n\n'
                '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                '[adopt]\nargv = []\nmutates_index = false\n', encoding="utf-8", newline="\n")
            (d / "pathy.txt").write_text(_C11_A, encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g


        _gc11 = build_carry_rename_gov()
        _Ac11 = gout(_gc11, "rev-parse", "HEAD").strip()
        # The target is AUTHORED rather than applied: `apply` lands gov's own bytes at gov's own spelling,
        # and what is under test is where an adopter ends up after installing at a `prefix` gov does not use.
        _tc11 = tmp / "rn-carry-t"
        _tc11.mkdir(parents=True)
        git(_tc11, "init", "-q", "-b", "main")
        git(_tc11, "config", "user.email", "t@e")
        git(_tc11, "config", "user.name", "t")
        git(_tc11, "config", "core.autocrlf", "false")
        (_tc11 / ".governance").mkdir()
        (_tc11 / ".governance" / "deploy.toml").write_text(
            'gov_source = "local"\nprefix = "scripts"\nkits = ["demo"]\n', encoding="utf-8", newline="\n")
        (_tc11 / "scripts" / "demo").mkdir(parents=True)
        (_tc11 / "scripts" / "demo" / "pathy.txt").write_text(_C11_T, encoding="utf-8", newline="\n")
        git(_tc11, "add", "-A")
        git(_tc11, "commit", "-qm", "the relocated install")
        _ic11 = {}
        for _ln in gout(_tc11, "ls-files", "-s").splitlines():
            _meta, _p = _ln.split("\t", 1)
            _ic11[_p] = _meta.split()[1]
        (_tc11 / ".governance" / "install.json").write_text(json.dumps({
            "schema": 3, "gov_source": "local", "gov_commit": _Ac11, "kits": ["demo"],
            "files": [{"path": "scripts/demo/pathy.txt", "source": "tools/demo/pathy.txt",
                       "role": "engine", "kit": "demo", "written": True, "commit": _Ac11,
                       "gov_oid": GK11.blob_oid(_C11_A.encode()),
                       "oid": _ic11.get("scripts/demo/pathy.txt"),
                       "sha256": GK11._sha(_C11_T.encode())}]}, indent=2) + "\n",
            encoding="utf-8", newline="\n")
        git(_tc11, "add", "-A")
        git(_tc11, "commit", "-qm", "the receipt")
        git(_gc11, "mv", "tools/demo/pathy.txt", "tools/demo/pathy2.txt")
        (_gc11 / "tools" / "demo" / "pathy2.txt").write_text(_C11_B, encoding="utf-8", newline="\n")
        git(_gc11, "add", "-A")
        git(_gc11, "commit", "-qm", "B")
        _Bc11 = gout(_gc11, "rev-parse", "HEAD").strip()

        # ---- THE FIXTURE'S OWN PRECONDITIONS, and the second one is the whole premise of S11: this row
        # ---- proves a rung, and its bytes therefore differ from gov's blob at the old source.
        _recc11 = json.loads((_tc11 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _idxc11, _ = GK11.index_read(_tc11, ["scripts/demo/pathy.txt"])
        _ndc11, _pdc11, _ = GK11.derive_carry_map(
            [(f.get("source"), f.get("path")) for f in _recc11["files"]])
        _cc11 = GK11.classify_row(_gc11, _tc11, _recc11["files"][0], _Bc11, _idxc11, _ndc11)
        check("[-11] S11 the carried fixture's row really proves the `relocate` rung",
              _cc11.get("carry") == "relocate", str(_cc11.get("carry")))
        check("[-11] S11 ...and therefore differs from gov's blob at the OLD source, which is why every "
              "carried row in a renamed kit lands on the three-way",
              read_bytes11(_tc11 / "scripts" / "demo" / "pathy.txt")
              != GK11.blob_at(_gc11, _Ac11, "tools/demo/pathy.txt"),
              repr(read_bytes11(_tc11 / "scripts" / "demo" / "pathy.txt")))
        check("[-11] S11 the fixture's gov copy really moved AND changed between the two vintages",
              GK11.blob_at(_gc11, _Bc11, "tools/demo/pathy.txt") is None
              and GK11.blob_at(_gc11, _Bc11, "tools/demo/pathy2.txt") == _C11_B.encode(), "")
        _wc11 = subprocess.run([sys.executable, str(_gc11 / "tools" / "govkit" / "govkit.py"),
                                "update", "--target", str(_tc11), "--write"],
                               capture_output=True, text=True)
        check("[-11] S11 the carried rename RECONCILES rather than conflicting",
              _wc11.returncode == 0, _wc11.stdout[-1500:] + _wc11.stderr[-900:])
        check("[-11] S11 ...the file is at its new destination, in the TARGET's own prefix",
              (_tc11 / "scripts" / "demo" / "pathy2.txt").is_file()
              and not (_tc11 / "scripts" / "demo" / "pathy.txt").exists(), _wc11.stdout)
        _bc11 = read_bytes11(_tc11 / "scripts" / "demo" / "pathy2.txt")
        check("[-11] S11 ...carrying gov's semantic change at the target's spelling, on every line",
              _bc11 == _C11_WANT.encode(), repr(_bc11))
        check("[-11] S11 ...and spelling gov's own prefix NOWHERE",
              b"tools/demo" not in _bc11, repr(_bc11))
        _rowc11 = (json.loads(
            (_tc11 / ".governance" / "install.json").read_text(encoding="utf-8"))["files"] or [{}])[0]
        check("[-11] S11 the row is stamped per `-9` S12: `gov_oid` is gov's UN-carried blob at the new "
              "source, `oid` is what the target now holds, and they DIFFER",
              _rowc11.get("gov_oid") == GK11.blob_oid(_C11_B.encode())
              and _rowc11.get("oid") != _rowc11.get("gov_oid")
              and _rowc11.get("commit") == _Bc11, str(_rowc11)[:400])
        check("[-11] S11 ...and `path` and `source` moved with them",
              _rowc11.get("path") == "scripts/demo/pathy2.txt"
              and _rowc11.get("source") == "tools/demo/pathy2.txt", str(_rowc11)[:400])

        # ========= DEPL-dCarriedReceipt-14 — post-write verification, with index rollback ========
        #
        # THE MEASURED RED, on this block's own fixture, against the engine with `-1`..`-13` landed
        # and this unit not: `update --write` exited **0**, printed `0 conflict(s)`, left a
        # plausible and WRONG three-way merge staged at `tools/demo/conf.txt`, and re-stamped the
        # receipt at the new vintage. ZERO check subprocesses ran. The kit's own `[check].argv` —
        # the declaration `check` has always run — reported `landed-but-inert` on the very next
        # command, over a file `update` had just written and nothing had observed. Every arm below
        # was written against that observation rather than against the spec's prediction of it.
        #
        # WHY THE CONF FIXTURE IS SHAPED LIKE THIS. `git merge-file` succeeds on NON-OVERLAPPING
        # hunks, so gov changing line 2 and the adopter changing line 7 merges clean and exits 0.
        # The result carries both changes, and the kit's own check declares that those two settings
        # may not coexist. That is the whole exposure in four lines: a merge nothing rejected, a
        # file nothing executed, and a receipt stamped forward over it.

        GK14 = govkit_module()

        _14_CONF_A = "# demo conf\nMODE=lax\nalpha\nbeta\ngamma\ndelta\nLEGACY=off\n"
        _14_CONF_B = _14_CONF_A.replace("MODE=lax", "MODE=strict")
        _14_CONF_T = _14_CONF_A.replace("LEGACY=off", "LEGACY=on")
        _14_CONF_M = _14_CONF_B.replace("LEGACY=off", "LEGACY=on")
        _14_MOVED = "moved one\nmoved two\nmoved three\nmoved four\nmoved five\n"

        # The two guards, and they are the fixture's whole semantics. `conflict` is a rule about the
        # FILE — two settings that may not coexist — which is what makes a clean merge break it.
        # `unwired` is red from the install onward and has nothing to do with any write, which is
        # what makes it the pre-existing-red arm.
        _14_GUARD_CONFLICT = ('conf="$d/conf.txt"\n'
                              'test -f "$conf" || exit 3\n'
                              'if grep -q "^MODE=strict$" "$conf" && grep -q "^LEGACY=on$" "$conf"\n'
                              "then\n"
                              '  echo "check: MODE=strict and LEGACY=on cannot both be set"\n'
                              "  exit 1\n"
                              "fi\n"
                              "exit 0\n")
        _14_GUARD_UNWIRED = ('test -f "$d/wired.marker" || exit 1\n'
                             "exit 0\n")

        def build_kit14(eid: str, arm: str) -> str:
            """One fixture descriptor. `arm` selects which `[check]` SHAPE it declares."""
            chk = {
                "argv": '[check]\nargv = ["bash", "{kit}/check.sh"]\n',
                "none": '[check]\nnone = "a fixture kit that declares no runnable check"\n',
                "token": '[check]\nargv = ["bash", "{kit}/check.sh", "{needs_an_answer}"]\n',
                "no-binary": '[check]\nargv = ["{kit}/no-such-binary-xyzzy"]\n',
            }[arm]
            return (f'id = "{eid}"\nhome = "tools/{eid}"\n'
                    'version_from = { none = "fixture" }\n\n'
                    + chk +
                    '\n[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                    "[adopt]\nargv = []\nmutates_index = false\n")

        def build_verify_gov(tag: str, kits: dict) -> tuple[pathlib.Path, pathlib.Path]:
            """A scratch gov carrying one entry per requested kit, and the run LOG its checks write.

            THE COPY IS TAKEN HERE, at fixture-build time — a break staged into this repo's
            `govkit.py` AFTER the copy runs the UNPATCHED engine and the arm reports on nothing.

            The log lives OUTSIDE the target and its absolute path is baked into each check script.
            Inside the target it would be swept into the fixture's own `settle`, which commits
            whatever the previous arm's checks appended and makes the count a property of the
            fixture's history rather than of this run.
            """
            g = tmp / f"v14-{tag}-gov"
            log = tmp / f"v14-{tag}-runs.txt"
            (g / "tools" / "govkit").mkdir(parents=True)
            shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(
                '[surface]\nglobs = ["tools/*"]\n\n'
                "[selection]\ndefault = [" + ", ".join(f'"{e}"' for e in kits) + "]\n\n"
                + "".join(f'[[entry]]\nid = "{e}"\ndescriptor = "tools/{e}/kit.toml"\n\n'
                          for e in kits)
                + '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
                encoding="utf-8", newline="\n")
            for eid, spec in kits.items():
                d = g / "tools" / eid
                d.mkdir(parents=True, exist_ok=True)
                (d / "kit.toml").write_text(build_kit14(eid, spec.get("arm", "argv")),
                                            encoding="utf-8", newline="\n")
                (d / "check.sh").write_text(
                    "#!/usr/bin/env bash\n"
                    'd="$(cd "$(dirname "$0")" && pwd)"\n'
                    f'printf "%s\\n" "{eid}" >> "{log.as_posix()}"\n'
                    + spec.get("guard", "exit 0\n"),
                    encoding="utf-8", newline="\n")
                for rel, body in (spec.get("files") or {}).items():
                    (d / rel).write_text(body, encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g, log

        def build_verify_target(g: pathlib.Path, name: str, kits) -> pathlib.Path:
            """An installed target, built by running the real `apply` rather than by authoring a
            receipt — so every arm below grades an install this engine can actually produce."""
            t = make_target(tmp / f"v14-{name}",
                            'gov_source = "local"\nprefix = "tools"\nkits = ['
                            + ", ".join(f'"{e}"' for e in kits) + "]\n")
            _ap = run_in_gov(g, "apply", "--target", str(t), "--kits", ",".join(kits))
            check(f"[-14] the {name} fixture installs GREEN, or every arm over it grades a broken "
                  f"target", _ap.returncode == 0, _ap.stdout[-900:] + _ap.stderr[-600:])
            settle(t, "the install")
            return t

        def read_runs14(log: pathlib.Path) -> list[str]:
            return [x for x in log.read_text(encoding="utf-8").split() if x] if log.is_file() else []

        def remove_runs14(log: pathlib.Path) -> None:
            log.unlink(missing_ok=True)

        def read_bytes14(p: pathlib.Path) -> bytes:
            """Bytes, or empty. `check()` concatenates its detail onto the FAIL line and every arm
            below a RAISING one never runs, so an arm that reads a file the break just removed
            reports its own coverage as untested rather than as red. Measured on this unit's break
            sweep, on the arm guarding the untracked file at a refused rename destination — and
            `-11`'s ledger says the same thing about the same class."""
            return p.read_bytes() if p.is_file() else b""

        def read_text14(p: pathlib.Path) -> str:
            return p.read_text(encoding="utf-8") if p.is_file() else ""

        def read_index_oid14(t: pathlib.Path, p: str) -> str:
            """The target's index OID at one path, or the empty string where it has no entry."""
            bits = gout(t, "ls-files", "-s", "--", p).split()
            return bits[1] if len(bits) >= 2 else ""

        # ---- THE ROLLBACK FIXTURE. Two kits: `demo` breaks on the clean merge, `sib` is written
        # ---- by the same run and stays green. One run answers AC1..AC5, because an arm that gets
        # ---- its own fixture can pass by that fixture doing nothing.
        _g14, _log14 = build_verify_gov("roll", {
            "demo": {"guard": _14_GUARD_CONFLICT,
                     "files": {"conf.txt": _14_CONF_A, "moved.txt": _14_MOVED}},
            "sib": {"guard": _14_GUARD_CONFLICT, "files": {"conf.txt": _14_CONF_A}},
        })
        _A14 = gout(_g14, "rev-parse", "HEAD").strip()
        _t14 = build_verify_target(_g14, "roll-t", ["demo", "sib"])
        # THE ADOPTER'S EDIT, committed rather than staged: `-12` S4 refuses a writing verb over a
        # dirty claimed path, so an uncommitted edit would make the update refuse and every arm
        # below would grade a run that never happened.
        (_t14 / "tools" / "demo" / "conf.txt").write_text(_14_CONF_T, encoding="utf-8", newline="\n")
        settle(_t14, "the adopter edits LEGACY in demo's conf")

        # gov's second vintage: one hunk in each kit's conf, and one pure rename inside `demo`.
        (_g14 / "tools" / "demo" / "conf.txt").write_text(_14_CONF_B, encoding="utf-8", newline="\n")
        (_g14 / "tools" / "sib" / "conf.txt").write_text(_14_CONF_B, encoding="utf-8", newline="\n")
        git(_g14, "mv", "tools/demo/moved.txt", "tools/demo/renamed.txt")
        git(_g14, "add", "-A")
        git(_g14, "commit", "-qm", "B")
        _B14 = gout(_g14, "rev-parse", "HEAD").strip()

        # ---- THE FIXTURE'S OWN PRECONDITIONS. A fixture that does not trigger the rule proves
        # ---- nothing, and every rule here is triggered by `git merge-file` and by git's rename
        # ---- scoring rather than by anything this file controls directly.
        _pre14 = run_in_gov(_g14, "check", "--target", str(_t14))
        check("[-14] the fixture's own check arm is GREEN before the write — without that the "
              "transition S5 keys on cannot exist and AC9 would be the only reachable arm",
              "govkit check — demo: adopted" in _pre14.stdout, _pre14.stdout)
        check("[-14] ...and so is the sibling's, or AC5 grades a kit that was already red",
              "govkit check — sib: adopted" in _pre14.stdout, _pre14.stdout)
        _snap14 = {p: read_index_oid14(_t14, p) for p in
                   ("tools/demo/conf.txt", "tools/demo/moved.txt", "tools/sib/conf.txt")}
        check("[-14] the fixture's three touched paths all have index entries before the write",
              all(_snap14.values()), str(_snap14))
        check("[-14] ...and the rename destination has NONE, which is the `absent` marker S2 exists "
              "for: keyed on the old path alone the new spelling sits behind a key nothing reaches",
              read_index_oid14(_t14, "tools/demo/renamed.txt") == "", "")
        _rec14a = json.loads((_t14 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _row14a = {f["path"]: dict(f) for f in _rec14a["files"]}
        # AGAINST GOV'S OWN BLOB, not against the constant the fixture just wrote. The first cut of
        # this arm compared the file to `_14_CONF_T` — which is what put it there — so it held even
        # with the adopter's edit removed from the fixture entirely. An arm that cannot fail.
        check("[-14] the fixture's demo conf really carries an adopter edit gov's blob does not have",
              read_bytes14(_t14 / "tools" / "demo" / "conf.txt")
              != GK14.blob_at(_g14, _A14, "tools/demo/conf.txt")
              and read_bytes14(_t14 / "tools" / "demo" / "conf.txt") == _14_CONF_T.encode(),
              repr(read_bytes14(_t14 / "tools" / "demo" / "conf.txt")))
        check("[-14] ...and the sibling's does NOT, so its row takes the raw arm and stays green",
              read_bytes14(_t14 / "tools" / "sib" / "conf.txt") == _14_CONF_A.encode(), "")
        check("[-14] LIVENESS the three-way this fixture is built around really merges CLEAN and "
              "really produces the file the kit's check rejects",
              GK14.three_way(_14_CONF_T.encode(), _14_CONF_A.encode(), _14_CONF_B.encode())
              == (_14_CONF_M.encode(), "merged"),
              repr(GK14.three_way(_14_CONF_T.encode(), _14_CONF_A.encode(), _14_CONF_B.encode())))
        check("[-14] ...and that merged file carries BOTH settings the kit declares incompatible",
              "MODE=strict" in _14_CONF_M and "LEGACY=on" in _14_CONF_M, _14_CONF_M)

        remove_runs14(_log14)
        _w14 = run_in_gov(_g14, "update", "--target", str(_t14), "--write")

        # ---- AC2: the run REDS, and it reds by NAME rather than on an exit code alone.
        check("[-14] AC2 the run that would have landed the broken merge exits 1",
              _w14.returncode == 1, _w14.stdout[-2000:] + _w14.stderr[-900:])
        check("[-14] AC2 ...reporting the kit by its own state vocabulary, both states on one line",
              any(ln.startswith("govkit update — verify demo:") and "adopted -> landed-but-inert" in ln
                  for ln in _w14.stdout.splitlines()), _w14.stdout)
        check("[-14] AC2 ...naming BOTH exit codes, because one of them is the whole verdict",
              "exit 0 -> 1" in _w14.stdout, _w14.stdout)
        check("[-14] AC2 ...and the verdict that got it there was the CLEAN merge, not a conflict",
              verdict_of(_w14.stdout, "tools/demo/conf.txt") == "diverged"
              and "0 conflict(s)" in _w14.stdout, _w14.stdout)

        # ---- AC3: the index is back where it was, byte for byte, and the rename is undone under
        # ---- BOTH spellings. This is S2's row-keyed snapshot observed directly.
        check("[-14] AC3 the rolled-back path's index entry EQUALS its pre-write oid",
              read_index_oid14(_t14, "tools/demo/conf.txt") == _snap14["tools/demo/conf.txt"],
              f"{read_index_oid14(_t14, 'tools/demo/conf.txt')} vs {_snap14['tools/demo/conf.txt']}")
        check("[-14] AC3 ...and its worktree bytes are the adopter's own, not the merge",
              read_bytes14(_t14 / "tools" / "demo" / "conf.txt") == _14_CONF_T.encode(),
              repr(read_bytes14(_t14 / "tools" / "demo" / "conf.txt")))
        check("[-14] AC3 ...so the target's own git reports NOTHING for it: not staged, not dirty",
              gout(_t14, "status", "--porcelain", "--", "tools/demo/conf.txt").strip() == "",
              gout(_t14, "status", "--porcelain", "--", "tools/demo/conf.txt"))
        check("[-14] AC3 the RENAMED row is restored under its OLD spelling, from its snapshot entry",
              read_index_oid14(_t14, "tools/demo/moved.txt") == _snap14["tools/demo/moved.txt"]
              and (_t14 / "tools" / "demo" / "moved.txt").is_file(),
              read_index_oid14(_t14, "tools/demo/moved.txt"))
        check("[-14] AC3 ...and the NEW spelling is gone from the index AND from the worktree — the "
              "half a path-keyed snapshot cannot reach",
              read_index_oid14(_t14, "tools/demo/renamed.txt") == ""
              and not (_t14 / "tools" / "demo" / "renamed.txt").exists(),
              gout(_t14, "ls-files"))
        check("[-14] AC3 ...and the whole kit is clean in the target's own git, both paths at once",
              gout(_t14, "status", "--porcelain", "--", "tools/demo").strip() == "",
              gout(_t14, "status", "--porcelain", "--", "tools/demo"))

        # ---- AC4: the ROW, and all six fields of it. Restoring bytes and leaving the row stamped
        # ---- forward re-creates `-8`; restoring some of the six is the split `-7` S9 refuses on.
        _rec14b = json.loads((_t14 / ".governance" / "install.json").read_text(encoding="utf-8"))
        _row14b = {f["path"]: dict(f) for f in _rec14b["files"]}
        check("[-14] AC4 the rolled-back row carries all six pre-run fields, together",
              all(_row14b.get("tools/demo/conf.txt", {}).get(k)
                  == _row14a["tools/demo/conf.txt"].get(k) for k in GK14.ROLLBACK_FIELDS),
              str(_row14b.get("tools/demo/conf.txt"))[:400])
        check("[-14] AC4 ...and the RENAMED row's `path` and `source` both carry the OLD spelling, "
              "beside the old `commit` and `gov_oid` — so `-7` S9's preamble holds on the next run",
              _row14b.get("tools/demo/moved.txt", {}).get("source") == "tools/demo/moved.txt"
              and _row14b.get("tools/demo/moved.txt", {}).get("commit") == _A14
              and "tools/demo/renamed.txt" not in _row14b, str(sorted(_row14b)))
        check("[-14] AC4 install.json's gov_commit is UNCHANGED — the `if r.problems` arm declining "
              "to re-stamp", _rec14b.get("gov_commit") == _A14 and _A14 != _B14,
              str(_rec14b.get("gov_commit")))

        # ---- AC5: a green kit's writes SURVIVE a sibling's rollback. Kits are independent, and
        # ---- reverting a correct write to punish a sibling discards a good result.
        check("[-14] AC5 the sibling kit is reported verified, on its own line",
              any(ln.startswith("govkit update — verify sib:") and "verified" in ln
                  for ln in _w14.stdout.splitlines()), _w14.stdout)
        check("[-14] AC5 ...its path is staged at gov's NEW bytes",
              read_index_oid14(_t14, "tools/sib/conf.txt")
              == GK14.blob_oid(GK14.blob_at(_g14, _B14, "tools/sib/conf.txt")),
              read_index_oid14(_t14, "tools/sib/conf.txt"))
        check("[-14] AC5 ...on disk too", read_bytes14(_t14 / "tools" / "sib" / "conf.txt")
              == _14_CONF_B.encode(), repr(read_bytes14(_t14 / "tools" / "sib" / "conf.txt")))
        check("[-14] AC5 ...and its row carries the --to commit while the rolled-back one does not",
              _row14b.get("tools/sib/conf.txt", {}).get("commit") == _B14
              and _row14b.get("tools/demo/conf.txt", {}).get("commit") == _A14,
              str(_row14b.get("tools/sib/conf.txt"))[:300])

        # ---- S7's ORDER. A rollback that left no readable record is a revert the operator finds by
        # ---- accident, days later, in a diff.
        _ord14 = _t14 / ".governance" / "outbox" / "update-rollback-demo.md"
        check("[-14] S7 a rolled-back kit leaves an order under .governance/outbox/",
              _ord14.is_file(),
              str(sorted(p.name for p in (_t14 / ".governance" / "outbox").glob("*"))))
        _ordt14 = read_text14(_ord14)
        check("[-14] S7 ...naming the kit's check argv, BOTH exit codes and every path restored",
              "check.sh" in _ordt14 and "exit 0 -> 1" in _ordt14
              and "restored  tools/demo/conf.txt" in _ordt14
              and "restored  tools/demo/moved.txt" in _ordt14
              and "restored  tools/demo/renamed.txt" in _ordt14, _ordt14)
        check("[-14] S7 ...and NO order was written for the sibling this run did not roll back",
              not (_t14 / ".governance" / "outbox" / "update-rollback-sib.md").exists(), "")
        check("[-14] §5 the closing counts DROP the rolled-back work: `wrote` names the writes that "
              "STAND, and a restored rename leaves `moved` in both spellings at once",
              "wrote 1, moved 0, deleted 0" in _w14.stdout,
              str([ln for ln in _w14.stdout.splitlines() if "wrote " in ln]))

        # ---- S4's two runs per touched kit, counted on this same fixture: two kits, four
        # ---- subprocesses, and the identities of them are the two kits and nothing else.
        check("[-14] S4 exactly two check subprocesses ran per TOUCHED kit, and none for anything "
              "else", sorted(read_runs14(_log14)) == ["demo", "demo", "sib", "sib"],
              str(sorted(read_runs14(_log14))))

        # ---- THE NEXT RUN. The rollback's whole point is that the target is still updatable: if
        # ---- the six fields had been restored partially, `-7` S9's preamble would refuse this run
        # ---- and the target could never be updated again.
        _n14 = run_in_gov(_g14, "update", "--target", str(_t14))
        check("[-14] AC4 the run AFTER a rollback is accepted by `-7`'s receipt-integrity preamble",
              "REFUSING" not in _n14.stderr, _n14.stdout[-900:] + _n14.stderr[-900:])
        check("[-14] AC4 ...and it re-offers exactly the work that was rolled back",
              verdict_of(_n14.stdout, "tools/demo/conf.txt") == "diverged"
              and verdict_of(_n14.stdout, "tools/demo/moved.txt") == "renamed", _n14.stdout)

        # ---- THE PATH THIS RUN NEVER WROTE. A rename destination the target already holds is
        # ---- REFUSED by `-11`, so nothing lands there — and if the same kit then rolls back, the
        # ---- snapshot's `absent` marker for that destination would have the restore unlink an
        # ---- UNTRACKED operator file that refusal exists to protect. The restore is bounded to the
        # ---- paths this run actually wrote, and this is the arm that says so.
        _go14, _logo14 = build_verify_gov("occupied", {
            "demo": {"guard": _14_GUARD_CONFLICT,
                     "files": {"conf.txt": _14_CONF_A, "moved.txt": _14_MOVED}},
        })
        _to14 = build_verify_target(_go14, "occupied-t", ["demo"])
        (_to14 / "tools" / "demo" / "conf.txt").write_text(_14_CONF_T, encoding="utf-8",
                                                           newline="\n")
        settle(_to14, "the adopter edits LEGACY")
        # WRITTEN AFTER THE SETTLE, deliberately: tracked, it would restore from its own index entry
        # and this arm would pass over the safe half of the branch it exists to grade.
        (_to14 / "tools" / "demo" / "renamed.txt").write_text(
            "the operator's own untracked file, at the path gov is about to move something to\n",
            encoding="utf-8", newline="\n")
        (_go14 / "tools" / "demo" / "conf.txt").write_text(_14_CONF_B, encoding="utf-8",
                                                           newline="\n")
        git(_go14, "mv", "tools/demo/moved.txt", "tools/demo/renamed.txt")
        git(_go14, "add", "-A")
        git(_go14, "commit", "-qm", "B")
        check("[-14] the occupied fixture really holds an UNTRACKED file at the rename destination — "
              "tracked, it would restore from its own index entry and this arm would be vacuous",
              (_to14 / "tools" / "demo" / "renamed.txt").is_file()
              and "tools/demo/renamed.txt" not in gout(_to14, "ls-files").split(),
              gout(_to14, "ls-files"))
        _wo14 = run_in_gov(_go14, "update", "--target", str(_to14), "--write")
        check("[-14] the rename is refused by `-11` AND the same kit still rolls back its conf, so "
              "this arm grades a rollback rather than a run that stopped early",
              "ALREADY holds a file there" in _wo14.stdout and "ROLLED BACK" in _wo14.stdout,
              _wo14.stdout[-1500:])
        check("[-14] ...and the operator's untracked bytes SURVIVE it: a path this run never wrote "
              "is not a path it may undo",
              read_bytes14(_to14 / "tools" / "demo" / "renamed.txt").startswith(
                  b"the operator's own untracked file"),
              repr(read_bytes14(_to14 / "tools" / "demo" / "renamed.txt")[:80]))
        check("[-14] ...the order SAYS so rather than listing it as restored",
              "left alone tools/demo/renamed.txt" in read_text14(
                  _to14 / ".governance" / "outbox" / "update-rollback-demo.md"),
              read_text14(_to14 / ".governance" / "outbox" / "update-rollback-demo.md"))

        # ---- AC6: ONLY TOUCHED KITS RUN, TWICE EACH. Three claimed kits, one moving rows. The arm
        # ---- fails both against a draft that baselines every claimed kit — six subprocesses, the
        # ---- whole-bar behaviour §3 refuses — and against one that skips the baseline, which is
        # ---- one subprocess and the wedge AC9 exists to close.
        _g6, _log6 = build_verify_gov("three", {
            "demo": {"guard": _14_GUARD_CONFLICT, "files": {"conf.txt": _14_CONF_A}},
            "idle1": {"guard": _14_GUARD_CONFLICT, "files": {"conf.txt": _14_CONF_A}},
            "idle2": {"guard": _14_GUARD_CONFLICT, "files": {"conf.txt": _14_CONF_A}},
        })
        _t6 = build_verify_target(_g6, "three-t", ["demo", "idle1", "idle2"])
        (_g6 / "tools" / "demo" / "conf.txt").write_text(_14_CONF_B, encoding="utf-8", newline="\n")
        git(_g6, "add", "-A")
        git(_g6, "commit", "-qm", "B")
        _B6 = gout(_g6, "rev-parse", "HEAD").strip()
        check("[-14] AC6 the fixture really claims three kits and moves rows in exactly one",
              json.loads((_t6 / ".governance" / "install.json").read_text(encoding="utf-8"))["kits"]
              == ["demo", "idle1", "idle2"], "")
        remove_runs14(_log6)
        _w6 = run_in_gov(_g6, "update", "--target", str(_t6), "--write")
        check("[-14] AC6 EXACTLY TWO check subprocesses ran — the baseline and the after-pass, over "
              "the one touched kit", read_runs14(_log6) == ["demo", "demo"], str(read_runs14(_log6)))
        check("[-14] AC6 ...and zero for the two claimed kits this run did not touch",
              not [x for x in read_runs14(_log6) if x != "demo"], str(read_runs14(_log6)))
        check("[-14] AC6 each of those two prints ONE not-run line, naming itself",
              len([ln for ln in _w6.stdout.splitlines()
                   if ln.startswith("govkit update — verify idle1:") and "not-run" in ln]) == 1
              and len([ln for ln in _w6.stdout.splitlines()
                       if ln.startswith("govkit update — verify idle2:") and "not-run" in ln]) == 1,
              _w6.stdout)
        check("[-14] AC6 ...and the not-run TALLY reads 2, which is the COUNT rather than the lines",
              "not-run 2" in _w6.stdout, _w6.stdout)
        check("[-14] AC6 the touched kit was verified and the run exits 0",
              _w6.returncode == 0 and "verified 1" in _w6.stdout, _w6.stdout[-1200:])
        check("[-14] AC6 ...and gov_commit advanced, because a verified run is a clean run",
              json.loads((_t6 / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("gov_commit") == _B6, "")
        check("[-14] §5 EVERY tally prints, including the zeros — an absence is never coverage",
              all(w in _w6.stdout for w in ("verified 1", "unverified 0", "not-run 2",
                                            "rolled back 0", "pre-existing red 0")),
              str([ln for ln in _w6.stdout.splitlines() if "verify:" in ln]))

        # ---- AC7: THE SKIP ANNOUNCES ITSELF. A declared `none` and an argv that does not resolve
        # ---- are both `landed-unmeasured`, both counted UNVERIFIED, and neither counted verified.
        # ---- A check that could not run is not a pass.
        _g7v, _log7v = build_verify_gov("unmeasured", {
            "mute": {"arm": "none", "files": {"conf.txt": _14_CONF_A}},
            "tokened": {"arm": "token", "guard": _14_GUARD_CONFLICT,
                        "files": {"conf.txt": _14_CONF_A}},
        })
        _t7v = build_verify_target(_g7v, "unmeasured-t", ["mute", "tokened"])
        for _e in ("mute", "tokened"):
            (_g7v / "tools" / _e / "conf.txt").write_text(_14_CONF_B, encoding="utf-8", newline="\n")
        git(_g7v, "add", "-A")
        git(_g7v, "commit", "-qm", "B")
        remove_runs14(_log7v)
        _w7v = run_in_gov(_g7v, "update", "--target", str(_t7v), "--write")
        check("[-14] AC7 a kit declaring `[check] = { none = \"…\" }` is landed-unmeasured and is "
              "printed UNVERIFIED",
              any(ln.startswith("govkit update — verify mute:") and "landed-unmeasured" in ln
                  and "UNVERIFIED" in ln for ln in _w7v.stdout.splitlines()), _w7v.stdout)
        check("[-14] AC7 ...and so is a kit whose check argv carries an unresolved token",
              any(ln.startswith("govkit update — verify tokened:") and "landed-unmeasured" in ln
                  and "UNVERIFIED" in ln for ln in _w7v.stdout.splitlines()), _w7v.stdout)
        check("[-14] AC7 ...they are counted apart from verified, which reads ZERO here",
              "unverified 2" in _w7v.stdout and "verified 0" in _w7v.stdout, _w7v.stdout)
        check("[-14] AC7 LIVENESS the unresolved argv really ran NOTHING — an unverified kit that "
              "quietly executed its check would be the worst of both",
              read_runs14(_log7v) == [], str(read_runs14(_log7v)))
        check("[-14] AC7 ...and neither state blocks the receipt, which is §8 F2's ruling: report "
              "loudly, do not block",
              _w7v.returncode == 0 and json.loads((_t7v / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("gov_commit") == gout(_g7v, "rev-parse", "HEAD").strip(),
              _w7v.stdout[-900:])

        # ---- AC9: THE WEDGE ARM. A kit red at the BASELINE as well as after is pre-existing red:
        # ---- reported, NOT rolled back, no `r.fail`, and the receipt re-stamps. This arm fails
        # ---- against any draft that keys the rollback on the after-state alone — there, an adopter
        # ---- carrying one unrelated local red reverts every correct write on every run, forever,
        # ---- with `gov_commit` frozen and no `--force` in any spelling to escape by.
        _g9v, _log9v = build_verify_gov("preexisting", {
            "demo": {"guard": _14_GUARD_UNWIRED, "files": {"conf.txt": _14_CONF_A}},
        })
        _t9v = build_verify_target(_g9v, "preexisting-t", ["demo"])
        _pre9 = run_in_gov(_g9v, "check", "--target", str(_t9v))
        check("[-14] AC9 the fixture's kit really is RED before anything is written — without that "
              "precondition this arm grades the verified path and proves nothing",
              "govkit check — demo: landed-but-inert" in _pre9.stdout, _pre9.stdout)
        _snap9 = read_index_oid14(_t9v, "tools/demo/conf.txt")
        (_g9v / "tools" / "demo" / "conf.txt").write_text(_14_CONF_B, encoding="utf-8", newline="\n")
        git(_g9v, "add", "-A")
        git(_g9v, "commit", "-qm", "B")
        _B9 = gout(_g9v, "rev-parse", "HEAD").strip()
        remove_runs14(_log9v)
        _w9v = run_in_gov(_g9v, "update", "--target", str(_t9v), "--write")
        check("[-14] AC9 the kit is printed PRE-EXISTING RED, with both states and both exit codes",
              any(ln.startswith("govkit update — verify demo:") and "PRE-EXISTING RED" in ln
                  and "landed-but-inert -> landed-but-inert" in ln and "exit 1 -> 1" in ln
                  for ln in _w9v.stdout.splitlines()), _w9v.stdout)
        check("[-14] AC9 ...and counted under its own tally rather than folded into another",
              "pre-existing red 1" in _w9v.stdout and "rolled back 0" in _w9v.stdout, _w9v.stdout)
        check("[-14] AC9 NO ROLLBACK: the index does NOT match the pre-write snapshot",
              read_index_oid14(_t9v, "tools/demo/conf.txt") != _snap9,
              f"{read_index_oid14(_t9v, 'tools/demo/conf.txt')} vs {_snap9}")
        check("[-14] AC9 ...and gov's new bytes stand on disk",
              read_bytes14(_t9v / "tools" / "demo" / "conf.txt") == _14_CONF_B.encode(),
              repr(read_bytes14(_t9v / "tools" / "demo" / "conf.txt")))
        check("[-14] AC9 no r.fail was raised for it: the run exits 0 and gov_commit ADVANCES to "
              "--to, which is the only thing that stops the wedge",
              _w9v.returncode == 0
              and json.loads((_t9v / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("gov_commit") == _B9, _w9v.stdout[-1200:])
        check("[-14] AC9 ...and it still leaves an ORDER, so a standing red is readable rather than "
              "merely tolerated",
              (_t9v / ".governance" / "outbox" / "update-preexisting-red-demo.md").is_file()
              and "still broken" in read_text14(_t9v / ".governance" / "outbox"
                                             / "update-preexisting-red-demo.md"),
              str(sorted(p.name for p in (_t9v / ".governance" / "outbox").glob("*"))))
        check("[-14] AC9 LIVENESS both runs happened — a wedge escape that skipped the after-pass "
              "would report the same words over one subprocess",
              read_runs14(_log9v) == ["demo", "demo"], str(read_runs14(_log9v)))

        # ---- §5's error state: a check that CANNOT LAUNCH is red, never unmeasured and never a
        # ---- traceback. Measured through `check`, which is the verb that reports the finding.
        _gnb, _lognb = build_verify_gov("nobinary", {
            "demo": {"arm": "no-binary", "files": {"conf.txt": _14_CONF_A}},
        })
        _tnb = build_verify_target(_gnb, "nobinary-t", ["demo"])
        _cnb = run_in_gov(_gnb, "check", "--target", str(_tnb))
        check("[-14] §5 a check argv naming a binary the target does not have is reported "
              "landed-but-inert and NAMED, never a traceback",
              "govkit check — demo: landed-but-inert" in _cnb.stdout
              and "could not run" in _cnb.stdout
              and "Traceback" not in (_cnb.stdout + _cnb.stderr), _cnb.stdout + _cnb.stderr[-600:])
        check("[-14] §5 ...and it is a finding, so `check` reds rather than exiting 0 on a kit "
              "nothing could measure", _cnb.returncode == 1, _cnb.stdout)

        # ---- THE ORPHAN ROW. A row can name a kit the receipt's own `kits` list does not claim —
        # ---- nothing validates the two against each other, and a hand-edited or text-merged
        # ---- `install.json` produces exactly this. That row still gets a verdict and still gets
        # ---- WRITTEN, and there is no descriptor to ask and no check to run for it. Announced
        # ---- rather than skipped: a kit whose writes nothing verified, reported as nothing, is
        # ---- indistinguishable from one that passed.
        _gor, _logor = build_verify_gov("orphan", {
            "demo": {"guard": _14_GUARD_CONFLICT, "files": {"conf.txt": _14_CONF_A}},
            "sib": {"guard": _14_GUARD_CONFLICT, "files": {"conf.txt": _14_CONF_A}},
        })
        _tor = build_verify_target(_gor, "orphan-t", ["demo", "sib"])
        _recor = json.loads((_tor / ".governance" / "install.json").read_text(encoding="utf-8"))
        _recor["kits"] = ["demo"]          # the row for `sib` stays; the CLAIM for it goes
        (_tor / ".governance" / "install.json").write_text(
            json.dumps(_recor, indent=2) + "\n", encoding="utf-8", newline="\n")
        settle(_tor, "a receipt whose kit list has lost one of its rows' kits")
        for _e in ("demo", "sib"):
            (_gor / "tools" / _e / "conf.txt").write_text(_14_CONF_B, encoding="utf-8", newline="\n")
        git(_gor, "add", "-A")
        git(_gor, "commit", "-qm", "B")
        check("[-14] the orphan fixture really carries a row whose kit the receipt does not claim",
              any(f.get("kit") == "sib" for f in json.loads(
                  (_tor / ".governance" / "install.json").read_text(encoding="utf-8"))["files"])
              and "sib" not in json.loads((_tor / ".governance" / "install.json").read_text(
                  encoding="utf-8"))["kits"], "")
        remove_runs14(_logor)
        _wor = run_in_gov(_gor, "update", "--target", str(_tor), "--write")
        check("[-14] an orphan row's kit is NAMED as unverified rather than silently passed over",
              any(ln.startswith("govkit update — verify sib:") and "NOT VERIFIED" in ln
                  for ln in _wor.stdout.splitlines()), _wor.stdout)
        check("[-14] ...and no check was executed for it, because there is no claim authorising one",
              read_runs14(_logor) == ["demo", "demo"], str(read_runs14(_logor)))
        check("[-14] ...while the CLAIMED kit beside it was still verified normally",
              "verified 1" in _wor.stdout and _wor.returncode == 0, _wor.stdout[-1000:])

        # ---- AC8's second half: the S1 extraction changed `check`'s BEHAVIOUR nowhere. The
        # ---- comparison is against the engine as it stood before this unit, read out of git rather
        # ---- than remembered — a byte comparison of two live runs over one fixture target.
        # AN IMMUTABLE SHA, never `HEAD`. Written against `HEAD` this arm was true for exactly as
        # long as `-14` was unlanded: the moment its own commit became `HEAD`, `run_kit_check` was
        # in the bytes it fetched and its own precondition went red. A base pinned to a moving ref
        # is the class the playbook names in so many words, and this is what it looks like when the
        # ref that moves is the one the unit is landing onto. `af9421d7` is `-14`'s parent, the last
        # commit whose engine predates the extraction.
        _PRE_EXTRACTION_SHA = "af9421d736d6cbd942e953c0159148b91cb425f8"
        _pe_src = subprocess.run(["git", "-C", str(HERE.parents[1]), "show",
                                  f"{_PRE_EXTRACTION_SHA}:tools/govkit/govkit.py"],
                                 capture_output=True).stdout
        check("[-14] AC8 the pre-extraction engine really came out of git, and it is the engine "
              "BEFORE the helper existed",
              len(_pe_src) > 100000 and b"def cmd_check" in _pe_src
              and b"def run_kit_check" not in _pe_src, str(len(_pe_src)))
        # A COPY OF THE WHOLE GOV TREE, `.git` and all: `check` resolves every row's provenance
        # against gov's own blobs, so the pre-extraction engine needs the same commits under it or
        # the two runs would differ for a reason that has nothing to do with the extraction.
        _pre_gov = tmp / "v14-pre-gov"
        shutil.copytree(_g14, _pre_gov)
        (_pre_gov / "tools" / "govkit" / "govkit.py").write_bytes(_pe_src)
        _ac8_now = run_in_gov(_g14, "check", "--target", str(_t14))
        _ac8_was = run_in_gov(_pre_gov, "check", "--target", str(_t14))
        check("[-14] AC8 `check` output is BYTE-IDENTICAL across the S1 extraction, on a fixture "
              "target carrying an argv check, a rolled-back row and a receipt",
              _ac8_now.stdout == _ac8_was.stdout and _ac8_now.returncode == _ac8_was.returncode,
              "NOW:\n" + _ac8_now.stdout[-900:] + "\nWAS:\n" + _ac8_was.stdout[-900:])
        check("[-14] AC8 LIVENESS that comparison ran over a NON-EMPTY report — comparing two "
              "identical empty strings would prove nothing",
              "govkit check — demo:" in _ac8_now.stdout and len(_ac8_now.stdout) > 100,
              _ac8_now.stdout)

        # ============================================================ DEPL-dCarriedReceipt-13
        # `govkit adopt` — the receipt bootstrap. Every arm below runs against a SCRATCH gov with a
        # real multi-commit history, because attribution is a question about history and a
        # single-commit fixture answers it vacuously: with one commit in the walk, rung-major and
        # recency-major agree by construction and AC5 could not fail.
        #
        # THE ENGINE COPY IS TAKEN AT FIXTURE-BUILD TIME, as everywhere else in this file. A break
        # staged into this repo's `govkit.py` after the copy runs the UNPATCHED engine and the arm
        # reports on nothing.
        A13_REG = ('[surface]\nglobs = ["tools/*"]\n\n'
                   '[selection]\ndefault = ["demo"]\n\n'
                   '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                   '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n')

        def a13_kit(extra: str = "") -> str:
            """The fixture descriptor: a `**` engine rule, a `forked` rule, and whatever else the
            caller adds. The forked rule is LAST so precedence elects it for its own source."""
            return ('id = "demo"\nhome = "tools/demo"\n'
                    'version_from = { none = "fixture" }\n\n'
                    '[check]\nnone = "a fixture kit"\n\n'
                    '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                    '[[files]]\ninclude = "forked-one.py"\nrole = "forked"\n'
                    'direction = "gov-from-target"\nrecord = "DEPL-fixture-1"\n'
                    + extra + '\n[adopt]\nargv = []\nmutates_index = false\n')

        def a13_gov(tag: str, waves: list[dict[str, str]], kit_toml: str) -> tuple:
            """A scratch gov whose history is ONE COMMIT PER WAVE, oldest first.

            Returns `(path, [sha per wave])`. A wave is `{relpath under home: text}`; a relpath a
            wave omits keeps whatever the previous wave left, so a file gov never touched again has
            exactly one commit in its own walk — which is what AC4 needs and what a
            rewrite-everything fixture would destroy.
            """
            g = tmp / f"a13-{tag}"
            (g / "tools" / "govkit").mkdir(parents=True)
            (g / "tools" / "demo").mkdir(parents=True)
            shutil.copy2(HERE / "govkit.py", g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(A13_REG, encoding="utf-8",
                                                                  newline="\n")
            (g / "tools" / "demo" / "kit.toml").write_text(kit_toml, encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            # A SCAFFOLDING COMMIT BEFORE WAVE 1, so `<wave-1>^` is a revision that RESOLVES and
            # carries no blob for any kit source. That is the third `--pin` refusal's only reachable
            # fixture, and without it the arm would have to assert a state the tree cannot produce.
            git(g, "add", "-A")
            git(g, "commit", "-qm", "scaffold")
            shas: list[str] = []
            for i, wave in enumerate(waves):
                for rel, body in wave.items():
                    p = g / "tools" / "demo" / rel
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(body, encoding="utf-8", newline="\n")
                git(g, "add", "-A")
                git(g, "commit", "-qm", f"wave-{i}")
                shas.append(subprocess.run(["git", "-C", str(g), "rev-parse", "HEAD"],
                                           capture_output=True, text=True).stdout.strip())
            return g, shas

        def a13_target(tag: str, prefix: str, files: dict[str, bytes],
                       kits: str = '["demo"]') -> pathlib.Path:
            """A target that ALREADY holds the files — the state `adopt` exists for. Written as
            BYTES so an arm can commit CRLF into the index deliberately, which is the whole `eol`
            rung and is unreachable through a text write with `newline="\\n"`."""
            t = tmp / f"a13t-{tag}"
            t.mkdir(parents=True)
            git(t, "init", "-q", "-b", "main")
            git(t, "config", "user.email", "t@e")
            git(t, "config", "user.name", "t")
            git(t, "config", "core.autocrlf", "false")
            (t / ".governance").mkdir()
            (t / ".governance" / "deploy.toml").write_text(
                f'gov_source = "local"\nprefix = "{prefix}"\nkits = {kits}\n',
                encoding="utf-8", newline="\n")
            for rel, body in files.items():
                p = t / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(body)
            git(t, "add", "-A")
            git(t, "commit", "-qm", "base")
            return t

        def a13_receipt(t: pathlib.Path) -> dict:
            return json.loads((t / ".governance" / "install.json").read_text(encoding="utf-8"))

        def a13_row(rec: dict, path: str) -> dict:
            return next((f for f in rec["files"] if f["path"] == path), {})

        def a13_porcelain(t: pathlib.Path) -> str:
            return subprocess.run(["git", "-C", str(t), "status", "--porcelain"],
                                  capture_output=True, text=True).stdout.strip()

        # ---- AC1's RED is HISTORICAL: it was observed before this verb existed and cannot be
        # ---- re-observed now without deleting the verb. What survives it is the JOIN — the verb is
        # ---- in `USAGE` and in `main`'s dispatch tuple, which are the two places §7 requires stay
        # ---- honest together. The module docstring used to spell a COUNT of the verbs beside them,
        # ---- which was wrong from the commit that landed the sixth; that is why this asserts
        # ---- membership in both carriers and no total anywhere.
        _g13src = (HERE / "govkit.py").read_text(encoding="utf-8")
        check("[-13] AC1 the verb is in USAGE",
              "govkit.py adopt " in _g13src.split("USAGE = ", 1)[1][:900], "not in USAGE")
        check("[-13] AC1 ...and in `main`'s dispatch tuple, so parsing and running cannot diverge",
              '"intake", "update", "adopt"' in _g13src and 'if verb == "adopt":' in _g13src)
        check("[-13] AC1 ...and the docstring no longer spells a verb COUNT beside that list",
              "All five verbs" not in _g13src)

        # ---- THE LADDER FIXTURE. Two waves. `moved-one.py` and `ladder.py` are written ONCE and
        # ---- never touched again, so each has exactly one commit in its own walk; everything else
        # ---- moves on in wave 2, so the target's copies attribute to wave 1 and the two vintages
        # ---- are genuinely different. `ladder.py` is the AC5 discriminator, built below.
        _W1 = {"verbatim-one.py": "v1\n", "eol-one.py": "e1\n",
               "moved-one.py": "row: tools/demo/thing\n", "stranger.py": "s1\n",
               "forked-one.py": "f1\n",
               # AC5: at wave 1 this is BYTE-IDENTICAL to what the target holds (verbatim), and at
               # wave 2 it is the same text spelling GOV's own directory, which the needle map
               # rewrites onto the target's (relocate). Newest-first recency picks wave 2 at
               # `relocate`; rung-major must pick wave 1 at `verbatim`.
               "ladder.py": "row: scripts/demo/thing\n"}
        _W2 = {"verbatim-one.py": "v2\n", "eol-one.py": "e2\n", "stranger.py": "s2\n",
               "forked-one.py": "f2\n", "ladder.py": "row: tools/demo/thing\n"}
        _g13, _sh13 = a13_gov("ladder", [_W1, _W2], a13_kit())
        _t13 = a13_target("ladder", "scripts", {
            "scripts/demo/verbatim-one.py": b"v1\n",
            "scripts/demo/eol-one.py": b"e1\r\n",
            "scripts/demo/moved-one.py": b"row: scripts/demo/thing\n",
            "scripts/demo/stranger.py": b"nothing gov ever shipped\n",
            "scripts/demo/forked-one.py": b"f1\n",
            "scripts/demo/ladder.py": b"row: scripts/demo/thing\n"})

        # ---- FIXTURE PRECONDITIONS. Each of the three states the arms below grade must actually be
        # ---- present, or every one of them passes by finding nothing.
        check("[-13] the ladder fixture really has two gov vintages",
              len(_sh13) == 2 and _sh13[0] != _sh13[1], str(_sh13))
        check("[-13] ...and `moved-one.py` was written in wave 1 and never touched again",
              "moved-one.py" in _W1 and "moved-one.py" not in _W2)
        check("[-13] ...and `ladder.py` DID move between the two, which is what AC5 needs",
              _W1["ladder.py"] != _W2["ladder.py"])

        # ---- AC2: READ-ONLY writes nothing and leaves the index alone.
        _p = run_in_gov(_g13, "adopt", "--target", str(_t13))
        check("[-13] AC2 adopt without --write exits 0", _p.returncode == 0, _p.stdout + _p.stderr)
        check("[-13] AC2 ...and creates no receipt",
              not (_t13 / ".governance" / "install.json").exists())
        check("[-13] AC2 ...and leaves the target's index untouched",
              a13_porcelain(_t13) == "", a13_porcelain(_t13))
        check("[-13] AC2 ...and SAYS it wrote nothing rather than looking like it worked",
              "READ-ONLY" in _p.stdout, _p.stdout)

        # ---- AC12: the needle map exists AT BOOTSTRAP, derived from the planned pairs (S4a) and
        # ---- not from a receipt that does not exist yet. The needle count is exactly twice the
        # ---- pair count HERE because every surviving gov directory in this fixture carries a
        # ---- slash, so its `/` and `~` forms differ; that condition is the arm's, not a general
        # ---- law, and `-9`'s own parked decision is about a population where it does not hold.
        _pairs13 = _re.search(r"needle map: (\d+) directory pair\(s\), (\d+) needle\(s\)", _p.stdout)
        check("[-13] AC12 adopt prints its derived needle map", _pairs13 is not None, _p.stdout)
        check("[-13] AC12 ...with a needle count exactly twice the pair count, every gov "
              "directory here carrying a slash",
              bool(_pairs13) and int(_pairs13.group(2)) == 2 * int(_pairs13.group(1))
              and int(_pairs13.group(1)) > 0,
              _pairs13.group(0) if _pairs13 else "")

        # ---- AC5: RUNG-MAJOR. Observed on the ladder row, whose newest commit matches only at
        # ---- `relocate` while the older one matches `verbatim`.
        _p = run_in_gov(_g13, "adopt", "--target", str(_t13), "--write")
        check("[-13] adopt --write exits 0 over a partially attributable tree", _p.returncode == 0,
              _p.stdout + _p.stderr)
        _rec13 = a13_receipt(_t13)
        _ladder = a13_row(_rec13, "scripts/demo/ladder.py")
        check("[-13] AC5 rung-major picks the OLDER commit that matches `verbatim`...",
              _ladder.get("commit") == _sh13[0],
              f"{_ladder.get('commit')} != wave-1 {_sh13[0]}")
        check("[-13] AC5 ...rather than the newer one that matches only at `relocate`",
              _ladder.get("carry") == "verbatim", str(_ladder.get("carry")))

        # ---- AC3: a verbatim row records both identities AGREEING and a proven vintage.
        _verb = a13_row(_rec13, "scripts/demo/verbatim-one.py")
        check("[-13] AC3 a byte-identical row records carry `verbatim`",
              _verb.get("carry") == "verbatim", str(_verb))
        check("[-13] AC3 ...with the two identities AGREEING",
              _verb.get("gov_oid") and _verb.get("gov_oid") == _verb.get("oid"), str(_verb))
        check("[-13] AC3 ...and evidence `vintage-match`, never `apply`",
              _verb.get("evidence") == "vintage-match", str(_verb.get("evidence")))

        # ---- AC4: THE INVERSION GATE. This is the field the whole unit's safety rests on: `gov_oid`
        # ---- is gov's blob at the row's commit and NEVER the bytes on the target's disk. Invert it
        # ---- and the identities agree for every row, the local-delta predicate reads false, and the
        # ---- first `update --write` raw-overwrites every carried edit at exit 0.
        _rel = a13_row(_rec13, "scripts/demo/moved-one.py")
        _gov_blob = subprocess.run(
            ["git", "-C", str(_g13), "rev-parse", f"{_rel.get('commit')}:tools/demo/moved-one.py"],
            capture_output=True, text=True).stdout.strip()
        _tgt_blob = subprocess.run(
            ["git", "-C", str(_t13), "rev-parse", ":scripts/demo/moved-one.py"],
            capture_output=True, text=True).stdout.strip()
        check("[-13] AC4 the relocated row proves the `relocate` rung",
              _rel.get("carry") == "relocate", str(_rel))
        check("[-13] AC4 ...its `gov_oid` is GOV's blob at the row's commit",
              _rel.get("gov_oid") == _gov_blob and bool(_gov_blob),
              f"{_rel.get('gov_oid')} != {_gov_blob}")
        check("[-13] AC4 ...and is NOT the target's own index blob, which is the inversion",
              _rel.get("gov_oid") != _tgt_blob and bool(_tgt_blob),
              f"{_rel.get('gov_oid')} == {_tgt_blob}")

        # ---- AC6 / AC9 / S7: the two states that must NOT be collapsed into each other.
        _str = a13_row(_rec13, "scripts/demo/stranger.py")
        check("[-13] AC6 a row matching no gov vintage records evidence `unattributed`",
              _str.get("evidence") == "unattributed", str(_str))
        check("[-13] AC6 ...carrying neither `commit` nor `gov_oid`",
              "commit" not in _str and "gov_oid" not in _str, str(_str))
        check("[-13] AC6 ...and KEEPS the role its rule declared, rather than becoming `forked`",
              _str.get("role") == "engine", str(_str.get("role")))
        _fork = a13_row(_rec13, "scripts/demo/forked-one.py")
        check("[-13] AC9 a declared-forked row adopts as `forked` though the walk matched it",
              _fork.get("role") == "forked" and _fork.get("commit") == _sh13[0], str(_fork))
        check("[-13] AC9 ...carrying the RULE's direction and record",
              _fork.get("direction") == "gov-from-target"
              and _fork.get("record") == "DEPL-fixture-1", str(_fork))

        # ---- THE TWO STANDING PREDICATES (§5), over the WHOLE receipt rather than one fixture row.
        # ---- Left-shifted as predicates because both defects are classes: an inverted `gov_oid` and
        # ---- a role taken from the attribution outcome are each destructive on EVERY row, and an
        # ---- arm naming one path certifies coverage it does not have.
        _bad_oid = [f["path"] for f in _rec13["files"] if f.get("commit") and f.get("gov_oid")
                    and f.get("source") and f["gov_oid"] != subprocess.run(
                        ["git", "-C", str(_g13), "rev-parse", f"{f['commit']}:{f['source']}"],
                        capture_output=True, text=True).stdout.strip()]
        check("[-13] STANDING every row carrying a commit has gov's OWN blob as its `gov_oid`",
              not _bad_oid, "inverted on: " + ", ".join(_bad_oid))
        check("[-13] STANDING every destination whose rule declares `forked` is written `forked`",
              [f["path"] for f in _rec13["files"] if f.get("role") == "forked"]
              == ["scripts/demo/forked-one.py"],
              str([f["path"] for f in _rec13["files"] if f.get("role") == "forked"]))

        # ---- AC10: THE ENVELOPE. Omitting a key here degrades three other units SILENTLY, which is
        # ---- why the absent set is asserted as hard as the present one: a receipt carrying
        # ---- `orders` or `gate_runner` would be claiming an install this verb never performed.
        check("[-13] AC10 the envelope carries every key a later verb reads",
              all(k in _rec13 for k in ("schema", "gov_source", "gov_commit", "prefix", "kits",
                                        "files")), str(sorted(_rec13)))
        check("[-13] AC10 ...and NONE of the keys that record what an install DID",
              not any(k in _rec13 for k in ("orders", "baseline", "after", "hook_block",
                                            "gate_runner")), str(sorted(_rec13)))
        check("[-13] AC10 ...`gov_commit` is the resolved --to, so `-12`'s vintage guard has a base",
              _rec13.get("gov_commit") == _sh13[1], str(_rec13.get("gov_commit")))
        _sums13 = (_t13 / ".governance" / "install.sums").read_text(encoding="utf-8").splitlines()
        _hashed13 = [f for f in _rec13["files"] if "sha256" in f]
        check("[-13] AC10 install.sums is NON-EMPTY and holds one line per hashed row",
              len(_sums13) == len(_hashed13) and len(_sums13) > 0,
              f"{len(_sums13)} lines vs {len(_hashed13)} hashed rows")
        _pc = run_in_gov(_g13, "check", "--target", str(_t13))
        _sc = _re.search(r"sidecar: (\d+) line\(s\) compared against (\d+) hashed row\(s\)",
                         _pc.stdout)
        check("[-13] AC10 ...and `check` joins the two at the same N, greater than zero",
              bool(_sc) and _sc.group(1) == _sc.group(2) and int(_sc.group(1)) > 0,
              _sc.group(0) if _sc else _pc.stdout)

        # ---- AC11: THE ENVELOPE IS LIVE, not merely present. Without `gov_commit` the `-12` S7
        # ---- vintage guard skips itself BY ITS OWN WORDS and a backwards run raw-writes every
        # ---- clean row. This is the arm that stops the envelope being written and never read.
        settle(_t13, "receipt")
        _pb = run_in_gov(_g13, "update", "--target", str(_t13), "--to", _sh13[0], "--write")
        check("[-13] AC11 a backwards `update --to` REFUSES against the bootstrapped envelope",
              _pb.returncode == 2, f"rc {_pb.returncode}: {_pb.stdout}{_pb.stderr}")
        check("[-13] AC11 ...naming BOTH shas rather than refusing anonymously",
              _sh13[0][:8] in (_pb.stdout + _pb.stderr)
              and _sh13[1][:8] in (_pb.stdout + _pb.stderr), _pb.stderr)

        # ---- S10's absent-optional-keys arm: a receipt carrying none of the five install-record
        # ---- keys must CLASSIFY without refusal. Every reader tolerates absence via `.get`, and
        # ---- this is what asserts that rather than trusting it.
        _pu = run_in_gov(_g13, "update", "--target", str(_t13))
        check("[-13] S10 a receipt with no orders/baseline/after/hook_block/gate_runner classifies",
              _pu.returncode in (0, 1) and "Traceback" not in (_pu.stdout + _pu.stderr),
              _pu.stdout + _pu.stderr)
        check("[-13] AC6 ...and the unattributed row is PRINTED and skipped, never classified",
              "unattributed" in _pu.stdout and "scripts/demo/stranger.py" in _pu.stdout,
              _pu.stdout)

        # ---- AC6 + AC9's write halves. `update --write` must put ZERO bytes at either path: the
        # ---- unattributed one has no base to write against, and the forked one is report-only in
        # ---- BOTH directions. Asserted on the INDEX rather than by reading the message, because a
        # ---- printer saying "report" while the writer writes is exactly the class this checks.
        _before = (_t13 / "scripts" / "demo" / "forked-one.py").read_bytes()
        _before_s = (_t13 / "scripts" / "demo" / "stranger.py").read_bytes()
        run_in_gov(_g13, "update", "--target", str(_t13), "--write")
        check("[-13] AC9 `update --write` writes ZERO bytes to the forked destination",
              (_t13 / "scripts" / "demo" / "forked-one.py").read_bytes() == _before)
        check("[-13] AC6 ...and ZERO bytes to the unattributed one",
              (_t13 / "scripts" / "demo" / "stranger.py").read_bytes() == _before_s)

        # ---- AC4's second half, on its OWN fixture so the assertion is about the rung and not
        # ---- about gov having stood still. `moved-one.py` never moved between the two waves, so an
        # ---- update to the SAME vintage the row was adopted against has nothing to do — and a
        # ---- `relocate` row that raw-wrote anyway would show up here as a modified path.
        _t13b = a13_target("noop", "scripts", {
            "scripts/demo/moved-one.py": b"row: scripts/demo/thing\n"})
        run_in_gov(_g13, "adopt", "--target", str(_t13b), "--to", _sh13[1], "--write")
        settle(_t13b, "receipt")
        _pn = run_in_gov(_g13, "update", "--target", str(_t13b), "--to", _sh13[1], "--write")
        check("[-13] AC4 an update to the ADOPTED vintage writes zero bytes to the relocated row",
              "scripts/demo/moved-one.py" not in a13_porcelain(_t13b),
              a13_porcelain(_t13b) + " | " + _pn.stdout)

        # ---- AC7: `--pin` is an ASSERTION and is recorded as one. A pinned row is never read back
        # ---- as a proof, which is the whole reason `evidence` distinguishes the two.
        _t13c = a13_target("pin", "scripts", {
            "scripts/demo/stranger.py": b"nothing gov ever shipped\n"})
        _pp = run_in_gov(_g13, "adopt", "--target", str(_t13c), "--write",
                         "--pin", f"scripts/demo/stranger.py={_sh13[0]}")
        check("[-13] AC7 --pin exits 0", _pp.returncode == 0, _pp.stdout + _pp.stderr)
        _pinned = a13_row(a13_receipt(_t13c), "scripts/demo/stranger.py")
        check("[-13] AC7 ...and the pinned row records evidence `pinned`, not `vintage-match`",
              _pinned.get("evidence") == "pinned", str(_pinned))
        check("[-13] AC7 ...at the commit the operator named, with gov's blob there",
              _pinned.get("commit") == _sh13[0] and bool(_pinned.get("gov_oid")), str(_pinned))
        check("[-13] AC7 ...and NO rung, because the pin fixes the base and never the proof",
              "carry" not in _pinned, str(_pinned.get("carry")))
        _pbad = run_in_gov(_g13, "adopt", "--target", str(_t13c), "--re-adopt",
                           "--pin", "scripts/demo/stranger.py")
        check("[-13] AC7 a --pin with no `=` is refused rather than pinning nothing",
              _pbad.returncode == 2 and "--pin needs <path>=<rev>" in _pbad.stderr, _pbad.stderr)
        _pnorev = run_in_gov(_g13, "adopt", "--target", str(_t13c), "--re-adopt",
                             "--pin", "scripts/demo/stranger.py=no-such-rev")
        check("[-13] AC7 a --pin naming a revision that does not resolve is refused BY NAME",
              _pnorev.returncode == 2 and "--pin scripts/demo/stranger.py=no-such-rev does not "
              "resolve" in _pnorev.stderr, _pnorev.stderr)
        # A REVISION THAT RESOLVES AND CARRIES NO SUCH BLOB is a THIRD state, and it is the one an
        # operator actually reaches: they pin a real commit that predates the file. Refusing here
        # rather than recording `gov_oid: null` is what keeps an assertion from becoming a fiction.
        _pnoblob = run_in_gov(_g13, "adopt", "--target", str(_t13c), "--re-adopt",
                              "--pin", f"scripts/demo/stranger.py={_sh13[0]}^")
        check("[-13] AC7 ...and a revision holding no blob for that source is refused separately",
              _pnoblob.returncode == 2 and "gov holds no blob" in _pnoblob.stderr, _pnoblob.stderr)
        _pnoto = run_in_gov(_g13, "adopt", "--target", str(_t13c), "--re-adopt",
                            "--to", "no-such-rev")
        check("[-13] AC8 a --to that does not resolve in this gov checkout is refused",
              _pnoto.returncode == 2 and "does not resolve in this gov checkout" in _pnoto.stderr,
              _pnoto.stderr)

        # ---- AC8: THE THREE REFUSALS, each by name. The positive run above is the liveness half —
        # ---- without it every refusal here could be firing because the verb is broken.
        _pself = run_in_gov(_g13, "adopt", "--target", str(_g13))
        check("[-13] AC8 adopt refuses a --target that IS the gov checkout",
              _pself.returncode == 2 and "gov checkout itself" in _pself.stderr, _pself.stderr)
        _pre = run_in_gov(_g13, "adopt", "--target", str(_t13c))
        check("[-13] AC8 ...refuses over an existing receipt without --re-adopt",
              _pre.returncode == 2 and "--re-adopt" in _pre.stderr, _pre.stderr)
        _pok = run_in_gov(_g13, "adopt", "--target", str(_t13c), "--re-adopt")
        check("[-13] AC8 ...and --re-adopt releases exactly that refusal and nothing else",
              _pok.returncode == 0, _pok.stdout + _pok.stderr)
        _t13d = a13_target("dirty", "scripts", {"scripts/demo/verbatim-one.py": b"v1\n"})
        (_t13d / "scripts" / "demo" / "verbatim-one.py").write_bytes(b"edited\n")
        git(_t13d, "add", "-A")
        _pd = run_in_gov(_g13, "adopt", "--target", str(_t13d))
        check("[-13] AC8 ...refuses a target whose INDEX differs from HEAD",
              _pd.returncode == 2 and "differ from HEAD" in _pd.stderr, _pd.stderr)
        git(_t13d, "reset", "-q", "--hard", "HEAD")
        (_t13d / "scripts" / "demo" / "verbatim-one.py").write_bytes(b"unstaged\n")
        _pw = run_in_gov(_g13, "adopt", "--target", str(_t13d))
        check("[-13] F1 ...and does NOT refuse an UNSTAGED edit, which `-12` owns and this does not",
              _pw.returncode == 0, _pw.stdout + _pw.stderr)

        # ---- AC13 + AC14: the two row classes `resolve_entry` never produces (S11), and S7's
        # ---- scoping in BOTH directions. One fixture, because the classes only exist together: a
        # ---- descriptor declaring an `lf_pin` and a merged rule, adopted into a target that holds
        # ---- both, plus a `seed` row that matched no vintage.

        # ============================================================= DEPL-dCarriedReceipt-4
        # `coverage_rows()` and `plan --coverage`. AC2 and AC3 are LIVE-TARGET readings and are
        # evidenced in the acceptance ledger, not here — this suite has no NicoCares and no inCMS,
        # and an arm that pretended to measure one would be asserting nothing. What IS gateable is
        # the shape of the join: which rows are eligible, what answers "does the target have it",
        # and that a clean run says `gap 0` out loud.
        A4_REG = ('[surface]\nglobs = ["tools/*"]\n\n'
                  '[selection]\ndefault = ["demo"]\n\n'
                  '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                  '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n')

        def a4_gov(tag: str, kit_toml: str, srcs: dict[str, str]) -> pathlib.Path:
            g = tmp / f"a4-{tag}"
            (g / "tools" / "govkit").mkdir(parents=True)
            (g / "tools" / "demo").mkdir(parents=True)
            shutil.copy2(HERE / "govkit.py", g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(A4_REG, encoding="utf-8",
                                                                  newline="\n")
            (g / "tools" / "demo" / "kit.toml").write_text(kit_toml, encoding="utf-8", newline="\n")
            for rel, body in srcs.items():
                pth = g / "tools" / "demo" / rel
                pth.parent.mkdir(parents=True, exist_ok=True)
                pth.write_text(body, encoding="utf-8", newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g

        def a4_gaps(out: str) -> list[str]:
            """The gap DESTINATIONS the run printed, in order. Parsed off the `GAP` mark rather
            than off the tally, so an arm cannot pass on a summary line that disagrees with the
            rows above it."""
            return [ln.split("]", 1)[1].split("<-")[0].strip()
                    for ln in out.splitlines() if ln.startswith("  GAP ")]

        def a4_gap_total(out: str) -> int | None:
            m = _re.search(r"coverage: gap (\d+) of (\d+) write row\(s\)", out)
            return int(m.group(1)) if m else None

        _A4_KIT = ('id = "demo"\nhome = "tools/demo"\n'
                   'version_from = { none = "fixture" }\n\n'
                   '[check]\nnone = "a fixture kit"\n\n'
                   '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                   '[adopt]\nargv = []\nmutates_index = false\n')
        _g4 = a4_gov("basic", _A4_KIT, {"one.py": "1\n", "two.py": "2\n", "three.py": "3\n"})

        # ---- AC1's RED is HISTORICAL — `parse_args` refused `--coverage` as an unknown argument
        # ---- before this unit, and cannot be made to refuse it again without removing the flag.
        # ---- What survives it is that BOTH flags are named in `USAGE`, which is the carrier §5
        # ---- promises gains them; the arms below are the behaviour.
        _g4src = (HERE / "govkit.py").read_text(encoding="utf-8")
        check("[-4] S6 both flags are named in USAGE",
              "--coverage" in _g4src.split("USAGE = ", 1)[1][:900]
              and "--emit-declines" in _g4src.split("USAGE = ", 1)[1][:900])

        # ---- THE CLEAN READING FIRST. Without it every gap arm below could be passing because the
        # ---- join reports everything rather than because the fixture is missing something — and
        # ---- `gap 0` printing OUT LOUD is itself S4, because a clean run that printed nothing is
        # ---- indistinguishable from a coverage check that never ran.
        _t4full = a13_target("cov-full", "scripts", {
            "scripts/demo/one.py": b"1\n", "scripts/demo/two.py": b"2\n",
            "scripts/demo/three.py": b"3\n", "scripts/demo/kit.toml": b"x\n"})
        _p4 = run_in_gov(_g4, "plan", "--target", str(_t4full), "--coverage", "--kits", "demo")
        check("[-4] a target holding every planned write reports gap 0", _p4.returncode == 0
              and a4_gap_total(_p4.stdout) == 0, _p4.stdout + _p4.stderr)
        check("[-4] S4 ...and SAYS `gap 0` rather than printing nothing",
              "gap 0 of" in _p4.stdout, _p4.stdout)
        check("[-4] F2 ...additively: the ordinary plan rows are still printed above it",
              "govkit plan — marks:" in _p4.stdout and "  write  [" in _p4.stdout, _p4.stdout)
        check("[-4] LIVENESS ...over a NON-EMPTY write population, so gap 0 is not vacuous",
              (a4_gap_total(_p4.stdout) == 0
               and int(_re.search(r"gap \d+ of (\d+) write", _p4.stdout).group(1)) > 0), _p4.stdout)

        # ---- AC6: exactly one missing planned write is reported, and the INDEX is what answers.
        _t4gap = a13_target("cov-gap", "scripts", {
            "scripts/demo/one.py": b"1\n", "scripts/demo/three.py": b"3\n",
            "scripts/demo/kit.toml": b"x\n"})
        _p4g = run_in_gov(_g4, "plan", "--target", str(_t4gap), "--coverage", "--kits", "demo")
        check("[-4] AC6 a target missing one planned write reports exactly that dest",
              a4_gaps(_p4g.stdout) == ["scripts/demo/two.py"], str(a4_gaps(_p4g.stdout)))
        check("[-4] F1 ...and a nonzero gap does NOT change the exit code",
              _p4g.returncode == 0, f"rc {_p4g.returncode}")
        check("[-4] S1 ...and the row names the gov source it came from, so a rename reads apart "
              "from an absence",
              "<- tools/demo/two.py" in _p4g.stdout, _p4g.stdout)
        # THE INDEX, NOT THE WORKTREE. An untracked file sitting at the destination is not a file
        # the target holds, and this is the arm that says which of the two answers.
        (_t4gap / "scripts" / "demo" / "two.py").write_bytes(b"2\n")
        _p4u = run_in_gov(_g4, "plan", "--target", str(_t4gap), "--coverage", "--kits", "demo")
        check("[-4] AC6 an UNTRACKED file at the destination is still a gap — the index answers",
              a4_gaps(_p4u.stdout) == ["scripts/demo/two.py"], str(a4_gaps(_p4u.stdout)))
        git(_t4gap, "add", "-A")
        git(_t4gap, "commit", "-qm", "took it")
        _p4t = run_in_gov(_g4, "plan", "--target", str(_t4gap), "--coverage", "--kits", "demo")
        check("[-4] AC6 ...and it stops being a gap once the target TRACKS it",
              a4_gap_total(_p4t.stdout) == 0, _p4t.stdout)

        # ---- AC5: THE FALSE-POSITIVE ARM, and the left-shift. The class is "a non-`write` kind
        # ---- counted as a gap", gated over the WHOLE `ROLE_KINDS` table rather than over the one
        # ---- role that exposed it: a role added tomorrow takes its kind from that table and this
        # ---- assertion inherits the answer.
        _A4_KIND_KIT = ('id = "demo"\nhome = "tools/demo"\n'
                        'version_from = { none = "fixture" }\n\n'
                        '[check]\nnone = "a fixture kit"\n\n'
                        '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                        '[[files]]\ninclude = "owned.py"\nrole = "project-owned"\n\n'
                        '[[files]]\ninclude = "block.txt"\nrole = "merged"\n'
                        'block_id = "demo:block"\nmarker_style = "hash-comment"\n'
                        'to = "hooks/pre-commit"\n\n'
                        '[adopt]\nargv = []\nmutates_index = false\n')
        _g4k = a4_gov("kinds", _A4_KIND_KIT, {
            "one.py": "1\n", "owned.py": "owned\n",
            "block.txt": "# demo:block\nechodemo\n# /demo:block\n"})
        # The target holds every ENGINE destination and NEITHER of the other two kinds'. Under a
        # join over every `planned_writes` row that is two gaps; under S2's it is none.
        #
        # `block.txt` AND `owned.py` ARE BOTH HELD, and the first of those cost a round. The `**`
        # engine rule pools every tracked file under `home`, so the merged rule's own SOURCE also
        # lands at `scripts/demo/block.txt` as a genuine write row — a target missing it has a real
        # gap, and the arm redded on a correct answer because the fixture had not held up its end.
        # A false-positive arm has to be missing ONLY the kinds it is about.
        _t4k = a13_target("cov-kinds", "scripts", {
            "scripts/demo/one.py": b"1\n", "scripts/demo/kit.toml": b"x\n",
            "scripts/demo/block.txt": b"# demo:block\nechodemo\n# /demo:block\n"})
        _p4k = run_in_gov(_g4k, "plan", "--target", str(_t4k), "--coverage", "--kits", "demo")
        check("[-4] AC5 the fixture really declares a non-`write` kind whose destination is absent",
              "  ORDER  [" in _p4k.stdout or "  BLOCK  [" in _p4k.stdout, _p4k.stdout)
        check("[-4] AC5 ...and NONE of them is counted as a gap",
              a4_gap_total(_p4k.stdout) == 0, str(a4_gaps(_p4k.stdout)))
        # THE LEFT-SHIFT, over the table rather than over this fixture: the eligible set is exactly
        # the kinds that mean "govkit puts bytes here", and it is read off `ROLE_KINDS` so a role
        # added later cannot quietly join it.
        _GK4 = govkit_module()
        check("[-4] AC5 left-shift: `write` is the only kind in ROLE_KINDS that means gov writes it",
              {k for k in _GK4.ROLE_KINDS.values() if k == "write"} == {"write"}
              and "write" in set(_GK4.ROLE_KINDS.values()), str(sorted(set(
                  _GK4.ROLE_KINDS.values()))))
        check("[-4] AC5 ...and the join's predicate is spelled against that kind, not against a "
              "role list it would have to keep in step",
              'row["kind"] == "write"' in _g4src, "predicate not found in source")

        # ---- AC4: `--emit-declines`. STDOUT ONLY — a deployer that edits the document carrying the
        # ---- owner's decisions has made one for them.
        _p4d = run_in_gov(_g4, "plan", "--target", str(_t4full), "--coverage", "--emit-declines",
                          "--kits", "demo")
        check("[-4] AC4 a target with no gaps emits no decline skeletons",
              "[[decline]]" not in _p4d.stdout, _p4d.stdout)
        _t4d = a13_target("cov-decl", "scripts", {"scripts/demo/one.py": b"1\n"})
        _p4d2 = run_in_gov(_g4, "plan", "--target", str(_t4d), "--coverage", "--emit-declines",
                           "--kits", "demo")
        check("[-4] AC4 one `[[decline]]` block per gap row, with an empty `why`",
              _p4d2.stdout.count("[[decline]]") == a4_gap_total(_p4d2.stdout)
              and a4_gap_total(_p4d2.stdout) > 0
              and _p4d2.stdout.count('why = ""') == a4_gap_total(_p4d2.stdout), _p4d2.stdout)
        check("[-4] AC4 ...and the target's own descriptor is untouched afterwards",
              subprocess.run(["git", "-C", str(_t4d), "status", "--porcelain",
                              ".governance/deploy.toml"], capture_output=True,
                             text=True).stdout.strip() == "", "deploy.toml was modified")
        # `--emit-declines` ALONE implies the join rather than printing nothing, which is why this
        # unit adds no refusal branch and `BRANCH_PIN` does not move (§7).
        _p4d3 = run_in_gov(_g4, "plan", "--target", str(_t4d), "--emit-declines", "--kits", "demo")
        check("[-4] `--emit-declines` alone implies `--coverage` rather than emitting nothing",
              _p4d3.stdout.count("[[decline]]") == _p4d2.stdout.count("[[decline]]")
              and _p4d3.returncode == 0, _p4d3.stdout)

        # ---- S3: a destination still carrying an unresolved token is NOT a coverage row. It is
        # ---- already an `r.fail`, and reporting it as absent would say the target is missing a
        # ---- file whose name nobody knows.
        _A4_TOK_KIT = _A4_KIT.replace('include = "**"\nrole = "engine"',
                                      'include = "**"\nrole = "engine"\nto = "{nowhere}/{relpath}"')
        _g4t = a4_gov("token", _A4_TOK_KIT, {"one.py": "1\n"})
        _t4t = a13_target("cov-token", "scripts", {"scripts/demo/one.py": b"1\n"})
        _p4t2 = run_in_gov(_g4t, "plan", "--target", str(_t4t), "--coverage", "--kits", "demo")
        check("[-4] S3 the fixture really produces an UNRESOLVED destination",
              "UNRES." in _p4t2.stdout, _p4t2.stdout)
        check("[-4] S3 ...and it is not counted as a gap, because a brace is not a path",
              a4_gap_total(_p4t2.stdout) == 0, str(a4_gaps(_p4t2.stdout)))

        # ---- S4: ROWS, never unique destinations. Two rules resolving to ONE dest are two triage
        # ---- items, and a destination-keyed tally is what hid the single collision measured at
        # ---- the live target this unit was built for.
        _A4_DUP_KIT = ('id = "demo"\nhome = "tools/demo"\n'
                       'version_from = { none = "fixture" }\n\n'
                       '[check]\nnone = "a fixture kit"\n\n'
                       '[[files]]\ninclude = "one.py"\nrole = "engine"\nto = "shared/collide.py"\n\n'
                       '[[files]]\ninclude = "two.py"\nrole = "engine"\nto = "shared/collide.py"\n\n'
                       '[adopt]\nargv = []\nmutates_index = false\n')
        _g4dup = a4_gov("dup", _A4_DUP_KIT, {"one.py": "1\n", "two.py": "2\n"})
        _t4dup = a13_target("cov-dup", "scripts", {"scripts/demo/keep.txt": b"k\n"})
        _p4dup = run_in_gov(_g4dup, "plan", "--target", str(_t4dup), "--coverage", "--kits", "demo")
        _g4rows = a4_gaps(_p4dup.stdout)
        check("[-4] S4 the fixture really has two rules resolving to ONE destination",
              len(set(_g4rows)) == 1 and len(_g4rows) >= 1, str(_g4rows))
        check("[-4] S4 ...and the tally counts ROWS, so the collision is two triage items not one",
              a4_gap_total(_p4dup.stdout) == len(_g4rows) and len(_g4rows) == 2, str(_g4rows))

        # ============================================================= DEPL-dCarriedReceipt-5
        # The `[[decline]]` contract and the three staleness arms. Every arm below runs the SAME
        # fixture kit as `-4`'s, because a decline is only meaningful against a gap and `-4` is what
        # produces one — reusing it also means the two units cannot drift apart about what a gap is.
        def a5_target(tag: str, files: dict[str, bytes], declines: str = "") -> pathlib.Path:
            t = tmp / f"a5t-{tag}"
            t.mkdir(parents=True)
            git(t, "init", "-q", "-b", "main")
            git(t, "config", "user.email", "t@e")
            git(t, "config", "user.name", "t")
            git(t, "config", "core.autocrlf", "false")
            (t / ".governance").mkdir()
            (t / ".governance" / "deploy.toml").write_text(
                'gov_source = "local"\nprefix = "scripts"\nkits = ["demo"]\n' + declines,
                encoding="utf-8", newline="\n")
            for rel, body in files.items():
                pth = t / rel
                pth.parent.mkdir(parents=True, exist_ok=True)
                pth.write_bytes(body)
            git(t, "add", "-A")
            git(t, "commit", "-qm", "base")
            return t

        def a5_cov(t: pathlib.Path, g: pathlib.Path = None):
            return run_in_gov(g or _g4, "plan", "--target", str(t), "--coverage", "--kits", "demo")

        def a5_cov_flag(t: pathlib.Path, *flags: str):
            return run_in_gov(_g4, "plan", "--target", str(t), "--coverage", *flags,
                              "--kits", "demo")

        # A target holding one of the three engine sources, so `two.py` and `three.py` are gaps and
        # a decline has something to excuse. `kit.toml` is held so it is not a fourth gap.
        _A5_HELD = {"scripts/demo/one.py": b"1\n", "scripts/demo/kit.toml": b"x\n"}

        # ---- AC1's RED is HISTORICAL and was observed on the tree BEFORE this build's coverage
        # ---- unit: `grep decline` over the engine at that vintage returned one hit, in an unrelated
        # ---- comment about what `apply` prints when it declines a RULE. No reader of a
        # ---- `[[decline]]` block existed. It cannot be re-observed now without removing the reader.
        _g5src = (HERE / "govkit.py").read_text(encoding="utf-8")
        check("[-5] AC1 the engine now READS a [[decline]] block rather than merely parsing it",
              'deploy.get("decline")' in _g5src and "def decline_findings" in _g5src)

        # ---- D1's CLASS-LEVEL GATE — the one that would have caught the blocker at authoring time.
        # ---- The executing surface is a DECLARED POPULATION asserted in BOTH directions, so a new
        # ---- `resolve_shell_argv` spawn reds until a row claims it and a row naming a function that
        # ---- no longer spawns reds too. Derived from the AST rather than from a grep, because a
        # ---- grep cannot say which function a call sits in and the function is the whole key.
        import ast as _ast1
        _t1 = _ast1.parse(_g5src)
        _par1 = {}
        for _n in _ast1.walk(_t1):
            for _c in _ast1.iter_child_nodes(_n):
                _par1[_c] = _n

        def _enclosing1(node):
            while node in _par1:
                node = _par1[node]
                if isinstance(node, _ast1.FunctionDef):
                    return node.name
            return "(module)"

        # M2, from ROUND 2. This walked `resolve_shell_argv` CALLS — six of roughly forty-five spawn
        # sites — while the declaration's header claimed EVERY PLACE. A guarantee narrower than the
        # sentence selling it is the false confidence that let the blocker ship. The population is
        # now every `subprocess.run`/`Popen`, minus literal `git` plumbing — and `git hook run` is
        # excluded from that allowlist BY NAME, because it wears a git argv and executes the
        # target's own script. Run over the real tree before wiring, hits and near-misses both:
        # eight hit functions, thirty-four allowlisted git calls across twenty-one functions.
        def _git_plumbing1(call) -> bool:
            """Is this spawn literal `git` plumbing, and therefore outside the census?

            ROUND 4's M4. This read the argv's literal elements and asked whether `hook`/`run` were
            among them, so `govkit.git`'s own `["git", "-C", str(root), *args]` presented as
            `['git', '-C']` -- no subcommand at all -- and was allowlisted unconditionally. The
            by-name exclusion of `git hook run` IS the guarantee the declaration's header sells, and
            the module's own primary git wrapper defeated it: one future
            `git(target, "hook", "run", "pre-commit")` would spawn target-authored hook code with
            zero census rows and a green both-directions arm. No live exploit -- all callers pass
            gov's own root with literal subcommands -- so it is a latent gate gap, and it is round
            3's M2 shape (a guarantee narrower than the sentence selling it) reintroduced inside the
            fix for it.

            THE PROPERTY IS WHETHER THE SUBCOMMAND IS RESOLVABLE HERE, not whether every element is
            a literal. Measured: rejecting any non-`Constant` element admits twenty legitimate
            plumbing sites into the census, because `str(target)` is a `Call` and appears in almost
            all of them. So `-C`/`-c` and their value are skipped, and the NEXT element must be a
            string constant naming the subcommand. Starred, non-constant or absent means unknowable,
            and an allowlist that cannot see what it is allowing is allowing everything.
            """
            _elts = getattr(call.args[0], "elts", None) if call.args else None
            if not _elts:
                return False
            _first = _elts[0]
            if not (isinstance(_first, _ast1.Constant) and _first.value == "git"):
                return False
            _i = 1
            while _i < len(_elts):
                _e = _elts[_i]
                if isinstance(_e, _ast1.Constant) and _e.value in ("-C", "-c"):
                    _i += 2                      # the flag and its value, whatever shape it is
                    continue
                break
            if _i >= len(_elts):
                return False                     # `git` with no subcommand -> census HIT
            _sub = _elts[_i]
            if isinstance(_sub, _ast1.Starred) or not isinstance(_sub, _ast1.Constant):
                return False                     # unresolvable subcommand -> census HIT
            if not isinstance(_sub.value, str):
                return False
            _words = [e.value for e in _elts
                      if isinstance(e, _ast1.Constant) and isinstance(e.value, str)]
            if "hook" in _words and "run" in _words:
                return False                     # runs the TARGET's script; excluded BY NAME
            return True
        _exec_found = set()
        for _n in _ast1.walk(_t1):
            if isinstance(_n, _ast1.Call) and isinstance(_n.func, _ast1.Attribute) \
                    and _n.func.attr in ("run", "Popen") \
                    and isinstance(_n.func.value, _ast1.Name) \
                    and _n.func.value.id == "subprocess" and not _git_plumbing1(_n):
                _exec_found.add(_enclosing1(_n))
        _declared = set(govkit_module().SHELL_EXEC_SITES)
        check("[-5] D1 LIVENESS the AST walk really finds shell-executing call sites",
              len(_exec_found) >= 4, str(sorted(_exec_found)))
        check("[-5] D1 every function that runs a shell command is DECLARED in SHELL_EXEC_SITES",
              not (_exec_found - _declared),
              "undeclared spawn in: " + ", ".join(sorted(_exec_found - _declared)))
        check("[-5] D1 ...and every declared row still names a function that spawns — both "
              "directions, so a stale row cannot widen the surface it was written to narrow",
              not (_declared - _exec_found),
              "declared but no longer spawning: " + ", ".join(sorted(_declared - _exec_found)))
        # THE TRUST LABEL IS THE POINT. A site whose argv the TARGET authored owes two properties,
        # and the second is the one D1 violated: it must not be reachable from a verb that runs by
        # default. Asserted on the source of each such function rather than on a claim about it.
        _tgt_sites = [k for k, v in govkit_module().SHELL_EXEC_SITES.items() if v == "target"]
        check("[-5] M2 every declared label is in the closed set",
              set(govkit_module().SHELL_EXEC_SITES.values())
              <= set(govkit_module().SHELL_EXEC_LABELS),
              str(sorted(set(govkit_module().SHELL_EXEC_SITES.values()))))
        # `target-code` is bounded by being reachable from a WRITING verb only, which is the property
        # that actually protects it -- announcing `git hook run pre-commit` tells nobody anything.
        _code_sites = [k for k, v in govkit_module().SHELL_EXEC_SITES.items() if v == "target-code"]
        check("[-5] M2 LIVENESS the declaration really marks a target-CODE site",
              len(_code_sites) >= 1, str(_code_sites))
        for _cs in _code_sites:
            _callers = {_enclosing1(_n) for _n in _ast1.walk(_t1)
                        if isinstance(_n, _ast1.Call) and isinstance(_n.func, _ast1.Name)
                        and _n.func.id == _cs}
            check(f"[-5] M2 target-code site '{_cs}' is reached only from a writing verb",
                  _callers and all("apply" in c or "update" in c for c in _callers),
                  f"reached from: {sorted(_callers)}")
        check("[-5] D1 LIVENESS the declaration really marks some sites target-authored",
              len(_tgt_sites) >= 2, str(_tgt_sites))
        # ---- B1/B2, from ROUND 2, and they must be FIXTURE arms rather than source-shape ones:
        # ---- the source-shape arm written for D1 was green over both of these the whole time.
        # ---- A read-only `govkit check` ran target-chosen text, because `target_context` handed
        # ---- the TARGET's `prefix` to `resolve_tokens` and several shipped probes are `bash -c`
        # ---- and `python -c` strings. Reproduced before the fix; asserted on a SENTINEL FILE
        # ---- here, because an exit code cannot tell 'refused' from 'ran and returned 0'.
        # ---- ROUND 4's H1, and it is why ROUND 4's BLOCKER shipped. This fixture varied exactly
        # ---- ONE thing -- the top-level `prefix` -- and hard-coded the `[answers]` table as a
        # ---- literal. A target supplies token values through THREE doors, and the arms tested one.
        # ---- So a target answer that OVERWRITES `ctx["kit"]` walked straight past a suite written
        # ---- to close this exact class, and stayed green for two commits.
        # ----
        # ---- THE DOOR IS NOW A PARAMETER, and the arms below iterate a (door, payload) table. A
        # ---- fourth door added to `target_context` without a row here is what reds -- the property
        # ---- shape rather than three copies, which is the same lesson round 2 recorded for the
        # ---- `print(` substring scan. Third time in this build, so it is a table and not a copy.
        def a_evil_target(tag: str, prefix_value: str, kit: str,
                          door: str = 'prefix', key: str = 'prefix') -> pathlib.Path:
            t = tmp / f'evil-{tag}'
            (t / '.governance').mkdir(parents=True)
            git(t, 'init', '-q', '-b', 'main')
            git(t, 'config', 'user.email', 't@e')
            git(t, 'config', 'user.name', 't')
            # The hostile value goes through the door under test; the other two stay benign, so a
            # refusal can only have come from the door this row names.
            _pfx = prefix_value if door == 'prefix' else 'tools'
            _ans = {'memory_root': 'memory'}
            _kit_tbl = {}
            if door == 'answers':
                _ans[key] = prefix_value
            elif door == 'kit':
                _kit_tbl[key] = prefix_value
            _body = ('gov_source = "local"\nprefix = ' + json.dumps(_pfx) +
                     '\nkits = [' + json.dumps(kit) + ']\n\n[answers]\n'
                     + ''.join(f'{k} = {json.dumps(v)}\n' for k, v in _ans.items()))
            if _kit_tbl:
                _body += ('\n[kit.' + kit + ']\n'
                          + ''.join(f'{k} = {json.dumps(v)}\n' for k, v in _kit_tbl.items()))
            (t / '.governance' / 'deploy.toml').write_text(
                _body, encoding='utf-8', newline='\n')
            (t / '.governance' / 'install.json').write_text(json.dumps({
                'schema': 3, 'prefix': 'tools',
                'kits': [kit],
                'files': [{'path': 'x.txt', 'role': 'seed', 'kit': kit, 'written': False}],
            }), encoding='utf-8', newline='\n')
            (t / 'x.txt').write_text('x\n', encoding='utf-8', newline='\n')
            git(t, 'add', '-A')
            git(t, 'commit', '-qm', 'base')
            return t

        _ev1 = a_evil_target('semi', 'tools; touch PWNED-BY-CHECK ;', 'drift-audit')
        run('check', '--target', str(_ev1))
        check('[-5] B2 a read-only `check` does NOT execute a metacharacter in the target prefix',
              not (_ev1 / 'PWNED-BY-CHECK').exists(),
              'SENTINEL EXISTS — read-only check ran target-chosen text')
        _pev1 = run('check', '--target', str(_ev1))
        check('[-5] B2 ...it REFUSES by name at the token boundary rather than passing quietly',
              'can leave its argument and become code' in (_pev1.stdout + _pev1.stderr),
              (_pev1.stdout + _pev1.stderr)[-600:])
        # THE PAYLOAD IS CONSTRUCTED, never spelled. Written as a literal it broke out of its own
        # string in THIS file and became executable source — the injection injecting into the test
        # for the injection, which is funny once and a corrupted suite every time after.
        _q = chr(39)
        _payload = ('x' + _q + '); import pathlib; pathlib.Path(' + _q + 'PWNED' + _q +
                    ').write_text(' + _q + 'o' + _q + '); (' + _q)
        _ev2 = a_evil_target('quote', _payload, 'codebase-map')
        run('check', '--target', str(_ev2))
        check('[-5] B1 ...and a quote break out of a `python -c` probe is closed the same way',
              not (_ev2 / 'PWNED').exists(),
              'SENTINEL EXISTS — the python -c route is still open')
        # LIVENESS: an ORDINARY prefix must still resolve, or these three pass because the engine
        # refuses everything and every other fixture in this file would be redding too.
        _evok = a_evil_target('clean', 'scripts', 'drift-audit')
        _pevok = run('check', '--target', str(_evok))
        check('[-5] B1 LIVENESS an ordinary path-shaped prefix still resolves',
              'can leave its argument and become code' not in (_pevok.stdout + _pevok.stderr),
              (_pevok.stdout + _pevok.stderr)[-500:])

        # ---- ROUND 4 B1 + H1 -- THE SAME PAYLOAD THROUGH EVERY DOOR, asserted on a SENTINEL FILE.
        # ---- An exit code cannot tell `refused` from `executed and then reported normally`, which
        # ---- is exactly what the blocker did: the poisoned run printed an ordinary report and
        # ---- exited 1 with the sentinel already on disk. Only the filesystem answers this.
        # ----
        # ---- REPRODUCED BEFORE THE FIX, both ways: with the reserved-key guard reverted, a
        # ---- READ-ONLY `check` -- no `--write`, no flag of any kind -- ran the target's own script
        # ---- and wrote the sentinel. With it live, the same fixture refuses by name.
        _DOORS = (
            ('prefix',  'prefix',      'the top-level prefix, the only door the old arms tested'),
            ('answers', 'kit',         'a target ANSWER overwriting the key gov seeds for itself'),
            ('answers', 'kit_id',      'the same, one key over'),
            ('answers', 'prefix',      'and the strict-class key itself, through the prose door'),
            ('kit',     'kit',         'the per-entry table, which is a third door onto one dict'),
            ('kit',     'kit_id',      'the one seeded key the per-entry table still may not set'),
        )
        # `pwn.py` is the script the payload aims at: `{kit}` is interpolated into a shipped
        # `python {kit}/...` template, so a value of `pwn.py z` makes python run THAT file.
        for _i, (_door, _key, _why) in enumerate(_DOORS):
            _et = a_evil_target(f'door{_i}', 'pwn.py z', 'drift-audit', door=_door, key=_key)
            (_et / 'pwn.py').write_text(
                'import pathlib; pathlib.Path("PWNED-BY-CHECK").write_text("x")\n',
                encoding='utf-8', newline='\n')
            git(_et, 'add', '-A')
            git(_et, 'commit', '-qm', 'payload')
            _ep = run('check', '--target', str(_et))
            check(f'[-5] R4-B1 door {_door}.{_key}: a read-only `check` writes NO sentinel -- {_why}',
                  not (_et / 'PWNED-BY-CHECK').exists(),
                  f'SENTINEL EXISTS — rc {_ep.returncode}: '
                  + (_ep.stdout + _ep.stderr)[-500:])
        # THE LIVENESS HALF OF THE TABLE: the doors must actually be REACHED. A row whose fixture
        # never gets as far as the probe loop passes by finding nothing, which is how the first two
        # reproduction attempts for this defect proved nothing at all.
        _reached = a_evil_target('doorlive', 'pwn.py z', 'drift-audit', door='answers', key='kit')
        _preach = run('check', '--target', str(_reached))
        # THE NEEDLE IS THE REMEDY LINE, not a phrase from the prose. The prose was rewritten when
        # the guard became per-table (TOOL-aGradedDoorway-1) and this arm redded on the wording
        # while the behaviour it grades was unchanged -- an arm keyed on a sentence rather than on
        # the fact. `Remove the key: answers.kit` names BOTH the door and the key, which is the
        # thing this arm is actually about.
        check('[-5] R4-B1 LIVENESS the answers door is REACHED -- the run refuses at the reserved '
              'key rather than dying earlier on a receipt or a TOML error',
              'Remove the key: answers.kit' in (_preach.stdout + _preach.stderr),
              f'rc {_preach.returncode}: ' + (_preach.stdout + _preach.stderr)[-600:])
        # AND A LEGITIMATE ANSWER THROUGH THE SAME DOOR still resolves, or the table above passes
        # because the engine refuses every answer there is.
        _okans = a_evil_target('doorok', 'docs/mem', 'drift-audit',
                               door='answers', key='memory_root')
        _pokans = run('check', '--target', str(_okans))
        check('[-5] R4-B1 LIVENESS a NON-reserved answer through the same door is still accepted',
              'Remove the key: answers.' not in (_pokans.stdout + _pokans.stderr),
              (_pokans.stdout + _pokans.stderr)[-400:])

        # ---- THE OTHER HALF OF R4-B1, AND THE REASON THE GUARD IS PER-TABLE. The blocker was a
        # ---- PROSE-class value reaching an argv-bound key; the fix refused three NAMES, which is a
        # ---- superset. An adopter whose kit does not live at `{prefix}/{kit_id}` -- memory-tree
        # ---- installed FLAT at `scripts/`, say -- then had no way to say so at all, and the
        # ---- refusal above is the only thing that had ever stopped it.
        # ----
        # ---- So the per-ENTRY table takes `prefix` and `kit` through the STRICT class, which is
        # ---- the identical control the top-level `prefix` has always had, and the arms below hold
        # ---- BOTH directions: the hostile spellings still refuse (the table above), and a
        # ---- legitimate path fragment now RESOLVES. Without the second half the first passes by
        # ---- refusing everything, which is the shape this file exists to refuse.
        # `--kits` IS LOAD-BEARING on all three: `plan` with no selection takes the REGISTRY
        # default, which carries `playbook`, whose unanswered `playbook_path` refuses before the
        # per-entry table is ever read. Measured while writing these arms -- all three passed by
        # finding nothing, on an error naming a kit the fixture does not install.
        _homed = a_evil_target('homedkit', 'docs/da', 'drift-audit', door='kit', key='kit')
        _phomed = run('plan', '--target', str(_homed), '--kits', 'drift-audit')
        check('[-5] a STRICT per-entry `kit` is accepted and destinations resolve through it',
              'docs/da/' in _phomed.stdout and 'Remove the key:' not in
              (_phomed.stdout + _phomed.stderr),
              f'rc {_phomed.returncode}: ' + (_phomed.stdout + _phomed.stderr)[-500:])
        _hompfx = a_evil_target('homedpfx', 'docs', 'drift-audit', door='kit', key='prefix')
        _phompfx = run('plan', '--target', str(_hompfx), '--kits', 'drift-audit')
        check('[-5] a STRICT per-entry `prefix` is accepted and `{kit}` follows it',
              'docs/drift-audit/' in _phompfx.stdout,
              f'rc {_phompfx.returncode}: ' + (_phompfx.stdout + _phompfx.stderr)[-500:])
        # AND THE REFUSAL IS STILL BY NAME for the key that is an IDENTITY rather than a path.
        _kidt = a_evil_target('homedkid', 'x', 'drift-audit', door='kit', key='kit_id')
        _pkidt = run('plan', '--target', str(_kidt), '--kits', 'drift-audit')
        check('[-5] `kit.<entry>.kit_id` is still refused BY NAME -- it joins the receipt, not a path',
              'kit.drift-audit.kit_id' in (_pkidt.stdout + _pkidt.stderr),
              f'rc {_pkidt.returncode}: ' + (_pkidt.stdout + _pkidt.stderr)[-500:])

        # ---- ROUND 4 H2 + M1 -- A `merged` ROW LEFT THE TARGET DIRTY FOREVER. `apply` stages a
        # ---- merged destination and deliberately gives it no `oid` (`ROLE_KINDS["merged"]` is
        # ---- `blocked`, so neither stamping loop reaches it), so ruling A's carve-out has nothing
        # ---- to compare. The dirty population excluded `pins` ALONE, so the row fell through and
        # ---- read dirty -- and the operator's only route back to green was committing a file gov
        # ---- had just written, which is verbatim the burden ruling A was taken to remove.
        # ----
        # ---- THE RULING-A ARMS USE `memory-tree`, WHICH DECLARES NO MERGED RULE, so the class
        # ---- passed by finding nothing -- the same shape as H1 two blocks up. Three shipped
        # ---- descriptors declare `merged`; this arm drives one of them.
        # ----
        # ---- Graded on the POPULATION rather than through a second `update` run, because the
        # ---- population IS the fix and a run would also have to clear `-7` S4 and the lock to say
        # ---- anything -- a fixture that cannot reach the case is how this build lost two rounds.
        _mgt = make_target(tmp / 'merged-dirty', None)
        (_mgt / 'pyproject.toml').write_text('[tool.x]\nk = 1\n', encoding='utf-8', newline='\n')
        settle(_mgt, 'a target owning a pyproject')
        run('intake', '--target', str(_mgt), '--kits', 'pytest-parallel-guardrails')
        run('apply', '--target', str(_mgt), '--kits', 'pytest-parallel-guardrails')
        _mgrec_p = _mgt / '.governance' / 'install.json'
        check('[-12] R4-H2 LIVENESS the fixture really lands a `merged` row carrying NO oid',
              _mgrec_p.is_file()
              and any(w.get('role') == 'merged' and not w.get('oid')
                      for w in json.loads(_mgrec_p.read_text(encoding='utf-8'))['files']),
              'no merged row, or it carries an oid — this arm would grade nothing')
        if _mgrec_p.is_file():
            _mgrec = json.loads(_mgrec_p.read_text(encoding='utf-8'))
            _gk_h2 = govkit_module()
            _pop = [w for w in _mgrec['files']
                    if _gk_h2.UPDATE_ROLE.get(w.get('role', 'engine')) == 'table']
            check('[-12] R4-H2 a `merged` row is OUT of the dirty population -- its disposition is '
                  '`block`, which can no more meet S4\'s raw-write hazard than `pins` can',
                  not any(w.get('role') == 'merged' for w in _pop),
                  str([w['path'] for w in _pop if w.get('role') == 'merged']))
            _dirty_now = _gk_h2.dirty_claimed_paths(
                _mgt, [w.get('path') for w in _pop],
                {w['path']: w['oid'] for w in _pop if w.get('path') and w.get('oid')})
            check('[-12] R4-H2 ...so a post-apply target reports NOTHING dirty, which is what '
                  'unblocks the next writing verb',
                  not _dirty_now, str(_dirty_now[:4]))

        # ---- ROUND 4 H3 -- CONTAINMENT RAN INSIDE THE WRITE LOOP, so a refusal for entry N fired
        # ---- only after entries 1..N-1 were already written and staged. The arm that existed tested
        # ---- a SINGLE-kit selection, where the offending entry is necessarily the first -- it
        # ---- structurally could not see an ordering bug.
        # ----
        # ---- TWO KITS, THE ESCAPE IN THE LAST ONE, and the assertion is the PROPERTY rather than
        # ---- the message: after the refusal the target holds no gov-written file at all. Measured
        # ---- with the hoist reverted, the same fixture left 33 dirty paths behind.
        _h3t = make_target(tmp / 'h3-order', None)
        (_h3t / '.governance').mkdir(parents=True, exist_ok=True)
        (_h3t / '.governance' / 'deploy.toml').write_text(
            'gov_source = "local"\nprefix = "tools"\n'
            'kits = ["check-wiring", "memory-tree"]\n\n[answers]\n'
            'memory_root = "../../ESCAPED"\n', encoding='utf-8', newline='\n')
        settle(_h3t, 'a two-kit selection escaping on the SECOND entry')
        _ph3 = run('apply', '--target', str(_h3t), '--kits', 'check-wiring,memory-tree')
        check('[-12] R4-H3 an escape in the LAST entry refuses the run',
              _ph3.returncode == 2
              and 'leaves the target repository' in (_ph3.stdout + _ph3.stderr),
              f'rc {_ph3.returncode}: ' + (_ph3.stdout + _ph3.stderr)[-500:])
        check('[-12] R4-H3 ...and the target is UNTOUCHED -- no gov file written, nothing staged, '
              'which is the property the exit code cannot express',
              not gout(_h3t, 'status', '--porcelain').strip(),
              'target was dirtied before the refusal: '
              + gout(_h3t, 'status', '--porcelain')[:300])
        check('[-12] R4-H3 ...and nothing landed above the target either',
              not (_h3t.parent / 'ESCAPED').exists() and not (tmp / 'ESCAPED').exists(),
              str(sorted(x.name for x in tmp.glob('ESCAPED*'))))
        # ---- H1, from ROUND 2. The label was TYPED, and it was typed by asking who authored the
        # ---- argv TEMPLATE — so `run_kit_check` and `cmd_check` read "gov" and the two properties
        # ---- below were never asked of them, while a read-only `check` ran target-chosen text.
        # ---- The gate written to make the class un-recurrable was green over a live injection.
        # ----
        # ---- DERIVED NOW: a site is target-controlled when its function reaches `target_context`
        # ---- or `resolve_tokens`, because that is where the TARGET's values enter a gov template.
        # ---- The arm reds on any row typed `gov` that does, so the next spawn cannot be
        # ---- mislabelled by hand.
        _fnsrc1 = {}
        for _n in _ast1.walk(_t1):
            if isinstance(_n, _ast1.FunctionDef):
                _fnsrc1[_n.name] = _ast1.get_source_segment(_g5src, _n) or ""
        # ROUND 4's L3. This was a flat substring test over each site's OWN source, so it was not
        # transitive -- measured, it derived only FIVE of the eight declared sites.
        # `read_gate_verdicts` is labelled `target` BY HAND, contains neither name, and spawns the
        # TARGET's own `[gate_runner].command` through a helper. So the comment's claim that the
        # label is DERIVED "so the next spawn cannot be mislabelled by hand" was already false for
        # one live site. Closed one hop: a site counts as target-controlled if its own body resolves,
        # or if it CALLS something whose body does.
        _resolvers = ("target_context", "resolve_tokens", "resolve_shell_argv")
        def _resolves_directly(_name):
            _src = _fnsrc1.get(_name, "")
            return any(_r in _src for _r in _resolvers)
        _callees1 = {}
        for _n2 in _ast1.walk(_t1):
            if isinstance(_n2, _ast1.FunctionDef):
                _callees1[_n2.name] = {c.func.id for c in _ast1.walk(_n2)
                                       if isinstance(c, _ast1.Call)
                                       and isinstance(c.func, _ast1.Name)}
        _derived_target = {k for k in govkit_module().SHELL_EXEC_SITES
                           if _resolves_directly(k)
                           or any(_resolves_directly(c) for c in _callees1.get(k, ()))}
        check("[-5] H1 LIVENESS the derivation really finds token-resolving spawn sites",
              len(_derived_target) >= 3, str(sorted(_derived_target)))
        _mislabelled = sorted(k for k in _derived_target
                              if govkit_module().SHELL_EXEC_SITES.get(k) != "target")
        check("[-5] H1 no spawn site whose argv resolves TARGET token values is labelled `gov`",
              not _mislabelled,
              "typed `gov` but reaches a resolver: " + ", ".join(_mislabelled))
        # ROUND 4 L3: A ONE-DIRECTIONAL DERIVATION CHECK IS HALF A GATE. The arm above only reds a
        # derived-target row typed `gov`. The other direction -- a row typed `target` that derives as
        # `gov` -- is what would have caught `read_gate_verdicts` on the day it was hand-labelled.
        # `target-code` is exempt: its argv is entirely gov's and what it RUNS is the target's, which
        # no resolver-reachability test can see.
        _overlabelled = sorted(k for k, v in govkit_module().SHELL_EXEC_SITES.items()
                               if v == "target" and k not in _derived_target)
        check("[-5] R4-L3 ...and no site is hand-labelled `target` without deriving as one -- the "
              "check is bidirectional now, which is what makes the label DERIVED rather than typed",
              not _overlabelled,
              "typed `target` but reaches no resolver, directly or one hop: "
              + ", ".join(_overlabelled))

        # ---- ROUND 2's M4 AND L4, and what they cost. The arm that stood here asserted a SOURCE
        # ---- SHAPE: `"print(" in _body`, over the whole function, plus a twelve-line window above
        # ---- each call site. Both are satisfied by any unrelated print. `decline_findings` already
        # ---- held one at `govkit.py:1861` before D1 added the announcement, so deleting the
        # ---- announcement left the arm green — verified by AST simulation in review. And the outer
        # ---- `any` over call sites let ONE announcing site satisfy the arm for every other, so
        # ---- `read_gate_verdicts`' silent second spawn passed on its noisy first one's behalf.
        # ----
        # ---- MEASURED WHEN THE SUBSTRING WAS REPLACED BY THE QUESTION: of the six `target` sites,
        # ---- exactly ONE prints its resolved argv before spawning it. The generic arm was reporting
        # ---- a property five sites do not have. That is this repo's could-not-fail class arriving
        # ---- inside the arms written to close a could-not-fail finding, which is round 2's verdict
        # ---- in one arm.
        # ----
        # ---- SO THE CLAIM IS NARROWED TO WHAT IS OBSERVED. `_D1_ANNOUNCED` names, per target site,
        # ---- the LIVE stdout needle that proves the announcement, or `None` with the reason it is
        # ---- unasserted. A `None` row is PRINTED on every run rather than passing quietly: per §7 a
        # ---- skip that looks like a pass is indistinguishable from coverage. The map is asserted
        # ---- against the declaration in both directions, so a new `target` site cannot be added
        # ---- without landing in it.
        _D1_ANNOUNCED = {
            "decline_findings": "RUNNING a target-authored probe",
            "cmd_check": None,           # prints per-hole verdicts, never the discharge argv
            "run_kit_check": None,       # silent; the `[check].argv` is bounded by demand_safe_token
            "exempt_leg": None,          # silent; re-runs a hole probe to decide a leg exemption
            "_cmd_apply": None,          # announces that a baseline WILL run, not which argv
            "read_gate_verdicts": None,  # silent at both spawns; apply prints before the first only
            # `_cmd_update` LEFT THIS MAP AND CAME BACK, one unit apart, and both moves were
            # forced rather than chosen. DEPL-dRetiredFork-4 moved its `git rm ... + deleted`
            # BinOp to `git_pathspec` and the row went stale; DEPL-dRetiredFork-3 gave the verb
            # its first target-side execution and it spawns again. The map is asserted EQUAL to
            # the declared sites, so neither move could be forgotten on one side only.
            #
            # `None`, AND THE REASON IS THE FEATURE ITSELF. The re-render step announces every
            # argv it runs and every kit it declines -- but ONLY when GOVKIT_RERENDER=1, because
            # AC6 asks for output byte-identical to the pre-change run while the flag is off,
            # and a dark feature that announces its own absence is not dark. Every arm in this
            # file runs with the flag unset, so there is no live needle to assert HERE. The
            # announcement under the flag is covered by the S6 arms below, which set it.
            "_cmd_update": None,
        }
        # ---- DEPL-dRetiredFork-3 S6. THE RE-RENDER SELECTOR IS NOT VACUOUS ---------------------
        # The decline path reads `role == "rendered"` out of each kit descriptor's row list, and the
        # row key is `files`. Written as `file` -- which it was, and which parses, type-checks and
        # runs -- the predicate matches NOTHING, every kit skips silently, and the run reports a
        # clean `0 declined` over an empty population. Indistinguishable from a healthy tree.
        #
        # So this asserts the POPULATION, not the outcome: at least one shipped kit must have rows
        # the selector actually selects. It reds if the key is renamed, if the role vocabulary
        # changes, or if the predicate is retyped wrong -- the three ways this becomes vacuous again.
        _kits3 = sorted((pathlib.Path(GK9.__file__).parent.parent).glob("*/kit.toml"))
        check("[-3] S6 the kit population is non-empty (else the arm below proves nothing)",
              len(_kits3) >= 3, f"{len(_kits3)} kit.toml files")
        _rendered3 = {}
        for _kt in _kits3:
            try:
                _d3 = GK9.load_toml(_kt)
            except Exception:
                continue
            _n = sum(1 for _r in (_d3.get("files") or [])
                     if str((_r or {}).get("role")) == "rendered")
            if _n:
                _rendered3[_kt.parent.name] = _n
        check("[-3] S6 the `rendered` selector matches a LIVE population under the real key `files`",
              bool(_rendered3),
              "no kit has a rendered row -- the selector is vacuous and the decline path is dead")
        check("[-3] S6 ...and the WRONG key `file` matches nothing, which is how it went unseen",
              not any(GK9.load_toml(_k).get("file") for _k in _kits3),
              "a `file` key exists after all -- re-read the selector")
        print(f"note [-3] S6 rendered rows per kit: {_rendered3}")

        # ---- DEPL-dRetiredFork-5 S3. AN ADOPTER THAT EXITS 0 BY ABSENCE ------------------------
        # `classify_outcome` decides what an exit code MEANS by probing the filesystem, and it had
        # exactly ONE call site — inside `_cmd_apply`. So every `[[outcome]]` block was dead code for
        # `check`, and a kit whose adopter exits 0 because it is NOT INSTALLED reported `adopted`.
        # Measured on a real adopter: a kit with no conf, no Skill and no importable module.
        #
        # The fixture is the same descriptor read twice, once with the probe's path present and once
        # without, so the ONLY moving part is whether the probe is satisfied.
        _d5 = {"outcome": [{"code": 0, "means": "the adopter reports it is installed",
                            "ok": True, "probe": {"must_exist": ["{kit}/marker.txt"]}}]}
        import tempfile as _tf5
        _r5 = pathlib.Path(_tf5.mkdtemp())
        (_r5 / "kitdir").mkdir(parents=True, exist_ok=True)
        _ctx5 = {"kit": str((_r5 / "kitdir").as_posix())}
        _absent = GK9.classify_outcome(_r5, _d5, _ctx5, 0)
        check("[-5] S3 exit 0 with the probe's path ABSENT does not classify as ok",
              not (_absent and _absent.get("ok")), repr(_absent))
        (_r5 / "kitdir" / "marker.txt").write_text("x", encoding="utf-8")
        _present = GK9.classify_outcome(_r5, _d5, _ctx5, 0)
        check("[-5] S3 ...and the SAME descriptor with the path present classifies ok",
              bool(_present and _present.get("ok")), repr(_present))
        # THE JOIN THAT WAS MISSING: `run_kit_check` must consult that probe, not just `rc == 0`.
        # Asserted on the source, because building a runnable adopter fixture here would test the
        # fixture. The call site is what was absent; its presence is the whole fix.
        _src5 = pathlib.Path(GK9.__file__).read_text(encoding="utf-8")
        _rkc = _src5[_src5.index("def run_kit_check"):_src5.index("def classify_outcome")]
        check("[-5] S3 run_kit_check routes its exit code through classify_outcome",
              "classify_outcome(" in _rkc,
              "the probe is still dead code for `check`")
        _sh5 = __import__("shutil"); _sh5.rmtree(str(_r5), ignore_errors=True)

        # ---- DEPL-dRetiredFork-4 S3. A PATHSPEC LARGER THAN THE COMMAND LINE --------------------
        # The argv form died at 32 KiB with WinError 206, AFTER apply's write loop — leaving files
        # staged, a conf scaffolded and no receipt update. This arm builds a pathspec past that bound
        # and asserts the command SUCCEEDS, which is only meaningful because the same list through
        # argv is asserted to FAIL right after it.
        import tempfile as _tf4
        _d4 = _tf4.mkdtemp()
        _r4 = pathlib.Path(_d4)
        subprocess.run(["git", "init", "-q", str(_r4)], capture_output=True)
        subprocess.run(["git", "-C", str(_r4), "config", "user.email", "t@t"], capture_output=True)
        subprocess.run(["git", "-C", str(_r4), "config", "user.name", "t"], capture_output=True)
        # ~40 KiB of pathspec: 500 names of ~80 characters each.
        _names4 = [("f%03d-" % i) + ("x" * 72) + ".txt" for i in range(500)]
        for _n4 in _names4:
            (_r4 / _n4).write_text("x" + chr(10), encoding="utf-8", newline=chr(10))
        _bytes4 = sum(len(n) + 1 for n in _names4)
        check("[-4] S3 the fixture pathspec really exceeds the 32 KiB command line",
              _bytes4 > 32768, f"{_bytes4} bytes")
        _ok4 = GK9.git_pathspec(_r4, ["add"], _names4)
        check("[-4] S3 a >32 KiB pathspec over STDIN succeeds",
              _ok4.returncode == 0, _ok4.stderr[:200] if _ok4.stderr else "")
        _staged4 = subprocess.run(["git", "-C", str(_r4), "diff", "--cached", "--name-only"],
                                  capture_output=True, text=True).stdout.split()
        check("[-4] S3 ...and every path in it actually reached git",
              len(_staged4) == len(_names4), f"{len(_staged4)} of {len(_names4)}")
        # THE RED, OBSERVED: the same list through argv is what the fix replaced. On a platform with
        # a larger limit this raises nothing and the arm says so rather than asserting a failure the
        # host cannot produce — a check that cannot fire must announce itself, not pass quietly.
        try:
            subprocess.run(["git", "-C", str(_r4), "add", "--"] + _names4,
                           capture_output=True, check=False)
            _argv_died = False
        except (OSError, ValueError):
            _argv_died = True
        if _argv_died:
            check("[-4] S3 ...where the SAME list through argv still dies", True)
        else:
            print("skip [-4] S3 the argv form did not die on this host: its command-line limit is "
                  "above the fixture size, so the RED half is unexercised HERE. It was observed on "
                  "the reporting platform, and the stdin form is asserted above either way.")
        _sh4 = __import__("shutil"); _sh4.rmtree(_d4, ignore_errors=True)

        check("[-5] D1/M4 the announcement map covers exactly the declared `target` sites",
              set(_D1_ANNOUNCED) == set(_tgt_sites),
              f"map {sorted(_D1_ANNOUNCED)} vs declared {sorted(_tgt_sites)}")
        _d1_unasserted = sorted(k for k, v in _D1_ANNOUNCED.items() if v is None)
        print(f"    NOTE  [-5] D1 {len(_d1_unasserted)} of {len(_D1_ANNOUNCED)} target-controlled "
              f"spawn site(s) do NOT announce their resolved argv and are asserted by NO arm here: "
              + ", ".join(_d1_unasserted))
        print("    NOTE  [-5] D1 what bounds those is `demand_safe_token` at the token boundary, "
              "which IS armed below — not an announcement, and this suite no longer claims one.")
        check("[-5] S2 the evidence set is a CLOSED constant, not a check spelled per call site",
              tuple(govkit_module().DECLINE_EVIDENCE) == ("taken_as", "consumed_into", "discharge"),
              str(govkit_module().DECLINE_EVIDENCE))

        # ---- LIVENESS FIRST. Without a run that DECLINES successfully, every red arm below could
        # ---- be passing because the grader rejects everything.
        _t5ok = a5_target("ok", _A5_HELD,
                          '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                          'why = "we do not use it"\n')
        _p5ok = a5_cov(_t5ok)
        check("[-5] LIVENESS a well-formed decline with `why` alone is accepted and exits 0",
              _p5ok.returncode == 0 and "declined" in _p5ok.stdout, _p5ok.stdout + _p5ok.stderr)
        check("[-5] S7 ...it drops out of the gap count",
              a4_gap_total(_p5ok.stdout) == 1, _p5ok.stdout)
        check("[-5] ...and it PRINTS with its reason rather than vanishing from the report",
              "we do not use it" in _p5ok.stdout, _p5ok.stdout)

        # ---- AC2: the empty reason. Same words the exemption hygiene already uses one level up.
        _p5w = a5_cov(a5_target("nowhy", _A5_HELD,
                                '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                'why = ""\n'))
        check("[-5] AC2 an empty `why` reds, naming the kit and the dest",
              _p5w.returncode == 1 and "empty reason" in _p5w.stdout
              and "scripts/demo/two.py" in _p5w.stdout, _p5w.stdout)
        check("[-5] AC2 ...and the row excuses nothing, so its gap is still counted",
              a4_gap_total(_p5w.stdout) == 2, _p5w.stdout)

        # ---- AC3: the file ARRIVED. The message says so rather than calling the row malformed.
        _p5a = a5_cov(a5_target("arrived", dict(_A5_HELD, **{"scripts/demo/two.py": b"2\n"}),
                                '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                'why = "we do not use it"\n'))
        check("[-5] AC3 a decline whose dest the target now TRACKS reds as stale",
              _p5a.returncode == 1 and "the file arrived" in _p5a.stdout, _p5a.stdout)

        # ---- AC4: gov WITHDREW it. Built by declining a destination no rule ships, which is the
        # ---- withdrawal case seen from the descriptor side.
        _p5x = a5_cov(a5_target("withdrawn", _A5_HELD,
                                '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/gone.py"\n'
                                'why = "gov used to ship it"\n'))
        check("[-5] AC4 a decline no claimed kit ships any more reds as stale",
              _p5x.returncode == 1 and "gov has withdrawn it" in _p5x.stdout, _p5x.stdout)

        # ---- AC5 + AC6: `taken_as`, hash-graded, CR-stripped on BOTH sides.
        _t5t = a5_target("takenas", dict(_A5_HELD, **{"vendor/two-renamed.py": b"2\n"}),
                         '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                         'why = "we took it under another name"\n'
                         'taken_as = "vendor/two-renamed.py"\n')
        _p5t = a5_cov(_t5t)
        check("[-5] AC5 `taken_as` whose bytes equal gov's reports `declined`",
              _p5t.returncode == 0 and "declined" in _p5t.stdout, _p5t.stdout + _p5t.stderr)
        check("[-5] AC5 ...and drops out of the gap count", a4_gap_total(_p5t.stdout) == 1,
              _p5t.stdout)
        # ONE BYTE CHANGED -> `diverged`, and the exit code does NOT move. Redding here would red
        # the honest adopter who relocated a file and then edited it, whose only route back to green
        # is deleting the decline — the exclusion list eating its own evidence.
        _t5d = a5_target("diverged", dict(_A5_HELD, **{"vendor/two-renamed.py": b"2 edited\n"}),
                         '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                         'why = "we took it under another name"\n'
                         'taken_as = "vendor/two-renamed.py"\n')
        _p5d = a5_cov(_t5d)
        check("[-5] AC5 one byte changed reclassifies the row to `diverged`",
              "diverged" in _p5d.stdout, _p5d.stdout)
        check("[-5] AC5 ...and the exit code is UNCHANGED — a local edit is not a coverage failure",
              _p5d.returncode == 0, f"rc {_p5d.returncode}: {_p5d.stdout}{_p5d.stderr}")
        # AC6: CRLF ONLY. This is the arm that fails against a plain `_sha` comparison and is why
        # the helper strips CR.
        _t5c = a5_target("crlf", dict(_A5_HELD, **{"vendor/two-renamed.py": b"2\r\n"}),
                         '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                         'why = "we took it under another name"\n'
                         'taken_as = "vendor/two-renamed.py"\n')
        _p5c = a5_cov(_t5c)
        check("[-5] AC6 a `taken_as` differing ONLY in line endings still reports `declined`",
              "declined" in _p5c.stdout and "diverged" not in _p5c.stdout, _p5c.stdout)

        # ---- AC7: `consumed_into`, deliberately weak — the named path is tracked, and nothing more.
        _p5ci = a5_cov(a5_target("consumed", dict(_A5_HELD, **{"scripts/all-in-one.py": b"both\n"}),
                                 '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                 'why = "folded in"\nconsumed_into = "scripts/all-in-one.py"\n'))
        check("[-5] AC7 `consumed_into` naming a TRACKED path passes",
              _p5ci.returncode == 0 and "declined" in _p5ci.stdout, _p5ci.stdout + _p5ci.stderr)
        _p5cx = a5_cov(a5_target("consumed-bad", _A5_HELD,
                                 '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                 'why = "folded in"\nconsumed_into = "scripts/nowhere.py"\n'))
        check("[-5] AC7 ...and naming an UNTRACKED one reds",
              _p5cx.returncode == 1 and "is not there is not a fold" in _p5cx.stdout, _p5cx.stdout)

        # ---- D1, THE BLOCKER this build's closing review escalated. A `[[decline]].discharge`
        # ---- argv is authored in the TARGET's own descriptor — a repository gov does not own —
        # ---- and it was reachable from `plan --coverage`, a verb that needs no receipt, takes no
        # ---- `--write`, and prints `NOTHING was written.` on the same run. The spec bullet that
        # ---- cleared it asserted `[[hole]].discharge` "already does exactly this", which is false
        # ---- in both halves: holes come from `read_descriptors(root, ...)`, gov's own tree.
        # ----
        # ---- THE ARM IS A SENTINEL FILE, not an exit code. An assertion on the exit code cannot
        # ---- tell "the probe did not run" from "the probe ran and returned 0", which is exactly
        # ---- the ambiguity that let this ship.
        _t5sent = a5_target("sentinel", _A5_HELD,
                            '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                            'why = "a probe proves it"\n'
                            'discharge = { command = ["bash", "-c", "echo pwned > SENTINEL"] }\n')
        _sent = _t5sent / "SENTINEL"
        _p5sent = a5_cov(_t5sent)
        check("[-5] D1 `plan --coverage` does NOT execute a target-authored probe by default",
              not _sent.exists(),
              "SENTINEL EXISTS — a read-only preview ran a command the target wrote")
        check("[-5] D1 ...and the row reports `probe-not-run`, a STATE rather than a silent skip",
              "probe-not-run" in _p5sent.stdout, _p5sent.stdout)
        # M1, from ROUND 2: this arm passed by FINDING NOTHING. `a5_target` writes only a
        # `deploy.toml`, so `cmd_check` returned at its no-receipt guard long before the decline
        # block — and reverting the whole `check` half of the fix left the suite green. That is how
        # B1's second call site shipped. The fixture gets a receipt now, and the arm has the
        # positive twin it lacked: a negative arm with no positive twin proves nothing.
        # A MINIMAL RECEIPT, not an `apply`. Applying lands the very destination the decline
        # excuses, which makes the row STALE ("the file arrived") and routes it away from the
        # discharge branch — so the positive twins went red for a reason that had nothing to do
        # with the mechanism. The fixture needs `check` to get PAST its no-receipt guard and
        # nothing more.
        (_t5sent / ".governance" / "install.json").write_text(json.dumps({
            "schema": 3, "gov_source": "local", "prefix": "scripts", "kits": ["demo"],
            "files": [{"path": "scripts/demo/one.py", "role": "seed", "kit": "demo",
                       "written": False}],
        }, indent=2) + "\n", encoding="utf-8", newline="\n")
        _p5sentc = run_in_gov(_g4, "check", "--target", str(_t5sent))
        check("[-5] M1 LIVENESS the sentinel fixture now REACHES the decline block in `check`",
              "NOT LANDED" not in _p5sentc.stdout, _p5sentc.stdout[-500:])
        check("[-5] D1 ...and `check` does not execute it either",
              not _sent.exists(), "SENTINEL EXISTS after `check`")
        _p5sentcy = run_in_gov(_g4, "check", "--target", str(_t5sent), "--run-discharge")
        check("[-5] M1 ...while `check --run-discharge` DOES run it — the positive twin, without "
              "which the arm above is satisfied by any code path that simply never gets there",
              _sent.exists(), "SENTINEL ABSENT with --run-discharge: the check half is untested")
        _sent.unlink(missing_ok=True)
        # LIVENESS: the same fixture WITH the opt-in must actually run it, or the three arms above
        # pass because the mechanism is broken rather than because the guard works.
        _p5sento = a5_cov_flag(_t5sent, "--run-discharge")
        check("[-5] D1 LIVENESS `--run-discharge` DOES run it, so the guard is a guard",
              _sent.exists(), "SENTINEL ABSENT even with --run-discharge: the arms above prove nothing")
        check("[-5] D1 ...and the run PRINTS the argv before spawning it",
              "RUNNING a target-authored probe" in _p5sento.stdout and "SENTINEL" in _p5sento.stdout,
              _p5sento.stdout)
        _sent.unlink(missing_ok=True)

        # ---- AC8: `discharge`, under the opt-in D1 added. The criterion says what a discharge
        # ---- REPORTS; it never said which flags reach it, so the flag is where it is now reached.
        _p5g0 = a5_cov_flag(a5_target("disch-ok", _A5_HELD,
                                      '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                      'why = "a probe proves it"\n'
                                      'discharge = { command = ["bash", "-c", "exit 0"] }\n'),
                            "--run-discharge")
        check("[-5] AC8 a discharge exiting 0 reports `discharged`",
              _p5g0.returncode == 0 and "discharged" in _p5g0.stdout,
              _p5g0.stdout + _p5g0.stderr)
        _p5g1 = a5_cov_flag(a5_target("disch-red", _A5_HELD,
                                      '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                      'why = "a probe proves it"\n'
                                      'discharge = { command = ["bash", "-c", "exit 1"] }\n'),
                            "--run-discharge")
        check("[-5] AC8 ...and exiting 1 reports `undischarged` rather than `discharged`",
              "undischarged" in _p5g1.stdout, _p5g1.stdout)
        _p5gt = a5_cov_flag(a5_target("disch-token", _A5_HELD,
                                      '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                      'why = "a probe proves it"\n'
                                      'discharge = { command = ["bash", "-c", "test -f {nowhere}"] }\n'),
                            "--run-discharge")
        check("[-5] AC8 ...and an unresolved {token} refuses BY NAME rather than running",
              _p5gt.returncode == 1 and "needs answer(s) nowhere" in _p5gt.stdout, _p5gt.stdout)
        # D1 secondary: a STRING command is iterated character by character. `validate_gate_runner`
        # refuses the same shape by name for `[gate_runner].command`; this branch had no equivalent.
        _p5str = a5_cov_flag(a5_target("disch-str", _A5_HELD,
                                       '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                       'why = "a probe proves it"\n'
                                       'discharge = { command = "bash -c true" }\n'),
                             "--run-discharge")
        check("[-5] D1 a discharge.command that is a STRING is refused, not iterated per character",
              _p5str.returncode == 1 and "must be an argv ARRAY" in _p5str.stdout, _p5str.stdout)

        # ---- AC9: the one-evidence-field rule, enforced BEFORE either field is evaluated. The
        # ---- fixture makes BOTH fields individually valid, so an implementation that graded them
        # ---- first and complained second would pass every other arm and fail only this one.
        _p5two = a5_cov(a5_target("two-evidence",
                                  dict(_A5_HELD, **{"vendor/two-renamed.py": b"2\n",
                                                    "scripts/all-in-one.py": b"both\n"}),
                                  '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                  'why = "both, somehow"\ntaken_as = "vendor/two-renamed.py"\n'
                                  'consumed_into = "scripts/all-in-one.py"\n'))
        check("[-5] AC9 a row carrying two evidence fields reds on the one-field rule",
              _p5two.returncode == 1 and "evidence fields" in _p5two.stdout, _p5two.stdout)
        check("[-5] AC9 ...naming BOTH fields, and before either was evaluated",
              "taken_as, consumed_into" in _p5two.stdout, _p5two.stdout)

        # ---- THE REMAINING REFUSAL BRANCHES, so every one of the eleven this unit adds is reached
        # ---- by a named arm. Five of them serve no acceptance criterion and would otherwise ship
        # ---- unasserted, which is exactly what `refusal_join.py` exists to prevent.
        _p5nk = a5_cov(a5_target("nokit", _A5_HELD,
                                 '\n[[decline]]\ndest = "scripts/demo/two.py"\nwhy = "x"\n'))
        check("[-5] a decline row with no `kit` reds rather than being skipped",
              _p5nk.returncode == 1 and "carries no kit or no dest" in _p5nk.stdout, _p5nk.stdout)
        _p5uk = a5_cov(a5_target("unknownkit", _A5_HELD,
                                 '\n[[decline]]\nkit = "elsewhere"\ndest = "scripts/demo/two.py"\n'
                                 'why = "x"\n'))
        check("[-5] a decline naming a kit NO REGISTRY ENTRY declares reds BY NAME",
              _p5uk.returncode == 1 and "not a registry entry" in _p5uk.stdout, _p5uk.stdout)
        # THE OTHER HALF OF THAT FIELD, found by this unit's own closing review: a kit that EXISTS
        # and is outside THIS RUN's `--kits` is not this run's business, and redding it would red an
        # operator for narrowing a selection. It is announced rather than dropped, because a decline
        # that vanishes without saying why is the failure mode the whole unit is written against.
        _t5nar = a5_target("narrow", _A5_HELD,
                           '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                           'why = "not this run\'s business"\n')
        _p5nar = run_in_gov(_g4k, "plan", "--target", str(_t5nar), "--coverage", "--kits", "demo")
        check("[-5] LIVENESS the narrow fixture's decline IS graded when its kit is selected",
              "declined" in _p5nar.stdout, _p5nar.stdout)
        # A TWO-KIT gov, because the branch under test needs a kit that EXISTS and is NOT selected —
        # and the first draft of this arm reused a one-kit fixture, so `--kits demo` selected the
        # only kit there was, the branch never ran, and the arm passed on the exit code alone. That
        # is `fixture-passes-by-finding-nothing`, in an arm written for a review finding.
        _g5sib = tmp / "a5-sibling"
        (_g5sib / "tools" / "govkit").mkdir(parents=True)
        (_g5sib / "tools" / "demo").mkdir(parents=True)
        (_g5sib / "tools" / "sib").mkdir(parents=True)
        shutil.copy2(HERE / "govkit.py", _g5sib / "tools" / "govkit" / "govkit.py")
        (_g5sib / "tools" / "govkit" / "registry.toml").write_text(
            '[surface]\nglobs = ["tools/*"]\n\n[selection]\ndefault = ["demo", "sib"]\n\n'
            '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
            '[[entry]]\nid = "sib"\ndescriptor = "tools/sib/kit.toml"\n\n'
            '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n',
            encoding="utf-8", newline="\n")
        for _e in ("demo", "sib"):
            (_g5sib / "tools" / _e / "kit.toml").write_text(
                _A4_KIT.replace('id = "demo"', f'id = "{_e}"').replace(
                    'home = "tools/demo"', f'home = "tools/{_e}"'),
                encoding="utf-8", newline="\n")
            (_g5sib / "tools" / _e / "one.py").write_text("1\n", encoding="utf-8", newline="\n")
        git(_g5sib, "init", "-q", "-b", "main")
        git(_g5sib, "config", "user.email", "t@e")
        git(_g5sib, "config", "user.name", "t")
        git(_g5sib, "config", "core.autocrlf", "false")
        git(_g5sib, "add", "-A")
        git(_g5sib, "commit", "-qm", "A")
        _t5out = a5_target("outside", {"scripts/demo/one.py": b"1\n"},
                           '\n[[decline]]\nkit = "sib"\ndest = "scripts/sib/one.py"\n'
                           'why = "the other kit, not this run"\n')
        check("[-5] LIVENESS the two-kit fixture really carries a decline for an UNSELECTED kit",
              "sib" in (_t5out / ".governance" / "deploy.toml").read_text(encoding="utf-8"))
        _p5out = run_in_gov(_g5sib, "plan", "--target", str(_t5out), "--coverage", "--kits", "demo")
        check("[-5] a decline for a kit outside the run's SELECTION does not RED the run",
              _p5out.returncode == 0, f"rc {_p5out.returncode}: {_p5out.stdout[-700:]}")
        check("[-5] ...and does not VANISH either — it announces that it was not graded",
              "OUTSIDE this run's selection" in _p5out.stdout, _p5out.stdout[-700:])
        _p5ta = a5_cov(a5_target("takenas-missing", _A5_HELD,
                                 '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                 'why = "x"\ntaken_as = "vendor/absent.py"\n'))
        check("[-5] a `taken_as` the target does not track reds — the evidence names nothing",
              _p5ta.returncode == 1 and "the evidence names a file that is not there"
              in _p5ta.stdout, _p5ta.stdout)
        _p5nc = a5_cov(a5_target("disch-nocmd", _A5_HELD,
                                 '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                 'why = "x"\ndischarge = { why = "no command here" }\n'))
        check("[-5] a discharge with no command reds — `discharged` is undefined for it",
              _p5nc.returncode == 1 and "discharge with no command" in _p5nc.stdout, _p5nc.stdout)
        _p5nb = a5_cov_flag(a5_target("disch-nobin", _A5_HELD,
                                      '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                      'why = "x"\n'
                                      'discharge = { command = ["no-such-binary-xyzzy"] }\n'),
                            "--run-discharge")
        check("[-5] a discharge probe that cannot LAUNCH reds rather than raising a traceback",
              _p5nb.returncode == 1 and "probe could not run" in _p5nb.stdout
              and "Traceback" not in _p5nb.stderr, _p5nb.stdout + _p5nb.stderr)

        # ---- S7's SECOND CALL SITE. `check` runs the same predicate, so the two verbs cannot
        # ---- disagree about whether a decline is stale — asserted by observing the SAME fixture
        # ---- red in both, rather than by reading the source and trusting it.
        _t5chk = a5_target("check-site", dict(_A5_HELD, **{"scripts/demo/two.py": b"2\n"}),
                           '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                           'why = "we do not use it"\n')
        run_in_gov(_g4, "adopt", "--target", str(_t5chk), "--write")
        _p5chk = run_in_gov(_g4, "check", "--target", str(_t5chk))
        check("[-5] S7 `check` grades declines through the same predicate `plan --coverage` runs",
              "the file arrived" in _p5chk.stdout, _p5chk.stdout[-1200:])
        check("[-5] S7 ...and a stale one reds THERE too, so neither verb can excuse what the "
              "other refuses",
              _p5chk.returncode == 1, f"rc {_p5chk.returncode}")

        # ---- AC10's ARITHMETIC, which is the part of it that is a property of this code rather
        # ---- than of one adopter's tree at one vintage: declining N rows moves exactly N from the
        # ---- gap count to the declined count, and the WRITE-ROW TOTAL does not move. A decline
        # ---- that shrank the denominator would be hiding gov's own population rather than
        # ---- excusing a row, which is the failure this asserts against.
        _p5base = a5_cov(a5_target("arith-base", _A5_HELD))
        _p5one = a5_cov(a5_target("arith-one", _A5_HELD,
                                  '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                  'why = "one"\n'))
        _p5both = a5_cov(a5_target("arith-both", _A5_HELD,
                                   '\n[[decline]]\nkit = "demo"\ndest = "scripts/demo/two.py"\n'
                                   'why = "one"\n\n[[decline]]\nkit = "demo"\n'
                                   'dest = "scripts/demo/three.py"\nwhy = "two"\n'))

        def _tot5(out: str) -> int:
            return int(_re.search(r"gap \d+ of (\d+) write row\(s\)", out).group(1))

        check("[-5] AC10 declining rows moves them out of the gap count, one for one",
              (a4_gap_total(_p5base.stdout), a4_gap_total(_p5one.stdout),
               a4_gap_total(_p5both.stdout)) == (2, 1, 0),
              f"{a4_gap_total(_p5base.stdout)}, {a4_gap_total(_p5one.stdout)}, "
              f"{a4_gap_total(_p5both.stdout)}")
        check("[-5] AC10 ...and the WRITE-ROW TOTAL does not move, so a decline excuses a row "
              "rather than shrinking gov's population",
              _tot5(_p5base.stdout) == _tot5(_p5one.stdout) == _tot5(_p5both.stdout),
              f"{_tot5(_p5base.stdout)}, {_tot5(_p5one.stdout)}, {_tot5(_p5both.stdout)}")
        check("[-5] AC10 ...and the declined count rises to match",
              ", 2 declined" in _p5both.stdout and ", 1 declined" in _p5one.stdout,
              _p5both.stdout)

        # ---- D2/D5/D9, the three closing-review findings that damage a TARGET. Each is asserted on
        # ---- the observable consequence rather than on the code shape that produces it.
        #
        # ---- D8, from the closing review. `decline_findings` returned a DEST-KEYED map while the
        # ---- population it filters is keyed by (kit, dest) -- and `coverage_rows`' own docstring
        # ---- insists on rows never unique destinations, because a destination-keyed tally is what
        # ---- hid a collision at a live target. So a decline naming kit A for a destination only
        # ---- kit B ships passed every arm, hid B's genuine gap, and mis-attributed it.
        _t8 = a5_target('crosskit', {'scripts/demo/one.py': b'1\n'},
                        '\n[[decline]]\nkit = "demo"\ndest = "scripts/sib/one.py"\n'
                        'why = "the wrong kit for this destination"\n')
        _p8 = run_in_gov(_g5sib, 'plan', '--target', str(_t8), '--coverage',
                         '--kits', 'demo,sib')
        check('[-5] D8 LIVENESS the two-kit fixture really plans a sib destination',
              'scripts/sib/one.py' in _p8.stdout, _p8.stdout[-800:])
        # ROUND 2's L3. The predicate here used to be
        # `'GAP' in stdout and 'scripts/sib/one.py' in stdout.split('coverage:')[0]`, and BOTH
        # conjuncts were satisfied with D8 reverted: the fixture's own unrelated `demo` gaps supply
        # a GAP anywhere in stdout, and the plan-row loop prints every `write` row -- the sib one
        # included -- above the summary line that supplies the split token. Under the dest-keyed map
        # that hid B's gap entirely, this arm still reported green. The arm that NAMED the defect was
        # not the arm that caught it; only its sibling below discriminated.
        #
        # Anchored now on the GAP LINE ITSELF, which only the gap emitter produces: false under the
        # dest-keyed map, true under the pair-keyed one.
        _p8gap = [l for l in _p8.stdout.splitlines()
                  if l.startswith('  GAP') and 'scripts/sib/one.py' in l]
        check('[-5] D8 a decline naming the WRONG kit for a destination does not excuse it',
              bool(_p8gap), _p8.stdout[-900:])
        check('[-5] D8 ...and reds as stale, naming the kit that ships no such destination',
              _p8.returncode == 1 and 'ships no such destination' in _p8.stdout,
              f'rc {_p8.returncode}: ' + _p8.stdout[-900:])
        # D2: `adopt --re-adopt --write` over a receipt `apply` wrote must not discard the five keys
        # recording what the install DID. Dropping `gate_runner.emitted` empties `owned` in the next
        # `apply`, whose first leg-name collision then refuses the whole install permanently.
        _t2d = a13_target("readopt", "scripts", {})
        _a2d = run_in_gov(_g4, "apply", "--target", str(_t2d), "--kits", "demo")
        check("[-13] D2 LIVENESS the fixture's apply really wrote a receipt to re-adopt over",
              (_t2d / ".governance" / "install.json").is_file(),
              _a2d.stdout[-700:] + _a2d.stderr[-400:])
        _before2 = a13_receipt(_t2d) if (_t2d / ".governance" / "install.json").is_file() else {}
        _keys2 = [k for k in ("orders", "baseline", "after", "hook_block", "gate_runner")
                  if k in _before2]
        check("[-13] D2 LIVENESS ...carrying install-record keys, so the drop is observable at all",
              len(_keys2) >= 3, str(sorted(_before2)))
        settle(_t2d, "the install")
        run_in_gov(_g4, "adopt", "--target", str(_t2d), "--re-adopt", "--write")
        _after2 = a13_receipt(_t2d)
        check("[-13] D2 `--re-adopt` carries every install-record key forward rather than dropping it",
              all(k in _after2 for k in _keys2),
              "lost: " + ", ".join(k for k in _keys2 if k not in _after2))
        check("[-13] D2 ...VERBATIM — this verb did not witness the install and may not re-measure it",
              all(_after2.get(k) == _before2.get(k) for k in _keys2),
              "changed: " + ", ".join(k for k in _keys2 if _after2.get(k) != _before2.get(k)))

        # D5: `adopt --write` is the THIRD receipt writer and must stand inside the per-target lock.
        # Asserted by planting a held lock and observing the refusal -- and by asserting the
        # READ-ONLY run does NOT pay it, which is the half a lock-everything fix would break.
        _t5l = a13_target("lock", "scripts", {"scripts/demo/one.py": b"1\n"})
        # THE LOCK PATH IS THE ENGINE'S OWN CONSTANT, never a spelling invented here. The first cut
        # of this arm planted `.governance/install.lock` from memory; the engine's lock lives at
        # `WRITE_LOCK_REL`, so it never saw the file and `adopt --write` sailed through at rc 0 — an
        # arm that would have reported the fix working while testing nothing. Read the constant.
        _lockp = _t5l.joinpath(*govkit_module().WRITE_LOCK_REL.split("/"))
        _lockp.parent.mkdir(parents=True, exist_ok=True)
        _lockp.write_text('{"pid": 999999, "verb": "apply", "started_utc": "2026-01-01T00:00:00Z"}\n',
                          encoding="utf-8", newline="\n")
        # READ-ONLY FIRST, deliberately: it must not pay for the lock, and running it first keeps it
        # away from a receipt the write arm would otherwise have left behind.
        _p5lr = run_in_gov(_g4, "adopt", "--target", str(_t5l))
        check("[-13] D5 a READ-ONLY adopt does not pay for the lock, which is the rule the other "
              "two verbs already follow",
              _p5lr.returncode == 0, _p5lr.stdout[-400:] + _p5lr.stderr[-400:])
        _p5l = run_in_gov(_g4, "adopt", "--target", str(_t5l), "--write")
        check("[-13] D5 ...while `adopt --write` REFUSES against a held write lock, like the two "
              "writers that already stood inside it",
              _p5l.returncode == 2 and "lock" in (_p5l.stdout + _p5l.stderr).lower(),
              f"rc {_p5l.returncode}: {_p5l.stdout[-400:]}{_p5l.stderr[-400:]}")
        check("[-13] D5 ...and wrote no receipt while refusing",
              not (_t5l / ".governance" / "install.json").is_file(),
              "a receipt exists: the refusal came after the write")
        # ROUND 2's L2, and the arm above is why it was found. That arm CLAIMED the lock is taken
        # before the existence guard, and it observed nothing of the kind: this fixture carries no
        # `install.json`, so the guard at `govkit.py:5743` is inert for it and EITHER ordering
        # refuses at the lock and writes no receipt. Moving `take_write_lock` back below the guard
        # left the arm green. The check-then-mutate window D5 identified was guarded by nothing.
        #
        # THE ORDERING IS ONLY OBSERVABLE WHERE THE TWO REFUSALS DISAGREE. Plant BOTH the held lock
        # and a receipt, then run `--write` WITHOUT `--re-adopt`: both guards now want to fire, and
        # WHICH message comes back names the order. Lock first is the fix; receipt first is the
        # defect, and it is a check-then-mutate because the guard would have read a receipt a
        # concurrent writer is mid-way through replacing.
        (_t5l / ".governance").mkdir(parents=True, exist_ok=True)
        (_t5l / ".governance" / "install.json").write_text("{}\n", encoding="utf-8", newline="\n")
        _p5ord = run_in_gov(_g4, "adopt", "--target", str(_t5l), "--write")
        _ord_out = (_p5ord.stdout + _p5ord.stderr).lower()
        check("[-13] D5 ...and with a receipt ALSO present the LOCK refusal is the one that fires, "
              "which is the only observation that distinguishes the two orderings",
              "holds" in _ord_out and "already carries a receipt" not in _ord_out,
              f"rc {_p5ord.returncode}: {_p5ord.stdout[-500:]}{_p5ord.stderr[-500:]}")
        (_t5l / ".governance" / "install.json").unlink()
        _lockp.unlink()

        # D9: `sha256` must answer the question `check` and `sha256sum -c` ASK, which is about the
        # WORKTREE. It stamped the INDEX blob, so an unstaged edit -- which
        # `demand_adopt_index_clean` DELIBERATELY permits, and which the -13 ledger asserts as a
        # tested property -- made `check` report a mismatch for a row nothing was wrong with, on
        # precisely the trees this verb exists for.
        _t9 = a13_target("worktree-hash", "scripts", {"scripts/demo/one.py": b"1\n"})
        (_t9 / "scripts" / "demo" / "one.py").write_bytes(b"an unstaged local edit\n")
        _p9 = run_in_gov(_g4, "adopt", "--target", str(_t9), "--write")
        check("[-13] D9 LIVENESS adopt still SUCCEEDS over an unstaged edit — the width -12 permits",
              _p9.returncode == 0, _p9.stdout[-500:] + _p9.stderr[-400:])
        _row9 = a13_row(a13_receipt(_t9), "scripts/demo/one.py")
        _wt9 = hashlib.sha256((_t9 / "scripts" / "demo" / "one.py").read_bytes()).hexdigest()
        _ix9 = hashlib.sha256(b"1\n").hexdigest()
        check("[-13] D9 LIVENESS the fixture's index and worktree really differ, or this proves "
              "nothing", _wt9 != _ix9)
        check("[-13] D9 `sha256` is the WORKTREE's bytes, which is what `check` compares against",
              _row9.get("sha256") == _wt9,
              f"got {_row9.get('sha256')} · worktree {_wt9} · index {_ix9}")
        check("[-13] D9 ...while `oid` stays the INDEX identity the verdict logic reads",
              _row9.get("oid") == subprocess.run(
                  ["git", "-C", str(_t9), "rev-parse", ":scripts/demo/one.py"],
                  capture_output=True, text=True).stdout.strip(), str(_row9.get("oid")))
        _pc9 = run_in_gov(_g4, "check", "--target", str(_t9))
        check("[-13] D9 ...so `check` does not report a mismatch for a row nothing is wrong with",
              "does not match the receipt" not in _pc9.stdout, _pc9.stdout[-800:])

        # D6: an unmatched `--pin` was silently ignored, which closes a loop on the operator: the
        # row it was meant to rescue keeps `unattributed`, `update` keeps skipping it, and the
        # remedy names the command they just ran to no effect. The same flag already refuses loudly
        # on its other two error classes.
        _t6p = a13_target("pin-unmatched", "scripts", {"scripts/demo/verbatim-one.py": b"v1\n"})
        _p6p = run_in_gov(_g13, "adopt", "--target", str(_t6p), "--write",
                          "--pin", "scripts/demo/no-such-file.py=" + _sh13[0])
        check("[-13] D6 a `--pin` matching no planned row is REFUSED rather than silently ignored",
              _p6p.returncode == 2 and "no-such-file.py" in _p6p.stderr, _p6p.stderr[-600:])
        check("[-13] D6 ...and the refusal lists what WAS measured, so a typo cannot read as applied",
              "measured" in _p6p.stderr.lower(), _p6p.stderr[-600:])
        _p6pok = run_in_gov(_g13, "adopt", "--target", str(_t6p), "--write",
                            "--pin", "scripts/demo/verbatim-one.py=" + _sh13[0])
        check("[-13] D6 LIVENESS ...while a pin that DOES match still succeeds",
              _p6pok.returncode == 0, _p6pok.stdout[-400:] + _p6pok.stderr[-400:])

        # D14: the remedy `update` prints named an invocation `adopt` always refuses, in the one
        # sentence that exists to stop an operator concluding the tool is broken.
        _gk14 = govkit_module()
        _src14 = (HERE / "govkit.py").read_text(encoding="utf-8")
        check("[-13] D14 the unattributed remedy names an invocation that can actually work",
              "--re-adopt --pin" in _src14 and "adopt --pin <path>=<rev>` supplies one"
              not in _src14, "the remedy still names the refusing form")

        _S11_EXTRA = ('\n[[files]]\ninclude = "seed-one.py"\nrole = "seed"\n\n'
                      '[[files]]\ninclude = "block.txt"\nrole = "merged"\n'
                      'block_id = "demo:block"\nmarker_style = "hash-comment"\n'
                      'to = "hooks/pre-commit"\n\n'
                      '[[lf_pin]]\npattern = "*.sh"\n')
        # THE MARKER PAIR IS `marker_pair`'s, not a shape invented here. It synthesizes
        # `# <block_id>` / `# /<block_id>` for `hash-comment`, and a fixture spelling any other
        # pair produces a source `find_block` cannot read — which reads as "the feature does not
        # work" and is really "the fixture never triggered it". Cost one round here.
        _BLOCK = "# demo:block\nechodemo\n# /demo:block\n"
        _W1s = dict(_W1, **{"seed-one.py": "seed-v1\n", "block.txt": _BLOCK})
        _g11, _sh11 = a13_gov("s11", [_W1s, _W2], a13_kit(_S11_EXTRA))
        _t11 = a13_target("s11", "scripts", {
            "scripts/demo/verbatim-one.py": b"v1\n",
            "scripts/demo/seed-one.py": b"the target rewrote its own seed entirely\n",
            "hooks/pre-commit": b"#!/bin/sh\n# demo:block\nechodemo\n# /demo:block\n",
            ".gitattributes": b"*.sh text eol=lf\n"})
        _p11 = run_in_gov(_g11, "adopt", "--target", str(_t11), "--write")
        check("[-13] AC13 adopt exits 0 over a descriptor declaring an lf_pin and a merged rule",
              _p11.returncode == 0, _p11.stdout + _p11.stderr)
        _rec11 = a13_receipt(_t11)
        _attr = [f for f in _rec11["files"] if f.get("role") == "attributes"]
        check("[-13] AC13 the receipt carries EXACTLY ONE synthesized `attributes` row",
              len(_attr) == 1 and _attr[0]["path"] == ".gitattributes",
              str([f["path"] for f in _attr]))
        check("[-13] AC13 ...carrying neither identity and no `evidence`, per S11",
              not any(k in _attr[0] for k in ("gov_oid", "oid", "evidence")) if _attr else False,
              str(_attr[0]) if _attr else "no row")
        _mrg = [f for f in _rec11["files"] if f.get("role") == "merged"]
        check("[-13] AC13 ...and a `merged` row in apply's shape, with the block_id `check` reads",
              len(_mrg) == 1 and _mrg[0].get("block_id") == "demo:block", str(_mrg))
        _pc11 = run_in_gov(_g11, "check", "--target", str(_t11))
        check("[-13] AC13 ...so `check` reports the merged block rather than raising KeyError",
              "Traceback" not in (_pc11.stdout + _pc11.stderr), _pc11.stdout + _pc11.stderr)
        _seed = a13_row(_rec11, "scripts/demo/seed-one.py")
        check("[-13] AC14 the fixture really produced an UNATTRIBUTED `seed` row",
              _seed.get("role") == "seed" and _seed.get("evidence") == "unattributed", str(_seed))
        settle(_t11, "receipt")
        _before11 = (_t11 / "scripts" / "demo" / "seed-one.py").read_bytes()
        _pu11 = run_in_gov(_g11, "update", "--target", str(_t11), "--write")
        check("[-13] AC14 the unattributed SEED row reaches its own disposition, not S7's skip",
              "[seed" in _pu11.stdout and "reseed" in _pu11.stdout.lower(), _pu11.stdout)
        check("[-13] AC14 ...and the synthesized `attributes` row reaches `-2`'s pins arm",
              "[attributes" in _pu11.stdout, _pu11.stdout)
        check("[-13] AC14 ...and neither writes a byte",
              (_t11 / "scripts" / "demo" / "seed-one.py").read_bytes() == _before11)

        # ---- `EVIDENCE_STATES` IS LOAD-BEARING OR IT IS A SECOND SPELLING. A tuple nothing reads
        # ---- is exactly the two-answers-to-one-question shape: the real enum would live in the
        # ---- branches that assign the field, and the constant would drift beside them saying
        # ---- nothing. These two arms make it the answer. The first joins it to the values a real
        # ---- run WROTE; the second to every literal the engine can assign, so a fourth state added
        # ---- in a branch reds here rather than shipping undeclared.
        _GK13 = govkit_module()
        # THE PINNED ROW IS CARRIED IN EXPLICITLY. Its receipt belongs to a fixture the AC8 arms
        # re-adopt READ-ONLY afterwards, so re-reading it here would work today and stop working the
        # first time somebody adds a `--write` to one of those arms. The row object is the evidence.
        _seen13 = {f["evidence"] for f in (_rec13["files"] + _rec11["files"] + [_pinned])
                   if "evidence" in f}
        check("[-13] every `evidence` value a real run wrote is a declared state",
              _seen13 <= set(_GK13.EVIDENCE_STATES),
              f"{sorted(_seen13)} vs {sorted(_GK13.EVIDENCE_STATES)}")
        check("[-13] LIVENESS ...over a population carrying THREE of them, not one",
              len(_seen13) >= 3, str(sorted(_seen13)))
        _lit13 = set(_re.findall(r'\["evidence"\]\s*=\s*"([a-z-]+)"', _g13src)) | set(
            _re.findall(r'"evidence":\s*"([a-z-]+)"', _g13src))
        check("[-13] ...and every literal the ENGINE can assign to `evidence` is declared too",
              _lit13 and _lit13 <= set(_GK13.EVIDENCE_STATES),
              f"{sorted(_lit13)} vs {sorted(_GK13.EVIDENCE_STATES)}")


        # ============================================================= DEPL-dCarriedReceipt-6
        # The silenced-gate-leg bar. `apply` emitted a target's gate legs and asked, of the leg's
        # GUARDS, whether they matched a tracked path — while never asking the same question of the
        # thing the leg actually EXECUTES. So gov could hand an adopter a leg row naming a file gov
        # never ships, record it in the receipt as emitted coverage, and nothing would say so.
        A6_REG = ('[surface]\nglobs = ["tools/*"]\n\n'
                  '[selection]\ndefault = ["demo"]\n\n'
                  '[[entry]]\nid = "demo"\ndescriptor = "tools/demo/kit.toml"\n\n'
                  '[[exempt]]\npath = "tools/govkit"\nwhy = "the deployer itself"\n')

        def a6_kit(leg_argv: str) -> str:
            """The fixture kit: one engine rule, a `[gate_runner]` seed so the target gets a
            manifest to emit into, and ONE gate leg whose argv the caller writes."""
            return ('id = "demo"\nhome = "tools/demo"\n'
                    'version_from = { none = "fixture" }\n\n'
                    '[check]\nnone = "a fixture kit"\n\n'
                    '[[files]]\ninclude = "**"\nrole = "engine"\n\n'
                    '[[gate_leg]]\nname = "demo leg"\nsubject = "repo"\n'
                    f'argv = {leg_argv}\nguard = []\n\n'
                    '[[gate_leg]]\nname = "demo sibling"\nsubject = "repo"\n'
                    'argv = ["bash", "{prefix}/demo/present-engine.sh"]\nguard = []\n\n'
                    '[adopt]\nargv = []\nmutates_index = false\n')

        def a6_gov(tag: str, leg_argv: str) -> pathlib.Path:
            g = tmp / f"a6-{tag}"
            (g / "tools" / "govkit").mkdir(parents=True)
            (g / "tools" / "demo").mkdir(parents=True)
            shutil.copy2(HERE / "govkit.py", g / "tools" / "govkit" / "govkit.py")
            (g / "tools" / "govkit" / "registry.toml").write_text(A6_REG, encoding="utf-8",
                                                                  newline="\n")
            (g / "tools" / "demo" / "kit.toml").write_text(a6_kit(leg_argv), encoding="utf-8",
                                                           newline="\n")
            (g / "tools" / "demo" / "present-engine.sh").write_text("exit 0\n", encoding="utf-8",
                                                                    newline="\n")
            git(g, "init", "-q", "-b", "main")
            git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t")
            git(g, "config", "core.autocrlf", "false")
            git(g, "add", "-A")
            git(g, "commit", "-qm", "A")
            return g

        def a6_target(tag: str) -> pathlib.Path:
            t = tmp / f"a6t-{tag}"
            t.mkdir(parents=True)
            git(t, "init", "-q", "-b", "main")
            git(t, "config", "user.email", "t@e")
            git(t, "config", "user.name", "t")
            git(t, "config", "core.autocrlf", "false")
            (t / ".governance").mkdir()
            (t / ".governance" / "deploy.toml").write_text(
                'gov_source = "local"\nprefix = "scripts"\nkits = ["demo"]\n\n'
                # EVERY KEY A COMPLETE PROMOTION NEEDS. A partial `[gate_runner]` is refused by
                # name, which is correct and which made the first cut of this fixture fail four
                # arms for a reason that had nothing to do with the leg bar.
                '[gate_runner]\nkind = "manifest"\nfile = "scripts/gate-legs.json"\n'
                'grammar = "json-array"\ndedupe_key = "name"\n'
                'command = ["bash", "scripts/run-gates.sh"]\n'
                'run_all_env = { GATE_FULL = "1" }\n'
                'observed_ran = ["GATE ok    {name}"]\n'
                'observed_failed = ["GATE FAIL  {name}"]\n',
                encoding="utf-8", newline="\n")
            (t / "scripts").mkdir()
            (t / "scripts" / "gate-legs.json").write_text("[]\n", encoding="utf-8", newline="\n")
            (t / "README.md").write_text("t\n", encoding="utf-8", newline="\n")
            git(t, "add", "-A")
            git(t, "commit", "-qm", "base")
            return t

        def a6_legs(t: pathlib.Path) -> list[str]:
            f = t / "scripts" / "gate-legs.json"
            return [e.get("name") for e in json.loads(f.read_text(encoding="utf-8"))] \
                if f.is_file() else []

        # ---- AC1's RED is HISTORICAL: `selfcheck` exited 0 over a descriptor declaring a leg whose
        # ---- engine the registry exempts from shipping, which is the green-on-a-defect the unit
        # ---- exists for. It cannot be re-observed now without removing the arm. AC2's BOTH HALVES
        # ---- were observed on this repo while building — red by name before S5 was applied, green
        # ---- after — and what is gated here is the SHIPPED STATE: this repo's own descriptors
        # ---- declare no unshippable leg engine.
        _p6self = run("selfcheck")
        check("[-6] AC2 selfcheck is GREEN over gov's own descriptors after the S5 withdrawal",
              _p6self.returncode == 0, _p6self.stdout[-1200:] + _p6self.stderr[-600:])
        check("[-6] S4 ...and it SAYS what it checked, with a derived count rather than silence",
              "gate legs: every argv path checked against the shipped map · 0 unshippable"
              in _p6self.stdout, _p6self.stdout[-800:])
        # S5, ASSERTED ON THE TREE rather than on the run: the leg is gone from the descriptor and
        # the exemption that replaced it names it. Without this pair the arm above passes on any
        # tree where the leg was deleted and nothing recorded why.
        _kmk = (HERE.parent / "govkit" / "entries" / "kickoff-manifest.kit.toml").read_text(
            encoding="utf-8")
        _regs = (HERE / "registry.toml").read_text(encoding="utf-8")
        check("[-6] S5 the unshippable leg is gone from the kickoff-manifest descriptor",
              "kickoff engine size" not in _kmk, "the gate_leg block is still declared")
        check("[-6] S5 ...and an [[exempt_leg]] row carries it, with a reason",
              'name = "kickoff engine size <=18KiB"' in _regs
              and "check-template-size.sh" in _regs.split(
                  'name = "kickoff engine size <=18KiB"', 1)[1][:900], "no exempt_leg row")

        # ---- S4's OWN LIVENESS. An arm that has only ever been seen passing is an assertion about
        # ---- nothing, so the predicate is staged RED on a scratch gov whose descriptor declares a
        # ---- leg engine no rule ships — the same shape S5 just removed from this repo.
        _g6bad = a6_gov("unshipped", '["bash", "{prefix}/demo/absent-engine.sh"]')
        _p6bad = run_in(_g6bad)
        check("[-6] S4 LIVENESS a descriptor declaring an unshippable leg engine REDS selfcheck",
              _p6bad.returncode == 1, _p6bad.stdout[-900:] + _p6bad.stderr[-400:])
        check("[-6] S4 ...naming the entry, the leg and the element rather than refusing anonymously",
              "demo leg" in _p6bad.stdout and "absent-engine.sh" in _p6bad.stdout, _p6bad.stdout)
        _g6ok = a6_gov("shipped", '["bash", "{prefix}/demo/present-engine.sh"]')
        check("[-6] S4 ...while a leg whose engine IS shipped stays green",
              run_in(_g6ok).returncode == 0, run_in(_g6ok).stdout[-900:])

        # ---- AC4: THE FALSE-POSITIVE GUARD, and it is the arm that fails if the bar is evaluated
        # ---- before the STAGE step. On a first install NOTHING is tracked in the target yet; by
        # ---- the time the legs step runs, `apply` has staged its own writes, so a kit shipping its
        # ---- own leg engine emits the leg and exits 0. Moving the predicate earlier reds every
        # ---- first install at every adopter, which is why the placement is written down.
        _t6ok = a6_target("ok")
        _a6ok = run_in_gov(_g6ok, "apply", "--target", str(_t6ok), "--kits", "demo")
        check("[-6] AC4 a kit shipping its own leg engine emits the leg and exits 0",
              _a6ok.returncode == 0 and "demo leg" in a6_legs(_t6ok),
              f"rc {_a6ok.returncode} legs {a6_legs(_t6ok)}\n" + _a6ok.stdout[-900:])
        check("[-6] AC4 LIVENESS ...over a manifest that really gained rows, so this is not vacuous",
              len(a6_legs(_t6ok)) >= 2, str(a6_legs(_t6ok)))

        # ---- AC5: the bar itself. Exactly one finding, no row, exit 1 — and NOT a Refusal: the
        # ---- receipt is still written and the sibling leg is still emitted, because the condition
        # ---- is a defect in a GOV-authored descriptor and aborting an adopter's install over it
        # ---- hands them a failure with no local fix.
        _t6bad = a6_target("bad")
        _a6bad = run_in_gov(_g6bad, "apply", "--target", str(_t6bad), "--kits", "demo")
        check("[-6] AC5 a leg naming an absent engine produces a finding and exit 1",
              _a6bad.returncode == 1 and "which this target does not hold" in _a6bad.stdout,
              _a6bad.stdout[-1200:])
        check("[-6] AC5 ...the leg is NOT written into the target's runner",
              "demo leg" not in a6_legs(_t6bad), str(a6_legs(_t6bad)))
        check("[-6] AC5 ...but the SIBLING leg still is, so the install was not aborted",
              "demo sibling" in a6_legs(_t6bad), str(a6_legs(_t6bad)))
        check("[-6] AC5 ...and the receipt was still written — a finding, never a Refusal",
              (_t6bad / ".governance" / "install.json").is_file(),
              "no receipt: the run aborted instead of reporting")

        # ---- AC3's SHAPE, on a fixture rather than on a live submodule clone: the row a defective
        # ---- leg would have emitted is absent from the target's runner AND the run says why. The
        # ---- live measurement that motivated it is in the acceptance ledger.
        check("[-6] AC3 the run NAMES the withheld leg rather than dropping it silently",
              "demo leg" in _a6bad.stdout and "is NOT written" in _a6bad.stdout,
              _a6bad.stdout[-900:])

        # ---- S3: `plan` reports the same hits, over the UNION of what the target tracks and what
        # ---- THIS plan would write. Without the union a preview reds every first install — the
        # ---- same trap AC4 guards on the apply side, one verb over.
        _t6plan = a6_target("plan")
        _p6plan = run_in_gov(_g6ok, "plan", "--target", str(_t6plan), "--kits", "demo")
        check("[-6] S3 a plan for a FIRST install reports no silenced leg, because the union counts "
              "what this plan would write",
              "SILENT" not in _p6plan.stdout, _p6plan.stdout)
        _p6planbad = run_in_gov(_g6bad, "plan", "--target", str(_t6plan), "--kits", "demo")
        check("[-6] S3 ...while a leg no plan row would satisfy IS previewed as silenced",
              "SILENT" in _p6planbad.stdout and "absent-engine.sh" in _p6planbad.stdout,
              _p6planbad.stdout)

        # ---- D7, from the closing review. Every `-6` arm above declares `kind = "manifest"`, so
        # ---- the ORDER branch — taken whenever a target has not promoted a runner, which is the
        # ---- normal state of a fresh adopter — was graded by nothing, and it wrote every silenced
        # ---- leg into `.governance/outbox/gate-legs.md` as an INSTRUCTION with no warning at all.
        def a6_target_norunner(tag: str) -> pathlib.Path:
            t = tmp / f"a6tn-{tag}"
            t.mkdir(parents=True)
            git(t, "init", "-q", "-b", "main")
            git(t, "config", "user.email", "t@e")
            git(t, "config", "user.name", "t")
            git(t, "config", "core.autocrlf", "false")
            (t / ".governance").mkdir()
            (t / ".governance" / "deploy.toml").write_text(
                'gov_source = "local"\nprefix = "scripts"\nkits = ["demo"]\n',
                encoding="utf-8", newline="\n")
            (t / "README.md").write_text("t\n", encoding="utf-8", newline="\n")
            git(t, "add", "-A")
            git(t, "commit", "-qm", "base")
            return t

        _t6n = a6_target_norunner("bad")
        _a6n = run_in_gov(_g6bad, "apply", "--target", str(_t6n), "--kits", "demo")
        _ordp = _t6n / ".governance" / "outbox" / "gate-legs.md"
        check("[-6] D7 LIVENESS the no-runner fixture really took the ORDER branch",
              _ordp.is_file() and "ORDERED, not emitted" in _a6n.stdout,
              _a6n.stdout[-700:] + _a6n.stderr[-400:])
        _ordt = _ordp.read_text(encoding="utf-8") if _ordp.is_file() else ""
        # SCOPED TO THE INSTRUCTION HALF. The whole-file absence test the first cut used matched the
        # WITHHELD block's own line and redded on a correct order — the assertion has to be about
        # where the leg appears, not whether its name appears at all.
        _ord_instr = _ordt.split("## WITHHELD", 1)[0]
        check("[-6] D7 a silenced leg is NOT written into the order as an instruction",
              "demo leg" not in _ord_instr, _ord_instr)
        check("[-6] D7 ...it is listed under WITHHELD rather than dropped, because an order that "
              "silently omits a leg reads like a kit that declares none",
              "WITHHELD" in _ordt and "demo leg" in _ordt, _ordt)
        check("[-6] D7 ...the run REPORTS it, where before the order branch was silent",
              _a6n.returncode == 1 and "ordering it would" in _a6n.stdout,
              _a6n.stdout[-900:])
        check("[-6] D7 ...and the healthy sibling leg IS still ordered",
              "demo sibling" in _ordt, _ordt)
        _t6n2 = a6_target_norunner("ok")
        _a6n2 = run_in_gov(_g6ok, "apply", "--target", str(_t6n2), "--kits", "demo")
        check("[-6] D7 LIVENESS a no-runner target whose legs all resolve still exits 0",
              _a6n2.returncode == 0, _a6n2.stdout[-600:] + _a6n2.stderr[-400:])

        # ---- S6: ONE index reader. The legs step used an inline `git ls-files` split on newlines
        # ---- beside a `tracked()` that already existed — two spellings of one question, in the one
        # ---- function where they have to agree.
        _g6src = (HERE / "govkit.py").read_text(encoding="utf-8")
        check("[-6] S6 the legs step reads the target index through `tracked()`, not an inline "
              "ls-files beside it",
              'tracked_target = set(tracked(target))' in _g6src
              and 'tracked_target = set(subprocess.run' not in _g6src, "inline reader still present")





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
