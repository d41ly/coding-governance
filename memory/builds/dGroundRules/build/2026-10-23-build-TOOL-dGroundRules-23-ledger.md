# TOOL-dGroundRules-23 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-23

No merge bar, no gate leg and no self-test suite ran in this pass. AC1 and AC2 were observed by the
kit's fixture CLI on the built tree and by an in-process probe that ran the same case over a scratch
copy of the census, AC3 by the spec-token checker's `--legs-for` query on the built tree, and AC4 by
`grep` over the waiver registry. The spec-token checker over the live tree ran inside `--dispatch`
with the widened guard and the one new waiver row, and the dispatch was declared and effective. The
`New arm:` line's red-first observation, and the §7 legs, are the close's.

**Evidences:** TOOL-dGroundRules-23
- AC1 — `manifest-bytes` — `python tools/policy/check_policy.py --fixture budgets-ships-join` on the built tree exited 0, `35 assertion(s) executed · 0 wrong`, its join line `26 shipped row(s) of 33, against 30 registry entries resolved by govkit.py`. With a scratch copy of `caps.toml` read in place of the census and the `manifest-bytes` row's `installed` staged to `skills/session-kickoff/manifest-check.sh`, under the kickoff entry's home, the case exited 1 printing `manifest-bytes · its kit writes its enforcer at installed, and no other entry writes it · WRONG: row: kit kickoff-manifest · installed skills/session-kickoff/manifest-check.sh · the resolver writes skills/session-kickoff/manifest-check.sh as kickoff-manifest -> tools/manifest-check.sh`.
- AC2 — `WRONG` — the same scratch copy with the `line-length` row's `kit` staged to `memory-tree`: exit 1 printing `line-length · ... · WRONG: row: kit memory-tree · installed {prefix}/check-line-length.sh · the resolver writes tools/check-line-length.sh as check-line-length -> tools/check-line-length.sh`. With `installed` staged onto the `ships = false` row `AGENTS.md`: exit 1 printing `WRONG: Refusal: ... caps.toml:42 · AGENTS.md has ships = false and carries installed`, the census reader's refusal naming the row.
- AC3 — `policy fixtures` — `python tools/check-spec-tokens.py --legs-for tools/govkit/govkit.py tools/govkit/entries/check-line-length.kit.toml` printed `policy fixtures <- tools/govkit/govkit.py [selftests/kit]` under `govkit.py` and `policy fixtures <- tools/govkit/entries/ [selftests/kit]` under the descriptor, exit 0.
- AC4 — `grep -cw tools/roles/kit.toml memory/project/spec-token-waivers.txt` — printed 1 and `grep -vc "^#" memory/project/spec-token-waivers.txt` printed 34; the registry holds 34 rows in 42 lines, and deviation 75 records the relaxed count.

Owed at the close, observed by no command in this pass:

- The `New arm:` line of §7, `--fixture budgets-ships-join`, RED on one shipped row's `installed` staged off its resolved destination and on one row's `kit` staged to another entry, GREEN restored, in the tree the close runs.
- The §7 legs over the built tree, `policy fixtures` and `spec tokens (a spec's own names resolve)` among them; the latter grades the new waiver row against the guards join's one hit on TOOL-aScoutedSeam-1, which this pass observed only through `--dispatch`'s green run.
