# The retrofit system: bringing an existing repository under gov's practices

**Serves:** research PLAY-dClosedLoop-1

The owner opened a sixth system after the five of the systems round: how gov brings its practices into a
repository that already has an extensive codebase and practices of its own. This record holds the owner's
words, what the design already holds for it, and the research and its method. Once the runs return, it
also holds what they agree on, and then the design.

## [words] The owner's words, 2026-10-17

> Continue with your current work queue but budget research+design for another system: retrofitting the
> gov practices. What layer (extension?) does it go to? When gov is adopted into a fresh repo, maintaining
> its methods (to be designed) like tagging, code annotations, decision log and its major decisions, etc.,
> is not an issue - they all happen along as code is planned, designed, and built. However, Gov may be
> adopted into a product/repo that has an extensive codebase already and has been following different
> practices. How would gov retrofit its practices into an existing repo as it goves over its code to
> ensure efficient practices?

## [scope] What the design already holds

- **No design record covers it.** The flow record names an existing codebase only as where Plan
  integrates a new feature (`build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md:112,119`). The deployer
  research's retrofit installs gov's kits into an adopter's toolchain
  (`memory/builds/aDeployScout/spec/governance-deployer-research.md:22`). It does not bring the adopter's
  code under gov's practices.
- **Pockets tolerate legacy, one practice at a time:**

  | Pocket | What it tolerates | Where |
  |---|---|---|
  | the codebase map's baseline | keys no dossier claims yet; it shrinks unless a recorded decision says otherwise | `memory/map/baseline.toml`, and AGENTS.md's section 2 |
  | IW-1's legacy list | hand-written instruction documents, shrink-only, each chain build migrating its own step's guides | the systems record's `[answers]` |
  | `instructions.legacy` | the same list's policy: `shrink-only` or `refuse` | the systems record's `[design-instruction-writing]` |
  | `memory.legacy-anchors` | legacy record headings, given derived anchors | the systems record's `[design-memory-structure]` |

- **What it lacks** is the system the owner asks for: where it sits, how it reaches the code as gov goes
  over it, what each practice derives from what the repository already holds, and the bound that keeps
  it out of the owner's way.

## [research] Dispatched, 2026-10-17

- **The method** is the systems round's. One handoff, `prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-1-researcher.md`, runs twice at the researcher's declared
  effort, medium, as dispatches 83 and 84. The design is based on what the two runs agree on.
- **The handoff** shares the systems round's handed facts, way of working and return shape. It differs
  in its context, which quotes the owner's words above, in its part, and in the return shape's third
  section, which asks across the five systems instead of the other four. The script below assembles it,
  `handoff.py render` renders it, and `handoff.py check` passes it.
- **The order.** Both runs go out together once review dispatch 65 returns, two agents at once. The
  review queue resumes at dispatch 66 after both return, so no more than five agents run at once.
- **The returns** are filed verbatim as `build/2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-<run>.md`.

### [instrument] The script that assembles the question

```python
"""Assemble the retrofit system's research question from the systems round's shared blocks and its own
part, for the system the owner opened on 2026-10-17, then render and check its handoff.

Usage: python assemble_retrofit.py <dir> <systems-dir>   (from the worktree root)
Writes <dir>/question-retrofit.md, renders the handoff with handoff.py into the build's prompts/ folder,
writes the spawn prompt (the marker line, a blank line and the Task section) to <dir>/prompt-27.txt, and
runs handoff.py check on the rendered file. The handed facts, the way of working and the return shape are
the systems round's, so this question differs from those five only in its context, its part, and the
return shape's third section, which asks across the five systems instead of the other four.
"""
import pathlib
import subprocess
import sys

d, sysd = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
head = (sysd / "head-expansions.md").read_text(encoding="utf-8").rstrip("\n") + "\n" + \
    (sysd / "head-more.md").read_text(encoding="utf-8")
tail = (sysd / "shared-tail.md").read_text(encoding="utf-8")
old = "   it; then what it needs from, and gives to, the other four systems.\n"
if tail.count(old) != 1:
    sys.exit("the return shape's third section has moved")
tail = tail.replace(old, "   it; then what it needs from, and gives to, each of the five systems the round designed.\n")
CONTEXT = (
    "**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development.\n"
    "The owner reviews the design layer by layer. All eight layers, the five core and the three expansions,\n"
    "are designed, reviewed and folded. Five systems that cut across every layer were then researched and\n"
    "designed: tags, code annotations, instruction writing, role workflow shapes and memory structure. The\n"
    "owner is settling their forks. The owner now opens a sixth system, in these words:\n\n"
    "> Continue with your current work queue but budget research+design for another system: retrofitting the\n"
    "> gov practices. What layer (extension?) does it go to? When gov is adopted into a fresh repo, maintaining\n"
    "> its methods (to be designed) like tagging, code annotations, decision log and its major decisions, etc.,\n"
    "> is not an issue - they all happen along as code is planned, designed, and built. However, Gov may be\n"
    "> adopted into a product/repo that has an extensive codebase already and has been following different\n"
    "> practices. How would gov retrofit its practices into an existing repo as it goves over its code to\n"
    "> ensure efficient practices?\n\n"
    "Yours is **retrofitting gov's practices into an existing repository**. Design it to fit the architecture\n"
    "handed below, across all eight layers and the five systems. Measure what today's product does, say what\n"
    "the current design already settles and what it lacks, and say what makes your pick efficient, in numbers\n"
    "a check could hold it to.\n")
part = (d / "part-retrofit.md").read_text(encoding="utf-8")
text = "\n".join([CONTEXT, head, part, tail]).rstrip("\n") + "\n"
if "\r" in text:
    sys.exit("a carriage return reached the question")
(d / "question-retrofit.md").write_text(text, encoding="utf-8", newline="\n")
print(f"question-retrofit.md: {len(text.split())} words, {len(text.encode('utf-8'))} bytes")

r = subprocess.run([sys.executable, "tools/roles/handoff.py", "render", "--role", "gov-researcher",
                    "--build", "dClosedLoop", "--unit", "PLAY-dClosedLoop-1", "--input", "question=" + text,
                    "--part", "task"], capture_output=True)
sys.stderr.write(r.stderr.decode("utf-8"))
if r.returncode:
    sys.exit(f"render exited {r.returncode}")
task = r.stdout.decode("utf-8")
(d / "prompt-27.txt").write_bytes(task.encode("utf-8"))
marker = task.split("\n", 1)[0]
path = marker.split(" path=", 1)[1].split(" ", 1)[0]
print(f"rendered {path}")
c = subprocess.run([sys.executable, "tools/roles/handoff.py", "check", path], capture_output=True)
print(c.stdout.decode("utf-8") + c.stderr.decode("utf-8"), end="")
sys.exit(c.returncode)
```
