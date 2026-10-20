# **Serves:** research PLAY-dClosedLoop-1
"""The whole-design audit's sealed copy: the design at one commit, twelve fixed past escapes reverted into it, the
sentences naming candidate plants cut, made a fresh one-commit repository, its design map rendered, and the key
written with its SHA-256. Kept outside the repository and the scratchpad until both runs are scored.

Usage: python -X utf8 seed.py <worktree> <base sha> <copy dir>   (writes the copy and key.json beside this script)
"""
import hashlib
import io
import json
import re
import subprocess
import sys
import tarfile
from pathlib import Path

WT, BASE, COPY = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
HERE = Path(__file__).resolve().parent
B = "memory/builds/dClosedLoop/build/"
V2 = B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
FS = B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md"
LM = B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md"
MP = B + "2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md"
FQ = B + "2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md"
RA = B + "2026-10-19-build-PLAY-dClosedLoop-1-research-final-audit.md"
WA = B + "2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md"
IR = B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md"

if COPY.exists():
    sys.exit(f"{COPY} exists; a sealed copy is made once, into an empty place")
raw = subprocess.run(["git", "-C", str(WT), "archive", "--format=tar", BASE], capture_output=True, check=True).stdout
with tarfile.open(fileobj=io.BytesIO(raw)) as tar:
    tar.extractall(COPY, filter="data")
files = {}


def text(rel):
    if rel not in files:
        files[rel] = (COPY / rel).read_text(encoding="utf-8")
    return files[rel]


def edit(rel, old, new, label, regex=False):
    t = text(rel)
    n = len(re.findall(old, t, flags=re.S)) if regex else t.count(old)
    if n != 1:
        sys.exit(f"{label}: the anchor matches {n} times in {rel}")
    files[rel] = re.sub(old, new, t, count=1, flags=re.S) if regex else t.replace(old, new, 1)


# The twelve plants, each a past escape's fix reverted.
edit(V2, ", a failed or killed step stopping the walk with the failure recorded, the steps before it left applied and the "
         "receipt naming the last completed one", "", "P01 walk-failure-route")
edit(V2, r"Serves kind `journal` renamed `log`, `journal` kept as its read-only retired alias, .*?, a `log` record with a "
         r"malformed AC line seen red in the ledger and today's `journal` records graded with no failure",
     "Serves kind `journal` renamed `log`, a `log` record with a malformed AC line seen red in the ledger",
     "P02 journal-rename, 0229", regex=True)
edit(V2, "its own upgrade steps: the `journal` alias, the `--new-build`", "its own upgrade steps: the `--new-build`",
     "P02 journal-rename, 0231")
edit(MP, r"the Serves kind is renamed `log` when dTotalRecall's registry lands, `journal` kept as its read-only\s+retired "
         r"alias, so no record is rewritten, and every reader of the value re-pointed by value in the rename's unit\.",
     "the Serves kind is renamed `log` when dTotalRecall's registry lands.", "P02 journal-rename, the memory plan", regex=True)
edit(V2, ", a restarted supervisor reconciling before its first beat: each act session the journal and process-monitor "
         "record under its lease re-adopted with its slot reservation rebuilt, or its tree killed, so a supervisor killed "
         "while an act runs and restarted by the node tick leaves exactly one act session on the item, seen in the fencing "
         "fixtures (the shape audit)", "", "P03 supervisor-restart")
edit(V2, "each intake marking its origin, the owner-bound hook, a mailbox sender or a cadence filer, only owner-origin "
         "intake, or mailbox intake carrying the owner binding's proof, ratifying a request and the rest routed to an owner "
         "breakpoint or an ask, an act posting an `intake` that proposes a build seen not to pass Plan's exit, and the intake",
     "and the intake", "P04 intake-ratification, 0305")
edit(V2, "its owner-origin intake alone read as the request's ratification", "its intake read as the request's ratification",
     "P04 intake-ratification, 0377")
edit(V2, ", and a declined retirement amending its part's row through the ratification record to `kept` or a new fate, which "
         "the join reads, a planted declined proposal passing on the amended row and red on an unamended one", "",
     "P05 declined-retirement")
edit(FS, "; the remote unreachable → no local id minted, the claim queued or refused as `leases.offline` says (DA-M13, FL1)",
     "", "P06 M13")
edit(V2, ", and builds witnessed under the fallback kept readable, the re-pointed readers accepting a fallback witness at any "
         "time from an adapter whose capability table lacks the prompt-submit event and from any other only before its own "
         "drain landing, seen on a build that crosses the drain and refused for a capable adapter's fallback witness written "
         "after its drain (DA-M15, FM3)", "", "P07 M15")
edit(FS, "| `entry.intake` | hook: prompt-submit, in an owner-bound session only |",
     "| `entry.intake` | orientation scout, in an owner-bound session only |", "P08 H2, actor")
edit(FS, "| the hook-written intake entry, carrying the session binding it came from,",
     "| the intake entry the scout writes, carrying the session binding it came from,", "P08 H2, witness")
edit(FS, "records the transition; under `plan.ratification: request`, the intake record stands as the ratification",
     "records the transition; under `plan.ratification: request`, the owner's go, as the planner records it, stands as the "
     "ratification", "P09 H1")
edit(V2, "workspaces by `build.worktree`, the commit queue, integration before release and the sweep",
     "workspaces by `build.worktree`, integration before release and the sweep", "P10 H6, 0289")
edit(V2, "the commit queue committing each role return into the build's trail at its item's witness",
     "each role agent committing its own return into the build's trail at its item's witness", "P10 H6, 0318")
edit(LM, "| dupes | dRankedPlan | its writer is `plan.dedupe` |",
     "| dupes | dRankedPlan | the duplicate and overlap record; writer item not named |", "P11 kind writer")
edit(V2, "; claims keyed and trusted by key and source `cl-dClosedLoop-0093`", "", "P12 principle clause")
# The sentences naming candidate plants, cut.
edit(FQ, r"reverted into a sealed clone outside the repository, among\s+them the session model's H1, H2 and H6, the failure "
         r"route, the supervisor restart and a dropped kind writer, the key", "reverted into a sealed clone outside the "
         "repository, the key", "cut, final-questions [audit]", regex=True)
edit(RA, r"- \*\*The plants\.\*\* Twelve fixed past defects are reverted into it, for example:\n.*?which Stage 0 must catch "
         r"100% of\.\n", "- **The plants.** Twelve fixed past defects are reverted into it.\n",
     "cut, research-final-audit [5]", regex=True)
edit(WA, r"Two are mechanical, a kind's writer dropped and a principle's enforcing\s+clause dropped, and Stage 0",
     "Two are mechanical, and Stage 0", "cut, the round record's [recall]", regex=True)
files[IR] = ("# Instruments: the night pass\n\n**Serves:** research PLAY-dClosedLoop-1\n\nKept out of the audit's sealed "
             "copy: it carries the audit's own instruments whole. The working tree holds it.\n")
for rel, t in files.items():
    (COPY / rel).write_text(t, encoding="utf-8", newline="\n")


def git(*args):
    return subprocess.run(["git", "-C", str(COPY), *args], capture_output=True, text=True, check=True).stdout


git("init", "-q")
git("add", "-A")
git("-c", "user.name=walk", "-c", "user.email=walk@localhost", "commit", "-q", "-m", "the design under audit")
r = subprocess.run([sys.executable, "-X", "utf8", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py", "--out",
                    str(COPY / "design-map.txt")], cwd=COPY, capture_output=True, text=True)
print("map:", (r.stdout + r.stderr).strip().split("\n")[0], "rc", r.returncode)
WORDS = {"fail": ["fail", "killed", "interrupt", "stop"], "alias": ["alias", "journal", "rename"]}
plants = [
    ("P01", "architecture-v2", "chain", ["cl-dClosedLoop-0018", "cl-dClosedLoop-0019", "cl-dClosedLoop-0021"],
     ["fail", "killed", "interrupt", "stop"], False, "the shape audit's walk-failure-route"),
    ("P02", "architecture-v2", "chain", ["cl-dClosedLoop-0229", "cl-dClosedLoop-0231"], ["alias", "journal", "rename"],
     False, "the shape audit's journal-rename"),
    ("P03", "architecture-v2", "chain", ["cl-dClosedLoop-0284", "cl-dClosedLoop-0303", "cl-dClosedLoop-0310"],
     ["restart", "second act", "two act", "duplicate", "re-adopt", "reconcil"], False, "the shape audit's supervisor-restart"),
    ("P04", "architecture-v2", "chain", ["cl-dClosedLoop-0305", "cl-dClosedLoop-0377"], ["origin", "ratif"], False,
     "the shape audit's intake-ratification"),
    ("P05", "architecture-v2", "chain", ["cl-dClosedLoop-0488", "cl-dClosedLoop-0478"], ["declin", "refus", "reject"], False,
     "the shape audit's declined-retirement"),
    ("P06", "flow-steps", "entry", ["entry.claim"], ["unreachable", "offline", "remote"], False, "the design audit's M13"),
    ("P07", "architecture-v2", "chain", ["cl-dClosedLoop-0283", "cl-dClosedLoop-0378"],
     ["drain", "fallback", "in flight", "migrat"], False, "the design audit's M15"),
    ("P08", "flow-steps", "entry", ["entry.intake"], ["agent", "typed", "verbatim", "scout", "hook", "witness"], False,
     "the session model's H2"),
    ("P09", "flow-steps", "plan", ["plan.exit"], ["ratif", "typed", "planner", "agent"], False, "the session model's H1"),
    ("P10", "architecture-v2", "chain", ["cl-dClosedLoop-0289", "cl-dClosedLoop-0318", "build.worktree"],
     ["index", "lock", "concurren", "serial", "commit queue", "parallel"], False, "the session model's H6"),
    ("P11", "layer-memory", ["contract", "design"], ["dupes"], ["writer"], True, "mechanical: a kind's writer dropped"),
    ("P12", "architecture-v2", ["chain", "enforcement", "principles"], ["cl-dClosedLoop-0093", "P23"],
     ["P23", "claim", "trusted", "enforc"], True, "mechanical: a principle's only enforcing clause dropped"),
]
key = {"base": BASE, "plants": [{"id": i, "record": rec, "tag": tag, "anchors": anchors, "words": words,
                                 "mechanical": mech, "source": src} for i, rec, tag, anchors, words, mech, src in plants]}
path = HERE / "key.json"
path.write_text(json.dumps(key, indent=1) + "\n", encoding="utf-8", newline="\n")
print(f"copy {COPY.as_posix()} at {git('rev-parse', 'HEAD').strip()[:9]} from {BASE[:9]}; plants {len(plants)}; key "
      f"{path.as_posix()} sha256 {hashlib.sha256(path.read_bytes()).hexdigest()}")
