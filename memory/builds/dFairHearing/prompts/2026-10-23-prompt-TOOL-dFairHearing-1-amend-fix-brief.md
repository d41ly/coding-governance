**Serves:** research TOOL-dFairHearing-1 TOOL-dFairHearing-17

# Amend-fix brief — the two deviation records rewrite their clauses in part

The as-built view (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`) replaces an amended clause's whole text with its deviation record's **After:** line. That makes **Before:** and **After:** each a WHOLE clause, never an excerpt.

## Deviation 11

File: `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-1-deviation-11.md`.

Its **Before:** line stops at "in each run". Its **After:** line drops the clause's opening (the blind run at blob 767187aa, from a bundle of the history to 6cfd21619 cloned outside the repository) and its tail (the miss rule and the three further replays). So the amended clause at `89c89732` loses words while the record claims risk `additive`.

- Rewrite **Before:** as the clause's whole baseline text. It is the text at `cl-dClosedLoop-0068@b4e6c04e` in the packet as committed at `455442c67`: `git show 455442c67:memory/builds/dFairHearing/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, Items 1.
- Rewrite **After:** as that same whole text, with only the known-set change the record argues for.

## Deviation 171

File: `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-17-deviation-171.md`.

Its **After:** line names CONVERGING only "on a round that is still falling under its limit". The spec's rule also gives CONVERGING:

- on round 1 with findings standing, which has no round before it;
- on any run with no `roundLimit`.

Reword **After:** so it states the rule the spec builds, and keep every other word of the clause.

## Then re-pin both specs

For each record, compute the amended clause's new hash with the shipped parser. This is a read-only probe:
`python -c "import sys; sys.path.insert(0,'tools/memory-tree'); import design_lib; print(design_lib.derive_clause_hash(open('<file>', encoding='utf-8').read()))"`, applied to the After text exactly as the as-built generator takes it. Read `derive_clause_hash` (`tools/memory-tree/design_lib.py:169`), and the view's generator through `gen_build_index.py`'s as-built render, to see which text it hashes.

Then set:

- `TOOL-dFairHearing-1`'s `**Carries:**` to `cl-dClosedLoop-0068@<new hash>`;
- `TOOL-dFairHearing-17`'s `**Carries:**` to `cl-dClosedLoop-0084@<new hash>`.

Both specs stay at rev-2. Amend each rev-2 §9 line to name the new hash, since rev-2 is uncommitted.

## Rules for this pass

- Change nothing else.
- Do not commit, do not stage, and do not run the build-index generator or any gate; the main loop re-renders the view and runs the token check, which confirms or refutes your hashes.
- Report each record's new Before and After lines, and each new hash.
