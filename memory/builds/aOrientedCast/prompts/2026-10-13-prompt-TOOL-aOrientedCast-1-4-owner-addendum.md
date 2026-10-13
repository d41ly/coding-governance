**Serves:** research TOOL-aOrientedCast-1 PLAY-aOrientedCast-1

# The owner's second addendum — the roles join the v4.3 charter as a rendered section

Sent by the owner in this build's session on 2026-10-13, after the build merged onto local main at
`6081d92e4`. The merge kept main's v4.3 charter, which carries no `## §<n> — ` headings, so every
role's `charter` id resolves to nothing: `check_roles.py` reports one R4 defect per id and
`render_agents.py --check` refuses on the first. The owner's answer, verbatim:

```text
Brainstorm the design of this feature - protocol files are already cited in their _GENERATED_ section - that's where they go if they need to be read, never hand-authored directly. However, the use of agent roles when gov's adopted is now non-negotiable (unless it really is impossible) and this must be clearly stipulated and integrated with the new charter layout - it should become a new GENERATED (rendered) section of the charter, listing available agent roles - same one liner, citing the role, what it does, when it's mandatory to invoke it and where its output goes. Help me come up with a seamless design to fit.
```

## The design the owner chose

Four forks, each answered on its own:

- **Rules:** each role cites section 1 rule TAGS (`rules: [spec, verify, gate]`), replacing the
  `charter` key; its agent type carries those one-liners verbatim from the rendered charter.
- **Protocols:** every agent type carries the rendered `## Protocols` section whole and reads the
  protocol whose trigger holds. No role file names a protocol path.
- **The exception:** a tool or run that cannot spawn a sub-agent at all, AND an owner waiver row
  for any inline stand-in, graded like the other waiver registries.
- **Home:** new units in this build, minted by `--rescope add` when the run resumes.

## What gets built

1. **A section 1 rule, `[roles]`,** in the `kit:roles` fence: spec writing, spec review, building
   and the closing review go to the role named under Agent roles, and doing them inline is refused,
   short of the exception above.
2. **A generated section 3 subsection, `## Agent roles — hand the work to its role`,** between Tools
   and Protocols, in a one-line region: a derived placeholder, `{{ROLE_ROSTER}}`, as `{{NODE_TABLE}}`
   is. One line per role: what it does, when it is mandatory, where its output goes. The playbook
   probe asks the roles kit for the lines through a `roster` verb, so `roles_lib` stays the one
   reader of role files and the playbook kit names no sibling kit by literal.
3. **Two role front-matter fields,** `mandatory` and `output`. The checker refuses a mandatory role
   whose workflow's `enforced-by` names no hook, unless its line says it is unenforced, and a writer
   role whose `output` does not name its write class's folder.
4. **The render order** is charter first, agents second: the roster needs only role files, and an
   agent type needs the rendered charter. A role edit stales the charter, which the playbook render
   check reads; a rule edit stales the agent types, which `roles render wiring` reads.
5. **The `Tools to rely on` roles line** shrinks to its `/build` clause.
