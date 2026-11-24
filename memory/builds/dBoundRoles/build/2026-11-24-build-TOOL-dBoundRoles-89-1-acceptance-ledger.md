**Serves:** journal TOOL-dBoundRoles-89

# TOOL-dBoundRoles-89 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit on its worktree before the pass commit, at base
`85f58623b`. The probes are Python programs in the run's scratch directory: each builds the placement fixture
repository with `tools/loop/placement.py#write_placement_fixture` under `%TEMP%`, writes a return file there and runs
`placement.py place` and `handoff.py check-return-file` over it as processes. No gate, suite or bar ran in the pass and
no plant ran through `--fixture`: the `return-json` and `return-sent-back` plants, their RED-first observation and the
legs of section 7 are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-89
- AC1 — `return-json` — a fenced JSON return naming a build exited 0 at `check-return-file` and at `place`, and its block equalled the lines' block but for `placed-utc`; the whole text as one object and a CRLF fence placed too; with the graded object withheld from `read_scout_return` the same file was refused at its first line. OWED at the close: the plant itself, RED on `read_scout_return` ignoring the object.
- AC2 — `RETURN_KEYS` — the `return` line's fields, less `outcome` and `card`, equalled it. OWED at the close: the plant's arm, RED on a `return` line without `build`.
- AC3 — `--object` — over a passing fenced or whole JSON return it printed the object on one line, exit 0, and over passing lines it printed nothing, exit 0; without it nothing printed over any of them; over a return lacking `outcome` it printed the defect line alone, exit 1, and on an unknown slot exited 2.
- AC4 — `return-sent-back` — the lines lacking `outcome` exited 1 naming it with no block, then the fenced block exited 0 placed, in the probe. OWED at the close: the plant itself.
- AC5 — `reason` — a JSON return with a line break in it, one with a `card` key and one whose `outcome` is `oriented` each exited 1 naming the key, and no block was written; a list value, a lone surrogate, a `refused` outcome and another role's work order were each refused too, and `owner-places` printed no evidence line of the one with the break.
- AC6 — `--plant return-untyped` — not run, being a case of the leg; the probe read the lines' refusals it and the other two plants hold: an odd line, a key given twice, a bad slug, no `outcome`, an `oriented` one, a `gov-researcher` work order and no work order each exited 1 as before. OWED at the close: the plants.
- AC7 — `roles_lib.render_static_block` — its UTF-8 length was 6529 (DERIVED, at the pass tree) against `read_role_budget`'s 6530, and `python tools/roles/render_agents.py --check` exited 0 after `--write`.
- AC8 — `grep -n -i "json" help/roles.md help/loop.md tools/roles/README.md` — it prints a line of step 2, of the `agent-places` bullet and of the README's "A return read from a file", and over `tools/loop/placement.py` a line of its TYPED CHANNEL paragraph, each stating one JSON object.
