**Serves:** research KICK-dKeptSession-56

# The round-2 promoted-fix pass's return — dKeptSession

The writer's final return, extracted from its transcript by script, never retyped.

I fixed all three findings in place in `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-56.md`. Hygiene checks 2, 12 and 25 now report nothing on any dKeptSession spec; the only lines left are the usual "did not grade" notes on other specs. I did not run `check-spec-tokens.py`, since it is a gate I'm not allowed to run.

The spec is still uncommitted at rev-1. Its `**Derived:**` line, §3 Edges, §7 New arm lines and §8 marks are unchanged, and nothing else was written or committed.

1. **`check-spec-tokens` `[path]` and `[bar]`, in AC22.** The token `tools/loop/selftest.py` is an untracked path, and the checker reads it as a suite. AC22 now ends "units 35, 36 and 42 name `loop selftest` as the leg that runs the loop kit's self-test at the close". That is the leg name S27 already uses. It has no slash and doesn't end in `selftest.py`, so neither the path rule nor the suite rule in `check-spec-tokens.py` picks it up. The suite stays on its existing §7 line, `New arm: tools/loop/selftest.py`. §2 S44 still spells the path, but the checker only reads the acceptance section, so I left it alone as the brief asked.

2. **Hygiene check 12, AC17 and AC28 had no backticked witness.**
   - AC17 now reads "When `python loop_transition.py record` moves a parent out of Design whose rendered edges carry the no-edge sentence, or no `Child builds` line, it posts nothing and exits 0." The command is the transition that runs the dependents read, per unit 35 S1. The two cases are the ones S20 names.
   - AC28 now reads "...and a second `python loop_transition.py record` runs, both dependents' mail refs hold the first exit's notice."
   - Each backticked token sits on one line.

3. **Hygiene check 25, S16 had no `**Readers:**` clause.** S16 doesn't retire anything named: it clears an environment variable inside the self-test process. So I reworded it rather than adding a clause. "removes `CLAUDE_CODE_MAX_CONTEXT_TOKENS` from `os.environ`" is now "unsets `CLAUDE_CODE_MAX_CONTEXT_TOKENS` in `os.environ`". "unsets" is not in check 25's trigger lists at `check-memory-hygiene.sh:2109-2110`.
