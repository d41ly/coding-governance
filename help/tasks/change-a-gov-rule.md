<!-- unit: unit.unit-registry -->
# Change one of gov's rules

Gov's instruction units ship in each kit and are overwritten at every update, so you never edit them in
place. You change one from your overlay, `.governance/instructions.toml`: amend it, replace it, exclude
it, and re-pin your change when gov's text moves. [The instruction overlay](../overlay.md) holds the row
grammar; this page is the commands.

The commands run in a repository gov is installed in. The docs leg's run arm runs this page in its own
scratch repository, so the page opens with the install [the tutorial](../tutorial/adopt-gov.md) shows,
`GOV` set to your gov checkout:

```bash
python "$GOV/tools/govkit/govkit.py" intake --target . --kits playbook,playbook-render,memory-tree,policy
printf '%s\n' '' '[charter]' 'PROJECT_NAME = "demo"' 'PRODUCT_PREAMBLE = "demo is a scratch repository that adopts gov."' \
  'PRODUCT_CONTEXT_HOME = "README.md"' 'DOC_ROUTING_TABLE = "README.md"' 'REPO_LAYOUT_MAP = "root holds README.md"' \
  'STREAM_OWNERSHIP = "one stream"' 'CI_FILE = "none yet"' 'GATE_RUNNER = "none yet"' 'GATE_COMMANDS = "none yet"' \
  'COMMAND_CATALOG = "none yet"' 'ID_FAMILIES = "none yet"' 'MEMORY_DISCIPLINES = "none yet"' \
  'KIND_FACTORY_MAP = "none yet"' 'SHARED_PRIMITIVES_LOCATION = "none yet"' 'TOOLCHAIN_NOTES = "none yet"' \
  'COMMIT_TRAILER = "none"' 'WORKTREE_SCRIPT = "none"' >> .governance/deploy.toml
python "$GOV/tools/govkit/govkit.py" apply --target .
git add -A
git commit -qm "install gov"
```

## 1. Find the unit and its pin

Every change to a gov unit names it by tag and pins the text you read as `<tag>@<hash8>`:

```bash
python tools/playbook/instructions_edit.py list
```

It prints one `<tag>@<hash8>` line per unit, gov's and yours. <!-- usage: script:tools/playbook/instructions_edit.py#list ede47769 -->

## 2. Amend it or replace it

Add a unit of your own whose `edges` names gov's, pinned. `amends` renders your unit right after gov's,
which keeps rendering; `supersedes` renders yours in its place:

```toml
[[unit]]
tag = "repo.verify-staged"
level = 3
type = "directive"
scope = ["reader.every"]
trigger = "before every pass commit"
text = "MUST verify against the staged bytes."
edges = ["amends=unit.some-rule@1a2b3c4d"]
```

## 3. Exclude it

List its tag in `instructions.exclude` in `.governance/policy.toml`:

```toml
[instructions]
exclude = ["unit.some-rule"]
```

A fixed unit, a `principle.` unit or one whose `fixed-by` resolves, refuses all three.

## 4. Commit, render and check

The render reads the overlay and the policy at your last commit, so commit them first, then render and
check:

```bash
python tools/playbook/render_playbook.py --render-scope charter
python tools/playbook/overlay.py check
```

The render's delta report names each gov unit `unchanged`, `amended`, `replaced` or `excluded`, and
`overlay.py check` exits 1 naming every refusal. <!-- usage: script:tools/playbook/overlay.py#check b50e110b -->

## 5. Re-pin when gov's text moves

When gov changes a unit you pinned with a `semantic` change, your edge is `stale` at the next update.
Read the new pin with `list`, then move your edge to it:

<!-- run: no — its tag and pin are placeholders, and the write door refuses until its guard lands -->
```bash
python tools/playbook/instructions_edit.py edit --manifest overlay --tag <your tag> --edges amends=<gov tag>@<hash8>
```

<!-- usage: script:tools/playbook/instructions_edit.py#edit b1db1612 --> What `instructions.stale` does
with a stale or orphaned edge until you re-pin is on [the instruction overlay](../overlay.md).
