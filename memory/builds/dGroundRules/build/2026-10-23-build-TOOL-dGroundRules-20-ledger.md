# TOOL-dGroundRules-20 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-20

No merge bar, no gate leg and no self-test suite ran in this pass; the lexicon's `--suggest` answered
OK for `run_fixtures_guard_census`. AC1 and AC2 were observed by the spec-token checker's
`--legs-for` query on the built tree, AC3 by the kit's fixture CLI on the built tree and on a scratch
copy, and AC4 by `grep` over the files this pass writes. The spec-token checker over the live tree ran
inside `--dispatch` with the widened guard and the four waiver rows, and the dispatch was declared
and effective. The `New arm:` line's red-first observation, and the §7 legs, are the close's.

**Evidences:** TOOL-dGroundRules-20
- AC1 — `policy fixtures` — `python tools/check-spec-tokens.py --legs-for tools/hooks/agent-cap.js tools/memory-tree/tree_lib.py` printed `policy fixtures <- tools/hooks/agent-cap.js [selftests/kit]` under the hook and `policy fixtures <- tools/memory-tree/tree_lib.py [selftests/kit]` under `tree_lib.py`, exit 0.
- AC2 — `policy fixtures` — the sixteen distinct enforcers of `tools/policy/caps.toml`, derived from the census at observation with `{prefix}` read as `tools`, piped to `python tools/check-spec-tokens.py --legs-for -`: each printed a `policy fixtures <- <the enforcer>` line, 16 of 16, `skills/session-kickoff/manifest-check.sh` among them.
- AC3 — `WRONG` — a scratch git repository holding a copy of the policy kit and of `tools/gate-legs.json`, `{prefix}/roles/handoff.py` removed from the copy's `policy fixtures` guard: `python check_policy.py --fixture fixtures-guard-census` exited 1 printing `{prefix}/roles/handoff.py · inside the policy fixtures guard · WRONG: {prefix}/roles/handoff.py is run by budgets-cap-roster-line and is outside the policy fixtures guard` and `17 assertion(s) executed · 1 wrong`; the manifest restored, it exited 0 with no `WRONG` line, `17 assertion(s) executed · 0 wrong`. On the built tree the case prints sixteen `covered by` lines and `16 enforcer(s) of 33 row(s) · leg found in tools/gate-legs.json`, exit 0; with the census read as empty in-process, its join line reads `WRONG: 0 enforcer(s) of 0 row(s)`.
- AC4 — `grep -c "^policy fixtures <- " memory/project/spec-token-waivers.txt` printed 5 and `grep -cE "^- TOOL-dGroundRules-11[01] · " memory/builds/dGroundRules/BACKLOG.md` printed 2; the registry holds 33 rows in 41 lines, each new row naming the specs it hits, its ask and the count, and deviation 74 records the relaxed count.

Owed at the close, observed by no command in this pass:

- The `New arm:` line of §7, `--fixture fixtures-guard-census`, RED on one census enforcer staged out of the guard and GREEN restored, in the tree the close runs.
- The §7 legs over the built tree, `policy fixtures` and `spec tokens (a spec's own names resolve)` among them; the latter grades the four waiver rows against the guards join's eight hits, which this pass observed only through `--dispatch`'s green run.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: --fixture fixtures-guard-census, check-line-length.sh removed from the policy fixtures guard -> `WRONG: tools/check-line-length.sh is run by budgets-cap-line-length and trips no policy fixtures guard` + guard-trace WRONG (2 wrong). GREEN `151 assertion(s) executed · 0 wrong`.
