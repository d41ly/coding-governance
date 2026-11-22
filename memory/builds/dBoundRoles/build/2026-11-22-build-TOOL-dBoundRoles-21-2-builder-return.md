**Serves:** journal TOOL-dBoundRoles-21

# TOOL-dBoundRoles-21 — the second builder's return, a divergence

Run `wf_43eb6f46-c2c`, started at `07f2d4b12` on rev-6. It restored every product path and committed nothing;
`diverged: true`. Its unverified partial implementation is kept in the session scratchpad as
`TOOL-dBoundRoles-21-partial.patch`.

## The divergence, as returned

(1) BLOCKING, §2 S3 with §4 Files touched and §7. S3 makes `effort` a `required` row of
`tools/roles/role-schema.toml` on every agent role, graded by R2 through `tools/roles/check_roles.py#AGENT_ROLE_KEYS`.
gov's role factory writes no `effort`: `tools/loop/factories.py#write_role` builds its front matter from
`roles_lib.FRONT_MATTER_KEYS` with a `values` dict holding `model=ROLE_MODEL` and no effort, then runs the kind's gate
innermost (`tools/loop/factories.py#write_kind_instance`, `#run_kind_gate`) and restores every file when it reds. So
`core.py new role` fails on every new agent role once S3 lands, and the `role-new` plant of the `loop factories
fixtures` leg reds at the close. §4 does not list `tools/loop/factories.py`, §7 does not list that leg, and the spec
does not say what effort a factory-made role declares: a constant beside `ROLE_TOOLS` and `ROLE_MODEL` (such as the
house `[effort] default` level), or a new `--effort` flag, which would also touch `tools/govkit/usage.toml`,
`help/loop.md` and the `NEW_ARGV["role-new"]` plant.

(2) §2 S8 folds the regenerated `.governance/policy.json` into the pass commit with `git commit --amend --no-edit`, and
AC7 checks `policy: mirror fresh` at the pass commit. The builder role commits as a new commit and never amends, and
`policy.py mirror --write` refuses while the catalogue differs from HEAD (`tools/policy/policy.py#cmd_mirror`), so no
amend-free route leaves the mirror fresh at the pass commit itself. Options it named: a second commit naming the unit,
with AC7 observed there, the two-commit shape `tools/policy/guard.py`'s docstring describes; or the main loop amends.

## What held

At `07f2d4b12`: every symbol S1 to S8 cites; the five `.get("gates", {})` readers S6 names; the selftest's twelve
temporary-directory fixtures; F8's premise (four derived-default refusals, `roles.retries` at source `default`);
`mirror --check` fresh at base; no write-set path on the kickoff manifest's watch list; the lexicon admits every new
name. A risk for the next builder: a repository with no commit on its landed branch makes `get` refuse with a
non-derived line, which S1 reads as a RolesError, so every render refuses there; gov's fixtures commit on `main` first.
