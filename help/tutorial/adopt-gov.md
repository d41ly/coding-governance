# Adopt gov in an empty repository

This tutorial installs gov's charter kits into a repository that holds nothing yet, adds one rule of the
repository's own, renders the charter and reads what the render reports. Every command below is run by
the docs leg's run arm, in order, in a fresh scratch repository, so the page is the path an adopter
follows.

Before you start: a repository with at least one commit, its directory your working directory for every
command, and `GOV` set in your shell to the path of your gov checkout.

## 1. Answer the install's questions

`intake` writes `.governance/deploy.toml`, the kits you select and the answers they need. It refuses to
guess an answer, and names each one it is missing.

```bash
python "$GOV/tools/govkit/govkit.py" intake --target . --kits playbook,playbook-render,memory-tree,policy,agent-instructions --answer playbook_path=AGENTS.md
```

The charter's render asks for values no probe can derive in an empty repository: what the product is, how
it is laid out, which commands gate it. They go in the `[charter]` table of the same file, one line each:

```bash
printf '%s\n' '' '[charter]' 'PROJECT_NAME = "demo"' 'PRODUCT_PREAMBLE = "demo is a scratch repository that adopts gov."' \
  'PRODUCT_CONTEXT_HOME = "README.md"' 'DOC_ROUTING_TABLE = "README.md"' 'REPO_LAYOUT_MAP = "root holds README.md"' \
  'STREAM_OWNERSHIP = "one stream"' 'CI_FILE = "none yet"' 'GATE_RUNNER = "none yet"' 'GATE_COMMANDS = "none yet"' \
  'COMMAND_CATALOG = "none yet"' 'ID_FAMILIES = "none yet"' 'MEMORY_DISCIPLINES = "none yet"' \
  'KIND_FACTORY_MAP = "none yet"' 'SHARED_PRIMITIVES_LOCATION = "none yet"' 'TOOLCHAIN_NOTES = "none yet"' \
  'COMMIT_TRAILER = "none"' 'WORKTREE_SCRIPT = "none"' >> .governance/deploy.toml
```

## 2. Install and commit

`apply` lands each kit's files, configures it and writes the receipt `.governance/install.json`. It
commits nothing.

```bash
python "$GOV/tools/govkit/govkit.py" apply --target .
git add -A
git commit -qm "install gov"
```

Commit the install before you add a rule: the render reads your rules and your policy at your last
commit, and in a repository with no landed revision it renders gov's units alone.

## 3. Add a rule of your own

Your rules live in the overlay, `.governance/instructions.toml`, a `[[unit]]` row each, its tag in the
`repo.` namespace. A level-0 unit renders in the charter's own rules section. Write the overlay at your
terminal, then commit it:

```bash
printf '%s\n' '[[unit]]' 'tag = "repo.verify-staged"' 'level = 0' 'type = "directive"' 'scope = ["reader.every"]' \
  'trigger = "always"' 'text = "Verify against the staged bytes before every commit."' > .governance/instructions.toml
git add .governance/instructions.toml
git commit -qm "a repository rule"
```

## 4. Render and read the delta report

```bash
python tools/playbook/render_playbook.py --render-scope charter
grep -n "Verify against the staged bytes" AGENTS.md
```

The render prints each placeholder's source, then `render-playbook — composition:` and one line per unit
whose state it reports, here `unchanged  [repository] repo.verify-staged`: your unit, rendered as you wrote
it. A unit of yours that amends, replaces or excludes one of gov's reads `amended`, `replaced` or
`excluded` there. The `grep` finds your rule's line in `AGENTS.md`. Commit the charter with the overlay
and the render check agrees.

Next: [the instruction layer](../concepts/instruction-layer.md) explains what you just composed, and
[change a gov rule](../tasks/change-a-gov-rule.md) amends, replaces and excludes one of gov's units.
