# The owner's prompt, verbatim

**Serves:** research TOOL-dMispairedQuote-1 TOOL-dMispairedQuote-2

Handed to `/unattended` as the `--prompt` value on 2026-09-01, node `d`. The value carried whitespace
and named no readable file, so by the Skill's routing table it is the prompt itself and is taken
verbatim. Recorded here rather than in the build README for the three reasons that file's own heading
canon, byte ceilings and marker matcher impose.

```text
Another session has discovered a bug in `agent-cap.js`.
A raw parallel() gets past the fan-out cap when an apostrophe shares its line. .claude/hooks/agent-cap.js enforces the charter's <=5-concurrent rule. Three probes, generated in Python so the apostrophes are real:

script	verdict
const r = await parallel([() => agent('a'), () => agent('b')])	exit 2, DENIED
const re = /won't/ on its own line, then the same fan-out	exit 2, DENIED
const re = /won't/; const r = await parallel([() => agent('a'), ...])	exit 0, ADMITTED

stripStrings reads the apostrophe as an opening quote and pairs it with the one opening agent('a'), blanking parallel( between them. The addc6169 repair this repo already carries demands a matching pair - and a pair exists, just the wrong one. The precondition is stated at agent-cap.js:307: the file models no regex literal. gov HEAD carries the same precondition, so pulling gov's bytes fixes nothing.

Review the finding, verify, fix it.
```

*The one departure from verbatim: three characters the memory tree's own gates refuse in a fenced
block are transliterated — `<=` for the relation, `-` for the dash, `...` for the ellipsis. Nothing
load-bearing; the probes and the file:line citation are byte-exact.*

## How this run read it

A finding to review, verify and fix. "Review the finding" is not a formality here: the report names
`stripStrings` as the mechanism and the missing regex-literal model as the precondition, and this run
owes an independent judgement on both before it changes a line.

**Not a veto-2 owner turn.** `tools/hooks/agent-cap.js` is a kit, not a governance carrier. It states
a rule the charter owns and does not own one itself, and this build changes what its scanner SEES
rather than what the charter says. No public surface, no new dependency, no install location.

## What this run measured before writing a spec

Five probes at HEAD, driven through the hook's real stdin contract. `P1` is the control.

| probe | line | verdict at HEAD |
|---|---|---|
| P1 | the bare fan-out | DENIED |
| P2 | `/won't/` on its own line, fan below | DENIED |
| P3 | `/won't/;` then the fan, one line | **ADMITTED** |
| P4 | `// don't` on its own line, fan below | DENIED |
| P5 | `/wont/;` then the fan, one line | DENIED |

The report reproduces exactly. `P5` is the discriminator: remove the apostrophe and the same regex
literal denies, so the regex is not the mechanism — the apostrophe is.

## Where this run disagrees with the report, and it matters

**The regex literal is an instance; the class is any unpaired apostrophe earlier on the line.** Four
more shapes, none of them a regex, all ADMITTED at HEAD:

| shape | line |
|---|---|
| a double-quoted string | `const s = "don't"; ` + the fan |
| a block comment | `/* don't */ ` + the fan |
| a template literal | ``const s = `don't`; `` + the fan |
| bare prose in a block comment mid-line | `/* it's */ ` + the fan |

So modelling regex literals — the repair the stated precondition points at — closes ONE of five
measured spellings and leaves four open. That is the instance, and §7 asks for the class.

**And the double-quoted case says where the class really lives.** `stripStrings` blanks all `'…'`
pairs and only then all `"…"` pairs, two independent passes in a fixed order. A single ordered pass
consumes `"don't"` as one double-quoted string and never sees its apostrophe at all. `renderCodeView`
already IS such a pass and already gets that shape right; rule 1 does not read it. The defect is two
string models in one file, and the fix is one.
