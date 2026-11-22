**Serves:** journal TOOL-dBoundRoles-2

# TOOL-dBoundRoles-2 — the first builder's return, a divergence

Run `wf_07a97cf8-bbd`, builder agent `a9676557097c5c03f`, started at `bfbf7b391` on rev-4. It wrote no product path and
committed nothing; `diverged: true`.

## The divergence, as returned

(1) §6 AC5 and §4 "The rendered block" conflict with how agent files are rendered now. AC5 requires
`.claude/agents/gov-builder.md` to hold `## Never`, `## Ceiling` and `## Return` "in that order before `## Charter`".
§4/S6 has render_role append those sections after `## House rules`. Since PLAY-dOrderedCharter-5 S1,
`tools/roles/render_agents.py#render_agent_file` renders `## Charter` FIRST whenever the playbook document registry reads
(it does in this repo). The rendered role comes after the charter (`body = blocks + "\n" + body`). At the spec's base
4ed9e567 the role came first, so AC5 held then and does not now. §4 or AC5 must say where the three sections go
relative to `## Charter` under the ranked render: either AC5 says "after `## Charter`, at the end of the role", or the
design moves them in render_agent_file, which is not the one-composition route S6 states.

(2) §2 S5's readers list and §4 Files touched leave out the role kind's factory. `tools/loop/factories.py#write_role`
takes `--returns` and writes a role file with `render_front_matter(roles_lib.FRONT_MATTER_KEYS, values)`, setting
`returns=` and neither `never` nor `return`. Once `returns` retires and `never`/`return` are required on every role, the
factory writes empty `never:`/`return:` lines and check_roles reds R2. Two fixtures break: `role-new` (the NEW_ARGV
row expecting "gate green") goes red; `role-hand` (write_hand_plant, `returns: x`, expected R2 for a hand role file
missing writes) still reds R2, but for the unknown key `returns`, the wrong reason. The kind's usage line in
`tools/playbook/kinds.toml` (kind.role) also names `--returns`. The spec must add `tools/loop/factories.py` and
`tools/playbook/kinds.toml` to Files touched and S5, and state the factory's replacement flags and the fixture values.

(3) Re-grounding for the same revision, symbols present and lines drifted, each read at `bfbf7b391`:
`tools/roles/roles_lib.py@a3e28716:478` parse_front_matter, `@a3e28716:828` render_role, `@a3e28716:680` load_policy's
gates; `tools/roles/check_roles.py@abcde1da:110` WRITES, `@abcde1da:111` REQUIRED_ROLE_KEYS, `@abcde1da:115`
WRITE_FOLDERS, `@abcde1da:121` UNENFORCED_RE, `@abcde1da:146` render_catalogue_region, `@abcde1da:201` R2,
`@abcde1da:62` the R13 doc; `tools/roles/render_agents.py@0d96af1a:157` render_agent_file;
`tools/roles/handoff.py@ba4a9fad:538` render_handoff; `tools/roles/README.md@d01a5615:465` the catalogue header;
`tools/workflows/unattended-build.template.js@55695bb4:800` alreadyPresent. S5 lists ten role files; HEAD holds eleven,
`tools/roles/agents/gov-tester.agent.md` among them, which §8 F4 covers but S5's readers list omits.
