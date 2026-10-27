# The step gate

**What it is.** `step-gate` is a leg of the merge bar that reds a landing which makes something an
adopter can see disappear — a renamed or removed installed file, hook, Skill, agent, conf key,
policy key, CLI verb or registry entry — without an `[[upgrade]]` or `[[retired]]` row saying where
it went. It reads the adopter-visible population at the landing's base and at its tip, and every
member present at the base and missing at the tip must be named in some row's `surfaces`. An edit
that changes a file's bytes but not its name moves no member and needs no row.

A member is spelled `<class>:<name>`. A path under the tool root is spelled with `{prefix}` in place
of that root, so one spelling names the member at every install prefix:

| Class | A member is |
|---|---|
| `file` | each `files` row's path in gov's source-mode receipt, `.governance/install.json`, else each destination gov's own plan derives |
| `installable` | each destination a shipped kit file lands at, e.g. `installable:{prefix}/roles/README.md` |
| `hook` | each tracked hook fragment's `name`, e.g. `hook:scratch-guard` |
| `command` | each Skill shipped to `.claude/skills/<name>/SKILL.md`, by `<name>` |
| `agent` | each `tools/roles/agents/<name>.agent.md`, by `<name>` |
| `conf` | each conf key a kit's `[config]` declares, as `<conf file>#<KEY>` |
| `policy` | each `[[key]]` name in `tools/policy/catalogue.toml` |
| `verb` | each verb `govkit.py`'s usage or `unattended.sh`'s header states, as `<cli>:<verb>` |
| `entry` | each registry `[[entry]]` id |

## How to use it

- **Run it:** `python tools/govkit/step_gate.py` grades from `GATE_PUSH_BASE`, else the merge-base <!-- usage: script:tools/govkit/step_gate.py 90245caf -->
  with the default branch — the same base `kit epoch` reads; `--base <rev>` grades from another
  commit, and `--print-base` prints the base it would use. A red line reads:

  ```
  step-gate: RED agent:gov-skeptic vanished with no [[upgrade]] or [[retired]] row naming it in surfaces
  ```

- **Answer a red:** write the step that carries adopters across and name the member in its
  `surfaces` — an `[[upgrade]]` row in the owning kit's `kit.toml`, or in `tools/govkit/steps.toml`
  for a surface no kit owns (see [upgrade steps](upgrade-steps.md)). A kit that leaves gov gets a
  `[[retired]]` row in `tools/govkit/registry.toml`; name its vanished members in that row's
  `surfaces`. The gate only names what is missing; it never writes a row.
- **See the population:** `python tools/govkit/step_gate.py --list` prints each class and its member
  count at the tip. A class with no member refuses the gate (exit 2), because a green over an empty
  class grades nothing.
- **Watch it red:** `python tools/govkit/step_gate.py --fixture --plant <class>` clones HEAD, commits
  one vanished member of that class, and grades the range (exit 1); `--with-row` adds the witness
  row and grades again (exit 0). `--plant content-edit` changes bytes only and stays green.

## How a class joins

A class is one `[[class]]` row in `tools/govkit/surface-classes.toml`: its `id`, a `reader` that
returns the member names over a tree, a `plant` that stages one vanished member in a scratch clone,
a `summary`, and optionally a `witness` reading the class's own change record, whose names count as
witnessed. Add the row and its functions, then run `--fixture --plant <id>` with and without
`--with-row`. A row with no `plant` is refused, so a class cannot join without its own red.

## What it does not check

A change of meaning behind an unchanged name; whether a step actually carries the member it names
(the `upgrade-walk` leg's question); and anything no class reads — a conf key a kit reads but never
declares, a verb of a CLI no usage source names, an agent or Skill an adopter wrote itself.
