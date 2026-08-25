**Serves:** spec-audit TOOL-dPromptedSeam-1

# Spec audit — TOOL-dPromptedSeam-1, round 1

**Range:** the spec at `671e953d`, before any code. **2026-08-25** · node `d`.

**Shape:** three cold lenses — mechanism feasibility, acceptance falsifiability, premise and
proportion. None of the three wrote the spec. Every headline claim below was re-verified by hand
against the tree before being accepted, because two of them overturn the author's own work and one
of them corrects an author error.

## Verdict: BLOCKED

The GOAL survives and the MECHANISM does not. Three lenses converged independently on the same
conclusion: the spec proposes to feed `reuse_lookup.py` the one input its own documentation tells
callers not to give it, priced against a cost figure that is roughly ten times too large, in a
direction this repo's own declaration forbids.

## The three findings that refute the design

**R1 — the cost figure was wrong, and it was load-bearing.** §4's D4 is titled "cost is the binding
constraint" and cites 1.85 s. Two lenses independently measured ~0.19 s; re-running the author's
*exact* original command now gives 0.197 s, and a pycache-cleared cold run gives 0.24 s. The 1.85 s
was a single wall reading taken while a full gate bar and three subagents were running — contention
recorded as steady state. `memory/gotchas/process-creation-is-the-suite-cost.md` says in as many
words that wall readings on this node vary and that spawns should be counted instead; the author had
read it and measured once anyway. D4 buys `REUSE_HINT_TIMEOUT_S`, its grammar, the kill logic, one
of the five outcomes, and AC5. At 0.19 s against a `--suggest` baseline of 0.07 s, that is a declared
budget guarding nothing.

**R2 — the query shape contradicts the called tool's written contract.**
`tools/codebase-map/reuse-lookup.agent.md:14` reads: *"Describe the behaviour, not a name you already
picked."* D3 feeds it a bare token mechanically stripped from a name the author has just picked. The
premise was tested on three objects — `conf`, `index`, `verbs` — all of them objects of the file the
author was looking at. Measured against the real population instead: over 326 live P1 offenders,
35.3% produce no object at all, 8.0% produce an object matching nothing, 40.2% produce noise, and
16.6% surface a real seam. A second lens measured 231 off-table symbols and got 15%. The premise
"a bare object token is a useful query" is established for three hand-picked cases and refuted for
roughly five in six.

**R3 — the direction is one this repo's own declaration forbids.** `.lexicon.conf` declares
`LAYERS: tools/lexicon/* -> tools/codebase-map/*`, with the conf's own comment stating that the kit
must ship self-contained and that this is *"the machine-checkable form of it."* The spec proposes a
subprocess in exactly that direction and satisfies the gate only because P3 grades `ast` imports and
cannot see an exec. The spec is open about the subprocess — it is not sneaking — but it neither
widens P3 nor amends the declaration, and §7's rule that a gate's own header must state what it does
not check is left unaddressed. This is the charter's "a structural check reads as a semantic one to
everybody who did not write it" class, and this unit would be the first thing through the gap.

## What the acceptance criteria were worth

Four of eight cannot fail.

- **AC1** asks the hint to name `load_conf` — which the *primary line already prints*, because
  `load_conf` is the suggestion. The empty implementation passes. This is the exact collision
  documented in the file this unit extends, `tools/lexicon/selftest.py:884-897`, where a row passed
  on the message template rather than the suggestion. The author fixed that defect earlier the same
  day and then re-picked the one example where the collision is guaranteed.
- **AC6** names `python tools/lexicon/selftest.py` to observe adapter behaviour, but every arm in
  that suite runs in a fixture holding only the lexicon kit — so the adapter takes the *map not
  adopted* branch and never reaches the code AC6 makes raise. True before the adapter exists, true
  for a broken one.
- **AC2** and **AC8** are satisfied by doing nothing: pure absence, and absence is the default.
- The stated **non-vacuity arm** is satisfied by the degenerate outcome, because every existing
  fixture lacks `.codebase-map.conf`. That is the same `or`-escape recorded at
  `tools/drift-audit/selftest.py:828-831`, which the author had fixed hours earlier.

All eight carry a backticked witness token, so the shape gate passes on all eight. Three of them are
shape-green and meaning-empty — which is the gap a witness gate states plainly it does not close.

## Two claims of the author's that did NOT survive, and one that did

- **D5's "there is no cycle"** is true about imports and misleading as reassurance. Verified:
  `reuse_lookup.py` imports `map_lib`, which imports only stdlib, and never reaches
  `map_extractors.py`. But `lexicon-verbs` IS one of the 172 inventory keys in the corpus the hint
  reads — confirmed by reading `inventories.json` — so the lexicon's own declared vocabulary is part
  of the population its hint would search. No cycle breaks; a self-reference the spec said did not
  exist does.
- **D7 contradicts itself.** "No reformatting: a second renderer for another tool's output is a
  second answer" cannot coexist with "capped at the top three candidates". `reuse_lookup` has no
  `--top` and no `--json`, so capping means slicing its uncontracted prose on a heading anchor —
  which is a parser. Worse, the cap drops the partial-recall notice, and this repo declares `bash`
  recall-dark so that notice fires on **every** run here. §10 claims it is "consumed verbatim"; as
  designed it is discarded.
- **The §5 security note is correct**, on two lenses' independent reading: `subtokens` yields word
  characters joined by `_`, so no separator and no leading `-` can reach argv.

## The outcome taxonomy was wrong in both directions

The spec worried that five names might describe four states. Measured, they are genuinely
distinguishable — exit 2 with empty stdout for refused, exit 0 with a rendered report for no match.
The real defect is the opposite: there are **six** states and the missing one is modal. "The corpus
was read and nothing matched" is neither *object empty* nor *hint printed*, and under D7's cap it
renders as zero appended lines — the silent omission S4 says is not one of the five. Exit 1 on a
malformed committed artifact has no name either.

## Recommendation

Ship the goal through the Skill, not through the kit. Both halves already exist and are already
wired: `.claude/skills/lexicon/SKILL.md` carries a "When a name genuinely will not fit" ladder, and
`tools/codebase-map/reuse-lookup.agent.md` already turns a shortlist into a decision. The integration
is one more rung on that ladder — *if the refusal suggests the function may not need to exist,
describe the BEHAVIOUR to `reuse_lookup.py`, a sentence, not the name you picked.*

That costs a few lines in one template and a re-render, gated by `lexicon wiring`, which is
unguarded and runs on every bar. It needs no subprocess, no conf key, no timeout, no discovery
logic, no outcome taxonomy, and no off-switch. It does not touch the LAYERS ban. And it hands
`reuse_lookup` a behavioural sentence written by someone who knows what they are about to build,
which is the input the tool documents wanting and the difference between a 16.6% mechanical hit rate
and the tool working as designed.

It loses automatic firing, and that is a real loss rather than one to argue away. Weighed against
automating the wrong query, prompting for the right one wins.

## The better unit this audit surfaced

`read_object()` has no stopword handling and no minimum length. Measured: 68 of 231 off-table symbols
yield no object at all, and 15 more yield objects that are entirely stopwords — `pin_of` → `of`,
`fan_in` → `in`, `boundedK` → `k`. Falling back to the FULL IDENTIFIER when the object has no live
stem recovers a non-self seed in **51 of those 68** and **12 of the 15**: `Dossier` →
`parse_dossier`, `Conf` → `load_conf`, `cache_of` → `build_cache`.

That is a defect in the lexicon's own helper, it improves `--brief` today, it needs no cross-kit
anything, and it is a smaller unit than the one this spec proposes. It should probably be built
first regardless of what happens to the integration.
