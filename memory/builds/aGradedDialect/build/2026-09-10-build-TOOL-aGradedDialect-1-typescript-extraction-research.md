# TOOL-aGradedDialect-1 — reading TypeScript: the candidates, the tests that killed three of them, and the pick

**Serves:** research TOOL-aGradedDialect-1

**Commissions:** TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5

## Verdict: CLEAN

The fork is resolved by measurement rather than by preference, and the losing conditions were
written down before anything ran. Everything below re-derives from the two snippets in §6 against a
corpus this record names by path and by date.

## 1. What was being decided

`TOOL-dScaffoldedMirror-13` declared `.ts` and `.tsx` dark deliberately on 2026-08-24, and named its
own revisit test: revisit after `-8` lands, and only with conformance fixtures extracted from real
adopter files rather than authored. Both halves hold on 2026-09-10 — `-8` closed 2026-08-25, and the
adopter tree it was measured against is present on node `a`. The owner's prompt for this build is the
session that test asked for.

So the question is not "should the kit read TypeScript" — the owner answered that. It is **by what
MECHANISM**, and `-13` left four recorded objections that any mechanism has to answer.

## 2. The corpus, measured

Read-only, on 2026-09-10, at `C:/projects/incms/main`. Nothing in that tree was written.

| figure | value | re-derived by |
|---|---|---|
| tracked files | 6550 | `git ls-files \| wc -l` |
| tracked `.ts` | 656 | `git ls-files '*.ts' \| wc -l` |
| tracked `.tsx` | 601 | `git ls-files '*.tsx' \| wc -l` |
| function/method definitions | 5017 | the §6 oracle |
| type definitions | 1369 | the §6 oracle |

`-13` measured 626 `.ts` and 572 `.tsx` on 2026-08-24; both grew, and the armed-coverage headline it
recorded (19.3%) is unchanged to one decimal at 19.2%. The two measurements agree, which is worth one
line because a disagreement here would have meant one of them read a different tree.

**The oracle is `typescript@5.9.3`, already present in that tree as a dev dependency.** It is the
TypeScript compiler's own parser, so it is INDEPENDENT of everything this kit ships and of everything
this build will write. That independence is the whole answer to `-13`'s fixture objection, and it is
a property of which program produced the numbers rather than a claim about the author's care.

## 3. The candidates, and what would make each LOSE

Written before any measurement ran, which is what makes them tests rather than rationalisations.

| # | mechanism | loses if |
|---|---|---|
| C1 | a `ts-regex` set added to `PATTERN_SETS` in `lexicon.py`, mode `probe` | two plausible regex sets disagree by more than 20% of the population, or recall falls below ~70% |
| C2 | a tokenizer-plus-locator in the kit, mode `parser`, the `shell-tokens` design ported | the corpus carries constructs no tokenizer can locate definitions through, or a `parser` claim cannot be substantiated against the oracle |
| C3 | shell out to `tsc` or `esbuild` at grade time | M3 veto 2 — a new external dependency and install location |
| C4 | the same regexes shipped as rows `scaffold_lexicon.py` PROPOSES into the adopter's own `.lexicon.conf`, mode `probe` | the regex family loses on C1's test, since C4 changes the carrier and not the reading |

C4 is on the list because it is the option `-13`'s literal wording leaves open — that record refuses
"no `PATTERN_SETS` entry, no regex probe set", and a scaffold-proposed row is neither an engine
constant nor a thing an upgrade overwrites. It is a real mechanism, not a technicality, and it loses
on evidence rather than on the wording.

## 4. What the tests returned

### 4.1 The regex family, scored against the compiler

Reading A is the set the kit ships TODAY (`PATTERN_SETS["js-regex"]`, copied verbatim), pointed at
`.ts`/`.tsx` — which is the best an adopter can do right now with no code change at all. Reading B is
a good-faith TypeScript-aware set: `export default function`, generics, type annotations on arrow
bindings, class and object-literal methods, class-property arrows, and `interface`/`type`/`enum` for
types.

| reading | functions recall | functions precision | types recall | types precision |
|---|---|---|---|---|
| A — shipped `js-regex` | 76.1% (3819/5017) | 99.2% | **0.6% (8/1369)** | 100.0% |
| B — best-faith TS regex | 85.8% (4303/5017) | 86.5% | 100.0% | 76.0% |

**A's type row is the sharpest number in this build.** `js-regex.types` matches `class` and nothing
else, and TypeScript declares its types with `interface`, `type` and `enum`. So the escape hatch that
exists today — point `js-regex` at `.ts` — grades 8 of 1369 type definitions and reports a clean run
over the other 1361. That is the concrete shape of "ships without TypeScript support at all", and it
is worse than the absence, because it is an absence that answers `OK`.

**B buys its recall with false positives.** 670 spurious function names and 432 spurious types. A
false positive in P1 is not incompleteness — it is a name graded that no definition site produced, so
an adopter draining their verb debt would be chasing offenders that do not exist.

**The pre-registered test fired.** A and B disagree on 1123 function names against an oracle total of
5017, which is 22.4% of the population — over the 20% threshold written down in §3. Per-file, B's
function recall has a median of 100.0% and a worst-decile of 50.0%, and 19 of the 1055
definition-carrying files score ZERO. A reading that is perfect on the median file and blind on the
worst tenth is exactly the distribution a per-file report cannot surface.

**C1 and C4 LOSE.** Same test, same evidence, and C4 loses for C1's reason because it ships C1's
reading in a different file.

### 4.2 Why the regex family loses, structurally

The constructs that break a same-line regex are not rare in this corpus; they are the corpus.

| construct | files carrying it | share |
|---|---|---|
| template literal | 1135 | 90.3% |
| JSX element | 907 | 72.2% |
| generic call or declaration | 711 | 56.6% |
| nested template expression | 548 | 43.6% |
| regex literal | 313 | 24.9% |
| `satisfies` operator | 37 | 2.9% |
| decorator | 1 | 0.1% |
| overload signature | 0 | 0.0% |

A `${...}` inside a backtick string can contain anything, including a `function` keyword and a `=>`.
That is 43.6% of files carrying a construct in which a regex cannot tell code from data. This is the
same finding `shell-tokens` was built on, one language over, and it arrives with a larger share.

The last two rows earn their place by being SMALL: decorators are one file and overload signatures
are none, so a reader may declare both out of scope and lose almost nothing. Recording a zero here is
the point — it is what lets unit 3's refusal list be short and defensible instead of imagined.

### 4.3 C3, and the veto that kills it

`tsc` and `esbuild` are a new external dependency and a new install location, which is M3's veto 2
verbatim. Two further facts make it not close. The kit ships a self-containment REFUSAL asserting
that every non-relative import names stdlib or a sibling file in the kit directory, and an adopter of
this kit is not required to have Node at all — this repo, its reference dogfood, does not run it in
any gate. C3 loses without a measurement, and the test that decides it is the reading of a shipped
constraint rather than a run.

### 4.4 The two objections `-13` raised about the VOCABULARY, now measured

These do not decide the mechanism fork. They are recorded here because `-13` named them as blockers,
and measuring them is how they are discharged rather than argued away.

**The casing objection — "it would arm a casing rule over 1072 PascalCase React components".** True,
and it lands almost entirely in one extension:

| cell | camel | pascal | screaming | snake / other |
|---|---|---|---|---|
| `.ts` function/method (2409) | 94.8% | 4.2% | 0.9% | 0.1% |
| `.tsx` function/method (3108) | 69.4% | **30.3% (943)** | 0.2% | 0.1% |
| `.ts` type (865) | 0.5% | 99.1% | 0.3% | 0.1% |
| `.tsx` type (504) | — | 99.8% | 0.2% | — |

`.ts` and `.tsx` are SEPARATE CELLS in this kit's matrix, so three of those four rows are answered by
a declaration and no exception list: `ts.function` is camel at 94.8%, and both type rows are pascal
at over 99%. The fourth row is not answered, and §5 says so plainly rather than rounding it away.

**The unmeasured-vocabulary objection — "a synonym predicate over a TypeScript corpus nobody has
measured".** Measured now, against the kit's own shipped canon of 20 verb spellings: **13.7% of `.ts`
and 11.2% of `.tsx` definitions lead with a canon verb.** The consequence, stated rather than
implied: arming extraction does NOT arm P1 usefully by itself, because an adopter switching it on
against the shipped canon meets roughly seven offenders in eight. That is not a defect in this build
— pins are MEASURED from the adopter's own corpus by `--scaffold`, and the `CANON:` door exists for
exactly this — but a session that ships extraction and calls P1 "armed for TypeScript" would be
making a claim these figures refuse.

## 5. The pick, and the one thing it does not solve

**C2 wins**, by M3's rule: the most feature-rich survivor after the vetoes. It is the only candidate
with no false positives by construction, the only one that reaches every definition form rather than
the ones a pattern author remembered, and the only one whose failure mode is a REFUSAL — an
unreadable file raises, the way `parse_shell_defs` raises — rather than a quiet undercount. It
answers all four of `-13`'s objections: the casing rule is answered per cell by §4.4, the vocabulary
is measured in §4.4, the fixtures come from a compiler this build does not ship, and the vacuity
defect that made a second probe set unwise was closed by `DEAD PROBE`, `DEAD CELL` and the
armed-but-grading-nothing report.

It is also the design this repo has already ratified once. `shell-tokens` shipped for the same reason
against the same evidence shape, and porting a ratified design is the tie-break M3 names last.

**`parser` is a CLAIM THIS BUILD MUST EARN, not a label it may write.** The mode table says `parser`
means complete over its extension. So unit 3 declares `parser` only if it scores at or above the
floor unit 2's fixtures set, against the oracle, on the real corpus; below that floor it declares
`probe` and says so every run. Writing `parser` because the code contains a tokenizer would be the
gate-satisfied-by-its-own-shape class this kit exists to refuse.

**THE ONE THING C2 DOES NOT SOLVE, stated here so no later reader has to find it.** `.tsx` functions
are 69.4% camel and 30.3% pascal, and the split is by ROLE — a React component is a function that
returns JSX. The kit's own README names this exact population as the selector's motivating case:
"the languages whose case is a function of ROLE rather than of surface — Go's export rule, React's
PascalCase components". But the two shipped selector kinds are `prefix` and `decorator`, and a React
component is neither prefixed nor decorated. **So the mechanism designed for this population cannot
reach it**, and the three dispositions available today are all bad: declare `tsx.function` camel and
carry a 943-offender pin that reds on every new component; declare it pascal and make 2157 correct
names offenders; or declare it dark and lose 3108 definitions of coverage.

A `case:` selector kind is NOT the answer and is refused here rather than left to be discovered: a
name selected BECAUSE it is pascal and then graded AGAINST pascal can never fail, which is the
vacuous-selector class this repo names. The selector has to key on something the EXTRACTOR knows and
the name does not — whether the definition's body returns JSX — which is available only once C2
exists. That is why it is unit 4's, and why it is a fork in that unit's spec rather than a decision
taken here.

## 6. The evidence, runnable

Both snippets are read-only. Run the first from the adopter repo root, then the second from anywhere.

`ts-oracle.js` — ground truth from the TypeScript compiler. It answers the question
`lexicon.py:_python_defs` answers for Python: every function or method defined anywhere in the file,
and every type defined there, nested definitions included the way `ast.walk` counts them.

```javascript
const ts = require(process.env.TS_MODULE);
const fs = require('fs');
const files = fs.readFileSync(process.argv[2], 'utf8').split('\n').filter(Boolean);
function nameOf(node) {
  if (!node) return null;
  if (ts.isIdentifier(node)) return node.text;
  if (ts.isStringLiteral(node) || ts.isNumericLiteral(node)) return node.text;
  if (ts.isPrivateIdentifier(node)) return node.text;
  return null;   // a computed key has no definition-site NAME to grade
}
for (const f of files) {
  let src;
  try { src = fs.readFileSync(f, 'utf8'); } catch (e) { continue; }
  const sf = ts.createSourceFile(f, src, ts.ScriptTarget.Latest, true,
    f.endsWith('.tsx') ? ts.ScriptKind.TSX : ts.ScriptKind.TS);
  const funcs = [], types = [];
  const at = (n) => sf.getLineAndCharacterOfPosition(n.getStart(sf)).line + 1;
  function push(list, node, nameNode) { const n = nameOf(nameNode); if (n) list.push([n, at(node)]); }
  function walk(node) {
    if (ts.isFunctionDeclaration(node)) push(funcs, node, node.name);
    else if (ts.isMethodDeclaration(node) || ts.isMethodSignature(node)) push(funcs, node, node.name);
    else if (ts.isGetAccessorDeclaration(node) || ts.isSetAccessorDeclaration(node)) push(funcs, node, node.name);
    else if (ts.isConstructorDeclaration(node)) funcs.push(['constructor', at(node)]);
    else if (ts.isVariableDeclaration(node) && node.initializer &&
             (ts.isArrowFunction(node.initializer) || ts.isFunctionExpression(node.initializer)))
      push(funcs, node, node.name);
    else if ((ts.isPropertyAssignment(node) || ts.isPropertyDeclaration(node)) && node.initializer &&
             (ts.isArrowFunction(node.initializer) || ts.isFunctionExpression(node.initializer)))
      push(funcs, node, node.name);
    if (ts.isClassDeclaration(node) || ts.isInterfaceDeclaration(node) ||
        ts.isTypeAliasDeclaration(node) || ts.isEnumDeclaration(node)) push(types, node, node.name);
    ts.forEachChild(node, walk);
  }
  walk(sf);
  process.stdout.write(JSON.stringify({ file: f, funcs, types }) + '\n');
}
```

```bash
cd <adopter-root>
git ls-files '*.ts' '*.tsx' > /tmp/tsfiles.txt
TS_MODULE=<adopter-root>/node_modules/typescript node ts-oracle.js /tmp/tsfiles.txt > /tmp/oracle.jsonl
```

`regex_vs_oracle.py` — the scoring arm. Reading A is copied verbatim from
`tools/lexicon/lexicon.py`'s `PATTERN_SETS["js-regex"]`, so the arm grades the shipped bytes rather
than a paraphrase of them; reading B is the four function patterns and four type patterns §4.1
describes. Both readings drop a short control-keyword stop-list from the method arm only. It prints
recall, precision, the A-versus-B disagreement count, and B's per-file recall distribution. The full
source, including reading B's eight patterns, is reproduced in
`memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md` §4, where the fixture
unit that owns the oracle can keep it beside the format it feeds.

## 7. What this record does NOT claim

- It does not claim a tokenizer WILL reach the `parser` floor. That is unit 3's acceptance criterion
  and unit 2's fixtures are what would refuse it. This record picks the mechanism; it does not
  certify an artifact that does not exist.
- It does not measure extraction QUALITY for `.js`. Reading A was scored against TypeScript files,
  which is the question this build asks; whether the shipped `js-regex` set should also retire is a
  separate question with a separate population, and it is a backlog row rather than a scope item.
- It does not adopt the kit onto the adopter tree. `-13` §3 draws that line and this build keeps it.
