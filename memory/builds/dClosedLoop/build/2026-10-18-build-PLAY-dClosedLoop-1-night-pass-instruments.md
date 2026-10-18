# Instruments: the night pass

**Serves:** research PLAY-dClosedLoop-1

The scripts the night pass ran or wrote, the researchers' probes, the red runs as they were captured, and the final
run of every check, re-run when this record was written. The record they serve is
`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`. Scripts live in the session's scratchpad, and are kept here
whole.

## [scripts] The night pass's own scripts

### `save_return.py`

Saves an agent's final return verbatim from its transcript, so no return passes through a retyping.

````python
"""Save one agent's final return, verbatim, as a research record in the build folder.

Usage: python -X utf8 save_return.py <transcript.jsonl> <record-name> <title> <dispatch> <prompt-file> <use>
  record-name  e.g. research-unattended-core, saved as build/2026-10-18-build-PLAY-dClosedLoop-1-<record-name>.md
  title        the record's H1, after "Research: "
  dispatch     the session log's dispatch number
  prompt-file  the handoff's file name under prompts/
  use          where the return is used, a record name under build/

Reads the transcript's last assistant message, joins its text blocks, demotes any H1 to bold, and writes the
record. Prints the record's path, its size and the return's first line only. Refuses to overwrite.
"""
import json
import pathlib
import re
import sys

src, name, title, dispatch, prompt, use = sys.argv[1:7]
last = None
with open(src, encoding="utf-8") as f:
    for line in f:
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        msg = ev.get("message") if isinstance(ev, dict) else None
        if ev.get("type") == "assistant" and isinstance(msg, dict):
            texts = [b.get("text", "") for b in msg.get("content", []) if isinstance(b, dict) and b.get("type") == "text"]
            if any(t.strip() for t in texts):
                last = "\n".join(t for t in texts if t.strip())
if not last:
    sys.exit("no assistant text in " + src)
body = re.sub(r"^# (.+)$", r"**\1**", last.replace("\r\n", "\n").strip("\n"), flags=re.M)
out = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-%s.md" % name)
if out.exists():
    sys.exit("%s exists" % out)
head = ("# Research: %s\n\n**Serves:** research PLAY-dClosedLoop-1\n\n"
        "This is dispatch %s's return, verbatim, except that a title line would be demoted to keep one H1 per record. "
        "Its question is in `prompts/%s`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-%s.md`.\n\n---\n\n"
        % (title, dispatch, prompt, use))
out.write_text(head + body + "\n", encoding="utf-8", newline="\n")
print("%s · %d bytes · first line: %s" % (out, out.stat().st_size, body.split("\n", 1)[0][:100]))
````

### `fold_state.py`

Point 7: each progress row's fold state as the atlas derives it, red on a row read unfolded despite a fold section.

````python
"""Print each progress row's review count and fold state, as the atlas derives them, and the pill the page draws.

Usage: python -X utf8 fold_state.py [<atlas.py>]   (from the worktree root; default: the build's generator)
Exit 1 when a row with reviews reads unfolded while one of its records holds a section whose tag ends in "fold".
"""
import importlib.util
import pathlib
import re
import sys

path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
                    "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py")
spec = importlib.util.spec_from_file_location("atlas", path)
atlas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atlas)
data = atlas.derive()
missed = 0
for p in data["progress"]:
    pill = ("reviewed x%d · folded" % len(p["reviews"]) if p["folded"]
            else "in review" if p["reviews"] else "review owed")
    marks = sorted({m for n in p["records"] for m in re.findall(r"^## \[([a-z0-9-]*fold)\]",
                                                              atlas.text(atlas.HERE / n), flags=re.M)})
    flag = ""
    if p["reviews"] and not p["folded"] and marks:
        flag = "  <- unfolded, yet it holds " + ", ".join("[%s]" % m for m in marks)
        missed += 1
    print("%-14s reviews %d  %-22s%s" % (p["layer"], len(p["reviews"]), pill, flag))
print("rows read unfolded despite a fold section: %d" % missed)
sys.exit(1 if missed else 0)
````

### `fix_map_layer.py`

The design map's kit-to-layer join and its arm, applied with `--arm-only` first to see the arm red.

````python
"""Join each kit node to its layer on the design map, and arm a check that it does.

The map compared the instruction layer's kits table's prose layer cell ("Instruction: renders the charter") and its
compound kit cells ("codebase-map, lexicon, memory-recall") with lowercase layer tags, so 0 of 19 kits carried a
layer link, and nothing checked it. Found by dispatch 104 (`research-tool-fates.md`, section 5, item 12).

Usage: python -X utf8 fix_map_layer.py [--arm-only]   (from the worktree root; --arm-only leaves the old join, to see the arm red)
"""
import pathlib
import sys

P = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py")
t = P.read_text(encoding="utf-8")


def sub(old, new, label):
    global t
    if t.count(old) != 1:
        sys.exit(f"{label}: the anchor matches {t.count(old)} times")
    t = t.replace(old, new, 1)


sub('''DECLARED = set()
''', '''DECLARED = set()
# Kits whose row in the instruction layer's kits table says "no layer"; every other kit joins a layer (the layer arm).
NO_LAYER = set()
''', "global")

if "--arm-only" not in sys.argv:
  sub('''    kit_layer = {k["kit"].strip("`").split("/")[-1].strip(): k["layer"] for k in A["kits"]}
    layer_tags = {l["tag"] for l in A["layers"]}
''', '''    # The instruction layer's kits table names one kit, or several joined by ", " or " and ", and opens its layer cell
    # with a layer's name, or two joined by " and ". A row whose kind cell says "no layer" places its kits on none.
    kit_layer = {}
    for row in A["kits"]:
        lead = re.match(r"\\s*([A-Za-z]+(?:\\s+and\\s+[A-Za-z]+)?)", row["layer"])
        lays = [w.lower() for w in re.split(r"\\s+and\\s+", lead.group(1))] if lead else []
        for name in re.split(r",\\s*|\\s+and\\s+", row["kit"]):
            name = name.strip().strip("`").split("/")[-1].strip()
            kit_layer.setdefault(name, lays)
            if row["kind"].strip() == "no layer":
                NO_LAYER.add(name)
    layer_tags = {l["tag"] for l in A["layers"]}
''', "kit_layer")

if "--arm-only" not in sys.argv:
  sub('''        lay = kit_layer.get(k, "")
        kits.append(node(k, purpose, src="derived", rels=[("layer", [lay] if lay in layer_tags else [])]))
''', '''        kits.append(node(k, purpose, src="derived", rels=[("layer", [l for l in kit_layer.get(k, []) if l in layer_tags])]))
''', "kit node")

sub('''    elif plant == "ghost-rel":
        i = next(i for i, ln in enumerate(lines) if ln.startswith("- chain."))
        lines[i] += " owner=dGhostBuild"
''', '''    elif plant == "ghost-rel":
        i = next(i for i, ln in enumerate(lines) if ln.startswith("- chain."))
        lines[i] += " owner=dGhostBuild"
    elif plant == "no-layer":
        i = next(i for i, ln in enumerate(lines) if ln.startswith("- kit.") and " layer=" in ln)
        lines[i] = re.sub(r" · layer=\\S+", "", lines[i])
''', "plant")

sub('''    if any(re.search(r"\\b20\\d\\d-\\d\\d-\\d\\d\\b", ln) for ln in lines[2:]):
''', '''    # Layer: every kit line joins a layer, unless its kits-table row says "no layer" (dispatch 104 found all 19 empty).
    for ln in lines[2:]:
        m = LINE.match(ln)
        if m and m.group(1) == "kit" and m.group(2) not in NO_LAYER and " layer=" not in ln:
            findings.append(f"layer: kit.{m.group(2)} joins no layer")
    if any(re.search(r"\\b20\\d\\d-\\d\\d-\\d\\d\\b", ln) for ln in lines[2:]):
''', "arm")

sub('''      cases: drop-line, bad-count, ghost-rel, census, no-owner, orphan (an item's owner emptied), two-owners,''',
    '''      cases: drop-line, bad-count, ghost-rel, no-layer, census, no-owner, orphan (an item's owner emptied), two-owners,''',
    "usage")

P.write_text(t, encoding="utf-8", newline="\n")
print("map.py: the kit layer join and its arm")
````

### `paren_semis.py`

The clause scan, extended to double quotes.

````python
"""Find every [chain] row whose planned-units cell holds "; " inside parentheses, backticks or double quotes, where the
unit count's split on "; " cuts one clause into several.

Usage: python -X utf8 paren_semis.py   (from the worktree root); exit 1 when any is found
"""
import re
import sys

v2 = open("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
found = 0
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
    if not m:
        continue
    depth, tick, quote, at = 0, False, False, []
    cell = m.group(2)
    for i, ch in enumerate(cell):
        if ch == "`" and not quote:
            tick = not tick
        elif ch == '"' and not tick:
            quote = not quote
        elif not tick and ch == "(":
            depth += 1
        elif not tick and ch == ")":
            depth = max(0, depth - 1)
        elif cell.startswith("; ", i) and (depth or tick or quote):
            at.append(i)
    for i in at:
        found += 1
        print(f"{m.group(1)}: ...{cell[max(0, i - 70):i + 50]}...")
print(f"splits inside a clause: {found}")
sys.exit(1 if found else 0)
````

### `fold_np_v2.py`

v2: the revision note, the principles, the keys and their preset rows, the chain's clauses and gaps, and the owed checks.

````python
"""Fold the night pass into architecture v2: the revision note, the principles, the keys and their preset rows, the
chain rows' new and amended clauses with the gaps each now owns, and the owed checks.

Usage: python -X utf8 fold_np_v2.py   (from the worktree root); refuses unless every anchor matches exactly once.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

V = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
NP = "`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`"

# 1. The revision note, after the audit fold's closing review's note.
V.sub("""- the review's other items are folded row by row, each marked with its item.

Revised: 2026-10-17, after the folds' closing review""", f"""- the review's other items are folded row by row, each marked with its item.

Revised: 2026-10-18, the night pass ({NP}), the owner's eight points worked in while the owner was away:
- unattended is the core flow's default state, and attendance an override that adds only the owner's interactions:
  P4, P20 and P25 amended, `attendance` and `attendance.scope` added, the unattended kit dissolved into the chain, and
  playbook mode seated through the `repeat` disposition and the playbook record kind (point 1);
- testing happens wherever the work needs it: P31, the probe program and its keys, the tester agent, the experiment
  shape and the visual witness (point 2);
- every role sees the code its item touches: P32, the core `code` record replacing the optional symbols and callers,
  and a `code` slot per item (point 3);
- one relational syntax across memory: P33, the closed edge set, the span rule and `gov tag bundle` (point 4);
- the compaction replay carries the whole default load and ends with `next`'s line (point 5);
- five practices from Anthropic's AI-native SDLC playbook (point 6);
- twenty-eight gaps registered, each owned, and the forks the owner's words leave open parked as NP-1 to NP-24, the
  defaults they set shown as recommendations until answered.

Revised: 2026-10-17, after the folds' closing review""", "revision note")

# 2. Principles.
V.sub("""- **P4 One contract, two authorizations.** Attended and unattended work run the same stage
  contracts; the autonomy level decides which transitions need the owner (R1.4).""",
      """- **P4 One flow, attended or not.** Unattended is the default state: the request is the mandate, and the
  driver carries a build from entry to its terminal state with no owner turn but those `autonomy` places.
  Attendance, set by `attendance` or by an attend request, adds only the owner's interactions: the announcement of
  each act's step and role, the owner's confirmations at breakpoints, and owner questions asked live. It never
  changes an item, its actor, the driver, a role's use or its enforcement (R1.4; the owner's point 1, night pass).""",
      "P4")
V.sub("""Builds run unattended past Plan by default, with the executor
  running the steps (flow record, walked 2026-10-14; layers round two).""",
      """Builds run unattended by default, from the request that is their
  mandate, with the executor running the steps (flow record, walked 2026-10-14; layers round two; night pass,
  point 1).""", "P20")
V.sub("""The main session
  drives and orients its sidechains: it does no role's work, and holds only composed cards, typed
  returns and cheap state reads (roles record).""",
      """The driver
  drives and orients its sidechains: the supervisor in every mode, or the owner's session while it hosts the
  driver (night pass, point 1). It does no role's work, and holds only composed cards, typed
  returns and cheap state reads (roles record).""", "P25")
V.sub("""  (Layers round four.)

## [front-door]""", """  (Layers round four.)
- **P31 Testing happens wherever the work needs it.** A probe, a verification, a reproduction or an experiment, is
  placed at any item boundary by the driver, the owner or a policy, or raised by any role as the outcome of its
  item. It pins its subject by SHA, commits its losing outcome before it runs, and returns a typed record to the item
  that asked (P26). Its verdict is computed by a re-run or a scorer, and an agent's judgment is held as claimed (P2).
  Test stays the landing verdict, the one test that gates a landing (the owner's point 2, night pass).
- **P32 Every role sees the code its item touches.** The core derives a code record from the tree: files,
  definitions with their ranges, imports, resolved calls, tests and kit membership, cached by tree hash. Each item
  declares a seed, and its work order carries the seed's code neighbourhood as ranges, never bodies: its
  definitions, their callers, callees and tests, and their kit's siblings. Purposes are derived first and enriched
  by an agent, each keyed to its definition's body hash, so a stale one is found, never trusted. `git grep` is the
  floor where no extractor runs (the owner's point 3, night pass).
- **P33 One relational syntax.** Every part of memory and code is a node named by a tag, and parts relate by typed
  edges from one closed set, each declared once at the site that owns its fact, its inverse derived. A span is
  derived where a definition's extent is known, and marked only where it is not. Pulling a tag returns its bundle:
  every member, region and instruction joined to it, as a manifest of ranges under a row budget (the owner's
  point 4, night pass).

## [front-door]""", "P31 to P33")

# 3. The keys, each beside its family, and their preset rows.
PEND = "night pass, pending {}; the default shown is the recommendation until the owner answers"
V.insert_before("| `policy.guard` | owner-only, agents-with-reason, agents-within-mandate |", (
    "| `attendance` | unattended, announce, confirm-steps, confirm-acts | unattended | the owner's point 1, night pass: "
    "unattended is the default state; which attended value a bare attend request selects, " + PEND.format("NP-2") +
    " | dDeclaredLoop |\n"
    "| `attendance.scope` | session, build, repository | build | how long an attend or unattend request holds, " +
    PEND.format("NP-3") + " | dWellOiledMachine |\n"), "attendance keys")
review_bp = next(l for l in V.text.split("\n") if l.startswith("| `review.breakpoints` | a set of named item boundaries |"))
V.sub(review_bp + "\n", review_bp + "\n" + (
    "| `probe.points` | a set of named item boundaries | none | the owner's point 2, night pass: probes placed beyond "
    "those `probe.observations` owes and the roles raise | dDeclaredLoop |\n"
    "| `probe.raise` | roles-and-owner, owner-only, off | roles-and-owner | the owner's point 2: \"roles need to be able "
    "to work a problem out by testing\" | dDeclaredLoop |\n"
    "| `probe.observations` | verify-before-place, verify-at-plan, on-request | verify-before-place | an owner's "
    "observation in a request, " + PEND.format("NP-7") + " | dDeclaredLoop |\n"
    "| `probe.experiment.authority` | owner-opts-in, within-cap, free | owner-opts-in | aScoutedSeam's one re-run spent "
    "195 agents, " + PEND.format("NP-6") + " | dDeclaredLoop |\n"
    "| `probe.verifier` | tester, asking-role, researcher | tester | who verifies cold, " + PEND.format("NP-5") +
    " | dDeclaredLoop |\n"), "probe keys")
default_load = next(l for l in V.text.split("\n") if l.startswith("| `memory.default-load` | card, card-and-live, card-and-map |"))
V.sub(default_load + "\n", default_load + "\n" + (
    "| `memory.code-budget` | 4k, 8k, 16k | 8k | the `code` slot's budget, ranges and never bodies, " +
    PEND.format("NP-8") + " | dBoundRoles |\n"
    "| `memory.code-roles` | working-roles, every-role, structural-roles | working-roles | the working roles are the spec "
    "writer, builder, researcher, architect and reviewer, and the prompt writer through its actor, " +
    PEND.format("NP-9") + " | dBoundRoles |\n"
    "| `memory.code-languages` | python-shell-js, file-level-only, ctags | python-shell-js | other languages at file "
    "level, `git grep` the floor, " + PEND.format("NP-10") + " | dTotalRecall |\n"
    "| `memory.code-enrich` | symbol-hash-slots, in-code-notes, derived-only | symbol-hash-slots | purposes keyed to a "
    "definition's body hash, " + PEND.format("NP-11") + " | dTotalRecall |\n"), "code keys")
bare = next(l for l in V.text.split("\n") if l.startswith("| `tags.bare-refs` | charter-only, unique, never |"))
V.sub(bare + "\n", bare + "\n" + (
    "| `tags.bundle` | manifest, inline, both | manifest | what `gov tag bundle` returns, " + PEND.format("NP-14") +
    " | dOrderedCharter |\n"
    "| `tags.bundle-rows` | 20, 40, 80 | 40 | night pass, point 4: the `roles` feature's bundle runs about 44 rows "
    "unfolded and 39 with its kit folded | dOrderedCharter |\n"), "bundle keys")

V.sub("""- Presets never touch the floor, `preset` itself, `policy.guard`, `policy.proof`, `policy.on-invalid`,
  `charter.practices`,
  `instructions.edit`, `instructions.proof`, `policy.on-missing-expansion`, `release.environments` or
  `verdict.remote.pin`:
  loosening the guard or switching an invariant off stays an explicit owner choice, never a side
  effect of picking a posture; a methodology is a choice about the product, not a posture; and a
  repository's environments and its pinned workflow are facts about it.""",
      """- Presets never touch the floor, `preset` itself, `policy.guard`, `policy.proof`, `policy.on-invalid`,
  `charter.practices`,
  `instructions.edit`, `instructions.proof`, `policy.on-missing-expansion`, `release.environments`,
  `verdict.remote.pin`, `attendance` or `attendance.scope`:
  loosening the guard or switching an invariant off stays an explicit owner choice, never a side
  effect of picking a posture; a methodology is a choice about the product, not a posture; a
  repository's environments and its pinned workflow are facts about it; and whether the owner attends is
  the owner's own choice (night pass, point 1).""", "never-touch")

for key, rest in (("review.breakpoints", "| `probe.points` | none | none | none | none |\n"
                   "| `probe.raise` | roles-and-owner | roles-and-owner | roles-and-owner | roles-and-owner |\n"
                   "| `probe.observations` | on-request | verify-before-place | verify-before-place | verify-before-place |\n"
                   "| `probe.experiment.authority` | within-cap | owner-opts-in | owner-opts-in | owner-opts-in |\n"
                   "| `probe.verifier` | tester | tester | tester | tester |\n"),
                  ("memory.default-load", "| `memory.code-budget` | 8k | 8k | 16k | 8k |\n"
                   "| `memory.code-roles` | working-roles | working-roles | every-role | working-roles |\n"
                   "| `memory.code-languages` | python-shell-js | python-shell-js | python-shell-js | python-shell-js |\n"
                   "| `memory.code-enrich` | derived-only | symbol-hash-slots | symbol-hash-slots | symbol-hash-slots |\n"),
                  ("tags.bare-refs", "| `tags.bundle` | manifest | manifest | manifest | manifest |\n"
                   "| `tags.bundle-rows` | 40 | 40 | 40 | 40 |\n")):
    exact = {"review.breakpoints": "| `review.breakpoints` | none | none | none | none |",
             "memory.default-load": "| `memory.default-load` | card-and-map | card-and-map | card-and-map | card-and-map |",
             "tags.bare-refs": "| `tags.bare-refs` | unique | charter-only | never | charter-only |"}[key]
    V.sub(exact + "\n", exact + "\n" + rest, f"preset rows after {key}")

# 4. The chain: amended clauses, then new clauses and owned gaps, row by row.
AMEND = [
    ("dTotalRecall", "the caller map: every Python definition, import-aware calls, shell and JavaScript edges under the "
     "ambiguity test, cross-language invocation edges, freshness-checked, with dossiers anchored to symbol keys",
     "the core `code` record (night pass, point 3), replacing the optional symbols and callers: files, definitions with "
     "their ranges and body hashes, imports, every Python definition with import-aware calls, shell and JavaScript "
     "edges under the ambiguity test, cross-language invocation and registry edges, tests and kit membership, derived "
     "per blob through the shared extraction primitive in the languages `memory.code-languages` names and cached by "
     "tree hash, freshness-checked, with dossiers anchored to symbol keys"),
    ("dBoundRoles", "with its kind (`single`, `per-unit`, `panel`, `twin`)",
     "with its kind (`single`, `per-unit`, `panel`, `twin`, and `experiment`, whose cases, variants, bounded fan, "
     "scorer or blind judge and re-runs keyed by variant and effort come from aScoutedSeam's benchmark, night pass "
     "point 2)"),
    ("dWellOiledMachine", "the owner's pause, resume, withdraw and supersede through the guarded command, mapped onto "
     "unattended's verbs", "the owner's pause, resume, withdraw and supersede through the guarded command, mapped onto "
     "unattended's verbs, and attend and unattend, each writing an `override` record scoped by `attendance.scope` "
     "(night pass, point 1)"),
    ("dWellOiledMachine", "the compact hook re-injecting the build's current card, never the kickoff's, the PreCompact "
     "flush and the keep-list", "the compact hook re-injecting the build's current card, never the kickoff's, the "
     "PreCompact flush and the keep-list, the keep-list naming the classes a summary drops (handles, a decision's "
     "condition, rejected options, open forks), and each compaction journaled with its session, build, item in flight "
     "and trigger (night pass, point 5)"),
    ("dWellOiledMachine", "the session-start hook loading the set `memory.default-load` names, the card and the map in "
     "an attended session (PM-7, PM-12)", "the session-start hook loading the set `memory.default-load` names, the card "
     "and the map by default in the owner's session, at startup, at resume and at a compaction, ending with `next`'s "
     "line computed at that moment (PM-7, PM-12, night pass point 5)"),
    ("dIndexedDesign", "the research harness", "the research harness, built on the `experiment` shape (night pass, "
     "point 2)"),
    ("dCalibratedLens", "computed from the author's slice manifest and the map", "computed from the author's slice "
     "manifest, the map and the `code` slot (night pass, point 3)"),
    ("dConvergedCharter", "each described \"Use when …; runs …\"", "each described \"Use when …, runs …\""),
]
ADD = {
    "dOrderedCharter": (["a build run unattended by default from its request, said in the drive section, and the "
                         "charter's `[land]` rule read through the request's mandate (night pass, point 1)",
                         "the edge-type registry and the `edge` grammar: one closed set of typed edges, each declared "
                         "once at the site that owns its fact and its inverse derived, with `feature` added as an "
                         "instruction selector (night pass, point 4)",
                         "`gov tag bundle`, returning a tag's members, regions and instructions as a manifest of ranges "
                         "under `tags.bundle-rows`, folded past it, with its type-registered and target-resolves checks "
                         "each seen red (night pass, point 4)",
                         "file:line citations joined to the positional population `tags.positional` holds, new text "
                         "citing `path#symbol` or a blob-pinned line, as NP-17 settles (night pass, point 4)",
                         "each role's load set budgeting the `code` slot (night pass, point 3)"],
                        ["gap-found-24", "gap-found-25", "gap-found-26"]),
    "dFairHearing": (["the scorer factory: one deterministic scorer that re-derives every figure from committed raw "
                      "outputs, pairs the cases every variant answered and refuses a partial population, extracted from "
                      "`review_replay.py` with aScoutedSeam's grader as its second instance (night pass, point 2)"],
                     ["gap-test-18"]),
    "dDeclaredLoop": (["the attendance rule: `attendance` places owner breakpoints, turns the `step —` announcement on "
                       "and has owner questions asked live, and never selects an item's actor, the driver or a binding, "
                       "its arm seen red on a planted value that swaps an actor (night pass, point 1)",
                       "the `repeat` disposition in the placement set, routing a request onto a playbook (night pass, "
                       "point 1)",
                       "the probe program (`probe.trigger`, `probe.pin`, `probe.design`, `probe.run`, `probe.judge`, "
                       "`probe.return`) and the `probe` record kind, a probe placed at any item boundary by "
                       "`probe.points` or the owner and raised by any role's `probe` outcome under `probe.raise`, its "
                       "record handed to the asking item, an entry-time probe keyed by content as triage is (night "
                       "pass, point 2)",
                       "each item's declared code seed: its write set, its scope paths or its question's paths (night "
                       "pass, point 3)"],
                      ["gap-flow-16", "gap-flow-18"]),
    "dWitnessedBar": (["the probe witness: the executor re-running a probe's declared commands at its pinned SHA, a "
                       "figure an agent judged kept as claimed (night pass, point 2)",
                       "a fix pass that keeps its check: its allowance excluding the red leg's own test files and gate "
                       "script, a change to them routed through the tester's wrong-spec judgment to Design as a new "
                       "unit (night pass, point 6)",
                       "the playbook set record and its set check at Test (night pass, point 1)",
                       "the `tests=` and `enforces=` edge fields on legs (night pass, point 4)"],
                      ["gap-test-19"]),
    "dBoundRoles": (["the tester agent, absent today, with its allowance (scratch, and the browser where the harness "
                     "has it), and the `probe` outcome on every role's return template (night pass, point 2)",
                     "owner questions asked live while the build is attended, best effort recorded once the wait "
                     "passes (night pass, point 1)",
                     "the `code` slot rendered per item from its declared seed: the seed's definitions with their "
                     "ranges, their callers, callees and tests and their kit's siblings, as ranges under "
                     "`memory.code-budget`, for the roles `memory.code-roles` names, with the map's delivery extended "
                     "to the researcher and the prompt writer (night pass, point 3)",
                     "the work order selecting instruction units by `feature.*`, and the code-notes slot filled from "
                     "the tag's bundle (night pass, point 4)"],
                    ["gap-roles-21", "gap-roles-22"]),
    "dTotalRecall": (["`gov map code` and `gov code show`, `callers`, `tests` and `where`, `git grep` the engine of "
                      "`where` and the floor for a language with no extractor, the map's level 0 holding one counted "
                      "`code` line (night pass, point 3)",
                      "the enrichment workflow: purposes derived first from docstrings and headers, an agent's pass for "
                      "the rest as `memory.code-enrich` says, each keyed to its definition's body hash and stale when "
                      "the hash moves, joined both ways with a pending population (night pass, point 3)",
                      "the replay's losing test extended to code: a unit's files read and its lookups counted, with the "
                      "`code` slot and without it (night pass, point 3)",
                      "extractors emitting typed edges from annotations, front matter, dossiers and decision rows, "
                      "`decides` written on decision rows, and the span rule: a definition's extent where one derives, "
                      "`gov:end <tag>` only where none does (night pass, point 4)",
                      "the region-parser factory in `tools/lib`, today's five region parsers re-pointed to it (night "
                      "pass, point 4)",
                      "the dossier's header becoming the feature node and its prose moving into units and records, as "
                      "NP-16 settles (night pass, point 4)"],
                     ["gap-mem-28", "gap-mem-29", "gap-mem-30", "gap-mem-31", "gap-mem-32", "gap-mem-33"]),
    "dWellOiledMachine": (["the supervisor the only driver in every mode, the owner's session its client, and before "
                           "this build lands the owner's session hosting the same driver program under the same act "
                           "binding (night pass, point 1)",
                           "the `step —` announcement before each act while attended, and once when attendance begins, "
                           "rendered from `next` and the item's declaration, never typed by a model (night pass, "
                           "point 1)",
                           "intake for a prompt that reaches no owner session, through the mailbox's `intake` message "
                           "or a cadence filer (night pass, point 1)",
                           "the unattended kit dissolved into the loop kit and the runtime's own kit: its hooks "
                           "repacked, its supervisor seam taken, `/unattended` a client of `run` until dConvergedCharter "
                           "retires it (night pass, point 1)",
                           "a measured `browser` row in each harness adapter's capability table, and the "
                           "`visual.capture` command adapter: the pinned tree served, the cache busted, the declared "
                           "viewports taken, screenshots kept by hash after the secret scan, console and DOM results "
                           "returned (night pass, point 2)",
                           "act binding and shape-run rows for an experiment's acts (night pass, point 2)",
                           "a hook pack's refusal text, naming its rule and its remedy, declared in the pack's contract "
                           "and checked at registration (night pass, point 6)"],
                          ["gap-rt-22", "gap-rt-23", "gap-rt-24", "gap-orient-16", "gap-orient-17", "gap-orient-18"]),
    "dIndexedDesign": (["the playbook record kind: dScriptedRepeat's canon, its declaration block, pieces and sets "
                        "identified by hash, amendment by proposal, and `check-playbook` as Design's pack (night pass, "
                        "point 1)",
                        "the structured spec declaring `implements=` and `decides=` edges, and `design.seams` reading a "
                        "tag's bundle (night pass, point 4)"],
                       ["gap-flow-17"]),
    "dRankedPlan": (["`plan.record` declaring the probes owed before Design (night pass, point 2)",
                     "the plan record's intent fields: the affected systems derived from the `code` record and checked, "
                     "and the open questions as fork tags (night pass, point 6)"],
                    ["gap-plan-08"]),
    "dScopedBuild": (["a red-first reproduction, a `reproduction` probe, before a patch build's fix when the build comes "
                      "from a bug report (night pass, point 2)",
                      "a playbook's pieces built as units with piece records joined by hash, and a proposal to amend "
                      "the playbook filed as an ask (night pass, point 1)"],
                     []),
    "dTendedCadence": (["a cyclic playbook's cadence item, filing `repeat` intakes (night pass, point 1)",
                        "a detector for bundle members whose code changed while their head line did not (night pass, "
                        "point 4)"],
                       []),
    "dCalibratedLens": (["probe cost priced in the value ledger, and compactions counted per item kind as a sizing "
                         "signal (night pass, points 2 and 5)",
                         "instruction evals: a replay suite of recorded items with known outcomes, re-run as a held leg "
                         "when an instruction unit changes, a confirmed finding whose cause is an instruction adding a "
                         "case (night pass, point 6)",
                         "the Loop Review's delivery metrics: lead time, landing frequency, change failure rate, time "
                         "to restore, first-pass verdict rate, route-backs per build and scope drift (night pass, "
                         "point 6)"],
                        ["gap-review-14", "gap-review-15"]),
    "dMindYourWords": (["the overloaded terms settled: attended as a session kind and as a mode, playbook as the "
                        "charter renderer and as playbook mode, and baseline as retrofit's debt and as a measured "
                        "reference (night pass, points 1 and 2)"],
                       ["gap-lex-09"]),
    "dConvergedCharter": (["the unattended kit, its four guides and `/unattended` retired once dWellOiledMachine's "
                           "driver carries every run, the kit's README and the product rule's \"four-verb driver\" "
                           "corrected with them (night pass, point 1)",
                           "feature-specific guide prose migrated into feature-scoped units (night pass, point 4)",
                           "every part in the fates table at its fate, the table's join run as convergence's exit check "
                           "(night pass, point 8)"],
                          ["gap-tool-08", "gap-tool-09"]),
}
ROW = re.compile(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| ([^|]+) \|$", re.M)


def row_of(build):
    rows = [m for m in ROW.finditer(V.text) if m.group(1) == build]
    if len(rows) != 1:
        sys.exit(f"{build}: {len(rows)} chain rows")
    return rows[0]


for build, old, new in AMEND:
    m = row_of(build)
    if m.group(4).count(old) != 1:
        sys.exit(f"{build}: the clause to amend matches {m.group(4).count(old)} times: {old[:60]}")
    line = m.group(0)
    V.sub(line, line.replace(old, new, 1), f"{build} amend")
for build, (clauses, gaps) in ADD.items():
    for c in clauses:
        if "; " in c or "|" in c:
            sys.exit(f"{build}: a clause holds a separator: {c[:60]}")
    m = row_of(build)
    units = m.group(4) + "; " + "; ".join(clauses)
    owned = m.group(5).strip() + (", " + ", ".join(gaps) if gaps else "")
    V.sub(m.group(0), f"| {build} | {m.group(2)} | {m.group(3)} | {units} | {owned} |", f"{build} add")

# 5. The owed checks.
if not V.text.endswith("\n"):
    sys.exit("v2 does not end with a newline")
V.text += f"""- **The night pass's owed checks** ({NP}):
  - the compact and resume hooks' output cap, measured with a 32 KiB map, so the default load comes back whole
    (point 5);
  - the platform spike decides where the driver runs: if a role-typed Workflow agent cannot run inside a headless
    act session, the owner's session keeps hosting the driver, bound as an act session (point 1, NP-1);
  - the span share re-measured with the map's own extractors: the hybrid loses if 80% or more of a feature's outside
    spans sit in a derivable definition (point 4);
  - the code record's cold derivation re-timed at dTotalRecall's first unit: over 30 s or over 1 MB loses (point 3);
  - the level-0 map's headroom, 30,304 of 32,768 B with the kits' layer links, budgeted for the `code` line before
    it lands (point 3).
"""
V.done += 1
V.save()
````

### `fold_np_v2b.py`

v2, second fold: the `feature` selector moved to dTotalRecall, and dBoundRoles' slots waiting on it.

````python
"""The night pass's second v2 fold, from the reconciliation probe's run over the first:
- dOrderedCharter's clause cited the `feature` namespace, which dTotalRecall registers later. The tag system's own rule
  arms a later namespace's join in the build that registers it, so the selector moves to dTotalRecall.
- dBoundRoles' two new slots read the `feature` namespace and the `code` record, both dTotalRecall's, a sibling. The
  probe cannot see `feature.*` or a record through a wildcard, so the slots take the map slot's existing pattern:
  each renders "not installed" until dTotalRecall lands.

Usage: python -X utf8 fold_np_v2b.py   (from the worktree root); refuses unless every anchor matches exactly once.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

V = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
V.sub("each declared once at the site that owns its fact and its inverse derived, with `feature` added as an instruction "
      "selector (night pass, point 4)",
      "each declared once at the site that owns its fact and its inverse derived, and the instruction selectors open to "
      "a namespace a later build registers (night pass, point 4)", "dOrderedCharter selector")
V.sub("the dossier's header becoming the feature node and its prose moving into units and records, as NP-16 settles "
      "(night pass, point 4)",
      "the dossier's header becoming the feature node and its prose moving into units and records, as NP-16 settles "
      "(night pass, point 4); the `feature` namespace armed as an instruction selector when it registers, as NP-13 "
      "settles (night pass, point 4)", "dTotalRecall selector")
V.sub("as ranges under `memory.code-budget`, for the roles `memory.code-roles` names, with the map's delivery extended "
      "to the researcher and the prompt writer (night pass, point 3)",
      "as ranges under `memory.code-budget`, for the roles `memory.code-roles` names, with the map's delivery extended "
      "to the researcher and the prompt writer, rendering \"not installed\" until dTotalRecall's `code` record lands "
      "(night pass, point 3)", "dBoundRoles code slot")
V.sub("the work order selecting instruction units by `feature.*`, and the code-notes slot filled from the tag's bundle "
      "(night pass, point 4)",
      "the work order selecting instruction units by `feature.*` once dTotalRecall arms that selector, and the "
      "code-notes slot filled from the tag's bundle (night pass, point 4)", "dBoundRoles feature selection")
V.save()
````

### `fold_np_flow.py`

flow-steps: `repeat`, the entry-time probe, `[rules]`, the attendance gates, `[probe]`, attend and unattend, and the fix pass.

````python
"""Fold the night pass into flow-steps: the `repeat` disposition and the entry-time probe, the `probe` outcome and the
attendance rule in `[rules]`, what attendance places at the breakpoint, the `[probe]` program, attend and unattend among
the owner's controls, and the fix pass that keeps its check in Test.

Usage: python -X utf8 fold_np_flow.py   (from the worktree root); refuses unless every anchor matches exactly once.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

F = Record("memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")

# [rules]
F.sub("""  - Routes are declared explicitly where a policy value decides them.
""", """  - Routes are declared explicitly where a policy value decides them.
  - Every role item's outcome set includes `probe`, routed to `[probe]` under `probe.raise`, the probe's record
    returned as the item's input on re-entry (night pass, point 2).
- **Attendance changes no item.** Whether the owner attends never changes an item's actor, the driver or a binding.
  It adds only the owner's interactions: the announcement, confirmations at breakpoints and owner questions asked
  live (P4; `[breakpoint]`; night pass, point 1).
""", "rules")

# [entry]
F.sub("| `entry.intake` | hook: prompt-submit, in an attended-bound session only |",
      "| `entry.intake` | hook: prompt-submit, in an owner-bound session only |", "intake actor")
F.sub("(continue, amend, new, patch, ask, none)", "(continue, amend, new, patch, repeat, ask, none)", "dispositions")
F.sub("patch → `entry.claim`, then Design as a patch build;",
      "patch → `entry.claim`, then Design as a patch build; repeat → `entry.claim`, then Design as a playbook run, its "
      "playbook supplying the feature design; an observation the request claims → `probe.trigger` first, as "
      "`probe.observations` says, and back to `entry.place` with the probe's record;", "place routes")
F.sub("| `entry.claim` | command | a `new` or `patch` disposition", "| `entry.claim` | command | a `new`, `patch` or "
      "`repeat` disposition", "claim needs")
F.sub("On `patch` it also takes the build's lease, which a patch build never reaches `plan.lease` to take",
      "On `patch` or `repeat` it also takes the build's lease, which such a build never reaches `plan.lease` to take",
      "claim lease")
F.sub("on `patch`, the lease record too | claimed → Plan, or Design on `patch`;",
      "on `patch` or `repeat`, the lease record too | claimed → Plan, or Design on `patch` or `repeat`;", "claim routes")
F.sub("""- **Whose prompt is intake.** Only a session whose binding record says "attended" writes intake. An
  act session is bound to its act, and a `claude -p` an attended model runs from its shell is unbound,
  so neither writes intake (Runtime's session binding).""",
      """- **Whose prompt is intake.** Only a session whose binding record says "owner" writes intake: the session the
  owner types in, attended or not, since attendance is a mode and not a kind of session (night pass, point 1). An
  act session is bound to its act, and a `claude -p` the owner's session runs from its shell is unbound,
  so neither writes intake (Runtime's session binding).""", "whose intake")
F.sub("""- trackers and adopter feedback, from integrations.
""", """- trackers and adopter feedback, from integrations.

A prompt that reaches no owner session, through the mailbox's `intake` message or a cadence filer, a cyclic
playbook's `repeat` included, is recorded as intake by dWellOiledMachine's filer and placed by `entry.place` the same
way (night pass, point 1).
""", "non-session intake")

# [breakpoint]
F.sub("""- `every-stage` adds a gate at every step's exit.
""", """- `every-stage` adds a gate at every step's exit.

`attendance` adds the owner's interactions while the owner attends (night pass, point 1):
- every attended value announces each act before it runs, with the `step —` line, and asks owner questions live;
- `confirm-steps` adds a gate at every step's exit, and `confirm-acts` one before every act;
- no value changes an item's actor, the driver or a binding, which the attendance rule's arm checks.
""", "attendance gates")

# [probe], before [lifecycle]
F.sub("## [lifecycle] The owner's controls: pause, resume, withdraw, supersede", """## [probe] The probe: testing at any boundary

Testing is not a step either (P31). A probe is one program with two ways in:
- **placed** at an item boundary, as a breakpoint is: by `probe.points`, by the owner's request, or owed by
  `probe.observations` when a request claims an observation;
- **raised** by a role as the outcome of its item, under `probe.raise`, as research is routed: the asking item waits,
  and the probe's record returns as its input on re-entry.

Test stays the landing verdict. Only `test.verdict`'s runner-written record gates a landing, and no probe's verdict
feeds `deploy.current`.

- **Its kinds:**
  - a **verification** checks a claim at a pinned SHA: an owner's observation, in the code or on screen;
  - a **reproduction** makes a reported bug red before its fix;
  - an **experiment** compares variants over a pre-registered corpus, and its record is the measured reference that
    later acceptance cites.
- **The driver knows a probe is owed,** because `next` returns the probe's items as the frontier while the asker
  waits (P22).

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `probe.trigger` | command | — | records why the probe opened: the boundary `probe.points` names, the owner's request, the observation `probe.observations` owes, or a role item's `probe` outcome under `probe.raise` | the trigger record, keyed by the boundary or the raising return, and by content for a probe before placement, which mints no id | opened → `probe.pin`; not opened → the flow continues | dDeclaredLoop |
| `probe.pin` | command | `probe.trigger` | pins the subject by SHA, and records the question, the kind and the losing outcome before anything runs | the probe record's head, its losing outcome committed first | `probe.design` | dDeclaredLoop |
| `probe.design` | the role `probe.verifier` names; for an experiment, the researcher | `probe.pin` | declares the method: the commands, or the `experiment` shape with its corpus, its variants and its judge | the method's schema check, and an experiment's fan checked against `probe.experiment.authority` | `probe.run`; an experiment beyond its authority → an owner item, resolved as `[breakpoint]`'s owner gate is | dDeclaredLoop |
| `probe.run` | executor | `probe.design` | runs the commands at the pinned SHA, or launches the experiment's harness, keeping each output by hash; a visual verification runs through the visual capture adapter | the captured outputs by hash, and an experiment's shape-run rows | `probe.judge`; no capability for the method → `probe.return`, the verdict unrunnable | dDeclaredLoop |
| `probe.judge` | command: the executor's re-run, or the experiment's scorer | `probe.run` | compares the outcome with the losing outcome: confirmed, refuted or inconclusive; an experiment measured, within noise or aborted | the re-run's or the scorer's computed verdict; where no command can judge, the verifier's judgment, recorded as claimed | `probe.return` | dDeclaredLoop |
| `probe.return` | command, idempotent, through `record` | `probe.judge` | writes the probe record and hands it to the asking item as an input, or to the item after the boundary | the probe record | the asking item's re-entry, or the boundary's next item; a claimed verdict → an owner item, resolved as `[breakpoint]`'s owner gate is | dDeclaredLoop |

- **Against Test and the breakpoint.** A probe gates nothing past the item that asked. A breakpoint disposes its
  findings into folds, units or asks, while a probe hands its record back to the work. `probe.points` names
  boundaries in `review.breakpoints`' grammar.
- **The experiment shape,** dBoundRoles' `experiment` kind, after aScoutedSeam's benchmark, which no chain build
  counts on:
  - a corpus pinned to a point, with controls and decoys, and blinding at that point;
  - variants sharing one return schema, run in a bounded fan;
  - the scorer factory (dFairHearing) re-deriving every figure from committed raw outputs, paired over the cases every
    variant answered;
  - a blind judge for what no matcher can see;
  - re-runs keyed by variant and effort, and cost as a pinned reading.
- **A visual witness** is a set of deterministic DOM, console and layout assertions that the visual capture adapter
  captured at the pinned SHA and the executor can re-run. An agent's reading of a screenshot is claimed. The owner's
  own observation is an owner disposition. A visual defect worth keeping becomes a deterministic probe, seen red.
- **Roles:** the tester verifies cold, as `probe.verifier` says; the researcher designs an experiment; the executor
  runs it; a scorer or a blind judge decides it.
- **Instruction:** the probe and tester-return schemas, each verdict set closed; the policies: `probe.points`,
  `probe.raise`, `probe.observations`, `probe.experiment.authority`, `probe.verifier` and `flow.route-backs`.
- **Memory:** writes the trigger, the probe record and an experiment's shape-run rows.
- **Runtime:** the harness adapter's browser capability and the visual capture adapter, dWellOiledMachine's; act
  binding for an experiment's acts.

## [lifecycle] The owner's controls: pause, resume, withdraw, supersede""", "probe section")

# [lifecycle]
F.sub("""| `life.request` | owner | — | asks to pause, resume, withdraw or supersede the build, through the guarded command | the command's record | `life.quiesce`; resume → the build's `next` | dWellOiledMachine |""",
      """| `life.request` | owner | — | asks to pause, resume, withdraw or supersede the build, or to attend or unattend it, through the guarded command | the command's record | `life.quiesce`; resume → the build's `next`; attend or unattend → the `override` record, scoped by `attendance.scope`, then the build's `next`, announced while attended | dWellOiledMachine |""",
      "life.request")
F.sub("""- **A paused build keeps its leases.**""", """- **Attend and unattend stop at the record** (night pass, point 1). They quiesce nothing, since attendance changes no
  item (P4): the next act reads the override and announces itself, or no longer does.
- **A paused build keeps its leases.**""", "attend note")

# [test]
F.sub("""- **Roles:** tester; builders and the architect through its routes; reviewers with the gate lens at a
  breakpoint.""", """- **A fix pass keeps its check** (night pass, point 6). A fix pass's allowance excludes the red leg's own test files
  and its gate script. Changing them takes the tester's `test.attribute` judgment that the spec is wrong, which
  routes to Design as a new unit (P19).
- **Test is the landing verdict; testing elsewhere is a probe** (`[probe]`, P31).
- **Roles:** tester; builders and the architect through its routes; reviewers with the gate lens at a
  breakpoint.""", "test bullets")
F.save()
````

### `fold_np_gaps.py`

The gap register: twenty-eight rows and the re-measured tally.

````python
"""Register the night pass's twenty-eight gaps, each after its area's last row, and re-measure the register.

Usage: python -X utf8 fold_np_gaps.py   (from the worktree root); refuses unless every anchor matches exactly once.
"""
import collections
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

G = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
NP = "night pass"
UC = "`research-unattended-core.md`"
TA = "`research-testing-anywhere.md`"
CO = "`research-code-orientation.md`"
RS = "`research-relational-syntax.md`"
TF = "`research-tool-fates.md`"
NEW = [
    ("gap-flow-16", "Flow", "HIGH", "Attendance is not one rule: about 30 catalogue keys carry an owner-valued option, and "
     "nothing stops a posture from swapping an item's actor for the owner. The owner's rule (2026-10-18): attended "
     "changes only the owner's confirmations and interactions, never the flow or role use. Raised by the owner.",
     f"{NP} `[p1-unattended]`; {UC} sections 4 and 7"),
    ("gap-flow-17", "Flow", "MED", "Playbook mode has no seat in the chain: v2 runs Maintain as never a recipe-mode "
     "playbook, and nothing carries the unattended kit's recipe half (`--record-piece`, `--record-set`, "
     "`check-playbook`), which has run 0 times.", f"{UC} sections 3 and 6"),
    ("gap-flow-18", "Flow", "HIGH", "No testing outside Test: an owner's observation cannot be verified before "
     "placement, a reported bug cannot be made red before its fix, and no experiment can set a measured reference; 61 "
     "of 81 items have no role that could ask for a test. The unattended driver's pre-spec TESTING position "
     "(`tools/unattended/unattended.sh:852`) never reached the design. Raised by the owner.",
     f"{NP} `[p2-testing]`; {TA} sections 1 and 3"),
    ("gap-found-24", "Foundation", "MED", "No instruction can be scoped to a feature: the selectors are reader, role, "
     "item, step, practice and policy, so a feature's instructions are found by grep and a guess. Raised by the owner.",
     f"{RS} section 3; `layer-instruction` `[recommendations]`"),
    ("gap-found-25", "Foundation", "MED", "Two relation vocabularies and no closed edge set: the map's layer, owner, "
     "after and implements, and memory's depends-on, patches, amends, supersedes and implements, with no tests, "
     "decides or instructs edge.", f"{RS} section 3"),
    ("gap-found-26", "Foundation", "MED", "file:line citations go stale unseen: 10,655 code citations sit in memory, "
     "and of a sample of 60, 6 still point at the same line.", f"{RS} section 2"),
    ("gap-lex-09", "Lexicon", "LOW", "Overloaded terms: attended names both a session kind and a mode, playbook both "
     "the charter renderer and playbook mode, and baseline both retrofit's tolerated debt and a measured reference.",
     f"{UC} section 8; {TA} section 7"),
    ("gap-mem-28", "Memory", "HIGH", "No core code record: only the reuse scout is designed to see callers, and only "
     "with the optional codebase map installed; `symbols.json` holds public module-level names with no line ranges, "
     "and no caller index is committed. One unit's spec writer made 80 code lookups and its builder 45. Raised by "
     "the owner.", f"{CO} sections 2 and 3"),
    ("gap-mem-29", "Memory", "MED", "Enrichment keyed by file or feature rots: 25 of 31 dossiers are stale at HEAD, and "
     "60% of code files change in a week, against 3.4% of definition bodies.", f"{CO} sections 2 and 4"),
    ("gap-mem-30", "Memory", "LOW", "The level-0 map stands at 30,304 of its 32,768 B with the kits' layer links, "
     "against the project-map record's estimate of 13.2 to 13.7 KB.", f"{CO} section 3; {NP} `[instrument]`"),
    ("gap-mem-31", "Memory", "MED", "`gov:note` has no code extent: nothing says where an annotated block ends, and "
     "68% of a feature's outside spans sit in no derivable definition.", f"{RS} sections 3 and 4"),
    ("gap-mem-32", "Memory", "MED", "The decision-to-feature join runs one way: the `roles` dossier lists 11 spec ids "
     "and omits both decision-log rows that name the feature.", f"{RS} section 2"),
    ("gap-mem-33", "Memory", "LOW", "Five region parsers and no factory, one each in `check-unattended.sh`, "
     "`resolve-python.test.sh`, `render_playbook.py`, `map_lib.py` and `gen_build_index.py`.", f"{RS} section 2"),
    ("gap-orient-16", "Orient", "MED", "No announcement before an act: nothing tells an attending owner which step, "
     "item and role gov is about to take, or why. The recommendation explains only a step's exit, and `notify.owner` "
     "only transitions and parks. Raised by the owner.", f"{UC} section 5"),
    ("gap-orient-17", "Orient", "MED", "A prompt that reaches no owner session gets no intake: the intake hook writes "
     "only in the owner's session, so a request through the mailbox or a cadence is placed with no intake record.",
     f"{UC} section 6"),
    ("gap-orient-18", "Orient", "MED", "The compaction replay carries the card alone: the level-0 map returns only when "
     "a session regenerates and reads it by hand, and a compaction leaves no journal line.",
     f"{NP} `[p5-compaction]`; the project map's `[reload-summary]`"),
    ("gap-plan-08", "Plan", "LOW", "The plan record names no affected systems and no open questions, the two intent "
     "fields the AI-native SDLC playbook's intent carries beside gov's.", f"{NP} `[p6-sdlc]`"),
    ("gap-review-14", "Review", "MED", "No eval suite over instruction units: a change to the charter, a role file, a "
     "Skill or a hook pack's text is never replayed against recorded tasks.", f"{NP} `[p6-sdlc]`"),
    ("gap-review-15", "Review", "LOW", "The Loop Review names no delivery metrics: lead time, landing frequency, change "
     "failure rate, time to restore, first-pass verdict rate, route-backs per build and scope drift.",
     f"{NP} `[p6-sdlc]`"),
    ("gap-roles-21", "Roles", "HIGH", "No role may run an experiment that writes, and no tester agent exists: "
     "`.claude/agents/` holds nine role files, none of them a tester, though the design makes the tester a core "
     "role.", f"{TA} sections 2 and 7"),
    ("gap-roles-22", "Roles", "HIGH", "No work order carries code: the spec writer and the builder get no neighbourhood "
     "of the code their unit changes, the researcher and the prompt writer get no map at all, and `map.code` is "
     "declared in no chain row and no slot list. Raised by the owner.", f"{CO} section 3"),
    ("gap-rt-22", "Runtime", "HIGH", "Attended changes the driver and the binding: the design has the owner's session "
     "drive and keep its freedom from act binding and allowances, and today's attended builds lose five of the "
     "driver's checks (`tools/workflows/unattended-build.js:49-61`). Raised by the owner.",
     f"`layer-runtime` `[terms]` and `[act]`; {UC} section 4"),
    ("gap-rt-23", "Runtime", "MED", "No browser capability and no visual witness: a visual check is done by hand and "
     "recorded as prose, with no screenshot and no assertion a re-run could repeat.",
     f"{TA} sections 2 and 6; `atlas-instruments.md`"),
    ("gap-rt-24", "Runtime", "LOW", "A hook pack's refusal text is unchecked: nothing requires a refusal to name its "
     "rule and its remedy.", f"{NP} `[p6-sdlc]`"),
    ("gap-test-18", "Test", "MED", "The experiment scorer has two instances and no factory: aScoutedSeam's `bench.py` "
     "and `tools/workflows/review_replay.py`.", f"{TA} section 4"),
    ("gap-test-19", "Test", "HIGH", "A fix pass may edit the check that reds it: nothing keeps a red leg's own test "
     "files or gate script out of the fix pass's write set.", f"{NP} `[p6-sdlc]`"),
    ("gap-tool-08", "Tooling", "LOW", "The unattended kit's README and the product rule call it a four-verb driver; "
     "the code declares 30 verbs (`tools/unattended/unattended.sh:111,114`).", f"{UC} section 2"),
    ("gap-tool-09", "Tooling", "MED", "No function-level fate for today's parts: memory's tooling map is kit-level and "
     "stale in at least nine rows, and 11 of 118 functions had no fate any record decided. Raised by the owner.",
     f"{TF} sections 1 and 5; {NP} `[p8-fates]`"),
]
ROW = re.compile(r"^\| (gap-([a-z]+)-(\d\d)) \| ([^|]+) \| ([A-Z]+) \|.*$", re.M)
for key, stage, sev, gap, ev in NEW:
    for cell in (gap, ev):
        if "|" in cell:
            sys.exit(f"{key}: a cell holds a pipe")
    prefix = key.rsplit("-", 1)[0]
    rows = [m for m in ROW.finditer(G.text) if m.group(1).rsplit("-", 1)[0] == prefix]
    if not rows:
        sys.exit(f"{key}: no row of its area")
    if key in {m.group(1) for m in rows}:
        sys.exit(f"{key} exists")
    last = max(rows, key=lambda m: int(m.group(3)))
    if int(key.rsplit("-", 1)[1]) != int(last.group(3)) + 1:
        sys.exit(f"{key} does not follow {last.group(1)}")
    G.sub(last.group(0) + "\n", last.group(0) + "\n" + f"| {key} | {stage} | {sev} | {gap} | {ev} | — |\n", key)

rows = list(ROW.finditer(G.text))
stage = collections.Counter(m.group(4).strip() for m in rows)
sev = collections.Counter(m.group(5) for m in rows)
order = ["Roles", "Deploy", "Plan", "Spine", "Orient", "Test", "Runtime", "Lexicon", "Tooling", "Review", "Foundation",
         "Build", "Memory", "Flow", "Maintain", "Design"]
tally = " ".join(f"{s}={stage[s]}" for s in order) + "\n" + " ".join(f"{g}={sev[g]}" for g in ("LOW", "MED", "HIGH"))
if not G.text.endswith("```\n"):
    sys.exit("the register does not end with the last tally's fence")
G.text += f"""
Re-measured after the night pass added twenty-eight gaps, `gap-flow-16` to `gap-flow-18`, `gap-found-24` to
`gap-found-26`, `gap-lex-09`, `gap-mem-28` to `gap-mem-33`, `gap-orient-16` to `gap-orient-18`, `gap-plan-08`,
`gap-review-14`, `gap-review-15`, `gap-roles-21`, `gap-roles-22`, `gap-rt-22` to `gap-rt-24`, `gap-test-18`, `gap-test-19`,
`gap-tool-08` and `gap-tool-09` (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`), same instrument. A join of
these {len(rows)} keys against v2's chain rows finds each owned by exactly one build:

```text
{tally}
```
"""
G.done += 1
G.save()
print(tally)
````

### `fold_np_records.py`

The layer records, the project map, the systems record and the ownership amendment.

````python
"""Fold the night pass into the layer records: memory's kinds and its superseded tooling map, the library's optional
components, the project map's placement and delivery, the systems' tags and annotations, the instruction layer's kits
table and selectors, the runtime's driver and binding, and the ownership table's amendment.

Usage: python -X utf8 fold_np_records.py   (from the worktree root); refuses unless every anchor matches exactly once.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/2026-10-1"
NP = "`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`"

# layer-memory
M = Record(B + "5-build-PLAY-dClosedLoop-1-layer-memory.md")
M.sub("""Runtime registers its return, act (launch, epoch, outcome), lease,
  session binding, mailbox message and journal records.""", """Runtime registers its return, act (launch, epoch, outcome), lease,
  session binding, mailbox message and journal records. The night pass adds the `code` record, the `probe` record, and
  the playbook and playbook set kinds (points 1 to 3).""", "core kinds")
M.sub("""- **Optional components** (KN-1; Knowledge's before it): dossier, symbols and callers, with the map; the
  lexicon; the recall index.""", """- **Optional components** (KN-1; Knowledge's before it): the dossier and the map's owner views; the
  lexicon; the recall index. Code depth left this list in the night pass (point 3): the core `code` record replaces
  the optional symbols and callers, which partly reverses KN-1 for the codebase map.""", "optional kinds")
M.sub("""| symbols | dTotalRecall | the caller map |
| callers | dTotalRecall | the caller map |
""", """| code | dTotalRecall | the core code record: files, definitions with their ranges and body hashes, imports, resolved calls, tests and kit membership, derived per blob and cached by tree hash. It replaces the optional symbols and callers (night pass, point 3) |
""", "code kind")
inv = next(l for l in M.text.split("\n") if l.startswith("| inventory | dIndexedDesign |"))
M.sub(inv + "\n", inv + "\n| playbook | dIndexedDesign | a design record kind carrying dScriptedRepeat's canon, which an "
      "ordinary build authors and the `repeat` disposition follows (night pass, point 1) |\n", "playbook kind")
sr = next(l for l in M.text.split("\n") if l.startswith("| seen-red | dWitnessedBar |"))
M.sub(sr + "\n", sr + "\n| playbook set | dWitnessedBar | its writer is the set check at Test: a playbook run's pieces "
      "joined by hash, and the set's identity derived from them (night pass, point 1) |\n", "playbook set kind")
rec = next(l for l in M.text.split("\n") if l.startswith("| recommendation | dDeclaredLoop |"))
M.sub(rec + "\n", rec + "\n| probe | dDeclaredLoop | its writer is `probe.return`: one record per probe, its kind a "
      "verification, a reproduction or an experiment, an experiment's record the measured reference that later "
      "acceptance cites (night pass, point 2) |\n", "probe kind")
M.sub("""## [tools] The tooling map: keep, re-engineer, retire

From dispatch 26.""", f"""## [tools] The tooling map: keep, re-engineer, retire

Superseded 2026-10-18 by the function-level fates table (`build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md`), which
found nine of these verdicts overtaken by later rounds (night pass, point 8). The table below is kept as it was.

From dispatch 26.""", "tools superseded")
M.sub("""### [map] The map: symbols and callers, generated
""", f"""### [map] The map: symbols and callers, generated

Revised 2026-10-18, the night pass ({NP}, point 3): the symbols and callers below are one core record kind, `code`,
no longer an optional component, with each definition's range and body hash, tests and kit membership added. Each
item's work order carries its seed's neighbourhood from it in a `code` slot (P32).
""", "map note")
M.save()

# layer-library
L = Record(B + "6-build-PLAY-dClosedLoop-1-layer-library.md")
L.sub("""- Recall's is layer-memory `[reuse]`: a record finder for "why" questions.
""", """- Recall's is layer-memory `[reuse]`: a record finder for "why" questions.
- **Revised 2026-10-18, the night pass (point 3):** the map's code depth is core now, the `code` record, which partly
  reverses KN-1. The map's owner views and the dossier stay optional, and the table's map row reads for those alone.
""", "consult note")
L.save()

# project map
P = Record(B + "7-build-PLAY-dClosedLoop-1-project-map.md")
P.sub("""- **The codebase map adds code depth** where it is installed: symbols, callers and dossiers, through
  an optional slot, `map.code`. That slot renders filled, searched with nothing found, or not
  installed, with `gov tag where` named as the fallback.""", """- **Code depth is core** (revised 2026-10-18, the night pass, point 3). dTotalRecall's `code` record fills each
  item's `code` slot with its seed's neighbourhood, and level 0 holds one counted `code` line, never a line per file.
  The slot renders filled, derived with nothing related, or not extracted for a language, with `gov code where`
  named as the fallback. The map's owner views and the dossier's prose stay optional.""", "placement")
P.sub("""| an attended session | the card and the whole map when it opens, under `memory.default-load: card-and-map` (PM-7) |""",
      """| the researcher, at `plan.research` and `design.research` | the map, and the `code` slot of its question's paths (night pass, point 3) |
| the prompt writer | its actor's `map` and `code` slots, through the work order it frames (night pass, point 3) |
| the owner's session | the card and the whole map when it opens, and again at a resume and a compaction, under `memory.default-load: card-and-map` (PM-7; night pass, point 5) |""", "delivery")
P.sub("""no map. They get their slice and the `refs` rows of their write set.""",
      """no map. They get their slice and the `refs` rows of their write set, and since the night pass the builder and
the tester get their write set's `code` slot (point 3).""", "unit workers")
P.save()

# systems
Y = Record(B + "6-build-PLAY-dClosedLoop-1-systems.md")
Y.sub("""### [design-tags] Tags
""", f"""### [design-tags] Tags

Revised 2026-10-18, the night pass ({NP}, point 4): the tag system gains one closed set of typed edges, each declared
at the site that owns its fact, with every inverse derived, and `gov tag bundle`, which returns a tag's members,
regions and instructions as a manifest of ranges under `tags.bundle-rows`. `feature` becomes an instruction selector
once dTotalRecall registers it (P33).
""", "tags note")
Y.sub("""### [design-annotations] Code annotations
""", """### [design-annotations] Code annotations

Revised 2026-10-18, the night pass (point 4): a `gov:note` block's extent is its definition's extent where one
derives, and `gov:end <tag>` closes it only where none does. Its tags are `part-of` edges in the closed set (P33).
""", "annotations note")
Y.sub("""### [design-memory-structure] Memory structure
""", """### [design-memory-structure] Memory structure

Revised 2026-10-18, the night pass (point 3): code depth joins the core as the `code` record, and each item's work
order carries a `code` slot beside its memory slices (P32).
""", "memory structure note")
Y.save()

# layer-instruction
I = Record(B + "5-build-PLAY-dClosedLoop-1-layer-instruction.md")
I.sub("""| unattended | Runtime: the supervisor, `resume-tick.sh` grown, and the `next` verb (RT-3); the `/unattended` Skill is a client of `run <build>` | core |""",
      """| unattended | Runtime: dissolved by the night pass (point 1). Its supervisor seam, hooks and controls go to the runtime's own kit, and its ladder, transitions and claims to the loop kit; the `/unattended` Skill is a client of `run <build>` until dConvergedCharter retires it | core, until dissolved |""",
      "kits row")
I.sub("""  - **selectors** decide who loads a unit: `reader` (with `reader.every`, for every reader), `role`,
    `item`, `step`, `practice` and `policy`;""", """  - **selectors** decide who loads a unit: `reader` (with `reader.every`, for every reader), `role`,
    `item`, `step`, `practice` and `policy`, and, since the night pass, `feature`, armed by dTotalRecall (point 4,
    P33);""", "selectors")
I.save()

# layer-runtime
R = Record(B + "5-build-PLAY-dClosedLoop-1-layer-runtime.md")
R.sub(""" attended: the owner's session is the driver, and runs acts from next through the same harness
 calls, bound the same way""", """ attended or not: the supervisor drives, and the owner's session is its client; until dWellOiledMachine
 lands, the owner's session hosts the same driver, bound the same way (night pass, point 1)""", "diagram")
R.sub("""| attended, the owner's session; unattended, the supervisor. No model session drives unattended work. |""",
      """| the supervisor, in every mode (night pass, point 1). The owner's session is its client: it shows the announcements, takes the owner's dispositions and issues the owner's controls. Until dWellOiledMachine lands, the owner's session hosts the same driver program, bound as an act session. No model session drives. |""",
      "terms driver")
R.sub("""  - `run <build>`. Attended, it binds the owner's session as the driver. Unattended, it takes the build
    lease and registers the build with the node's supervisor;""", """  - `run <build>`, which takes the build lease and registers the build with the node's supervisor, attended
    or not, the owner's session becoming its client (night pass, point 1);""", "run verb")
R.sub("""  The `/build` and `/unattended` skills become clients of these verbs.""",
      """  The `/build` and `/unattended` skills become clients of these verbs, and `/unattended` retires with the kit at
  dConvergedCharter (night pass, point 1).""", "skills clients")
R.sub("""The act session, or attended the owner's session,
  makes exactly one call:""", """The act session, or the owner's session while it
  hosts the driver, bound the same way, makes exactly one call (night pass, point 1):""", "act call")
R.sub("""An attended owner's session keeps its freedom, and its product-code writes still pass
    the write gate.""", """The owner's session is bound the same way for every role act it hosts. Outside role
    acts it reads and orients, and its product-code writes still pass the write gate (night pass, point 1).""",
      "act freedom")
R.sub("""either the act and its epoch or
      "attended".""", """either the act and its epoch or
      "owner", the session the owner types in, attended or not (night pass, point 1).""", "binding value")
R.sub("""  - Attended, the PreToolUse entry on Workflow and Agent reserves the same way, and refuses instead of
    queueing.""", """  - In the owner's session, while it hosts the driver, the PreToolUse entry on Workflow and Agent reserves
    the same way, and refuses instead of queueing.""", "slot reservation")
if not R.text.endswith("\n"):
    sys.exit("layer-runtime does not end with a newline")
R.text += f"""
## [revised-night] Revised 2026-10-18, the night pass

The owner's point 1 ({NP} `[p1-unattended]`): unattended is the default state, and attendance changes only the
owner's interactions, never the flow or role use. Amended in place:
- `[terms]`: the supervisor is the driver in every mode, and the owner's session is its client;
- the diagram, `[decide]`'s `run <build>` and its clients: the owner's session hosts the driver only until
  dWellOiledMachine lands, bound as an act session, and `/unattended` retires with the kit;
- `[act]`: the owner's session is bound the same way for every role act it hosts, and its binding record reads
  "owner", since attendance is a mode and not a kind of session.

The night pass's other runtime additions are units in v2's dWellOiledMachine row: the attend and unattend controls,
the `step —` announcement, intake for a prompt that reaches no owner session, the browser capability and the visual
capture adapter, the default load replayed at a compaction with `next`'s line, compactions journaled, and a hook
pack's refusal text checked.
"""
R.done += 1
R.save()

# ownership
O = Record(B + "7-build-PLAY-dClosedLoop-1-ownership.md")
if not O.text.endswith("\n"):
    sys.exit("the ownership record does not end with a newline")
O.text += f"""- **The night pass, 2026-10-18** ({NP}): the new nodes and their owners, proposed for the owner's approval as PM-10's
  were (NP-23), each owner the build that implements the behaviour or registers the kind:
  - items `probe.trigger`, `probe.pin`, `probe.design`, `probe.run`, `probe.judge` and `probe.return`: dDeclaredLoop;
  - keys `attendance`, `probe.points`, `probe.raise`, `probe.observations`, `probe.experiment.authority` and
    `probe.verifier`: dDeclaredLoop; `attendance.scope`: dWellOiledMachine; `memory.code-budget` and
    `memory.code-roles`: dBoundRoles; `memory.code-languages` and `memory.code-enrich`: dTotalRecall; `tags.bundle`
    and `tags.bundle-rows`: dOrderedCharter;
  - record kinds `probe`: dDeclaredLoop; `code`: dTotalRecall, replacing `symbols` and `callers`; `playbook`:
    dIndexedDesign; `playbook set`: dWitnessedBar.
"""
O.done += 1
O.save()
````

### `reconcile_probe.py`

The order's reconciliation gate, its cites rule now reading a namespace cited through a wildcard.

````python
"""The order's reconciliation gate: what a build's row cites, what its stage's items are, where its items route,
what keys its items read, and where its expansion registers, is built by that build or one of its ancestors in
[chain]'s after relation, or carries a declared class saying why it may not be.

Usage: python reconcile_probe.py <recut-record> [plants]   (from the worktree root)

Rules, each over a population it names in its summary line:
1. cites: each backticked citation of an owned node in a [chain] row.
2. stage: each item of the plan, design, build, test and deploy steps is built by the stage's build, named by
   [chain]'s Stage column, or by an ancestor of it.
3. routes: a source that reaches the breakpoint program needs the whole program from its own build or an ancestor.
   A source is a flow item's Then cell, an expansion item's Routes cell or a [chain] row, and it reaches the
   program by naming it, in the names flow-steps [breakpoint] declares. An expansion item's Routes cell that hands
   into a stage, named by [chain]'s Stage column, also needs that stage's build.
4. reads: each backticked policy key in a flow item's cells, the Owner cell aside, is built by the item's owner or
   an ancestor of it.
5. registers: each expansion's contract names, in its "extension points used" row, the Runtime points it registers
   at; each point's owner is an ancestor of, or one of, the owners of that expansion's items. Points of another
   layer are not modelled as nodes, so the summary names each one left unread.

A dependency is classed only by a row of the re-cut's [reconciled-order] table naming its build, its node and its
owner, with a class from the closed set; a row whose class is blank or outside the set, or that no dependency needs,
is a finding. Exit 1 on any finding.
Plants, each in memory: --plant-drop <build>:<node> removes a class row; --plant-edge-drop <child>:<parent> removes
a parent edge (repeatable); --plant-class <build>:<node>=<text> sets a class cell; --plant-add <build>:<node>:<owner>
adds a class row; --plant-item <tag>:<step>:<owner>:<then> adds a flow item.
"""
import importlib.util
import re
import sys

B = "memory/builds/dClosedLoop/build/"
CLASSES = {"tolerance", "homonym", "not a use", "moved"}
spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)
A, ns = mp.derive()
owner = {}
for kind in ("item", "policy-key", "point", "record-kind", "tag-namespace"):
    for n in ns[kind]:
        own = [v for k, vs in n["rels"] if k == "owner" for v in vs]
        if own:
            owner[(kind, n["key"])] = own[0]


def plants(flag):
    return [sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == flag]


v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
rows, parents, stage_build = {}, {}, {}
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        rows[m.group(1)] = m.group(4)
        parents[m.group(1)] = [p.strip() for p in m.group(3).split(",") if p.strip() in names]
        stage_build[m.group(2).strip().lower()] = m.group(1)
for arg in plants("--plant-edge-drop"):
    child, parent = arg.split(":")
    parents[child] = [p for p in parents[child] if p != parent]


def ancestors(b, acc=None):
    acc = set() if acc is None else acc
    for p in parents[b]:
        if p not in acc:
            acc.add(p)
            ancestors(p, acc)
    return acc


def within(dep_owner, build):
    return dep_owner == build or dep_owner in ancestors(build)


def cells(ln):
    return [c.strip() for c in re.split(r"(?<!\\)\|", ln.strip().strip("|"))]


STAGES = [s for s in ("plan", "design", "build", "test", "deploy") if s in stage_build]
deps, unread = [], []   # deps: (rule, build, node, node's owner)
# 1. cites.
for b, text in rows.items():
    tokens = set(re.findall(r"`([^`\s][^`]*?)(?::[^`]*)?`", text))
    # A namespace cited through a wildcard, `<ns>.*`, cites the namespace's tag node and every policy key under it
    # (the night pass: dBoundRoles' `feature.*` read dTotalRecall's namespace, and this rule did not see it).
    wild = {t[:-2] for t in tokens if t.endswith(".*")}
    for (kind, key), own in owner.items():
        spelled = key if kind != "record-kind" else key.replace("-", " ")
        through = (kind == "tag-namespace" and key in wild) or \
            (kind == "policy-key" and any(key.startswith(w + ".") for w in wild))
        if (key in tokens or spelled in tokens or through) and not within(own, b):
            deps.append(("cites", b, key, own))
# The flow items, and the breakpoint program's declared names.
items = {}   # tag: (step, owner, cells but Item, Actor and Owner, Then cell)
fs = open(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md", encoding="utf-8").read()
for m in re.finditer(r"^## \[([a-z-]+)\][^\n]*\n(.*?)(?=^## |\Z)", fs, flags=re.M | re.S):
    for ln in m.group(2).split("\n"):
        if ln.startswith("| `"):
            c = cells(ln)
            if len(c) == 7:
                for tag in re.findall(r"`([a-z]+\.[a-z0-9-]+)`", c[0]):
                    items[tag] = (m.group(1), c[6], " ".join(c[2:6]), c[5])
for arg in plants("--plant-item"):
    tag, step, own, then = arg.split(":", 3)
    items[tag] = (step, own, then, then)
bp = fs.split("\n## [breakpoint]", 1)[1].split("\n## ", 1)[0]
names_line = next((ln for ln in bp.split("\n") if ln.startswith("- **Its names**")), "")
vocab = re.findall(r"`([a-z][a-z ]+)`", names_line)
if not vocab:
    sys.exit("flow-steps [breakpoint] declares no names line, so the routes rule would read nothing")
BREAK = re.compile("|".join(re.escape(v) for v in sorted(vocab, key=len, reverse=True)), re.I)
STAGE_WORD = re.compile(r"\b(" + "|".join(s.capitalize() for s in STAGES) + r")\b")
# 2. stage.
for tag, (step, own, _, _) in items.items():
    if step in STAGES and own and not within(own, stage_build[step]):
        deps.append(("stage", stage_build[step], tag, own))
# 3. routes: into the breakpoint program, from flow items, expansion items and rows; and into a stage, from expansion
# items.
program = {(t, o) for t, (s, o, _, _) in items.items() if s == "breakpoint" and o}
sources = {own for tag, (step, own, _, then) in items.items() if own and step != "breakpoint" and BREAK.search(then)}
sources |= {b for b, text in rows.items() if BREAK.search(text)}
le = open(B + "2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md", encoding="utf-8").read()
contracts = []   # (expansion's entry, its "extension points used" cell, the owners of its items)
for sec in re.split(r"(?m)^\| Contract field \|", le)[1:]:
    entry = sec.split("|", 1)[0].strip()
    used = next((cells(ln)[1] for ln in sec.split("\n") if ln.startswith("| extension points used |")), "")
    owners = set()
    for blk in sec.split("\n| Item | Actor |")[1:]:
        head = cells("| Item | Actor |" + blk.split("\n", 1)[0])
        oc = head.index("Owner") if "Owner" in head else None
        rc = head.index("Routes") if "Routes" in head else None
        for ln in blk.split("\n")[2:]:
            if not ln.startswith("| `"):
                break
            c = cells(ln)
            own = c[oc] if oc is not None and oc < len(c) else ""
            if not own:
                continue
            owners.add(own)
            routes = c[rc] if rc is not None and rc < len(c) else ""
            if BREAK.search(routes):
                sources.add(own)
            for stage in STAGE_WORD.findall(routes):
                sb = stage_build[stage.lower()]
                if not within(sb, own):
                    deps.append(("routes", own, stage.lower() + " step", sb))
    contracts.append((entry, used, owners))
for src in sorted(sources):
    outside = sorted({o for _, o in program if not within(o, src)})
    if outside:
        deps.append(("routes", src, "review.trigger", ",".join(outside)))
# 4. reads.
keys = {n["key"]: owner.get(("policy-key", n["key"])) for n in ns["policy-key"]}
templated = {re.sub(r"<stage>", "(" + "|".join(STAGES) + ")", re.escape(k).replace(r"\<stage\>", "<stage>")): o
             for k, o in keys.items() if "<stage>" in k}
for tag, (step, own, text, _) in items.items():
    if not own:
        continue
    for tok in set(re.findall(r"`([a-z][a-z0-9.<>-]*\.[a-z0-9<>-]+)(?::[^`]*)?`", text)):
        kown = keys.get(tok)
        if kown is None:
            kown = next((o for pat, o in templated.items() if re.fullmatch(pat, tok)), None)
        if kown and not within(kown, own):
            deps.append(("reads", own, tok, kown))
# 5. registers.
points = {n["key"]: owner.get(("point", n["key"])) for n in ns["point"]}
for entry, used, owners in contracts:
    for seg in re.split(r";\s*", used):
        layer = re.match(r"(?:and\s+)?([A-Z][a-z]+)'s\b", seg.strip())
        if layer and layer.group(1) != "Runtime":
            unread.append(f"{entry}: {seg.strip()}")
    runtime = re.search(r"Runtime's ([^;]+)", used)
    words = set(re.findall(r"[a-z]+", runtime.group(1))) if runtime else set()
    for key, pown in points.items():
        if pown and key.split("-")[0] in words:
            for o in owners:
                if not within(pown, o):
                    deps.append(("registers", o, key, pown))
# The classes: (build, node) -> (owner, class), from the re-cut's table.
recut = open(sys.argv[1], encoding="utf-8").read()
section = recut.split("### [reconciled-order]", 1)[1].split("\n## ", 1)[0] if "### [reconciled-order]" in recut else ""
classes = {}
for ln in section.split("\n"):
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    if ln.startswith("| d") and len(c) >= 5:
        classes[(c[0], c[1].strip("`"))] = (c[2], c[3])
for arg in plants("--plant-drop"):
    classes.pop(tuple(arg.split(":", 1)), None)
for arg in plants("--plant-class"):
    key, text = arg.split("=", 1)
    b, node = key.split(":", 1)
    classes[(b, node)] = (classes.get((b, node), ("", ""))[0], text)
for arg in plants("--plant-add"):
    b, node, own = arg.split(":", 2)
    classes[(b, node)] = (own, "tolerance")
deps = sorted(set(deps))
count = {k: sum(d[0] == k for d in deps) for k in ("cites", "stage", "routes", "reads", "registers")}
print(f"chain rows {len(rows)} · owned nodes read {len(owner)} · flow items read {len(items)} · stages {len(STAGES)} · "
      f"breakpoint items {len(program)}, names {len(vocab)} · contracts read {len(contracts)} · on a non-ancestor's node "
      f"{len(deps)} ({', '.join(f'{k} {v}' for k, v in count.items())})")
print(f"left out: systems, cited in prose; points of another layer, not modelled as nodes ({len(unread)}): "
      + "; ".join(unread))
findings = 0
for rule, b, key, own in deps:
    row = classes.get((b, key))
    ok = row is not None and row[1] in CLASSES and row[0] == own
    label = row[1] if ok else ("UNCLASSED" if row is None else f"BAD CLASS ROW (owner {row[0] or '-'}, class {row[1] or '-'})")
    print(f"  {b} {rule} `{key}` ({own}'s, not an ancestor): {label}")
    findings += not ok
needed = {(b, key) for _, b, key, _ in deps}
for (b, key), (own, cls) in sorted(classes.items()):
    if (b, key) not in needed:
        print(f"  class row with no dependency: {b} `{key}` ({own}, {cls or '-'})")
        findings += 1
    elif cls not in CLASSES:
        print(f"  class row outside the closed set: {b} `{key}` ({cls or 'blank'})")
print(f"findings {findings}")
sys.exit(1 if findings else 0)
````

### `make_fates.py`

Point 8: dispatch 104's rows, its citations resolved to section tags at `beda01950`, the night's updates and proposals.

````python
"""Derive the fates table from dispatch 104's disposition, with the night pass's updates, and print what it would write.

Each line-number citation (`v2:1186`, `lr:595`) is resolved, against the records as committed before the night pass's
fold (`git show <base>:<path>`), to the section tag that holds the line, or for a [chain] row to its build. The rows
the night pass decides or proposes are replaced or added by key. Rows that still name no chain build where their fate
needs one are listed, and the script exits 1.

Usage: python -X utf8 make_fates.py <base-sha> --print     list the derived rows and any row still unbuilt
       python -X utf8 make_fates.py <base-sha> --rows <out.tsv>   write the rows, tab-separated
"""
import re
import subprocess
import sys

BASE = sys.argv[1]
B = "memory/builds/dClosedLoop/build/"
SRC = {"v2": "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
       "li": "2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md",
       "lm": "2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
       "lr": "2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
       "lx": "2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md",
       "rf": "2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md",
       "roles": "2026-10-14-build-PLAY-dClosedLoop-1-roles.md",
       "ownership": "2026-10-17-build-PLAY-dClosedLoop-1-ownership.md",
       "gap-register": "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md"}
NAME = {"v2": "v2", "li": "layer-instruction", "lm": "layer-memory", "lr": "layer-runtime", "lx": "layer-expansions",
        "rf": "retrofit", "roles": "roles", "ownership": "ownership", "gap-register": "the gap register"}
text = {k: subprocess.run(["git", "show", f"{BASE}:{B}{f}"], capture_output=True, text=True, encoding="utf-8",
                          check=True).stdout.split("\n") for k, f in SRC.items()}


def tag_at(src, n):
    lines = text[src]
    ln = lines[n - 1] if 0 < n <= len(lines) else ""
    m = re.match(r"^\| (d[A-Z]\w+) \|", ln)
    if src == "v2" and m:
        return f"v2 `[chain]` {m.group(1)}"
    g = re.match(r"^\| (gap-[a-z]+-\d\d) \|", ln)
    if src == "gap-register" and g:
        return g.group(1)
    for i in range(min(n, len(lines)) - 1, -1, -1):
        h = re.match(r"^#{2,3} \[([a-z0-9-]+)\]", lines[i])
        if h:
            return f"{NAME[src]} `[{h.group(1)}]`"
    return f"{NAME[src]}"


def convert(cite):
    out = []
    for src, nums in re.findall(r"\b(v2|li|lm|lr|lx|rf|roles|ownership|gap-register):(\d[\d,-]*)", cite):
        for part in nums.split(","):
            if part:
                t = tag_at(src, int(part.split("-")[0]))
                if t not in out:
                    out.append(t)
    rest = re.sub(r"\b(v2|li|lm|lr|lx|rf|roles|ownership|gap-register):\d[\d,-]*", "", cite).strip(" ;,")
    if rest and rest != "—":
        out.append(rest)
    return "; ".join(out) if out else "—"


rec = open(B + "2026-10-18-build-PLAY-dClosedLoop-1-research-tool-fates.md", encoding="utf-8").read()
table = rec.split("## 3. The disposition", 1)[1].split("\n## 4.", 1)[0]
rows = []
for ln in table.split("\n"):
    if ln.startswith("| ") and not ln.startswith("| Kit") and not ln.startswith("|---"):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        kit, fn, job, fate, where, cite = c
        fate = fate.replace(" (kit)", "")
        rows.append([kit, fn, job, fate, where, convert(cite)])

NP = "the owner's point {} (night pass)"
PROP = "proposed by the night pass (NP-22)"
# The night pass's updates, keyed by (kit, function).
REPLACE = {
    ("unattended", "`--authorization`, `--attest`"): [
        ["unattended", "`--authorization`", "the build folder or prompt record as the mandate", "RESHAPED",
         "the request is the mandate under `plan.ratification: request` (dRankedPlan), its intake written by the hook "
         "(dWellOiledMachine); ANCHOR_SCOPE and AUTH_PARAM retired", NP.format(1) + "; v2 `[chain]` dRankedPlan"],
        ["unattended", "`--attest`", "a typed attestation of a directive", "RETIRED",
         "none: an agent-typed witness, which P2 forbids; witnesses are computed", NP.format(1)]],
    ("unattended", "`run-lease.js`"): [
        ["unattended", "`run-lease.js`", "binds a session to its run for the three hooks", "RESHAPED",
         "the session binding record (dWellOiledMachine)", PROP + "; layer-runtime `[act]`"]],
    ("unattended", "playbook mode (record-piece, record-set, `check-playbook`)"): [
        ["unattended", "playbook mode (`--record-piece`, `--record-set`, `check-playbook`)",
         "repeatable content as pieces and sets", "RESHAPED",
         "the playbook record kind and `check-playbook` as Design's pack (dIndexedDesign), pieces built as units "
         "(dScopedBuild), the set check (dWitnessedBar), a cyclic playbook's filer (dTendedCadence), reached by the "
         "`repeat` disposition (dDeclaredLoop)", NP.format(1)]],
    ("unattended", "check-unattended, pass-order, brief-recorded, arms-groups"): [
        ["unattended", "`check-unattended`", "the kit's own gate", "RESHAPED",
         "the stage coverage gates and the loop kit's conformance gates (dDeclaredLoop)", PROP],
        ["unattended", "`check-pass-order`, `check-brief-recorded`", "pass order and brief records", "RESHAPED",
         "the work order's hash and the shape-run rows (dBoundRoles)", PROP + "; `research-unattended-core.md`"],
        ["unattended", "`check-arms-groups`", "lints the batched self-test's groups", "RETIRED",
         "none: it lints the kit's own self-test file, which dissolves with the kit (dConvergedCharter)", PROP]],
    ("unattended", "guide templates, Skill"): [
        ["unattended", "guide templates (PROTOCOL, VERBS, STOPS, ASKS)", "the protocol text", "RESHAPED",
         "rendered views of the loop's checklists (dConvergedCharter)", "v2 `[chain]` dConvergedCharter"],
        ["unattended", "the `/unattended` Skill", "starts, resumes or closes a run", "RETIRED",
         "a client of `run` until dConvergedCharter retires it, unattended being the default state (NP-4)",
         NP.format(1)]],
    ("workflows", "`drift-audit-*.js`"): [
        ["workflows", "`drift-audit-*.js`", "drift audit harnesses", "RESHAPED",
         "observability's detectors, read as Maintain's cadence readings (dTendedCadence)", PROP]],
    ("workflows", "`orient-counterfactual.js`"): [
        ["workflows", "`orient-counterfactual.js`", "a one-off kickoff experiment", "RETIRED",
         "the `experiment` shape kind (dBoundRoles), of which it is an early instance", PROP]],
    ("memory-tree", "`routed_commits`, `check-arms`, `row_grammar`, `migrate_backlog`"): [
        ["memory-tree", "`routed_commits`", "every commit on a product path names a unit specced before it", "MERGED",
         "`build.scope`'s commit check and the touch join (dScopedBuild)", PROP],
        ["memory-tree", "`check-arms`", "a check's armed-population rows", "RESHAPED",
         "the ledger's armed populations (dWitnessedBar)", PROP],
        ["memory-tree", "`row_grammar`", "check 20, row grammar and id collisions in one file", "RESHAPED",
         "the record-kind registry's generated schema checks (dTotalRecall)", PROP],
        ["memory-tree", "`migrate_backlog`", "plans and relocates the backlog from shards to builds", "RETIRED",
         "the ask register, once the migration has run (dTotalRecall)", PROP]],
    ("codebase-map", "`gen_map.py`, dossiers"): [
        ["codebase-map", "`gen_map.py`, its symbols", "the inventory map and its public-name index", "RESHAPED",
         "the core `code` record and `gov map code` (dTotalRecall)", NP.format(3) + "; v2 `[chain]` dTotalRecall"],
        ["codebase-map", "dossiers, `MAP.md`, `CARDS.md`", "feature prose and the owner's views", "STAYS",
         "optional: dossiers anchored to symbol keys, their header the feature node as NP-16 settles (dTotalRecall)",
         NP.format(3) + "; layer-memory `[map]`"]],
    ("codebase-map", "`map_diff`, `check_gate_coverage`"): [
        ["codebase-map", "`map_diff`", "a range's feature digest, and stale dossiers", "RESHAPED",
         "a range read over the `code` record, and enrichment staleness by body hash (dTotalRecall)", PROP],
        ["codebase-map", "`check_gate_coverage`", "the adopter's gate compares every artifact the engine writes",
         "STAYS", "a distribution check for the optional map's install (dShippedRelease)", PROP]],
    ("memory-recall", "`bench`, `check-recall`, `union`"): [
        ["memory-recall", "`bench`, `union`", "the retrieval bench and its union of runs", "RESHAPED",
         "an `experiment` shape instance over recall's corpus (dBoundRoles)", PROP],
        ["memory-recall", "`check-recall`", "recall's floor check", "RESHAPED", "the record finder's leg (dTotalRecall)",
         PROP]],
    ("pytest-parallel-guardrails", "xdist guard"): [
        ["pytest-parallel-guardrails", "xdist guard", "bounded parallel tests", "STAYS",
         "an adopter-only Flow leg pack, declared so in gov, which runs no xdist suite (dWitnessedBar)", PROP]],
    ("top-level", "`check-agent-cap-restatement.sh`"): [
        ["top-level", "`check-agent-cap-restatement.sh`", "the fan-out bound restated", "RESHAPED",
         "generalised to a policy value restated outside the catalogue (dOrderedCharter)", PROP + "; layer-memory `[tools]`"]],
    ("skills", "manifest ratchet"): [
        ["skills", "manifest ratchet", "the kickoff manifest audit", "RESHAPED",
         "the guarded instruction manifest (dOrderedCharter)", PROP]],
}
ADD = [
    ["unattended", "the kit as a kit", "the unattended-run kit", "RETIRED",
     "dissolved: its ladder, transitions and claims into the loop kit (dDeclaredLoop), its supervisor seam, hooks and "
     "controls into the runtime's own kit (dWellOiledMachine)", NP.format(1)],
    ["unattended", "slug mode", "a run started on a named build", "RETIRED",
     "none: every run is a placed request, continue among `entry.place`'s dispositions (dDeclaredLoop)", NP.format(1)],
    ["unattended", "ask mode", "a run started on ask ids", "RETIRED",
     "none: asks enter through Plan's triage (dRankedPlan)", NP.format(1)],
]
# The build that keeps or receives a part whose row names none, from the design's own placement of it.
BUILD_FOR = {
    ("roles", "gov-session"): "dBoundRoles",
    ("workflows", "four harness checks"): "dBoundRoles, whose role harnesses they check",
    ("unattended", "`stall-recorder.js`"): "dWellOiledMachine",
    ("hooks", "`agent-cap.js`"): "dWellOiledMachine",
    ("hooks", "`scratch-guard.js`"): "dBoundRoles, packed by dWellOiledMachine",
    ("process-monitor", "reap, scope, classify"): "dWellOiledMachine",
    ("process-monitor", "census, procmon-hook"): "dTendedCadence",
    ("branch-reconcile", "report, cleanup Skill"): "dTendedCadence, observability's prune fix",
    ("gate-lint", "scans"): "dWitnessedBar, at Test's leg-pack point",
    ("run-gates", "turnstile"): "dWitnessedBar",
    ("run-gates", "`read_held_reds`"): "dWitnessedBar, which owns gap-test-13",
    ("govkit", "epoch, selfcheck 5c"): "dShippedRelease, which owns gap-tool-02",
    ("govkit", "`govkit check`"): "dShippedRelease",
    ("top-level", "`check-wiring.sh` install arms"): "dShippedRelease",
    ("top-level", "`check-placeholders.sh`"): "dShippedRelease",
    ("top-level", "`check-kit-versions.sh`"): "dShippedRelease, which owns gap-tool-02",
    ("top-level", "`check-line-length.sh`"): "dOrderedCharter, whose statement grammar extends it",
    ("top-level", "`check-spec-tokens.py`"): "dIndexedDesign",
    ("top-level", "`check-dead-paths.sh`"): "dTendedCadence, whose dead-pointer detector shares its function",
    ("top-level", "`settings-merge.py`"): "dWellOiledMachine",
    ("skills", "rendered Skills (7)"): "dConvergedCharter, with dWellOiledMachine for the clients",
}
for r in rows:
    b = BUILD_FOR.get((r[0], r[1]))
    if b:
        r[4] = (r[4] if r[4] != "—" else "kept") + f" ({b})"
out, seen = [], set()
for r in rows:
    key = (r[0], r[1])
    if key in REPLACE:
        out.extend(REPLACE[key])
        seen.add(key)
    else:
        out.append(r)
missing = sorted(set(REPLACE) - seen)
if missing:
    sys.exit(f"replacements with no row: {missing}")
out.extend(ADD)
# A row whose fate names a destination must name a chain build; take it from its [chain] citation where it lacks one.
unbuilt = []
for r in out:
    if r[3] in ("STAYS", "RESHAPED", "MERGED") and not re.search(r"\bd[A-Z]\w+", r[4]):
        builds = re.findall(r"v2 `\[chain\]` (d[A-Z]\w+)", r[5])
        if builds:
            r[4] += " (" + ", ".join(dict.fromkeys(builds)) + ")"
        else:
            unbuilt.append(r)
if "--print" in sys.argv:
    for r in out:
        print(" | ".join(r))
for r in unbuilt:
    print("UNBUILT:", " | ".join(r), file=sys.stderr)
if "--rows" in sys.argv:
    with open(sys.argv[sys.argv.index("--rows") + 1], "w", encoding="utf-8", newline="\n") as fh:
        for r in out:
            fh.write("\t".join(r) + "\n")
print(f"rows {len(out)} · unbuilt {len(unbuilt)}", file=sys.stderr)
sys.exit(1 if unbuilt else 0)
````

### `record_fates.py`

Writes the fates record from those rows.

````python
"""Write the fates record from make_fates.py's rows: each kit's fate, every function's fate, the stale verdicts it
supersedes, and the check that holds it.

Usage: python -X utf8 record_fates.py <fates.tsv>   (from the worktree root); refuses to overwrite
"""
import collections
import pathlib
import sys

OUT = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md")
if OUT.exists():
    sys.exit(f"{OUT} exists")
rows = [l.rstrip("\n").split("\t") for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
for r in rows:
    if len(r) != 6 or any("|" in c for c in r):
        sys.exit(f"a row is malformed: {r[:2]}")
count = collections.Counter(r[3] for r in rows)
by = collections.defaultdict(collections.Counter)
for r in rows:
    by[r[0]][r[3]] += 1
KITS = [
    ("agent-instructions", "absorbed", "the one renderer takes its wiring (dOrderedCharter), and each harness's files come "
     "from the harness adapters (dWellOiledMachine)"),
    ("branch-reconcile", "optional", "observability's prune fix (dTendedCadence)"),
    ("codebase-map", "optional", "its symbols become the core `code` record (dTotalRecall); its dossiers and owner views "
     "stay optional, and `reuse_lookup.py` retires"),
    ("drift-audit", "optional", "its gateable signals become core legs, and its report half is observability's "
     "(dTendedCadence)"),
    ("gate-lint", "optional", "a Flow leg pack (dWitnessedBar)"),
    ("govkit", "optional", "distribution's engine: release tags, the receipt, the one version check (dShippedRelease)"),
    ("hooks", "kept", "its guards become packs on the one enforcement surface (dWellOiledMachine)"),
    ("lexicon", "optional", "rebuilt by dMindYourWords"),
    ("lib", "kept", "the shared primitives, and the join, ledger, extraction, region-parser and scorer factories"),
    ("memory-recall", "optional", "narrowed to a record finder (dTotalRecall)"),
    ("memory-tree", "kept", "the memory contract's engine: the kind registry, `record` and the `code` record "
     "(dTotalRecall)"),
    ("playbook", "kept", "the instruction engine, the one renderer (dOrderedCharter)"),
    ("process-monitor", "kept", "Runtime's reaping (dWellOiledMachine); its census an observability reading"),
    ("pytest-parallel-guardrails", "optional", "an adopter-only Flow leg pack, as proposed (NP-22)"),
    ("roles", "kept", "the roles kit: the core roles, work orders and shapes (dBoundRoles)"),
    ("run-gates", "kept", "Test's verdict runner (dWitnessedBar)"),
    ("runlog", "optional", "observability's reader; its line grammar becomes the core journal (dWellOiledMachine)"),
    ("unattended", "absorbed", "dissolved: the loop kit takes its ladder, transitions and claims (dDeclaredLoop), and "
     "the runtime's own kit its supervisor seam, hooks and controls (dWellOiledMachine); `/unattended` retires at "
     "dConvergedCharter"),
    ("workflows", "kept", "the role harnesses (dBoundRoles, dWellOiledMachine) and the Tier-2 review (dFairHearing)"),
]
known = {k for k, _, _ in KITS}
PSEUDO = {"top-level", "skills", ".githooks", "guides"}
stray = {r[0] for r in rows} - known - PSEUDO
if stray:
    sys.exit(f"rows name kits the kits table lacks: {sorted(stray)}")
kit_rows = "\n".join(f"| {k} | {f} | {w} |" for k, f, w in KITS)
table = "\n".join("| " + " | ".join(r) + " |" for r in rows)
body = f"""# Today's parts and their fates

**Serves:** research PLAY-dClosedLoop-1

The owner's point 8 asked what becomes of each of gov's tools under the new architecture. This record answers it, part
by part: every shipped kit, each function in it, and its fate. Dispatch 104 derived the first table
(`build/2026-10-18-build-PLAY-dClosedLoop-1-research-tool-fates.md`). The night pass updated it with the night's
decisions and proposed a fate for every part no record decided
(`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[p8-fates]`).

## [words] The owner's question, 2026-10-18

> 8. The inventory and mapping of the current Gov tools and their functionality - has it been done at any stage, is it helpful? We need a clear understanding of how the current kit is getting rebuilt under the new architecture - what functions stay and different shape, which functions go, what tools will stay, what tools with disappear?

## [inventories] What existed, and why it did not answer

- **Several inventories existed, none at function level with a fate.**
  - Dispatch 26's census (`research-memory-tooling.md`) counted every kit's tools, runs, legs and asks.
  - Memory's tooling map (`layer-memory` `[tools]`) turned it into 25 kit-level verdicts on 2026-10-15.
  - The gap register's implicit loop pictures the stages, not the tools.
  - The runtime layer's hook-owner table is the only part-level inventory with a fate, and covers hooks alone.
  - The codebase map's dossiers, `tools/gate-legs.json` and the kits' descriptors list parts with no fate.
  - The design map's kit, feature, hook and leg nodes are derived live, but carry no fate.
- **The kit-level map went stale.** The expansions, retrofit, systems and audit rounds overtook at least nine of its
  25 verdicts, and it still states them (`[stale]`). It is marked superseded.
- **It helped as a count, not as an answer.** The owner's question is about functions, so the table below is.

## [kits] Each kit's fate

A kit's fate is one of four:
- **kept:** it stays a kit, its functions kept or reshaped in place;
- **optional:** it stays as an optional component or an expansion's kit, which the core never needs (P28);
- **absorbed:** its directory goes, and its functions move into other kits;
- **retired:** it goes with no successor.

| Kit | Fate | What becomes of it |
|---|---|---|
{kit_rows}

- **Two kits are new:** the loop kit (dDeclaredLoop) and the runtime's own kit (dWellOiledMachine), whose name the
  lexicon gives it (gap-lex-09).
- **Two kits disappear:** agent-instructions and unattended, both absorbed. No kit is retired outright.
- **Beside the kits:** the top-level checks fold into packs or into govkit's one version check, `skills/`
  loses `deploy-governance` and reshapes the kickoff into the entry step and the orientation scout, the git hooks
  stay with their bar and trap changes, and the hand-written guides retire into rendered views.

## [table] Every part, function by function

The fate is one of STAYS, RESHAPED, MERGED and RETIRED. "Where it goes" names the chain build that keeps or receives
it. "Decided by" names the record that decides it, a line-number citation of dispatch 104's resolved to its section
tag, or "proposed by the night pass (NP-22)" for a part no record decided. Counts: {count['STAYS']} stay,
{count['RESHAPED']} reshaped, {count['MERGED']} merged and {count['RETIRED']} retired, over {len(rows)} rows.

| Kit | Function | Today's job | Fate | Where it goes | Decided by |
|---|---|---|---|---|---|
{table}

## [stale] Where the records disagreed, and what stands

Dispatch 104 found thirteen places where a later round overtook an earlier verdict, or records disagree. What stands:
1. **`DECISIONS.md`:** `[tools]` retires it, but `layer-memory` `[decisions]` keeps its path with a holds-now view, and
   v2's dTotalRecall row builds that view. The later design stands.
2. **check-wiring:** only its install arms fold into govkit (`layer-expansions` `[design-distribution]`). Its session
   arm stays, with a fail-closed class arm under Runtime (`layer-runtime` `[enforce]`).
3. **workflows:** reshaped by dFairHearing, dBoundRoles and dWellOiledMachine, not kept as is.
4. **push-main, session-kickoff, process-monitor and settings-merge:** reshaped, not kept as is. The census of
   process-monitor moves to observability.
5. **drift-audit:** its seven gateable signals leave it for core and lexicon legs, and its hand-typed lists retire.
6. **The lexicon's pin:** held as a keyed ledger population, not a shrink-only count (v2's dMindYourWords row).
7. **The leg manifest:** proposed as one manifest whose rows the leg factory generates from the packs' declarations
   (dWitnessedBar, NP-22), which keeps `tools/gate-legs.json` the single read source the charter names.
8. **lib:** the class widened to 261 markers over 17 primitives, and lib became the home of the join, ledger and
   extraction factories, with a descriptor that marks it not installable (v2's dShippedRelease row).
9. **branch-reconcile's layer:** observability's prune fix stands (`layer-expansions` `[design-observability]`).
10. **process-monitor's layer:** reaping is Runtime's, and its census observability's. Both stand.
11. **The tooling order:** the instruction layer first (RC-4), not "Flow first".
12. **The design map's kit lines** carried no layer: the map compared prose cells with tags. Fixed in the night pass,
    with an arm seen red (`night-pass` `[instrument]`).
13. **The gap register's owner column** reads "—" throughout. Owners come from v2's `[chain]`, by design.

## [check] How the table stays true

The design map reads this record, as it reads the ownership table:
- each kit line renders its fate from `[kits]` as `fate=`;
- every kit node has a `[kits]` row and at least one `[table]` row;
- every `[table]` row's kit is a kit node, or one of `top-level`, `skills`, `.githooks` and `guides`;
- every fate is in its closed set, for kits and for rows alike;
- every STAYS, RESHAPED or MERGED row names a chain build in "Where it goes";
- every RETIRED row names its replacement, or says "none" and why.

Each arm is seen red on a planted case (`night-pass` `[instrument]`). What the check does not do: it does not prove
that a row's fate is right, only that every part has one, in the closed set, landing in a build that exists. Whether
each lands is dConvergedCharter's exit check (v2's `[chain]`).
"""
OUT.write_text(body, encoding="utf-8", newline="\n")
print(f"wrote {OUT}: {len(rows)} rows · {dict(count)}")
````

### `fix_map_fates.py`

The design map reads the fates record: `fate=` on each kit line, and six arms.

````python
"""Have the design map read the fates record (night pass, point 8): each kit line renders its declared fate, and six
arms hold the table to the tree and the chain, each with a plant.

Usage: python -X utf8 fix_map_fates.py   (from the worktree root)
"""
import pathlib
import sys

P = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py")
t = P.read_text(encoding="utf-8")


def sub(old, new, label):
    global t
    if t.count(old) != 1:
        sys.exit(f"{label}: the anchor matches {t.count(old)} times")
    t = t.replace(old, new, 1)


sub('''NO_LAYER = set()
''', '''NO_LAYER = set()
# The fates record (night pass, point 8): each kit's declared fate, and every part's row, read for the fates arms.
FATES = HERE / "2026-10-18-build-PLAY-dClosedLoop-1-fates.md"
FATE_KITS, FATE_ROWS = {}, []
FATE_KIT_SET = {"kept", "optional", "absorbed", "retired"}
FATE_ROW_SET = {"STAYS", "RESHAPED", "MERGED", "RETIRED"}
FATE_PSEUDO = {"top-level", "skills", ".githooks", "guides"}
''', "globals")

sub('''        kits.append(node(k, purpose, src="derived", rels=[("layer", [l for l in kit_layer.get(k, []) if l in layer_tags])]))
    ns["kit"] = kits
''', '''        kits.append(node(k, purpose, src="derived", rels=[("layer", [l for l in kit_layer.get(k, []) if l in layer_tags])]))
    if FATES.exists():
        body = FATES.read_text(encoding="utf-8")
        for tag, width, sink in (("kits", 3, "kits"), ("table", 6, "rows")):
            _, block = section(body, tag)
            for ln in block.split("\\n"):
                c = atlas.cells(ln) if ln.startswith("| ") else []
                if len(c) == width and c[0] != "Kit" and not set(c[0]) <= set("-"):
                    if sink == "kits":
                        FATE_KITS[c[0]] = c[1]
                    else:
                        FATE_ROWS.append(c)
        for n in kits:
            if n["key"] in FATE_KITS:
                n["rels"].append(("fate", [FATE_KITS[n["key"]]]))
    ns["kit"] = kits
''', "derive")

sub('''    # Layer: every kit line joins a layer''', '''    # Fates: every kit has a declared fate and rows, every row a known kit, a fate in its set and a destination.
    if FATE_KITS or FATE_ROWS:
        rows_, kits_ = [list(r) for r in FATE_ROWS], dict(FATE_KITS)
        if plant == "fates-drop":
            rows_ = [r for r in rows_ if r[0] != rows_[0][0]]
        elif plant == "fates-ghost":
            rows_.append(["ghostkit", "a part", "a job", "STAYS", "kept (dGroundRules)", "a plant"])
        elif plant == "fates-bad":
            rows_[0][3] = "MAYBE"
        elif plant == "fates-unbuilt":
            i = next(i for i, r in enumerate(rows_) if r[3] == "RESHAPED")
            rows_[i][4] = "somewhere"
        elif plant == "fates-empty":
            i = next(i for i, r in enumerate(rows_) if r[3] == "RETIRED")
            rows_[i][4] = ""
        elif plant == "fates-kit":
            kits_[next(iter(kits_))] = "maybe"
        kitkeys, chainkeys = {n["key"] for n in ns["kit"]}, {n["key"] for n in ns["chain"]}
        for k in sorted(kitkeys):
            if k not in kits_:
                findings.append(f"fates: kit.{k} has no [kits] row")
            if not any(r[0] == k for r in rows_):
                findings.append(f"fates: kit.{k} has no [table] row")
        for k, f in kits_.items():
            if f not in FATE_KIT_SET:
                findings.append(f"fates: kit.{k}'s fate {f} is outside the set")
            if k not in kitkeys:
                findings.append(f"fates: [kits] names {k}, which is no kit node")
        for r in rows_:
            if r[0] not in kitkeys and r[0] not in FATE_PSEUDO:
                findings.append(f"fates: a row names {r[0]}, which is no kit")
            if r[3] not in FATE_ROW_SET:
                findings.append(f"fates: {r[0]} · {r[1]} has the fate {r[3]}, outside the set")
            elif r[3] != "RETIRED" and not set(re.findall(r"\\bd[A-Z]\\w+", r[4])) & chainkeys:
                findings.append(f"fates: {r[0]} · {r[1]} names no chain build where it goes")
            elif r[3] == "RETIRED" and not r[4].strip():
                findings.append(f"fates: {r[0]} · {r[1]} retires with no replacement named")
    # Layer: every kit line joins a layer''', "arms")

sub('''      cases: drop-line, bad-count, ghost-rel, no-layer, census,''',
    '''      cases: drop-line, bad-count, ghost-rel, no-layer, fates-drop, fates-ghost, fates-bad, fates-unbuilt,
      fates-empty, fates-kit, census,''', "usage")
P.write_text(t, encoding="utf-8", newline="\n")
print("map.py: the fates arms")
````

### `merge_np.py`

Orders the night-pass record's sections point by point.

````python
"""Merge the drafted sections into the night-pass record, ordered point by point.

Usage: python -X utf8 merge_np.py <sections-a.md> <sections-b.md>   (from the worktree root)
"""
import pathlib
import re
import sys

P = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md")
ORDER = ["words", "research", "p1-unattended", "p2-testing", "p3-code", "p4-relations", "p5-compaction", "p6-sdlc",
         "p7-atlas", "p8-fates", "chain-impact", "forks", "instrument"]


def split(text):
    parts = re.split(r"(?m)^(?=## \[)", text)
    head, secs = parts[0], {}
    for s in parts[1:]:
        tag = re.match(r"## \[([a-z0-9-]+)\]", s).group(1)
        if tag in secs:
            sys.exit(f"[{tag}] twice")
        secs[tag] = s.rstrip("\n") + "\n"
    return head, secs


head, secs = split(P.read_text(encoding="utf-8"))
for f in sys.argv[1:3]:
    _, more = split("\n" + pathlib.Path(f).read_text(encoding="utf-8"))
    for tag, s in more.items():
        if tag in secs:
            sys.exit(f"[{tag}] is already in the record")
        secs[tag] = s
if sorted(secs) != sorted(ORDER):
    sys.exit(f"sections {sorted(secs)} are not the order's {sorted(ORDER)}")
P.write_text(head.rstrip("\n") + "\n\n" + "\n".join(secs[t] for t in ORDER), encoding="utf-8", newline="\n")
print(f"{P.name}: {len(ORDER)} sections, {P.stat().st_size} bytes")
````

### `record_instruments.py`

This record's own writer.

````python
"""Write the night pass's instruments record: every script it ran or wrote, the researchers' probes, the red runs as
captured, and the final runs of every check, re-run here.

Usage: python -X utf8 record_instruments.py   (from the worktree root); overwrites the record it owns
"""
import pathlib
import subprocess
import sys

S = pathlib.Path(__file__).resolve().parent.parent
B = "memory/builds/dClosedLoop/build/"
OUT = pathlib.Path(B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md")
FENCE = "`" * 4   # built, so this script's own source holds no fence it would refuse


def read(p):
    t = pathlib.Path(p).read_bytes().decode("utf-8").replace("\r\n", "\n").strip("\n")
    if FENCE in t:
        sys.exit(f"{p} holds a four-backtick fence")
    return t


def run(*args):
    r = subprocess.run([sys.executable, "-X", "utf8", *args], capture_output=True)
    out = (r.stdout + r.stderr).decode("utf-8").replace("\r\n", "\n").strip("\n")
    return out, r.returncode


def block(lang, body):
    return f"{FENCE}{lang}\n{body}\n{FENCE}\n"


MINE = [
    ("night/save_return.py", "Saves an agent's final return verbatim from its transcript, so no return passes through "
     "a retyping."),
    ("night/fold_state.py", "Point 7: each progress row's fold state as the atlas derives it, red on a row read unfolded "
     "despite a fold section."),
    ("night/fix_map_layer.py", "The design map's kit-to-layer join and its arm, applied with `--arm-only` first to see "
     "the arm red."),
    ("walk/paren_semis.py", "The clause scan, extended to double quotes."),
    ("night/fold_np_v2.py", "v2: the revision note, the principles, the keys and their preset rows, the chain's clauses "
     "and gaps, and the owed checks."),
    ("night/fold_np_v2b.py", "v2, second fold: the `feature` selector moved to dTotalRecall, and dBoundRoles' slots "
     "waiting on it."),
    ("night/fold_np_flow.py", "flow-steps: `repeat`, the entry-time probe, `[rules]`, the attendance gates, `[probe]`, "
     "attend and unattend, and the fix pass."),
    ("night/fold_np_gaps.py", "The gap register: twenty-eight rows and the re-measured tally."),
    ("night/fold_np_records.py", "The layer records, the project map, the systems record and the ownership amendment."),
    ("audit/reconcile_probe.py", "The order's reconciliation gate, its cites rule now reading a namespace cited through "
     "a wildcard."),
    ("night/make_fates.py", "Point 8: dispatch 104's rows, its citations resolved to section tags at `beda01950`, the "
     "night's updates and proposals."),
    ("night/record_fates.py", "Writes the fates record from those rows."),
    ("night/fix_map_fates.py", "The design map reads the fates record: `fate=` on each kit line, and six arms."),
    ("night/merge_np.py", "Orders the night-pass record's sections point by point."),
    ("night/record_instruments.py", "This record's own writer."),
]
PROBES = [("p4rel/" + n, "dispatch 103") for n in ("census.py", "sec.py", "fl_drift.py", "dossier.py", "regions.py",
                                                    "spans.py", "spandecay.py")] + \
         [(n, "dispatch 102") for n in ("codemap.py", "nbhd2.py", "probe_unit.py", "lookups.py")]

parts = ["""# Instruments: the night pass

**Serves:** research PLAY-dClosedLoop-1

The scripts the night pass ran or wrote, the researchers' probes, the red runs as they were captured, and the final
run of every check, re-run when this record was written. The record they serve is
`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`. Scripts live in the session's scratchpad, and are kept here
whole.

## [scripts] The night pass's own scripts
"""]
for rel, why in MINE:
    parts.append(f"### `{pathlib.Path(rel).name}`\n\n{why}\n\n" + block("python", read(S / rel)))
parts.append("""## [inline] The inline edits, as run

""" + block("text", read(S / "night/inline_edits.txt")))
parts.append("""## [red] The red runs, as captured

Each check was seen red before its fix, as `[gate]` asks. These are the outputs as they ran.

The fold-state probe on the atlas before point 7's fix:

""" + block("text", """$ python fold_state.py
instruction    reviews 2  reviewed x2 · folded
flow           reviews 2  reviewed x2 · folded
roles          reviews 2  reviewed x2 · folded
memory         reviews 2  reviewed x2 · folded
runtime        reviews 2  reviewed x2 · folded
observability  reviews 2  reviewed x2 · folded
integrations   reviews 2  reviewed x2 · folded
distribution   reviews 2  reviewed x2 · folded
lexicon        reviews 2  in review               <- unfolded, yet it holds [debt-fold]
review system  reviews 2  in review               <- unfolded, yet it holds [debt-fold]
rows read unfolded despite a fold section: 2
rc 1""") + """
The map's layer arm, applied alone over the old join (`fix_map_layer.py --arm-only`):

""" + block("text", read(S / "night/map_armonly.out") + "\nrc 1") + """
The clause scan, extended to double quotes, before the join:

""" + block("text", """$ python paren_semis.py
dConvergedCharter: ...; Skills converged to level-4 thin entries, each described "Use when …; runs …"; the protocol slices and Skill entries r...
splits inside a clause: 1
rc 1""") + """
The reconciliation probe, its wildcard reading added, before dBoundRoles' `feature` class row:

""" + block("text", read(S / "night/reconcile4.out") + "\nrc 1") + """
The reconciliation probe after the records fold, before the two `code` class rows:

""" + block("text", read(S / "night/reconcile6.out") + "\nrc 1"))
plants = []
for p in ("no-layer", "fates-drop", "fates-ghost", "fates-bad", "fates-unbuilt", "fates-empty", "fates-kit"):
    out, rc = run(B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py", "--check", "--plant", p)
    plants.append(f"$ python map.py --check --plant {p}\n" + "\n".join(l for l in out.split("\n") if l.startswith("FINDING"))
                  + f"\nrc {rc}")
    if rc != 1:
        sys.exit(f"plant {p} did not red")
parts.append("""
## [plants] The map's plants, re-run

""" + block("text", "\n".join(plants)))
final = []
for label, args in (("design map", [B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py", "--check"]),
                    ("atlas", [B + "2026-10-16-build-PLAY-dClosedLoop-1-atlas.py", "--check"]),
                    ("fold state", [str(S / "night/fold_state.py")]),
                    ("reconciliation probe", [str(S / "audit/reconcile_probe.py"),
                                              B + "2026-10-18-build-PLAY-dClosedLoop-1-recut.md"]),
                    ("clause scan", [str(S / "walk/paren_semis.py")]),
                    ("gap join", [str(S / "join_canonical.py"), B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md",
                                  B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"]),
                    ("preset check", [str(S / "preset_check_canonical.py"),
                                      B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"]),
                    ("critical path", [str(S / "order/critical_path.py")])):
    out, rc = run(*args)
    if rc != 0:
        sys.exit(f"{label} is red: {out[-400:]}")
    final.append(f"$ {label}\n{out}\nrc {rc}")
parts.append("""
## [final] Every check, re-run at the commit

""" + block("text", "\n\n".join(final)))
parts.append("""
## [probes] The researchers' probes

Each researcher wrote its probes to the scratchpad and ran them read-only. They are kept here whole. Dispatch 101 re-ran
aScoutedSeam's committed grader on copies of that branch's files, which stay on the branch,
`origin/branch/deterministic-reuse-workflows-f70c33`. Dispatches 100 and 104 measured with inline commands, which their
returns show.
""")
for rel, who in PROBES:
    parts.append(f"### `{pathlib.Path(rel).name}`, {who}\n\n" + block("python", read(S / rel)))
OUT.write_text("\n".join(parts), encoding="utf-8", newline="\n")
print(f"wrote {OUT}: {OUT.stat().st_size} bytes")
````

## [inline] The inline edits, as run

````text
The night pass's inline edits, each run once through a quoted heredoc that held no backslash, as run.

1. fold_state.py read each record by its file name (its first draft passed the name to the atlas's record lookup):
   old: atlas.text(atlas.record(n))
   new: atlas.text(atlas.HERE / n)

2. paren_semis.py, extended to double quotes (four exact replacements, each asserted to match once):
   - the docstring's "inside parentheses or backticks" became "inside parentheses, backticks or double quotes";
   - `depth, tick, at = 0, False, []` became `depth, tick, quote, at = 0, False, False, []`;
   - a backtick toggles `tick` only outside a quote, and a double quote toggles `quote` only outside backticks;
   - a "; " counts as a split when `depth or tick or quote`.

3. fold_np_v2.py's preset rows: its first run refused before writing, its filter matching the catalogue row too, so
   the script was edited to name each preset row exactly (as it now reads), and run again. After it, one sed:
   sed -i 's/^| `tags.bundle-rows` | a row count | 40 |/| `tags.bundle-rows` | 20, 40, 80 | 40 |/' <v2>
   since the preset check reads a free-form value only from a fixed list of phrases; the script was edited to match.

4. The re-cut's `[reconciled-order]`, three class rows, each inserted before the row
   "| dTotalRecall | `roster` | dIndexedDesign | homonym |":
   | dBoundRoles | `feature` | dTotalRecall | tolerance | the work order selects by `feature.*` only once dTotalRecall arms that selector, and its code-notes and `code` slots render "not installed" until dTotalRecall lands, as the `map` slot does (night pass, point 4) |
   | dBoundRoles | `code` | dTotalRecall | tolerance | the work order's `code` slot renders "not installed" until dTotalRecall's `code` record lands, as the `map` slot does (night pass, point 3) |
   | dOrderedCharter | `code` | dTotalRecall | not a use | each role's load set budgets the `code` slot's bytes, and never reads the record (night pass, point 3) |

5. The atlas's step list gained `probe`, by one sed over its `STEPS = [...]` line, after `breakpoint`.

6. The quoted map numbers, updated to the staged tree's (2,232 nodes, 31,133 of 32,768 B; the atlas's 154 records):
   in the night-pass record's `[instrument]` and `[p3-code]`, v2's `[owed]` and gap-mem-30's text.
````

## [red] The red runs, as captured

Each check was seen red before its fix, as `[gate]` asks. These are the outputs as they ran.

The fold-state probe on the atlas before point 7's fix:

````text
$ python fold_state.py
instruction    reviews 2  reviewed x2 · folded
flow           reviews 2  reviewed x2 · folded
roles          reviews 2  reviewed x2 · folded
memory         reviews 2  reviewed x2 · folded
runtime        reviews 2  reviewed x2 · folded
observability  reviews 2  reviewed x2 · folded
integrations   reviews 2  reviewed x2 · folded
distribution   reviews 2  reviewed x2 · folded
lexicon        reviews 2  in review               <- unfolded, yet it holds [debt-fold]
review system  reviews 2  in review               <- unfolded, yet it holds [debt-fold]
rows read unfolded despite a fold section: 2
rc 1
````

The map's layer arm, applied alone over the old join (`fix_map_layer.py --arm-only`):

````text
map: 2170 nodes in 30 namespaces; 29982 B of 32768 (no degrade); folded 14; unarmed none
map: purposes declared 1449, derived 244, pending 477
FINDING layer: kit.agent-instructions joins no layer
FINDING layer: kit.branch-reconcile joins no layer
FINDING layer: kit.codebase-map joins no layer
FINDING layer: kit.drift-audit joins no layer
FINDING layer: kit.gate-lint joins no layer
FINDING layer: kit.govkit joins no layer
FINDING layer: kit.hooks joins no layer
FINDING layer: kit.lexicon joins no layer
FINDING layer: kit.lib joins no layer
FINDING layer: kit.memory-recall joins no layer
FINDING layer: kit.memory-tree joins no layer
FINDING layer: kit.playbook joins no layer
FINDING layer: kit.process-monitor joins no layer
FINDING layer: kit.pytest-parallel-guardrails joins no layer
FINDING layer: kit.roles joins no layer
FINDING layer: kit.run-gates joins no layer
FINDING layer: kit.runlog joins no layer
FINDING layer: kit.unattended joins no layer
FINDING layer: kit.workflows joins no layer
rc 1
````

The clause scan, extended to double quotes, before the join:

````text
$ python paren_semis.py
dConvergedCharter: ...; Skills converged to level-4 thin entries, each described "Use when …; runs …"; the protocol slices and Skill entries r...
splits inside a clause: 1
rc 1
````

The reconciliation probe, its wildcard reading added, before dBoundRoles' `feature` class row:

````text
chain rows 16 · owned nodes read 416 · flow items read 87 · stages 5 · breakpoint items 8, names 7 · contracts read 3 · on a non-ancestor's node 17 (cites 13, stage 0, routes 1, reads 3, registers 0)
left out: systems, cited in prose; points of another layer, not modelled as nodes (5): Observability's entry: Flow's Plan intake, the patch-build entry at Design and the breakpoints; Observability's entry: Memory's record kinds through `record`; Integrations' entry: Flow's verdict backends and release slot; Distribution's entry: Flow's version slot in Test's `test.merge`; Distribution's entry: Test's leg-pack point, for the `currency` leg
  dBoundRoles cites `feature` (dTotalRecall's, not an ancestor): UNCLASSED
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `hooks.bypass` (dWitnessedBar's, not an ancestor): not a use
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dDeclaredLoop cites `run.on-owner-question` (dBoundRoles's, not an ancestor): tolerance
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): homonym
  dDeclaredLoop reads `decisions.major` (dTotalRecall's, not an ancestor): tolerance
  dFairHearing reads `flow.route-backs` (dDeclaredLoop's, not an ancestor): not a use
  dRankedPlan reads `run.host` (dWellOiledMachine's, not an ancestor): tolerance
  dFairHearing routes `review.trigger` (dDeclaredLoop's, not an ancestor): not a use
findings 1
rc 1
````

The reconciliation probe after the records fold, before the two `code` class rows:

````text
chain rows 16 · owned nodes read 418 · flow items read 87 · stages 5 · breakpoint items 8, names 7 · contracts read 3 · on a non-ancestor's node 19 (cites 15, stage 0, routes 1, reads 3, registers 0)
left out: systems, cited in prose; points of another layer, not modelled as nodes (5): Observability's entry: Flow's Plan intake, the patch-build entry at Design and the breakpoints; Observability's entry: Memory's record kinds through `record`; Integrations' entry: Flow's verdict backends and release slot; Distribution's entry: Flow's version slot in Test's `test.merge`; Distribution's entry: Test's leg-pack point, for the `currency` leg
  dBoundRoles cites `code` (dTotalRecall's, not an ancestor): UNCLASSED
  dBoundRoles cites `feature` (dTotalRecall's, not an ancestor): tolerance
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `hooks.bypass` (dWitnessedBar's, not an ancestor): not a use
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dDeclaredLoop cites `run.on-owner-question` (dBoundRoles's, not an ancestor): tolerance
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `code` (dTotalRecall's, not an ancestor): UNCLASSED
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): homonym
  dDeclaredLoop reads `decisions.major` (dTotalRecall's, not an ancestor): tolerance
  dFairHearing reads `flow.route-backs` (dDeclaredLoop's, not an ancestor): not a use
  dRankedPlan reads `run.host` (dWellOiledMachine's, not an ancestor): tolerance
  dFairHearing routes `review.trigger` (dDeclaredLoop's, not an ancestor): not a use
findings 2
rc 1
````


## [plants] The map's plants, re-run

````text
$ python map.py --check --plant no-layer
FINDING layer: kit.agent-instructions joins no layer
rc 1
$ python map.py --check --plant fates-drop
FINDING fates: kit.agent-instructions has no [table] row
rc 1
$ python map.py --check --plant fates-ghost
FINDING fates: a row names ghostkit, which is no kit
rc 1
$ python map.py --check --plant fates-bad
FINDING fates: agent-instructions · harness wiring has the fate MAYBE, outside the set
rc 1
$ python map.py --check --plant fates-unbuilt
FINDING fates: agent-instructions · harness wiring names no chain build where it goes
rc 1
$ python map.py --check --plant fates-empty
FINDING fates: workflows · `orient-counterfactual.js` retires with no replacement named
rc 1
$ python map.py --check --plant fates-kit
FINDING fates: kit.agent-instructions's fate maybe is outside the set
rc 1
````


## [final] Every check, re-run at the commit

````text
$ design map
map: 2232 nodes in 30 namespaces; 31133 B of 32768 (no degrade); folded 14; unarmed none
map: purposes declared 1494, derived 257, pending 481
rc 0

$ atlas
atlas: derived — 154 records, 2630 sections, 175 decision sections, 16 comparison areas, 33 principles
rc 0

$ fold state
instruction    reviews 2  reviewed x2 · folded  
flow           reviews 2  reviewed x2 · folded  
roles          reviews 2  reviewed x2 · folded  
memory         reviews 2  reviewed x2 · folded  
runtime        reviews 2  reviewed x2 · folded  
observability  reviews 2  reviewed x2 · folded  
integrations   reviews 2  reviewed x2 · folded  
distribution   reviews 2  reviewed x2 · folded  
lexicon        reviews 2  reviewed x2 · folded  
review system  reviews 2  reviewed x2 · folded  
rows read unfolded despite a fold section: 0
rc 0

$ reconciliation probe
chain rows 16 · owned nodes read 418 · flow items read 87 · stages 5 · breakpoint items 8, names 7 · contracts read 3 · on a non-ancestor's node 19 (cites 15, stage 0, routes 1, reads 3, registers 0)
left out: systems, cited in prose; points of another layer, not modelled as nodes (5): Observability's entry: Flow's Plan intake, the patch-build entry at Design and the breakpoints; Observability's entry: Memory's record kinds through `record`; Integrations' entry: Flow's verdict backends and release slot; Distribution's entry: Flow's version slot in Test's `test.merge`; Distribution's entry: Test's leg-pack point, for the `currency` leg
  dBoundRoles cites `code` (dTotalRecall's, not an ancestor): tolerance
  dBoundRoles cites `feature` (dTotalRecall's, not an ancestor): tolerance
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `hooks.bypass` (dWitnessedBar's, not an ancestor): not a use
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dDeclaredLoop cites `run.on-owner-question` (dBoundRoles's, not an ancestor): tolerance
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `code` (dTotalRecall's, not an ancestor): not a use
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): homonym
  dDeclaredLoop reads `decisions.major` (dTotalRecall's, not an ancestor): tolerance
  dFairHearing reads `flow.route-backs` (dDeclaredLoop's, not an ancestor): not a use
  dRankedPlan reads `run.host` (dWellOiledMachine's, not an ancestor): tolerance
  dFairHearing routes `review.trigger` (dDeclaredLoop's, not an ancestor): not a use
findings 0
rc 0

$ clause scan
splits inside a clause: 0
rc 0

$ gap join
register keys 250 · chain builds 16
unowned: none
owned twice or more: none
owned but not in the register: none
builds owning nothing: none
rc 0

$ preset check
catalogue keys 206 · presettable 193 · preset rows 193
no findings
rc 0

$ critical path
critical path: 213 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 8, dFairHearing 20, dOrderedCharter 35, dDeclaredLoop 82, dWitnessedBar 106, dBoundRoles 140, dTotalRecall 145, dIndexedDesign 156, dRankedPlan 158, dWellOiledMachine 176, dScopedBuild 187, dTendedCadence 188, dMindYourWords 193, dShippedRelease 196, dCalibratedLens 199, dConvergedCharter 213
rc 0
````


## [probes] The researchers' probes

Each researcher wrote its probes to the scratchpad and ran them read-only. They are kept here whole. Dispatch 101 re-ran
aScoutedSeam's committed grader on copies of that branch's files, which stay on the branch,
`origin/branch/deterministic-reuse-workflows-f70c33`. Dispatches 100 and 104 measured with inline commands, which their
returns show.

### `census.py`, dispatch 103

````python
"""Read-only census of every pointer kind in the tracked tree. Usage: python -I census.py <worktree>"""
import os, re, subprocess, sys, collections, random
root = sys.argv[1]; os.chdir(root)
files = subprocess.run(["git","ls-files","-z"],capture_output=True).stdout.decode("utf-8","replace").split("\0")
files = [f for f in files if f]
def read(f):
    try:
        with open(f,"rb") as h: return h.read().decode("utf-8","replace")
    except Exception: return ""
TEXT = {f: read(f) for f in files if not f.endswith((".png",".jpg",".svg",".ico",".gz",".zip"))}
mem = [f for f in TEXT if f.startswith("memory/")]
code = [f for f in TEXT if f.startswith(("tools/","skills/",".githooks/",".claude/",".github/"))]
docs = [f for f in TEXT if f not in mem and f not in code]
exists = set(files)
dirs = set()
for f in files:
    p = f
    while "/" in p:
        p = p.rsplit("/",1)[0]; dirs.add(p)
def count(rx, group):
    n=0; fs=set()
    for f in group:
        k=len(rx.findall(TEXT[f]))
        if k: n+=k; fs.add(f)
    return n,len(fs)
R = {}
# 1 section tag definitions
sec_def = re.compile(r"^#{2,4} \[([a-z0-9][a-z0-9-]*)\]", re.M)
R["section-tag defs (memory)"] = count(sec_def, mem)
# 2 section tag citations: backticked [tag]
sec_cite = re.compile(r"`\[([a-z0-9][a-z0-9-]*)\]`")
R["`[tag]` citations memory"] = count(sec_cite, mem)
R["`[tag]` citations code"] = count(sec_cite, code)
# 3 charter rule tags
R["charter rule lines AGENTS.md"] = count(re.compile(r"^- \[[a-z0-9-]+\] ", re.M), ["AGENTS.md"])
R["role rules: lines"] = count(re.compile(r"^rules: ", re.M), [f for f in code if f.startswith("tools/roles/")])
# 4 item tags
item = re.compile(r"`(entry|plan|design|build|test|deploy|review|maintain|life|release|kits|adopt|loop)\.[a-z][a-z0-9-]+`")
R["item-tag cites memory"] = count(item, mem); R["item-tag cites code"] = count(item, code)
# 5 namespaced tags ns.x in code (designed namespaces)
ns = re.compile(r"\b(step|item|role|policy|record|section|feature|class|marker|kind|kit|leg|doc|unit|layer|practice|principle)\.[a-z][a-z0-9-]+\b")
R["ns.tag in code (any ns word)"] = count(ns, code)
# 6 ids
idrx = re.compile(r"\b(PLAY|KICK|TOOL|DEPL)-[a-z][A-Za-z0-9]+-\d+\b")
R["ids memory"] = count(idrx, mem); R["ids code"] = count(idrx, code); R["ids docs"]=count(idrx, docs)
gap = re.compile(r"\bgap-[a-z]+-\d+\b")
R["gap ids memory"] = count(gap, mem); R["gap ids code"] = count(gap, code)
# 7 gov: markers
gm = re.compile(r"gov:([a-z][a-z0-9-]*)")
words = collections.Counter(); wf=collections.defaultdict(set)
for f in code+docs:
    for w in gm.findall(TEXT[f]): words[w]+=1; wf[w].add(f)
R["gov: words outside memory"] = (sum(words.values()), len(set().union(*wf.values())))
# 8 paths and file:line
path = re.compile(r"(?<![\w/.-])((?:tools|skills|memory|\.githooks|\.claude|\.github)/[A-Za-z0-9_.@-]+(?:/[A-Za-z0-9_.@*-]+)*)(?::(\d+)(?:-(\d+))?)?")
def path_stats(group):
    tot=0; fl=0; dead=0; deadfl=0; overrun=0; sample=[]
    for f in group:
        for m in path.finditer(TEXT[f]):
            p=m.group(1).rstrip(".,;:)`'\""); tot+=1
            if "*" in p or "<" in p: continue
            ok = p in exists or p.rstrip("/") in dirs
            if not ok: dead+=1
            if m.group(2):
                fl+=1
                if not ok: deadfl+=1
                elif p in TEXT and int(m.group(2)) > TEXT[p].count("\n")+1: overrun+=1
                if ok and p in TEXT: sample.append((f,p,int(m.group(2))))
    return tot,dead,fl,deadfl,overrun,sample
for name,g in (("memory",mem),("code",code),("docs",docs)):
    t,d,fl,dfl,ov,smp = path_stats(g)
    R["paths "+name] = (t, f"dead {d} ({100*d/max(t,1):.1f}%)", f"file:line {fl}", f"file:line dead-file {dfl}", f"line past EOF {ov}")
    if name=="memory": MEMSAMPLE=smp
for k,v in R.items(): print(f"{k}: {v}")
print("gov: words:", ", ".join(f"{w}={n}" for w,n in words.most_common()))
random.seed(4)
s = random.sample(MEMSAMPLE, 40)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"fl_sample.tsv"),"w") as h:
    for f,p,l in s: h.write(f"{f}\t{p}\t{l}\n")
print("file:line sample written:", len(s), "of", len(MEMSAMPLE))
````

### `sec.py`, dispatch 103

````python
"""Section-tag definitions vs backticked [tag] citations under memory/. Read-only."""
import os,re,subprocess,sys,collections
os.chdir(sys.argv[1])
fs=[f for f in subprocess.run(["git","ls-files","memory"],capture_output=True,text=True).stdout.split("\n") if f.endswith(".md")]
D=collections.defaultdict(set); C=[]
dre=re.compile(r"^#{2,4} \[([a-z0-9][a-z0-9-]*)\]",re.M); cre=re.compile(r"`\[([a-z0-9][a-z0-9-]*)\]`")
for f in fs:
    t=open(f,encoding="utf-8",errors="replace").read()
    for m in dre.finditer(t): D[m.group(1)].add(f)
    for m in cre.finditer(t): C.append((f,m.group(1)))
rules=set(re.findall(r"^- \[([a-z0-9-]+)\] ",open("AGENTS.md",encoding="utf-8").read(),re.M))
k=collections.Counter()
for f,t in C:
    if t in D and f in D[t]: k["defined in the citing file"]+=1
    elif len(D.get(t,()))==1: k["one defining file elsewhere"]+=1
    elif len(D.get(t,()))>1: k["2+ defining files (ambiguous unqualified)"]+=1
    elif t in rules: k["charter rule tag"]+=1
    else: k["defined nowhere"]+=1
print("defs",sum(len(v) for v in D.values()),"distinct",len(D),"files",len(set().union(*D.values())))
print("tags defined in 2+ files:",sum(1 for v in D.values() if len(v)>1))
print("citations",len(C)); [print(" ",a,b) for a,b in k.most_common()]
nb=collections.Counter(t for f,t in C if t not in D and t not in rules); print("defined-nowhere top:",nb.most_common(12))
print("defs outside dClosedLoop:", sum(1 for v in D.values() for f in v if "dClosedLoop" not in f))
````

### `fl_drift.py`, dispatch 103

````python
"""For a random sample of `path:line` citations in tracked memory records, compare the cited line at the
commit that wrote the citation with the same line number at HEAD. Read-only. Usage: python -I fl_drift.py <wt> <n> <seed>"""
import os, re, subprocess, sys, random
root, n, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); os.chdir(root)
def git(*a): return subprocess.run(["git",*a],capture_output=True).stdout.decode("utf-8","replace")
files=[f for f in git("ls-files","memory").split("\n") if f.endswith(".md")]
rx=re.compile(r"(?<![\w/.-])((?:tools|skills|\.githooks|\.claude|\.github)/[A-Za-z0-9_.@/-]+\.[a-z]+):(\d+)")
cites=[]
for f in files:
    try: t=open(f,encoding="utf-8",errors="replace").read().split("\n")
    except Exception: continue
    for i,l in enumerate(t,1):
        for m in rx.finditer(l): cites.append((f,i,m.group(1),int(m.group(2))))
print("code file:line citations in memory:", len(cites))
random.seed(seed); smp=random.sample(cites,n)
same=moved=gone=changed=0; rows=[]
for f,i,p,l in smp:
    b=git("blame","--porcelain","-L",f"{i},{i}","HEAD","--",f).split(" ")[0]
    then=git("show",f"{b}:{p}").split("\n")
    now=git("show",f"HEAD:{p}").split("\n")
    if not now or now==[""]: gone+=1; rows.append(("gone",f,i,p,l)); continue
    a=then[l-1].strip() if 0<l<=len(then) else None
    c=now[l-1].strip() if 0<l<=len(now) else None
    if a is not None and a==c: same+=1; k="same"
    elif a is not None and a in [x.strip() for x in now]: moved+=1; k="moved"
    else: changed+=1; k="changed"
    rows.append((k,f,i,p,l,b[:9]))
print(f"sample {n}: same {same}  moved(line text elsewhere) {moved}  changed/removed {changed}  file gone {gone}")
for r in rows[:12]: print(*r)
````

### `dossier.py`, dispatch 103

````python
"""Dossier claims and ids, read-only. Usage: python -I dossier.py <wt>"""
import os,re,subprocess,sys,json,glob,tomllib,fnmatch
os.chdir(sys.argv[1])
def git(*a): return subprocess.run(["git",*a],capture_output=True,text=True,encoding="utf-8",errors="replace").stdout
files=git("ls-files").split("\n")
memtext="\n".join(open(f,encoding="utf-8",errors="replace").read() for f in files if f.startswith("memory/") and f.endswith(".md"))
legs={l["name"] for l in json.load(open("tools/gate-legs.json",encoding="utf-8"))["legs"]} if isinstance(json.load(open("tools/gate-legs.json",encoding="utf-8")),dict) else None
D=sorted(glob.glob("memory/map/features/*.md")); stale=0; deadglob=0; deadleg=0; legn=0; decn=0; deaddec=0; rows=[]
idanchor=re.compile(r"\b(PLAY|KICK|TOOL|DEPL)-([a-z][A-Za-z0-9]+)-(\d+)\b")
for d in D:
    t=open(d,encoding="utf-8").read(); m=re.search(r"```toml\n(.*?)```",t,re.S); c=tomllib.loads(m.group(1))
    gl=c.get("paths",{}).get("globs",[])
    hit=[f for f in files if any(fnmatch.fnmatch(f,g) for g in gl)]
    if not hit: deadglob+=1
    dl=git("log","-1","--format=%ct","--",d).strip(); pl=git("log","-1","--format=%ct","--",*gl).strip() if gl else ""
    if pl and dl and int(pl)>int(dl): stale+=1
    for lg in c.get("claims",{}).get("gate-legs",[]):
        legn+=1
        if legs is not None and lg not in legs: deadleg+=1
    for i in c.get("decisions",[]):
        decn+=1; mm=idanchor.match(i)
        if not mm or not os.path.isdir(f"memory/builds/{mm.group(2)}") : deaddec+=1
print(f"dossiers {len(D)}; code newer than dossier {stale}; globs matching nothing {deadglob}")
print(f"claimed gate legs {legn}, not in gate-legs.json {deadleg}; decision ids {decn}, build folder missing {deaddec}")
# ids cited in code that appear nowhere in memory
codeids=set()
for f in files:
    if f.startswith(("tools/","skills/",".githooks/",".claude/",".github/")):
        try: codeids|={m.group(0) for m in idanchor.finditer(open(f,encoding="utf-8",errors="replace").read())}
        except Exception: pass
miss=sorted(i for i in codeids if i not in memtext)
print(f"distinct ids cited in code {len(codeids)}; appearing nowhere in memory/*.md {len(miss)}: {miss[:8]}")
````

### `regions.py`, dispatch 103

````python
"""Balance of every existing begin/end region family in the tracked tree. Read-only."""
import os,re,subprocess,sys,collections
os.chdir(sys.argv[1])
fs=[f for f in subprocess.run(["git","ls-files"],capture_output=True,text=True).stdout.split("\n") if f]
fam={
 ">>>/<<< inline copy": (re.compile(r"^\s*(?:#|//) >>> ([A-Za-z_]\w*)"), re.compile(r"^\s*(?:#|//) <<< ([A-Za-z_]\w*)")),
 "gov:argv": (re.compile(r"^\s*# gov:argv-begin()$"), re.compile(r"^\s*# gov:argv-end()$")),
 "gov:conf-allow": (re.compile(r"^\s*# gov:conf-allow-begin()$"), re.compile(r"^\s*# gov:conf-allow-end()$")),
 "gov:playbook": (re.compile(r"^<!-- gov:playbook -->()$"), re.compile(r"^<!-- /gov:playbook -->()$")),
 "README gen:/roster:": (re.compile(r"^<!-- ((?:gen|roster):[a-z-]+) -->$"), re.compile(r"^<!-- /((?:gen|roster):[a-z-]+) -->$")),
}
for name,(o,c) in fam.items():
    pairs=0; bad=[]; files=0
    for f in fs:
        try: L=open(f,encoding="utf-8",errors="replace").read().split("\n")
        except Exception: continue
        st=[]; hit=False
        for i,l in enumerate(L,1):
            l=l.rstrip("\r")
            m=o.match(l)
            if m: st.append((m.group(1),i)); hit=True; continue
            m=c.match(l)
            if m:
                hit=True
                if st and st[-1][0]==m.group(1): st.pop(); pairs+=1
                else: bad.append((f,i,"close without open"))
        bad+= [(f,i,"open without close") for _,i in st]
        files+=hit
    print(f"{name}: files {files} pairs {pairs} unbalanced {len(bad)} {bad[:3]}")
````

### `spans.py`, dispatch 103

````python
"""For one feature's outside readers: cluster the feature's lines into spans, and test whether each span
sits inside a symbol whose extent a map could derive (py: ast; js/sh: brace/function scan). Read-only."""
import os,re,sys,ast,subprocess
os.chdir(sys.argv[1]); pat=re.compile(sys.argv[2]); files=sys.argv[3:]
def py_syms(t):
    out=[]
    for n in ast.walk(ast.parse(t)):
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): out.append((n.lineno,n.end_lineno,n.name))
    return out
def brace_syms(L,kind):
    out=[]; 
    fre = re.compile(r"^\s*(?:function\s+)?([A-Za-z_][\w]*)\s*\(\)\s*\{") if kind=="sh" else re.compile(r"^\s*(?:async\s+)?function\s*\*?\s*([A-Za-z_$][\w$]*)\s*\(|^\s*(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:function|\([^)]*\)\s*=>)")
    for i,l in enumerate(L):
        m=fre.match(l)
        if not m: continue
        d=0; started=False
        for j in range(i,len(L)):
            s=re.sub(r"(\"[^\"]*\"|'[^']*'|`[^`]*`)","",L[j]); s=s.split("#")[0] if kind=="sh" else s.split("//")[0]
            d+=s.count("{")-s.count("}"); started|=("{" in s)
            if started and d<=0: out.append((i+1,j+1,m.group(1) or m.group(2))); break
    return out
tot_sp=tot_in=tot_lines=0
for f in files:
    t=open(f,encoding="utf-8",errors="replace").read(); L=t.split("\n")
    hits=[i+1 for i,l in enumerate(L) if pat.search(l)]
    if not hits: continue
    sp=[]; 
    for h in hits:
        if sp and h-sp[-1][1]<=8: sp[-1][1]=h
        else: sp.append([h,h])
    ext=os.path.splitext(f)[1] or (".sh" if L[0].startswith("#!") and "sh" in L[0] else "")
    try: syms = py_syms(t) if ext==".py" else brace_syms(L,"sh" if ext in (".sh","") else "js") if ext in (".sh",".js","") else []
    except Exception: syms=[]
    inside=0
    for a,b in sp:
        enc=[s for s in syms if s[0]<=a and b<=s[1] and (s[1]-s[0])<400]
        inside+= bool(enc)
    n=sum(b-a+1 for a,b in sp)
    tot_sp+=len(sp); tot_in+=inside; tot_lines+=n
    print(f"{f}: lines {len(L)} spans {len(sp)} span-lines {n} inside a <400-line symbol {inside}")
print(f"TOTAL spans {tot_sp} span-lines {tot_lines} inside derivable symbol {tot_in} ({100*tot_in/max(tot_sp,1):.0f}%)")
````

### `spandecay.py`, dispatch 103

````python
"""Line-range anchor survival: Python def/class extents at an old commit vs HEAD. Read-only (git show)."""
import os,sys,ast,subprocess
os.chdir(sys.argv[1]); old=sys.argv[2]
def git(*a): return subprocess.run(["git",*a],capture_output=True,text=True,encoding="utf-8",errors="replace").stdout
def syms(rev):
    out={}
    for f in git("ls-tree","-r","--name-only",rev,"--","tools","skills").split("\n"):
        if not f.endswith(".py"): continue
        try: tree=ast.parse(git("show",f"{rev}:{f}"))
        except Exception: continue
        for n in ast.walk(tree):
            if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): out.setdefault((f,n.name),(n.lineno,n.end_lineno))
    return out
a=syms(old); b=syms("HEAD")
same=shift=gone=0
for k,v in a.items():
    if k not in b: gone+=1
    elif b[k]==v: same+=1
    else: shift+=1
n=len(a); print(f"symbols at {old[:9]} {n}: same line range {same} ({100*same/n:.1f}%), range changed {shift} ({100*shift/n:.1f}%), path::name gone {gone} ({100*gone/n:.1f}%)")
````

### `codemap.py`, dispatch 102

````python
"""Read-only probe: derive a code map (files, defs, imports, calls, tests, cross-language edges) and size it."""
import ast, json, os, re, subprocess, sys, time, hashlib, collections
t0=time.perf_counter()
files=subprocess.run(['git','ls-files','tools','skills','.githooks'],capture_output=True,text=True).stdout.split()
py=[f for f in files if f.endswith('.py')]; sh=[f for f in files if f.endswith('.sh') or (f.startswith('.githooks/') and '.' not in os.path.basename(f))]; js=[f for f in files if f.endswith('.js')]
defs=[]; imports=[]; calls=[]; doc=0
modname={f:os.path.splitext(os.path.basename(f))[0] for f in py}
bymod=collections.defaultdict(list)
for f in py: bymod[modname[f]].append(f)
for f in py:
    src=open(f,encoding='utf-8').read(); tree=ast.parse(src)
    def walk(node,q):
        global doc
        for ch in ast.iter_child_nodes(node):
            if isinstance(ch,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
                name=q+ch.name
                seg=ast.get_source_segment(src,ch) or ''
                ds=ast.get_docstring(ch)
                doc+= 1 if ds else 0
                defs.append(dict(f=f,s=name,k=type(ch).__name__[:5],l=ch.lineno,e=ch.end_lineno,h=hashlib.sha1(seg.encode()).hexdigest()[:10],d=bool(ds)))
                walk(ch,name+'.')
            else: walk(ch,q)
    walk(tree,'')
    alias={}
    for n in ast.walk(tree):
        if isinstance(n,ast.Import):
            for a in n.names: imports.append((f,a.name)); alias[(a.asname or a.name).split('.')[0]]=a.name
        elif isinstance(n,ast.ImportFrom):
            for a in n.names: imports.append((f,(n.module or '')+':'+a.name)); alias[a.asname or a.name]=(n.module or '')+':'+a.name
    for n in ast.walk(tree):
        if isinstance(n,ast.Call):
            fn=n.func
            if isinstance(fn,ast.Name): calls.append((f,n.lineno,'name',fn.id,alias.get(fn.id)))
            elif isinstance(fn,ast.Attribute) and isinstance(fn.value,ast.Name): calls.append((f,n.lineno,'attr',fn.value.id+'.'+fn.attr,alias.get(fn.value.id)))
            else: calls.append((f,n.lineno,'other','',None))
t1=time.perf_counter()
# resolve: local def in same file, or imported module that is a repo module
deffile=collections.defaultdict(set)
for d in defs:
    if '.' not in d['s']: deffile[d['s']].add(d['f'])
local_mods=set(bymod)
res=collections.Counter(); edges=set()
for f,l,kind,name,al in calls:
    if kind=='name':
        if name in deffile and f in deffile[name]: res['local']+=1; edges.add((f,name,f))
        elif al and ':' in al and al.split(':')[0].split('.')[-1] in local_mods:
            m=al.split(':')[0].split('.')[-1]; tgt=[x for x in bymod[m] if name in {d for d in deffile if x in deffile[d]}]
            res['imported-resolved' if tgt else 'imported-unresolved']+=1
            for x in tgt: edges.add((f,al.split(':')[1],x))
        else: res['builtin/external/unresolved']+=1
    elif kind=='attr':
        mod=name.split('.')[0]; m=(al or '').split('.')[-1]
        if m in local_mods and al and ':' not in al:
            tgt=[x for x in bymod[m] if x in deffile.get(name.split('.')[1],set())]
            res['module-attr-resolved' if tgt else 'module-attr-unresolved']+=1
            for x in tgt: edges.add((f,name.split('.')[1],x))
        else: res['method/external attr']+=1
    else: res['other']+=1
t2=time.perf_counter()
# shell defs and edges
shdefs=[];shedges=[];jsdefs=[];jsedges=[]
FN=re.compile(r'^\s*(?:function\s+)?([A-Za-z_][\w-]*)\s*\(\)\s*\{',re.M)
INV=re.compile(r'(?:python3?|bash|sh|node|\$PY(?:THON)?|"\$\{?PY\w*\}?")\s+"?(?:\$[\w{}]+/)*([\w./-]+\.(?:py|sh|js))')
SRC=re.compile(r'^\s*(?:source|\.)\s+"?(?:\$[\w{}()\-]+/)*([\w./-]+\.sh)',re.M)
for f in sh:
    t=open(f,encoding='utf-8',errors='replace').read()
    shdefs+= [(f,m.group(1)) for m in FN.finditer(t)]
    shedges+= [(f,'invokes',m.group(1)) for m in INV.finditer(t)]+[(f,'sources',m.group(1)) for m in SRC.finditer(t)]
JF=re.compile(r'\bfunction\s+([A-Za-z_$][\w$]*)\s*\(|\b(?:const|let)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:function|\([^)]*\)\s*=>)')
REQ=re.compile(r'require\(\s*[\'"]([^\'"]+)[\'"]\s*\)')
for f in js:
    t=open(f,encoding='utf-8',errors='replace').read()
    jsdefs+=[(f,m.group(1) or m.group(2)) for m in JF.finditer(t)]
    jsedges+=[(f,'requires',m.group(1)) for m in REQ.finditer(t) if m.group(1).startswith('.')]
for f in py:
    t=open(f,encoding='utf-8').read()
    shedges+=[(f,'invokes',m.group(1)) for m in re.finditer(r'[\'"]([\w./-]+\.(?:sh|js))[\'"]',t)]
t3=time.perf_counter()
# tests: test files and what they name
tests=[f for f in files if re.search(r'(^|/)(test_[^/]*\.py|[^/]*\.test\.sh|selftest\.py|[^/]*selftest[^/]*)$',f)]
tedges=0
for f in tests:
    t=open(f,encoding='utf-8',errors='replace').read()
    tedges+=len({x for x in files if x!=f and os.path.basename(x) in t})
t4=time.perf_counter()
fileline=sum(len(f)+2+40 for f in files)  # one line per file: path + ~40B purpose
rec=json.dumps(dict(defs=defs,imports=imports,edges=sorted(edges),sh=shdefs,she=shedges,js=jsdefs,jse=jsedges))
print(f'files {len(files)} py {len(py)} sh {len(sh)} js {len(js)}')
print(f'py defs {len(defs)} (top-level {sum(1 for d in defs if "." not in d["s"])}, methods/nested {sum(1 for d in defs if "." in d["s"])}), with docstring {doc} ({100*doc/len(defs):.1f}%)')
print(f'py imports {len(imports)}  call sites {len(calls)}  resolved edges {len(edges)}')
for k,v in res.most_common(): print(f'   calls {k}: {v} ({100*v/len(calls):.1f}%)')
print(f'shell defs {len(shdefs)} shell/py cross-lang edges {len(shedges)}  js defs {len(jsdefs)} js requires {len(jsedges)}')
print(f'test files {len(tests)} test->file name edges {tedges}')
print(f'record bytes (json, uncompressed) {len(rec)}  file-level level-0 lines est {fileline} B')
print(f'time: py ast+calls {t1-t0:.2f}s resolve {t2-t1:.2f}s sh/js {t3-t2:.2f}s tests {t4-t3:.2f}s total {t4-t0:.2f}s')
json.dump(dict(defs=defs,edges=sorted(edges),she=shedges,jse=jsedges,files=files,tests=tests),open(sys.argv[1],'w'))
````

### `nbhd2.py`, dispatch 102

````python
import json,sys,os,re,collections
S=sys.argv[1]
cm=json.load(open(S+'/codemap.json')); reads=json.load(open(S+'/reads24.json'))
files=set(cm['files']); base=collections.defaultdict(set)
for f in files: base[os.path.basename(f)].add(f)
PROC={'tools/memory-tree/gotchas.py','tools/lexicon/lexicon.py','tools/codebase-map/gen_map.py','tools/memory-tree/gen_build_index.py','skills/session-kickoff/manifest-check.sh','tools/memory-tree/check-memory-hygiene.sh','tools/check-spec-tokens.py','tools/codebase-map/reuse_lookup.py','tools/memory-recall/query.py','tools/check-install-prefix.sh','tools/push-main.sh','tools/drift-audit/drift_report.py','tools/memory-tree/check-verdict-epoch.sh','tools/line-length-limits.txt','tools/template-size-highwater.txt','tools/template-size-limits.txt'}|{f for f in files if f.startswith('.githooks/')}
out=collections.defaultdict(set); inn=collections.defaultdict(set)
def add(a,b):
    if b and a!=b: out[a].add(b); inn[b].add(a)
for a,_,b in cm['edges']: add(a,b)
def resolve(n,src):
    if n in files: return n
    c=base.get(os.path.basename(n),set())
    if len(c)==1: return next(iter(c))
    same=[x for x in c if x.split('/')[:2]==src.split('/')[:2]]
    return same[0] if len(same)==1 else None
for a,_,n in cm['she']+cm['jse']: add(a,resolve(n,a))
reg=0
for f in files:
    if f.endswith(('.json','.toml')):
        t=open(f,encoding='utf-8',errors='replace').read()
        for m in set(re.findall(r'((?:tools|skills|\.githooks)/[\w./-]+\.(?:py|sh|js))',t)):
            if m in files and m!=f: add(f,m); reg+=1
print('registry edges',reg)
tests=set(cm['tests']); tt={t:open(t,encoding='utf-8',errors='replace').read() for t in tests}
def kit(f): p=f.split('/'); return '/'.join(p[:2]) if len(p)>2 else None
bykit=collections.defaultdict(set)
for f in files:
    if kit(f): bykit[kit(f)].add(f)
def hop(seed,withkit):
    n=set(seed)
    for f in seed:
        n|=out[f]|inn[f]|{t for t in tests if t!=f and os.path.basename(f) in tt[t]}
        if withkit and kit(f): n|=bykit[kit(f)]
    return n
ws=[l.strip() for l in open(S+'/ws24.txt') if l.strip()]
first=json.loads(open(sys.argv[2],encoding='utf-8').readline())['message']['content']
first=first if isinstance(first,str) else ''.join(x.get('text','') for x in first)
swseed=sorted({m.rstrip('.,:;)`') for m in re.findall(r'((?:tools|skills|\.githooks)/[\w./-]+)',first)} & files)
spec=set(l.strip() for l in open(S+'/spec24.txt') if l.strip() in files)
for who,key,seed in [('builder','agent-adce44e26da247627.jsonl',ws),('spec writer','agent-a8d6dbd5da111b2da.jsonl',swseed)]:
    r=(set(reads[key])&files)-PROC
    for lab,s in [('seed only',set(seed)),('1-hop',hop(seed,False)),('1-hop + kit',hop(seed,True)),('2-hop',hop(hop(seed,False),False)),('2-hop + kit',hop(hop(seed,True),True)),('spec-named (after)',spec)]:
        hit=r&s; by=sum(os.path.getsize(f) for f in s)
        print(f'{who:11} {lab:18} files {len(s):4} recall {len(hit):2}/{len(r)} = {100*len(hit)/max(1,len(r)):3.0f}%  list {sum(len(f)+1 for f in s):5} B  their content {by/1024:7.0f} KiB')
    print(f'{who:11} feature reads (procedure tools removed): {len(r)}; missed by 1-hop+kit: {sorted(r-hop(seed,True))}')
````

### `probe_unit.py`, dispatch 102

````python
import sys,json,re,collections
CODE=re.compile(r'(?:^|[\s"\'/])((?:tools|skills|\.githooks|\.claude/hooks)/[\w./-]+)')
LOOK=re.compile(r'\b(grep|rg|git grep|find|ls|git ls-files)\b')
READ=re.compile(r'\b(cat|sed|head|tail|awk|wc)\b')
def text_of(c):
    if isinstance(c,str): return c
    out=[]
    for x in c or []:
        if isinstance(x,dict):
            if x.get('type')=='text': out.append(x.get('text',''))
            elif x.get('type')=='tool_result':
                cc=x.get('content'); out.append(text_of(cc) if not isinstance(cc,str) else cc)
    return ''.join(out)
for p in sys.argv[1:]:
    lines=[json.loads(l) for l in open(p,encoding='utf-8')]
    first=text_of(lines[0]['message']['content'])
    calls=[];res={}
    for l in lines:
        m=l.get('message',{})
        for x in m.get('content',[]) if isinstance(m.get('content'),list) else []:
            if x.get('type')=='tool_use': calls.append(x)
            if x.get('type')=='tool_result': res[x.get('tool_use_id')]=len(text_of([x]).encode())
    k=collections.Counter(); b=collections.Counter(); files=set()
    for c in calls:
        n=c['name'];i=c.get('input',{});s=json.dumps(i)
        isc=bool(CODE.search(' '+s))
        if n=='Read':
            cls='read-code' if isc else 'read-other'
            if isc: files.add(i.get('file_path','').replace(chr(92),'/').split('coding-governance/')[-1].split('b80cc3/')[-1])
        elif n in('Grep','Glob'): cls='lookup-code' if isc or 'tools' in s or 'path' not in i else 'lookup-other'
        elif n=='Bash':
            cmd=i.get('command','')
            if LOOK.search(cmd): cls='lookup-code' if isc or 'tools' in cmd else 'lookup-other'
            elif READ.search(cmd): cls='read-code' if isc else 'read-other'
            else: cls='bash-other'
            if isc and cls=='read-code': files.update(m for m in CODE.findall(' '+cmd))
        else: cls=n
        k[cls]+=1; b[cls]+=res.get(c['id'],0)
    print(p.split('/')[-1],'prompt B',len(first.encode()),'code paths named in prompt',len(set(CODE.findall(' '+first))),'calls',len(calls))
    for cls in sorted(k): print(f'  {cls:14} n={k[cls]:4} bytes={b[cls]}')
    print('  distinct code files read',len(files))
````

### `lookups.py`, dispatch 102

````python
import json,sys,re,collections
cm=json.load(open(sys.argv[1]))
names={d['s'].split('.')[-1] for d in cm['defs']}
shn=set()
for f in cm['files']:
    if f.endswith('.sh'):
        for m in re.finditer(r'^\s*(?:function\s+)?([A-Za-z_][\w-]*)\s*\(\)\s*\{',open(f,encoding='utf-8',errors='replace').read(),re.M): shn.add(m.group(1))
names|=shn
for p in sys.argv[2:]:
    c=collections.Counter(); ex=collections.defaultdict(list)
    for l in open(p,encoding='utf-8'):
        d=json.loads(l);m=d.get('message',{});cc=m.get('content')
        if not isinstance(cc,list): continue
        for x in cc:
            if x.get('type')!='tool_use': continue
            n=x['name'];i=x.get('input',{})
            if n=='Grep': pat=i.get('pattern','')
            elif n=='Bash' and re.search(r'\b(grep|rg|git grep)\b',i.get('command','')):
                mm=re.search(r'(?:grep|rg)[^\'"]*[\'"]([^\'"]+)[\'"]',i['command']); pat=mm.group(1) if mm else i['command'][:60]
            elif n in('Glob',) or (n=='Bash' and re.search(r'\b(ls|find|git ls-files)\b',i.get('command',''))): c['locate-files']+=1; continue
            else: continue
            toks=set(re.findall(r'[A-Za-z_][\w-]{3,}',pat))
            hit=toks&names
            cls='symbol (def/caller)' if hit else ('line-number/structure' if re.search(r'\^|\b|def |\(\)',pat) else 'text/literal')
            c[cls]+=1; ex[cls].append(pat[:50])
    print(p.split('/')[-1],dict(c))
    for k,v in ex.items(): print('  ',k,v[:6])
````
