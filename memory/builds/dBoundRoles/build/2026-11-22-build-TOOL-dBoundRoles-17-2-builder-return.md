**Serves:** journal TOOL-dBoundRoles-17

# TOOL-dBoundRoles-17 — the second builder's return, a divergence on rev-6

Run `wf_25370bd3-656`, started at `f50b88cde` on rev-6. It wrote nothing and committed nothing; `diverged: true`.

## The divergence, as returned

1. §5 says no help page describes handoffs, which is false: `help/roles.md` describes `handoff.py render` in its
   steps and carries a usage anchor for the render verb, and `tools/govkit/usage.toml` declares that verb's flags as
   an authored list without `--item`. This unit adds `--item`, the `**Answers:**` obligation and the R16 refusal, so
   the docs rule owes both files, and the render row's fingerprint moves with the flag list.
2. S6 edits `tools/memory-tree/check-memory-hygiene.sh`, which is on the kickoff manifest's `watch:` list in
   `memory/guides/SESSION-KICKOFF.md`, so the pass owes the manifest's re-stamp, and that path is not in the write set.
3. S6 renders `memory/HYGIENE.md` through a `.test.sh` file, which a builder may not run.
4. §4's return predicate, a research record whose text names exactly one handoff's path, reads two ways: matching
   the repository-relative path string, or matching a handoff's file name in any cited path. Only the second reproduces
   the population pin the spec carries. The spec does not say whether the `**Answers:**` line's own path counts.
5. S2 says each reader returns an `item` beside the fields it returned before, but `handoff.py#check_handoff`,
   `#print_agent_lines` and `tools/playbook/edge_grammar.py#read_handoff_edges` return check lines, ledger lines and
   edges, with no field record to extend.

It also advised that `--legacy-rows` read the head itself to stamp the home's header sha, since the seed argv cannot
pass one. Every blob-pinned citation held at `f50b88cde`.

## The decision

Items 2 and 3 are the main loop's: the write set gains the manifest and the pass re-stamps it in its own commit, and
the main loop renders `memory/HYGIENE.md` from the template in a follow-up commit naming the unit, the route unit 21's
mirror took. Items 1, 4 and 5 go to the spec writer: item 4 takes the reading that reproduces the pin, by M3 as a
delegated resolution. widens: none · relaxes: none.
