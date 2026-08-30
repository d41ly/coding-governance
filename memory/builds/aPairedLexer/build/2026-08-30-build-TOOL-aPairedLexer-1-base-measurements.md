# BASE measurements — the three views `aLexedStripper` left behind

**Serves:** journal TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3

Node `a`, 2026-08-30, BASE `14e21399`. Every verdict is `node tools/hooks/agent-cap.js` over a
`Workflow` payload, taking the exit code and, where it matters, CLASSIFYING which rule fired from the
deny message. `0` is ADMIT, `2` is DENY.

## 1. `TOOL-aPairedLexer-1` — rule 3 is blind below an unterminated template literal

The severe one. `capFindings` reads `blankLiterals`, whose `mode` is carried across lines, so an
unterminated backtick blanks every later line and the rule sees no cap at all.

**The first fixture proved nothing and is recorded because of that.** Four scripts with an UNBOUNDED
receiver all returned `2`, which looked like "rule 3 is fine". They were denied by rule 2's arity
rule before rule 3 ever ran — an unbounded receiver masks the rule under test. The isolation is a
BOUNDED receiver, so rule 2 is satisfied and only the cap can fail, plus classification by message.

| script | template terminated | below an unterminated backtick |
|---|---|---|
| bounded receiver, cap `args.width` (unresolvable) | **2** — rule3 CAP | **0 ADMIT** |
| bounded receiver, cap `500` | **2** — rule3 CAP | **0 ADMIT** |

A cap of **500** is admitted. The rule that exists to stop an unbounded burst does not see it.

## 2. `TOOL-aPairedLexer-2` — rule 1 reads prose as a call

`offendingLines` builds its view with the per-line `stripStrings` and then `.split('//')`, so a
template literal is left intact and a block comment is never stripped. A lens PROMPT naming a
primitive is therefore read as a call.

| where the prose sits | verdict | correct |
|---|---|---|
| in a backticked lens prompt, naming `parallel(` | **2 DENY** | 0 |
| in a backticked lens prompt, naming `pipeline(` | **2 DENY** | 0 |
| in a `/* */` block comment | **2 DENY** | 0 |
| in a `//` line comment | 0 | 0 |
| control: clean prose | 0 | 0 |
| control: a REAL raw primitive | 2 DENY | 2 |

The `//` row admits because `offendingLines` splits on `//` already. The file's own header calls the
block-comment case "benign, fail-closed" — benign is a judgement about cost, and the cost is that
the harness this repo tells authors to write cannot document the rule it is subject to.

## 3. `TOOL-aPairedLexer-3` — the definition probe swallows after a line-comment opener

`scan_js_definitions` strips BLOCK comments before LINE comments (`map_lib.py:461`, mirrored at
`:539`), so a bare block-opener written inside a `//` comment opens a DOTALL span that runs to the
next closer.

Fixture: four definitions, with a block-opener inside a line comment after the first.

```
probe order   finds: alpha
correct order finds: alpha, bravo, charlie
SWALLOWED:           bravo, charlie
```

Adopter-side scale, measured during `aLexedStripper` with `map_lib`'s own `JS_DEFINITION_RULES`
rather than a retyped regex: `d41ly/incms` carries 35 files with the shape and loses **14
definitions across 9**, including an account component pair and a fetch helper. This repo lost 4
until a comment was reworded, which fixes an instance and not the class.

**Swallow SIZE is not harm.** One file there loses 4368 characters and zero definitions; another
loses 5968 and two real components. Only a rule-accurate diff distinguishes them.

## What this record does not claim

No number here is about the FIX; every one is the shipped code at `14e21399`. The `-1` figures are
the ones to re-derive first after any change, because that is the fail-open.
