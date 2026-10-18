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

### `build_args_night.py`

The closing review's args: a light diff review of the night-pass commit at medium.

````python
"""Build the args of the night pass's closing review: a light Tier-2 diff review of the night-pass commit, at the
owner's medium effort, from the audit fold's closing review's args.

Usage: python -X utf8 build_args_night.py <scratch-dir> <base> <head>   (from the worktree root)
Writes <scratch-dir>/night/args-night-review.json.
"""
import json
import pathlib
import subprocess
import sys

S, BASE, HEAD = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]
B = "memory/builds/dClosedLoop/build/"
REPORT = "memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md"
a = json.loads((S / "audit" / "args-fold-review.json").read_text(encoding="utf-8"))
full = lambda r: subprocess.run(["git", "rev-parse", r], capture_output=True, text=True, check=True).stdout.strip()
a["base"], a["head"] = full(BASE), full(HEAD)
a["intensity"], a["round"], a["scratch"] = "light", 1, (S / "review-night-pass").as_posix()
a["efforts"] = {"diffFinder": "medium", "skeptic": "medium", "synthesis": "medium"}
a["specs"] = a["specs"] + [B + "2026-10-18-build-PLAY-dClosedLoop-1-fates.md",
                           B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md"]
for p in a["specs"]:
    if not pathlib.Path(p).exists():
        sys.exit(f"missing: {p}")
if pathlib.Path(REPORT).exists():
    sys.exit(f"{REPORT} exists")
a["checklist"] = subprocess.run([sys.executable, "tools/memory-tree/gotchas.py", "--for-diff", f"{BASE}..{HEAD}"],
                                capture_output=True, text=True, encoding="utf-8", check=True).stdout
a["byDesign"] = "\n".join([
    "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to "
    "the chain builds, and a row's planned units are prose, counted one per clause.",
    "- The owner's eight points, recorded verbatim in the night-pass record's [words], are decisions where they "
    "direct: unattended is the default state, attendance changes only the owner's interactions, testing can happen "
    "anywhere, code depth is core, and playbook mode stays in the flow. A finding may show the fold contradicting a "
    "record or the tree, not re-argue the owner's direction.",
    "- The forks NP-1 to NP-24 are parked for the owner. A key's default marked pending is the recommendation shown "
    "until the owner answers; a finding may show that a pending default contradicts a record, not that a fork should "
    "have been settled.",
    "- Every earlier answer stands: PM-1 to PM-12, RC-1 to RC-9, AF-1 to AF-3, FL1, CX-1 to CX-3, RT-1 to RT-4, KN-1 "
    "as the night pass amends it, and every round's before them.",
    "- The five research returns (research-unattended-core, -testing-anywhere, -code-orientation, -relational-syntax "
    "and -tool-fates) are verbatim and dated, and their prompts are rendered handoffs: neither is under review. The "
    "instruments record holds the scripts as they ran.",
    "- Dated records keep what held when they were written: revision notes, the session log's past entries, and the "
    "ownership record's approved tables, which its [amended] bullets amend.",
    "- Generated files (memory/LIVE.md and the build README's generated regions) are rendered, not reviewed. The map "
    "generator's and the atlas's changes are instruments, and are reviewed: can each new arm fail, and does each say "
    "what it does not check?",
])
a["context"] = (
    "The diff is one commit, " + a["head"][:9] + " over " + a["base"][:9] + ": build dClosedLoop's night pass, which "
    "worked the owner's eight points into the design while the owner was away. dClosedLoop is a design-only build that "
    "re-architects gov onto one loop. The night-pass record, " + B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md, "
    "says what each point changed ([p1-unattended] to [p8-fates]), the chain's growth ([chain-impact]) and the parked "
    "forks ([forks]). The edits land in v2 (P4, P20, P25 amended, P31 to P33 added, thirteen keys and their preset rows, "
    "every [chain] row's new clauses and owned gaps, [owed]), flow-steps (the `repeat` disposition, the entry-time "
    "probe, [rules], the attendance gates in [breakpoint], a new [probe] program, attend and unattend in [lifecycle], "
    "the fix pass in [test]), the gap register (28 gaps), layer-memory's kinds, layer-runtime's driver and binding, "
    "layer-instruction, layer-library, the project map, the systems record, the ownership amendment, the re-cut's "
    "class rows, a new fates record of 131 parts, and the design map's and the atlas's generators. Review it as a "
    "design change. Does each edit say one thing, the same way in every record it touches, and leave no text that "
    "still states the old answer, such as an attended session that drives or keeps its freedom? Does every new item, "
    "key and record kind have one owner, and does every step's or row's new dependency sit on its own build or an "
    "ancestor, or in a slot that renders not installed? Does each probe, attendance and code clause close the gaps it "
    "owns? Is each fate in the fates record right against the tree and the design, and does each destination exist? "
    "Can each new check arm fail? A fold's own text is new surface: check it as hard as the text it replaced. Write the "
    "report to " + REPORT + ". Its head carries an H1, then, within its first twelve lines, the line `**Serves:** "
    "diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH "
    "FIXES or BLOCKED and nothing else.")
out = S / "night" / "args-night-review.json"
out.write_text(json.dumps(a, indent=1, ensure_ascii=False), encoding="utf-8", newline="\n")
print(f"args: {a['kind']} {a['base'][:9]}..{a['head'][:9]}, {a['intensity']}, {len(a['specs'])} specs, checklist "
      f"{len(a['checklist'].splitlines())} lines, efforts {a['efforts']}, context {len(a['context'].split())} words")
````

### `plain_cites.py`

H2: plain-word spellings of a non-ancestor's record kind in the chain rows, measured.

````python
"""Measure H2's proposed widening of the reconciliation probe's cites rule: plain-word spellings of owned record kinds
(and roles), whole-word, in each [chain] row, owned by a build that is not the row's own or an ancestor.

Usage: python -X utf8 plain_cites.py   (from the worktree root); prints every hit, grouped by node
"""
import collections
import importlib.util
import re

B = "memory/builds/dClosedLoop/build/"
spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)
A, ns = mp.derive()
owner = {}
for n in ns["record-kind"]:
    own = [v for k, vs in n["rels"] if k == "owner" for v in vs]
    if own:
        owner[n["key"].replace("-", " ")] = own[0]
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
rows, parents = {}, {}
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        rows[m.group(1)] = m.group(4)
        parents[m.group(1)] = [p.strip() for p in m.group(3).split(",") if p.strip() in names]


def anc(b, acc=None):
    acc = set() if acc is None else acc
    for p in parents[b]:
        if p not in acc:
            acc.add(p)
            anc(p, acc)
    return acc


hits = collections.defaultdict(list)
for b, text in rows.items():
    plain = re.sub(r"`[^`]*`", " ", text)          # backticked tokens are the existing rule's
    for kind, own in owner.items():
        if own == b or own in anc(b):
            continue
        if re.search(r"(?<![\w-])" + re.escape(kind) + r"(?![\w-])", plain):
            hits[kind].append(f"{b} ({own}'s)")
total = sum(len(v) for v in hits.values())
for k in sorted(hits, key=lambda k: -len(hits[k])):
    print(f"{k:22} {len(hits[k]):3}  {', '.join(hits[k][:6])}{' …' if len(hits[k]) > 6 else ''}")
print(f"plain-word hits on a non-ancestor's record kind: {total}, over {len(hits)} kinds")
````

### `pinned_counts.py`

After the fold's commit: the design records' quoted map counts and their pins, run over the real tree before the map's arm was written.

````python
"""Probe: the design records that state a design map count (its nodes, or its bytes against the 32,768 cap) as a
current fact, with no commit pinning it. A count the map prints goes stale with every fold, so a record may quote it
only as a snapshot pinned to a sha on the same line.

Usage: python -X utf8 pinned_counts.py   (from the worktree root); rc 1 on an unpinned quote
Reads every build record except research returns, instruments, the session log and the review reports, which are
dated by their own kind. It does not read counts spelled without a thousands comma, or quotes split across lines.
"""
import pathlib
import re
import sys

B = pathlib.Path("memory/builds/dClosedLoop/build")
SKIP = ("-research-", "-instruments", "-session-log")
COUNT = re.compile(r"\b\d{1,3}(?:,\d{3})+ (?:nodes\b|of (?:its |the )?32,768\b)")
PIN = re.compile(r"`[0-9a-f]{7,40}`")

found = pinned = 0
for p in sorted(B.glob("*.md")):
    if any(s in p.name for s in SKIP):
        continue
    for i, line in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
        for m in COUNT.finditer(line):
            if PIN.search(line):
                pinned += 1
                continue
            found += 1
            print(f"UNPINNED {p.name}:{i}: {m.group(0)!r} in {line.strip()[:110]!r}")
print(f"map counts quoted: {found + pinned} · pinned {pinned} · unpinned {found}")
sys.exit(1 if found else 0)
````

### `pinned_counts2.py`

The same, widened to the class: every derived count the map's arm reads, each with its disposition, through the generator's own patterns.

````python
"""Probe, widened to the class: every derived count the design records quote (the map's nodes or bytes, and the
chain's critical path), each with its disposition: pinned on its line, inside a fenced run capture, or unpinned. It
imports the map generator's own COUNT and PIN, so the population it prints is the one the map's arm reads.

Usage: python -X utf8 pinned_counts2.py   (from the worktree root); rc 1 on an unpinned quote
"""
import importlib.util
import pathlib
import re
import sys

B = pathlib.Path("memory/builds/dClosedLoop/build")
spec = importlib.util.spec_from_file_location("map", B / "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

tally = {"pinned": 0, "fenced": 0, "unpinned": 0}
for p in sorted(B.glob("*.md")):
    if any(s in p.name for s in M.DATED):
        continue
    fence = ""
    for i, row in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
        f = re.match(r"\s*(`{3,})", row)
        if f and not fence:
            fence = f.group(1)
            continue
        if f and len(f.group(1)) >= len(fence) and not row.strip().strip("`"):
            fence = ""
            continue
        for m in M.COUNT.finditer(row):
            how = "fenced" if fence else "pinned" if M.PIN.search(row) else "unpinned"
            tally[how] += 1
            print(f"{how:8} {p.name}:{i}: {m.group(0)!r}")
print("derived counts quoted: " + " · ".join(f"{k} {v}" for k, v in tally.items()))
sys.exit(1 if tally["unpinned"] else 0)
````

### `fold_np_self.py`

The night pass's own sweep while the review ran: one actor per probe item, the observation entry.place returns, verify-at-plan's route, and Design's seventh input.

````python
"""The night pass's self-review, found while its closing review ran, folded beside the review's own findings.

1. `probe.design`'s actor was chosen by a policy key, `probe.verifier`, and by the probe's kind. flow-steps `[rules]`
   gives every item one actor, and an item whose actor a policy value chooses becomes one item per value. So the
   experiment gets its own item, `probe.experiment` (the researcher), `probe.design` keeps the tester, and the
   verifier is a structural decision, NP-5, not a key: `probe.verifier` leaves the catalogue and the presets.
2. `entry.place` routed on "an observation the request claims", which no field of its return carried. Its return now
   names the observations.
3. `probe.observations: verify-at-plan` had no route (the class `policy-value-with-no-route`). `plan.input` now routes
   an owed observation to `probe.trigger` first.
4. The `repeat` disposition sent a playbook run into Design, whose inputs did not list it. Design gains a seventh
   input, and `design.input` routes it.

Usage: python -X utf8 fold_np_self.py   (from the worktree root); refuses unless every anchor matches exactly once.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
F = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
# 1. The probe's design items, one actor each.
F.sub("""| `probe.pin` | command | `probe.trigger` | pins the subject by SHA, and records the question, the kind and the losing outcome before anything runs | the probe record's head, its losing outcome committed first | `probe.design` | dDeclaredLoop |
| `probe.design` | the role `probe.verifier` names; for an experiment, the researcher | `probe.pin` | declares the method: the commands, or the `experiment` shape with its corpus, its variants and its judge | the method's schema check, and an experiment's fan checked against `probe.experiment.authority` | `probe.run`; an experiment beyond its authority → an owner item, resolved as `[breakpoint]`'s owner gate is | dDeclaredLoop |
| `probe.run` | executor | `probe.design` |""",
      """| `probe.pin` | command | `probe.trigger` | pins the subject by SHA, and records the question, the kind and the losing outcome before anything runs | the probe record's head, its losing outcome committed first | a verification or a reproduction → `probe.design`; an experiment → `probe.experiment` | dDeclaredLoop |
| `probe.design` | tester | `probe.pin` | declares the commands that test the claim at the pinned SHA, cold: from the claim and the subject, never from the asker's reasoning | the method's schema check | `probe.run` | dDeclaredLoop |
| `probe.experiment` | researcher | `probe.pin` | declares the experiment: the `experiment` shape with its corpus, its variants and its judge | the method's schema check, and the experiment's fan checked against `probe.experiment.authority` | `probe.run`; an experiment beyond its authority → an owner item, resolved as `[breakpoint]`'s owner gate is | dDeclaredLoop |
| `probe.run` | executor | `probe.design` or `probe.experiment` |""", "probe items")
F.sub("""- **Roles:** the tester verifies cold, as `probe.verifier` says; the researcher designs an experiment; the executor
  runs it; a scorer or a blind judge decides it.
- **Instruction:** the probe and tester-return schemas, each verdict set closed; the policies: `probe.points`,
  `probe.raise`, `probe.observations`, `probe.experiment.authority`, `probe.verifier` and `flow.route-backs`.""",
      """- **Roles:** the tester verifies cold; the researcher designs an experiment; the executor runs it; a scorer or a
  blind judge decides it. Who verifies is a structural choice, NP-5, since one actor acts per item (`[rules]`).
- **Instruction:** the probe and tester-return schemas, each verdict set closed; the policies: `probe.points`,
  `probe.raise`, `probe.observations`, `probe.experiment.authority` and `flow.route-backs`.""", "probe roles")
# 2. The observation entry.place routes on.
F.sub("returns the disposition from the closed set (continue, amend, new, patch, repeat, ask, none), with its reason and "
      "evidence",
      "returns the disposition from the closed set (continue, amend, new, patch, repeat, ask, none), with its reason and "
      "evidence, and names each observation the request claims", "place return")
# 3. verify-at-plan's route.
F.sub("| `plan.input` | command | — | pins the intake record, or the selected ask, filing or proposal | its SHA | "
      "`plan.dedupe` | dRankedPlan |",
      "| `plan.input` | command | — | pins the intake record, or the selected ask, filing or proposal | its SHA | "
      "`plan.dedupe`; an observation the request claims, under `probe.observations: verify-at-plan` → `probe.trigger` "
      "first, then `plan.dedupe` with the probe's record | dRankedPlan |", "plan input")
# 4. A playbook run into Design.
F.sub("""**Enters** on any of six inputs:""", """**Enters** on any of seven inputs:""", "design inputs count")
F.sub("""- a fix unit, for a red whose spec is wrong or a core red the build's own commits introduced.
""", """- a fix unit, for a red whose spec is wrong or a core red the build's own commits introduced;
- a playbook run's derived plan record, its playbook pinned beside it, its slug claimed and its lease taken by
  `entry.claim` (the `repeat` disposition; night pass, point 1).
""", "design seventh input")
F.sub("finding or fix unit → `design.unit-spec` for its new unit, or `design.decompose` when it changes an interface | "
      "dIndexedDesign |",
      "finding or fix unit → `design.unit-spec` for its new unit, or `design.decompose` when it changes an interface; "
      "playbook run → `design.unit-spec`, one unit for each piece its playbook declares | dIndexedDesign |",
      "design input route")
F.save()

V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
V.sub("""| `probe.verifier` | tester, asking-role, researcher | tester | who verifies cold, night pass, pending NP-5; the default shown is the recommendation until the owner answers | dDeclaredLoop |
""", "", "verifier key")
V.sub("""| `probe.verifier` | tester | tester | tester | tester |
""", "", "verifier preset row")
V.sub("the probe program (`probe.trigger`, `probe.pin`, `probe.design`, `probe.run`, `probe.judge`, `probe.return`)",
      "the probe program (`probe.trigger`, `probe.pin`, `probe.design`, `probe.experiment`, `probe.run`, `probe.judge`, "
      "`probe.return`)", "probe items clause")
V.save()

O = Record(B + "2026-10-17-build-PLAY-dClosedLoop-1-ownership.md")
O.sub("""  - items `probe.trigger`, `probe.pin`, `probe.design`, `probe.run`, `probe.judge` and `probe.return`: dDeclaredLoop;
  - keys `attendance`, `probe.points`, `probe.raise`, `probe.observations`, `probe.experiment.authority` and
    `probe.verifier`: dDeclaredLoop;""", """  - items `probe.trigger`, `probe.pin`, `probe.design`, `probe.experiment`, `probe.run`, `probe.judge` and
    `probe.return`: dDeclaredLoop;
  - keys `attendance`, `probe.points`, `probe.raise`, `probe.observations` and `probe.experiment.authority`:
    dDeclaredLoop;""", "ownership")
O.save()

N = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md")
N.sub("| NP-5 | Who verifies a probe? | the tester, cold; the asking role; the researcher | `probe.verifier`'s default |",
      "| NP-5 | Who verifies a probe? | the tester, cold; the asking role; the researcher | a structural decision: "
      "`probe.design`'s actor, since one actor acts per item |", "NP-5")
N.save()
````

### `fold_np_residue.py`

Residue: layer-roles' driver sentence, and the owner's session named in the design text.

````python
"""The night pass's residue, found by a sweep while its closing review ran: text that still states the old model.
- layer-roles still said the main session drives, and the executor only when no one attends;
- design text in layer-runtime, the project map and the systems record still said "attended session" for the session
  the owner types in, whose binding now reads "owner" (the night pass, point 1). Dated answers and the session model
  keep their words.

Usage: python -X utf8 fold_np_residue.py   (from the worktree root); refuses unless every anchor matches exactly once.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/2026-10-1"
RO = Record(B + "5-build-PLAY-dClosedLoop-1-layer-roles.md")
RO.sub("""  The main session is the driver and never a worker. The executor drives when no one attends.""",
       """  The driver is never a worker. It is the supervisor in every mode, the owner's session its client. The owner's
  session hosts the driver only until dWellOiledMachine lands, or if its platform spike fails, under its owner
  binding, each role act it hosts act-bound with that act's epoch (the night pass, point 1, and its closing review's
  M6, which replaced "the main session is the driver; the executor drives when no one attends").""", "driver")
RO.save()

RT = Record(B + "5-build-PLAY-dClosedLoop-1-layer-runtime.md")
for old, new, label in (
    ("      In an attended session under `allowance` or `person`, it goes to the person.",
     "      In the owner's session under `allowance` or `person`, it goes to the person.", "dispatcher down"),
    ("    - Under `runtime.attended-judge: classifier-or-person`, the default (RT-4), an attended session\n"
     "      loads no ask rule,",
     "    - Under `runtime.attended-judge: classifier-or-person`, the default (RT-4), the owner's session\n"
     "      loads no ask rule,", "judge default"),
    ("    baseline. An attended session under the default fails closed where the CLI carries",
     "    baseline. The owner's session under the default fails closed where the CLI carries", "fails closed"),
    ("    records an exception included, and puts it to the person when attended.",
     "    records an exception included, and puts it to the person in the owner's session.", "exception"),
    ("  - Attended sessions enter it only to land.", "  - The owner's session enters it only to land.", "primary tree"),
    ("  - Attended sessions also get the card.", "  - The owner's session also gets the card.", "card"),
    ("settled by RT-1. An attended session starts fresh at an item\n    boundary by default.",
     "settled by RT-1. The owner's session starts fresh at an item\n    boundary by default.", "fresh"),
    ("  - attended sessions follow `context.on-full`,", "  - the owner's session follows `context.on-full`,", "context"),
    ("  - under `runtime.attended-judge: classifier-or-person`, an attended session loads no ask rule. A",
     "  - under `runtime.attended-judge: classifier-or-person`, the owner's session loads no ask rule. A",
     "judge test"),
):
    RT.sub(old, new, label)
RT.sub("""  "owner", since attendance is a mode and not a kind of session.""",
       """  "owner", since attendance is a mode and not a kind of session. Its design text says "the owner's session" for what
  it called an attended session; `runtime.attended-judge` and `runtime.attended-allowance` keep their names until the
  lexicon settles the term (gap-lex-09).""", "revised note")
RT.save()

PM = Record(B + "7-build-PLAY-dClosedLoop-1-project-map.md")
PM.sub("| `memory.default-load` | card, card-and-live, card-and-map | card-and-map (PM-7), read by an attended session; an act "
       "session loads its work order |",
       "| `memory.default-load` | card, card-and-live, card-and-map | card-and-map (PM-7), read by the owner's session at "
       "startup, resume and a compaction (night pass, point 5); an act session loads its work order |", "keys row")
PM.save()

SY = Record(B + "6-build-PLAY-dClosedLoop-1-systems.md")
SY.sub("  - **An attended session also opens with the map** (PM-7,",
       "  - **The owner's session also opens with the map,** and gets it back at a resume and a compaction (PM-7; the night "
       "pass, point 5;", "opens with the map")
SY.sub("| `memory.default-load` | card, card-and-live, card-and-map | card-and-map for attended sessions (PM-7) |",
       "| `memory.default-load` | card, card-and-live, card-and-map | card-and-map for the owner's session (PM-7) |",
       "keys row")
SY.save()
````

### `fold_review_np.py`

The closing review's fold into the design records.

````python
"""Fold the night pass's closing review (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md`) into the
design records. Run after fold_np_self.py and fold_np_residue.py; the map's fixes are fix_map_review.py's, and the
order's gate is the committed `build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py`.

Usage: python -X utf8 fold_review_np.py   (from the worktree root); refuses unless every anchor matches exactly once.
"""
import collections
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
REV = "`reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md`"

# ---------------------------------------------------------------- flow-steps
F = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
patch_row = ("| none | a placement disposition `patch`, from any of the three, its slug claimed and its lease taken by "
             "`entry.claim` | designing | the patch's derived plan record, the claim ref and the lease record |\n")
F.sub(patch_row, patch_row + "| none | a placement disposition `repeat`, from any of the three, its slug claimed and its "
      "lease taken by `entry.claim` | designing | the playbook's record, the run's derived plan record, the claim ref and "
      "the lease record (the night pass's closing review, H1) |\n", "H1 transition row")
F.sub("""- **The driver knows a probe is owed,** because `next` returns the probe's items as the frontier while the asker
  waits (P22).
""", """- **The driver knows a probe is owed,** because `next` returns the probe's items as the frontier while the asker
  waits (P22).
- **Its verdicts are closed.** A verification or a reproduction is confirmed, refuted, inconclusive or unrunnable, and
  an experiment is measured, within noise, aborted or unrunnable. A claimed or an unrunnable verdict goes to an owner
  item (the closing review's M3).
- **When an observation is verified,** as `probe.observations` says: before `entry.place` places the request; at
  `plan.input` under `verify-at-plan`, though a patch or a repeat build, which never reaches Plan, is verified before
  placement under that value too; and under `on-request` only when the owner asks, through the owner's request (M9).
""", "M3 M9 probe intro")
F.sub("| the asking item's re-entry, or the boundary's next item; a claimed verdict → an owner item, resolved as "
      "`[breakpoint]`'s owner gate is | dDeclaredLoop |",
      "| the asking item's re-entry, or the boundary's next item; a claimed or an unrunnable verdict → an owner item, "
      "resolved as `[breakpoint]`'s owner gate is | dDeclaredLoop |", "M3 return route")
F.sub("""- **Runtime:** the harness adapter's browser capability and the visual capture adapter, dWellOiledMachine's; act
  binding for an experiment's acts.
""", """- **Runtime:** the harness adapter's browser capability and the visual capture adapter, dWellOiledMachine's; act
  binding for an experiment's acts.
- **Before the builds it rests on land** (the closing review's H2 and M2). dDeclaredLoop builds the program ahead of
  them, so each later part has a stand-in until its build lands:
  - dBoundRoles' tester and `experiment` shape: `probe.design` and `probe.experiment` route to an owner item;
  - dBoundRoles' `probe` outcome on the role templates: probes are placed, never raised;
  - dTotalRecall's `record` command: `probe.return` writes the probe record into the build folder, keyed as its kind
    declares;
  - dWellOiledMachine's visual capture adapter: a visual verification is unrunnable.

  The executor's re-run is dDeclaredLoop's own, its witnesses computed rather than typed, and the scorer factory is
  dFairHearing's, an ancestor, so a probe is judged from the start.
""", "H2 M2 stand-ins")
F.sub("""  and its gate script. Changing them takes the tester's `test.attribute` judgment that the spec is wrong, which
  routes to Design as a new unit (P19).""", """  and its gate script. Changing them takes the tester's `test.attribute` judgment that the spec is wrong, which
  routes to Design as a new unit (P19). Its arm is seen red on a planted fix pass that writes the red leg's test file,
  and a fix pass after a failed `build.acceptance` leaves the acceptance commands' own files alone too (M16).""",
      "M16 fix pass")
F.sub("attend or unattend → the `override` record, scoped by `attendance.scope`,",
      "attend or unattend → the `attendance override` record, scoped by `attendance.scope`,", "M13 life.request")
F.save()

# ---------------------------------------------------------------- v2
V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
V.sub("""Revised: 2026-10-17, after the folds' closing review""", f"""Revised: 2026-10-18, after the night pass's closing review ({REV}), CLEAN WITH FIXES, 26 items, 3 high:
- `repeat` gains its transition row and its Design entry (H1), and the order's gate now checks both (H1);
- each new dependency on a later build gets a stand-in, a class row or a move: the playbook set check moves to
  dIndexedDesign, the probe's re-run joins dDeclaredLoop's computed witnesses, and the probe program declares its
  stand-ins (H2, M1, M2);
- the owner's session hosts the driver under its owner binding, each role act it hosts act-bound, one statement
  everywhere (M6); attendance writes its own record kind, the attendance override (M13);
- the map's fates arms fail hard on an absent record and are counted, and the order's gate is one committed script
  (H3, M7, M8, M14, M15);
- the other items are folded row by row in the night-pass record's `[review-fold]`.

Revised: 2026-10-17, after the folds' closing review""", "revision note")
V.sub("""complex features enter at Plan, in-goal amendments and patch
  builds at Design.""", """complex features enter at Plan, in-goal amendments, patch
  builds and playbook runs (`repeat`) at Design.""", "H1 P20")
V.sub("review as breakpoints, with the verdict engine and the lander |",
      "review as breakpoints and testing as probes at any boundary, with the verdict engine and the lander |", "flow row")
V.sub("Its optional components, the map, recall and the lexicon, are what agents consult to decide",
      "Its optional components, the map's owner views and dossiers, recall and the lexicon, are what agents consult to "
      "decide; the map's code depth is core since the night pass (point 3)", "M12 memory row")
CL = [
    ("the attendance rule: `attendance` places owner breakpoints, turns the `step —` announcement on and has owner "
     "questions asked live, and never selects an item's actor, the driver or a binding, its arm seen red on a planted "
     "value that swaps an actor (night pass, point 1)",
     "the attendance rule: `attendance` places owner breakpoints and has owner questions asked live, and never selects "
     "an item's actor, the driver or a binding, its arm seen red on a planted value that swaps an actor, the `step —` "
     "announcement joining when dWellOiledMachine lands it (night pass, point 1)"),
    ("the `repeat` disposition in the placement set, routing a request onto a playbook (night pass, point 1)",
     "the `repeat` disposition in the placement set and its `none` row in the transition table, routing a request "
     "onto a `playbook`, filed as an ask until dIndexedDesign lands that record kind (night pass, point 1)"),
    ("its record handed to the asking item, an entry-time probe keyed by content as triage is (night pass, point 2)",
     "its record handed to the asking item, an entry-time probe keyed by content as triage is, and a stand-in for each "
     "later part it rests on, as flow-steps' `[probe]` declares (night pass, point 2)"),
    ("witnesses computed rather than typed by the acting agent (acceptance re-run by the executor, red attribution "
     "joined to the verdict)",
     "witnesses computed rather than typed by the acting agent (acceptance re-run by the executor, a probe's commands "
     "re-run at its pinned SHA, red attribution joined to the verdict)"),
    ("; the probe witness: the executor re-running a probe's declared commands at its pinned SHA, a figure an agent "
     "judged kept as claimed (night pass, point 2)", ""),
    ("; the playbook set record and its set check at Test (night pass, point 1)", ""),
    ("a change to them routed through the tester's wrong-spec judgment to Design as a new unit (night pass, point 6)",
     "a change to them routed through the tester's wrong-spec judgment to Design as a new unit, its arm seen red on a "
     "planted fix pass that writes the red leg's test file, and a fix pass after a failed acceptance leaving the "
     "acceptance commands' own files alone (night pass, point 6)"),
    ("the research harness, built on the `experiment` shape (night pass, point 2)",
     "the research harness, built on the `experiment` shape once dBoundRoles registers it, and run as today until then "
     "(night pass, point 2)"),
    ("amendment by proposal, and `check-playbook` as Design's pack (night pass, point 1)",
     "amendment by proposal, and `check-playbook` as Design's pack (night pass, point 1); the playbook set record and "
     "its set check, registered at Test's leg-pack point (night pass, point 1)"),
    ("and attend and unattend, each writing an `override` record scoped by `attendance.scope` (night pass, point 1)",
     "and attend and unattend, each writing an `attendance override` record scoped by `attendance.scope` (night pass, "
     "point 1)"),
    ("the supervisor the only driver in every mode, the owner's session its client, and before this build lands the "
     "owner's session hosting the same driver program under the same act binding (night pass, point 1)",
     "the supervisor the only driver in every mode, the owner's session its client, which hosts the driver only before "
     "this build lands or if its platform spike fails, under its owner binding, each role act it hosts act-bound with "
     "that act's epoch (night pass, point 1)"),
]
for old, new in CL:
    if "; " in new or "|" in new:
        if not old.startswith("amendment by proposal"):
            sys.exit(f"a clause holds a separator: {new[:60]}")
    V.sub(old, new, old[:40])
V.sub("""    act session, the owner's session keeps hosting the driver, bound as an act session (point 1, NP-1);""",
      """    act session, the owner's session keeps hosting the driver under its owner binding, each role act it hosts
    act-bound with that act's epoch (point 1, NP-1);""", "M6 owed")
V.sub("an attended session opens with the card and the map, and an act session loads its work order",
      "the owner's session opens with the card and the map, and an act session loads its work order", "M11 default-load")
V.sub("the working roles are the spec writer, builder, researcher, architect and reviewer, and the prompt writer through "
      "its actor", "the working roles are the spec writer, builder, tester, researcher, architect and reviewer, and the "
      "prompt writer through its actor", "M5 code-roles")
V.save()

# ---------------------------------------------------------------- layer-runtime (M6, L5)
R = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md")
R.sub(""" attended or not: the supervisor drives, and the owner's session is its client; until dWellOiledMachine
 lands, the owner's session hosts the same driver, bound the same way (night pass, point 1)""",
      """ attended or not: the supervisor drives, and the owner's session is its client; it hosts the driver only
 until dWellOiledMachine lands, or if its spike fails, each role act it hosts act-bound (night pass, point 1)""",
      "M6 diagram")
R.sub("Until dWellOiledMachine lands, the owner's session hosts the same driver program, bound as an act session. No "
      "model session drives. |",
      "The owner's session hosts the driver only until dWellOiledMachine lands, or if its platform spike fails (v2 "
      "`[owed]`), under its owner binding, each role act it hosts act-bound with that act's epoch. No model session "
      "drives. |", "M6 terms")
R.sub("""The act session, or the owner's session while it
  hosts the driver, bound the same way, makes exactly one call (night pass, point 1):""",
      """The act session, or the owner's session while it
  hosts the driver, its role act act-bound with that act's epoch, makes exactly one call (night pass, point 1):""",
      "M6 act call")
R.sub("""The owner's session is bound the same way for every role act it hosts. Outside role
    acts it reads and orients,""", """Each role act the owner's session hosts is act-bound with that act's epoch, under the
    session's owner binding. Outside role acts it reads and orients,""", "M6 act freedom")
R.sub("""    - The orientation scout's spawn at session start is a bound act of the attended binding.""",
      """    - The orientation scout's spawn at session start is a bound act of the owner binding.""", "L5")
R.sub("""- the diagram, `[decide]`'s `run <build>` and its clients: the owner's session hosts the driver only until
  dWellOiledMachine lands, bound as an act session, and `/unattended` retires with the kit;""",
      """- the diagram, `[decide]`'s `run <build>` and its clients: the owner's session hosts the driver only until
  dWellOiledMachine lands, or if its platform spike fails, under its owner binding, each role act it hosts act-bound
  with that act's epoch (the closing review's M6), and `/unattended` retires with the kit;""", "M6 revised")
R.save()

# ---------------------------------------------------------------- layer-memory (H2 move, M13, M12)
M = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md")
M.sub("""The night pass adds the `code` record, the `probe` record, and
  the playbook and playbook set kinds (points 1 to 3).""", """The night pass adds the `code` record, the `probe` record, the
  playbook and playbook set kinds, and the attendance override (points 1 to 3).""", "core kinds")
M.sub("| playbook set | dWitnessedBar | its writer is the set check at Test: a playbook run's pieces joined by hash, and "
      "the set's identity derived from them (night pass, point 1) |",
      "| playbook set | dIndexedDesign | its writer is the set check, which dIndexedDesign registers at Test's leg-pack "
      "point: a playbook run's pieces joined by hash, and the set's identity derived from them (night pass, point 1, "
      "moved by its closing review's H2) |", "playbook set owner")
ov = next(l for l in M.text.split("\n") if l.startswith("| override | dOrderedCharter |"))
M.sub(ov + "\n", ov + "\n| attendance override | dWellOiledMachine | its writer is `life.request`'s attend and unattend: "
      "the attendance value and its scope, which `attendance.scope` reads (the night pass's closing review, M13) |\n",
      "attendance override kind")
M.sub("""  - the map's symbols and callers;""", """  - the core `code` record's definitions and callers (night pass, point 3);""",
      "M12 reuse index")
M.sub("""Without the map,
  an optional component since KN-1, the index holds the reuse entries alone, and the slot says so.""",
      """Without the map's
  optional parts, the index still reads the core `code` record, and the slot names the parts absent (night pass,
  point 3).""", "M12 reuse absent")
M.save()

# ---------------------------------------------------------------- ownership
O = Record(B + "2026-10-17-build-PLAY-dClosedLoop-1-ownership.md")
O.sub("""    dIndexedDesign; `playbook set`: dWitnessedBar.""", """    dIndexedDesign; `playbook set`: dIndexedDesign, which registers its set check at Test's leg-pack point (the
    closing review's H2); `attendance override`: dWellOiledMachine (M13).""", "ownership kinds")
O.save()

# ---------------------------------------------------------------- project map (L1, L2, M5)
P = Record(B + "2026-10-17-build-PLAY-dClosedLoop-1-project-map.md")
P.sub("""and since the night pass the builder and
the tester get their write set's `code` slot (point 3).""", """and since the night pass the builder and the tester get their write set's `code` slot (point 3).""", "L1 join")
P.sub("| the map, with `design.inventory`'s unfolds |",
      "| the map, with `design.inventory`'s unfolds, and the `code` slot of its scope paths (night pass, point 3) |",
      "M5 architect")
P.sub("| the spec writer, at `design.unit-spec` and `review.fold` | the map |",
      "| the spec writer, at `design.unit-spec` and `review.fold` | the map, and the `code` slot of its unit's write set "
      "(night pass, point 3) |", "M5 spec writer")
P.sub("| the reviewer, at `review.lens` under the coherence and reuse lenses | the map |",
      "| the reviewer, at `review.lens` under the coherence and reuse lenses | the map, and the `code` slot of the "
      "pinned range (night pass, point 3) |", "M5 reviewer")
P.sub("""  The slot renders filled, derived with nothing related, or not extracted for a language, with `gov code where`
  named as the fallback.""", """  The slot renders filled, derived with nothing related, not extracted for a language, with `gov code where`
  named as the fallback, or not installed, until dTotalRecall's `code` record lands (the closing review's L2).""",
      "L2 states")
P.save()

# ---------------------------------------------------------------- layer-instruction (L4)
I = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md")
I.sub("| branch-reconcile and the cleanup Skill | Runtime: isolation housekeeping | expansion |",
      "| branch-reconcile and the cleanup Skill | Observability: the prune fix, its isolation housekeeping read as a "
      "reading (the fates record's `[stale]` 9) | expansion |", "L4 branch-reconcile")
I.save()

# ---------------------------------------------------------------- the re-cut (M7, H2)
C = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-recut.md")
C.sub("""tolerance, homonym, not a use and moved. That probe is the order's gate
(`build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md` `[instrument]`).""",
      """tolerance, homonym, not a use and moved. That probe is the order's gate, kept as one committed script,
`build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py`, which also checks each routed disposition's transition row (the
night pass's closing review, M7 and H1). Its copies in the audit fold's `[review-instrument]` and the night pass's
instruments record are snapshots.""", "M7 gate")
anchor = "| dTotalRecall | `roster` | dIndexedDesign | homonym |"
i = C.text.index(anchor)
if C.text.count(anchor) != 1:
    sys.exit("roster anchor")
C.text = C.text[:i] + ("| dDeclaredLoop | `playbook` | dIndexedDesign | tolerance | the `repeat` disposition files an ask "
                       "until dIndexedDesign lands the playbook record kind (the night pass's closing review, H2) |\n") + C.text[i:]
C.done += 1
C.save()

# ---------------------------------------------------------------- the audit fold's probe copy (M7)
A = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md")
A.sub("""## [review-instrument] The reconciliation probe, hardened
""", """## [review-instrument] The reconciliation probe, hardened

A snapshot: the order's gate is now one committed script, `build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py`
(the night pass's closing review, M7).
""", "M7 snapshot note")
A.save()

# ---------------------------------------------------------------- the fates record (M4, L3, L4)
T = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-fates.md")
T.sub("| roles | `house/policy.toml` | effort and gates | STAYS | until dConvergedCharter folds it; on dGroundRules's "
      "legacy list until then |",
      "| roles | `house/policy.toml` | effort and gates | MERGED | into `.governance/policy.toml` (dConvergedCharter); on "
      "dGroundRules's legacy list until then |", "M4 house policy")
T.sub("| unattended | `stall-recorder.js` | API-stall record | STAYS | the supervisor's limit signal (dWellOiledMachine) |",
      "| unattended | `stall-recorder.js` | API-stall record | RESHAPED | the supervisor's limit signal, in the runtime's "
      "own kit (dWellOiledMachine) |", "L3 stall-recorder")
T.sub("the set check (dWitnessedBar), a cyclic playbook's filer", "the set check, registered at Test (dIndexedDesign), a "
      "cyclic playbook's filer", "H2 set check")
T.sub("| expansion; its layer is disputed (section 5) (dTendedCadence, observability's prune fix) |",
      "| observability's prune fix (dTendedCadence; `[stale]` 9) |", "L4 branch-reconcile")
T.sub("| `tag` and `purpose` fields (dWitnessedBar); JSON-or-packs UNDECIDED | v2 `[chain]` dWitnessedBar |",
      "| `tag` and `purpose` fields, and one manifest whose rows the leg factory generates from the packs' declarations "
      "(dWitnessedBar) | v2 `[chain]` dWitnessedBar; proposed by the night pass (NP-22) |", "L4 gate-legs")
T.sub("| the shared function is undecided (dTendedCadence, whose dead-pointer detector shares its function) | "
      "layer-memory `[tools]` |",
      "| its dangling-path function shared with Maintain's dead-pointer detector (dTendedCadence) | layer-memory `[tools]`; "
      "proposed by the night pass (NP-22) |", "L4 dead-paths")
T.sub("| skills | rendered Skills (7) | entries | RESHAPED | thin level-4 entries; build and unattended become clients of "
      "`next` and `run` (dConvergedCharter, with dWellOiledMachine for the clients) |",
      "| skills | rendered Skills, six of seven, `/unattended` apart | entries | RESHAPED | thin level-4 entries; `/build` "
      "becomes a client of `next` and `run` (dConvergedCharter, with dWellOiledMachine for the client) |", "M4 Skills")
rows = [l for l in T.text.split("## [table]", 1)[1].split("\n## ", 1)[0].split("\n") if l.startswith("| ") and
        not l.startswith("| Kit") and not l.startswith("|---")]
fate = collections.Counter(l.split(" | ")[3].strip() for l in rows)
proposed = sum("proposed by the night pass (NP-22)" in l for l in rows)
old_counts = re.search(r"Counts: \d+ stay,\s+\d+ reshaped, \d+ merged and \d+ retired, over \d+ rows\.", T.text)
T.sub(old_counts.group(0), f"Counts: {fate['STAYS']} stay,\n{fate['RESHAPED']} reshaped, {fate['MERGED']} merged and "
      f"{fate['RETIRED']} retired, over {len(rows)} rows.", "counts")
T.sub("""- every STAYS, RESHAPED or MERGED row names a chain build in "Where it goes";
- every RETIRED row names its replacement, or says "none" and why.

Each arm is seen red on a planted case (`night-pass` `[instrument]`). What the check does not do: it does not prove
that a row's fate is right, only that every part has one, in the closed set, landing in a build that exists. Whether
each lands is dConvergedCharter's exit check (v2's `[chain]`).""",
      """- every STAYS, RESHAPED or MERGED row names a chain build in "Where it goes";
- every RETIRED row's "Where it goes" names something other than a bare "none";
- no STAYS part sits in a kit whose fate is absorbed or retired;
- the rows match the counts this record states, fate by fate;
- each kit node's `fate` equals its `[kits]` row.

The record is read by name, so a renamed or missing record stops the check, and a row of the wrong width stops it too
(the night pass's closing review, H3, M8 and M14). Each arm is seen red on a planted case (`night-pass`
`[instrument]`). What the check does not do:
- it does not prove that a row's fate is right, only that every part has one, in the closed set, landing in a build
  that exists;
- it does not judge a RETIRED row's replacement or reason, only that one is named;
- it does not catch one part named in two rows under different kits;
- whether each part reaches its fate is dConvergedCharter's exit check (v2's `[chain]`).""", "L3 check")
T.save()
print(f"fates: {dict(fate)} over {len(rows)} rows, {proposed} proposed")
````

### `fix_map_review.py`

The closing review's fold into the map's generator.

````python
"""Fold the night pass's closing review into the design map's generator (H3, M8, M14, M15, L3, L6, L7):
- the fates record is resolved by name through the atlas's lookup, which exits when none or two carry it, so a rename,
  a re-date or a move fails hard instead of switching every fates arm off (H3, M8), and `--plant fates-absent` sees it;
- its two tables parse through the atlas's table reader, which stops on a row of the wrong width (M14), and the rows
  are counted against the counts the record states;
- plants reach every fates arm (M15), a kit node's `fate` rel is checked against `[kits]`, and a STAYS part under an
  absorbed or retired kit, and a RETIRED row that names nothing or a bare "none", red (L3);
- the layer arm reads the derived kit nodes, not rendered lines, and its plant empties a node's rel (L6);
- the printed size leaves out the head line's dirty marker, so a recorded figure reproduces on any tree (L7).

Usage: python -X utf8 fix_map_review.py   (from the worktree root)
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


sub('''FATES = HERE / "2026-10-18-build-PLAY-dClosedLoop-1-fates.md"
FATE_KITS, FATE_ROWS = {}, []
''', '''# Resolved by name through the atlas's record lookup, which exits when no record or two carry it (the closing review's
# H3 and M8): a renamed, re-dated or moved record fails hard, never switching the fates arms off.
FATES = "fates"
FATE_KITS, FATE_ROWS, FATE_COUNTS = {}, [], []
''', "globals")

sub(r'''    if FATES.exists():
        body = FATES.read_text(encoding="utf-8")
        for tag, width, sink in (("kits", 3, "kits"), ("table", 6, "rows")):
            _, block = section(body, tag)
            for ln in block.split("\n"):
                c = atlas.cells(ln) if ln.startswith("| ") else []
                if len(c) == width and c[0] != "Kit" and not set(c[0]) <= set("-"):
                    if sink == "kits":
                        FATE_KITS[c[0]] = c[1]
                    else:
                        FATE_ROWS.append(c)
        for n in kits:
            if n["key"] in FATE_KITS:
                n["rels"].append(("fate", [FATE_KITS[n["key"]]]))
''', r'''    # The fates record's two tables, read through the atlas's table reader, which stops the run on a row of the wrong
    # width (M14), and the counts its [table] lead-in states, which the count arm compares with the rows.
    body = atlas.record(FATES).read_text(encoding="utf-8")
    _, kits_block = section(body, "kits")
    FATE_KITS.update({c[0]: c[1] for c in atlas.table(kits_block, "Kit", "fates [kits]")})
    _, rows_block = section(body, "table")
    FATE_ROWS.extend(atlas.table(rows_block, "Kit", "fates [table]"))
    stated = re.search(r"Counts: (\d+) stay,\s+(\d+) reshaped,\s+(\d+) merged and (\d+) retired, over (\d+) rows", rows_block)
    FATE_COUNTS.extend(int(x) for x in stated.groups()) if stated else None
    for n in kits:
        if n["key"] in FATE_KITS:
            n["rels"].append(("fate", [FATE_KITS[n["key"]]]))
''', "derive")

sub('''    elif plant == "no-layer":
        i = next(i for i, ln in enumerate(lines) if ln.startswith("- kit.") and " layer=" in ln)
        lines[i] = re.sub(r" · layer=\\S+", "", lines[i])
''', '''''', "old no-layer plant")

sub(r'''    # Fates: every kit has a declared fate and rows, every row a known kit, a fate in its set and a destination.
    if FATE_KITS or FATE_ROWS:
        rows_, kits_ = [list(r) for r in FATE_ROWS], dict(FATE_KITS)
''', r'''    # Fates: every kit has a declared fate and rows, every row a known kit, a fate in its set and a destination, the
    # rows match the counts the record states, and no STAYS part sits in a kit that goes. The record is read hard in
    # derive(), so an absent one never reaches here (H3).
    if True:
        rows_, kits_ = [list(r) for r in FATE_ROWS], dict(FATE_KITS)
        fate_rel = {n["key"]: next((v[0] for k, v in n["rels"] if k == "fate"), None) for n in ns["kit"]}
''', "fates head")

sub('''        elif plant == "fates-kit":
            kits_[next(iter(kits_))] = "maybe"
''', '''        elif plant == "fates-kit":
            kits_[next(iter(kits_))] = "maybe"
        elif plant == "fates-kit-drop":
            kits_.pop(next(iter(kits_)))
        elif plant == "fates-kit-ghost":
            kits_["ghostkit"] = "kept"
        elif plant == "fates-count":
            rows_[next(i for i, r in enumerate(rows_) if r[3] == "STAYS")][3] = "RESHAPED"
        elif plant == "fates-absorbed-stays":
            k = next(k for k, f in kits_.items() if f == "absorbed")
            rows_[next(i for i, r in enumerate(rows_) if r[0] == k)][3] = "STAYS"
        elif plant == "fates-bare-none":
            rows_[next(i for i, r in enumerate(rows_) if r[3] == "RETIRED")][4] = "none"
        elif plant == "fates-rel":
            k = next(iter(fate_rel))
            fate_rel[k] = "retired" if fate_rel[k] != "retired" else "kept"
        if not rows_ or not kits_:
            findings.append("fates: the record's [kits] or [table] holds no row")
''', "plants")

sub('''            elif r[3] == "RETIRED" and not r[4].strip():
                findings.append(f"fates: {r[0]} · {r[1]} retires with no replacement named")
''', '''            elif r[3] == "RETIRED" and r[4].strip().rstrip(".").lower() in ("", "none"):
                findings.append(f"fates: {r[0]} · {r[1]} retires naming neither a replacement nor a reason")
            if r[3] == "STAYS" and kits_.get(r[0]) in ("absorbed", "retired"):
                findings.append(f"fates: {r[0]} · {r[1]} stays, yet its kit is {kits_[r[0]]}")
        counted = [sum(r[3] == f for r in rows_) for f in ("STAYS", "RESHAPED", "MERGED", "RETIRED")] + [len(rows_)]
        if counted != FATE_COUNTS:
            findings.append(f"fates: the rows count {counted}, and the record states {FATE_COUNTS or 'no counts'}")
        for k, f in sorted(fate_rel.items()):
            if f != kits_.get(k):
                findings.append(f"fates: kit.{k} carries fate={f}, and [kits] says {kits_.get(k)}")
''', "arms")

sub('''    # Layer: every kit line joins a layer, unless its kits-table row says "no layer" (dispatch 104 found all 19 empty).
    for ln in lines[2:]:
        m = LINE.match(ln)
        if m and m.group(1) == "kit" and m.group(2) not in NO_LAYER and " layer=" not in ln:
            findings.append(f"layer: kit.{m.group(2)} joins no layer")
''', '''    # Layer: every kit node joins a layer, unless its kits-table row says "no layer" (dispatch 104 found all 19 empty).
    # It reads the derived nodes, so a folded kit namespace still checks (the closing review's L6), and it does not
    # check that the layer is the right one.
    kit_nodes = [dict(n, rels=list(n["rels"])) for n in ns["kit"]]
    if plant == "no-layer":
        i = next(i for i, n in enumerate(kit_nodes) if any(k == "layer" and v for k, v in n["rels"]))
        kit_nodes[i]["rels"] = [r for r in kit_nodes[i]["rels"] if r[0] != "layer"]
    for n in kit_nodes:
        if n["key"] not in NO_LAYER and not any(k == "layer" and v for k, v in n["rels"]):
            findings.append(f"layer: kit.{n['key']} joins no layer")
''', "layer arm")

sub('''    out, folded, unarmed, steps = fit(ns, unfold)
    plant = argv[argv.index("--plant") + 1] if "--plant" in argv else None
''', '''    out, folded, unarmed, steps = fit(ns, unfold)
    plant = argv[argv.index("--plant") + 1] if "--plant" in argv else None
''', "plant read (unchanged anchor)")

sub('''def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
''', '''def main(argv):
    global FATES
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if "--plant" in argv and argv[argv.index("--plant") + 1] == "fates-absent":
        FATES = "fates-absent-plant"   # no record carries this name, so derive() must exit non-zero
''', "fates-absent plant")

sub('''    size = len(out.encode("utf-8"))
''', '''    # The printed size leaves out the head line's dirty marker, so a recorded figure reproduces on a clean tree (L7).
    size = len(re.sub(r"^(map \\S+) dirty", r"\\1", out, count=1).encode("utf-8"))
''', "size")

sub('''      cases: drop-line, bad-count, ghost-rel, no-layer, fates-drop, fates-ghost, fates-bad, fates-unbuilt,
      fates-empty, fates-kit, census,''', '''      cases: drop-line, bad-count, ghost-rel, no-layer, fates-absent, fates-drop, fates-ghost, fates-bad, fates-unbuilt,
      fates-empty, fates-kit, fates-kit-drop, fates-kit-ghost, fates-count, fates-absorbed-stays, fates-bare-none,
      fates-rel, census,''', "usage")
P.write_text(t, encoding="utf-8", newline="\n")
print("map.py: the closing review's fixes")
````

### `fold_np_record_review.py`

The night-pass record brought in line with the review's fold.

````python
"""Bring the night-pass record in line with its closing review's fold: the points' text, the chain's impact recomputed,
the review's items and where each is fixed, and the instruments' numbers.

Usage: python -X utf8 fold_np_record_review.py <v2-before-the-night.md>   (from the worktree root)
"""
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

S = pathlib.Path(__file__).resolve().parent.parent
B = "memory/builds/dClosedLoop/build/"
N = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md")
N.sub("""     request, which writes an `override` record scoped by `attendance.scope`.""",
      """     request, which writes an `attendance override` record scoped by `attendance.scope` (its own kind, after the
     closing review's M13).""", "p1 override")
N.sub("""   - Until dWellOiledMachine lands, the owner's session hosts the same driver program, bound as an act session
     (NP-1).""", """   - The owner's session hosts the driver only until dWellOiledMachine lands, or if its platform spike fails. It
     keeps its owner binding, and each role act it hosts is act-bound with that act's epoch (NP-1; the closing
     review's M6).""", "p1 hosting")
N.sub("the supervisor always, the owner's session its client, hosting the same driver, bound as an act session, until "
      "dWellOiledMachine lands;",
      "the supervisor always, the owner's session its client, hosting the driver under its owner binding, each role act "
      "act-bound, only until dWellOiledMachine lands or if its spike fails;", "NP-1")
N.sub("""8. **The tester agent** is defined by dBoundRoles. Every role's return template gains the `probe` outcome.""",
      """8. **The tester agent** is defined by dBoundRoles. Every role's return template gains the `probe` outcome.
9. **Stand-ins until the later builds land,** declared in `[probe]` after the closing review's H2 and M2:
   - an owner item stands in for the tester and for the experiment shape;
   - probes are placed only, never raised;
   - the probe record is a plain file;
   - a visual check is unrunnable.

   The verifier is the tester. Choosing another is a structural choice, NP-5, because flow-steps gives each item one
   actor, so the experiment has its own item, `probe.experiment`.""", "p2 stand-ins")
N.sub("""5. **Who gets it:** the spec writer, builder, researcher, architect and reviewer, and the prompt writer through its
   actor (`memory.code-roles`).""", """5. **Who gets it:** the spec writer, builder, tester, researcher, architect and reviewer, and the prompt writer
   through its actor (`memory.code-roles`).""", "p3 roles")
N.sub("the working roles: spec writer, builder, researcher, architect, reviewer, and the prompt writer through its actor;",
      "the working roles: spec writer, builder, tester, researcher, architect, reviewer, and the prompt writer through its "
      "actor;", "NP-9")
N.sub("""  - 131 parts: 28 stay, 69 are reshaped, 20 are merged and 14 retired. None is left undecided.""",
      """  - 131 parts: 26 stay, 70 are reshaped, 21 are merged and 14 retired. None is left undecided.""", "p8 counts")
N.sub("""  - It proposed a fate for each of the 11 parts no record decided (NP-22).""",
      """  - It proposed fates for 19 parts no record decided (NP-22): dispatch 104's 11 undecided rows, split into 17 parts,
    and two cells the table had left open.""", "p8 proposed")

# [chain-impact], recomputed against v2 before the night.
def units(path):
    v2 = open(path, encoding="utf-8").read()
    chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    out = {}
    for ln in chain.split("\n"):
        m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| ([^|]+) \|$", ln)
        if m:
            out[m.group(1)] = len(m.group(4).split("; "))
    return out


before, after = units(sys.argv[1]), units(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
order = ["dGroundRules", "dOrderedCharter", "dFairHearing", "dDeclaredLoop", "dWitnessedBar", "dBoundRoles",
         "dTotalRecall", "dIndexedDesign", "dRankedPlan", "dWellOiledMachine", "dScopedBuild", "dTendedCadence",
         "dMindYourWords", "dCalibratedLens", "dShippedRelease", "dConvergedCharter"]
rows = []
for b in order:
    was = before[b] - (1 if b == "dConvergedCharter" else 0)
    shown = f"{before[b]}, of which 11 meant" if b == "dConvergedCharter" else str(before[b])
    rows.append(f"| {b} | {shown} | {after[b]} | {after[b] - was} |")
cp = subprocess.run([sys.executable, "-X", "utf8", str(S / "order/critical_path.py")], capture_output=True,
                    text=True, encoding="utf-8").stdout.split("\n")[0]
path_units = re.search(r"critical path: (\d+) units", cp).group(1)
old = N.text.split("## [chain-impact] What the night pass did to the chain\n", 1)[1].split("\n## [forks]", 1)[0]
N.sub(old, f"""
| Build | Units before | Units after | Added |
|---|---|---|---|
{chr(10).join(rows)}

- **Units: {sum(before.values())} to {sum(after.values())}.** dConvergedCharter's old count held a quoted clause split
  in two, the same defect as dFairHearing's before the walk. The clause scan now reads double quotes too, and was seen
  red on it.
- **The critical path: 181 to {path_units} units.**
  - It now runs dGroundRules, dOrderedCharter, dDeclaredLoop, dWitnessedBar, dTotalRecall, dWellOiledMachine,
    dTendedCadence, dCalibratedLens and dConvergedCharter.
  - The Maintain and Review builds' additions (instruction evals, delivery metrics, a cyclic playbook's filer, a
    bundle detector) put them ahead of dShippedRelease.
- **dDeclaredLoop grows from 43 to {after['dDeclaredLoop']} units.** It holds the attendance rule, the `repeat`
  disposition, the probe program and the code seed. The walk's offer to price a split stands, and NP-24 asks it.
- **No edge changed, but not every new dependency was seen at first.** The closing review found five clauses that
  rested on a build outside their ancestry, named in plain words the order's gate cannot read (its H2). Each was then
  fixed one of three ways:
  - **a stand-in:** the probe program's stand-ins, the research harness running as today, and the announcement joining
    with dWellOiledMachine;
  - **a class row:** `repeat`'s `playbook`, a tolerance;
  - **a move:** the playbook set check to dIndexedDesign, and the probe's re-run into dDeclaredLoop's own computed
    witnesses.

  The re-cut's `[reconciled-order]` gained four class rows tonight: `feature` and `code` from dBoundRoles, `code` from
  dOrderedCharter, and `playbook` from dDeclaredLoop.
""", "chain impact")

N.sub("\n## [instrument] The checks, as run\n", """
## [review-fold] The closing review, folded

The night pass's closing review ran as dispatch 105, a light Tier-2 diff review at medium effort, with 9 agents
(`reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md`):
- **What ran:** three lenses, correctness, seams and verification, then skeptic batches and one synthesis. The security
  and intent lenses did not run.
- **What it found:** CLEAN WITH FIXES. 26 items, 0 blocker, 3 high, 16 medium and 7 low, over 30 confirmed findings of
  31.

Every item is folded.

| Item | What was wrong | Where it is fixed |
|---|---|---|
| H1 | `repeat` had no transition row and no Design entry | flow-steps `[transitions]`, `[design]`'s seventh input and `design.input`; P20; and the order's gate, now checking every routed disposition's row |
| H2 | five clauses rested on a later build, named in plain words the probe cannot read | a stand-in, a class row or a move each (`[chain-impact]`); widening the rule to plain words was measured at 47 hits over 27 kinds, mostly homonyms, so the probe prints that count as unread |
| H3, M8 | the fates arms switched off when the record was missing or re-dated | the map resolves the record by name and stops when it is absent; the `fates-absent` plant |
| M1, M2 | the research harness and the probe program rested on later builds | as H2 |
| M3 | `unrunnable` sat outside the closed verdict set | `[probe]`'s closed verdicts, with `probe.return` routing it to an owner item |
| M4 | two fate rows contradicted their destination, or each other | `house/policy.toml` MERGED; the Skills row names six, `/unattended` apart |
| M5 | two copies disagreed on who gets the `code` slot | the tester joins the working roles; the delivery table gives the slot to the architect, spec writer and reviewer |
| M6 | the hosting rule was stated two ways | one statement in layer-runtime, layer-roles, v2's row and `[owed]`, and NP-1 |
| M7 | the re-cut pointed at a superseded copy of the order's gate | the gate is one committed script, `build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py` |
| M9 | `verify-at-plan` and `on-request` had no route | `plan.input` routes the first, and `[probe]` says how each value runs |
| M10 | `probe.verifier: asking-role` had no actor for a placed probe | the key is gone: the experiment has its own item, and the verifier is a structural choice, NP-5 |
| M11 | `[sessions]` still classed sessions as attended | the owner's session there, in `[enforce]` and in v2's `memory.default-load` reason |
| M12 | memory's `[reuse]` still treated symbols and callers as optional | `[reuse]` reads the core `code` record; v2's memory row narrowed |
| M13 | attendance wrote into dOrderedCharter's `override` kind | its own kind, the attendance override, dWellOiledMachine's |
| M14 | the fates parser dropped wrong-width rows | the atlas's table reader, which stops on one (seen red), and a count arm |
| M15 | two fates arms were never seen red, and `fate=` went unchecked | plants for both, and an arm comparing each kit node's fate with `[kits]` |
| M16 | the fix-pass clause named no witness | its arm and seen-red case, and the acceptance fix pass |
| L1 | a delivery row was split across two lines | joined |
| L2 | the `code` slot's states lacked "not installed" | added |
| L3 | the RETIRED arm was overstated, and a STAYS part sat in an absorbed kit | the arm refuses a bare "none"; a STAYS-under-absorbed arm; `stall-recorder.js` RESHAPED; `[check]` matched to the arms |
| L4 | stale text in the fates record | branch-reconcile's row and layer; the two open cells proposed; the proposed count restated |
| L5 | "the attended binding" survived the rename | "the owner binding" |
| L6 | the layer arm read rendered lines | it reads the derived kit nodes |
| L7 | recorded map sizes included the dirty marker | the printed size leaves the marker out |

**Beside the review,** the night pass's own sweep ran while the review was reading, and folded four more:
- `probe.design`'s actor was chosen by a key and by the probe's kind, against flow-steps' rule of one actor per item.
  `probe.experiment` is now its own item.
- `entry.place` routed on an observation its return did not carry. Its return now names each observation.
- `verify-at-plan` had no route. `plan.input` routes it, as M9 also asked.
- layer-roles still said the main session drives, and design passages still said "attended session" for the owner's
  session.

**Left-shift.** Each class is gated where a gate fits:
- the transitions rule and its plant (H1);
- the map's fates arms and plants (H3, M8, M14, M15, L3);
- the layer arm on derived nodes (L6).

The rest are checklist lessons:
- H2 recurs `step-depends-on-a-later-build`. Its entry now says to cite a dependency backticked and to state a
  stand-in.
- A renamed term is grepped across every record before the fold commits (M6, M11, L5:
  `amendment-leaves-its-other-half-standing`).
- An instrument lives in one committed file (M7: `two-answers-to-one-question`).
- Every value of a policy key has a route (M9: `policy-value-with-no-route`).

## [instrument] The checks, as run
""", "review-fold section")
N.save()
````

### `log_np.py`

The session log: dispatches 100 to 104 and the night's event.

````python
"""Log the night pass in the session log: dispatches 100 to 104 with their derived agent lines, and the event.

Usage: python -X utf8 log_np.py <agent-lines.txt>   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

L = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
lines = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")
if lines.count("- agent — ") != 5 or lines.count("- returned — ") != 5:
    sys.exit("expected five agent and five returned lines")
P = "`prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-{}-researcher.md`"
R = "`build/2026-10-18-build-PLAY-dClosedLoop-1-research-{}.md`"
ROWS = [
    (100, 4, "The night pass's point 1: unattended as the core flow's default state, the kit's functions homed, attended "
     "as an override", "7m40s, 42.1k out: one driver, with attendance on the breakpoint seam, and playbook mode seated by "
     "`repeat`", "unattended-core"),
    (101, 5, "Point 2: testing anywhere in the flow, the driver aware, roles testing and handing results down",
     "7m41s, 42.3k out: one probe program with two ways in, four other mechanisms each losing a test",
     "testing-anywhere"),
    (102, 6, "Point 3: code depth in the core, the map shaped mechanically and enriched, orientation by role",
     "16m59s, 54.8k out: a core code record, a per-item code slot, `git grep` as the floor", "code-orientation"),
    (103, 7, "Point 4: one relational syntax across memory, pulling a tag for its regions and instructions",
     "9m30s, 50.6k out: declare at the site, derive the rest, four other mechanisms each losing a test",
     "relational-syntax"),
    (104, 8, "Point 8: today's tools, function by function, and their fates under v2",
     "11m18s, 70.3k out: 118 function rows, 11 undecided, the kit-level map stale in nine rows", "tool-fates"),
]
row99 = next(l for l in L.text.split("\n") if l.startswith("| 99 | "))
new = "\n".join(f"| {n} | gov-researcher, at the owner's medium effort | {what} | {P.format(h)} | 1799cb98 | returned, {out} | "
                f"{R.format(rec)} |" for n, h, what, out, rec in ROWS)
L.sub(row99 + "\n", row99 + "\n" + new + "\n", "dispatch rows")
L.insert_before("\n## Events\n", f"""
The night pass's researchers, dispatches 100 to 104, derived from their handoffs the same way:

```text
{lines}
```
""", "agent lines")
L.insert_before("\n## Instruments\n", """
- 2026-10-18, session 1799cb98: during the walk, after wave 1 was presented, the owner handed over eight points and
  stepped away for the night. Their words are in `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[words]`.
  The night pass, unattended:
  - dispatched five researchers, 100 to 104, one point each, and worked points 5 to 7 itself;
  - folded unattended-by-default, testing anywhere, code depth in the core, one relational syntax, the compaction
    replay and five practices from Anthropic's AI-native SDLC playbook into v2 (P4, P20 and P25 amended, P31 to P33
    added), flow-steps (a new `[probe]` program), the layer records and the ownership record;
  - wrote the fates table, 131 parts, in `build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md`;
  - fixed the atlas's fold test (point 7), the map's kit-to-layer join, the clause scan's reading of quotes and the
    reconciliation probe's reading of wildcard citations, each seen red first;
  - registered twenty-eight gaps, grew the chain from 285 units to 331 and the critical path from 181 to 213, and
    parked NP-1 to NP-24 for the owner.
""", "event")
L.done += 1
L.save()
````

### `log_review.py`

The session log: dispatch 105 and the review's fold.

````python
"""Log the night pass's closing review in the session log: dispatch 105, its derived agent lines, and the fold.

Usage: python -X utf8 log_review.py <workflow-lines.txt>   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

L = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
lines = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").strip("\n")
if lines.count("- agent — ") != 10 or lines.count("- returned — ") != 10:
    sys.exit("expected ten agent and ten returned lines")
row104 = next(l for l in L.text.split("\n") if l.startswith("| 104 | "))
L.sub(row104 + "\n", row104 + "\n" + (
    "| 105 | `tier2-review.js`, diff review, light: three `gov-diff-reviewer` lenses (correctness, seams, verification), "
    "`gov-skeptic` batches and one `gov-synthesizer`, all at the owner's medium, round 1 | The night pass's closing "
    "review: `9ab7a5c5c` over `beda01950`, twenty-two design records as specs | the args, recorded with its fold "
    "(`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md`) | 1799cb98 | returned as `wf_ce0c2168-8c2`, "
    "CLEAN WITH FIXES, 30 of 31 confirmed, 26 items, 3 high | "
    "`reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md` |\n"), "dispatch row")
L.insert_before("\n## Events\n", f"""
The night pass's closing review, dispatch 105, derived from its run the same way:

```text
{lines}
```
""", "agent lines")
L.insert_before("\n## Instruments\n", """
- 2026-10-18, session 1799cb98: the night pass's closing review, dispatch 105, returned CLEAN WITH FIXES, with 26
  items, 3 of them high, and no blocker (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md`). Every
  item is folded, with four more from the night pass's own sweep (the night-pass record's `[review-fold]`):
  - `repeat` gained its transition row and its Design entry. The order's gate, now one committed script
    (`build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py`), checks every routed disposition's row.
  - Five dependencies on a later build, named in plain words, each gained a stand-in, a class row or a move.
  - The map's fates arms now stop on an absent or malformed record, and are counted and planted, every finding seen
    red.
  - The hosting rule reads one way everywhere. Attendance writes its own record kind, and `probe.design` keeps one
    actor.
""", "event")
L.done += 1
L.save()
````

### `plants_committed.sh`

The probe's earlier plant suite, pointed at the committed copy.

````python
#!/usr/bin/env bash
# The hardened reconciliation probe, red on one plant per rule and per class-table defect, and the superseded
# citations-only probe re-run red on the committed table. Run from the worktree root.
S=C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad
RC=memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md
P=memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py
plant() {   # label, then the probe's plant arguments
  local label="$1"; shift
  echo "\$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md $*   ($label)"
  python -X utf8 "$P" $RC "$@" 2>&1 | grep -v ': tolerance$\|: homonym$\|: not a use$\|: moved$\|^chain rows\|^left out' ; echo "rc ${PIPESTATUS[0]}"
}
{
  plant "cites" --plant-drop dTotalRecall:roster
  plant "stage" --plant-edge-drop dRankedPlan:dDeclaredLoop --plant-edge-drop dRankedPlan:dTotalRecall
  plant "routes into the breakpoint, by a declared name (FM8)" --plant-item "plan.fake:plan:dOrderedCharter:an owner item"
  plant "routes into a stage, from an expansion (FH3)" --plant-edge-drop dTendedCadence:dIndexedDesign
  plant "routes keyed by owner (FL6)" --plant-item "review.extra:breakpoint:dCalibratedLens:done"
  plant "reads (FM4)" --plant-item 'plan.reader:plan:dRankedPlan:reads `runtime.journal`'
  plant "registers" --plant-edge-drop dShippedRelease:dWellOiledMachine
  plant "a blank class cell (FH2)" --plant-class "dFairHearing:review.trigger="
  plant "a class outside the set (FH2)" --plant-class "dFairHearing:review.trigger=anything"
  plant "a class row no dependency needs (FL5)" --plant-add dRankedPlan:review.trigger:dDeclaredLoop
  echo '$ python ancestor_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md   (superseded, re-run on the committed table, FM5)'
  python -X utf8 "$S/order/ancestor_probe.py" $RC 2>&1 | grep -v ': tolerance$\|: homonym$\|: not a use$\|: moved$'; echo "rc ${PIPESTATUS[0]}"
} > "$S/audit/plants-review.txt"
cat "$S/audit/plants-review.txt"
````

### `chain_clauses.py`

The owner's answers: prints a chain row's planned-units clauses, numbered, to find each clause an answer touches.

````python
"""Print chosen chain rows of architecture v2, one planned-units clause per line, numbered, with the row's other cells.

Usage: python -X utf8 chain_clauses.py <v2.md> <build> [<build> ...] [--grep <regex>]
"""
import re
import sys

args = sys.argv[1:]
pat = None
if "--grep" in args:
    i = args.index("--grep")
    pat = re.compile(args[i + 1], re.I)
    args = args[:i] + args[i + 2:]
text = open(args[0], encoding="utf-8").read()
chain = re.search(r"^## \[chain\].*?(?=^## \[)", text, flags=re.M | re.S).group(0)
for b in args[1:]:
    row = next((ln for ln in chain.split("\n") if ln.startswith(f"| {b} |")), None)
    if row is None:
        print(f"=== {b}: no row")
        continue
    cells = [c.strip() for c in row.strip().strip("|").split(" | ")]
    print(f"=== {b} · {len(cells)} cells · stage {cells[1]} · after {cells[2]}")
    # split on '; ' outside parentheses, backticks and double quotes, as the clause scan does
    out, depth, tick, quote, cur = [], 0, False, False, ""
    s = cells[3]
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "`" and not quote:
            tick = not tick
        elif ch == '"' and not tick:
            quote = not quote
        elif ch == "(" and not tick and not quote:
            depth += 1
        elif ch == ")" and not tick and not quote:
            depth -= 1
        if s.startswith("; ", i) and not (depth or tick or quote):
            out.append(cur)
            cur = ""
            i += 2
            continue
        cur += ch
        i += 1
    out.append(cur)
    for n, c in enumerate(out, 1):
        if pat is None or pat.search(c):
            print(f"{n:2}: {c[:300]}")
    print(f"   units {len(out)} · other cells: {' | '.join(x[:200] for x in cells[4:])}")
````

### `fold_answers.py`

The owner's answers to NP-1 to NP-24, folded into v2, the gap register, the fates record, the ownership record, flow-steps, the systems record and the night-pass record's summaries.

````python
"""Fold the owner's answers to NP-1..NP-24 (2026-10-18) into the design records: v2's catalogue, presets, P33 and
chain rows, the gap register's rows, the fates record, the ownership amendment, flow-steps, the systems record and
the night-pass record's summaries. The night-pass record's [answers] and [folded-answers] sections, and the register's
tally, are written by their own scripts after this one runs.

Usage: python -X utf8 fold_answers.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"


def after_line(rec, prefix, block, label):
    """Insert block after the one line starting with prefix."""
    lines = rec.text.split("\n")
    hits = [i for i, ln in enumerate(lines) if ln.startswith(prefix)]
    if len(hits) != 1:
        sys.exit(f"{rec.path.name}: {label}: {len(hits)} lines start with {prefix!r}")
    lines[hits[0] + 1:hits[0] + 1] = block.split("\n")
    rec.text = "\n".join(lines)
    rec.done += 1


# --- architecture v2 -------------------------------------------------------------------------------------------
V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
V.insert_before("\nRevised: 2026-10-17, after the folds' closing review", """
Revised: 2026-10-18, the owner's answers to the night pass's forks (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[answers]`):
- the recommendation stands for NP-1 to NP-5, NP-7, NP-11 to NP-13, NP-15 to NP-20 and NP-24, and for NP-10, asked
  again after its pros and cons;
- four defaults move: `probe.experiment.authority` to within-cap (NP-6), `memory.code-budget` to 16k with any size
  allowed (NP-8), `memory.code-roles` to every-role (NP-9) and `tags.bundle` to both (NP-14);
- `maintain.tiers` lands with bands as its default (NP-21), beside `maintain.security-review` (NP-19) and
  `install.guards` (NP-20), each with its gap and planned unit; the owner queue's depth joins the Loop Review's
  readings with no bound (NP-18), and `memory.code-languages`' ctags pack gains its unit and gap (NP-10);
- the fates record's nineteen proposed rows are decided row by row, four of them changed (NP-22), and the night
  pass's nodes and owners are approved, with the three new keys' (NP-23);
- a split of dDeclaredLoop and a lighter dCalibratedLens are priced before the walk resumes (NP-24).
""", "revision note")

V.sub("which attended value a bare attend request selects, night pass, pending NP-2; the default shown is the "
      "recommendation until the owner answers |",
      "a bare attend request selects confirm-steps, the owner's NP-2, 2026-10-18 |", "attendance")
V.sub("how long an attend or unattend request holds, night pass, pending NP-3; the default shown is the recommendation "
      "until the owner answers |",
      "how long an attend or unattend request holds, the owner's NP-3, 2026-10-18 |", "attendance.scope")
V.sub("an owner's observation in a request, night pass, pending NP-7; the default shown is the recommendation until the "
      "owner answers |",
      "an owner's observation in a request, the owner's NP-7, 2026-10-18 |", "probe.observations")
V.sub("| `probe.experiment.authority` | owner-opts-in, within-cap, free | owner-opts-in | aScoutedSeam's one re-run spent "
      "195 agents, night pass, pending NP-6; the default shown is the recommendation until the owner answers |",
      "| `probe.experiment.authority` | within-cap, owner-opts-in, free | within-cap | the owner's NP-6, 2026-10-18: "
      "\"Within the agent cap by default, opt-in as an owner switchable policy\"; aScoutedSeam's one re-run spent 195 "
      "agents |", "probe.experiment.authority")
V.sub("| `tags.bundle` | manifest, inline, both | manifest | what `gov tag bundle` returns, night pass, pending NP-14; the "
      "default shown is the recommendation until the owner answers |",
      "| `tags.bundle` | manifest, inline, both | both | what `gov tag bundle` returns: under both, the manifest, or with "
      "`--inline` the content under the byte budget the call names, the owner's NP-14, 2026-10-18 |", "tags.bundle")
V.sub("| `memory.code-budget` | 4k, 8k, 16k | 8k | the `code` slot's budget, ranges and never bodies, night pass, pending "
      "NP-8; the default shown is the recommendation until the owner answers |",
      "| `memory.code-budget` | any size, in KB per role per item, 4k, 8k and 16k among them | 16k | the `code` slot's "
      "budget, ranges and never bodies, the owner's NP-8, 2026-10-18: \"16KB default, freely adjustable by the owner by "
      "policy\" |", "memory.code-budget")
V.sub("| `memory.code-roles` | working-roles, every-role, structural-roles | working-roles | the working roles are the spec "
      "writer, builder, tester, researcher, architect and reviewer, and the prompt writer through its actor, night pass, "
      "pending NP-9; the default shown is the recommendation until the owner answers |",
      "| `memory.code-roles` | working-roles, every-role, structural-roles | every-role | the owner's NP-9, 2026-10-18; "
      "the working roles are the spec writer, builder, tester, researcher, architect and reviewer, and the prompt writer "
      "through its actor |", "memory.code-roles")
V.sub("| `memory.code-languages` | python-shell-js, file-level-only, ctags | python-shell-js | other languages at file "
      "level, `git grep` the floor, night pass, pending NP-10; the default shown is the recommendation until the owner "
      "answers |",
      "| `memory.code-languages` | builtin, builtin+ctags, ctags | builtin | Python, shell and JavaScript extracted in "
      "core with their calls, other languages at file level, `git grep` the floor; `builtin+ctags` adds the ctags pack's "
      "definitions for every other language, and `ctags` takes every language's definitions from it, the built-in "
      "extractors still giving calls; under either, a missing ctags stops the run and the record names its extractors "
      "and the ctags version; the owner's NP-10, 2026-10-18, asked again after its pros and cons |",
      "memory.code-languages")
V.sub("purposes keyed to a definition's body hash, night pass, pending NP-11; the default shown is the recommendation "
      "until the owner answers |",
      "purposes keyed to a definition's body hash, the owner's NP-11, 2026-10-18 |", "memory.code-enrich")
after_line(V, "| `install.from` | release-tag, any-commit |",
           "| `install.guards` | project, managed | project | where the core guards install: the project's settings, or "
           "managed settings where the operator opts in, never set by a preset; the owner's NP-20, 2026-10-18 (the SDLC "
           "playbook's practice 16) | dShippedRelease |", "install.guards")
after_line(V, "| `maintain.record-when` | every-period, on-finding |",
           "| `maintain.security-review` | weekly, every-landing, off | weekly | dFairHearing's security lens over the "
           "landed tree, the owner's NP-19, 2026-10-18: \"Weekly by default, owner-adjustable by policy\" (the SDLC "
           "playbook's practice 21) | dTendedCadence |\n"
           "| `maintain.tiers` | bands, pins | bands | a reading's response tiered by its deviation from its pin, to log, "
           "to diagnose read-only or to act within `maintain.fixes`, or one severity per pin as before; the owner's "
           "NP-21, 2026-10-18 (the SDLC playbook's practice 20) | dTendedCadence |", "maintain keys")
V.sub("`verdict.remote.pin`, `attendance` or `attendance.scope`:",
      "`verdict.remote.pin`, `attendance`, `attendance.scope` or `install.guards`:", "never-touch keys")
V.sub("repository's environments and its pinned workflow are facts about it; and whether the owner attends is\n"
      "  the owner's own choice (night pass, point 1).",
      "repository's environments and its pinned workflow are facts about it; whether the owner attends is\n"
      "  the owner's own choice (night pass, point 1); and where the core guards install is the operator's (NP-20).",
      "never-touch reasons")
V.sub("| `probe.experiment.authority` | within-cap | owner-opts-in | owner-opts-in | owner-opts-in |",
      "| `probe.experiment.authority` | within-cap | within-cap | owner-opts-in | within-cap |", "preset authority")
V.sub("| `tags.bundle` | manifest | manifest | manifest | manifest |",
      "| `tags.bundle` | both | both | both | both |", "preset bundle")
V.sub("| `memory.code-budget` | 8k | 8k | 16k | 8k |",
      "| `memory.code-budget` | 8k | 16k | 16k | 16k |", "preset code-budget")
V.sub("| `memory.code-roles` | working-roles | working-roles | every-role | working-roles |",
      "| `memory.code-roles` | working-roles | every-role | every-role | every-role |", "preset code-roles")
V.sub("| `memory.code-languages` | python-shell-js | python-shell-js | python-shell-js | python-shell-js |",
      "| `memory.code-languages` | builtin | builtin | builtin | builtin |", "preset code-languages")
after_line(V, "| `maintain.record-when` | on-finding |",
           "| `maintain.security-review` | weekly | weekly | every-landing | every-landing |\n"
           "| `maintain.tiers` | bands | bands | bands | bands |", "preset maintain keys")
V.sub("every member, region and instruction joined to it, as a manifest of ranges under a row budget (the owner's\n"
      "  point 4, night pass).",
      "every member, region and instruction joined to it, as a manifest of ranges under a row budget, or with its\n"
      "  content inlined, by flag (the owner's point 4, night pass, and NP-14).", "P33")
# The chain rows.
V.sub("returning a tag's members, regions and instructions as a manifest of ranges under `tags.bundle-rows`, folded past "
      "it, with its type-registered",
      "returning a tag's members, regions and instructions as a manifest of ranges under `tags.bundle-rows`, folded past "
      "it, or with their content inlined under the byte budget the call names, by flag as `tags.bundle` allows (NP-14), "
      "with its type-registered", "dOrderedCharter bundle")
V.sub(" | gap-mem-01, gap-mem-02, gap-mem-03,",
      "; the ctags extractor pack, opted into by `memory.code-languages: builtin+ctags` or `ctags`: definitions and "
      "their ranges for every language the built-in extractors do not read, the record naming its extractors and the "
      "ctags version, and a missing ctags stopping the run rather than degrading to file level (NP-10)"
      " | gap-mem-01, gap-mem-02, gap-mem-03,", "dTotalRecall ctags pack")
V.sub("gap-mem-32, gap-mem-33 |", "gap-mem-32, gap-mem-33, gap-mem-34 |", "dTotalRecall gap")
V.sub("the install and update hooks that call `adopt` and `test.seed`, attended;",
      "the install and update hooks that call `adopt` and `test.seed`, attended, and the shards-to-builds backlog "
      "migration as an update's upgrade step, run attended until no tree is left on shards (NP-22);",
      "dShippedRelease upgrade step")
V.sub("registered through dBoundRoles's layer contract | gap-deploy-01,",
      "registered through dBoundRoles's layer contract; `install.guards`: the core guards installed into the project's "
      "settings, or into managed settings where the operator opts in (NP-20) | gap-deploy-01,",
      "dShippedRelease install.guards")
V.sub("gap-deploy-13, gap-flow-08,", "gap-deploy-13, gap-deploy-14, gap-flow-08,", "dShippedRelease gap")
V.sub("a detector for the memory's dead pointers, owned by Maintain;",
      "a detector for the memory's dead pointers, owned by Maintain, absorbing `check-dead-paths.sh` and keeping its "
      "merge-bar leg at Test's leg-pack point (NP-22);", "dTendedCadence dead pointers")
V.sub("(night pass, point 4) | gap-maint-01, gap-maint-02,",
      "(night pass, point 4); the recurring security review, a cadence item running dFairHearing's security lens over "
      "the landed tree as `maintain.security-review` says, weekly by default (NP-19); readings tiered by their "
      "deviation from their pins under `maintain.tiers: bands`, to log, to diagnose read-only or to act within "
      "`maintain.fixes` (NP-21) | gap-maint-01, gap-maint-02,", "dTendedCadence clauses")
V.sub("gap-maint-11, gap-orient-10 |", "gap-maint-11, gap-maint-12, gap-maint-13, gap-orient-10 |", "dTendedCadence gaps")
V.sub("route-backs per build and scope drift (night pass, point 6) | gap-review-01,",
      "route-backs per build and scope drift (night pass, point 6), and the owner queue's depth, read with no bound "
      "(NP-18) | gap-review-01,", "dCalibratedLens owner queue")
V.sub("gap-review-14, gap-review-15 |", "gap-review-14, gap-review-15, gap-review-16 |", "dCalibratedLens gap")
V.save()

# --- the gap register ------------------------------------------------------------------------------------------
G = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
ANS = "the owner's NP-{} (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[answers]`)"
after_line(G, "| gap-mem-33 |",
           "| gap-mem-34 | Memory | LOW | A language other than Python, shell and JavaScript stays at file level: an "
           "adopter written in one gets no definitions, ranges or calls for it. | night pass `[p3-code]`; "
           + ANS.format(10) + " | — |", "gap-mem-34")
after_line(G, "| gap-deploy-13 |",
           "| gap-deploy-14 | Deploy | LOW | The core guards install only into a project's own settings, which the "
           "project can edit, and managed settings are not designed. | night pass `[p6-sdlc]`, the playbook's practice "
           "16; " + ANS.format(20) + " | — |", "gap-deploy-14")
after_line(G, "| gap-maint-11 |",
           "| gap-maint-12 | Maintain | MED | No security review recurs: the security lens runs only when a build opts "
           "into it, and nothing re-reads the landed tree for security on a period. | night pass `[p6-sdlc]`, the "
           "playbook's practice 21; " + ANS.format(19) + " | — |\n"
           "| gap-maint-13 | Maintain | LOW | A reading's breach gets one response whatever its size: nothing tiers it "
           "by how far the reading deviates, to log, to diagnose read-only or to act. | night pass `[p6-sdlc]`, the "
           "playbook's practice 20; " + ANS.format(21) + " | — |", "gap-maint-12, 13")
after_line(G, "| gap-review-15 |",
           "| gap-review-16 | Review | LOW | No reading measures the owner queue's depth, so parallel work cannot be "
           "weighed against the owner's capacity to review it. | night pass `[p6-sdlc]`, the playbook's practice 10; "
           + ANS.format(18) + " | — |", "gap-review-16")
G.save()

# --- the fates record ------------------------------------------------------------------------------------------
F = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-fates.md")
F.sub("or \"proposed by the night pass (NP-22)\" for a part no record decided. Counts: 26 stay,\n"
      "70 reshaped, 21 merged and 14 retired, over 131 rows.",
      "or \"the owner, NP-22, 2026-10-18\" for a part the night pass proposed and the owner decided row by row. "
      "Counts: 24 stay,\n70 reshaped, 23 merged and 14 retired, over 131 rows.", "lead-in")
F.sub("| RETIRED | the ask register, once the migration has run (dTotalRecall) |",
      "| RESHAPED | an update's upgrade step, run attended, retired once no tree is left on shards (dShippedRelease) |",
      "migrate_backlog")
F.sub("| STAYS | a distribution check for the optional map's install (dShippedRelease) |",
      "| MERGED | into `govkit check`, the one install check (dShippedRelease) |", "check_gate_coverage")
F.sub("| RESHAPED | the stage coverage gates and the loop kit's conformance gates (dDeclaredLoop) |",
      "| RETIRED | none: it gates the unattended kit itself, which dissolves at convergence (dConvergedCharter) |",
      "check-unattended")
F.sub("| STAYS | its dangling-path function shared with Maintain's dead-pointer detector (dTendedCadence) |",
      "| MERGED | into Maintain's dead-pointer detector, which keeps its merge-bar leg (dTendedCadence) |",
      "check-dead-paths")
n = F.text.count("proposed by the night pass (NP-22)")
if n != 19:
    sys.exit(f"fates: expected 19 proposed rows, found {n}")
F.text = F.text.replace("proposed by the night pass (NP-22)", "the owner, NP-22, 2026-10-18")
F.done += 1
F.sub("| pytest-parallel-guardrails | optional | an adopter-only Flow leg pack, as proposed (NP-22) |",
      "| pytest-parallel-guardrails | optional | an adopter-only Flow leg pack (the owner, NP-22, 2026-10-18) |",
      "pytest kit row")
F.sub("7. **The leg manifest:** proposed as one manifest whose rows the leg factory generates from the packs' "
      "declarations\n   (dWitnessedBar, NP-22),",
      "7. **The leg manifest:** decided as one manifest whose rows the leg factory generates from the packs' "
      "declarations\n   (dWitnessedBar, the owner's NP-22),", "stale 7")
F.save()

# --- the ownership record --------------------------------------------------------------------------------------
O = Record(B + "2026-10-17-build-PLAY-dClosedLoop-1-ownership.md")
O.text = O.text.rstrip("\n") + """
- **NP-23, 2026-10-18:** the owner approved the night pass's nodes and owners on review, asked as four groups
  (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[answers]`), with the keys NP-19 to NP-21 add:
  `maintain.security-review` and `maintain.tiers`: dTendedCadence; `install.guards`: dShippedRelease.
"""
O.done += 1
O.save()

# --- flow-steps and the systems record -------------------------------------------------------------------------
FS = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
FS.sub("  blind judge decides it. Who verifies is a structural choice, NP-5, since one actor acts per item (`[rules]`).",
       "  blind judge decides it. The tester verifies, as the owner chose (NP-5, 2026-10-18), since one actor acts per\n"
       "  item (`[rules]`).", "NP-5")
FS.save()
SY = Record(B + "2026-10-16-build-PLAY-dClosedLoop-1-systems.md")
SY.sub("regions and instructions as a manifest of ranges under `tags.bundle-rows`. `feature` becomes",
       "regions and instructions as a manifest of ranges under `tags.bundle-rows`, or with their content inlined, by\n"
       "flag (`tags.bundle`, NP-14). `feature` becomes", "bundle")
SY.save()

# --- the night-pass record's summaries -------------------------------------------------------------------------
N = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md")
N.sub("5. **Who gets it:** the spec writer, builder, tester, researcher, architect and reviewer, and the prompt writer\n"
      "   through its actor (`memory.code-roles`).",
      "5. **Who gets it:** every role, by the owner's NP-9. The night pass proposed the working roles: the spec writer,\n"
      "   builder, tester, researcher, architect and reviewer, and the prompt writer through its actor\n"
      "   (`memory.code-roles`).", "p3 who gets it")
N.sub("4. **`gov tag bundle <tag>`** returns one manifest.",
      "4. **`gov tag bundle <tag>`** returns one manifest, or by flag the content inlined (`tags.bundle: both`, NP-14).",
      "p4 bundle")
N.sub("  - 131 parts: 26 stay, 70 are reshaped, 21 are merged and 14 retired. None is left undecided.",
      "  - 131 parts: 24 stay, 70 are reshaped, 23 are merged and 14 retired, after the owner's row-by-row review\n"
      "    (NP-22). None is left undecided.", "p8 counts")
N.sub("The walk is not a fork: wave 1 still waits for the owner's read, and wave 2 follows it.",
      "The owner answered all twenty-four on 2026-10-18 (`[answers]`), and the design carries the answers\n"
      "(`[folded-answers]`).\n\n"
      "The walk is not a fork: wave 1 still waits for the owner's read, and wave 2 follows it.", "forks pointer")
N.save()
````

### `write_answers.py`

Writes the night-pass record's `[answers]`, verbatim, and `[folded-answers]`, the register's re-measured tally and the session log's event.

````python
"""Write the owner's answers to NP-1..NP-24 into the night-pass record ([answers], verbatim, and [folded-answers]),
the gap register's re-measured tally, and the session log's event.

Usage: python -X utf8 write_answers.py <fork_answers.md> <tally.out>   (from the worktree root)
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
answers = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n")
tally = "\n".join(ln.rstrip() for ln in pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").strip("\n").split("\n"))

pairs = re.findall(r'^"(.+)"="(.+)"$', answers, flags=re.M)
if len(pairs) != 48:
    sys.exit(f"expected 48 answered questions (24 forks, NP-10 twice, 19 NP-22 rows, 4 NP-23 groups), found {len(pairs)}")


def bullets(sel):
    out = []
    for q, a in pairs:
        if sel(q):
            fid = re.match(r"(NP-\d+)", q).group(1)
            # a question quoting a derived count is pinned to the commit it was asked at, for the map's arm
            at = " at `a15c1f55c`" if "critical path" in q else ""
            out.append(f"- {fid}, asked{at} as \"{q}\": \"{a}\"")
    return "\n".join(out)


main = bullets(lambda q: re.match(r"NP-\d+(?: \(SDLC playbook\))?: ", q) and not q.startswith(("NP-22 ·", "NP-23 ·")))
again = bullets(lambda q: q.startswith("NP-10, again"))
rows = bullets(lambda q: q.startswith("NP-22 ·"))
groups = bullets(lambda q: q.startswith("NP-23 ·"))
for name, block, want in (("main", main, 24), ("again", again, 1), ("rows", rows, 19), ("groups", groups, 4)):
    if block.count("\n- ") + 1 != want:
        sys.exit(f"{name}: expected {want} bullets, found {block.count(chr(10) + '- ') + 1}")

N = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md")
N.text = N.text.rstrip("\n") + f"""

## [answers] The owner's answers, 2026-10-18

Asked on the owner's return, "put the forks to me", through AskUserQuestion in six batches of four, the
recommendation first. Each answer is quoted as the tool returned it.

{main}

NP-10 was answered with a question. The session then gave its pros and cons. ctags gives definitions, their kinds and
mostly their end lines for about 140 languages. It gives no calls and no docstrings, and adds nothing for gov's own
Python, shell and JavaScript. It costs a binary on every node and adopter, version skew between nodes and a GPL
licence, and a missing ctags must stop the run rather than degrade. The session recommended the built-in extractors
by default with a ctags pack a repository opts into, and asked again:

{again}

NP-22, "Review row by row", was asked one row at a time. The session changed one recommendation on review:
`migrate_backlog` should not retire after gov's own migration, since gov and its adopters still carry backlog
shards and `[core]` asks for an upgrade step.

{rows}

NP-23, "Review them", was asked as four groups, the fourth adding the keys NP-19 to NP-21 bring:

{groups}

## [folded-answers] What the answers changed

- **v2's catalogue and presets** (`build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`, its revision note
  dated 2026-10-18):
  - every pending marker gives way to the owner's answer;
  - four defaults move: `probe.experiment.authority` to within-cap, `memory.code-budget` to 16k, `memory.code-roles`
    to every-role and `tags.bundle` to both;
  - `memory.code-languages` reads builtin, builtin+ctags or ctags;
  - three keys land: `maintain.security-review`, `maintain.tiers` and `install.guards`, the last among the keys presets
    never touch;
  - the preset rows follow, each `standard` cell equal to the default.
- **v2's chain rows:** four planned units, and the clause changes the answers imply:
  - dTotalRecall gains the ctags extractor pack;
  - dShippedRelease gains `install.guards`, and its update hooks run the backlog migration as an upgrade step;
  - dTendedCadence gains the recurring security review and the deviation bands, and its dead-pointer detector absorbs
    `check-dead-paths.sh` with its merge-bar leg;
  - dCalibratedLens reads the owner queue's depth with no bound;
  - dOrderedCharter's `gov tag bundle` inlines content by flag.
- **The gap register:** gap-mem-34, gap-deploy-14, gap-maint-12, gap-maint-13 and gap-review-16, each owned once, and
  the tally re-measured.
- **The fates record:** the nineteen proposed rows are now decided by the owner, and four fates change:
  - `migrate_backlog` is reshaped into an update's upgrade step;
  - `check_gate_coverage` merges into `govkit check`;
  - `check-unattended` retires with its kit;
  - `check-dead-paths.sh` merges into Maintain's dead-pointer detector.

  The counts become 24 stay, 70 reshaped, 23 merged and 14 retired, and the design map's count arm reads them.
- **The ownership record:** NP-23's approval, with the three new keys' owners.
- **flow-steps, the systems record and this record's summaries:** NP-5's verifier, NP-14's bundle, NP-9's roles and
  NP-22's counts.
- **The chain:** the critical path grows by three units, one in dTotalRecall and two in dTendedCadence, and still runs
  through dTendedCadence and dCalibratedLens. The instruments record's `[final]` holds the run.

**Interpretations, for the owner to correct:**
- NP-6 keeps `free` as an allowed value, since P10 makes every offered option one. The owner's words name within-cap
  as the default and opt-in as the switch.
- NP-8's "freely adjustable" reads as any size in KB, 4k, 8k and 16k among them, so the preset check reads it as
  free-form.
- NP-14's `both` returns the manifest unless a call passes `--inline` with the byte budget it names.
- NP-21's bands measure a reading's deviation from its pin. Rolling baselines, the playbook's reference, were not
  asked, and stay out.
- NP-20's `install.guards` joins the keys presets never touch, since where the guards install is the operator's
  choice.
- NP-22's merge of `check-dead-paths.sh` keeps its merge-bar leg, registered by the detector at Test's leg-pack point,
  so a dead path still blocks a merge.

**Owed next:** NP-24's pricing of a dDeclaredLoop split and a lighter dCalibratedLens, before the walk resumes.
"""
N.done += 1
N.save()

G = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
G.text = G.text.rstrip("\n") + f"""

Re-measured after the owner's answers added five gaps, `gap-deploy-14`, `gap-maint-12`, `gap-maint-13`, `gap-mem-34`
and `gap-review-16` (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[answers]`), same instrument. A join
of these 255 keys against v2's chain rows finds each owned by exactly one build:

```text
{tally}
```
"""
G.done += 1
G.save()

L = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
L.insert_before("\n## Instruments\n", """
- 2026-10-18, session 1799cb98: the owner answered NP-1 to NP-24 through AskUserQuestion in six batches. NP-10 was
  asked again after its pros and cons, NP-22 reviewed row by row and NP-23 in four groups (the night-pass record's
  `[answers]`). The fold moves four defaults, adds three keys, five gaps and four planned units, and decides the
  fates record's nineteen proposed rows, four of them changed (`[folded-answers]`). NP-24's pricing is next.
""", "event")
L.save()
````

### `pin_np24.py`

Pins NP-24's answer line, which quotes the critical path, to the commit it was asked at. The map's arm was red on it first.

````python
"""Pin NP-24's answer line, which quotes the critical path, to the commit it was asked at, as write_answers.py now
writes it. Usage: python -X utf8 pin_np24.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

N = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md")
N.sub("- NP-24, asked as \"NP-24: dDeclaredLoop is now 47 units, and the critical path is 211",
      "- NP-24, asked at `a15c1f55c` as \"NP-24: dDeclaredLoop is now 47 units, and the critical path is 211", "NP-24 pin")
N.save()
````

### `node_users.py`

NP-24: each node a build owns, the clauses naming it, and the later builds depending on it by the gate's own rules.

````python
"""For one chain build X: each node X owns, the X clauses that name it, and the later builds that depend on it, by the
reconciliation gate's own rules (cites, stage, reads, routes), read from the same records.

Usage: python -X utf8 node_users.py <build> [--json <out>]   (from the worktree root)
It reads backticked citations only, as the gate does; a dependency spelled in plain words is not seen.
"""
import importlib.util
import json
import re
import sys

B = "memory/builds/dClosedLoop/build/"
X = sys.argv[1]
spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)
_, ns = mp.derive()
owner = {}
for kind in ("item", "policy-key", "point", "record-kind", "tag-namespace"):
    for n in ns[kind]:
        own = [v for k, vs in n["rels"] if k == "owner" for v in vs]
        if own:
            owner[(kind, n["key"])] = own[0]

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


def ancestors(b, acc=None):
    acc = set() if acc is None else acc
    for p in parents[b]:
        if p not in acc:
            acc.add(p)
            ancestors(p, acc)
    return acc


later = [b for b in rows if X in ancestors(b)]
mine = {k: o for k, o in owner.items() if o == X}


def cells(ln):
    return [c.strip() for c in re.split(r"(?<!\\)\|", ln.strip().strip("|"))]


def tokens(text):
    t = set(re.findall(r"`([^`\s][^`]*?)(?::[^`]*)?`", text))
    return t, {x[:-2] for x in t if x.endswith(".*")}


def cites(text, kind, key):
    t, wild = tokens(text)
    spelled = key if kind != "record-kind" else key.replace("-", " ")
    return key in t or spelled in t or (kind == "tag-namespace" and key in wild) or \
        (kind == "policy-key" and any(key.startswith(w + ".") for w in wild))


fs = open(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md", encoding="utf-8").read()
items = {}
for m in re.finditer(r"^## \[([a-z-]+)\][^\n]*\n(.*?)(?=^## |\Z)", fs, flags=re.M | re.S):
    for ln in m.group(2).split("\n"):
        if ln.startswith("| `"):
            c = cells(ln)
            if len(c) == 7:
                for tag in re.findall(r"`([a-z]+\.[a-z0-9-]+)`", c[0]):
                    items[tag] = (m.group(1), c[6], " ".join(c[1:6]), c[5])
bp = fs.split("\n## [breakpoint]", 1)[1].split("\n## ", 1)[0]
names_line = next((ln for ln in bp.split("\n") if ln.startswith("- **Its names**")), "")
BREAK = re.compile("|".join(re.escape(v) for v in sorted(re.findall(r"`([a-z][a-z ]+)`", names_line),
                                                          key=len, reverse=True)), re.I)
clauses = [c for c in rows[X].split("; ") if c.strip()]

users = {}   # node -> {build: [rules]}
for (kind, key) in mine:
    u = {}
    for b in later:
        why = []
        if cites(rows[b], kind, key):
            why.append("cites")
        if kind == "item" and key in items:
            step = items[key][0]
            if stage_build.get(step) == b:
                why.append("stage")
        if kind == "policy-key":
            for tag, (step, own, body, then) in items.items():
                if own == b and cites(body, kind, key):
                    why.append(f"reads:{tag}")
                    break
        if kind == "item" and items.get(key, ("",))[0] == "breakpoint":
            if BREAK.search(rows[b]) or any(own == b and step != "breakpoint" and BREAK.search(then)
                                            for tag, (step, own, body, then) in items.items()):
                why.append("routes")
        if why:
            u[b] = why
    named = [i + 1 for i, c in enumerate(clauses) if cites(c, kind, key)]
    users[f"{kind}:{key}"] = {"clauses": named, "users": u}

if "--json" in sys.argv:
    json.dump({"build": X, "clauses": clauses, "later": later, "parents": parents, "nodes": users},
              open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1)
for node, d in sorted(users.items()):
    us = ", ".join(f"{b}({'/'.join(w)})" for b, w in sorted(d["users"].items()))
    print(f"{node:45} clauses {d['clauses'] or '-'} · used by {us or 'none'}")
print(f"{X}: {len(mine)} owned nodes, {len(clauses)} clauses, {len(later)} later builds")
````

### `price_split_asked.py`

NP-24's pricing as the owner was asked from, before its two corrections.

````python
"""NP-24: price a split of dDeclaredLoop and a lighter dCalibratedLens, as critical paths over v2's [chain].

Usage: python -X utf8 price_split.py   (from the worktree root)

A build's units are its planned-units clauses, split on "; " as critical_path.py and the map count them, and a build
starts when every parent has landed. A candidate split replaces one build by two or three, each holding a set of its
clauses, and makes each later build wait for every part holding a clause it needs.

What a later build needs is the classification below. It joins two readings: the gate's mechanical one
(node_users.py: backticked cites, stage items, keys read and routes into the breakpoint program), and a reading of
the plain-word structural dependencies the gate cannot see, each stated with its reason. A split loses if
dWitnessedBar, the spine's critical successor, needs any clause moved out of the spine's first part.
"""
import re
import sys

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
units, parents, clauses = {}, {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        clauses[m.group(1)] = [u for u in m.group(3).split("; ") if u.strip()]
        units[m.group(1)] = len(clauses[m.group(1)])
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]
assert len(units) == 16, len(units)


def path(units, parents):
    finish, via = {}, {}

    def fin(b):
        if b not in finish:
            best = max(parents[b], key=fin, default=None)
            via[b] = best
            finish[b] = units[b] + (fin(best) if best else 0)
        return finish[b]

    end = max(units, key=fin)
    chain_, b = [], end
    while b:
        chain_.append(b)
        b = via[b]
    return finish[end], list(reversed(chain_)), finish


# dDeclaredLoop's clauses, numbered as chain_clauses.py prints them, by who needs them.
X = "dDeclaredLoop"
SPINE_CORE = {1, 5, 6, 7, 8, 10, 15, 17, 20, 23, 30, 31, 32, 33, 34, 35, 36, 37}
# The breakpoint mechanism dWitnessedBar's stage needs: test.recommend and test.reason are its stage items (the
# gate's stage rule), and they run through breakpoints and the program's items (AF-1).
TEST_NEEDS = {40, 41, 43}
# Needed by dTotalRecall or dBoundRoles, which start as dWitnessedBar lands.
EARLY = {
    11: "dTotalRecall cites `leases.offline` and mints ids under a claim or lease; dRankedPlan and dScopedBuild read "
        "lease keys",
    18: "dBoundRoles renders every item's work order, the entry items' included; dRankedPlan follows entry",
    19: "dBoundRoles cites `placement.check`",
    38: "dBoundRoles's work order carries the `map` slot each item declares; dTotalRecall's replay reads it",
    46: "dBoundRoles cites the `probe` kind, each role's return gaining the probe outcome; dRankedPlan reads "
        "`probe.observations`",
    47: "dBoundRoles computes each item's `code` slot from its declared seed",
}
# Needed only by builds that start after dTotalRecall or dBoundRoles lands.
LATE = {
    2: "the named presets: until they land a key reads its catalogue default, so only `standard` works",
    3: "the preset step in the reader, with them",
    4: "the charter's preset section, with them",
    9: "policy at govkit intake: dShippedRelease",
    21: "`actions.free` at the tool call: dWellOiledMachine's hooks",
    39: "the policy namespaces' purposes, reviewed: no later build",
    16: "the card: dWellOiledMachine's session-start load and dRankedPlan's entry",
    22: "orientation cost per stage: dCalibratedLens",
    25: "`notify.owner`: dWellOiledMachine's notification adapters",
    26: "the fresh-session recommendation: dWellOiledMachine",
    27: "`card.pointers`: dWellOiledMachine's replay",
    28: "`context.on-full`: dWellOiledMachine",
    29: "a compaction summary read as a lead: dWellOiledMachine",
    12: "the mailbox: dWellOiledMachine's live delivery, dScopedBuild and dShippedRelease",
    13: "live delivery: dWellOiledMachine",
    14: "dependency coordination: dIndexedDesign, dScopedBuild and dShippedRelease",
    24: "`mailbox.reads`: dWellOiledMachine",
    42: "follow-up and design-audit rounds: dScopedBuild and dIndexedDesign",
    44: "the attendance rule: dWellOiledMachine's announcement and attendance override",
    45: "`repeat`: dIndexedDesign's seventh input and dTendedCadence's cyclic playbooks",
}
EARLY_USERS = {"dTotalRecall", "dBoundRoles", "dRankedPlan", "dScopedBuild"}
LATE_USERS = {"dShippedRelease", "dWellOiledMachine", "dRankedPlan", "dCalibratedLens", "dScopedBuild",
              "dIndexedDesign", "dTendedCadence", "dConvergedCharter"}
allc = SPINE_CORE | TEST_NEEDS | set(EARLY) | set(LATE)
if allc != set(range(1, units[X] + 1)) or len(SPINE_CORE) + len(TEST_NEEDS) + len(EARLY) + len(LATE) != units[X]:
    sys.exit(f"the classification covers {sorted(allc)} of {units[X]} clauses, or holds one twice")


def split(parts):
    """parts: [(name, clause set, parents of the part, builds needing it)]; the first part keeps X's name."""
    u, p = dict(units), {b: list(v) for b, v in parents.items()}
    del u[X]
    for name, cs, par, users in parts:
        u[name] = len(cs)
        p[name] = list(par)
    for b in p:
        if X in p[b]:
            p[b] = [q for q in p[b] if q != X] + [X] + [name for name, _, _, users in parts[1:] if b in users]
    return u, p


base, base_path, base_fin = path(units, parents)
print(f"baseline: {base} units, {' > '.join(base_path)}")
first = SPINE_CORE | TEST_NEEDS
cands = {
    "S1, two builds: the late parts leave": [
        (X, first | set(EARLY), parents[X], None),
        ("dDeclaredLoop-B", set(LATE), [X], LATE_USERS)],
    "S2, two builds: everything dWitnessedBar does not need leaves": [
        (X, first, parents[X], None),
        ("dDeclaredLoop-B", set(EARLY) | set(LATE), [X], EARLY_USERS | LATE_USERS)],
    "S3, three builds: the early and the late parts each leave": [
        (X, first, parents[X], None),
        ("dDeclaredLoop-B", set(EARLY), [X], EARLY_USERS),
        ("dDeclaredLoop-C", set(LATE), [X], LATE_USERS)],
}
for label, parts in cands.items():
    u, p = split(parts)
    n, pth, fin = path(u, p)
    sizes = ", ".join(f"{name} {len(cs)}" for name, cs, _, _ in parts)
    print(f"{label}: {sizes} · {n} units ({n - base:+d}), {' > '.join(pth)}")
    if "dWitnessedBar" in [b for b in p if any(q.startswith("dDeclaredLoop-") for q in p[b])]:
        print("  LOSES: dWitnessedBar waits for a moved part")
    for name, cs, _, _ in parts[1:]:
        print(f"  {name} lands at {fin[name]}, dWitnessedBar at {fin['dWitnessedBar']}")

# dCalibratedLens: the tail. dConvergedCharter starts when its last parent lands.
Y, Z = "dCalibratedLens", "dConvergedCharter"
tail = sorted(((base_fin[q], q) for q in parents[Z]), reverse=True)
print(f"{Z}'s parents land at: " + ", ".join(f"{q} {f}" for f, q in tail))
slack = tail[0][0] - tail[1][0]
print(f"lightening {Y} by k units saves min(k, {slack}): the next parent, {tail[1][1]}, lands only {slack} units before "
      f"{Y} does")
LOOP_REVIEW = {3, 5, 8, 11}   # the clauses that read the Loop Review, which dTendedCadence's cadence delivers
rest = set(range(1, units[Y] + 1)) - LOOP_REVIEW
u, p = dict(units), {b: list(v) for b, v in parents.items()}
u[Y] = len(LOOP_REVIEW)
u[Y + "-A"] = len(rest)
p[Y + "-A"] = [q for q in parents[Y] if q != "dTendedCadence"] + ["dWellOiledMachine"]
p[Y] = parents[Y] + [Y + "-A"]
n, pth, fin = path(u, p)
print(f"L1, {Y} split: the Loop Review's {len(LOOP_REVIEW)} after dTendedCadence, the other {len(rest)} after "
      f"dWellOiledMachine · {n} units ({n - base:+d}), {' > '.join(pth)}")
for label, parts in list(cands.items())[:1]:
    u2, p2 = split(parts)
    u2[Y] = len(LOOP_REVIEW)
    u2[Y + "-A"] = len(rest)
    p2[Y + "-A"] = [q for q in parents[Y] if q != "dTendedCadence"] + ["dWellOiledMachine"]
    p2[Y] = parents[Y] + [Y + "-A"]
    n2, pth2, _ = path(u2, p2)
    print(f"S1 with L1: {n2} units ({n2 - base:+d}), {' > '.join(pth2)}")
````

### `price_split.py`

NP-24's pricing, corrected: the classification, the candidate splits' critical paths and dCalibratedLens's slack.

````python
"""NP-24: price a split of dDeclaredLoop and a lighter dCalibratedLens, as critical paths over v2's [chain].

Usage: python -X utf8 price_split.py   (from the worktree root)

A build's units are its planned-units clauses, split on "; " as critical_path.py and the map count them, and a build
starts when every parent has landed. A candidate split replaces one build by two or three, each holding a set of its
clauses, and makes each later build wait for every part holding a clause it needs.

What a later build needs is the classification below. It joins two readings: the gate's mechanical one
(node_users.py: backticked cites, stage items, keys read and routes into the breakpoint program), and a reading of
the plain-word structural dependencies the gate cannot see, each stated with its reason. A split loses if
dWitnessedBar, the spine's critical successor, needs any clause moved out of the spine's first part.
"""
import re
import sys

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
units, parents, clauses = {}, {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        clauses[m.group(1)] = [u for u in m.group(3).split("; ") if u.strip()]
        units[m.group(1)] = len(clauses[m.group(1)])
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]
assert len(units) == 16, len(units)


def path(units, parents):
    finish, via = {}, {}

    def fin(b):
        if b not in finish:
            best = max(parents[b], key=fin, default=None)
            via[b] = best
            finish[b] = units[b] + (fin(best) if best else 0)
        return finish[b]

    end = max(units, key=fin)
    chain_, b = [], end
    while b:
        chain_.append(b)
        b = via[b]
    return finish[end], list(reversed(chain_)), finish


# dDeclaredLoop's clauses, numbered as chain_clauses.py prints them, by who needs them.
X = "dDeclaredLoop"
# 42 joined the core while the owner's S3 was folded: `review.dispose`, a core item, reads `review.follow-up`
# (the gate's reads rule over flow-steps), so the follow-up rounds cannot land after the core.
SPINE_CORE = {1, 5, 6, 7, 8, 10, 15, 17, 20, 23, 30, 31, 32, 33, 34, 35, 36, 37, 42}
CORRECTED = {
    16: "moved from the late parts to the early ones: `entry.orient`, an entry item, composes the card",
    42: "moved from the late parts to the core: `review.dispose`, a core item, reads `review.follow-up`",
}
# The breakpoint mechanism dWitnessedBar's stage needs: test.recommend and test.reason are its stage items (the
# gate's stage rule), and they run through breakpoints and the program's items (AF-1).
TEST_NEEDS = {40, 41, 43}
# Needed by dTotalRecall or dBoundRoles, which start as dWitnessedBar lands.
EARLY = {
    11: "dTotalRecall cites `leases.offline` and mints ids under a claim or lease; dRankedPlan and dScopedBuild read "
        "lease keys",
    18: "dBoundRoles renders every item's work order, the entry items' included; dRankedPlan follows entry",
    19: "dBoundRoles cites `placement.check`",
    38: "dBoundRoles's work order carries the `map` slot each item declares; dTotalRecall's replay reads it",
    46: "dBoundRoles cites the `probe` kind, each role's return gaining the probe outcome; dRankedPlan reads "
        "`probe.observations`",
    47: "dBoundRoles computes each item's `code` slot from its declared seed",
    16: "the card: `entry.orient` composes it, and dWellOiledMachine's session-start load reads it",
}
# Needed only by builds that start after dTotalRecall or dBoundRoles lands.
LATE = {
    2: "the named presets: until they land a key reads its catalogue default, so only `standard` works",
    3: "the preset step in the reader, with them",
    4: "the charter's preset section, with them",
    9: "policy at govkit intake: dShippedRelease",
    21: "`actions.free` at the tool call: dWellOiledMachine's hooks",
    39: "the policy namespaces' purposes, reviewed: no later build",
    22: "orientation cost per stage: dCalibratedLens",
    25: "`notify.owner`: dWellOiledMachine's notification adapters",
    26: "the fresh-session recommendation: dWellOiledMachine",
    27: "`card.pointers`: dWellOiledMachine's replay",
    28: "`context.on-full`: dWellOiledMachine",
    29: "a compaction summary read as a lead: dWellOiledMachine",
    12: "the mailbox: dWellOiledMachine's live delivery, dScopedBuild and dShippedRelease",
    13: "live delivery: dWellOiledMachine",
    14: "dependency coordination: dIndexedDesign, dScopedBuild and dShippedRelease",
    24: "`mailbox.reads`: dWellOiledMachine",
    44: "the attendance rule: dWellOiledMachine's announcement and attendance override",
    45: "`repeat`: dIndexedDesign's seventh input and dTendedCadence's cyclic playbooks",
}
EARLY_USERS = {"dTotalRecall", "dBoundRoles", "dRankedPlan", "dScopedBuild"}
LATE_USERS = {"dShippedRelease", "dWellOiledMachine", "dRankedPlan", "dCalibratedLens", "dScopedBuild",
              "dIndexedDesign", "dTendedCadence", "dConvergedCharter"}
allc = SPINE_CORE | TEST_NEEDS | set(EARLY) | set(LATE)
if allc != set(range(1, units[X] + 1)) or len(SPINE_CORE) + len(TEST_NEEDS) + len(EARLY) + len(LATE) != units[X]:
    sys.exit(f"the classification covers {sorted(allc)} of {units[X]} clauses, or holds one twice")


def split(parts):
    """parts: [(name, clause set, parents of the part, builds needing it)]; the first part keeps X's name."""
    u, p = dict(units), {b: list(v) for b, v in parents.items()}
    del u[X]
    for name, cs, par, users in parts:
        u[name] = len(cs)
        p[name] = list(par)
    for b in p:
        if X in p[b]:
            p[b] = [q for q in p[b] if q != X] + [X] + [name for name, _, _, users in parts[1:] if b in users]
    return u, p


base, base_path, base_fin = path(units, parents)
RESULTS = []   # (label, part sizes, new builds, path, saved), for the record's table
print(f"baseline: {base} units, {' > '.join(base_path)}")
for n_, why in sorted(CORRECTED.items()):
    print(f"corrected while folding: clause {n_} {why}")
first = SPINE_CORE | TEST_NEEDS
cands = {
    "S1, two builds: the late parts leave": [
        (X, first | set(EARLY), parents[X], None),
        ("dDeclaredLoop-B", set(LATE), [X], LATE_USERS)],
    "S2, two builds: everything dWitnessedBar does not need leaves": [
        (X, first, parents[X], None),
        ("dDeclaredLoop-B", set(EARLY) | set(LATE), [X], EARLY_USERS | LATE_USERS)],
    "S3, three builds: the early and the late parts each leave": [
        (X, first, parents[X], None),
        ("dDeclaredLoop-B", set(EARLY), [X], EARLY_USERS),
        ("dDeclaredLoop-C", set(LATE), [X], LATE_USERS)],
}
for label, parts in cands.items():
    u, p = split(parts)
    n, pth, fin = path(u, p)
    sizes = ", ".join(f"{name} {len(cs)}" for name, cs, _, _ in parts)
    print(f"{label}: {sizes} · {n} units ({n - base:+d}), {' > '.join(pth)}")
    RESULTS.append((label, [len(cs) for _, cs, _, _ in parts], len(parts) - 1, n, base - n))
    if "dWitnessedBar" in [b for b in p if any(q.startswith("dDeclaredLoop-") for q in p[b])]:
        print("  LOSES: dWitnessedBar waits for a moved part")
    for name, cs, _, _ in parts[1:]:
        print(f"  {name} lands at {fin[name]}, dWitnessedBar at {fin['dWitnessedBar']}")

# dCalibratedLens: the tail. dConvergedCharter starts when its last parent lands.
Y, Z = "dCalibratedLens", "dConvergedCharter"
tail = sorted(((base_fin[q], q) for q in parents[Z]), reverse=True)
print(f"{Z}'s parents land at: " + ", ".join(f"{q} {f}" for f, q in tail))
slack = tail[0][0] - tail[1][0]
print(f"lightening {Y} by k units saves min(k, {slack}): the next parent, {tail[1][1]}, lands only {slack} units before "
      f"{Y} does")
LOOP_REVIEW = {3, 5, 8, 11}   # the clauses that read the Loop Review, which dTendedCadence's cadence delivers
rest = set(range(1, units[Y] + 1)) - LOOP_REVIEW
u, p = dict(units), {b: list(v) for b, v in parents.items()}
u[Y] = len(LOOP_REVIEW)
u[Y + "-A"] = len(rest)
p[Y + "-A"] = [q for q in parents[Y] if q != "dTendedCadence"] + ["dWellOiledMachine"]
p[Y] = parents[Y] + [Y + "-A"]
n, pth, fin = path(u, p)
print(f"L1, {Y} split: the Loop Review's {len(LOOP_REVIEW)} after dTendedCadence, the other {len(rest)} after "
      f"dWellOiledMachine · {n} units ({n - base:+d}), {' > '.join(pth)}")
RESULTS.append(("L1: dCalibratedLens split at the Loop Review", [len(LOOP_REVIEW), len(rest)], 1, n, base - n))
for label, parts in list(cands.items())[:1]:
    u2, p2 = split(parts)
    u2[Y] = len(LOOP_REVIEW)
    u2[Y + "-A"] = len(rest)
    p2[Y + "-A"] = [q for q in parents[Y] if q != "dTendedCadence"] + ["dWellOiledMachine"]
    p2[Y] = parents[Y] + [Y + "-A"]
    n2, pth2, _ = path(u2, p2)
    print(f"S1 with L1: {n2} units ({n2 - base:+d}), {' > '.join(pth2)}")
    RESULTS.append(("S1 with L1", [], 2, n2, base - n2))
````

### `write_pricing.py`

Writes the pricing record from both runs, its table derived from the corrected one.

````python
"""Write NP-24's pricing record from price_split.py's classification, its corrected run and the run the owner was
asked from. Run it on the chain as priced, `1d32760f3`, before the split is folded.

Usage: python -X utf8 write_pricing.py <price.out> <price_asked.out>   (from the worktree root)
"""
import importlib.util
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("price", HERE / "price_split.py")
P = importlib.util.module_from_spec(spec)
_out = sys.stdout
sys.stdout = open(os.devnull, "w")
spec.loader.exec_module(P)   # its prints are the run, recorded from the captured file instead
sys.stdout = _out
run = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")
asked = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")
OUT = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md")
cl = P.clauses[P.X]


def short(n):
    c = cl[n - 1]
    return c if len(c) <= 90 else c[:87].rsplit(" ", 1)[0] + " …"


def table(d):
    rows = ["| Clause | The unit | Who needs it, and why |", "|---|---|---|"]
    rows += [f"| {n} | {short(n).replace('|', '/')} | {why} |" for n, why in sorted(d.items())]
    return "\n".join(rows)


def listed(xs):
    xs = [str(x) for x in xs]
    return "" if not xs else xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


core = listed(sorted(P.SPINE_CORE))
test = listed(sorted(P.TEST_NEEDS))
results = ["| Candidate | Parts, in units | New builds | Path, in units | Saved |", "|---|---|---|---|---|"]
results += [f"| {label} | {listed(sizes)} | {nb} | {n} | {saved} |" for label, sizes, nb, n, saved in P.RESULTS]
corrected = "\n".join(f"  - clause {n} {why};" for n, why in sorted(P.CORRECTED.items())).rstrip(";") + "."
OUT.write_text(f"""# NP-24 priced: a split of dDeclaredLoop, and a lighter dCalibratedLens

**Serves:** research PLAY-dClosedLoop-1

The owner's answer to NP-24, 2026-10-18, was "Price it now (Recommended)"
(`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[answers]`). This record prices both changes against the
chain at `1d32760f3`, the commit that folded the answers, and parks the choice as SP-1 and SP-2. At that commit the
critical path is {P.base} units, `1d32760f3`'s v2 `[chain]` read by the script below.

## [method] How a split is priced

- **Units.** A build's units are its planned-units clauses, split on "; " as the design map and the critical-path
  script count them. A build starts when every parent has landed.
- **A split** replaces dDeclaredLoop by two or three parts, each holding a set of its clauses. A later build waits for
  every part that holds a clause it needs.
- **What a later build needs** joins two readings:
  - the reconciliation gate's mechanical one: backticked cites, stage items, keys read, and routes into the breakpoint
    program (`node_users.py`, kept in the night-pass instruments record);
  - a reading of the structural needs the gate cannot see, because they are spelled in plain words, stated clause by
    clause in `[classification]`.
- **The losing test.** A split loses if dWitnessedBar, the spine's successor on the critical path, waits for a moved
  part.
- **What it does not price.** A new build's fixed cost, which no unit counts: its kickoff, README and roster, its specs
  and their audit, a closing review and a landing.

## [classification] dDeclaredLoop's {len(cl)} clauses, by who needs them

Clause numbers are those `chain_clauses.py` prints for dDeclaredLoop's row at `1d32760f3`.

- **The spine's core ({len(P.SPINE_CORE)}): clauses {core}.** Every later build rests on these: the loop kit, the
  guard and floor, transitions, stage claims and coverage, the witness-class rule, the factories, the position engine,
  claims, item declarations, the transition tables, the failure route, terminal states, the disposition set, computed
  witnesses and the tag namespaces. The follow-up rounds join them, since `review.dispose`, a core item, reads
  `review.follow-up`.
- **What dWitnessedBar's stage needs ({len(P.TEST_NEEDS)}): clauses {test}.** These are the breakpoint mechanism.
  `test.recommend` and `test.reason` are Test's stage items, by the gate's stage rule, and they run through the
  breakpoints and the program's items.
- **Needed by dTotalRecall or dBoundRoles ({len(P.EARLY)}).** Both builds start as dWitnessedBar lands.

{table(P.EARLY)}

- **Needed only by builds that start later ({len(P.LATE)}).** Each later build starts after dTotalRecall or dBoundRoles
  lands.

{table(P.LATE)}

## [results] The candidates, at `1d32760f3`

**As asked.** The owner was asked from the first run, as captured:

```text
{asked}
```

**As corrected.** Folding the owner's S3 found two clauses placed against the gate's own rules:
{corrected}

The run after both corrections, as captured:

```text
{run}
```

{chr(10).join(results)}

- **S3, the owner's choice, delays nothing.** Its early part lands before dWitnessedBar. Its late part's first user
  starts only after dTotalRecall lands.
- **S2 couples the early parts' users to the late ones.** dTotalRecall and dBoundRoles then wait for one moved part
  that holds both, and it lands after dWitnessedBar.
- **S1 leaves the early parts in the spine.** That keeps one build, but holds the spine's successor longer.
- **No lightening of dCalibratedLens saves more than {P.slack} units.** dShippedRelease lands only {P.slack} units
  before it, and the path then runs through dShippedRelease.

## [costs] What a split costs

- **One more build per new part.** Each new part brings the fixed cost `[method]` names.
- **While the moved parts land beside dWitnessedBar:**
  - only the `standard` preset works, since every key reads its catalogue default;
  - sessions orient on today's kickoff card until the early part lands;
  - no mailbox carries dependency notices;
  - `attendance` is not yet a key, so every run is unattended, which is its default anyway.
- **The re-cut it owes:**
  - the new builds' rows, rosters and gaps;
  - their nodes' owners, moved in the ownership record and flow-steps;
  - the later builds' after cells;
  - the reconciliation gate, re-run;
  - the walk's waves, derived again.

## [forks] Parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| SP-1 | Split dDeclaredLoop? | S1, the late parts leave as one new build; S3, the early and the late parts leave as two new builds; keep the chain as it stands | a structural decision about the chain |
| SP-2 | Lighten dCalibratedLens? | keep it whole, since no lightening saves more than the slack before dShippedRelease; split it at the Loop Review, L1 | a structural decision about the chain |

S1 was recommended because one new build buys most of what any split reaches (`[results]`).
""", encoding="utf-8", newline="\n")
print(f"wrote {OUT}: {OUT.stat().st_size} bytes")
````

### `fold_split.py`

The owner's S3 folded: the three rows, the moved owners, the parents, the class row, the fates destinations and the ownership amendment.

````python
"""Fold the owner's SP-1 (S3) and SP-2 into the design: dDeclaredLoop splits into itself, dPlacedRequest (Entry) and
dKeptSession (Session) along price_split.py's corrected classification, and dCalibratedLens stays whole. The nodes
move with their clauses: v2's chain rows and catalogue owners, flow-steps' item owners, layer-memory's kinds, the
re-cut's class row, the fates record's destinations and the ownership amendment.

Usage: python -X utf8 fold_split.py   (from the worktree root, on the chain as priced, before any split)
"""
import importlib.util
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "expansions"))
from fold_lib import Record  # noqa: E402

spec = importlib.util.spec_from_file_location("price", HERE / "price_split.py")
P = importlib.util.module_from_spec(spec)
_out = sys.stdout
sys.stdout = open(os.devnull, "w")
spec.loader.exec_module(P)
sys.stdout = _out

B = "memory/builds/dClosedLoop/build/"
A_SET = P.SPINE_CORE | P.TEST_NEEDS
E_SET, L_SET = set(P.EARLY), set(P.LATE)
CL = P.clauses[P.X]
assert len(A_SET) + len(E_SET) + len(L_SET) == len(CL) == 47
E, L = "dPlacedRequest", "dKeptSession"
GAPS = {
    "dDeclaredLoop": ["gap-spine-01", "gap-spine-02", "gap-orient-03", "gap-orient-05", "gap-flow-13", "gap-flow-14",
                      "gap-flow-15", "gap-spine-07", "gap-flow-11", "gap-flow-12"],
    E: ["gap-flow-07", "gap-conc-01", "gap-conc-02", "gap-orient-01", "gap-orient-02", "gap-orient-04", "gap-orient-11",
        "gap-flow-18"],
    L: ["gap-flow-06", "gap-orient-06", "gap-flow-16"],
}
E_KEYS = ["leases", "leases.granularity", "leases.renewal", "leases.expiry-hours", "leases.overlap", "leases.offline",
          "card.follows", "card.store", "card.snapshot", "resume.partial", "resume.context", "placement",
          "placement.check", "probe.points", "probe.raise", "probe.observations", "probe.experiment.authority"]
L_KEYS = ["preset", "attendance", "deps.coordination", "deps.early-build", "deps.messaging", "notify.owner",
          "mailbox.reads", "context.on-full", "context.threshold", "card.pointers", "actions.free", "orient.budget"]
E_ITEMS = ["entry.orient", "entry.place", "entry.place-check", "entry.place-owner", "entry.claim", "probe.trigger",
           "probe.pin", "probe.design", "probe.experiment", "probe.run", "probe.judge", "probe.return"]


def pick(nums):
    return "; ".join(CL[n - 1] for n in sorted(nums))


# --- v2 ---------------------------------------------------------------------------------------------------------
V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
old_row = next(ln for ln in V.text.split("\n") if ln.startswith("| dDeclaredLoop | Spine |"))
cells = [c.strip() for c in old_row.strip().strip("|").split(" | ")]
assert cells[3] == "; ".join(CL), "dDeclaredLoop's planned units differ from the priced row"
new_rows = "\n".join([
    f"| dDeclaredLoop | Spine | {cells[2]} | {pick(A_SET)} | {', '.join(GAPS['dDeclaredLoop'])} |",
    f"| {E} | Entry | dDeclaredLoop | {pick(E_SET)} | {', '.join(GAPS[E])} |",
    f"| {L} | Session | dDeclaredLoop, {E} | {pick(L_SET)} | {', '.join(GAPS[L])} |",
])
moved = set(g.strip() for g in cells[4].split(","))
assert moved == set(sum(GAPS.values(), [])), sorted(moved ^ set(sum(GAPS.values(), [])))
V.sub(old_row, new_rows, "dDeclaredLoop's row, split")
for build, stage, old, new in (("dBoundRoles", "Roles", "dDeclaredLoop, dWitnessedBar", f"dDeclaredLoop, dWitnessedBar, {E}"),
                               ("dTotalRecall", "Memory", "dDeclaredLoop, dWitnessedBar", f"dDeclaredLoop, dWitnessedBar, {E}"),
                               ("dWellOiledMachine", "Runtime", "dBoundRoles, dTotalRecall", f"dBoundRoles, dTotalRecall, {L}"),
                               ("dIndexedDesign", "Design", "dDeclaredLoop, dTotalRecall", f"dDeclaredLoop, dTotalRecall, {L}")):
    V.sub(f"| {build} | {stage} | {old} |", f"| {build} | {stage} | {new} |", f"{build}'s parents")
pol = V.text.split("\n## [policies]", 1)[1].split("\n## ", 1)[0]
new_pol = pol
for keys, owner in ((E_KEYS, E), (L_KEYS, L)):
    for k in keys:
        rows = [ln for ln in new_pol.split("\n") if ln.startswith(f"| `{k}` |")]
        if len(rows) != 1 or not rows[0].endswith("| dDeclaredLoop |"):
            sys.exit(f"catalogue: `{k}` has {len(rows)} rows, or another owner")
        new_pol = new_pol.replace(rows[0], rows[0][:-len("dDeclaredLoop |")] + f"{owner} |")
V.sub(pol, new_pol, "catalogue owners")
V.done += len(E_KEYS) + len(L_KEYS) - 1
V.sub("once dDeclaredLoop adds presets to this reader", f"once {L} adds presets to this reader", "dGroundRules presets")
V.sub("and dDeclaredLoop renders the charter's preset section",
      f"and {L}, split from dDeclaredLoop (SP-1), renders the charter's preset section", "owed preset section")
V.insert_before("\nRevised: 2026-10-17, after the folds' closing review", f"""
Revised: 2026-10-18, NP-24 priced and the owner's SP-1 and SP-2 (`build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`):
- dDeclaredLoop splits three ways, the owner's S3: it keeps the spine's core and the breakpoint mechanism; {E}, the
  entry, takes leases, the card, the entry items, placement, the `map` slot, the probe program and the code seed; and
  {L}, the session, takes presets, session handling across compaction, the mailbox and dependency notices, the
  attendance rule and `repeat`;
- each moved key, item and kind changes owner with its clause, and dBoundRoles and dTotalRecall gain {E} as a parent,
  dWellOiledMachine and dIndexedDesign {L};
- dDeclaredLoop's gaps split with its clauses, ten, eight and three;
- dCalibratedLens stays whole (SP-2): no lightening saves more than the slack before dShippedRelease.
""", "revision note")
V.save()

# --- flow-steps -------------------------------------------------------------------------------------------------
FS = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
for tag in E_ITEMS:
    rows = [ln for ln in FS.text.split("\n") if ln.startswith(f"| `{tag}` |")]
    if len(rows) != 1 or not rows[0].endswith("| dDeclaredLoop |"):
        sys.exit(f"flow-steps: `{tag}` has {len(rows)} rows, or another owner")
    FS.sub(rows[0], rows[0][:-len("dDeclaredLoop |")] + f"{E} |", tag)
FS.sub("- **Owner** (revised 2026-10-17, PM-9): dDeclaredLoop builds the step's items,",
       f"- **Owner** (revised 2026-10-17, PM-9, and 2026-10-18, SP-1): {E} builds the step's items,", "entry owner")
FS.sub("(the closing review's H2 and M2). dDeclaredLoop builds the program ahead of",
       f"(the closing review's H2 and M2). {E} builds the program ahead of", "probe owner")
FS.save()

# --- layer-memory -----------------------------------------------------------------------------------------------
LM = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md")
LM.sub("| card | dDeclaredLoop |", f"| card | {E} |", "card")
LM.sub("| lease | dDeclaredLoop | dDeclaredLoop's row builds the one lease grammar;",
       f"| lease | {E} | {E}'s row builds the one lease grammar;", "lease")
LM.sub("| mailbox message | dDeclaredLoop | dDeclaredLoop's row builds the mailbox and its message kinds;",
       f"| mailbox message | {L} | {L}'s row builds the mailbox and its message kinds;", "mailbox message")
LM.sub("| probe | dDeclaredLoop |", f"| probe | {E} |", "probe")
LM.save()

# --- the re-cut's class row ---------------------------------------------------------------------------------------
RC = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-recut.md")
RC.sub("| dFairHearing | `preset` | dDeclaredLoop | homonym |", f"| dFairHearing | `preset` | {L} | homonym |", "preset")
RC.save()

# --- the fates record's destinations -------------------------------------------------------------------------------
F = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-fates.md")
F.sub("fleet identity in the lease grammar (dDeclaredLoop) | v2 `[chain]` dDeclaredLoop; v2 `[chain]` dWellOiledMachine |",
      f"fleet identity in the lease grammar ({E}) | v2 `[chain]` {E}; v2 `[chain]` dWellOiledMachine |", "fleet.toml")
F.sub("| MERGED | the one lease grammar (dDeclaredLoop) | v2 `[chain]` dDeclaredLoop |",
      f"| MERGED | the one lease grammar ({E}) | v2 `[chain]` {E} |", "claims")
F.sub("reached by the `repeat` disposition (dDeclaredLoop) |", f"reached by the `repeat` disposition ({L}) |", "playbook mode")
F.sub("card ref (dDeclaredLoop); compact re-inject (dWellOiledMachine) | v2 `[chain]` dOrderedCharter; v2 `[chain]` "
      "dDeclaredLoop;",
      f"card ref ({E}); compact re-inject (dWellOiledMachine) | v2 `[chain]` dOrderedCharter; v2 `[chain]` {E};",
      "card hooks")
F.sub("continue among `entry.place`'s dispositions (dDeclaredLoop) |",
      f"continue among `entry.place`'s dispositions ({E}) |", "slug mode")
F.save()

# --- the ownership record -----------------------------------------------------------------------------------------
O = Record(B + "2026-10-17-build-PLAY-dClosedLoop-1-ownership.md")
O.text = O.text.rstrip("\n") + f"""
- **SP-1, 2026-10-18:** the owner chose S3, so dDeclaredLoop splits into itself, {E} and {L}
  (`build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`). The nodes move with their clauses:
  - to {E}: the entry items `entry.orient`, `entry.place`, `entry.place-check`, `entry.place-owner` and
    `entry.claim`, the probe program's seven items, the `lease`, `card` and `probe` kinds, and the keys
    {', '.join(f'`{k}`' for k in E_KEYS)};
  - to {L}: the `mailbox message` kind and the keys {', '.join(f'`{k}`' for k in L_KEYS)}.
"""
O.done += 1
O.save()
print(f"split: dDeclaredLoop {len(A_SET)}, {E} {len(E_SET)}, {L} {len(L_SET)}")
````

### `fold_split_classes.py`

The four class rows whose citing clause moved, re-pointed once the gate was red on them.

````python
"""The re-cut's class rows whose citing clause moved to dKeptSession with SP-1: the gate read them as rows no dependency
needs, and the moved clauses' citations as unclassed, until each row names the build that now cites.

Usage: python -X utf8 fold_split_classes.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

RC = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md")
for node in ("`build.closes`", "`intake`", "`playbook`", "`hooks.bypass`"):
    RC.sub(f"| dDeclaredLoop | {node} |", f"| dKeptSession | {node} |", node)
RC.save()
````

### `write_split_answers.py`

The pricing record's `[answers]` and `[folded]`, the night-pass record's owed line and the session log's event.

````python
"""Record the owner's SP-1, SP-2 and the two build names in the pricing record ([answers], verbatim, and [folded]),
amend the night-pass record's owed line, and log the event.

Usage: python -X utf8 write_split_answers.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
PR = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md")
PR.text = PR.text.rstrip("\n") + """

## [answers] The owner's answers, 2026-10-18

Asked through AskUserQuestion with the first run's figures (`[results]`, "As asked"), each answer quoted as the tool
returned it, the critical path's quoted length pinned to the commit it was read at:
- SP-1, asked at `1d32760f3` as "SP-1: Split dDeclaredLoop? (a structural decision about the chain; critical path 214 today)": "S3, two new builds"
- SP-2, asked as "SP-2: Lighten dCalibratedLens? (a structural decision about the chain)": "Keep it whole (Recommended)"

The two new builds' names, asked after:
- asked as "Name for the early build (7 units: leases, the card, the entry items and placement, the map slot, the probe program, the code seed), which lands beside dWitnessedBar?": "dPlacedRequest (Recommended)"
- asked as "Name for the late build (19 units: presets, session handling across compaction, the mailbox and dependency notices, follow-up review rounds, attendance, repeat)?": "dKeptSession (Recommended)"

The naming questions already carried the first correction, the card moving to the early build. The second, the
follow-up rounds staying in the spine, was found after them, so dKeptSession holds 18 units, not the 19 asked.

## [folded] What the answers changed

- **v2's chain** (its revision note dated 2026-10-18, SP-1):
  - dDeclaredLoop keeps 22 units, the spine's core and the breakpoint mechanism;
  - dPlacedRequest, stage Entry, after dDeclaredLoop, takes 7;
  - dKeptSession, stage Session, after dDeclaredLoop and dPlacedRequest, takes 18;
  - dBoundRoles and dTotalRecall gain dPlacedRequest as a parent, and dWellOiledMachine and dIndexedDesign gain
    dKeptSession;
  - dDeclaredLoop's 21 gaps split ten, eight and three;
  - dGroundRules's preset step and `[owed]`'s preset section now name dKeptSession.
- **The owners:**
  - v2's catalogue: 17 keys to dPlacedRequest and 12 to dKeptSession;
  - flow-steps: the five entry items and the probe program's seven to dPlacedRequest;
  - layer-memory: the `card`, `lease` and `probe` kinds to dPlacedRequest, and the `mailbox message` kind to
    dKeptSession;
  - the ownership record's amendment lists every moved node.
- **The re-cut's class rows:** the five whose citing clause moved now name dKeptSession. The gate read the old rows as
  needing no dependency, and the moved citations as unclassed, until they did.
- **The fates record:** five destinations that moved with their clauses.
- **The chain:** the critical path drops by twenty-five units, as the corrected run priced. Both new builds land before
  any build that waits on them starts. The instruments record's `[final]` holds the run.
- **dCalibratedLens** stays whole (SP-2).

**Owed next:** the walk resumes, its `[chain]` glance and wave 1 derived again over eighteen builds.
"""
PR.done += 1
PR.save()

N = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md")
N.sub("**Owed next:** NP-24's pricing of a dDeclaredLoop split and a lighter dCalibratedLens, before the walk resumes.",
      "**Owed next:** NP-24's pricing of a dDeclaredLoop split and a lighter dCalibratedLens, before the walk resumes.\n"
      "It is done in `build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`, where the owner chose a three-way split,\n"
      "dPlacedRequest and dKeptSession leaving dDeclaredLoop, and kept dCalibratedLens whole.", "owed next")
N.save()

L = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
L.insert_before("\n## Instruments\n", """
- 2026-10-18, session 1799cb98: NP-24 priced (`build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`). The owner
  chose S3 for SP-1, splitting dDeclaredLoop into itself, dPlacedRequest (Entry) and dKeptSession (Session), and kept
  dCalibratedLens whole for SP-2. Folding S3 found two clauses placed against the gate's own rules. The card moved
  to the early build, and the follow-up rounds stayed in the spine. That left dDeclaredLoop at 22 units,
  dPlacedRequest at 7 and dKeptSession at 18, and the critical path a unit longer than first priced. The gate was
  red on four class rows whose citing clause had moved, until each named dKeptSession.
""", "event")
L.save()
````

### `fix_split_wording.py`

The `[folded]` class-row line, reworded to tell the owner row from the four citing rows.

````python
"""The pricing record's [folded] class-row line: one row's owner moved and four rows' citing build moved, which the
first wording counted as five alike. Usage: python -X utf8 fix_split_wording.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

PR = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md")
PR.sub("- **The re-cut's class rows:** the five whose citing clause moved now name dKeptSession. The gate read the old rows as\n"
       "  needing no dependency, and the moved citations as unclassed, until they did.",
       "- **The re-cut's class rows:** `preset`'s row names dKeptSession as the key's owner. The four rows whose citing\n"
       "  clause moved name it as the citing build. The gate read those four as needing no dependency, and the moved\n"
       "  citations as unclassed, until they did.", "class rows")
PR.save()
````

### `critical_path.py`

The critical path over v2's `[chain]`, run by `[final]`. SP-1 raised its build count to 18.

````python
"""The chain's critical path: the longest chain of builds by planned units, over v2's [chain] after relation, and
what each candidate edge would add to it.

Usage: python critical_path.py [--edge <child>:<parent> ...]   (from the worktree root)

A build's units are its planned-units cell's clauses, counted as the map counts them (split on "; "). A build
starts when every parent has landed, so the path's length is the largest sum of units along a parent chain.
"""
import re
import sys

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
units, parents = {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        units[m.group(1)] = len([u for u in m.group(3).split("; ") if u.strip()])
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in
                               re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)]
assert len(units) == 20, len(units)   # 16 until SP-1, 18 until WK-4 split dTotalRecall and dBoundRoles, 2026-10-18


def longest(par):
    memo, via = {}, {}

    def f(b, seen=()):
        if b in seen:
            sys.exit(f"cycle through {b}")
        if b not in memo:
            best, arg = 0, None
            for p in par[b]:
                v = f(p, seen + (b,))
                if v > best:
                    best, arg = v, p
            memo[b], via[b] = best + units[b], arg
        return memo[b]

    for b in par:
        f(b)
    end = max(memo, key=memo.get)
    path, b = [], end
    while b:
        path.append(b)
        b = via[b]
    return memo[end], list(reversed(path)), memo


base, path, memo = longest(parents)
print(f"critical path: {base} units, {' > '.join(path)}")
print("each build's earliest finish, in units: " + ", ".join(f"{b} {memo[b]}" for b in sorted(memo, key=memo.get)))
for arg in [a for a in sys.argv[1:] if ":" in a]:
    child, parent = arg.split(":")
    par = {b: list(ps) for b, ps in parents.items()}
    par[child] = par[child] + [parent]
    length, p, _ = longest(par)
    print(f"with {child} after {parent}: {length} units ({length - base:+d}), {' > '.join(p)}")
````

### `record_walk2.py`

The walk derived again: the owner's words, `[chain-2]`, `[wave-1-2]` and `[walk-instrument-2]` in the walk record.

````python
"""Write the walk's re-derivation: the owner's words, `[chain-2]` (the glance over eighteen builds), `[wave-1-2]` (wave 1
presented again) and `[walk-instrument-2]` (the scripts and their runs), and point the first glance at them.

Usage: python -X utf8 record_walk2.py <facts.out> <since.out> <path.out>   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
FENCE = "`" * 3


def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")


facts, since, path = (read(p) for p in sys.argv[1:4])
W = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("""## [chain] The chain at a glance
""", """- Asked to resume after the night pass, the owner's answers and the spine's split, the owner said, verbatim:
  "re-derive the walk and present wave 1" (2026-10-18). The glance and wave 1 are derived again in `[chain-2]` and
  `[wave-1-2]`.

## [chain] The chain at a glance
""", "words")
W.insert_before("## [walk-instrument] The walk's facts, and the clause scan", """## [chain-2] The chain at a glance, derived again

Derived at `b3866c4ad`, after the night pass, the owner's answers and the spine's three-way split
(`build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`). The facts are the runs `[walk-instrument-2]` holds.

- **Eighteen builds,** ordered by when each can finish, in planned units: dGroundRules 8; dFairHearing 20;
  dOrderedCharter 35; dDeclaredLoop 57; dPlacedRequest 64; dWitnessedBar 79; dKeptSession 82; dBoundRoles 113;
  dTotalRecall 119; dIndexedDesign 131; dRankedPlan 132; dWellOiledMachine 150; dScopedBuild 161; dTendedCadence 164;
  dMindYourWords 167; dShippedRelease 171; dCalibratedLens 175; dConvergedCharter 189.
- **The critical path, 189 units at `b3866c4ad`:** dGroundRules, dOrderedCharter, dDeclaredLoop, dWitnessedBar,
  dTotalRecall, dWellOiledMachine, dTendedCadence, dCalibratedLens and dConvergedCharter. Its tail now runs through
  Maintain and Review, not dShippedRelease, since the night pass grew both.
- **Since the first glance:** the chain grew from 285 units to 334, with the night pass and the owner's answers. Its
  critical path went from 181 at `beda01950` to 214, and then fell to 189 at `b3866c4ad` with the split.
- **The waves,** grouped as first presented, the two new builds joining wave 1, where their units were:
  1. the foundation and the spine: dGroundRules, dOrderedCharter, dFairHearing, dDeclaredLoop, dPlacedRequest and
     dKeptSession;
  2. dWitnessedBar, dBoundRoles, dTotalRecall, dIndexedDesign and dRankedPlan;
  3. dWellOiledMachine, dScopedBuild, dTendedCadence and dMindYourWords;
  4. dCalibratedLens, dShippedRelease and dConvergedCharter.

## [wave-1-2] The foundation and the spine, presented again

### dGroundRules: Policy

First of all, 8 units, finishing at 8 of 189. It owns `policy.on-invalid` and closes gap-spine-06 (HIGH, the
policy sprawl).
- **The policy file:** `.governance/policy.toml`, its schema, its one reader and its JSON mirror, here so that both
  roots read policy from a build ahead of them (RC-1).
- **How a key resolves:** an override in the file, then the named preset once dKeptSession adds presets, then the
  catalogue default. An absent file reads defaults. A malformed file or an out-of-set value reads the last valid
  landed revision, or refuses (AF-2). Every consumer reads the landed revision, never the working tree (FM1).
- **A minimal guard:** owner-only writes to the policy file, its mirror and the instruction manifest, until
  dDeclaredLoop's full guard lands.
- **The legacy homes:** kit confs, `gate-env.sh` and the roles' house policy, on a shrink-only list derived from the
  files, and an arm red when a landed build's key has no reader.
- **Since first presented:** one word. Presets now come from dKeptSession, so until it lands at 82 a key resolves
  from the file straight to the catalogue default.
- **To look at:** it is still pure plumbing.

### dOrderedCharter: Foundation, the instruction layer

After dGroundRules, 27 units, finishing at 35. It owns 14 keys, the `exception` and `override` kinds, the tags and
instruction-writing systems and 9 tag namespaces, and closes 24 gaps, 12 of them HIGH.
- **The charter as the loop's front door:** its level-0 envelope (precedence and override, the instruction map, one
  line per practice, the hand-off to the loop, the project block) and the drive section from kit descriptors. It is
  held inside 32 KiB and re-injected on compact and resume.
- **The instruction system:**
  - the unit registry, schema and grammar;
  - one renderer, absorbing the playbook, roles and agent-instructions wiring;
  - the ladder renumbered 0 to 7, and load sets budgeted per reader and harness;
  - the guarded instruction manifest;
  - memory instructing nothing;
  - practices rendered per step into work orders.
- **The core that cannot be built around (P16):** the principle registry and meta-check, the kinds register, the
  conformance-gate contract, the exception register and `core.*` policies, and the factories for units, practices,
  Skills and layers.
- **The tag system and the relational syntax (P33):**
  - namespaced tags, a derived index and one resolver;
  - the closed edge registry, twelve types declared and `cites` derived;
  - `gov tag bundle`, a manifest of ranges or, by flag, the content inlined (NP-14);
  - new text citing `path#symbol` or a blob-pinned line, not file:line (NP-17).
- **Layers and P28:** the layer register and contract, and the check that the core never depends on an expansion or
  an optional part, over every edge kind. Today's edges are each made a declared slot or moved into the core.
- **The build's card** delivered at level 1, through a per-worktree file the charter imports.
- **Since first presented:** five units, all from the night pass.
  - The drive section says a build runs unattended by default from its request, and the `[land]` rule reads
    through the request's mandate (point 1).
  - The edge registry, `gov tag bundle` and the citation rule (point 4).
  - Each role's load set budgets the `code` slot (point 3).

  Three gaps came with them, gap-found-24 to gap-found-26.
- **To look at:**
  - It sits right after policy on the critical path. Half its gaps are HIGH, since the instruction layer is where
    gov's sprawl lives.
  - Its units are uneven. The core-independence check (clause 16) and the tag system (clause 19) each read like
    several units of work, so its count understates it. Spec time is the place to cut them.

### dFairHearing: the review harness

After dGroundRules and beside dOrderedCharter, 12 units, finishing at 20. It owns the harness's four items
(`review.pin`, `review.lens`, `review.refute`, `review.report`), `review.opt-in`, `review.unclassed` and
`review.twin`, and the `review` kind, and closes 10 gaps.
- **The owed replays first:** the design-audit preset run blind on a frozen history, scored against 59 known defects.
- **The preset:** five lenses for design records. They are coherence, grounding, reuse held to precedent, the failure
  envelope extended to trust boundaries, and alternatives and cost.
- **Opt-in lenses** (security, alternatives, cost, portability, adopter migration, topology), each swapped for a named
  default lens.
- **The panel:**
  - skeptic batches sorted by address;
  - duplicates counted as merged confirmations;
  - grades per id;
  - refuted claims and twins flagged to the synthesizer;
  - fix verdicts by class;
  - one disposition per confirmed finding.
- **The review records** realigned with the code, and the twin merge when the owner opts in (RS-1).
- **Since first presented:** one unit, the scorer factory (night pass, point 2). It is one deterministic scorer that
  re-derives every figure from raw outputs, extracted from `review_replay.py` with aScoutedSeam's grader as its second
  instance. gap-test-18 came with it.
- **To look at:**
  - It must land before dDeclaredLoop, whose breakpoints call it (AF-1), and does, at 20 against 35.
  - Its security lens now has a second caller, Maintain's weekly security review (NP-19).

### dDeclaredLoop: Spine, the loop

After dOrderedCharter and dFairHearing, 22 units, finishing at 57. Seven builds wait on it: dPlacedRequest,
dKeptSession, dWitnessedBar, dBoundRoles, dTotalRecall, dRankedPlan and dIndexedDesign. It owns 12 items, 19 keys,
4 kinds and 4 tag namespaces, and closes 10 gaps, 6 of them HIGH.
- **The loop:**
  - the loop kit, keyed by stage tags;
  - each step a program of declared items, named by semantic tags;
  - one transition table per level, backward transitions recorded, and an engine refusing any transition it lacks;
  - terminal states, a default failure route and one closed disposition set;
  - stage claims and the coverage gate;
  - the `step`, `item`, `policy` and `command` namespaces.
- **Witnesses and position:**
  - witnesses computed, never typed, a probe's commands among them, re-run at its pinned SHA;
  - the position engine, deriving step, next item and interrupts from witnesses;
  - claims keyed and trusted by key and source.
- **Policy machinery:** the guard, the TTY CLI and the default floor, and the factories and conformance gates for
  commands, keys, presets, stages, hooks, roles and workflows.
- **Review control flow (AF-1):**
  - breakpoints at any item boundary, with reviews and owner gates one mechanism;
  - the breakpoint program's trigger, disposal, fold and cost;
  - the follow-up and design-audit rounds, with `REVIEW_ROUNDS` retired;
  - the stage-exit recommendation for every step.
- **Since first presented:** split three ways (SP-1, S3).
  - It keeps the loop's core and the review control flow. Test's stage items run through that control flow, and
    `review.dispose` reads the follow-up rounds' key.
  - Twenty-one of its first 43 units moved to dPlacedRequest and dKeptSession, and so did the night pass's four
    additions.
- **To look at:**
  - It finishes at 57, not 73. Of the seven builds that wait on it, dWitnessedBar is the one on the critical path.
  - The review control flow is now its heaviest part: four units carrying eleven keys.

### dPlacedRequest: Entry, new

After dDeclaredLoop, 7 units, finishing at 64. dKeptSession, dBoundRoles and dTotalRecall wait on it. It owns the
five entry items and the probe program's seven, 17 keys, and the `card`, `lease` and `probe` kinds. It closes 8 gaps,
6 of them HIGH.
- **Leases:**
  - one lease grammar for builds, units and cadence runs, with epochs bumped at every take-over;
  - run claims migrated onto it, and overlap warned or refused;
  - fleet identity checked against the remote, and offline behaviour as `leases.offline` defines.
- **The card:** at level 1, a ref per build on the remote, cached in the clone, snapshotted and re-keyed on resume,
  with `resume.context` and `resume.partial`.
- **Entry:** the entry step's items (orientation, the three placing items and the claim), and the placement predicate
  and its check. An unattended prompt is placed the same way.
- **What each item carries:** its `map` slot declarations and its code seed (point 3).
- **The probe program:** seven items and the `probe` kind, placed at any boundary or raised by any role, with
  stand-ins until the tester and the experiment shape land (point 2).
- **To look at:**
  - Six HIGH gaps rest on seven units. Orientation and concurrency are where today's sessions lose most, so the
    leases and the card each carry several units of work.
  - It has slack. It lands at 64, and dBoundRoles and dTotalRecall cannot start before dWitnessedBar lands at 79. It
    can grow by 15 units at spec time without moving the path.

### dKeptSession: Session, new

After dDeclaredLoop and dPlacedRequest, 18 units, finishing at 82. dWellOiledMachine and dIndexedDesign wait on it.
It owns 12 keys and the `mailbox message` kind, and closes 3 gaps, 2 of them HIGH.
- **Presets:** the named presets and their completeness check, the preset step in dGroundRules's reader, the
  charter's preset section, and policy at govkit intake.
- **Coordination:** the mailbox per build, read at every item boundary; live delivery where the harness has it; and
  dependency coordination through the parent's lease.
- **Sessions:**
  - orientation cost recorded per stage;
  - progress reported through `notify.owner`;
  - a fresh session recommended until the card-import fixture passes;
  - the card's pointers;
  - what a session does as its window fills;
  - compaction summaries read as leads.
- **Attendance and `repeat`** (point 1): the attendance rule, which never selects an actor, the driver or a binding,
  and the `repeat` disposition onto a playbook.
- **Two small units:** `actions.free` at the tool call, and the policy namespaces' purposes reviewed.
- **To look at:**
  - It is grouped by when its parts are needed, not by theme. That is the split's price.
  - Until it lands at 82, only the `standard` preset works, no mailbox carries notices, and attendance is not yet a
    key.
  - It has the most slack in the wave. Nothing that waits on it starts before 119.

""", "chain-2 and wave-1-2")
W.text = W.text.rstrip("\n") + f"""

## [walk-instrument-2] The walk derived again, at `b3866c4ad`

`walk_facts.py` and `critical_path.py` as above, the latter's build count raised to 18 by the split. What changed
since the first presentation is `since.py`'s:

{FENCE}python
{read(HERE / "since.py")}
{FENCE}

{FENCE}text
$ python walk_facts.py dGroundRules dOrderedCharter dFairHearing dDeclaredLoop dPlacedRequest dKeptSession
{facts}
$ python critical_path.py
{path}
$ python since.py beda01950 dGroundRules dOrderedCharter dFairHearing dDeclaredLoop
{since}
{FENCE}
"""
W.done += 1
W.save()
````

### `fix_walk2.py`

Three corrections to the re-derivation, each checked against the records first.

````python
"""Three corrections to the walk's re-derivation, each checked against the records before it was made:
- the review control flow carries twelve keys: `autonomy`, `review.<stage>`, `review.breakpoints`, the program's four,
  the rounds' three and the recommendation's two, all still dDeclaredLoop's in v2's catalogue;
- the tail moved because the night pass and the owner's answers both grew dTendedCadence, and the night pass dCalibratedLens;
- the critical path's 214 is pinned to the commit it was read at.

Usage: python -X utf8 fix_walk2.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

W = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("  - The review control flow is now its heaviest part: four units carrying eleven keys.",
      "  - The review control flow is now its heaviest part: four units carrying twelve keys.", "twelve")
W.sub("Its tail now runs through\n  Maintain and Review, not dShippedRelease, since the night pass grew both.",
      "Its tail now runs through\n  Maintain and Review, not dShippedRelease, since the night pass and the owner's "
      "answers grew both.", "tail")
W.sub("critical path went from 181 at `beda01950` to 214, and then fell to 189 at `b3866c4ad` with the split.",
      "critical path went from 181 at `beda01950` to 214 at `1d32760f3`, and then fell to 189 at `b3866c4ad` with the\n"
      "  split.", "214 pin")
W.save()
````

### `stage_actors.py`

Wave 2: the stage items acted by a role no agent plays today, against the chain's order of dBoundRoles.

````python
"""Each stage item whose actor no agent plays today, with the stage's build and whether dBoundRoles, which binds the roles,
is an ancestor of it. An item listed with "no" acts through a role nothing provides before that build starts, unless
its records declare a stand-in.

Usage: python -X utf8 stage_actors.py   (from the worktree root)
It reads flow-steps' item rows (actor, owner), v2's [chain] (stages, parents) and tools/roles/agents/ (today's agents).
It does not read stand-ins; the probe program's are declared in flow-steps' [probe], and the walk names the others.
"""
import pathlib
import re

B = "memory/builds/dClosedLoop/build/"
fs = open(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md", encoding="utf-8").read()
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
parents, stage_build = {}, {}
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        parents[m.group(1)] = [p.strip() for p in m.group(3).split(",") if p.strip() in names]
        stage_build[m.group(2).strip().lower()] = m.group(1)


def ancestors(b, acc=None):
    acc = set() if acc is None else acc
    for p in parents[b]:
        if p not in acc:
            acc.add(p)
            ancestors(p, acc)
    return acc


today = {re.sub(r"^gov-|\.agent\.md$", "", p.name).replace("-", " ")
         for p in pathlib.Path("tools/roles/agents").glob("*.agent.md")}
ROLE_AGENT = {"spec writer": "spec writer", "builder": "builder", "researcher": "researcher", "reuse scout": "reuse scout",
              "orientation scout": "orienter", "reviewer": "diff reviewer", "skeptic": "skeptic",
              "synthesizer": "synthesizer"}
print(f"today's agents: {', '.join(sorted(today))}")
rows = 0
for m in re.finditer(r"^## \[([a-z-]+)\][^\n]*\n(.*?)(?=^## |\Z)", fs, flags=re.M | re.S):
    step = m.group(1)
    if step not in stage_build:
        continue
    for ln in m.group(2).split("\n"):
        c = [x.strip() for x in ln.strip().strip("|").split(" | ")]
        if not ln.startswith("| `") or len(c) != 7:
            continue
        actor = re.split(r"[,:]", c[1])[0].strip()   # the role, its qualifiers ("one per unit", "under ...") dropped
        if actor in ("command", "executor", "owner", "hook") or ROLE_AGENT.get(actor) in today:
            continue
        sb = stage_build[step]
        bound = "yes" if "dBoundRoles" in ancestors(sb) or sb == "dBoundRoles" else "no"
        rows += 1
        print(f"{step:7} {c[0]:22} actor {actor:12} owner {c[6]:15} stage build {sb:15} after dBoundRoles: {bound}")
print(f"stage items acted by a role no agent plays today: {rows}")
````

### `record_walk3.py`

The owner's word on wave 1, and wave 2 presented with its three forks.

````python
"""Record the owner's word on wave 1 and present wave 2: `[wave-2]`, `[wave-2-forks]` and `[walk-instrument-3]`.

Usage: python -X utf8 record_walk3.py <facts.out> <since.out> <actors.out>   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
FENCE = "`" * 3


def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")


facts, since, actors = (read(p) for p in sys.argv[1:4])
W = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("""  `[wave-1-2]`.

## [chain] The chain at a glance
""", """  `[wave-1-2]`.
- The owner's word on wave 1, 2026-10-18, verbatim: "approve wave 1, present wave 2".

## [chain] The chain at a glance
""", "words")
W.insert_before("## [walk-instrument] The walk's facts, and the clause scan", """**The owner's word:** approved, 2026-10-18 (`[words]`).

## [wave-2] The stage and memory builds, as presented

Derived at `9b4386707`, whose chain is `b3866c4ad`'s. Each build's "since the walk opened" reads its row against
`beda01950`, the commit the walk opened at.

### dWitnessedBar: Test

After dDeclaredLoop, 22 units, finishing at 79. Six builds wait on it: dBoundRoles, dTotalRecall, dMindYourWords,
dScopedBuild, dShippedRelease and dTendedCadence. It owns 9 items, 15 keys, 6 kinds, the retrofit system and 3 tag
namespaces, and closes 20 gaps, 6 of them HIGH.
- **The verdict:**
  - gate health measured against a reliability bar;
  - bypasses recorded;
  - attribution deciding what blocks;
  - the runner-written verdict the pre-push hook reads;
  - held legs by policy, and the peer-node verifier;
  - seen-red records and flake quarantine.
- **Tests as a product contract:** runner adapters, a derived pre-commit list, and multi-node cost evidence.
- **Legs:**
  - the gate-leg factory and its conformance gate, each leg declaring the principles it enforces;
  - the `leg`, `check` and `pack` namespaces;
  - each leg's purpose, today's 140 reviewed;
  - `tests=` and `enforces=` edges on legs.
- **The retrofit's ledger:** the baseline ledger factory (shrink-only debt, append-only history, declared set or
  ceiling), the `ratchet` pack and `test.seed` at registration. Gov's own 27 registries, pins and legacy lists move
  onto it.
- **A fix pass keeps its check** (night pass, point 6). A fix pass may not edit the red leg's own tests or gate
  script. A change there routes through the tester's wrong-spec judgment to Design as a new unit.
- **Since the walk opened:** two units from the night pass, the fix-pass rule and the leg edges, and gap-test-19.
- **To look at:**
  - It is the one stage build that lands before dBoundRoles binds the roles, and its stage names the tester three
    times: `test.attribute`, `test.reason` and the fix pass's judgment. No agent plays the tester today, and none
    until dBoundRoles lands at 113. The probe program declares a stand-in for the same gap, and Test declares none.
    That is W2-1.
  - The reliability bar is what lets `strict` and `guarded` refuse hook bypass without stalling (R5.1).

### dBoundRoles: Roles

After dDeclaredLoop, dWitnessedBar and dPlacedRequest, 34 units, finishing at 113. dWellOiledMachine and
dShippedRelease wait on it. It owns 20 keys, the `work order` kind, the role-shapes system and 2 tag namespaces, and
closes 25 gaps, 11 of them HIGH.
- **The roster:** twelve core roles, the tester among them, and the deployer and maintainer as expansion roles,
  defined by dShippedRelease and dTendedCadence.
- **The work order:**
  - rendered per item, hashed into the spawn marker and bound to its act;
  - memory slices, code-notes and legacy slots, each under its own budget;
  - the `map` slot, the `code` slot from each item's seed, and instruction units selected by `feature.*`, each
    "not installed" until dTotalRecall lands.
- **Roles as enforced fields:**
  - static instructions as fields, every limit paired with its enforcer;
  - returns through a schema-forced channel;
  - the role index beyond workers' reach;
  - shell writes held to the allowance;
  - write classes enforced.
- **Trust and repairs (P29):** inputs handed as content, each fact keyed and classed by the executor, trust profiles,
  the answered-call hook, and repairs filed as asks against the producer's record.
- **Who composes what:** the prompt writer composes every role's task, and the orientation scout composes the card
  and its map cell.
- **Shapes:** `single`, `per-unit`, `panel`, `twin` and `experiment`, each with its fan, checklist, merge and an agent
  cap.
- **Since the walk opened:** four units from the night pass, with the `experiment` shape, and gap-roles-21 and
  gap-roles-22:
  - the tester agent and the `probe` outcome on every return;
  - owner questions asked live while attended;
  - the `code` slot;
  - the `feature` selector and the code-notes slot from a tag's bundle.
- **To look at:**
  - Three of its slots render "not installed" until dTotalRecall lands, six units after it.
  - It binds the planner and the architect, whose items run dRankedPlan's and dIndexedDesign's stages, yet neither
    build follows it. That is W2-2.
  - 11 of its 25 gaps are HIGH. The roles layer is where P25, role work only in role agents, is enforced.

### dTotalRecall: Memory

After dDeclaredLoop, dWitnessedBar and dPlacedRequest, 40 units, finishing at 119. Four builds wait on it:
dWellOiledMachine, dRankedPlan, dIndexedDesign and dShippedRelease. It owns 4 items, 25 keys, 16 kinds, 3 systems and
5 tag namespaces, and closes 34 gaps, 9 of them HIGH.
- **The memory contract:** the record-kind registry, each kind with its tag, layer, home, id rule, schema, writer,
  readers, lifecycle and check. Templates and checks are generated from it, and one `record` command writes, minting
  ids under the build's claim or lease.
- **Builds and relations:** the README's front-matter schema, the slug and id grammar exported once, typed relations
  checked both ways, and the ask kind's acceptance at filing.
- **Decisions and reuse:**
  - decisions split by kind, reuse entries as level-3 units and a major-decision log;
  - the reuse scout's house index;
  - `reuse_lookup.py` retired, and memory-recall narrowed to a record finder.
- **Finding records:** the extractors, `record find` and `record show` over the one index, the read budget per role
  item, and the default load's memory share.
- **The project map:** the level-0 map, `gov map`, its completeness check, and the atlas from the same node table.
  The map is built only if it wins its replay.
- **Code depth** (P32, night pass):
  - the core `code` record, replacing symbols and callers;
  - `gov code show`, `callers`, `tests` and `where`;
  - enrichment keyed by body hash;
  - the replay extended to code;
  - the ctags pack (NP-10).
- **The relational syntax's memory half** (P33):
  - typed edges from annotations, front matter, dossiers and decision rows;
  - the region-parser factory;
  - the dossier's header becoming the feature node;
  - the `feature` selector armed.
- **The retrofit's memory half:** the `baseline` and `census` kinds, the `origin` field, the `adopt` program, the
  annotations leg and the marker namespace.
- **Since the walk opened:** nine units from the night pass and the owner's answers. The caller map gave way to the
  `code` record, and gap-mem-28 to gap-mem-34 came with them.
- **To look at:**
  - It is the largest build in the chain, 40 units, and all of them sit on the critical path.
  - The nine new units, code depth and the relational syntax's memory half, may not be needed by dWellOiledMachine,
    its successor on the path. If they are not, a split prices as dDeclaredLoop's did. That is W2-3.

### dIndexedDesign: Design

After dDeclaredLoop, dTotalRecall and dKeptSession, 12 units, finishing at 131. dScopedBuild and dTendedCadence wait on
it. It owns 10 items, 4 keys and 10 kinds, and closes 10 gaps, 4 of them HIGH.
- **The hand-off and the index:** the derived-READY hand-off and the design index.
- **Design review by policy,** with its opt-in, effort and audit guard.
- **Evidence:** reuse and alternatives backed by recorded probes, and the research harness on the `experiment` shape.
- **The spec as a contract:**
  - measured, and redesigned as a structured, tagged contract;
  - agreement and tier checks, and sections named by tag;
  - the feature level, each feature's interfaces declared, with two-level re-entry and fork resolution by policy;
  - `implements=` and `decides=` edges, and `design.seams` reading a tag's bundle.
- **Playbooks** (night pass, point 1): the playbook record kind, which is dScriptedRepeat's canon with its pieces and
  sets by hash and `check-playbook` as Design's pack. With it come the playbook set and its set check, registered at
  Test's leg-pack point.
- **Since the walk opened:** three units from the night pass, the playbook kinds and the structured spec's edges. The
  research harness was re-based on the `experiment` shape, and gap-flow-17 came with them.
- **To look at:** its stage's items are the architect's, and its research harness waits on dBoundRoles' `experiment`
  shape. dBoundRoles is not its ancestor (W2-2).

### dRankedPlan: Plan

After dDeclaredLoop and dTotalRecall, 13 units, finishing at 132. dTendedCadence waits on it. It owns 9 items, 6 keys
and 3 kinds, and closes 10 gaps, 5 of them HIGH.
- **Priority and triage:** priority beside `parents:` and the generated plan view, rule-based triage, dormancy
  disposal, and the live-build mapping carried out.
- **The planner's stage:**
  - the planner and triager role and the Plan workflow;
  - Plan Review;
  - kickoff offering the next item, with attended briefs gated;
  - the full kickoff only where `kickoff.runs` says.
- **Ratification:** the session's intake log is read as the request's ratification. Until dWellOiledMachine's hook
  writes it, `plan.exit` falls back to the owner gate.
- **What Plan hands on:**
  - each role item's memory read set, sized at Plan;
  - the probes owed before Design (night pass, point 2);
  - the intent fields: affected systems derived from the `code` record, and open questions as fork tags (point 6).
- **Since the walk opened:** two units from the night pass, and gap-plan-08.
- **To look at:**
  - Until dWellOiledMachine lands, eighteen units after it, every Plan exit waits for the owner. Under unattended by
    default, that is the one owner gate the chain keeps for a while.
  - Its stage's items are the planner's, and dBoundRoles is not its ancestor (W2-2).

## [wave-2-forks] Parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| W2-1 | Who plays the tester before dBoundRoles lands? | a minimal tester agent ships with dWitnessedBar in today's roles kit and dBoundRoles re-founds it with the other roles, one more unit in dWitnessedBar; an owner item stands in, as the probe program's does, so every own or mixed red and every Test exit waits for the owner until dBoundRoles lands; the skeptic stands in, a role doing another's work against P25 | a structural decision |
| W2-2 | Should dIndexedDesign and dRankedPlan follow dBoundRoles? | yes, both: dBoundRoles lands at 113, before either can start at 119, so the edges cost nothing and their stages' roles are bound first; keep them as they are, the stages' roles unplayed until dBoundRoles happens to land | a structural decision about the chain |
| W2-3 | Price a split of dTotalRecall? | price it before wave 3, as NP-24 was; keep it whole | a structural decision about the chain |

""", "wave-2")
W.text = W.text.rstrip("\n") + f"""

## [walk-instrument-3] Wave 2's facts, at `9b4386707`

`walk_facts.py` and `since.py` as above. `stage_actors.py` finds the stage items acted by a role no agent plays today:

{FENCE}python
{read(HERE / "stage_actors.py")}
{FENCE}

Its first run compared whole actor cells, qualifiers included ("builder, one per unit"), and listed 23 items. Matching
each actor's role name before its qualifiers gives the run below.

{FENCE}text
$ python walk_facts.py dWitnessedBar dBoundRoles dTotalRecall dIndexedDesign dRankedPlan
{facts}
$ python since.py beda01950 dWitnessedBar dBoundRoles dTotalRecall dIndexedDesign dRankedPlan
{since}
$ python stage_actors.py
{actors}
{FENCE}
"""
W.done += 1
W.save()
````

### `fix_fork_ids.py`

Wave 2's forks renamed to a family the map counts, under a title the atlas reads as forks.

````python
"""Wave 2's forks were minted as W2-1 to W2-3, which neither instrument reads as forks:
- the map counts ids of the shape [A-Z]{2,3}-\\d{1,2}, a letters-only family, in a record's decision sections;
- the atlas takes a section as a decision section by a tag it lists or a title naming forks, and "[wave-2-forks]
  Parked for the owner" had neither.

So the walk's forks become one family, WK-1 to WK-3, continued by later waves, under a title that names them. One
option's text cited NP-24, which the map would count as a fourth fork of this record, so it now says "the spine's
split". The session log's event carries the new ids. Usage: python -X utf8 fix_fork_ids.py   (from the worktree root)
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
W = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("## [wave-2-forks] Parked for the owner", "## [wave-2-forks] Wave 2's forks, parked for the owner", "title")
W.sub("| price it before wave 3, as NP-24 was; keep it whole |", "| price it before wave 3, as the spine's split was; keep "
      "it whole |", "NP-24 cite")
n = len(re.findall(r"\bW2-([123])\b", W.text))
if n != 8:
    sys.exit(f"walk: expected 8 W2- mentions, found {n}")
W.text = re.sub(r"\bW2-([123])\b", r"WK-\1", W.text)
W.done += 1
W.save()
L = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
L.sub("whom no agent plays today, in stages whose builds do not follow dBoundRoles (W2-1, W2-2). dTotalRecall, the\n"
      "  largest block on the path, may split as dDeclaredLoop did (W2-3).",
      "whom no agent plays today, in stages whose builds do not follow dBoundRoles (WK-1, WK-2). dTotalRecall, the\n"
      "  largest block on the path, may split as dDeclaredLoop did (WK-3). The forks were first minted as W2-1 to W2-3,\n"
      "  which the map does not count as forks, and were renamed before the owner saw them.", "event ids")
L.save()
````

### `fold_wk.py`

The owner's word on wave 2, and WK-1 and WK-2 folded: the minimal tester, and dBoundRoles as a parent of dIndexedDesign and dRankedPlan.

````python
"""Record the owner's word on wave 2 and fold WK-1 and WK-2; WK-3 is priced in its own record.
- WK-1: a minimal tester agent ships with dWitnessedBar in today's roles kit, and dBoundRoles re-founds it.
- WK-2: dIndexedDesign and dRankedPlan follow dBoundRoles, and the research harness's stand-in goes.

Usage: python -X utf8 fold_wk.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
W = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("""- The owner's word on wave 1, 2026-10-18, verbatim: "approve wave 1, present wave 2".
""", """- The owner's word on wave 1, 2026-10-18, verbatim: "approve wave 1, present wave 2".
- The owner's word on wave 2 and its forks, 2026-10-18, verbatim: "approve wave 2, take the recommendations".
""", "words")
W.insert_before("## [walk-instrument] The walk's facts, and the clause scan", """## [wave-2-answers] Wave 2's forks, answered

The owner approved wave 2 and took each fork's recommendation, 2026-10-18 (`[words]`):
- **WK-1:** a minimal tester agent ships with dWitnessedBar in today's roles kit, and plays `test.attribute`,
  `test.reason` and the fix pass's judgment. dBoundRoles re-founds it with the other roles. dWitnessedBar gains a
  unit, and the critical path with it.
- **WK-2:** dIndexedDesign and dRankedPlan follow dBoundRoles, so their stages' roles are bound before they start.
  The research harness builds on the `experiment` shape outright, and its stand-in is gone.
- **WK-3:** a split of dTotalRecall is priced before wave 3, in
  `build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md`.

""", "wave-2 answers")
W.save()

V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
V.insert_before("\nRevised: 2026-10-17, after the folds' closing review", """
Revised: 2026-10-18, the walk's wave 2 (`build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md` `[wave-2-answers]`):
- dWitnessedBar ships a minimal tester agent, which dBoundRoles re-founds with the other roles (WK-1);
- dIndexedDesign and dRankedPlan follow dBoundRoles, and the research harness builds on the `experiment` shape
  outright (WK-2).
""", "revision note")
V.sub("(night pass, point 4) | gap-test-01,",
      "(night pass, point 4); a minimal tester agent in today's roles kit, its allowance scratch only, playing "
      "`test.attribute`, `test.reason` and the fix pass's wrong-spec judgment until dBoundRoles re-founds it with the "
      "other roles (WK-1) | gap-test-01,", "dWitnessedBar tester")
V.sub("the tester agent, absent today, with its allowance",
      "the tester agent, re-founded from dWitnessedBar's minimal one (WK-1), with its allowance", "dBoundRoles tester")
V.sub("| dIndexedDesign | Design | dDeclaredLoop, dTotalRecall, dKeptSession |",
      "| dIndexedDesign | Design | dDeclaredLoop, dTotalRecall, dKeptSession, dBoundRoles |", "dIndexedDesign parents")
V.sub("| dRankedPlan | Plan | dDeclaredLoop, dTotalRecall |",
      "| dRankedPlan | Plan | dDeclaredLoop, dTotalRecall, dBoundRoles |", "dRankedPlan parents")
V.sub("the research harness, built on the `experiment` shape once dBoundRoles registers it, and run as today until then "
      "(night pass, point 2)",
      "the research harness, built on dBoundRoles' `experiment` shape (night pass, point 2, and WK-2)", "research harness")
V.save()

FS = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
FS.insert_before("- **Test is the landing verdict; testing elsewhere is a probe**", """- **The tester before dBoundRoles** (WK-1). Until dBoundRoles re-founds the roles, dWitnessedBar's minimal tester
  agent plays `test.attribute`, `test.reason` and the fix pass's judgment, its allowance scratch only.
""", "test tester")
FS.sub("  - dBoundRoles' tester and `experiment` shape: `probe.design` and `probe.experiment` route to an owner item;",
       "  - the tester, dWitnessedBar's minimal one first (WK-1), and dBoundRoles' `experiment` shape: until each lands,\n"
       "    `probe.design` and `probe.experiment` route to an owner item;", "probe stand-in")
FS.save()
````

### `gap_texts.py`

WK-4: each build's gaps with grade and text, to assign them across the split.

````python
"""Print each named build's gaps, ranges expanded, with their grade and text, to assign them across a split.

Usage: python -X utf8 gap_texts.py <build> [<build> ...]   (from the worktree root)
"""
import re
import sys

B = "memory/builds/dClosedLoop/build/"
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
reg = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md", encoding="utf-8").read()
text = {m.group(1): (m.group(2), m.group(3).strip())
        for m in re.finditer(r"(?m)^\| (gap-[a-z]+-\d\d) \| [^|]+ \| (HIGH|MED|LOW) \| ([^|]+) \|", reg)}
for b in sys.argv[1:]:
    row = next(ln for ln in v2.split("\n") if ln.startswith(f"| {b} |"))
    cell = row.strip().strip("|").rsplit(" | ", 1)[1]
    gaps = []
    for g in [x.strip() for x in cell.split(",")]:
        m = re.match(r"(gap-[a-z]+)-(\d\d) to gap-[a-z]+-(\d\d)", g)
        gaps += [f"{m.group(1)}-{i:02d}" for i in range(int(m.group(2)), int(m.group(3)) + 1)] if m else [g]
    print(f"=== {b}: {len(gaps)} gaps, cell: {cell}")
    for g in gaps:
        s, t = text.get(g, ("?", "?"))
        print(f"{g} [{s}] {t[:180]}")
````

### `price_wk3_asked.py`

WK-3's pricing as the owner was asked from.

````python
"""WK-3: price a split of dTotalRecall, alone and with dBoundRoles, as critical paths over v2's [chain].

Usage: python -X utf8 price_wk3.py   (from the worktree root)

Units and paths as price_split.py counts them. dWellOiledMachine, the build after dTotalRecall on the critical path,
waits for dBoundRoles too, so a dTotalRecall split saves no more than dBoundRoles' landing allows. The tables below say
which units dWellOiledMachine needs, joining the gate's reading (node_users.py found no backticked dependency of it on
either build) and a plain-word reading of its 31 clauses, each reason stated. A split loses if dWellOiledMachine waits
for a moved part.
"""
import re

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
units, parents, clauses = {}, {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        clauses[m.group(1)] = [u for u in m.group(3).split("; ") if u.strip()]
        units[m.group(1)] = len(clauses[m.group(1)])
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]
assert len(units) == 18, len(units)


def path(units, parents):
    finish, via = {}, {}

    def fin(b):
        if b not in finish:
            best = max(parents[b], key=fin, default=None)
            via[b] = best
            finish[b] = units[b] + (fin(best) if best else 0)
        return finish[b]

    end = max(units, key=fin)
    chain_, b = [], end
    while b:
        chain_.append(b)
        b = via[b]
    return finish[end], list(reversed(chain_)), finish


TR, BR, WOM = "dTotalRecall", "dBoundRoles", "dWellOiledMachine"
# dTotalRecall's units dWellOiledMachine needs, or that every later build rests on, and why.
TR_KEEP = {
    1: "the record-kind registry, where dWellOiledMachine registers its journal, act, return and binding kinds",
    2: "the `record` command, through which the supervisor alone writes shared records",
    3: "ids minted outside a build, for intake that reaches no owner session and for cadence filers",
    4: "the work order as each agent's root, where every act session starts",
    5: "the slug and id grammar every reader reads",
    6: "typed relations, the dependency graph waits and landings read",
    7: "the ask kind's acceptance at filing, kept so Plan's triage reads asks from the spine's memory alone",
    16: "record find and show, the read budget, and the default load's memory share the session-start hook loads",
    23: "derived anchors, part of the extractors",
    24: "the shape-run kind, whose rows dWellOiledMachine writes for each act",
    25: "the acceptance re-measure over every read channel, the runtime's among them",
    26: "the shared extraction primitive the map calls",
    28: "the level-0 map the session-start hook loads",
    29: "the map's completeness check and leg pack",
    31: "the purposes the map renders at level 0",
    32: "the replay that decides whether the map is built, and so whether dWellOiledMachine loads it",
}
CODE = 11   # the `code` record: dRankedPlan's intent fields and dCalibratedLens cite it
# dBoundRoles' units dWellOiledMachine needs, and why.
BR_KEEP = {
    1: "the roster, whose roles the act sessions run",
    2: "each role's structured instructions and ceilings, loaded into its act session",
    3: "the work order bound to its act by task-sha, which act binding checks",
    4: "the prompt writer, which composes every act's task",
    6: "returns through a schema-forced channel, which the persisted-return store keeps",
    7: "the role index and `role-sha` compared at spawn",
    8: "shell writes held to the allowance inside an act session",
    10: "the write classes enforced inside an act session",
    11: "`driver.reads`, `prompts.author` and `roles.no-spawn`, which the supervisor reads as the driver",
    12: "forks held as `run.on-owner-question` says, which the driver applies",
    16: "the driver recording the placement disposition, which dWellOiledMachine re-points to the intake record",
    17: "the trust mechanism, re-cut fresh at act launch",
    24: "the `role` and `field` namespaces the structured fields use",
    25: "the static block carried once per spawn",
    26: "the shapes, whose digest act binding checks, and the experiment shape's acts",
}
assert set(TR_KEEP) <= set(range(1, units[TR] + 1)) and set(BR_KEEP) <= set(range(1, units[BR] + 1))
TR_USERS = {"dIndexedDesign", "dScopedBuild", "dShippedRelease", "dTendedCadence", "dMindYourWords", "dCalibratedLens",
            "dConvergedCharter"}   # the reuse index, decisions, annotations, retrofit, views and the code depth
BR_USERS = {"dScopedBuild", "dShippedRelease", "dTendedCadence", "dMindYourWords", "dCalibratedLens",
            "dConvergedCharter"}   # the work order's slots, metrics, trust profiles and the answered-call hook


def split(u, p, x, first, users):
    u, p = dict(u), {b: list(v) for b, v in p.items()}
    rest = units[x] - len(first)
    u[x] = len(first)
    u[x + "-B"] = rest
    p[x + "-B"] = [x]
    for b in users:
        if x in p.get(b, []) or any(x in p[q] for q in p.get(b, [])):
            p[b] = p[b] + [x + "-B"]
    return u, p


base, base_path, fin0 = path(units, parents)
print(f"baseline: {base} units, {' > '.join(base_path)}")
print(f"{WOM} starts when its last parent lands: " +
      ", ".join(f"{q} {fin0[q]}" for q in sorted(parents[WOM], key=lambda q: -fin0[q])))
RESULTS = []
for label, parts in (
        ("T1, dTotalRecall alone: what dWellOiledMachine does not need leaves, the code record with it",
         [(TR, set(TR_KEEP), TR_USERS | {"dRankedPlan"})]),
        ("T2, dTotalRecall alone, the code record kept", [(TR, set(TR_KEEP) | {CODE}, TR_USERS)]),
        ("C1, both: each build's parts dWellOiledMachine does not need leave, the code record with them",
         [(TR, set(TR_KEEP), TR_USERS | {"dRankedPlan"}), (BR, set(BR_KEEP), BR_USERS)]),
        ("C2, both, the code record kept", [(TR, set(TR_KEEP) | {CODE}, TR_USERS), (BR, set(BR_KEEP), BR_USERS)])):
    u, p = dict(units), {b: list(v) for b, v in parents.items()}
    for x, first, users in parts:
        u, p = split(u, p, x, first, users)
    n, pth, fin = path(u, p)
    sizes = "; ".join(f"{x} {len(first)} and {x}-B {units[x] - len(first)}" for x, first, _ in parts)
    print(f"{label}: {sizes} · {n} units ({n - base:+d}), {' > '.join(pth)}")
    print("  lands: " + ", ".join(f"{b} {fin[b]}" for b in sorted(fin, key=fin.get)
                                  if b in (TR, BR, TR + '-B', BR + '-B', WOM, 'dRankedPlan', 'dIndexedDesign')))
    RESULTS.append((label, [(x, len(first), units[x] - len(first)) for x, first, _ in parts], len(parts), n, base - n))
````

### `price_wk3.py`

WK-3's pricing as folded: the role-gate escape's fix kept in dBoundRoles' first part.

````python
"""WK-3: price a split of dTotalRecall, alone and with dBoundRoles, as critical paths over v2's [chain].

Usage: python -X utf8 price_wk3.py   (from the worktree root)

Units and paths as price_split.py counts them. dWellOiledMachine, the build after dTotalRecall on the critical path,
waits for dBoundRoles too, so a dTotalRecall split saves no more than dBoundRoles' landing allows. The tables below say
which units dWellOiledMachine needs, joining the gate's reading (node_users.py found no backticked dependency of it on
either build) and a plain-word reading of its 31 clauses, each reason stated. A split loses if dWellOiledMachine waits
for a moved part.
"""
import re

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
units, parents, clauses = {}, {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        clauses[m.group(1)] = [u for u in m.group(3).split("; ") if u.strip()]
        units[m.group(1)] = len(clauses[m.group(1)])
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]
assert len(units) == 18, len(units)


def path(units, parents):
    finish, via = {}, {}

    def fin(b):
        if b not in finish:
            best = max(parents[b], key=fin, default=None)
            via[b] = best
            finish[b] = units[b] + (fin(best) if best else 0)
        return finish[b]

    end = max(units, key=fin)
    chain_, b = [], end
    while b:
        chain_.append(b)
        b = via[b]
    return finish[end], list(reversed(chain_)), finish


TR, BR, WOM = "dTotalRecall", "dBoundRoles", "dWellOiledMachine"
# dTotalRecall's units dWellOiledMachine needs, or that every later build rests on, and why.
TR_KEEP = {
    1: "the record-kind registry, where dWellOiledMachine registers its journal, act, return and binding kinds",
    2: "the `record` command, through which the supervisor alone writes shared records",
    3: "ids minted outside a build, for intake that reaches no owner session and for cadence filers",
    4: "the work order as each agent's root, where every act session starts",
    5: "the slug and id grammar every reader reads",
    6: "typed relations, the dependency graph waits and landings read",
    7: "the ask kind's acceptance at filing, kept so Plan's triage reads asks from the spine's memory alone",
    16: "record find and show, the read budget, and the default load's memory share the session-start hook loads",
    23: "derived anchors, part of the extractors",
    24: "the shape-run kind, whose rows dWellOiledMachine writes for each act",
    25: "the acceptance re-measure over every read channel, the runtime's among them",
    26: "the shared extraction primitive the map calls",
    28: "the level-0 map the session-start hook loads",
    29: "the map's completeness check and leg pack",
    31: "the purposes the map renders at level 0",
    32: "the replay that decides whether the map is built, and so whether dWellOiledMachine loads it",
}
CODE = 11   # the `code` record: dRankedPlan's intent fields and dCalibratedLens cite it
# dBoundRoles' units dWellOiledMachine needs, and why.
BR_KEEP = {
    1: "the roster, whose roles the act sessions run",
    2: "each role's structured instructions and ceilings, loaded into its act session",
    3: "the work order bound to its act by task-sha, which act binding checks",
    4: "the prompt writer, which composes every act's task",
    6: "returns through a schema-forced channel, which the persisted-return store keeps",
    7: "the role index and `role-sha` compared at spawn",
    8: "shell writes held to the allowance inside an act session",
    9: "the role-gate arm's field escape closed, kept while folding C2: allowances leak until it is, and keeping it "
       "costs nothing, since dBoundRoles' first part still lands before dTotalRecall's",
    10: "the write classes enforced inside an act session",
    11: "`driver.reads`, `prompts.author` and `roles.no-spawn`, which the supervisor reads as the driver",
    12: "forks held as `run.on-owner-question` says, which the driver applies",
    16: "the driver recording the placement disposition, which dWellOiledMachine re-points to the intake record",
    17: "the trust mechanism, re-cut fresh at act launch",
    24: "the `role` and `field` namespaces the structured fields use",
    25: "the static block carried once per spawn",
    26: "the shapes, whose digest act binding checks, and the experiment shape's acts",
}
assert set(TR_KEEP) <= set(range(1, units[TR] + 1)) and set(BR_KEEP) <= set(range(1, units[BR] + 1))
TR_USERS = {"dIndexedDesign", "dScopedBuild", "dShippedRelease", "dTendedCadence", "dMindYourWords", "dCalibratedLens",
            "dConvergedCharter"}   # the reuse index, decisions, annotations, retrofit, views and the code depth
BR_USERS = {"dScopedBuild", "dShippedRelease", "dTendedCadence", "dMindYourWords", "dCalibratedLens",
            "dConvergedCharter"}   # the work order's slots, metrics, trust profiles and the answered-call hook


def split(u, p, x, first, users):
    u, p = dict(u), {b: list(v) for b, v in p.items()}
    rest = units[x] - len(first)
    u[x] = len(first)
    u[x + "-B"] = rest
    p[x + "-B"] = [x]
    for b in users:
        if x in p.get(b, []) or any(x in p[q] for q in p.get(b, [])):
            p[b] = p[b] + [x + "-B"]
    return u, p


base, base_path, fin0 = path(units, parents)
print(f"baseline: {base} units, {' > '.join(base_path)}")
print(f"{WOM} starts when its last parent lands: " +
      ", ".join(f"{q} {fin0[q]}" for q in sorted(parents[WOM], key=lambda q: -fin0[q])))
RESULTS = []
for label, parts in (
        ("T1, dTotalRecall alone: what dWellOiledMachine does not need leaves, the code record with it",
         [(TR, set(TR_KEEP), TR_USERS | {"dRankedPlan"})]),
        ("T2, dTotalRecall alone, the code record kept", [(TR, set(TR_KEEP) | {CODE}, TR_USERS)]),
        ("C1, both: each build's parts dWellOiledMachine does not need leave, the code record with them",
         [(TR, set(TR_KEEP), TR_USERS | {"dRankedPlan"}), (BR, set(BR_KEEP), BR_USERS)]),
        ("C2, both, the code record kept", [(TR, set(TR_KEEP) | {CODE}, TR_USERS), (BR, set(BR_KEEP), BR_USERS)])):
    u, p = dict(units), {b: list(v) for b, v in parents.items()}
    for x, first, users in parts:
        u, p = split(u, p, x, first, users)
    n, pth, fin = path(u, p)
    sizes = "; ".join(f"{x} {len(first)} and {x}-B {units[x] - len(first)}" for x, first, _ in parts)
    print(f"{label}: {sizes} · {n} units ({n - base:+d}), {' > '.join(pth)}")
    print("  lands: " + ", ".join(f"{b} {fin[b]}" for b in sorted(fin, key=fin.get)
                                  if b in (TR, BR, TR + '-B', BR + '-B', WOM, 'dRankedPlan', 'dIndexedDesign')))
    RESULTS.append((label, [(x, len(first), units[x] - len(first)) for x, first, _ in parts], len(parts), n, base - n))
````

### `write_wk3.py`

Writes WK-3's pricing record from both runs.

````python
"""Write WK-3's pricing record from price_wk3.py's classification and its run.

Usage: python -X utf8 write_wk3.py <price.out>   (from the worktree root, on the chain as priced)
"""
import importlib.util
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("wk3", HERE / "price_wk3.py")
P = importlib.util.module_from_spec(spec)
_out = sys.stdout
sys.stdout = open(os.devnull, "w")
spec.loader.exec_module(P)
sys.stdout = _out
run = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")
asked = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")
OUT = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md")


def short(b, n):
    c = P.clauses[b][n - 1]
    return c if len(c) <= 90 else c[:87].rsplit(" ", 1)[0] + " …"


def kept(b, d):
    rows = ["| Clause | The unit | Why dWellOiledMachine needs it |", "|---|---|---|"]
    rows += [f"| {n} | {short(b, n).replace('|', '/')} | {why} |" for n, why in sorted(d.items())]
    return "\n".join(rows)


def moved(b, keep):
    return "; ".join(f"{n}, {short(b, n)}" for n in range(1, P.units[b] + 1) if n not in keep)


def listed(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


rows = ["| Candidate | Parts, in units | New builds | Path, in units | Saved |", "|---|---|---|---|---|"]
for label, parts, nb, n, saved in P.RESULTS:
    rows.append(f"| {label.split(':')[0]} | {'; '.join(f'{x} {a} and {b}' for x, a, b in parts)} | {nb} | {n} | {saved} |")
OUT.write_text(f"""# WK-3 priced: a split of dTotalRecall, and of dBoundRoles with it

**Serves:** research PLAY-dClosedLoop-1

The owner took WK-3's recommendation on 2026-10-18, pricing a split of dTotalRecall before wave 3
(`build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md` `[wave-2-answers]`). This record prices it against the chain at
`44c8c8435`, the commit that folded wave 2's answers. At that commit the critical path is {P.base} units.

## [method] How the split is priced

- **Units and paths** are counted as NP-24's pricing counts them (`build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`
  `[method]`).
- **The successor that matters** is dWellOiledMachine, the build after dTotalRecall on the critical path. A split
  loses if dWellOiledMachine waits for a moved part.
- **What dWellOiledMachine needs** joins two readings:
  - the gate's mechanical one: `node_users.py` finds no backticked dependency of dWellOiledMachine on either build;
  - a reading of its 31 clauses, stated unit by unit in `[classification]`.
- **The bound.** dWellOiledMachine waits for dBoundRoles too, so a dTotalRecall split saves no more than dBoundRoles'
  landing allows. dBoundRoles lands only six units before dTotalRecall.

## [classification] The units dWellOiledMachine needs

Clause numbers are those `chain_clauses.py` prints at `44c8c8435`.

**dTotalRecall: {len(P.TR_KEEP)} of its {P.units[P.TR]} units stay.** The code record, clause {P.CODE}, stays as
well in T2 and C2, since dRankedPlan's intent fields and dCalibratedLens cite the `code` kind.

{kept(P.TR, P.TR_KEEP)}

The units that move: {moved(P.TR, set(P.TR_KEEP) | {P.CODE})}. Their users are {listed(sorted(P.TR_USERS))}, each
starting after dWellOiledMachine or, for dIndexedDesign, after dTotalRecall.

**dBoundRoles: {len(P.BR_KEEP)} of its {P.units[P.BR]} units stay.**

{kept(P.BR, P.BR_KEEP)}

The units that move: {moved(P.BR, set(P.BR_KEEP))}. Their users are {listed(sorted(P.BR_USERS))}, each starting after
dWellOiledMachine.

## [results] The candidates, at `44c8c8435`

**As asked.** The owner was asked from the first run, as captured:

```text
{asked}
```

**As folded.** Folding C2 kept one more of dBoundRoles' units in its first part: clause 9, the role-gate arm's field
escape. Allowances leak until it is closed, and keeping it costs nothing, since dBoundRoles' first part still lands
before dTotalRecall's. The run after it, as captured:

```text
{run}
```

{chr(10).join(rows)}

- **dTotalRecall alone saves six units, however much moves.** dBoundRoles then decides when dWellOiledMachine starts,
  and the path runs through it.
- **Both together save eighteen or nineteen.** dWellOiledMachine then starts once both builds' first parts land. The
  path's new long arm is dTotalRecall's moved part, through dIndexedDesign or dRankedPlan, which need what it holds.
- **Keeping the code record (C2) beats moving it (C1) by one unit.** dRankedPlan, which cites it, then leaves the long
  arm.
- **What the pricing cannot settle.** dIndexedDesign's needs from the moved part are a reading, not a gate's. If
  spec time finds it needs only the reuse index and the typed edges, those two units can stay too, and the path
  shortens by about two more.

## [costs] What the split costs

- **Two more builds.** Each brings the fixed cost NP-24's `[method]` names, which no unit counts.
- **While the moved parts land beside dWellOiledMachine:**
  - no annotation index, research view or generated views;
  - no retrofit kinds or `adopt` program;
  - the `code` record's queries, enrichment and ctags pack absent;
  - each role's trust profile, metrics and slots beyond the map, code and memory slices absent, the work order
    carrying its core fields.
- **The re-cut it owes:** the new rows, rosters and gaps, the moved nodes' owners, the later builds' after cells, and
  the reconciliation gate re-run, as NP-24's split owed.

## [forks] Parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| WK-4 | Split dTotalRecall, and dBoundRoles with it? | C2, both split and the code record kept in dTotalRecall's first part: two new builds; T2, dTotalRecall alone: one new build; keep both whole | a structural decision about the chain |

C2 is recommended. dTotalRecall alone cannot save more than six units, and only splitting both lets dWellOiledMachine
start earlier (`[results]`).
""", encoding="utf-8", newline="\n")
print(f"wrote {OUT}: {OUT.stat().st_size} bytes")
````

### `fold_wk4.py`

The owner's C2 folded: the four rows, the moved owners, the parents, the kinds, the systems owner and the ownership amendment.

````python
"""Fold the owner's WK-4 (C2): dTotalRecall keeps the 17 units dWellOiledMachine needs and dLinkedLibrary (Library) takes
23; dBoundRoles keeps 16 and dFurnishedOrders (Orders) takes 18, as price_wk3.py's folded classification says. The
nodes move with their units: v2's rows, catalogue owners and parents, flow-steps' adopt items, layer-memory's kinds,
the systems record's annotations owner, and the ownership amendment.

Usage: python -X utf8 fold_wk4.py   (from the worktree root, on the chain as priced at 44c8c8435)
"""
import importlib.util
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "expansions"))
from fold_lib import Record  # noqa: E402

spec = importlib.util.spec_from_file_location("wk3", HERE / "price_wk3.py")
P = importlib.util.module_from_spec(spec)
_out = sys.stdout
sys.stdout = open(os.devnull, "w")
spec.loader.exec_module(P)
sys.stdout = _out

B = "memory/builds/dClosedLoop/build/"
L, F = "dLinkedLibrary", "dFurnishedOrders"
TR_A, BR_A = set(P.TR_KEEP) | {P.CODE}, set(P.BR_KEEP)
CL_TR, CL_BR = list(P.clauses["dTotalRecall"]), list(P.clauses["dBoundRoles"])
assert len(TR_A) == 17 and len(BR_A) == 16 and len(CL_TR) == 40 and len(CL_BR) == 34
# The feature selector's arming moves with dTotalRecall's clause 39, so dBoundRoles' clause 34 names its new home.
old34 = "once dTotalRecall arms that selector"
assert old34 in CL_BR[33]
CL_BR[33] = CL_BR[33].replace(old34, f"once {L} arms that selector")
GAPS = {
    "dTotalRecall": ["gap-mem-01", "gap-mem-04", "gap-mem-05", "gap-mem-06", "gap-mem-07", "gap-mem-13", "gap-mem-16",
                     "gap-mem-20", "gap-mem-21", "gap-mem-23", "gap-mem-26", "gap-mem-27", "gap-design-01",
                     "gap-mem-28", "gap-mem-30"],
    L: ["gap-mem-02", "gap-mem-03", "gap-mem-08", "gap-mem-09", "gap-mem-11", "gap-mem-12", "gap-mem-14", "gap-mem-15",
        "gap-mem-17", "gap-mem-18", "gap-mem-19", "gap-mem-22", "gap-mem-24", "gap-mem-25", "gap-mem-29", "gap-mem-31",
        "gap-mem-32", "gap-mem-33", "gap-mem-34"],
    "dBoundRoles": ["gap-roles-01", "gap-roles-02", "gap-roles-03", "gap-roles-04", "gap-roles-05", "gap-roles-06",
                    "gap-roles-07", "gap-roles-08", "gap-orient-07", "gap-orient-09", "gap-roles-11", "gap-roles-14",
                    "gap-roles-18", "gap-roles-19", "gap-roles-20"],
    F: ["gap-roles-09", "gap-roles-10", "gap-roles-12", "gap-roles-13", "gap-roles-15", "gap-roles-16", "gap-roles-17",
        "gap-orient-15", "gap-roles-21", "gap-roles-22"],
}
L_KEYS = ["annotations.budget", "annotations.grammar", "annotations.lookup", "annotations.resolve-scope",
          "decisions.major", "memory.code-enrich", "retrofit.decisions", "retrofit.practice-pending",
          "retrofit.reconstruct", "reuse.delivery", "reuse.propose"]
F_KEYS = ["annotations.delivery", "instructions.slices", "memory.code-budget", "memory.code-roles", "memory.map-unfold",
          "memory.project-map", "notices.record", "prompts.batch", "retrofit.slot-bytes", "roles.answered-calls",
          "roles.on-contradiction", "roles.orientation.house-index", "roles.trust", "roles.verifier-context"]
L_ITEMS = ["adopt.census", "adopt.practices", "adopt.decisions", "adopt.reconstruct"]
L_KINDS = ["research return", "decision", "gotcha", "annotation index", "recall index", "baseline", "census", "ruling"]


def pick(cl, keep, first):
    return "; ".join(c for i, c in enumerate(cl, 1) if (i in keep) == first)


V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
for build, stage, cl, keep, new, nstage in (("dTotalRecall", "Memory", CL_TR, TR_A, L, "Library"),
                                            ("dBoundRoles", "Roles", CL_BR, BR_A, F, "Orders")):
    row = next(ln for ln in V.text.split("\n") if ln.startswith(f"| {build} | {stage} |"))
    cells = [c.strip() for c in row.strip().strip("|").split(" | ")]
    assert cells[3] == "; ".join(P.clauses[build]), f"{build}'s planned units differ from the priced row"
    have = [g.strip() for g in cells[4].split(",")]
    assert set(have) == set(GAPS[build]) | set(GAPS[new]), sorted(set(have) ^ (set(GAPS[build]) | set(GAPS[new])))
    keep_g = [g for g in have if g in GAPS[build]]
    new_g = [g for g in have if g in GAPS[new]]
    V.sub(row, "\n".join([f"| {build} | {stage} | {cells[2]} | {pick(cl, keep, True)} | {', '.join(keep_g)} |",
                          f"| {new} | {nstage} | {build} | {pick(cl, keep, False)} | {', '.join(new_g)} |"]),
          f"{build}'s row, split")
for build, stage, old, add in (("dIndexedDesign", "Design", "dDeclaredLoop, dTotalRecall, dKeptSession, dBoundRoles", [L]),
                               ("dShippedRelease", "Deploy", "dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine",
                                [L, F]),
                               ("dMindYourWords", "Lexicon", "dWellOiledMachine, dWitnessedBar", [L, F]),
                               ("dScopedBuild", "Build", "dIndexedDesign, dWitnessedBar, dWellOiledMachine", [F]),
                               ("dTendedCadence", "Maintain", "dWitnessedBar, dRankedPlan, dWellOiledMachine, "
                                "dIndexedDesign", [F])):
    V.sub(f"| {build} | {stage} | {old} |", f"| {build} | {stage} | {old}, {', '.join(add)} |", f"{build}'s parents")
pol = V.text.split("\n## [policies]", 1)[1].split("\n## ", 1)[0]
new_pol = pol
for keys, frm, to in ((L_KEYS, "dTotalRecall", L), (F_KEYS, "dBoundRoles", F)):
    for k in keys:
        rows = [ln for ln in new_pol.split("\n") if ln.startswith(f"| `{k}` |")]
        if len(rows) != 1 or not rows[0].endswith(f"| {frm} |"):
            sys.exit(f"catalogue: `{k}` has {len(rows)} rows, or an owner other than {frm}")
        new_pol = new_pol.replace(rows[0], rows[0][:-len(f"{frm} |")] + f"{to} |")
V.sub(pol, new_pol, "catalogue owners")
V.done += len(L_KEYS) + len(F_KEYS) - 1
V.insert_before("\nRevised: 2026-10-17, after the folds' closing review", f"""
Revised: 2026-10-18, WK-3 priced and the owner's WK-4 (`build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md`):
- dTotalRecall keeps the 17 units dWellOiledMachine needs, the code record among them, and {L}, the library, takes
  23: decisions and reuse, annotations, the views, the retrofit's memory kinds, the code record's queries,
  enrichment and ctags pack, and the typed edges;
- dBoundRoles keeps the 16 units dWellOiledMachine needs, the role-gate escape's fix among them, and {F}, the
  orders, takes 18: the work order's slots, trust profiles, the answered-call hook, repairs, role metrics, the
  tester re-founded and owner questions asked live;
- each moved key, item, kind and the annotations system change owner with their unit, and five later builds gain a
  parent;
- the two builds' gaps split with their units, fifteen and nineteen, and fifteen and ten.
""", "revision note")
V.save()

FS = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
for tag in L_ITEMS:
    rows = [ln for ln in FS.text.split("\n") if ln.startswith(f"| `{tag}` |")]
    if len(rows) != 1 or not rows[0].endswith("| dTotalRecall |"):
        sys.exit(f"flow-steps: `{tag}` has {len(rows)} rows, or another owner")
    FS.sub(rows[0], rows[0][:-len("dTotalRecall |")] + f"{L} |", tag)
FS.save()

LM = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md")
for kind in L_KINDS:
    LM.sub(f"| {kind} | dTotalRecall |", f"| {kind} | {L} |", kind)
LM.sub("`adopt.practices` writes the ruling records, an item dTotalRecall owns",
       f"`adopt.practices` writes the ruling records, an item {L} owns", "ruling's writer")
LM.save()

SY = Record(B + "2026-10-16-build-PLAY-dClosedLoop-1-systems.md")
SY.sub("- **Owners.** The memory layer, kit memory-tree, chain build dTotalRecall. The tags come from",
       f"- **Owners.** The memory layer, kit memory-tree, chain build {L} (WK-4). The tags come from", "annotations owner")
SY.save()

O = Record(B + "2026-10-17-build-PLAY-dClosedLoop-1-ownership.md")
O.text = O.text.rstrip("\n") + f"""
- **WK-4, 2026-10-18:** the owner chose C2, so dTotalRecall splits into itself and {L}, and dBoundRoles into itself
  and {F} (`build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md`). The nodes move with their units:
  - to {L}: the items {', '.join(f'`{t}`' for t in L_ITEMS)}, the kinds {', '.join(f'`{k}`' for k in L_KINDS)}, the
    annotations system, and the keys {', '.join(f'`{k}`' for k in L_KEYS)};
  - to {F}: the keys {', '.join(f'`{k}`' for k in F_KEYS)}.
"""
O.done += 1
O.save()
print(f"split: dTotalRecall {len(TR_A)}, {L} {40 - len(TR_A)}; dBoundRoles {len(BR_A)}, {F} {34 - len(BR_A)}")
````

### `fold_wk4_classes.py`

The three class rows WK-4 moved, re-pointed once the gate was red on them.

````python
"""The re-cut's class rows WK-4 moved, re-pointed once the gate was red on them: the two whose citing units moved from
dBoundRoles to dFurnishedOrders, and the one whose key moved from dTotalRecall to dLinkedLibrary.

Usage: python -X utf8 fold_wk4_classes.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

RC = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md")
RC.sub("| dBoundRoles | `feature` | dTotalRecall | tolerance | the work order selects by `feature.*` only once dTotalRecall "
       "arms that selector,",
       "| dFurnishedOrders | `feature` | dTotalRecall | tolerance | the work order selects by `feature.*` only once "
       "dLinkedLibrary arms that selector (WK-4),", "feature")
RC.sub("| dBoundRoles | `code` | dTotalRecall | tolerance |", "| dFurnishedOrders | `code` | dTotalRecall | tolerance |",
       "code")
RC.sub("| dDeclaredLoop | `decisions.major` | dTotalRecall |", "| dDeclaredLoop | `decisions.major` | dLinkedLibrary |",
       "decisions.major")
RC.save()
````

### `fold_wk4_fates.py`

The fates record's thirteen destinations WK-4 moved.

````python
"""The fates record's destinations that WK-4 moved: thirteen rows whose function now lands in dLinkedLibrary or
dFurnishedOrders, each re-pointed with its "Decided by" chain row; a row whose function split names both builds.

Usage: python -X utf8 fold_wk4_fates.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

L, F = "dLinkedLibrary", "dFurnishedOrders"
FR = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md")
for old, new, label in (
        ("| memory-recall | optional | narrowed to a record finder (dTotalRecall) |",
         f"| memory-recall | optional | narrowed to a record finder ({L}) |", "memory-recall kit"),
        ("| the orientation scout, composing the card in a sidechain (dBoundRoles) | roles `[forks]`; v2 `[chain]` dBoundRoles |",
         f"| the orientation scout, composing the card in a sidechain ({F}) | roles `[forks]`; v2 `[chain]` {F} |",
         "gov-orienter"),
        ("| role-by-step matrix joined both ways (dBoundRoles); policy reader re-pointed (dConvergedCharter) | v2 `[chain]` "
         "dBoundRoles; v2 `[chain]` dConvergedCharter |",
         f"| role-by-step matrix joined both ways ({F}); policy reader re-pointed (dConvergedCharter) | v2 `[chain]` "
         f"{F}; v2 `[chain]` dConvergedCharter |", "check_roles.py"),
        ("| generated views, README schema, routing region (dTotalRecall); drift import becomes an optional slot "
         "(dOrderedCharter) | v2 `[chain]` dTotalRecall; v2 `[chain]` dOrderedCharter |",
         f"| generated views ({L}), README schema and routing region (dTotalRecall); drift import becomes an optional slot "
         f"(dOrderedCharter) | v2 `[chain]` {L}; v2 `[chain]` dTotalRecall; v2 `[chain]` dOrderedCharter |",
         "gen_build_index.py"),
        ("| handed by write set (dTotalRecall); check-18 probe becomes an optional slot | v2 `[chain]` dTotalRecall; "
         "v2 `[chain]` dOrderedCharter |",
         f"| handed by write set ({L}); check-18 probe becomes an optional slot | v2 `[chain]` {L}; "
         "v2 `[chain]` dOrderedCharter |", "gotchas.py"),
        ("| split by kind; the log keeps its path, with a holds-now view (dTotalRecall) | layer-memory `[decisions]`; "
         "v2 `[chain]` dTotalRecall |",
         f"| split by kind; the log keeps its path, with a holds-now view ({L}) | layer-memory `[decisions]`; "
         f"v2 `[chain]` {L} |", "DECISIONS.md"),
        ("| the core `code` record and `gov map code` (dTotalRecall) | the owner's point 3 (night pass); v2 `[chain]` "
         "dTotalRecall |",
         f"| the core `code` record (dTotalRecall) and `gov map code` ({L}) | the owner's point 3 (night pass); v2 "
         f"`[chain]` dTotalRecall; v2 `[chain]` {L} |", "gen_map.py"),
        ("| optional: dossiers anchored to symbol keys, their header the feature node as NP-16 settles (dTotalRecall) |",
         f"| optional: dossiers anchored to symbol keys (dTotalRecall), their header the feature node as NP-16 settles "
         f"({L}) |", "dossiers"),
        ("| 0 of 24 solved; replaced by the house index via **Reuse:** (dTotalRecall) |",
         f"| 0 of 24 solved; replaced by the house index via **Reuse:** ({L}) |", "reuse_lookup"),
        ("| a range read over the `code` record, and enrichment staleness by body hash (dTotalRecall) |",
         f"| a range read over the `code` record (dTotalRecall), and enrichment staleness by body hash ({L}) |",
         "map_diff"),
        ("| optional hook pack (dWellOiledMachine); shell reads too (dTotalRecall) | layer-runtime `[enforce]`; v2 "
         "`[chain]` dTotalRecall |",
         f"| optional hook pack (dWellOiledMachine); shell reads too ({L}) | layer-runtime `[enforce]`; v2 `[chain]` "
         f"{L} |", "recall-opened.js"),
        ("| observability's reader half; role metrics read it (dBoundRoles) | layer-expansions `[design-observability]`; "
         "v2 `[chain]` dBoundRoles |",
         f"| observability's reader half; role metrics read it ({F}) | layer-expansions `[design-observability]`; "
         f"v2 `[chain]` {F} |", "runlog reader"),
        ("| orientation scout (dBoundRoles); `kickoff.runs` (dRankedPlan); thin entry | v2 `[chain]` dBoundRoles; "
         "v2 `[chain]` dRankedPlan;",
         f"| orientation scout ({F}); `kickoff.runs` (dRankedPlan); thin entry | v2 `[chain]` {F}; "
         "v2 `[chain]` dRankedPlan;", "kickoff procedure")):
    FR.sub(old, new, label)
FR.save()
````

### `write_wk4_answers.py`

The pricing record's `[answers]` and `[folded]`, the walk's WK-4 line and the session log's event.

````python
"""Record WK-4's answer and the two names in the pricing record ([answers], verbatim, and [folded]), note WK-4 in the
walk record's [wave-2-answers], and log the event. Usage: python -X utf8 write_wk4_answers.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
PR = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md")
PR.text = PR.text.rstrip("\n") + """

## [answers] The owner's answers, 2026-10-18

Asked through AskUserQuestion from the run `[results]` keeps as asked, each answer quoted as the tool returned it, the
critical path's quoted length pinned to the commit it was read at:
- WK-4, asked at `44c8c8435` as "WK-4: Split dTotalRecall, and dBoundRoles with it? (a structural decision about the chain; critical path 190 today)": "C2, both split (Recommended)"

The two new builds' names, asked after:
- asked as "Name for dTotalRecall's split-off build (23 units: decisions and reuse, annotations, the views, the retrofit's memory kinds, the code record's queries, enrichment and ctags pack, and the typed edges)?": "dLinkedLibrary (Recommended)"
- asked as "Name for dBoundRoles' split-off build (19 units: the work order's slots, trust profiles, the answered-call hook, repairs, role metrics, the tester re-founded, owner questions live)?": "dFurnishedOrders (Recommended)"

The fold kept the role-gate escape's fix in dBoundRoles' first part (`[results]`, "As folded"), so dFurnishedOrders
holds 18 units, not the 19 asked.

## [folded] What the answers changed

- **v2's chain** (its revision note dated 2026-10-18, WK-4):
  - dTotalRecall keeps 17 units, and dLinkedLibrary, stage Library, after dTotalRecall, takes 23;
  - dBoundRoles keeps 16, and dFurnishedOrders, stage Orders, after dBoundRoles, takes 18;
  - dIndexedDesign gains dLinkedLibrary as a parent, and dScopedBuild and dTendedCadence gain dFurnishedOrders;
  - dShippedRelease and dMindYourWords gain both;
  - the two builds' gaps split fifteen and nineteen, and fifteen and ten.
- **The owners:**
  - v2's catalogue: 11 keys to dLinkedLibrary and 14 to dFurnishedOrders;
  - flow-steps: the four `adopt.*` items to dLinkedLibrary;
  - layer-memory: eight kinds to dLinkedLibrary;
  - the systems record: the annotations system to dLinkedLibrary;
  - the ownership record's amendment lists every moved node.
- **The re-cut's class rows:** the two whose citing units moved now name dFurnishedOrders, and `decisions.major`'s now
  names dLinkedLibrary as the key's owner. The gate was red on all three until they did.
- **The fates record:** thirteen destinations moved with their functions, and a row whose function split names both
  builds.
- **The chain:** the critical path drops by nineteen units, as C2 priced, and now runs through dLinkedLibrary and
  dIndexedDesign. The instruments record's `[final]` holds the run.
"""
PR.done += 1
PR.save()

W = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("""- **WK-3:** a split of dTotalRecall is priced before wave 3, in
  `build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md`.
""", """- **WK-3:** a split of dTotalRecall is priced before wave 3, in
  `build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md`.
- **WK-4,** asked once that pricing was written: the owner chose C2 (that record's `[answers]`). dTotalRecall and
  dBoundRoles each split, and dLinkedLibrary and dFurnishedOrders join wave 2, where their units were.
""", "WK-4")
W.save()

L = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
L.insert_before("\n## Instruments\n", """
- 2026-10-18, session 1799cb98: WK-3 priced (`build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md`). A
  dTotalRecall split alone saves six units at most, because dWellOiledMachine also waits for dBoundRoles. The owner
  chose C2 for WK-4: dTotalRecall splits off dLinkedLibrary (Library) and dBoundRoles splits off dFurnishedOrders
  (Orders), and the path drops by nineteen units. The fold kept the role-gate escape's fix in dBoundRoles' first part
  at no cost. The gate was red on three class rows whose units or key had moved, until they were re-pointed.
""", "event")
L.save()
````

### `leaves.py`

Wave 3: the builds no build waits on, and the fates rows each one owns.

````python
"""The chain builds no build waits on, and the fates table's destinations each one owns. A leaf other than the
convergence build lands outside convergence's exit check, which joins the fates table.

Usage: python -X utf8 leaves.py   (from the worktree root)
"""
import re

B = "memory/builds/dClosedLoop/build/"
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
fates = open(B + "2026-10-18-build-PLAY-dClosedLoop-1-fates.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
parents = {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| .+ \| [^|]+ \|$", ln)
    if m:
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]
children = {b: [c for c in parents if b in parents[c]] for b in parents}
table = fates.split("## [table]", 1)[1].split("\n## ", 1)[0]
for b in sorted(b for b, cs in children.items() if not cs):
    rows = [ln for ln in table.split("\n") if ln.startswith("| ") and re.search(rf"\b{b}\b", ln.split(" | ")[4] if
                                                                                   ln.count(" | ") >= 5 else "")]
    print(f"leaf {b}: {len(rows)} fates rows go to it")
    for ln in rows:
        c = [x.strip() for x in ln.strip().strip("|").split(" | ")]
        print(f"  {c[0]} · {c[1][:50]} · {c[3]} · {c[4][:110]}")
print(f"builds no build waits on: {sum(1 for cs in children.values() if not cs)} of {len(children)}")
````

### `record_walk5.py`

Wave 3 presented with its two forks.

````python
"""Present wave 3 in the walk record: the owner's request, `[wave-3]`, `[wave-3-forks]` and `[walk-instrument-4]`.

Usage: python -X utf8 record_walk5.py <facts.out> <since.out> <path.out> <leaves.out>   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
FENCE = "`" * 3


def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")


facts, since, path, leaves = (read(p) for p in sys.argv[1:5])
W = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("""- The owner's word on wave 2 and its forks, 2026-10-18, verbatim: "approve wave 2, take the recommendations".
""", """- The owner's word on wave 2 and its forks, 2026-10-18, verbatim: "approve wave 2, take the recommendations".
- The owner's request for wave 3, 2026-10-18, verbatim: "present wave 3".
""", "words")
W.insert_before("## [walk-instrument] The walk's facts, and the clause scan", """## [wave-3] The runtime and the builds it opens, as presented

Derived at `7788ac269`. Each build's "since the walk opened" reads its row against `beda01950`.

### dWellOiledMachine: Runtime

After dBoundRoles, dTotalRecall and dKeptSession, 31 units, finishing at 128. Four builds wait on it: dMindYourWords,
dScopedBuild, dShippedRelease and dTendedCadence. It owns 7 items, 10 extension points, 18 keys, 7 kinds and 2 tag
namespaces, and closes 35 gaps, 13 of them HIGH, the most of any build.
- **The platform spike first:** a role-typed Workflow agent run inside a headless act session, with the headless
  backend measured beside it.
- **The driver:**
  - the supervisor, the only driver in every mode, the owner's session its client;
  - `next` over the loop kit's position function, and the `next —` micro-format;
  - the owner's pause, resume, withdraw and supersede, and attend and unattend;
  - the `step —` announcement before each act while attended.
- **Intake:** the prompt-submit hook writing each owner prompt to the session's intake log, Plan's ratification and the
  placement dispositions re-pointed to it, and intake for a prompt that reaches no owner session.
- **Acts:**
  - one act session per role act, with act binding and the epoch check at every spawn;
  - binding against the resolved shape's digest, each act writing its shape-run row;
  - the persisted-return store, and agent slots reserved under the cap.
- **The enforcement surface:** one dispatcher entry per event, the kits' fragments as packs, ask rules only the
  dispatcher answers, and each pack's refusal naming its rule and remedy; grants on every adapter row, and the secret
  value scan.
- **Sessions:** bound on every source; the compact hook re-injecting the build's card; the session-start hook loading
  the default set, card and map, and ending with `next`'s line; each compaction journaled.
- **Hosts and adapters:** scheduler hosts, harness adapters with capability tables, a measured `browser` row among them,
  the node registry, and the `visual.capture` command adapter.
- **The rest:** workspaces and the commit queue, event waits, the journal grammar, and the unattended kit dissolved
  into the loop kit and this one.
- **Since the walk opened:** seven units from the night pass:
  - the one-driver statement;
  - the announcement;
  - intake beyond the owner's session;
  - the unattended kit's dissolution;
  - the browser row and visual capture;
  - experiments' acts;
  - refusal text.

  Three units were reworded, and gap-orient-16 to gap-orient-18 and gap-rt-22 to gap-rt-24 came with them.
- **To look at:**
  - It left the critical path with WK-4. It lands four units before dTendedCadence can start, so it can grow by four
    at spec time before it returns to the path.
  - Its first unit, the platform spike, decides the runtime's shape. If it fails, the owner's session keeps hosting
    the driver under its owner binding, as the night pass's hosting rule says.
  - It carries the most gaps of any build.

### dScopedBuild: Build

After dIndexedDesign, dWitnessedBar, dWellOiledMachine and dFurnishedOrders, 11 units, finishing at 143.
dConvergedCharter waits on it. It owns 9 items, 6 keys and 2 kinds, and closes 7 gaps, 3 of them HIGH.
- **The exit contract:** one contract with a history-derived base, refusing a build's exit while a core red its own
  commits introduced stands, and the core checks run by the executor at Build's exit.
- **Scope and specs:**
  - built specs frozen;
  - every closing-review finding disposed as new units;
  - scope checked at the push by the touch join over the unit's own commits.
- **The record:** the closing review recorded, a write gate reading derived state, and the checklist witnessed.
- **The retrofit's drain:** each unit drains the legacy it touches, in hunks under `retrofit.drain-cap`, and claims
  the baselined map keys its write set holds.
- **Since the walk opened:** two units from the night pass. A bug-report patch build gets a red-first `reproduction`
  probe before its fix, and a playbook's pieces are built as units.
- **To look at:** it has 14 units of slack before dConvergedCharter can start. Its builders' code and map slots come
  from dFurnishedOrders, its parent since WK-4.

### dTendedCadence: Maintain

After dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign and dFurnishedOrders, 14 units, finishing at 146.
dCalibratedLens waits on it. It owns 7 items, 15 keys and 2 kinds, and closes 12 gaps, 2 of them HIGH.
- **The Maintain run:** its step checklist on the flow's executor, never a recipe-mode playbook, the cadence on
  Runtime's hosts, the safe-fix set and the maintenance record.
- **Detectors:**
  - detectors with owners, and map freshness;
  - the memory's dead pointers, absorbing `check-dead-paths.sh` with its merge-bar leg;
  - bundle members whose code changed while their head line did not.
- **Delivery:** Maintain and the Loop Review as cadence steps of the observability expansion, patch intakes rendered
  from keyed readings, `maintain.retrofit-heat`'s sweeps filed as patch builds, and the maintainer's definition.
- **Since the walk opened:** four units from the night pass and the owner's answers, and gap-maint-12 and
  gap-maint-13:
  - a cyclic playbook's cadence item, filing `repeat` intakes;
  - the bundle detector;
  - the weekly security review;
  - readings tiered by their deviation.
- **To look at:**
  - It is on the critical path again, now after dIndexedDesign.
  - Its four new units sit on the path. A split could save at most eight units, since dConvergedCharter also waits for
    dShippedRelease, and moving only the four new units would save four. That is WK-6.

### dMindYourWords: Lexicon

After dWellOiledMachine, dWitnessedBar, dLinkedLibrary and dFurnishedOrders, 17 units, finishing at 145. No build waits
on it. It owns 5 keys and the lexicon-declaration kind, and closes 10 gaps, 3 of them HIGH.
- **Definition classes:** conforming, forced, out of scope, not a name, and debt. Only debt counts against the
  shrink-only pin, held as a keyed ledger population.
- **Forced names:** recognised by what forces them, from packs generated per host kit, and gov's own contract-forced
  names in a table the instruction write path owns. The first wave of packs covers Python's stdlib bases, its test
  frameworks, `ast`, `logging` and the shell hosts. Django, Flask, Starlette, FastAPI and React follow after an
  adopter census.
- **Enforcement:**
  - the work order's vocabulary slice;
  - staged definitions checked at commit;
  - the branch's offenders compared with its base's at the bar;
  - drift beyond verbs, one verb per declared family per object, and a frozen noun canon.
- **The vocabulary** changes only through the instruction write path, and the two drift signals are the lexicon's own
  leg pack.
- **Since the walk opened:** one unit, the overloaded terms settled: attended, playbook and baseline (gap-lex-09).
- **To look at:**
  - No build waits on it, not even dConvergedCharter, whose exit check joins the fates table, and four fates rows go
    to it. That is WK-5.
  - Its packs unit, clause 7, reads like several units of work: two waves of generated packs.

## [wave-3-forks] Wave 3's forks, parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| WK-5 | Should dConvergedCharter wait for dMindYourWords? | yes: dMindYourWords lands at 145, before dConvergedCharter can start at 157, so the edge costs nothing, and convergence's fates join covers the lexicon's four rows; no, the lexicon lands on its own and convergence's join leaves its rows unchecked | a structural decision about the chain |
| WK-6 | Split dTendedCadence? | keep it whole: no split saves more than eight units, bounded by dShippedRelease, and only its four new units could plausibly move, saving four; price a split, as WK-3 was | a structural decision about the chain |

""", "wave-3")
W.text = W.text.rstrip("\n") + f"""

## [walk-instrument-4] Wave 3's facts, at `7788ac269`

`walk_facts.py`, `since.py` and `critical_path.py` as above, the last now counting twenty builds. `leaves.py` finds the
builds no build waits on, and the fates rows each one owns:

{FENCE}python
{read(HERE / "leaves.py")}
{FENCE}

{FENCE}text
$ python walk_facts.py dWellOiledMachine dScopedBuild dTendedCadence dMindYourWords
{facts}
$ python since.py beda01950 dWellOiledMachine dScopedBuild dTendedCadence dMindYourWords
{since}
$ python critical_path.py
{path}
$ python leaves.py
{leaves}
{FENCE}
"""
W.done += 1
W.save()
````

### `fold_wk5.py`

The owner's word on wave 3, WK-5 folded: dMindYourWords a parent of dConvergedCharter.

````python
"""Record the owner's word on wave 3 and fold its forks: WK-5 makes dMindYourWords a parent of dConvergedCharter, and
WK-6 keeps dTendedCadence whole, which changes nothing.

Usage: python -X utf8 fold_wk5.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
W = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("""- The owner's request for wave 3, 2026-10-18, verbatim: "present wave 3".
""", """- The owner's request for wave 3, 2026-10-18, verbatim: "present wave 3".
- The owner's word on wave 3 and its forks, 2026-10-18, verbatim: "approve wave 3, take the recommendations, present
  wave 4".
""", "words")
W.insert_before("## [walk-instrument] The walk's facts, and the clause scan", """## [wave-3-answers] Wave 3's forks, answered

The owner approved wave 3 and took each fork's recommendation, 2026-10-18 (`[words]`):
- **WK-5:** dConvergedCharter follows dMindYourWords, so convergence's fates join covers the lexicon's rows. The
  lexicon lands before convergence can start, and the path does not move.
- **WK-6:** dTendedCadence stays whole.

""", "wave-3 answers")
W.save()

V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
V.insert_before("\nRevised: 2026-10-17, after the folds' closing review", """
Revised: 2026-10-18, the walk's wave 3 (`build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md` `[wave-3-answers]`):
dConvergedCharter follows dMindYourWords, the one build besides it that no build waited on, so its exit check's fates
join covers the lexicon's rows (WK-5); dTendedCadence stays whole (WK-6).
""", "revision note")
V.sub("| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens |",
      "| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens, dMindYourWords |",
      "dConvergedCharter parents")
V.save()

L = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
L.insert_before("\n## Instruments\n", """
- 2026-10-18, session 1799cb98: the owner approved wave 3 and took both recommendations (the walk record's
  `[wave-3-answers]`). dConvergedCharter now follows dMindYourWords at no cost to the path (WK-5), and dTendedCadence
  stays whole (WK-6).
""", "event")
L.save()
````

### `lens_now.py`

Wave 4: SP-2 re-priced on today's chain, dConvergedCharter's parents and the Loop Review split.

````python
"""SP-2 re-priced on today's chain: dConvergedCharter's parents and their slack, and L1, dCalibratedLens split at the
Loop Review, as NP-24's pricing defined it (its Loop Review units 3, 5, 8 and 11 after dTendedCadence, the other seven
after dWellOiledMachine and dFurnishedOrders, whose code slot and slices they read).

Usage: python -X utf8 lens_now.py   (from the worktree root)
"""
import re

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
units, parents = {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        units[m.group(1)] = len([u for u in m.group(3).split("; ") if u.strip()])
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]


def path(units, parents):
    finish = {}

    def fin(b):
        if b not in finish:
            finish[b] = units[b] + max((fin(p) for p in parents[b]), default=0)
        return finish[b]

    for b in units:
        fin(b)
    return max(finish.values()), finish


base, fin = path(units, parents)
Y, Z = "dCalibratedLens", "dConvergedCharter"
tail = sorted(((fin[q], q) for q in parents[Z]), reverse=True)
print(f"baseline: {base} units; {Z}'s parents land at " + ", ".join(f"{q} {f}" for f, q in tail))
print(f"slack before {Y} decides {Z}'s start: {tail[0][0] - tail[1][0]} units, to {tail[1][1]}")
LOOP = {3, 5, 8, 11}
u, p = dict(units), {b: list(v) for b, v in parents.items()}
u[Y], u[Y + "-A"] = len(LOOP), units[Y] - len(LOOP)
p[Y + "-A"] = ["dWellOiledMachine", "dFurnishedOrders", "dFairHearing"]
p[Y] = parents[Y] + [Y + "-A"]
n, f2 = path(u, p)
print(f"L1: {Y}-A {u[Y + '-A']} lands at {f2[Y + '-A']}, the Loop Review's {u[Y]} at {f2[Y]} · {n} units ({n - base:+d})")
````

### `record_walk7.py`

Wave 4 presented with its two forks.

````python
"""Present wave 4 in the walk record: `[wave-4]`, `[wave-4-forks]` and `[walk-instrument-5]`.

Usage: python -X utf8 record_walk7.py <facts.out> <since.out> <lens.out>   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
FENCE = "`" * 3


def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")


facts, since, lens = (read(p) for p in sys.argv[1:4])
W = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.insert_before("## [walk-instrument] The walk's facts, and the clause scan", """## [wave-4] Review, release and convergence, as presented

Derived at `7554745d5`. Each build's "since the walk opened" reads its row against `beda01950`.

### dCalibratedLens: Review

After dTendedCadence and dFairHearing, 11 units, finishing at 157. dConvergedCharter waits on it. It owns 6 items, 6
keys and 2 kinds, and closes 10 gaps, 3 of them HIGH.
- **Stage reviews:** each stage review's lenses and effort, for Plan, Test, Deploy and Maintain, drawn from
  dFairHearing's catalogue and run through dDeclaredLoop's breakpoints.
- **The value ledger:**
  - one shared ledger;
  - its shape rows priced from the shape-run rows and the journal;
  - probe cost priced in it;
  - compactions counted per item kind as a sizing signal.
- **Calibration:** caps re-derived from evidence and review cost, and each role's item budget derived from its p90
  over sliced work orders.
- **The weekly Loop Review:**
  - instruction effectiveness measured from returns and findings, with units that bear no load pruned;
  - the not-in-view cause and its share, proposing the map's retirement if the share does not fall;
  - delivery metrics, and the owner queue's depth.
- **Instruction evals:** a replay suite of recorded items, re-run as a held leg whenever an instruction unit changes.
- **Since the walk opened:** three units from the night pass, the not-in-view cause reworded, and gap-review-14 to
  gap-review-16:
  - probe cost and compaction counts;
  - instruction evals;
  - delivery metrics.
- **To look at:**
  - It is the critical path's last stage before convergence.
  - SP-2 kept it whole when no lightening could save more than four units. The splits since have changed that: it
    now leads dShippedRelease by eight. A split at the Loop Review saves five to seven units, depending on whether
    the caps and item budgets are the Loop Review's own computations. That is WK-7.

### dShippedRelease: Deploy

After dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary and dFurnishedOrders, 21 units,
finishing at 149. dConvergedCharter waits on it. It owns 25 items, 17 keys and 9 kinds, and closes 17 gaps, 5 of them
HIGH.
- **Landing:** the landing record, ordered through a landing queue, and a dependent held until its parent lands. The
  lander runs the core checks on the landed tree before it releases the build, and the landing review blocks the
  close.
- **Release:**
  - the deploy engine, and promotion after landing through environments, an integrations extension point;
  - kit release notes, and the deployer's definition;
  - a derived runbook;
  - the incms adapter.
- **Distribution:**
  - the kit factory and its conformance gate, with `kit.toml` for govkit and lib;
  - the fleet register and its currency watch, and optional emitted CI;
  - `kits.offer`, unattended or on update, running nothing from the adopter's tree;
  - the install and update hooks, with the backlog migration as an upgrade step;
  - an adopter's CI test jobs imported as legs;
  - `install.guards`.
- **Integrations:** the ask tracker's one-way mirror.
- **Since the walk opened:** one unit, `install.guards` (NP-20), the install hooks reworded for the backlog
  migration's upgrade step (NP-22), and gap-deploy-14.
- **To look at:**
  - It has eight units of slack before dConvergedCharter can start.
  - One unit, "the incms adapter", names an adopter. The adopter-name ban (govkit selfcheck's check 10) refuses any
    shipped file that names one, case-insensitively, and `adopters.toml` declares that name. Built as worded, the
    adapter fails its own distribution gate. That is WK-8.

### dConvergedCharter: Convergence

After dScopedBuild, dShippedRelease, dCalibratedLens and dMindYourWords, 14 units, finishing at 171, the end of the
chain. It owns no node, and closes 9 gaps, 2 of them HIGH.
- **Protocols as facts:** protocol text derived to facts only, each document in its envelope, and protocols and
  templates rendered as tag-sliced views. The hand-written guides retire, their rationale moving into their units'
  `help` fields, and feature-specific guide prose moves into feature-scoped units.
- **Migration:**
  - every remaining positional reference migrated to tags;
  - records merged by evidence;
  - superseded parts retired through ratified proposals;
  - adopters migrated onto the ranked charter and the loop.
- **Consolidation:**
  - the record-kind factory and its conformance gate;
  - the remaining renderers absorbed;
  - Skills converged to thin entries rendered from units;
  - every kit conf key the retrofit does not convert folded into the policy file.
- **Retirement:** the unattended kit, its four guides and `/unattended`, once dWellOiledMachine's driver carries every
  run.
- **The exit check:** every part in the fates table at its fate, the table's join run as convergence's exit check.
- **Since the walk opened:** three units from the night pass: the unattended kit's retirement, the guide prose's move,
  and the fates join. A clause split in two at the first count was rejoined, and gap-tool-08 and gap-tool-09 came with
  them.
- **To look at:**
  - Since WK-5 it waits for every build, so the fates join can hold.
  - Its record-kind factory comes last, although every build from dTotalRecall on registers kinds through the
    registry. The registry's generated checks carry them until then.
  - Migrating the adopters is one unit for three repositories. Spec time is the place to cut it.

## [wave-4-forks] Wave 4's forks, parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| WK-7 | Split dCalibratedLens at the Loop Review, now that its lead over dShippedRelease is eight units? | keep it whole: the split saves five to seven units for a new build, below what the splits taken so far returned per build, and the caps' home decides the low end; split it, the lens machinery after dWellOiledMachine and the weekly Loop Review after dTendedCadence | a structural decision about the chain |
| WK-8 | How should dShippedRelease's adopter-named adapter ship? | a neutral adapter named for the engine it drives, the adopter's values in its own policy file, so the ban stays clean; the adopter's own adapter, registered at the integrations point from its own repository, gov shipping only the point; keep the name, and let the ban refuse it at build time | a structural decision |

""", "wave-4")
W.text = W.text.rstrip("\n") + f"""

## [walk-instrument-5] Wave 4's facts, at `7554745d5`

`walk_facts.py` and `since.py` as above. `lens_now.py` re-prices SP-2 on today's chain:

{FENCE}python
{read(HERE / "lens_now.py")}
{FENCE}

{FENCE}text
$ python walk_facts.py dCalibratedLens dShippedRelease dConvergedCharter
{facts}
$ python since.py beda01950 dCalibratedLens dShippedRelease dConvergedCharter
{since}
$ python lens_now.py
{lens}
{FENCE}

The adopter-name ban's source is `tools/govkit/govkit.py`, check 10, and the names it reads are `tools/govkit/adopters.toml`'s
`[[adopter]]` rows.
"""
W.done += 1
W.save()
````

### `adopter_probe.py`

WK-8's class over the real tree before it became the map's adopter-free arm: the planned units and node keys that name an adopter, and the purposes that do, which never ship.

````python
"""WK-8's class, run over the real tree before it becomes an arm: which planned units, and which map node keys and
purposes, name an adopter as `tools/govkit/adopters.toml` declares them (govkit selfcheck arm 10's source).

Usage: python -X utf8 adopter_probe.py   (from the worktree root)
"""
import importlib.util
import pathlib
import re
import sys
import tomllib

ROOT = pathlib.Path.cwd()
MAP = ROOT / "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py"
spec = importlib.util.spec_from_file_location("map", MAP)
m = importlib.util.module_from_spec(spec)
sys.argv = [str(MAP)]
spec.loader.exec_module(m)
A, ns = m.derive()

rows = tomllib.loads((ROOT / "tools/govkit/adopters.toml").read_text(encoding="utf-8")).get("adopter", [])
names = [n for r in rows for n in r.get("names", [])]
pat = re.compile("|".join(re.escape(n) for n in names), re.I)
print(f"adopter names: {len(names)} from {len(rows)} rows")

units = [(c["build"], u) for c in A["chain"] for u in c["units"].split("; ")]
print(f"planned units scanned: {len(units)} over {len(A['chain'])} chain rows")
for b, u in units:
    if pat.search(u):
        print(f"  UNIT {b}: {u[:120]!r}")

keys = purposes = 0
for name, nodes in ns.items():
    for n in nodes or []:
        keys += 1
        if pat.search(n["key"]):
            print(f"  KEY {name}.{n['key']}")
        if n.get("purpose") and pat.search(n["purpose"]):
            purposes += 1
            print(f"  PURPOSE {name}.{n['key']}: {n['purpose'][:100]!r}")
print(f"node keys scanned: {keys}; purposes naming an adopter: {purposes}")
````

### `fold_wk7_wk8.py`

The owner's word on wave 4: WK-7 keeps dCalibratedLens whole, WK-8 names the first engine adapter for its engine, and the walk completes.

````python
"""Record the owner's word on wave 4 and fold its forks: WK-7 keeps dCalibratedLens whole, which changes nothing, and
WK-8 names dShippedRelease's first engine adapter for the engine it drives, never for an adopter. The walk completes.

Usage: python -X utf8 fold_wk7_wk8.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
W = Record(B + "2026-10-18-build-PLAY-dClosedLoop-1-walk.md")
W.sub("""- The owner's word on wave 3 and its forks, 2026-10-18, verbatim: "approve wave 3, take the recommendations, present
  wave 4".
""", """- The owner's word on wave 3 and its forks, 2026-10-18, verbatim: "approve wave 3, take the recommendations, present
  wave 4".
- The owner's word on wave 4 and its forks, 2026-10-18, verbatim: "wave 4 approved, go with your recommendations".
""", "words")
W.insert_before("## [walk-instrument] The walk's facts, and the clause scan", """## [wave-4-answers] Wave 4's forks, answered

The owner approved wave 4 and took each fork's recommendation, 2026-10-18 (`[words]`):
- **WK-7:** dCalibratedLens stays whole. The spine split's pricing kept it whole when nothing could save more than
  four units, and that answer stands on the moved premise. One new build would buy five to seven units, and each split
  taken so far returned more per new build.
- **WK-8:** dShippedRelease's first engine adapter is named for the engine it drives, never for an adopter. The
  adopter's values live in that adopter's own policy file. The adapter is still fitted to what the first adopter runs,
  as round 3 settled: signed container images on compose and systemd hosts. Its exact name is the spec's, under that
  rule.

WK-8's class is a planned unit or a node key that names an adopter. A unit becomes shipped work and many keys become
shipped names, and govkit selfcheck's arm 10 refuses an adopter's name in any file gov ships. The design map's
adopter-free arm now checks both against `tools/govkit/adopters.toml`, arm 10's own source, matched as arm 10
matches. It was red on this unit before the fold and is green after it (the instruments record's `[adopter-free]`).
It does not read purposes or prose, which describe gov's own records and never ship.

With wave 4 the walk is complete: every build is walked and approved, and every fork it raised is answered. The
build's exit, and any review before it, waits on the owner's word that the design has its full shape.

""", "wave-4 answers")
W.save()

V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
V.insert_before("\nRevised: 2026-10-17, after the folds' closing review", """
Revised: 2026-10-18, the walk's wave 4 (`build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md` `[wave-4-answers]`):
dCalibratedLens stays whole (WK-7). dShippedRelease's first engine adapter is named for the engine it drives, never
for an adopter, with the adopter's values in that adopter's own policy file, since govkit selfcheck's arm 10 refuses
an adopter's name in any file gov ships (WK-8). The walk is complete.
""", "revision note")
V.sub("; the deploy engine; the incms adapter; ",
      "; the deploy engine; the first engine adapter, named for the engine it drives and never for an adopter, fitted to "
      "signed container images on compose and systemd hosts, with the adopter's values in that adopter's own policy file (WK-8); ",
      "WK-8 unit")
V.save()

X = Record(B + "2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md")
X.sub("the release runner. Each adopter's engine adapter is a dShippedRelease unit |",
      "the release runner. Each engine adapter is named for the engine it drives, never for an adopter, and an "
      "adopter's values live in that adopter's own policy file (WK-8); the first is a dShippedRelease unit |",
      "WK-8 engine kits")
X.save()

L = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
L.insert_before("\n## Instruments\n", """
- 2026-10-18, session 1799cb98: the owner approved wave 4 and took both recommendations (the walk record's
  `[wave-4-answers]`), so the walk is complete. dCalibratedLens stays whole (WK-7). dShippedRelease's first engine
  adapter is named for its engine, never for an adopter (WK-8). The design map gains an adopter-free arm for the class,
  seen red on that unit before the fold.
""", "event")
L.save()
````

### `fix_plan_deps.py`

The away pass: the memory plan's session units moved to dWellOiledMachine, the build that owns acts and bindings, once a dependency check found dKeptSession before it.

````python
"""Move the memory plan's session units to dWellOiledMachine, the build that owns acts and bindings, and drop `act=`
from the work order's marker, since the act declares `follows`.

Usage: python -X utf8 fix_plan_deps.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

P = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md")
P.sub("| a work order | the `gov:handoff` marker (role, build, unit, path, `role-sha`, `task-sha`), gaining `item=` and `act=` | the handoff renderer |",
      "| a work order | the `gov:handoff` marker (role, build, unit, path, `role-sha`, `task-sha`), gaining `item=` | the handoff renderer |",
      "marker sites")
P.sub("| dBoundRoles | every work order carrying the marker with `item=` and `act=`, and every return its `answers` |",
      "| dBoundRoles | every work order carrying the marker with `item=`, and every return its `answers` |",
      "dBoundRoles unit")
P.sub("| dKeptSession | the session node derived from bindings, with `runs-in` and `after`, and live delivery through the inbox |",
      "| dWellOiledMachine | the session node derived from bindings, with `runs-in` and `after`, and live delivery through the inbox |",
      "session unit")
P.sub("| the live inbox | runtime | the harness's per-session inbox | Claude only; addressed by session id | witness: live delivery beside the mailbox | harness session id | dKeptSession |",
      "| the live inbox | runtime | the harness's per-session inbox | Claude only; addressed by session id | witness: live delivery beside the mailbox | harness session id | dWellOiledMachine |",
      "inbox owner")
P.sub("| orientation cards | runtime | `<git-common-dir>/orientation/<id>.md` | 22, one per session | retired into the session binding | — | dKeptSession |",
      "| orientation cards | runtime | `<git-common-dir>/orientation/<id>.md` | 22, one per session | retired into the session binding | — | dWellOiledMachine |",
      "cards owner")
P.save()
````

### `fold_away.py`

The away pass folded: P33 widened and P34 to P38, seventeen keys and their preset rows, the chain rows' thirty units and their gaps, thirty-nine gaps, six record kinds and the Codex facts.

````python
"""Fold the away pass into the design: P34 to P38 and P33's widened edge set, seventeen catalogue keys and their
preset rows, the chain rows' new units and gaps, the gap register's thirty-nine gaps and two amended Codex rows, six
record kinds in the kind registry, and the runtime record's Codex facts.

Usage: python -X utf8 fold_away.py   (from the worktree root)
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

B = "memory/builds/dClosedLoop/build/"
PLAN = "`build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`"
AWAY = "`build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`"

# ---- v2 -------------------------------------------------------------------------------------------------------------
V = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")

V.sub("""  content inlined, by flag (the owner's point 4, night pass, and NP-14).
""", """  content inlined, by flag (the owner's point 4, night pass, and NP-14). The twelve declared types gain eleven, the
  provenance and flow-data edges of the memory plan (""" + PLAN + """ `[edges]`): `serves`,
  `made-by`, `caused-by`, `follows`, `answers`, `runs-in`, `carries`, `pinned-at`, `reads`, `writes` and
  `promoted-from` (the away pass).
- **P34 Instruction and memory share one writing practice.** A record section and an instruction unit are written
  alike: named by a tag, one subject each, every relation a typed edge declared on its own line at the site that owns
  it, every quoted derived fact pinned, and rationale kept apart from what loads. They differ in level and lifecycle,
  never in grammar. Every pocket the loop writes or reads, in the tree or outside it, is a node or a declared witness
  joined by a key, and none is left to prose (the owner's point 1, the away pass; """ + PLAN + """).
- **P35 Every record names its cause.** Each record carries its own id and the id of what caused it, its inverse
  derived, so `gov trace <key>` returns what happened from any key and `gov why <key>` the instruction and request
  behind it. An act carries its own cost and duration. What lives on one node only renders `not-local` or `pruned`,
  never empty (the owner's point 5, the away pass).
- **P36 No harness is the runtime.** gov runs through harness adapters, each registered with capability rows that one
  conformance fixture measures. The core relies only on the rows every registered act adapter passes, and a
  capability above them is an optional slot. The supervisor launches acts through the CLI or an SDK, and the owner's
  application is a viewer chosen by policy (the owner's point 3, the away pass).
- **P37 One portable practice, a role per language.** Python carries logic, shell is a thin shim where a host demands
  it and its other lines only shrink, and JavaScript serves only the harness's own surfaces. One rule set governs
  encoding, line endings, paths, process launch, temp files, interpreter floors and quoting, each rule with its leg,
  over the platforms the repository declares (the owner's point 4, the away pass).
- **P38 Supersession walks declared steps.** A build that changes what an adopter can see ships its successor with an
  upgrade step that runs up and down. `update` walks every step between an adopter's receipt and its target in
  order, each idempotent by its witness; gov runs every step on itself first; and a surface an adopter can see keeps
  working, or warns, until its window closes (the owner's point 6, the away pass).
""", "P33 to P38")

POL = [
    ("memory.legacy-records", "anchors-only, backfill, retag", "backfill",
     "the away pass, point 1: an adopter's records reach the plan with no file rewritten under `backfill`; pending AP-3", "dTotalRecall"),
    ("commits.edge-check", "push-leg, commit-msg, off", "push-leg",
     "the away pass, point 1: the commit queue writes the trailers, a leg at the push reads the binding; pending AP-6", "dWellOiledMachine"),
    ("commits.squash", "re-emit-union, refuse, accept-loss", "re-emit-union",
     "the away pass, point 1: a squash drops every trailer; gov never squashes, an adopter may; pending AP-7", "dShippedRelease"),
    ("trace.identity", "act-only, session, salted", "act-only",
     "the away pass, points 1 and 5: committed memory names the act, as the owner's rule of 2026-09-13 keeps session ids out of committed records; never set by a preset; pending AP-8", "dWellOiledMachine"),
    ("trace.cost", "tokens+wall, tokens, none", "tokens+wall",
     "the away pass, point 5: durations from the act's process output, never journal times of day; pending AP-21", "dWellOiledMachine"),
    ("trace.leg-output", "tail-by-hash, node-local", "tail-by-hash",
     "the away pass, point 5: a failing leg's output outlives its worktree; pending AP-22", "dWitnessedBar"),
    ("trace.rows", "60, 120, all", "60",
     "the away pass, point 5: one unattended run alone held 259 model events; pending AP-23", "dWellOiledMachine"),
    ("runtime.binary", "newest-conforming, path, app-bundled, or a pinned path", "newest-conforming",
     "the away pass, point 3: the CLI on PATH and the application's drift apart; pending AP-11", "dWellOiledMachine"),
    ("runtime.owner-harness", "auto, or a registered harness adapter", "auto",
     "the away pass, point 3: the owner's application is a viewer; never set by a preset; pending AP-12", "dWellOiledMachine"),
    ("runtime.act-harness", "a registered harness adapter that passes the act rows", "claude-code",
     "the away pass, point 3: Codex registers as an act backend once its rows pass; pending AP-13", "dWellOiledMachine"),
    ("runtime.act-auth", "oauth-shared, setup-token, api-key", "oauth-shared",
     "the away pass, point 3: the operator's credentials, never set by a preset; pending AP-14", "dWellOiledMachine"),
    ("platforms.supported", "any subset of windows-gitbash, linux, macos, pwsh-launch", "windows-gitbash, linux",
     "the away pass, point 4: a fact about the repository, never set by a preset; pending AP-17", "dShippedRelease"),
    ("platforms.verify", "held, bar, ci, off", "held",
     "the away pass, point 4: `held` until the Linux half is green; pending AP-18", "dShippedRelease"),
    ("install.deprecation-window", "0, 1, 2, 4 releases", "2",
     "the away pass, point 6: equal to `currency.max-behind`, so an adopter inside its currency budget never meets a removed surface; pending AP-26", "dGroundRules"),
    ("install.on-shim-call", "warn, journal, refuse", "warn",
     "the away pass, point 6: a forwarded call prints and is journaled for the fleet view; pending AP-27", "dGroundRules"),
    ("install.retired-edits", "order, keep, delete", "order",
     "the away pass, point 6: an edited retired file is kept, marked forked and ordered, never silently patched; pending AP-28", "dGroundRules"),
    ("install.steps", "offer, attended", "offer",
     "the away pass, point 6: a step needing the target's own code always falls back to attended (NP-22); pending AP-29", "dShippedRelease"),
]
row = "| `retrofit.slot-bytes` | 512, 1024, 2048 | 1024 | the retrofit round | dFurnishedOrders |\n"
V.sub(row, row + "".join(f"| `{k}` | {v} | {d} | {s} | {o} |\n" for k, v, d, s, o in POL), "catalogue")

PRE = [
    ("memory.legacy-records", "anchors-only", "backfill", "backfill", "backfill"),
    ("commits.edge-check", "push-leg", "push-leg", "commit-msg", "push-leg"),
    ("commits.squash", "re-emit-union", "re-emit-union", "refuse", "re-emit-union"),
    ("trace.cost", "tokens", "tokens+wall", "tokens+wall", "tokens+wall"),
    ("trace.leg-output", "node-local", "tail-by-hash", "tail-by-hash", "tail-by-hash"),
    ("trace.rows", "60", "60", "60", "60"),
    ("runtime.binary", "newest-conforming", "newest-conforming", "newest-conforming", "newest-conforming"),
    ("runtime.act-harness", "claude-code", "claude-code", "claude-code", "claude-code"),
    ("platforms.verify", "held", "held", "ci", "held"),
    ("install.deprecation-window", "1", "2", "2", "4"),
    ("install.on-shim-call", "warn", "warn", "journal", "warn"),
    ("install.retired-edits", "order", "order", "order", "order"),
    ("install.steps", "offer", "offer", "attended", "offer"),
]
prow = "| `retrofit.slot-bytes` | 1024 | 1024 | 1024 | 1024 |\n"
V.sub(prow, prow + "".join(f"| `{k}` | {a} | {b} | {c} | {d} |\n" for k, a, b, c, d in PRE), "presets")

V.sub("""  `verdict.remote.pin`, `attendance`, `attendance.scope` or `install.guards`:""",
      """  `verdict.remote.pin`, `attendance`, `attendance.scope`, `install.guards`, `trace.identity`,
  `runtime.owner-harness`, `runtime.act-auth` or `platforms.supported`:""", "never-touch keys")
V.sub("""the owner's own choice (night pass, point 1); and where the core guards install is the operator's (NP-20).""",
      """the owner's own choice (night pass, point 1); where the core guards install is the operator's (NP-20); and
  whether committed memory names a session, which application the owner works in, the operator's credentials and the
  platforms a repository runs on are facts about the owner, the operator or the repository (the away pass).""",
      "never-touch reason")

UNITS = {
    "dGroundRules": ([
        "the upgrade-step kind: a kit descriptor's `[[upgrade]]` row (id, introducing commit, up and down argv run from gov's checkout, witness, surfaces, whether it needs the target's code) and the registry's `[[retired]]` succession rows, read by `update` and `check`, with the legacy homes declared as the translation window's population (P38, its home parked as AP-25)",
        "`update` walking every step between a receipt's vintage and its target, oldest first, each skipped when its witness holds",
        "down steps run in reverse, and a recorded rollback that lifts the downgrade refusal for a rollback only",
        "the release-0 fixture tree and the `upgrade-walk` leg: up, down byte-identical, up again, every planted edit carried or ordered, each step seen load-bearing by skipping it once",
    ], ["gap-deploy-15", "gap-deploy-16", "gap-deploy-17", "gap-tool-10"]),
    "dOrderedCharter": ([
        "the shared edge grammar at every site the memory plan names, the eleven new edge types registered with their namespaces, `decides` and `after` widened, `promoted-from` written by `instructions.edit`, and the edge checks in the tags leg pack (P33, P34)",
        "the one writing practice's checks over records as well as units: address, one subject, typed relations, pinned facts and one door (P34)",
        "the portable practice: a role per language, and one rule set for encoding, line endings, paths, launch, temp files, interpreter floors and quoting, each rule paired with its leg, absorbing `[cross-os]` and `[bytes]` (P37)",
        "its own upgrade steps: agent-instructions' wiring moved to the one renderer, and the `map_lib` re-export declared as a deprecation (P38)",
    ], ["gap-mem-35", "gap-tool-19"]),
    "dDeclaredLoop": ([
        "the commit node: the trailer keys `Gov-Unit`, `Gov-Item` and `Gov-Act` mapped to edge types, `Pass:` and `Decided:` registered with one reader, and the position engine reading them (the memory plan's `[sites]`)",
    ], ["gap-spine-08", "gap-spine-09"]),
    "dWitnessedBar": ([
        "the portability leg pack: a line-ending class leg, encoding arms for stdout and JavaScript, a bare-shell-name arm, an interpreter-floor arm with a feature census, the shell-role ledger, and the resolver preferring a direct executable that meets the floor (P37)",
        "the verdict record naming its bar run and its cause, and a failing leg's output tail kept by hash, as `trace.leg-output` says (P35)",
    ], ["gap-tool-12", "gap-tool-13", "gap-tool-15", "gap-test-20"]),
    "dTotalRecall": ([
        "the kind registry completed: home, lifecycle, readers and layer on every row, witness rows for the pockets outside the tree, the commit, view, registry, archive, instrument and witness kinds, and the Serves kind `journal` renamed `log` (the memory plan's `[pockets]`)",
        "`record` writing each record's header (Serves, Made-by, Caused-by) and each section's edge line, refusing a missing cause on a kind that is not a root, with the Serves lines read as `serves` edges and derived anchors for untagged headings, as `memory.legacy-records` says (P34, P35)",
    ], ["gap-mem-36", "gap-mem-37", "gap-mem-38", "gap-mem-40"]),
    "dLinkedLibrary": ([
        "`decides` on every decision row, `Decided:` trailers read as decision rows, and every bug class naming its cause, language and platform (the memory plan's `[cycle]`, P37)",
    ], ["gap-mem-39", "gap-tool-17"]),
    "dBoundRoles": ([
        "every work order carrying its marker with `item=`, and every return naming the work order it `answers` (the memory plan's `[sites]`)",
    ], ["gap-roles-23"]),
    "dWellOiledMachine": ([
        "the act as the key: minted at launch with the harness session preset, the act record holding item, work order, harness, harness session, node and cause, and the session's cost and duration from its JSON result (P35, P36)",
        "the commit queue writing the `Gov-*` trailers from the act binding, a `prepare-commit-msg` filler in the owner's session, and the commit-key leg at the push reading the binding, as `commits.edge-check` says",
        "`gov trace <key>` and `gov why <key>` over the one index, journal lines keyed by act or session, the health and stall logs folded into the journal grammar, and a fixture replaying four recorded events, each answered in one query (P35)",
        "the session node derived from bindings, joined to its act by `runs-in` and to its predecessor by `after`, live delivery through a session's inbox where its conformance row passes, and the card's session list filled through the harness adapter (P36)",
        "the harness conformance fixture: launch by a program, id preset or returned, resume, headless fork, schema return, the hook events and fields the packs read, the fail-closed path, the live inbox, transcript homes and interpreters, measured per binary into the node registry with OS, shell and interpreter versions (P36, P37)",
        "preflight refusing a launch that skips hooks or permissions, a launch-environment allowlist scrubbing the parent's messaging token, entrypoint and session variables, a transient-auth relaunch class, and worktree pointers written relative (P36, P37)",
    ], ["gap-rt-25", "gap-rt-26", "gap-rt-27", "gap-rt-28", "gap-rt-29", "gap-rt-30", "gap-rt-31", "gap-orient-19",
        "gap-tool-14", "gap-tool-16", "gap-tool-18"]),
    "dTendedCadence": ([
        "readings for an act launched with no outcome past `runtime.act-ceiling`, a node's run left unrecorded, and a pushed commit missing a required key (P35)",
    ], ["gap-maint-14"]),
    "dCalibratedLens": ([
        "the Loop Review pricing cost per item kind from trace rows (P35)",
    ], []),
    "dShippedRelease": ([
        "the receipt's schema 4 gaining `steps`, `superseded`, `deprecations` and `prior_commit`, `kits.currency` and the fleet register reading steps pending and shim calls, and `kits.offer` running the steps that need no target code, as `install.steps` says (P38)",
        "the lander running each new upgrade step on gov's own tree in the prepared merge, recorded in the source-mode receipt, gov's deploy plan accepted, a stale lock reclaimed, withdrawn hook fragments unwired, and an edited retired file kept as a `forked` row with an order, as `install.retired-edits` says (P38)",
        "the platform matrix verified per release: platform runner adapters for `platforms.supported` under `platforms.verify`, generalizing `run-held-wsl.sh`, per-kit interpreter floors in the kit factory and the receipt, and a Linux job in emitted CI (P37)",
        "`carries` on the landing record, a publication recorded as a release per (SHA, artifact environment), a squash re-emitting the union of trailers as `commits.squash` says, and Codex install targets with their trust step surfaced (P36)",
    ], ["gap-deploy-18", "gap-deploy-19", "gap-deploy-20", "gap-deploy-21", "gap-deploy-22", "gap-deploy-23",
        "gap-tool-11"]),
    "dConvergedCharter": ([
        "the guides' positional citations migrated to tags, legacy anchors kept as aliases, and the per-directory line-ending pins retired into class pins (P34, P37)",
        "the conf fold and the unattended kit's retirement shipped as upgrade steps, every shim removed when its window closes, and the exit check widened: every registered adopter at the converged commit with no step pending, or an owner item for that adopter (P38)",
    ], []),
    "dPlacedRequest": ([
        "the kickoff manifest's facts as level-2 instruction units the card reads (the memory plan's `[pockets]`)",
    ], ["gap-orient-20"]),
}
chain = V.text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
for build, (clauses, gaps) in UNITS.items():
    for c in clauses:
        if "; " in c or "|" in c:
            sys.exit(f"{build}: a clause holds a split: {c[:60]}")
    lines = [ln for ln in chain.split("\n") if ln.startswith(f"| {build} | ")]
    if len(lines) != 1:
        sys.exit(f"{build}: {len(lines)} chain rows")
    cells = lines[0].split(" | ")
    # | build | stage | after | units | gaps |
    m = re.match(r"^(\| \S+ \| [^|]+ \| [^|]+ \| )(.+)( \| )([^|]+)( \|)$", lines[0])
    if not m:
        sys.exit(f"{build}: the row does not parse")
    units = m.group(2) + "; " + "; ".join(clauses)
    gapcell = m.group(4) + ("".join(", " + g for g in gaps) if gaps else "")
    V.sub(lines[0], m.group(1) + units + m.group(3) + gapcell + m.group(5), f"{build} row")

V.insert_before("\nRevised: 2026-10-17, after the folds' closing review", """
Revised: 2026-10-18, the away pass (""" + AWAY + """), the owner's six points worked in while the owner
was away: P34 to P38 are added and P33's closed set grows by eleven types (the memory plan, """ + PLAN + """); seventeen keys join the catalogue, thirteen of them every preset and four the keys
presets never touch; [chain] rows gain the units the six points need, each on its own build or one it depends on;
the forks AP-1 to AP-30 are parked.
""", "revision note")
V.save()

# ---- the gap register ---------------------------------------------------------------------------------------------
G = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
NEW = {
    "gap-mem-34": [
        ("gap-mem-35", "Memory", "HIGH", "The closed edge set cannot carry the cycle the owner asked for: a record serving a unit, who made a thing and why, the instruction an act followed, a return answering its work order, an act's session, what a landing carried, a pin, an item's reads and writes, and a promotion have no type. Five of twelve hops on one feature need prose or search, and four of seven from one commit.", "`research-memory-pockets.md` section 4; `research-git-pockets.md` section 4; the memory plan `[edges]`"),
        ("gap-mem-36", "Memory", "MED", "Record sections declare no edges: outside dClosedLoop no record heading carries a tag, and the Serves line is the only typed link a record holds.", "`research-memory-pockets.md` section 2"),
        ("gap-mem-37", "Memory", "MED", "The kind registry declares an owner and a writer only: home, lifecycle, readers and layer are undeclared for every kind, and views, row registries, the archive, instruments and the pockets outside the tree have no kind.", "`research-memory-pockets.md` sections 2 and 5; `research-git-pockets.md` section 3"),
        ("gap-mem-38", "Memory", "LOW", "\"journal\" names two kinds: a Serves kind on 1,436 records and Runtime's journal.", "`research-memory-pockets.md` section 2"),
        ("gap-mem-39", "Memory", "MED", "Decision rows and bug classes relate to nothing they decide or came from: a feature edge on 0 of 200 decision rows, and `from:` on 0 of 149 bug classes.", "`research-memory-pockets.md` sections 2 and 4"),
        ("gap-mem-40", "Memory", "LOW", "A design-only build's records name a unit no spec defines, so the bindings check reports a row for each of them.", "`research-memory-pockets.md` section 2"),
    ],
    "gap-roles-22": [
        ("gap-roles-23", "Roles", "MED", "Most handoffs carry no typed marker, 59 of 595, and a return names the work order it answers only in prose.", "`research-memory-pockets.md` sections 2 and 4"),
    ],
    "gap-spine-07": [
        ("gap-spine-08", "Spine", "HIGH", "No commit names the item, act or session that made it, 0 of 6,084, and the trailer schema the flow records name is declared nowhere.", "`research-git-pockets.md` section 2"),
        ("gap-spine-09", "Spine", "LOW", "`Pass:` has two readers that disagree: one unions the subject's ids with the trailer's, the other lets the trailer replace them.", "`research-git-pockets.md` section 2"),
    ],
    "gap-rt-24": [
        ("gap-rt-25", "Runtime", "HIGH", "No record carries a key to its cause and no verb walks one: four past events each took six sources and eight or nine lookups to rebuild, and each left a question no record answers.", "`research-observability-trace.md` sections 2 and 3"),
        ("gap-rt-26", "Runtime", "MED", "An act records no cost or duration; committed cost covers review acts' output tokens only.", "`research-observability-trace.md` section 2"),
        ("gap-rt-27", "Runtime", "MED", "The journal carries no act or session key, and the health and stall logs carry no key at all, so a reap joins its bar only by the matching second.", "`research-observability-trace.md` sections 2 and 3"),
        ("gap-rt-28", "Runtime", "HIGH", "An act session inherits its parent's entrypoint, session variables and messaging token, a secret that posts into the parent's inbox.", "`research-harness-cli.md` section 4"),
        ("gap-rt-29", "Runtime", "MED", "The CLI on PATH and the application's bundled CLI drift apart, 2.1.292 against 2.1.299, the PATH one lacking a hook field the design needs, and a turn limit in use is undocumented.", "`research-harness-cli.md` section 3"),
        ("gap-rt-30", "Runtime", "MED", "No preflight refuses a launch that skips hooks or permissions (`--bare`, `--safe-mode`, the skip flag).", "`research-harness-cli.md` section 4"),
        ("gap-rt-31", "Runtime", "MED", "No fixture measures a harness adapter's capabilities: the Codex row went stale within days, and nothing separates what a harness can do from what an adapter claims.", "`research-harness-cli.md` sections 3 and 4"),
    ],
    "gap-orient-18": [
        ("gap-orient-19", "Orient", "MED", "A session is no node: its id keys a per-session card and a run claim, and joins nothing else.", "`research-harness-cli.md` section 5"),
        ("gap-orient-20", "Orient", "LOW", "The kickoff manifest has no record kind and no instruction unit; the card reads a guide.", "`research-memory-pockets.md` section 2"),
    ],
    "gap-test-19": [
        ("gap-test-20", "Test", "MED", "A failing leg's output lives in its worktree's run directory and dies with the worktree.", "`research-observability-trace.md` section 2"),
    ],
    "gap-maint-13": [
        ("gap-maint-14", "Maintain", "MED", "A node that dies before its journal reader writes the run record leaves a run nothing detects.", "`research-observability-trace.md` section 2"),
    ],
    "gap-deploy-14": [
        ("gap-deploy-15", "Deploy", "HIGH", "A receipt naming a retired or absorbed kit refuses the whole update, and `check` reds on it.", "`research-supersession.md` section 2, probe A"),
        ("gap-deploy-16", "Deploy", "HIGH", "No upgrade-step kind: a moved conf key is only reported, an old record shape is carried by date cutoffs, and the backlog migration stands alone.", "`research-supersession.md` section 2"),
        ("gap-deploy-17", "Deploy", "MED", "No rollback across versions: a downgrade is refused, and rollback exists only inside one run, per kit.", "`research-supersession.md` section 2"),
        ("gap-deploy-18", "Deploy", "MED", "An adopter's edit to a file gov retired reads as patched with no order, and a withdrawn hook stays wired.", "`research-supersession.md` section 2"),
        ("gap-deploy-19", "Deploy", "MED", "A half-applied update leaves a lock and staged paths that an operator clears by hand.", "`research-supersession.md` section 2"),
        ("gap-deploy-20", "Deploy", "MED", "gov cannot run `update` on itself, and `plan` refuses gov's own deploy file.", "`research-supersession.md` section 2, probe B"),
        ("gap-deploy-21", "Deploy", "LOW", "A Codex project hook is skipped until it is trusted, and no install step surfaces the trust.", "`research-harness-cli.md` section 3"),
        ("gap-deploy-22", "Deploy", "LOW", "A squash merge drops every trailer, at an adopter that squashes.", "`research-git-pockets.md` section 2"),
        ("gap-deploy-23", "Deploy", "LOW", "A publication records no tree: the atlas is published by hand, and nothing names what it showed.", "`research-git-pockets.md` section 3"),
    ],
    "gap-tool-09": [
        ("gap-tool-10", "Tooling", "LOW", "No release-0 adopter tree exists as a fixture: govkit's only fixture is a receipt, and its rename arm is graded by authored fixtures alone.", "`research-supersession.md` section 2"),
        ("gap-tool-11", "Tooling", "HIGH", "No platform matrix is declared: only Windows with Git-Bash is tested, and under WSL two of three read-only kit checks fail.", "`research-compatibility.md` sections 2 and 4"),
        ("gap-tool-12", "Tooling", "HIGH", "The Python resolver accepts an interpreter below the floor and prefers the Store alias, four times slower to spawn than the direct executable.", "`research-compatibility.md` section 2"),
        ("gap-tool-13", "Tooling", "MED", "Line-ending pins are per-directory instances, not the class: most Python files check out with CRLF in a worktree.", "`research-compatibility.md` section 4"),
        ("gap-tool-14", "Tooling", "MED", "node is an undeclared hard dependency: ten of thirteen hook commands run it, and the toolchain fact names bash and Python only.", "`research-compatibility.md` section 2"),
        ("gap-tool-15", "Tooling", "MED", "gate-lint ships its encoding-posture check with no adopter leg.", "`research-compatibility.md` section 4"),
        ("gap-tool-16", "Tooling", "MED", "A worktree's pointer holds a Windows path that WSL's git cannot open.", "`research-compatibility.md` section 2"),
        ("gap-tool-17", "Tooling", "LOW", "A bug class carries no cause, language or platform field.", "`research-compatibility.md` section 5"),
        ("gap-tool-18", "Tooling", "LOW", "The node registry's platform facts are free text.", "`research-compatibility.md` section 5"),
        ("gap-tool-19", "Tooling", "MED", "No practice gives each language its role: shell grows outside shims, and each kit picks its own launch, encoding and path idioms.", "`research-compatibility.md` section 3"),
    ],
}
for after, rows in NEW.items():
    lines = [ln for ln in G.text.split("\n") if ln.startswith(f"| {after} |")]
    if len(lines) != 1:
        sys.exit(f"register: {len(lines)} rows for {after}")
    G.sub(lines[0] + "\n", lines[0] + "\n" + "".join(f"| {k} | {s} | {v} | {g} | {e} | — |\n" for k, s, v, g, e in rows),
          f"after {after}")
G.sub("| gap-rt-09 | Runtime | LOW | gov wires none of the five hook events Codex ships. |",
      "| gap-rt-09 | Runtime | LOW | gov wires none of the five hook events Codex ships. Revised 2026-10-18, the away pass: Codex now documents twelve, SessionStart, Stop and PostCompact among them, each project hook trusted by hash before it runs (`research-harness-cli.md` section 3). |",
      "gap-rt-09")
G.sub("and Codex has no SessionStart, so only the harness adapter's launch input can carry the card.",
      "and Codex has no SessionStart, so only the harness adapter's launch input can carry the card. Revised 2026-10-18, the away pass: Codex now has SessionStart, so a trusted hook can carry the card (`research-harness-cli.md` section 3).",
      "gap-rt-11")
G.save()

# ---- the kind registry --------------------------------------------------------------------------------------------
M = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md")
last = [ln for ln in M.text.split("\n") if ln.startswith("| lexicon declaration | dMindYourWords |")]
if len(last) != 1:
    sys.exit(f"contract: {len(last)} lexicon rows")
KINDS = [
    ("commit", "dDeclaredLoop", "a git commit, its `Gov-*` trailers an edge site; written by the commit queue from the act binding and by the owner's `prepare-commit-msg` filler (the memory plan, the away pass)"),
    ("view", "dTotalRecall", "a generated view: LIVE.md, the ledger, the ask views; re-rendered, never merged (the away pass)"),
    ("registry", "dWitnessedBar", "a gate's row registry under `memory/project/`, written by its gate's pin emitter (the away pass)"),
    ("archive", "dTotalRecall", "a rotated record under `memory/archive/`, written by rotation (the away pass)"),
    ("instrument", "dTotalRecall", "a script, table or drawing kept beside the record it serves (the away pass)"),
    ("witness", "dTotalRecall", "a declared pocket outside the tree, such as a transcript, a Codex rollout, the auto-memory, the live inbox or a scheduled task: its home, key and reader, written by its own owner and never by `record` (the away pass)"),
]
M.sub(last[0] + "\n", last[0] + "\n" + "".join(f"| {k} | {o} | {w} |\n" for k, o, w in KINDS), "kinds")
M.save()

# ---- the runtime record's Codex facts ------------------------------------------------------------------------------
R = Record(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md")
R.sub("""    - its own docs call its hooks "not a complete enforcement boundary".
""", """    - its own docs call its hooks "not a complete enforcement boundary".
    - Revised 2026-10-18, the away pass (`build/2026-10-18-build-PLAY-dClosedLoop-1-research-harness-cli.md` section
      3): Codex CLI 0.139 documents twelve hook events, SessionStart, PermissionRequest, UserPromptSubmit, Stop and
      PostCompact among them, each project hook trusted by hash before it runs. The conformance fixture re-measures
      its row (P36).
""", "codex facts")
R.save()
````

### `fix_presets.py`

Two new keys' values spelled the way the preset check and their siblings read them.

````python
"""Spell two new keys' allowed values the way the preset check and their siblings read them.

Usage: python -X utf8 fix_presets.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

V = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
V.sub("| `runtime.act-harness` | a registered harness adapter that passes the act rows | claude-code |",
      "| `runtime.act-harness` | claude-code, codex, or another registered harness adapter that passes the act rows | claude-code |",
      "act-harness values")
V.sub("| `install.deprecation-window` | 0, 1, 2, 4 releases | 2 | the away pass, point 6: equal to",
      "| `install.deprecation-window` | 0, 1, 2, 4 | 2 | the away pass, point 6: a window counted in releases, equal to",
      "window values")
V.save()
````

### `fold_classes.py`

The two citations the away pass's clauses made on a non-ancestor's node, classed as homonyms once the reconciliation probe reddened on them.

````python
"""Class the two citations the away pass's clauses made on a non-ancestor's node: both homonyms.

Usage: python -X utf8 fold_classes.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

R = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md")
lines = R.text.split("\n")
head = lines.index("| Row | Node | Owner | Class | Why |")
end = head + 2
while end < len(lines) and lines[end].startswith("| "):
    end += 1
last = lines[end - 1]
R.sub(last + "\n", last + "\n"
      "| dGroundRules | `check` | dWitnessedBar | homonym | govkit's `check` verb beside `update`, which reads the `[[retired]]` rows, not the `check` tag namespace (the away pass) |\n"
      "| dTotalRecall | `journal` | dWellOiledMachine | homonym | the Serves kind named `journal`, which the registry renames `log`, not Runtime's journal record kind (the away pass) |\n",
      "class rows")
R.save()
````

### `fix_cycle_table.py`

The memory plan's cycle table given its families and a leading state word, so the atlas derives its memory diagram.

````python
"""Give the memory plan's [cycle] table the families each hop joins, and a status word leading each Today cell, so
the atlas derives its memory diagram from the record.

Usage: python -X utf8 fix_cycle_table.py   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

P = Record("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md")
old = P.text.split("| Hop | Edge | Today | Planned site |", 1)[1].split("\n\n", 1)[0]
old = "| Hop | Edge | Today | Planned site |" + old
new = """| Hop | From | To | Edge | Today | Planned site |
|---|---|---|---|---|---|
| charter practice → feature-scoped units | instruction | instruction | `instructs` | prose | the unit's `select` naming `feature.<name>` |
| units → work order | instruction | instruction | `instructs` | partly typed: `rules:` on role definitions | the work order's rendered slots, by tag |
| work order → act | instruction | runtime | `follows` | none | the act record's `task-sha` |
| act → session | runtime | runtime | `runs-in` | none: the run claim carries a session in prose | the session binding |
| act → commit | runtime | git | `made-by` | search: by SHA across transcripts | the `Gov-Act:` trailer |
| commit → unit and item | git | trail | `serves` (through `Gov-Unit:`), `made-by` | partly typed: the subject's scope, unchecked | `Gov-Unit:` and `Gov-Item:` trailers |
| commit → landing | git | trail | `carries` | none: landing records are designed | the landing record |
| landing → verdict | trail | trail | `caused-by` | none | the verdict record's parent |
| return → work order | trail | instruction | `answers` | prose: in most research records | the return's header |
| record → unit | trail | trail | `serves` | typed, and graded both ways | the Serves line, as today |
| finding → bug class | trail | library | `caused-by` | none: `from:` on 0 of 149 | the class's header |
| decision → feature, commit | library | git | `decides` | none: on 199 of 200 rows | the row's edge line; `Decided:` trailers |
| bug class, decision → unit | library | instruction | `promoted-from` | none: no route | `instructions.edit` |
| feature → code | library | code | `part-of`, `implements` | typed at kit level | annotations and claims |"""
P.sub(old, new, "cycle table")
P.save()
````

### `price_ap25.py`

AP-25 priced: the upgrade-step kind in dGroundRules, in a build of its own, or in dShippedRelease with adopters held.

````python
"""Price AP-25: where the upgrade-step kind is built. Reads v2's [chain] as committed in the working tree, then moves
the step kind's four dGroundRules clauses (each naming `[[upgrade]]`, `update` walking, down steps, or the release-0
fixture) to each candidate home in memory, and prints the critical path for each. Writes nothing.

Usage: python -X utf8 price_ap25.py   (from the worktree root)
"""
import re

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
chain = open(V, encoding="utf-8").read().split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
units, parents, clauses = {}, {}, {}
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        clauses[m.group(1)] = [u for u in m.group(3).split("; ") if u.strip()]
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]
STEP = ("the upgrade-step kind", "`update` walking every step", "down steps run in reverse", "the release-0 fixture tree")
moved = [c for c in clauses["dGroundRules"] if c.startswith(STEP)]
assert len(moved) == 4, moved


def path(units, parents):
    finish = {}

    def f(b):
        if b not in finish:
            finish[b] = max([f(p) for p in parents[b]] or [0]) + units[b]
        return finish[b]
    end = max(units, key=f)
    chain_, b = [end], end
    while parents[b]:
        b = max(parents[b], key=f)
        chain_.append(b)
    return finish[end], " > ".join(reversed(chain_))


base = {b: len(c) for b, c in clauses.items()}
print("as placed, in dGroundRules: %d units, %s" % path(base, parents))
alt = dict(base, dGroundRules=base["dGroundRules"] - 4, dShippedRelease=base["dShippedRelease"] + 4)
print("in dShippedRelease, adopters held until it lands: %d units, %s" % path(alt, parents))
new = dict(base, dGroundRules=base["dGroundRules"] - 4, dHandedOverStandIn=4)
par = dict(parents, dHandedOverStandIn=["dGroundRules"])
par["dOrderedCharter"] = parents["dOrderedCharter"] + ["dHandedOverStandIn"]
print("a build of its own between dGroundRules and dOrderedCharter: %d units, %s" % path(new, par))
````

### `write_impact_forks.py`

The away-pass record's [chain-impact] and [forks], the path and prices spliced from their runs.

````python
"""Append the away pass's [chain-impact] and [forks] to its record, the path and AP-25's prices spliced from their runs.

Usage: python -X utf8 write_impact_forks.py <cp-after.out> <price_ap25.out>   (from the worktree root)
"""
import pathlib
import sys

cp = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n").strip()
pr = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").replace("\r\n", "\n").strip()
F = "`" * 3
rec = pathlib.Path("memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md")
t = rec.read_text(encoding="utf-8")
if "## [chain-impact]" in t:
    sys.exit("the record already holds [chain-impact]")
FORKS = [
    ("AP-1", "How does a record section declare its edges? (a structural decision)", "one `**Edges:**` line under the heading, as the Serves line declares the record's; front matter keyed by section; a sidecar per record", "the plan's `[sites]`"),
    ("AP-2", "How far does the closed edge set grow? (a structural decision)", "the eleven types, each needed by a measured hop; a core four (`serves`, `made-by`, `caused-by`, `answers`) with the rest as record fields; `part-of` and `cites` widened to carry them", "P33's closed set"),
    ("AP-3", "`memory.legacy-records`: how do today's records reach the plan?", "backfill: Serves lines read as edges, derived anchors, no file rewritten; anchors-only; retag every record", "the key's default"),
    ("AP-4", "How does a design-only build's unit become a node?", "the build README's `ids:` defines it; design-only builds exempt from the bindings check", "dTotalRecall's registry"),
    ("AP-5", "How does git join the syntax? (a structural decision)", "typed trailers, one key per edge, mapped in the registry; one `Gov-Edge:` key; git notes; a derived commit index alone", "dDeclaredLoop's commit node"),
    ("AP-6", "`commits.edge-check`: where are the trailers checked?", "push-leg, reading the binding; commit-msg; off", "the key's default"),
    ("AP-7", "`commits.squash`: what happens to trailers on a squash?", "re-emit-union; refuse; accept-loss", "the key's default"),
    ("AP-8", "`trace.identity`: may committed memory name a session?", "act-only, as the owner's rule of 2026-09-13 keeps; session; salted", "the key's default, never set by a preset"),
    ("AP-9", "What are transcripts and the auto-memory to the graph?", "witnesses with keyed pointers; nodes; out", "the plan's `[pockets]`"),
    ("AP-10", "How does gov stay independent of the owner's application? (a structural decision)", "harness adapters with one conformance fixture, the CLI first, any application a viewer; the desktop app as the runtime; the CLI alone", "P36"),
    ("AP-11", "`runtime.binary`: which CLI does the supervisor launch?", "newest-conforming, read from the node registry; path; app-bundled; a pinned path", "the key's default"),
    ("AP-12", "`runtime.owner-harness`: which application is the owner's viewer?", "auto, taken from the session's binding; a named adapter", "the key's default, never set by a preset"),
    ("AP-13", "`runtime.act-harness`: which harness runs acts?", "claude-code; codex, once its rows pass", "the key's default"),
    ("AP-14", "`runtime.act-auth`: how does an act authenticate?", "oauth-shared, with transient retries; setup-token; api-key", "the key's default, never set by a preset"),
    ("AP-15", "Which coding practice does gov follow? (a structural decision)", "a role per language, gated, ratcheting toward Python; Python-first now; node-first; a compiled binary", "P37"),
    ("AP-16", "What language do harness hooks use?", "node, declared as a dependency; Python", "P37's roles"),
    ("AP-17", "`platforms.supported`: which platforms does gov promise?", "windows-gitbash and linux; add macos; add pwsh-launch", "the key's default, never set by a preset"),
    ("AP-18", "`platforms.verify`: how are they verified?", "held, until the Linux half is green, then ci; bar; ci; off", "the key's default"),
    ("AP-19", "Which Python does gov require?", "3.11, the resolver naming how to provision it; 3.10, with a vendored TOML parser", "the interpreter floor"),
    ("AP-20", "How are worktree pointers written?", "relative, tested first against WSL's git; absolute, WSL worktrees unsupported", "dWellOiledMachine's isolation"),
    ("AP-21", "`trace.cost`: what does a committed act record carry?", "tokens and wall time, from the act's own output, never a journal time of day; tokens; none", "the key's default; the owner's rule of 2026-09-16 bears on it"),
    ("AP-22", "`trace.leg-output`: where does a failing leg's output live?", "tail-by-hash, committed; node-local", "the key's default"),
    ("AP-23", "`trace.rows`: how long is a timeline?", "60 rows, folding by kind past that; 120; all", "the key's default"),
    ("AP-24", "How do the rebuilt kits supersede today's? (a structural decision)", "release-chained upgrade steps, up and down; one epoch release; shims alone; a translation layer alone", "P38"),
    ("AP-25", "Where is the upgrade-step kind built? (a structural decision)", "in dGroundRules, as placed; a build of its own between dGroundRules and dOrderedCharter, named by the owner, at the same path; in dShippedRelease, adopters held at today's kits until it lands, two units shorter", "the chain"),
    ("AP-26", "`install.deprecation-window`: how long does an old surface keep working?", "2 releases; 0; 1; 4", "the key's default"),
    ("AP-27", "`install.on-shim-call`: what does a forwarded call do?", "warn, journaled for the fleet view; journal only; refuse", "the key's default"),
    ("AP-28", "`install.retired-edits`: what happens to an adopter's edit of a retired file?", "order: kept, marked forked, with an order; keep silently; delete", "the key's default"),
    ("AP-29", "`install.steps`: who runs an upgrade step?", "offer: gov's no-target-code mode, a step needing the target's code falling back to attended; attended always", "the key's default"),
    ("AP-30", "How does gov itself migrate? (P8)", "the lander runs each new step on gov first, recorded in its source-mode receipt; gov's own diff is its migration", "dShippedRelease's lander unit"),
]
rows = "\n".join(f"| {a} | {q} | {o} | {s} |" for a, q, o, s in FORKS)
t = t.rstrip("\n") + f"""

## [chain-impact] What the away pass did to the chain

The chain keeps its twenty builds; no build is added, split or reordered, and the one structural question, where
the upgrade-step kind lives, is parked as AP-25. Thirteen builds gain units, 30 in all, each clause on its own build
or one it depends on:

| Build | Units added | For |
|---|---|---|
| dGroundRules | 4 | the upgrade-step kind, its walk, its down steps and its fixture (point 6) |
| dOrderedCharter | 4 | the edge grammar, the writing practice's checks, the portable practice, its own upgrade steps (points 1, 4, 6) |
| dDeclaredLoop | 1 | the commit node and its trailer keys (point 1) |
| dPlacedRequest | 1 | the kickoff manifest as instruction units (point 1) |
| dWitnessedBar | 2 | the portability leg pack, and the verdict's cause and leg tails (points 4, 5) |
| dTotalRecall | 2 | the completed kind registry, and `record`'s header and edge line (points 1, 5) |
| dLinkedLibrary | 1 | decision and bug-class edges (points 1, 4) |
| dBoundRoles | 1 | markers on every work order, `answers` on every return (point 1) |
| dWellOiledMachine | 6 | the act key, trailers, the trace verbs, the session node, the conformance fixture, preflight (points 1, 3, 4, 5) |
| dTendedCadence | 1 | readings for missing outcomes, runs and keys (point 5) |
| dCalibratedLens | 1 | the Loop Review priced from trace rows (point 5) |
| dShippedRelease | 4 | the receipt and fleet for steps, gov first, the platform matrix, landings and publications (points 1, 3, 4, 6) |
| dConvergedCharter | 2 | the migration to tags and class pins, and the steps that close the convergence (points 1, 4, 6) |

The path, recomputed by `critical_path.py` on the folded tree, against the one the walk closed with at `fa62092db`:

{F}text
before, at fa62092db: critical path 171 units over 335
{cp}
{F}

It grows by 19 units. Its run moves from dLinkedLibrary and dIndexedDesign onto dWellOiledMachine, whose six new
units make it finish one unit after dIndexedDesign. AP-25's homes for the step kind, priced the same way:

{F}text
{pr}
{F}

Holding adopters back until dShippedRelease saves two units, because dShippedRelease then becomes the critical
build, and it would freeze every adopter on today's kits through the whole chain. The other effects:
- **The gap register** grows by 39 gaps, every one owned by exactly one build: Memory 6, Roles 1, Spine 2,
  Runtime 7, Orient 2, Test 1, Maintain 1, Deploy 9, Tooling 10. Two Codex rows, `gap-rt-09` and `gap-rt-11`, are
  amended with Codex's current hooks.
- **The catalogue** gains 17 keys, 13 of them in every preset and 4 among the keys presets never touch.
- **The principles** gain P34 to P38, and P33's closed set eleven types.
- **The kind registry** gains six kinds: commit, view, registry, archive, instrument and witness.
- **The level-0 map** now uses its degrade order, shortening purposes to 40 characters to stay within its budget,
  as its design allows; gap-mem-30's owed measurement covers it.
- **The atlas** gains its Memory view, derived from the plan record and the kind registry.

## [forks] Parked for the owner, 2026-10-18

Thirty forks, each with the recommendation first. A key's default stands as recommended until the owner answers.

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
{rows}
"""
rec.write_text(t + "\n", encoding="utf-8", newline="\n")
print("away-pass record:", len(t.splitlines()), "lines")
````

### `tally.py`

The gap register's tally by stage and severity; it reproduces the register's last recorded tally at fa62092db.

````python
"""The gap register's tally by stage and severity, in the order the register's earlier re-measures print it.

Usage: python -X utf8 tally.py <gap-register.md>
"""
import collections
import re
import sys

rows = re.findall(r"^\| (gap-[a-z]+-\d\d) \| ([A-Za-z]+) \| (HIGH|MED|LOW)\b", open(sys.argv[1], encoding="utf-8").read(), flags=re.M)
stage = collections.Counter(r[1] for r in rows)
sev = collections.Counter(r[2] for r in rows)
ORDER = ["Roles", "Deploy", "Plan", "Spine", "Orient", "Test", "Runtime", "Lexicon", "Tooling", "Review", "Foundation",
         "Build", "Memory", "Flow", "Maintain", "Design"]
extra = sorted(set(stage) - set(ORDER))
print(" ".join(f"{s}={stage[s]}" for s in ORDER + extra))
print(" ".join(f"{s}={sev[s]}" for s in ("LOW", "MED", "HIGH")))
print(f"rows {len(rows)}")
````

### `log_away.py`

The register's re-measure and the session log's dispatch rows, agent lines and event.

````python
"""Record the away pass in the gap register's tally and the session log: the register re-measured, the six dispatch
rows, their derived agent lines, and the pass's event.

Usage: python -X utf8 log_away.py <tally-after.out> <agent-lines.txt>   (from the worktree root)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "expansions"))
from fold_lib import Record  # noqa: E402

tally = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n").strip().split("\n")[:2]
agents = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").replace("\r\n", "\n").strip()
if agents.count("- agent —") != 6 or agents.count("- returned —") != 6:
    sys.exit("six agent and six returned lines expected")
F = "`" * 3
B = "memory/builds/dClosedLoop/build/"

G = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
G.text = G.text.rstrip("\n") + "\n\nRe-measured after the away pass added thirty-nine gaps, `gap-mem-35` to `gap-mem-40`, `gap-roles-23`,\n" \
    "`gap-spine-08` and `gap-spine-09`, `gap-rt-25` to `gap-rt-31`, `gap-orient-19` and `gap-orient-20`, `gap-test-20`,\n" \
    "`gap-maint-14`, `gap-deploy-15` to `gap-deploy-23` and `gap-tool-10` to `gap-tool-19`\n" \
    "(`build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md` `[chain-impact]`), same instrument. A join of these 294 keys\n" \
    "against v2's chain rows finds each owned by exactly one build:\n\n" + F + "text\n" + "\n".join(tally) + "\n" + F + "\n"
G.done += 1
G.save()

L = Record(B + "2026-10-14-build-PLAY-dClosedLoop-1-session-log.md")
row105 = [ln for ln in L.text.split("\n") if ln.startswith("| 105 |")]
if len(row105) != 1:
    sys.exit("no single dispatch row 105")
P = "`prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-%d-researcher.md`"
R = "`build/2026-10-18-build-PLAY-dClosedLoop-1-research-%s.md`"
ROWS = [
    (106, "The away pass's point 1: the memory the repository holds, under one writing practice", 9, "returned, 9m46s, 49.5k out: 27 pockets, the Serves line the one typed link end to end, an edge line under each heading", "memory-pockets"),
    (107, "Point 1: git and the memory outside the tracked files", 10, "returned, 9m32s, 49.6k out: typed commit trailers, notes and a derived index each losing a test", "git-pockets"),
    (108, "Point 3, and point 1's session ids: the harness and its CLI, tested", 11, "returned, 8m58s, 44.1k out: a headless session run and resumed by id; adapters with one conformance fixture", "harness-cli"),
    (109, "Point 4: one coding practice across platforms, tested", 12, "returned, 11m08s, 48.0k out: a role per language, gated; WSL fails two of three checks", "compatibility"),
    (110, "Point 5: pointing at any part of the flow and telling what happened", 13, "returned, 8m30s, 43.7k out: not as designed; a cause on every record, cost on acts, a trace verb", "observability-trace"),
    (111, "Point 6: the rebuilt kits superseding today's, seamlessly", 14, "returned, 7m28s, 40.1k out: release-chained upgrade steps; a retired kit refuses today's whole update", "supersession"),
]
new = "\n".join(f"| {d} | gov-researcher, at the owner's medium effort | {stage} | {P % p} | 1799cb98 | {out} | {R % rec} |"
                for d, stage, p, out, rec in ROWS)
L.sub(row105[0] + "\n", row105[0] + "\n" + new + "\n", "dispatch rows")
L.insert_before("\n## Events\n", "\nThe away pass's researchers, dispatches 106 to 111, derived the same way:\n\n" + F + "text\n" + agents + "\n" + F + "\n",
                "agent lines")
L.insert_before("\n## Instruments\n", """
- 2026-10-18, session 1799cb98: the owner handed six points and stepped away (the away-pass record's `[words]`). Six
  researchers ran, dispatches 106 to 111, and the design took each point in: the instruction and memory plan
  (`build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`), P34 to P38, 17 keys, 39 gaps, 30 units on 13 builds,
  and the atlas's Memory view. The forks AP-1 to AP-30 are parked for the owner.
""", "event")
L.save()
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
    ("night/build_args_night.py", "The closing review's args: a light diff review of the night-pass commit at medium."),
    ("night/plain_cites.py", "H2: plain-word spellings of a non-ancestor's record kind in the chain rows, measured."),
    ("night/pinned_counts.py", "After the fold's commit: the design records' quoted map counts and their pins, run over "
     "the real tree before the map's arm was written."),
    ("night/pinned_counts2.py", "The same, widened to the class: every derived count the map's arm reads, each with its "
     "disposition, through the generator's own patterns."),
    ("night/fold_np_self.py", "The night pass's own sweep while the review ran: one actor per probe item, the "
     "observation entry.place returns, verify-at-plan's route, and Design's seventh input."),
    ("night/fold_np_residue.py", "Residue: layer-roles' driver sentence, and the owner's session named in the design "
     "text."),
    ("night/fold_review_np.py", "The closing review's fold into the design records."),
    ("night/fix_map_review.py", "The closing review's fold into the map's generator."),
    ("night/fold_np_record_review.py", "The night-pass record brought in line with the review's fold."),
    ("night/log_np.py", "The session log: dispatches 100 to 104 and the night's event."),
    ("night/log_review.py", "The session log: dispatch 105 and the review's fold."),
    ("night/plants_committed.sh", "The probe's earlier plant suite, pointed at the committed copy."),
    ("forks/chain_clauses.py", "The owner's answers: prints a chain row's planned-units clauses, numbered, to find each "
     "clause an answer touches."),
    ("forks/fold_answers.py", "The owner's answers to NP-1 to NP-24, folded into v2, the gap register, the fates "
     "record, the ownership record, flow-steps, the systems record and the night-pass record's summaries."),
    ("forks/write_answers.py", "Writes the night-pass record's `[answers]`, verbatim, and `[folded-answers]`, the "
     "register's re-measured tally and the session log's event."),
    ("forks/pin_np24.py", "Pins NP-24's answer line, which quotes the critical path, to the commit it was asked at. "
     "The map's arm was red on it first."),
    ("forks/node_users.py", "NP-24: each node a build owns, the clauses naming it, and the later builds depending on "
     "it by the gate's own rules."),
    ("forks/price_split_asked.py", "NP-24's pricing as the owner was asked from, before its two corrections."),
    ("forks/price_split.py", "NP-24's pricing, corrected: the classification, the candidate splits' critical paths and "
     "dCalibratedLens's slack."),
    ("forks/write_pricing.py", "Writes the pricing record from both runs, its table derived from the corrected one."),
    ("forks/fold_split.py", "The owner's S3 folded: the three rows, the moved owners, the parents, the class row, the "
     "fates destinations and the ownership amendment."),
    ("forks/fold_split_classes.py", "The four class rows whose citing clause moved, re-pointed once the gate was red on "
     "them."),
    ("forks/write_split_answers.py", "The pricing record's `[answers]` and `[folded]`, the night-pass record's owed line "
     "and the session log's event."),
    ("forks/fix_split_wording.py", "The `[folded]` class-row line, reworded to tell the owner row from the four citing "
     "rows."),
    ("order/critical_path.py", "The critical path over v2's `[chain]`, run by `[final]`. SP-1 raised its build count to "
     "18."),
    ("walk2/record_walk2.py", "The walk derived again: the owner's words, `[chain-2]`, `[wave-1-2]` and "
     "`[walk-instrument-2]` in the walk record."),
    ("walk2/fix_walk2.py", "Three corrections to the re-derivation, each checked against the records first."),
    ("walk3/stage_actors.py", "Wave 2: the stage items acted by a role no agent plays today, against the chain's "
     "order of dBoundRoles."),
    ("walk3/record_walk3.py", "The owner's word on wave 1, and wave 2 presented with its three forks."),
    ("walk3/fix_fork_ids.py", "Wave 2's forks renamed to a family the map counts, under a title the atlas reads as "
     "forks."),
    ("walk4/fold_wk.py", "The owner's word on wave 2, and WK-1 and WK-2 folded: the minimal tester, and dBoundRoles as "
     "a parent of dIndexedDesign and dRankedPlan."),
    ("wk3/gap_texts.py", "WK-4: each build's gaps with grade and text, to assign them across the split."),
    ("wk3/price_wk3_asked.py", "WK-3's pricing as the owner was asked from."),
    ("wk3/price_wk3.py", "WK-3's pricing as folded: the role-gate escape's fix kept in dBoundRoles' first part."),
    ("wk3/write_wk3.py", "Writes WK-3's pricing record from both runs."),
    ("wk3/fold_wk4.py", "The owner's C2 folded: the four rows, the moved owners, the parents, the kinds, the systems "
     "owner and the ownership amendment."),
    ("wk3/fold_wk4_classes.py", "The three class rows WK-4 moved, re-pointed once the gate was red on them."),
    ("wk3/fold_wk4_fates.py", "The fates record's thirteen destinations WK-4 moved."),
    ("wk3/write_wk4_answers.py", "The pricing record's `[answers]` and `[folded]`, the walk's WK-4 line and the session "
     "log's event."),
    ("walk5/leaves.py", "Wave 3: the builds no build waits on, and the fates rows each one owns."),
    ("walk5/record_walk5.py", "Wave 3 presented with its two forks."),
    ("walk6/fold_wk5.py", "The owner's word on wave 3, WK-5 folded: dMindYourWords a parent of dConvergedCharter."),
    ("walk7/lens_now.py", "Wave 4: SP-2 re-priced on today's chain, dConvergedCharter's parents and the Loop Review "
     "split."),
    ("walk7/record_walk7.py", "Wave 4 presented with its two forks."),
    ("walk8/adopter_probe.py", "WK-8's class over the real tree before it became the map's adopter-free arm: the "
     "planned units and node keys that name an adopter, and the purposes that do, which never ship."),
    ("walk8/fold_wk7_wk8.py", "The owner's word on wave 4: WK-7 keeps dCalibratedLens whole, WK-8 names the first "
     "engine adapter for its engine, and the walk completes."),
    ("away/fix_plan_deps.py", "The away pass: the memory plan's session units moved to dWellOiledMachine, the build that "
     "owns acts and bindings, once a dependency check found dKeptSession before it."),
    ("away/fold_away.py", "The away pass folded: P33 widened and P34 to P38, seventeen keys and their preset rows, the "
     "chain rows' thirty units and their gaps, thirty-nine gaps, six record kinds and the Codex facts."),
    ("away/fix_presets.py", "Two new keys' values spelled the way the preset check and their siblings read them."),
    ("away/fold_classes.py", "The two citations the away pass's clauses made on a non-ancestor's node, classed as "
     "homonyms once the reconciliation probe reddened on them."),
    ("away/fix_cycle_table.py", "The memory plan's cycle table given its families and a leading state word, so the "
     "atlas derives its memory diagram."),
    ("away/price_ap25.py", "AP-25 priced: the upgrade-step kind in dGroundRules, in a build of its own, or in "
     "dShippedRelease with adopters held."),
    ("away/write_impact_forks.py", "The away-pass record's [chain-impact] and [forks], the path and prices spliced "
     "from their runs."),
    ("away/tally.py", "The gap register's tally by stage and severity; it reproduces the register's last recorded "
     "tally at fa62092db."),
    ("away/log_away.py", "The register's re-measure and the session log's dispatch rows, agent lines and event."),
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
parts.append("""
## [review] The closing review's args, and its fold's red runs

The args dispatch 105 ran on, as `build_args_night.py` built them:

""" + block("json", read(S / "night/args-night-review.json")) + """
H2's measurement, re-run on the folded tree. The first fold read 47 mentions over 27 kinds:

""" + block("text", "$ python plain_cites.py\n" + run(str(S / "night/plain_cites.py"))[0]) + """
The committed probe's transitions rule, red before `repeat`'s row landed:

""" + block("text", read(S / "night/rc_h1_red.out") + "\nrc 1") + """
After the row, its two new plants:

""" + block("text", "$ python reconcile.py recut.md --plant-transition-drop repeat\n" + read(S / "night/rf_rcp.out")
                     + "\nrc 1\n$ python reconcile.py recut.md --plant-drop dDeclaredLoop:playbook\n"
                     + read(S / "night/rf_rcp2.out") + "\nrc 1") + """
The map on a fates record with one row widened by a cell, restored byte for byte afterwards:

""" + block("text", "$ python map.py --check\n" + read(S / "night/rf_wide.out") + "\nrc 1") + """
The earlier plant suite against the committed probe:

""" + block("text", read(S / "night/rf_plants.out")))
parts.append("""
## [after] After the fold's commit

The map's re-run at `15cec9200` read 2,235 nodes, where the night-pass record quoted 2,234. The predicate, run over the
build's records before any arm was written, took only a backticked sha for a pin:

""" + block("text", "$ python pinned_counts.py\n" + read(S / "night/pinned_counts.out")) + """
The map's arm, widened to a bare sha and a research record's cited line, on the records before their pins:

""" + block("text", "$ python map.py --check\n" + "\n".join(
    l for l in read(S / "night/map_unpinned_red.out").split("\n") if l.startswith(("FINDING", "map:"))) + "\nrc 1") + """
After that commit, `2403c49ba`, the class widened to the chain's critical path, skipping a fenced run capture. The
population, through the generator's own patterns, before the pins:

""" + block("text", "$ python pinned_counts2.py\n" + read(S / "night/pinned_counts2.out")) + """
The map's arm on the same tree:

""" + block("text", "$ python map.py --check\n" + "\n".join(
    l for l in read(S / "night/map_path_red.out").split("\n") if l.startswith(("FINDING", "map:"))) + "\nrc 1"))
parts.append("""
## [adopter-free] WK-8's class, before and after the fold

Wave 4 found a planned unit named for an adopter, which govkit selfcheck's arm 10 would refuse once built. The
predicate, run over the real tree before the arm was written, reports the purposes that name an adopter but grades
none of them:

""" + block("text", "$ python adopter_probe.py\n" + read(S / "walk8/adopter_probe.before.out")) + """
The map's adopter-free arm on the same tree, before the fold:

""" + block("text", "$ python map.py --check\n" + "\n".join(
    l for l in read(S / "walk8/map_adopter_red.out").split("\n") if l.startswith(("FINDING", "map:"))) + "\nrc 1") + """
The predicate after the fold, its purpose lines left out:

""" + block("text", "$ python adopter_probe.py\n" + read(S / "walk8/adopter_probe.after.out")) + """
The arm's two plants are re-run in `[plants]`, and the map's green run is in `[final]`.
""")
plants = []
for p in ("no-layer", "fates-absent", "fates-drop", "fates-ghost", "fates-bad", "fates-unbuilt", "fates-empty",
          "fates-kit", "fates-kit-drop", "fates-kit-ghost", "fates-count", "fates-absorbed-stays", "fates-bare-none",
          "fates-rel", "fates-none", "unpinned-count", "unpinned-path", "adopter-unit", "adopter-key"):
    out, rc = run(B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py", "--check", "--plant", p)
    plants.append(f"$ python map.py --check --plant {p}\n" + "\n".join(l for l in out.split("\n") if l.startswith(("FINDING", "atlas:")))
                  + f"\nrc {rc}")
    if rc != 1:
        sys.exit(f"plant {p} did not red")
    if p.startswith("adopter-") and "FINDING adopter-free" not in out:
        sys.exit(f"plant {p} redded without the adopter-free finding")
parts.append("""
## [plants] The map's plants, re-run

""" + block("text", "\n".join(plants)))
final = []
for label, args in (("design map", [B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py", "--check"]),
                    ("atlas", [B + "2026-10-16-build-PLAY-dClosedLoop-1-atlas.py", "--check"]),
                    ("fold state", [str(S / "night/fold_state.py")]),
                    ("reconciliation probe", [B + "2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py",
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

After the night pass's first commit, during the closing review's fold:

7. The reconciliation probe was copied into the build folder as
   `build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py` and edited there with the Edit tool: a Serves line and the
   note that records cite this one copy; rule 6, transitions, with its `--plant-transition-drop` plant; and the summary
   line naming what it does not read, with the plain-word count. Its source is the committed file.

8. The map's generator gained the `fates-none` plant by an Edit after `fix_map_review.py` ran, and its usage line
   names it (one sed). Every fates finding then had a red case.

9. A wrong-width row was seen to stop the map: one fates row widened by a cell in place, the check run (rc 1, the
   atlas's "7 cells under a 6-column header"), the record restored from a scratch copy, and `cmp` confirming it
   byte for byte before the check ran green again.

10. The gotcha `step-depends-on-a-later-build` gained the night pass in "Where it bit" and the backticked-citation fix,
    by two Edits, and `gotchas.py --write` re-rendered its index row's count.

11. The night-pass record's `[instrument]` section was rewritten with the final numbers, and its fates-arm count
    corrected once `fates-none` landed.

After the fold's commit, `15cec9200`:

12. The map's generator gained the records' half of its no-stale-facts check, by three Edits: the `COUNT`, `PIN` and
    `DATED` constants with `unpinned_counts()`, the arm in `check()`, and `unpinned-count` in its usage line. It was
    run red on the records first. Then five lines in four records were pinned by Edits: v2's `[owed]` headroom,
    gap-mem-30, and the night-pass record's `[p3-code]` item 6 and `[instrument]` map line, each at `15cec9200`; and
    the project map's test run, at `01dcdd1ae`, the commit that recorded it (`git log -S` names it).

After that commit, `2403c49ba`:

13. The check widened to the chain's critical path, by Edits: `COUNT`'s second alternative, a fence-skipping walk,
    and an `UNPINNED` table carrying the two plants, `unpinned-count` and `unpinned-path`. It was run red on the
    records first. Then four lines in two records were pinned by Edits: the night-pass record's `[chain-impact]`
    path, NP-24's question, now 211, and its `[instrument]` path line; and the walk's glance, at `beda01950`, under
    a note that the glance and wave 1 are derived again when the walk resumes.

After that commit, `0dce5cd2f`:

14. Two per-point lines of the night-pass record, fixed by Edits: point 1's set check, now registered by dIndexedDesign
    at Test's leg-pack point (as layer-memory's kind table says), and point 8's fates check, now twelve findings and two
    stops. The gotcha `amendment-leaves-its-other-half-standing` gained a checklist line by one Edit, and
    `gotchas.py --write` re-rendered its index.

After the owner's answers, `1d32760f3`, and NP-24's pricing:

15. The critical-path script's build count, raised from 16 to 18 by one sed once SP-1 split dDeclaredLoop three ways:
    sed -i 's/^assert len(units) == 16, len(units)$/assert len(units) == 18, len(units)   # 16 until SP-1 .../' \
    order/critical_path.py
16. The pricing script's first version, as the owner was asked from, was copied aside before its two corrections
    (`price_split_asked.py`, with its run). The corrections were Edits: clause 16 to the early parts, clause 42 to the
    core, a `CORRECTED` table naming both, and a `RESULTS` list the record's table derives from.

After the walk's wave 2, `44c8c8435`:

17. The critical-path script's build count, raised from 18 to 20 by one sed once WK-4 split dTotalRecall and dBoundRoles.
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


## [review] The closing review's args, and its fold's red runs

The args dispatch 105 ran on, as `build_args_night.py` built them:

````json
{
 "kind": "diff-review",
 "base": "beda01950b99c0c11e91fe2f12e5d019be39536d",
 "head": "9ab7a5c5cffa27b405c9caafa92d105db8a07ea0",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md",
  "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md",
  "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md",
  "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership.md",
  "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md",
  "memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md",
  "memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md",
  "memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds, and a row's planned units are prose, counted one per clause.\n- The owner's eight points, recorded verbatim in the night-pass record's [words], are decisions where they direct: unattended is the default state, attendance changes only the owner's interactions, testing can happen anywhere, code depth is core, and playbook mode stays in the flow. A finding may show the fold contradicting a record or the tree, not re-argue the owner's direction.\n- The forks NP-1 to NP-24 are parked for the owner. A key's default marked pending is the recommendation shown until the owner answers; a finding may show that a pending default contradicts a record, not that a fork should have been settled.\n- Every earlier answer stands: PM-1 to PM-12, RC-1 to RC-9, AF-1 to AF-3, FL1, CX-1 to CX-3, RT-1 to RT-4, KN-1 as the night pass amends it, and every round's before them.\n- The five research returns (research-unattended-core, -testing-anywhere, -code-orientation, -relational-syntax and -tool-fates) are verbatim and dated, and their prompts are rendered handoffs: neither is under review. The instruments record holds the scripts as they ran.\n- Dated records keep what held when they were written: revision notes, the session log's past entries, and the ownership record's approved tables, which its [amended] bullets amend.\n- Generated files (memory/LIVE.md and the build README's generated regions) are rendered, not reviewed. The map generator's and the atlas's changes are instruments, and are reviewed: can each new arm fail, and does each say what it does not check?",
 "checklist": "# recurring-bug-class checklist for beda01950..9ab7a5c5c (29 changed file(s))\n# 23 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 15 path · 4 directory · 4 basename; a cut tier prints one line per class\n# invariants are read at beda01950b99; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] pipe-in-a-code-span-splits-a-table-cell (path)\n      a markdown table cell holding a pipe, even inside backticks, splits into extra cells, so a reader that splits the row on its pipes reads the wrong cell as a column\n      memory/gotchas/pipe-in-a-code-span-splits-a-table-cell.md\n\n- [ ] policy-value-with-no-route (path)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] absence-read-from-one-of-several-homes (path)\n      a fact stated in several homes is read from one, so a derived view or a probe reports it absent wherever that home is silent, and the blank reads exactly like a real gap\n      memory/gotchas/absence-read-from-one-of-several-homes.md\n\n- [ ] an-allow-that-bypasses-a-judge-names-none (path)\n      a permission hook answers allow on calls that a judge, a classifier or a person, would otherwise have seen, and names no judge in its place, so a destructive call runs with nothing judging it\n      memory/gotchas/an-allow-that-bypasses-a-judge-names-none.md\n\n- [ ] append-without-an-idempotence-key (path)\n      a command that appends to an append-only record declares no key, so a retried run writes the same row twice and a set-join witness stays green\n      memory/gotchas/append-without-an-idempotence-key.md\n\n- [ ] insert-after-a-key-that-occurs-twice (path)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] instrument-recorded-into-the-corpus-it-scans (path)\n      a probe's source is recorded beside its results, the page it scans later embeds that record, and its literal pattern matches its own quotation, so a clean page reads as broken, or a broken one as clean\n      memory/gotchas/instrument-recorded-into-the-corpus-it-scans.md\n\n- [ ] owner-item-without-its-reject-outcome (path)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] parser-drops-rows-it-cannot-place (path)\n      a record-parsing instrument skips rows under a heading it does not know, or rows its pattern cannot read, and still prints a clean run, so its population shrinks without a word\n      memory/gotchas/parser-drops-rows-it-cannot-place.md\n\n- [ ] predicate-designed-without-a-run-over-the-tree (path)\n      a design states a new check's predicate without running it over today's population, so the check reds on hundreds of existing sites the day it arms, or ships with an exemption written by hand\n      memory/gotchas/predicate-designed-without-a-run-over-the-tree.md\n\n- [ ] rate-quoted-without-its-denominator (path)\n      a rate put to the owner in a fork divides by the wrong population, so the option's own cost reads several times off\n      memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] route-names-an-output-its-actor-never-emits (path)\n      a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever\n      memory/gotchas/route-names-an-output-its-actor-never-emits.md\n\n- [ ] rule-stated-with-no-check-that-fails (path)\n      a principle, a constraint between two keys or another rule is added in prose with no check that can fail on its breach, so it binds nothing and nobody can see that it does not\n      memory/gotchas/rule-stated-with-no-check-that-fails.md\n\n- [ ] summary-rewrites-the-text-it-carries (path)\n      a compaction summary that reproduces a block as verbatim quietly rewrites the lines that look wrong in it, so the defects the block carried read as fixed and the copy passes for the original\n      memory/gotchas/summary-rewrites-the-text-it-carries.md\n\n- [ ] zero-witness-over-an-unnamed-population (path)\n      a scan whose zero is the witness names no population, so a skipped scan and a scan over less than the guarded boundary publishes both read as clean\n      memory/gotchas/zero-witness-over-an-unnamed-population.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory) · memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory) · memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory) · memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory) · memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename) · memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] subagent-scratch-overwrites-the-parents-files (basename) · memory/gotchas/subagent-scratch-overwrites-the-parents-files.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename) · memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename) · memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "round": 1,
 "intensity": "light",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "medium",
  "skeptic": "medium",
  "synthesis": "medium"
 },
 "context": "The diff is one commit, 9ab7a5c5c over beda01950: build dClosedLoop's night pass, which worked the owner's eight points into the design while the owner was away. dClosedLoop is a design-only build that re-architects gov onto one loop. The night-pass record, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md, says what each point changed ([p1-unattended] to [p8-fates]), the chain's growth ([chain-impact]) and the parked forks ([forks]). The edits land in v2 (P4, P20, P25 amended, P31 to P33 added, thirteen keys and their preset rows, every [chain] row's new clauses and owned gaps, [owed]), flow-steps (the `repeat` disposition, the entry-time probe, [rules], the attendance gates in [breakpoint], a new [probe] program, attend and unattend in [lifecycle], the fix pass in [test]), the gap register (28 gaps), layer-memory's kinds, layer-runtime's driver and binding, layer-instruction, layer-library, the project map, the systems record, the ownership amendment, the re-cut's class rows, a new fates record of 131 parts, and the design map's and the atlas's generators. Review it as a design change. Does each edit say one thing, the same way in every record it touches, and leave no text that still states the old answer, such as an attended session that drives or keeps its freedom? Does every new item, key and record kind have one owner, and does every step's or row's new dependency sit on its own build or an ancestor, or in a slot that renders not installed? Does each probe, attendance and code clause close the gaps it owns? Is each fate in the fates record right against the tree and the design, and does each destination exist? Can each new check arm fail? A fold's own text is new surface: check it as hard as the text it replaced. Write the report to memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
 "scratch": "C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/review-night-pass"
}
````

H2's measurement, re-run on the folded tree. The first fold read 47 mentions over 27 kinds:

````text
$ python plain_cites.py
plan                     7  dOrderedCharter (dRankedPlan's), dDeclaredLoop (dRankedPlan's), dPlacedRequest (dRankedPlan's), dBoundRoles (dRankedPlan's), dTotalRecall (dRankedPlan's), dLinkedLibrary (dRankedPlan's) …
landing                  5  dGroundRules (dShippedRelease's), dOrderedCharter (dShippedRelease's), dKeptSession (dShippedRelease's), dWellOiledMachine (dShippedRelease's), dCalibratedLens (dShippedRelease's)
scope                    5  dOrderedCharter (dScopedBuild's), dDeclaredLoop (dScopedBuild's), dPlacedRequest (dScopedBuild's), dMindYourWords (dScopedBuild's), dCalibratedLens (dScopedBuild's)
code                     4  dGroundRules (dTotalRecall's), dFairHearing (dTotalRecall's), dDeclaredLoop (dTotalRecall's), dPlacedRequest (dTotalRecall's)
witness                  4  dGroundRules (dTotalRecall's), dOrderedCharter (dTotalRecall's), dDeclaredLoop (dTotalRecall's), dBoundRoles (dTotalRecall's)
seen red                 3  dGroundRules (dWitnessedBar's), dOrderedCharter (dWitnessedBar's), dKeptSession (dWitnessedBar's)
return                   3  dDeclaredLoop (dWellOiledMachine's), dBoundRoles (dWellOiledMachine's), dFurnishedOrders (dWellOiledMachine's)
intake                   3  dPlacedRequest (dWellOiledMachine's), dKeptSession (dWellOiledMachine's), dRankedPlan (dWellOiledMachine's)
fork                     3  dBoundRoles (dIndexedDesign's), dWellOiledMachine (dIndexedDesign's), dRankedPlan (dIndexedDesign's)
registry                 2  dGroundRules (dWitnessedBar's), dOrderedCharter (dWitnessedBar's)
playbook                 2  dOrderedCharter (dIndexedDesign's), dMindYourWords (dIndexedDesign's)
release                  2  dOrderedCharter (dShippedRelease's), dWellOiledMachine (dShippedRelease's)
probe                    2  dOrderedCharter (dPlacedRequest's), dDeclaredLoop (dPlacedRequest's)
spec                     2  dFairHearing (dIndexedDesign's), dBoundRoles (dIndexedDesign's)
act                      2  dDeclaredLoop (dWellOiledMachine's), dBoundRoles (dWellOiledMachine's)
claim                    2  dDeclaredLoop (dTotalRecall's), dPlacedRequest (dTotalRecall's)
baseline                 2  dFurnishedOrders (dLinkedLibrary's), dWitnessedBar (dLinkedLibrary's)
override                 1  dGroundRules (dOrderedCharter's)
receipt                  1  dGroundRules (dShippedRelease's)
commit                   1  dGroundRules (dDeclaredLoop's)
card                     1  dOrderedCharter (dPlacedRequest's)
inventory                1  dOrderedCharter (dIndexedDesign's)
disposition              1  dFairHearing (dDeclaredLoop's)
verdict                  1  dDeclaredLoop (dWitnessedBar's)
attribution              1  dDeclaredLoop (dWitnessedBar's)
triage                   1  dPlacedRequest (dRankedPlan's)
overlap                  1  dPlacedRequest (dIndexedDesign's)
fleet                    1  dPlacedRequest (dShippedRelease's)
routing                  1  dKeptSession (dWitnessedBar's)
ask                      1  dKeptSession (dTotalRecall's)
roster                   1  dBoundRoles (dIndexedDesign's)
value ledger             1  dFurnishedOrders (dCalibratedLens's)
work order               1  dTotalRecall (dBoundRoles's)
decision                 1  dWellOiledMachine (dLinkedLibrary's)
census                   1  dWitnessedBar (dLinkedLibrary's)
plain-word hits on a non-ancestor's record kind: 71, over 35 kinds
````

The committed probe's transitions rule, red before `repeat`'s row landed:

````text
chain rows 16 · owned nodes read 418 · flow items read 87 · stages 5 · breakpoint items 8, names 7 · contracts read 3 · on a non-ancestor's node 19 (cites 15, stage 0, routes 1, reads 3, registers 0)
left out: systems, cited in prose; roles, shapes and commands, not owned nodes; 47 plain-word mentions of a record kind a non-ancestor owns, mostly homonyms; points of another layer, not modelled as nodes (5): Observability's entry: Flow's Plan intake, the patch-build entry at Design and the breakpoints; Observability's entry: Memory's record kinds through `record`; Integrations' entry: Flow's verdict backends and release slot; Distribution's entry: Flow's version slot in Test's `test.merge`; Distribution's entry: Test's leg-pack point, for the `currency` leg
transitions: 3 dispositions routed through entry.claim, 3 `none` rows
  transitions: the disposition `repeat` routes through `entry.claim`, and [transitions] has no `none` row for it
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
findings 1
rc 1
````

After the row, its two new plants:

````text
$ python reconcile.py recut.md --plant-transition-drop repeat
chain rows 16 · owned nodes read 419 · flow items read 88 · stages 5 · breakpoint items 8, names 7 · contracts read 3 · on a non-ancestor's node 20 (cites 16, stage 0, routes 1, reads 3, registers 0)
left out: systems, cited in prose; roles, shapes and commands, not owned nodes; 46 plain-word mentions of a record kind a non-ancestor owns, mostly homonyms; points of another layer, not modelled as nodes (5): Observability's entry: Flow's Plan intake, the patch-build entry at Design and the breakpoints; Observability's entry: Memory's record kinds through `record`; Integrations' entry: Flow's verdict backends and release slot; Distribution's entry: Flow's version slot in Test's `test.merge`; Distribution's entry: Test's leg-pack point, for the `currency` leg
transitions: 3 dispositions routed through entry.claim, 3 `none` rows
  transitions: the disposition `repeat` routes through `entry.claim`, and [transitions] has no `none` row for it
  dBoundRoles cites `code` (dTotalRecall's, not an ancestor): tolerance
  dBoundRoles cites `feature` (dTotalRecall's, not an ancestor): tolerance
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `hooks.bypass` (dWitnessedBar's, not an ancestor): not a use
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dDeclaredLoop cites `playbook` (dIndexedDesign's, not an ancestor): tolerance
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
findings 1
rc 1
$ python reconcile.py recut.md --plant-drop dDeclaredLoop:playbook
chain rows 16 · owned nodes read 419 · flow items read 88 · stages 5 · breakpoint items 8, names 7 · contracts read 3 · on a non-ancestor's node 20 (cites 16, stage 0, routes 1, reads 3, registers 0)
left out: systems, cited in prose; roles, shapes and commands, not owned nodes; 46 plain-word mentions of a record kind a non-ancestor owns, mostly homonyms; points of another layer, not modelled as nodes (5): Observability's entry: Flow's Plan intake, the patch-build entry at Design and the breakpoints; Observability's entry: Memory's record kinds through `record`; Integrations' entry: Flow's verdict backends and release slot; Distribution's entry: Flow's version slot in Test's `test.merge`; Distribution's entry: Test's leg-pack point, for the `currency` leg
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dBoundRoles cites `code` (dTotalRecall's, not an ancestor): tolerance
  dBoundRoles cites `feature` (dTotalRecall's, not an ancestor): tolerance
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `hooks.bypass` (dWitnessedBar's, not an ancestor): not a use
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dDeclaredLoop cites `playbook` (dIndexedDesign's, not an ancestor): UNCLASSED
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
findings 1
rc 1
````

The map on a fates record with one row widened by a cell, restored byte for byte afterwards:

````text
$ python map.py --check
atlas: 7 cells under a 6-column header: | lib | resolvers, render-doc, health-log, arms | primitives | STAYS | inline copies gener
rc 1
````

The earlier plant suite against the committed probe:

````text
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-drop dTotalRecall:roster   (cites)
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): UNCLASSED
findings 1
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-edge-drop dRankedPlan:dDeclaredLoop --plant-edge-drop dRankedPlan:dTotalRecall   (stage)
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dRankedPlan cites `code` (dTotalRecall's, not an ancestor): UNCLASSED
  dRankedPlan reads `probe.observations` (dDeclaredLoop's, not an ancestor): UNCLASSED
  dRankedPlan routes `review.trigger` (dDeclaredLoop,dFairHearing's, not an ancestor): UNCLASSED
  dRankedPlan stage `plan.reason` (dDeclaredLoop's, not an ancestor): UNCLASSED
  dRankedPlan stage `plan.recommend` (dDeclaredLoop's, not an ancestor): UNCLASSED
findings 5
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-item plan.fake:plan:dOrderedCharter:an owner item   (routes into the breakpoint, by a declared name (FM8))
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dOrderedCharter routes `review.trigger` (dDeclaredLoop,dFairHearing's, not an ancestor): UNCLASSED
findings 1
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-edge-drop dTendedCadence:dIndexedDesign   (routes into a stage, from an expansion (FH3))
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dTendedCadence routes `design step` (dIndexedDesign's, not an ancestor): UNCLASSED
findings 1
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-item review.extra:breakpoint:dCalibratedLens:done   (routes keyed by owner (FL6))
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dDeclaredLoop routes `review.trigger` (dCalibratedLens's, not an ancestor): UNCLASSED
  dFairHearing routes `review.trigger` (dCalibratedLens,dDeclaredLoop's, not an ancestor): BAD CLASS ROW (owner dDeclaredLoop, class not a use)
  dRankedPlan routes `review.trigger` (dCalibratedLens's, not an ancestor): UNCLASSED
  dScopedBuild routes `review.trigger` (dCalibratedLens's, not an ancestor): UNCLASSED
  dShippedRelease routes `review.trigger` (dCalibratedLens's, not an ancestor): UNCLASSED
  dWellOiledMachine routes `review.trigger` (dCalibratedLens's, not an ancestor): UNCLASSED
findings 6
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-item plan.reader:plan:dRankedPlan:reads `runtime.journal`   (reads (FM4))
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dRankedPlan reads `runtime.journal` (dWellOiledMachine's, not an ancestor): UNCLASSED
findings 1
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-edge-drop dShippedRelease:dWellOiledMachine   (registers)
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dShippedRelease reads `build.release-ceiling` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `cadence-items` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `command-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `harness-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `host-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `journal-readers` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `notification-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
findings 7
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-class dFairHearing:review.trigger=   (a blank class cell (FH2))
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dFairHearing routes `review.trigger` (dDeclaredLoop's, not an ancestor): BAD CLASS ROW (owner dDeclaredLoop, class -)
  class row outside the closed set: dFairHearing `review.trigger` (blank)
findings 1
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-class dFairHearing:review.trigger=anything   (a class outside the set (FH2))
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dFairHearing routes `review.trigger` (dDeclaredLoop's, not an ancestor): BAD CLASS ROW (owner dDeclaredLoop, class anything)
  class row outside the closed set: dFairHearing `review.trigger` (anything)
findings 1
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-add dRankedPlan:review.trigger:dDeclaredLoop   (a class row no dependency needs (FL5))
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  class row with no dependency: dRankedPlan `review.trigger` (dDeclaredLoop, tolerance)
findings 1
rc 1
$ python ancestor_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md   (superseded, re-run on the committed table, FM5)
chain rows 16 · owned nodes read 419 (items, keys, points, record kinds, tag namespaces; systems are cited in prose and left out) · backticked citations 414 · of a non-ancestor's node 15
  class row with no citation: dBoundRoles `feature` (tolerance)
  class row with no citation: dDeclaredLoop `decisions.major` (tolerance)
  class row with no citation: dFairHearing `flow.route-backs` (not a use)
  class row with no citation: dFairHearing `review.trigger` (not a use)
  class row with no citation: dRankedPlan `run.host` (tolerance)
findings 5
rc 1
````


## [after] After the fold's commit

The map's re-run at `15cec9200` read 2,235 nodes, where the night-pass record quoted 2,234. The predicate, run over the
build's records before any arm was written, took only a backticked sha for a pin:

````text
$ python pinned_counts.py
UNPINNED 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1364: '31,133 of 32,768' in "- the level-0 map's headroom, 31,133 of 32,768 B with the kits' layer and fate keys, budgeted for the `code` l"
UNPINNED 2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:182: '31,133 of its 32,768' in "| gap-mem-30 | Memory | LOW | The level-0 map stands at 31,133 of its 32,768 B with the kits' layer and fate k"
UNPINNED 2026-10-16-build-PLAY-dClosedLoop-1-state.md:655: '2,008 nodes' in '161  01dcdd1ae records(dClosedLoop): the project map test-run — the whole design mapped at 2,008 nodes in 24.1'
UNPINNED 2026-10-16-build-PLAY-dClosedLoop-1-state.md:719: '2,008 nodes' in '161  01dcdd1ae records(dClosedLoop): the project map test-run — the whole design mapped at 2,008 nodes in 24.1'
UNPINNED 2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:504: '1,589 nodes' in '| A flat map | loses: one line for every node is far over any slot (`research-project-map-a.md:116`, `research'
UNPINNED 2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:913: '2,008 nodes' in 'is 2,008 nodes in 30 namespaces: 16 namespaces one line per node, and 14 folded to a counted line.'
UNPINNED 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:220: '31,133 of its 32,768' in '6. **Level 0 holds one counted `code` line,** never a line per file. The map stands at 31,133 of its 32,768 B.'
UNPINNED 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:607: '2,234 nodes' in '- **The design map** derives 2,234 nodes in 30 namespaces, 31,203 of 32,768 B, rc 0. Its printed size leaves o'
UNPINNED 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:607: '31,203 of 32,768' in '- **The design map** derives 2,234 nodes in 30 namespaces, 31,203 of 32,768 B, rc 0. Its printed size leaves o'
map counts quoted: 10 · pinned 1 · unpinned 9
rc=1
````

The map's arm, widened to a bare sha and a research record's cited line, on the records before their pins:

````text
$ python map.py --check
map: 2235 nodes in 30 namespaces; 31203 B of 32768 (no degrade); folded 14; unarmed none
map: purposes declared 1497, derived 256, pending 482
FINDING no stale facts: 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1364 quotes the map's '31,133 of 32,768' with nothing pinning it on its line
FINDING no stale facts: 2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:182 quotes the map's '31,133 of its 32,768' with nothing pinning it on its line
FINDING no stale facts: 2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:913 quotes the map's '2,008 nodes' with nothing pinning it on its line
FINDING no stale facts: 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:220 quotes the map's '31,133 of its 32,768' with nothing pinning it on its line
FINDING no stale facts: 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:607 quotes the map's '2,234 nodes' with nothing pinning it on its line
FINDING no stale facts: 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:607 quotes the map's '31,203 of 32,768' with nothing pinning it on its line
rc 1
````

After that commit, `2403c49ba`, the class widened to the chain's critical path, skipping a fenced run capture. The
population, through the generator's own patterns, before the pins:

````text
$ python pinned_counts2.py
pinned   2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1364: '31,203 of 32,768'
pinned   2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:182: '31,203 of its 32,768'
fenced   2026-10-16-build-PLAY-dClosedLoop-1-state.md:655: '2,008 nodes'
fenced   2026-10-16-build-PLAY-dClosedLoop-1-state.md:719: '2,008 nodes'
fenced   2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md:1209: 'critical path: 176'
pinned   2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:504: '1,589 nodes'
pinned   2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:913: '2,008 nodes'
pinned   2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md:127: '2,154 nodes'
fenced   2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md:377: 'critical path: 181'
fenced   2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md:808: 'critical path: 181'
pinned   2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:221: '31,203 of its 32,768'
unpinned 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:488: 'critical path: 181'
unpinned 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:540: 'critical path runs through dTendedCadence and dCalibratedLens at 213'
pinned   2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:608: '2,235 nodes'
pinned   2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:608: '31,203 of 32,768'
pinned   2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:611: '2,234 nodes'
unpinned 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:632: 'critical path** is 211'
fenced   2026-10-18-build-PLAY-dClosedLoop-1-recut.md:270: 'critical path: 168'
fenced   2026-10-18-build-PLAY-dClosedLoop-1-recut.md:277: 'critical path: 176'
unpinned 2026-10-18-build-PLAY-dClosedLoop-1-walk.md:20: 'critical path, 181'
fenced   2026-10-18-build-PLAY-dClosedLoop-1-walk.md:305: 'critical path: 181'
derived counts quoted: pinned 9 · fenced 8 · unpinned 4
rc=1
````

The map's arm on the same tree:

````text
$ python map.py --check
map: 2236 nodes in 30 namespaces; 31203 B of 32768 (no degrade); folded 14; unarmed none
map: purposes declared 1498, derived 256, pending 482
FINDING no stale facts: 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:488 quotes 'critical path: 181' with nothing pinning it on its line
FINDING no stale facts: 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:540 quotes 'critical path runs through dTendedCadence and dCalibratedLens at 213' with nothing pinning it on its line
FINDING no stale facts: 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:632 quotes 'critical path** is 211' with nothing pinning it on its line
FINDING no stale facts: 2026-10-18-build-PLAY-dClosedLoop-1-walk.md:20 quotes 'critical path, 181' with nothing pinning it on its line
rc 1
````


## [adopter-free] WK-8's class, before and after the fold

Wave 4 found a planned unit named for an adopter, which govkit selfcheck's arm 10 would refuse once built. The
predicate, run over the real tree before the arm was written, reports the purposes that name an adopter but grades
none of them:

````text
$ python adopter_probe.py
adopter names: 3 from 3 rows
planned units scanned: 335 over 20 chain rows
  UNIT dShippedRelease: 'the incms adapter'
  PURPOSE live-build.dPinnedHandoff: 'three habits of the NicoCares handoff briefs, as spec shapes a machine reads'
  PURPOSE live-build.aFerriedDossier: "an adopter's dossier, carried in from inCMS"
  PURPOSE closed-build.dGaugedVintage: 'the second inCMS dossier, triaged against this tree'
  PURPOSE decision-row.TOOL-dRetiredFork-4: "inCMS's D1 is nested template INTERPOLATION, not a nested agent loop; two spec revisions argued a fi"
  PURPOSE decision-row.TOOL-dUnstuckLanding-21: 'OWNER RULING (2026-10-04): dUnstuckLanding BUILDS asks TOOL-dUnstuckLanding-3 to -10 in gov, not des'
  PURPOSE decision-row.TOOL-dScaffoldedMirror-16: 'F4 (retire P1 if unused across two adopters) SUPERSEDED: 136 definitions and ZERO offenders since th'
  PURPOSE decision-row.DEPL-dRetiredFork-10: "the `forked` role is declared in OPPOSITE directions by gov and inCMS, and inCMS's own two registers"
  PURPOSE decision-row.TOOL-dMuffledSentinel-3: '**drift-audit 1.10 and unattended 1.19, over the bytes unit 2 changed**: an adopter pulling unit 2 c'
node keys scanned: 2273; purposes naming an adopter: 8
````

The map's adopter-free arm on the same tree, before the fold:

````text
$ python map.py --check
map: 2273 nodes in 30 namespaces; 32108 B of 32768 (no degrade); folded 14; unarmed none
map: purposes declared 1532, derived 259, pending 482
FINDING adopter-free: dShippedRelease plans 'the incms adapter', which names an adopter
rc 1
````

The predicate after the fold, its purpose lines left out:

````text
$ python adopter_probe.py
adopter names: 3 from 3 rows
planned units scanned: 335 over 20 chain rows
node keys scanned: 2275; purposes naming an adopter: 8
````

The arm's two plants are re-run in `[plants]`, and the map's green run is in `[final]`.


## [plants] The map's plants, re-run

````text
$ python map.py --check --plant no-layer
FINDING layer: kit.agent-instructions joins no layer
rc 1
$ python map.py --check --plant fates-absent
atlas: 0 records named fates-absent-plant
rc 1
$ python map.py --check --plant fates-drop
FINDING fates: kit.agent-instructions has no [table] row
FINDING fates: the rows count [24, 69, 23, 14, 130], and the record states [24, 70, 23, 14, 131]
rc 1
$ python map.py --check --plant fates-ghost
FINDING fates: a row names ghostkit, which is no kit
FINDING fates: the rows count [25, 70, 23, 14, 132], and the record states [24, 70, 23, 14, 131]
rc 1
$ python map.py --check --plant fates-bad
FINDING fates: agent-instructions · harness wiring has the fate MAYBE, outside the set
FINDING fates: the rows count [24, 69, 23, 14, 131], and the record states [24, 70, 23, 14, 131]
rc 1
$ python map.py --check --plant fates-unbuilt
FINDING fates: agent-instructions · harness wiring names no chain build where it goes
rc 1
$ python map.py --check --plant fates-empty
FINDING fates: workflows · `orient-counterfactual.js` retires naming neither a replacement nor a reason
rc 1
$ python map.py --check --plant fates-kit
FINDING fates: kit.agent-instructions's fate maybe is outside the set
FINDING fates: kit.agent-instructions carries fate=absorbed, and [kits] says maybe
rc 1
$ python map.py --check --plant fates-kit-drop
FINDING fates: kit.agent-instructions has no [kits] row
FINDING fates: kit.agent-instructions carries fate=absorbed, and [kits] says None
rc 1
$ python map.py --check --plant fates-kit-ghost
FINDING fates: [kits] names ghostkit, which is no kit node
rc 1
$ python map.py --check --plant fates-count
FINDING fates: the rows count [23, 71, 23, 14, 131], and the record states [24, 70, 23, 14, 131]
rc 1
$ python map.py --check --plant fates-absorbed-stays
FINDING fates: agent-instructions · harness wiring stays, yet its kit is absorbed
FINDING fates: the rows count [25, 69, 23, 14, 131], and the record states [24, 70, 23, 14, 131]
rc 1
$ python map.py --check --plant fates-bare-none
FINDING fates: workflows · `orient-counterfactual.js` retires naming neither a replacement nor a reason
rc 1
$ python map.py --check --plant fates-rel
FINDING fates: kit.agent-instructions carries fate=retired, and [kits] says absorbed
rc 1
$ python map.py --check --plant fates-none
FINDING fates: the record's [kits] or [table] holds no row
FINDING fates: kit.agent-instructions has no [kits] row
FINDING fates: kit.agent-instructions has no [table] row
FINDING fates: kit.branch-reconcile has no [kits] row
FINDING fates: kit.branch-reconcile has no [table] row
FINDING fates: kit.codebase-map has no [kits] row
FINDING fates: kit.codebase-map has no [table] row
FINDING fates: kit.drift-audit has no [kits] row
FINDING fates: kit.drift-audit has no [table] row
FINDING fates: kit.gate-lint has no [kits] row
FINDING fates: kit.gate-lint has no [table] row
FINDING fates: kit.govkit has no [kits] row
FINDING fates: kit.govkit has no [table] row
FINDING fates: kit.hooks has no [kits] row
FINDING fates: kit.hooks has no [table] row
FINDING fates: kit.lexicon has no [kits] row
FINDING fates: kit.lexicon has no [table] row
FINDING fates: kit.lib has no [kits] row
FINDING fates: kit.lib has no [table] row
FINDING fates: kit.memory-recall has no [kits] row
FINDING fates: kit.memory-recall has no [table] row
FINDING fates: kit.memory-tree has no [kits] row
FINDING fates: kit.memory-tree has no [table] row
FINDING fates: kit.playbook has no [kits] row
FINDING fates: kit.playbook has no [table] row
FINDING fates: kit.process-monitor has no [kits] row
FINDING fates: kit.process-monitor has no [table] row
FINDING fates: kit.pytest-parallel-guardrails has no [kits] row
FINDING fates: kit.pytest-parallel-guardrails has no [table] row
FINDING fates: kit.roles has no [kits] row
FINDING fates: kit.roles has no [table] row
FINDING fates: kit.run-gates has no [kits] row
FINDING fates: kit.run-gates has no [table] row
FINDING fates: kit.runlog has no [kits] row
FINDING fates: kit.runlog has no [table] row
FINDING fates: kit.unattended has no [kits] row
FINDING fates: kit.unattended has no [table] row
FINDING fates: kit.workflows has no [kits] row
FINDING fates: kit.workflows has no [table] row
FINDING fates: the rows count [0, 0, 0, 0, 0], and the record states [24, 70, 23, 14, 131]
FINDING fates: kit.agent-instructions carries fate=absorbed, and [kits] says None
FINDING fates: kit.branch-reconcile carries fate=optional, and [kits] says None
FINDING fates: kit.codebase-map carries fate=optional, and [kits] says None
FINDING fates: kit.drift-audit carries fate=optional, and [kits] says None
FINDING fates: kit.gate-lint carries fate=optional, and [kits] says None
FINDING fates: kit.govkit carries fate=optional, and [kits] says None
FINDING fates: kit.hooks carries fate=kept, and [kits] says None
FINDING fates: kit.lexicon carries fate=optional, and [kits] says None
FINDING fates: kit.lib carries fate=kept, and [kits] says None
FINDING fates: kit.memory-recall carries fate=optional, and [kits] says None
FINDING fates: kit.memory-tree carries fate=kept, and [kits] says None
FINDING fates: kit.playbook carries fate=kept, and [kits] says None
FINDING fates: kit.process-monitor carries fate=kept, and [kits] says None
FINDING fates: kit.pytest-parallel-guardrails carries fate=optional, and [kits] says None
FINDING fates: kit.roles carries fate=kept, and [kits] says None
FINDING fates: kit.run-gates carries fate=kept, and [kits] says None
FINDING fates: kit.runlog carries fate=optional, and [kits] says None
FINDING fates: kit.unattended carries fate=absorbed, and [kits] says None
FINDING fates: kit.workflows carries fate=kept, and [kits] says None
rc 1
$ python map.py --check --plant unpinned-count
FINDING no stale facts: 2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:646 quotes '31,203 of its 32,768' with nothing pinning it on its line
rc 1
$ python map.py --check --plant unpinned-path
FINDING no stale facts: 2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:646 quotes 'critical path is 211' with nothing pinning it on its line
rc 1
$ python map.py --check --plant adopter-unit
FINDING adopter-free: dGroundRules plans 'the NicoCares adapter', which names an adopter
rc 1
$ python map.py --check --plant adopter-key
FINDING adopter-free: layer.instruction-NicoCares names an adopter
rc 1
````


## [final] Every check, re-run at the commit

````text
$ design map
map: 2357 nodes in 30 namespaces; 30709 B of 32768 (degraded: purposes 40); folded 14; unarmed none
map: purposes declared 1590, derived 276, pending 491
rc 0

$ atlas
atlas: derived — 165 records, 2810 sections, 188 decision sections, 16 comparison areas, 38 principles
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
chain rows 20 · owned nodes read 445 · flow items read 88 · stages 5 · breakpoint items 8, names 7 · contracts read 3 · on a non-ancestor's node 22 (cites 18, stage 0, routes 1, reads 3, registers 0)
left out: systems, cited in prose; roles, shapes and commands, not owned nodes; 71 plain-word mentions of a record kind a non-ancestor owns, mostly homonyms; points of another layer, not modelled as nodes (5): Observability's entry: Flow's Plan intake, the patch-build entry at Design and the breakpoints; Observability's entry: Memory's record kinds through `record`; Integrations' entry: Flow's verdict backends and release slot; Distribution's entry: Flow's version slot in Test's `test.merge`; Distribution's entry: Test's leg-pack point, for the `currency` leg
transitions: 3 dispositions routed through entry.claim, 4 `none` rows
  dDeclaredLoop cites `run.on-owner-question` (dBoundRoles's, not an ancestor): tolerance
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dKeptSession's, not an ancestor): homonym
  dFurnishedOrders cites `code` (dTotalRecall's, not an ancestor): tolerance
  dFurnishedOrders cites `feature` (dTotalRecall's, not an ancestor): tolerance
  dGroundRules cites `check` (dWitnessedBar's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dKeptSession cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dKeptSession cites `hooks.bypass` (dWitnessedBar's, not an ancestor): not a use
  dKeptSession cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dKeptSession cites `playbook` (dIndexedDesign's, not an ancestor): tolerance
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `code` (dTotalRecall's, not an ancestor): not a use
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `journal` (dWellOiledMachine's, not an ancestor): homonym
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): homonym
  dDeclaredLoop reads `decisions.major` (dLinkedLibrary's, not an ancestor): tolerance
  dFairHearing reads `flow.route-backs` (dDeclaredLoop's, not an ancestor): not a use
  dRankedPlan reads `run.host` (dWellOiledMachine's, not an ancestor): tolerance
  dFairHearing routes `review.trigger` (dDeclaredLoop's, not an ancestor): not a use
findings 0
rc 0

$ clause scan
splits inside a clause: 0
rc 0

$ gap join
register keys 294 · chain builds 20
unowned: none
owned twice or more: none
owned but not in the register: none
builds owning nothing: none
rc 0

$ preset check
catalogue keys 225 · presettable 207 · preset rows 207
no findings
rc 0

$ critical path
critical path: 190 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 12, dFairHearing 24, dOrderedCharter 43, dDeclaredLoop 66, dPlacedRequest 74, dWitnessedBar 91, dKeptSession 92, dBoundRoles 108, dTotalRecall 110, dRankedPlan 123, dFurnishedOrders 126, dLinkedLibrary 134, dIndexedDesign 146, dWellOiledMachine 147, dScopedBuild 158, dTendedCadence 162, dMindYourWords 164, dShippedRelease 172, dCalibratedLens 174, dConvergedCharter 190
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
