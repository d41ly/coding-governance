**Serves:** research TOOL-dWitnessedBar-51

# Round-10 size brief — unit 51 is over the spec ceiling

TOOL-dWitnessedBar-51 is 49203 bytes against `check-spec-tokens.py`'s ceiling of 49152. You did not grow it: the
build index re-render adds each new unit id to the agent ledger's row in every spec's generated records table, and
round 10 added four. Each later round adds roughly 100 to 150 bytes the same way.

Trim unit 51's authored prose to 47800 bytes or less, measured with `wc -c` over the whole file as it stands, so
it carries headroom for about ten more rounds.

- Trim non-criterion text only: §1 context, §4 rollout narrative, §8 resolved-fork history and §9 rev entries
  restated elsewhere. Keep every §2 scope item, every §6 criterion and its observation, every §3 edge, every
  `**Carries:**` token and every §7 leg line exactly as they read.
- Never touch the `gen:` regions; the generator owns them.
- Unit 51 is committed and audited: this trim moves no criterion, so it joins the spec's latest rev entry in §9 as
  one line saying prose was trimmed for the size ceiling; do not bump the rev. Touch no other spec and no deviation
  record. Do not commit, do not stage, and do not run the build-index generator. Your role admits the hygiene gate
  and the lexicon only.
- Return the byte count before and after, and what you cut by section.
