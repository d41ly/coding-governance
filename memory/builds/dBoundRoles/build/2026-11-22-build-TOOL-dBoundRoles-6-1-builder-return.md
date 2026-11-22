**Serves:** journal TOOL-dBoundRoles-6

# TOOL-dBoundRoles-6 — the first builder's return, a divergence on rev-7

Run `wf_c709768a-dd5`, started at `cd6a8e18a` on rev-7. It wrote nothing and committed nothing; `diverged: true`.

## The divergence, as returned

1. The write set leaves out the `kit.policy` change record that §4 and S2 require the pass to stage.
2. §5 says no user docs are owed, which is false: `help/policy.md` describes the pre-commit guard's paths and admitted
   shapes, `help/roles.md` says the guard does not check a hand-edited role index and that the arms switch on only
   where the index exists, and `help/red-fix-lane.md` says only a broken role index closes the lane. S2, S3, S5 and S6
   change each statement.
3. `tools/policy/README.md` is missing from Files touched: its guard section lists the admitted shapes and counts the
   guard cases in `tools/policy/check_policy.py`, and S2 changes both.
4. Rev-7 says `tools/hooks/agent-cap.js` is still the blob it cites; TOOL-dBoundRoles-17 changed it since. The blob-pinned
   citations still resolve, but the lines have moved at HEAD.
5. A design gap: S4's `render_role_section` in `tools/roles/roles_lib.py` needs the drive lines
   (`tools/roles/handoff.py#extract_drive_lines`) and the role half of `#render_work_order`, but the library cannot
   import `handoff.py`, which imports it, and the renderer's ranked selftest points the kit at a fixture with no
   templates. S2's `resolve_kit_dir` lives in the policy kit only as `policy.py`'s inlined copy, while `guard.py`
   never imports `policy.py`.

It also noted that once S2 lands, a later pass committing a re-render off the run's branch is admitted only if
`render_agents.py --check` exits 0.

## The decision

Items 1 to 3 widen the write set; the spec names the pages. Items 4 and 5 go to the spec writer, item 5 as a §8 fork
resolved by M3 as a delegated resolution. widens: none · relaxes: none.
