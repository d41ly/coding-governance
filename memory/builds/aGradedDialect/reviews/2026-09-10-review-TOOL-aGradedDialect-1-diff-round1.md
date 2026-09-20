**Serves:** diff-review TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5

# aGradedDialect — Tier-2 diff review of the cumulative landing diff

*Node `a`, 2026-09-10, branch `branch/lexicon-kit-typescript-34c322`. Adversarial pass over the diff
that lands on `main`: four primed lens passes, five skeptic batches prompted to REFUTE, one
synthesis. Every finding below was re-checked at source — most by executing the cited function in
this tree — before it was written here.*

**Reviewed range: `d13576732e6837e4be62edf5c60eb43631f94cd0...HEAD`** (29 commits, 42 files, +6941
/ -82). HEAD is `5f1815af3411b055341746ab0d0f372ae294b922`. The four subjects that carry every
finding, pinned at the blob they were read at:

- `tools/lexicon/lexicon.py@8aeabac6dae16c547c984f5bc82a9bcce141441d`
- `tools/lexicon/lexicon_conf.py@4d0d9eaee45ce8d4c8f5b56be04b960b0abf7a63`
- `tools/lexicon/ts-conformance-fixtures.json@99521622975edb09390777d04ed847abd607ebe4`
- `tools/drift-audit/drift_report.py@042d3dd55717c3fec9da0d507b803cf1e7579316`

**Round: 1.** This is the first review of the CODE. Rounds 1-3 in this folder audited the five
specs; none of them read a line of `lexicon.py`, so nothing here is a re-report.

## Verdict: BLOCKED

One blocker and four highs. The blocker is not a code defect: this branch commits 76 KB of verbatim
source from a PRIVATE codebase into a repo whose `origin` is a PUBLIC GitHub repository, and the
unit that priced the disclosure priced only the adopter copy-install path, never publication. It
needs an owner decision before the push, not a patch. The four highs are all one shipped feature —
the TypeScript reader — refusing or mis-reading ordinary TypeScript, in classes the frozen
conformance corpus cannot see.

Nothing here overturns a design decision. The `.ts`/`.tsx` mechanism pick, the earned-mode rule, the
two-parser split, the frozen corpus as an instrument and the `resolve_extractor` consolidation all
held. Eleven of the fourteen entries are defects in one hand-written tokenizer, which is the
expected shape for a fresh 787-line parser and exactly the surface §8 says heavy multi-lens review
earns its tokens on.

**Read this repo's green bar carefully.** `.lexicon.conf` arms `py` and `sh` and leaves `ts`/`tsx`
undeclared, and this tree tracks ZERO `.ts` or `.tsx` files (checked). So no gate in this repo can
reach any parser finding below, and the 104/104 green covering this branch is not evidence about
them. Every one of them is adopter-facing, and the first adopter to arm `ts` pays.

### Review shape

Raw 20, confirmed 16, refuted 4, unverified 0. Precision 0.80.

Precision is well above the ~0.5 floor §8 names, and 0.80 against 0.47 in round 3 says the lens
priming was right for a fresh surface: this is the "fresh/complex write path" case where multi-lens
review pays, not the hardened-code case where it manufactures noise. The 16 confirmed findings
consolidate into the 14 entries below. Two pairs reached the same root cause from different
addresses and are folded, each entry naming the source ids it absorbs:

- Entry 2 absorbs raw ids 4 and 18 — both the `<` dispatch at `lexicon.py:1041`, two different
  triggers for the same wrong branch.
- Entry 3 absorbs raw ids 5 and 19 — both the catch-all `expr_end = False` at `lexicon.py:1092`;
  id 19 additionally documents the silent mis-lex half, which is kept.

The folding is a synthesis decision, not a pipeline discard.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted
to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. Nothing was
lost in this run, so the zero counts here are evidence rather than a gap: the unverified set is
genuinely empty, and every lens finding reached a skeptic and was adjudicated. The finding set is
COMPLETE for the lenses that ran — which is a statement about the pipeline, not about the corpus,
and the corpus caveat is entry 15's own subject.

## The findings, severity-ranked

| # | Sev | Subject | Site |
|---|-----|---------|------|
| 1 | BLOCKER | private source published to a public remote | `tools/lexicon/ts-conformance-fixtures.json:1` |
| 2 | HIGH | `<` opens JSX where TypeScript has an operator or a type | `tools/lexicon/lexicon.py:1041` |
| 3 | HIGH | `/` after `++`/`--`/`!` lexes as a regex literal | `tools/lexicon/lexicon.py:1092` |
| 4 | HIGH | a class property's ANNOTATION is graded as the function name | `tools/lexicon/lexicon.py:1407` |
| 5 | HIGH | DEAD SNIFFER on an object literal of arrow properties | `tools/lexicon/lexicon.py:186` |
| 6 | MEDIUM | a `PATTERNS:` set id colliding with a shipped parser is silently shadowed | `tools/lexicon/lexicon.py:1495` |
| 7 | MEDIUM | the armedness predicate forked into drift-audit | `tools/drift-audit/drift_report.py:1088` |
| 8 | MEDIUM | `case X: { … }` and labeled blocks are stepped over whole | `tools/lexicon/lexicon.py:1271` |
| 9 | MEDIUM | a semicolon-free `type` alias swallows the next block | `tools/lexicon/lexicon.py:1385` |
| 10 | MEDIUM | `export default { … }` drops every function property | `tools/lexicon/lexicon.py:1277` |
| 11 | LOW | an overload signature returning an object type reads as a body | `tools/lexicon/lexicon.py:1239` |
| 12 | LOW | a bare `<` comparison in semicolon-free source eats definitions | `tools/lexicon/lexicon.py:1108` |
| 13 | LOW | a multi-line JSX attribute value is refused | `tools/lexicon/lexicon.py:984` |
| 14 | LOW | the `decorator`-selector refusal misdiagnoses its own row | `tools/lexicon/lexicon_conf.py:414` |

---

### 1 — BLOCKER · 76 KB of a private codebase lands in a public repo

**Site:** `tools/lexicon/ts-conformance-fixtures.json:1` (raw id 1)

`ts-conformance-fixtures.json` holds 115 records, 76,245 bytes of verbatim `src` drawn from 110
distinct files of `C:/projects/incms/main`, each record stamped with its source path (`from.path`)
and a 40-hex git blob sha (`from.blob`). Verified: the file is 113,837 bytes and parses to a
115-element list.

**Impact.** `git remote -v` resolves `origin` to `https://github.com/d41ly/coding-governance.git`,
and `gh repo view d41ly/coding-governance --json isPrivate,visibility` returns
`{"isPrivate":false,"visibility":"PUBLIC"}`, while `d41ly/incms` returns `PRIVATE`. Landing and
pushing this branch therefore publishes the contents and the directory map of a private codebase to
an anonymous audience — including `apps/web/app/admin/layout.tsx` (CSP-nonce injection and the
`window.__ENV` inline script), `apps/web/app/api/csp-report/route.ts`,
`apps/web/components/admin/plugins/PluginSecretSection.tsx` with its `integrations.secrets`
permission gate, `apps/web/e2e/editor/paywall.spec.ts` with its `${API_URL}/account/auth/login`
flow, and `apps/web/credentialedFetch.test.ts`.

No credential-shaped literal survives in the corpus (checked). This is source and architecture
disclosure, not a leaked secret.

**Why the recorded price is the wrong price.** `TOOL-aGradedDialect-2`'s §5 security row
(`memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md:296`) and its §8 F1
(line 397) name exactly two containments: `kit.toml`'s `project-owned` withholding, and the `rm -f`
runbook step allocated as `TOOL-aGradedDialect-5` S7. Both stop an ADOPTER from receiving the
corpus. Neither touches the remote this repo pushes to. Grepping the whole build folder for
publication language (`public`, `publicly`, `isPrivate`, `public remote`) returns nothing but an
unrelated `ts.isPrivateIdentifier` code excerpt. The unit treats disclosure as a cost to be priced,
so this is not a difference of philosophy — the dominant channel is missing from its own ledger.

This is pre-emptive, not an accomplished leak: `git ls-tree origin/main` shows the blob is not yet
on the remote. That is the useful moment to raise it.

**Fix.** Get an explicit, recorded owner decision on publishing that source BEFORE the push, and add
the publication path to the §5 security row so the containment argument names the remote as well as
the adopter. If the answer is no, keep the corpus out of the tracked tree — a gitignored local
corpus, with the conformance arm reporting a named SKIP per §7's "a skip must announce itself" —
rather than relying on `kit.toml`.

**Left-shift.** A gate leg that refuses a tracked file carrying a `from.path` outside this repo's
own tree, or more generally: a `check-foreign-source.sh` asserting that no tracked file embeds an
absolute path from another checkout root. Stage the break with a one-record fixture and confirm RED
before wiring. The cheaper documented check, if the corpus stays: a line in `WIRE-INTO-PROJECT.md`
and in the kit README stating that this repo's remote is public and that any corpus record is
published by construction.

---

### 2 — HIGH · `<` opens a JSX element where TypeScript has an operator or a type

**Site:** `tools/lexicon/lexicon.py:1041` (raw ids 4 and 18, one wrong branch, two triggers)

The `<` dispatch pushes a `jsxtag` frame whenever `jsx and not expr_end and not
check_ts_generic(src, i)`, and `check_ts_generic` decides only by what follows the name (`,` or
`extends `). Two ordinary constructs fall through to JSX:

- **A left-shift.** `check_ts_generic` returns False when the char after `<` is not an identifier
  start, so `1 << 3` opens a JSX element. Reproduced: `parse_ts_defs('const x = 1 << 3;\nfunction
  ok() {}\n', jsx=True)` raises `SyntaxError: unterminated JSX element opened at line 1`; the same
  source at `jsx=False` returns `[('ok', 2)]`. Every shift form tried refuses the whole file —
  `a << 3`, `flags | (1 << bit)`, `(h << 5) - h` (the textbook string hash), `n = n << 1`.
- **A generic function TYPE.** After `=` the tokenizer sets `expr_end = False`, so in a `.tsx`
  source both `type Mapper = <T>(x: T) => T;` and `const f: <T>(x: T) => T = (x) => x;` take the JSX
  branch and raise the same error. Both parse correctly in `.ts` mode. TypeScript's comma/extends
  tie-break exists only in EXPRESSION position; these are type positions, which is where the
  function's docstring claim to implement "TypeScript's own tie-break" breaks.

**Impact.** `scan_corpus` (line 1592) converts the raise into a `declared 'parser' but does not
parse` refusal, and `problems` sets `exit_code = 1` at line 2596. So an adopter's gate REDS on
correct source, costing the entire file rather than one construct, with a message naming a construct
that is not there. Neither case is among the six refusals `parse_ts_defs`'s header enumerates.

**Fix.** Before opening a JSX frame, require the next non-space char to be a legal tag start
(`[A-Za-z_$]`, or `>` for a fragment); `<`, `=`, `!` and a digit are operator continuations and must
emit `op '<'`. Separately, suppress JSX lexing inside a type annotation: set a flag when a `type
<name> =` header or a `:` annotation is lexed, clear it at the next depth-0 `;` or `=`. At minimum
the second case is named as a seventh declared refusal rather than left as a mystery red.

**Left-shift.** Both cases go into `test_ts_constructs` as `.tsx` fixtures — a shift expression and
a generic function type — and both must be observed RED against today's code before the fix lands
(§7: a gate whose failing case has never been seen is an assertion about nothing). The corpus
cannot substitute: its only three `<<`/`>>` hits are nested generics (`Promise<Record<string,
unknown>>`), not shifts.

---

### 3 — HIGH · `/` after `++`, `--` or `!` lexes as a regex literal

**Site:** `tools/lexicon/lexicon.py:1092` (raw ids 5 and 19)

The tokenizer's catch-all runs `i += 1; expr_end = False` for every character it does not dispatch
on, and `!`, `+` and `-` are all undispatched. A postfix `++`, `--` or a TypeScript non-null
assertion therefore leaves the lexer believing it is NOT after an expression, and the following `/`
goes to `read_regex`.

**Impact, two shapes from one defect.** Loud: `const q = i++ / 2;`, `const half = count! / 2;` and a
class method `compute(n){ return n++ / 2; }` each raise `SyntaxError: unterminated regex literal`,
refusing the whole file (`problem` → exit 1). Silent: when a second `/` sits on the same line the
read SUCCEEDS and swallows the span between — `const pct = done++ / total / 2;` tokenizes with
` total ` consumed as a regex body. The same defect is a false red on one line and a quiet mis-lex
on the next, and the second is the worse half because nothing reports it.

**Fix.** Leave `expr_end` UNCHANGED for `!` (prefix negation arrives with it already False, a
postfix assertion with it already True — both then correct), and consume `++`/`--` as a
two-character token that also leaves it unchanged. Every other catch-all character keeps clearing
it.

**Left-shift.** A `test_ts_constructs` fixture per shape: a division after `++`, after `!`, and the
two-slash line whose mis-lex is silent. The silent one needs a POSITIVE assertion — that the
definition after it is still extracted — because a mis-lex that swallows a span produces no error to
assert on. Observe all three RED first.

---

### 4 — HIGH · a class property's annotation is graded as the function name

**Site:** `tools/lexicon/lexicon.py:1407` (raw id 6)

The `const` arm at line 1392 steps over a `:` annotation with `read_ts_type_end`; the class arm
tests only `nt == "="`. So for a class property with a function-type annotation, the token sitting
before the `=` is the annotation's last word, and that word is appended as the name.

**Impact.** `class Store { private onChange: (e: Event) => void = (e) => {...} }` yields
`funcs = [('void', 2)]`. A realistic `handleClick: React.MouseEventHandler = () => {...}` yields
`('MouseEventHandler', 3)`. A FABRICATED identifier enters the graded population — P1 verb
offenders, the `.conv` cell pins, `--list` output — while the real name is never graded. `_TS_NAME`
(line 799) matches `void`, so no downstream keyword filter catches it, and no declared refusal
covers it. Any return type spelled `void`, `string` or `Promise` produces the same phantom.

**Fix.** Mirror the `const` arm: when `cur == "class"` and `nt == ":"`, step the annotation with
`read_ts_type_end(toks, k + 2, "=")` and test `check_ts_arrow` past it, appending the property name.
Guard the `nt == "="` arm so it cannot fire on a token inside an annotation.

**Left-shift.** A fixture asserting BOTH directions — that `onChange` appears and that `void` does
not. A test asserting only the first would pass today. Beyond the fixture, the durable gate is a
grader-side assertion that no extracted identifier is a TypeScript keyword or a primitive type name;
that catches the whole class rather than this instance (§7: gate the class, not the instance).

---

### 5 — HIGH · DEAD SNIFFER on an object literal of arrow properties

**Site:** `tools/lexicon/lexicon.py:186` (the `const|let|var` row of `DEFINITION_SNIFF`; raw id 15)

The row requires `=` followed by `(` or `<`, so `= {` matches nothing. `parse_ts_defs` extracts
arrow properties out of that object literal via the `cur == "object" and nt == ":" and
check_ts_arrow` branch at line 1401. Sniffer and extractor disagree — the exact DEAD SNIFFER
contradiction the widening at this block was written to prevent.

**Impact.** Reproduced end-to-end in a throwaway adopter repo: with `LANGS="ts:ts-tokens:probe
conf::dark"` and one tracked file `src/handlers.ts` containing only `export const handlers = {
readRow: () => 1, renderCell: () => 2, };`, `lexicon.py` exits 1 with `DEAD SNIFFER (the coverage
sniffer found no definition in 1 file(s) where an ARMED extractor did, e.g. src/handlers.ts)`.
Adding one top-level `export function` to the same file returns exit 0, so the object literal alone
is the red. DEAD SNIFFER is appended to `problems` with NO waiver registry — waivers exist only for
verb and suffix offender text — so an adopter cannot proceed except by disarming the language, and
the message blames the denominator while offering no repair.

The class is NEW: `_probe_defs(src, 'js-regex')` returns `[]` on the same source, so no armed
extractor found these before `ts`/`tsx` existed. Reachability is stronger than filed — the kit's own
frozen corpus holds two records of exactly this shape, `tsx-jsx-001` and `tsx-nested-001` (vi.mock
factories returning object literals of arrow properties), both of which sniff negative while
`parse_ts_defs` extracts from them. Handler maps, reducer objects and config-of-callbacks are
near-universal in a real TypeScript tree.

**Fix.** One character on that row: `=[ \t]*(?:async[ \t]*)?[(<{]`.

**Left-shift.** A `.ts` fixture carrying ONLY an object literal of arrow properties, run through the
sniffer/extractor agreement arm and observed RED first — this row has never been seen red. The
stronger gate, if it is cheap: assert sniffer/extractor agreement across every record in the frozen
corpus, which would have caught this on the two records already in it.

---

### 6 — MEDIUM · a `PATTERNS:` set id colliding with a shipped parser is silently shadowed

**Site:** `tools/lexicon/lexicon.py:1495` (raw id 2)

`resolve_extractor` tests `pset in PARSERS` before the resolved pattern sets, unconditionally. So a
`PATTERNS:` row whose set id collides with a shipped parser id (`python-ast`, `shell-tokens`,
`ts-tokens`, `tsx-tokens`) is parsed, merged into `sets`, printed as a declared extractor row — and
never run.

**Impact.** Verified in-tree: with `sets = resolve_pattern_sets({'PATTERNS': {'ts-tokens.functions':
<rx>}})`, `sets` holds `['js-regex', 'ts-tokens']` yet `resolve_extractor('probe', 'ts-tokens',
sets)` returns `parse_ts_defs`. An adopter arming or repairing TypeScript extraction with
`LANGS="ts:ts-tokens:probe"` plus a `PATTERNS: ts-tokens.functions=…` row is graded by the shipped
tokenizer instead, while the run prints `lexicon: PATTERNS — 1 declared extractor row(s):
ts-tokens.functions` and says nothing about the shadowing: the override warning at line 2695
computes `over` against `PATTERN_SETS`, which holds only `js-regex`, so it cannot see a
`PARSERS` collision. The declaration and the reading disagree inside one run.

The colliding-id case on a foreign extension is worse in a different direction:
`resolve_extractor('probe', 'python-ast', sets)` returns `_python_defs`, and
`extract_text('fn foo() {}', 'probe', 'python-ast')` raises `SyntaxError` — a true refusal under a
false reason. Nothing refuses the collision: `lexicon_conf.py`'s PATTERNS validation (309-330)
checks key shape, part name, compilability and group count only, and its LANGS validation (line 453)
accepts `probe` for any set id with no reserved-name check. `README.md`'s PATTERNS section states
outright that a declared set is walked exactly as a shipped one, so this contradicts a written
contract. `scan_corpus`'s comment ("a `PATTERNS:` row cannot declare a parser") states the design
assumption; nothing enforces it.

**Fix.** Make the collision a refusal, not a silent precedence: raise `ConfError` in
`lexicon_conf.py`'s `_parse_patterns` (or in `resolve_pattern_sets`) when a row's pattern-set id is
a key of `PARSERS`, naming the shipped parser and the fact that a regex row cannot replace one.
Widen the guard at line 2695 to `k.split('.')[0] in (PATTERN_SETS.keys() | PARSERS.keys())` so a
shadowed row can never be printed as live.

**Left-shift.** A `selftest.py` arm per half: a conf declaring `PATTERNS: ts-tokens.functions=…` must
raise `ConfError`, and the printed declared-row line must never name a set that `resolve_extractor`
will not use. The second arm is the one that generalises — it asserts the declaration and the
reading agree, which is the class.

---

### 7 — MEDIUM · the armedness predicate forked into drift-audit

**Site:** `tools/drift-audit/drift_report.py:1088` (raw id 12)

The armedness predicate was consolidated into `lexicon.resolve_extractor` at four sites inside the
lexicon kit. The fifth site — `_build_armed_exts` in the drift-audit kit — still spells the
pre-consolidation rule inline (`mode == "probe" and pset not in sets`) and consults `lex.PARSERS`
only on the `parser` arm.

**Impact.** Reproduced in-process: for `LANGS="ts:ts-tokens:probe tsx:tsx-tokens:parser
py:python-ast:parser"`, `lex.resolve_extractor` arms all three while `_build_armed_exts` returns
only `{tsx, py}` — `ts` is dropped because `ts-tokens` is not in `PATTERN_SETS`. That pairing is not
hypothetical: `resolve_extractor`'s own header blesses probe-with-a-parser-id as the shape a
below-floor tokenizer ships as, `read_ts_mode` returns exactly `"probe"` when the conformance floor
is missed, and the kit's `read_ts_readers` selftest scores the TypeScript reader as
`("ts-tokens", "probe")`. Both consumers — `signal_lexicon_verbs_unused` (gateable, whose `live`
flag is `bool(used)` over this same narrowed population) and
`build_lexicon_marginal_offense_rate` — then report a clean number over a corpus narrower than the
lexicon gate actually grades. That is the green-by-absence class `_resolve_lexicon_sets`'s docstring
says it was written to close, and the very defect `_build_armed_exts`'s own docstring names: "the
two readers of one declaration disagreed".

**Fix.** Replace both drops with the one predicate: `if lex.resolve_extractor(mode, pset, sets) is
None: continue`, keeping a `getattr(lex, 'resolve_extractor', None)` fallback if drift-audit must
tolerate an older copy-installed lexicon. Delete the now-redundant `mode == "parser" and pset not in
lex.PARSERS` arm, and correct the docstring's "`lex.PARSERS` IS READ, NEVER RESTATED" paragraph to
say the PREDICATE is read — that is the carrier which just forked.

**Left-shift.** A drift-audit arm that feeds one LANGS string to both readers and asserts the armed
sets are equal. That is the gate the class needs; a fixture asserting only today's answer would fork
again on the next widening.

---

### 8 — MEDIUM · `case X: { … }` and labeled blocks are stepped over whole

**Site:** `tools/lexicon/lexicon.py:1271` (raw id 7)

`read_ts_block_kind` maps any `{` whose previous token is an op `:` to `"type"`, so a braced case
clause, a labeled block and a ternary's object arm are all classified as a type and stepped over by
`read_ts_brace_end` at line 1344. The `case`/`return` word arm at line 1277 catches only a brace
directly after the keyword, not the ordinary `case X: {` form.

**Impact.** Silent recall loss. Reproduced: an `outerFn` whose switch carries `case 1: { const inner
= () => 1; function alsoInner() {} }` returns only `[('outerFn', 1)]` — both inner definitions
dropped; `outer: { const b = () => 2 }` returns `[]`; `flag ? { f: () => 1 } : { g: () => 2 }`
returns `[]`. Braced case clauses are ordinary TypeScript, and this is loss under a `parser`
standing, which — unlike `probe` — does not report its own incompleteness. Not one of the six
declared refusals.

**Fix.** Distinguish the two meanings of `:` — track a `case`/`default` word and a statement-start
label in `parse_ts_defs` so the `{` after their `:` classifies as `statement`, and classify a `{`
after a ternary `:` as `object`. Keep `"type"` only for a `:` that follows a declarator name.

**Left-shift.** A fixture per shape in `test_ts_constructs` asserting the inner definitions ARE
found. Silent-drop classes need positive assertions; there is no exception to catch.

---

### 9 — MEDIUM · a semicolon-free `type` alias swallows the next block

**Site:** `tools/lexicon/lexicon.py:1385` (raw id 16)

The `type` branch sets `pend = "type"`, and `pend` is cleared only by a `;` or by consuming the next
`{`. A `}`, a newline or any word token leaves it armed, so an alias with no trailing semicolon and
no braces in its RHS arms the NEXT block as a type and `read_ts_brace_end` (line 1146) swallows it
whole.

**Impact.** Measured: `type Id = string` followed by `export function make() { const helper = () =>
1; return helper }` returns `[('make', 2)]` — `helper` is gone; adding a `;` after the alias returns
`[('make', 2), ('helper', 3)]`. `type Id = string` followed by `export const api = { readRow: () =>
1, }` returns zero funcs. Names inside the swallowed block are never graded, so the P1/P2 verdicts
green by absence, and no DEAD SNIFFER fires because the alias line itself sniffs positive. The loss
is silent, and `prettier --no-semi` / standard style is mainstream. The frozen corpus genuinely
cannot see it: all 8 type-alias records terminate their alias with a `;` or an opening brace, and
`TS_SENTINEL` is fully semicoloned — the floor was measured on a fully-semicoloned population.

**Fix.** Clear `pend` when the walk reaches a statement-starting word (`function const let var class
interface enum type export import return`) before the `{` arrives — one guard at the top of the word
dispatch — or consume the alias outright with a depth-0 walk instead of arming `pend`.

**Left-shift.** A semicolon-free fixture in `test_ts_constructs`. Given entries 9 and 12 are both
semicolon-free classes, the better gate is a corpus-wide arm: run a de-semicoloned copy of the
frozen fixtures and assert the extracted name set is unchanged. That catches the class, and it is
cheap because the corpus already exists.

---

### 10 — MEDIUM · `export default { … }` drops every function property

**Site:** `tools/lexicon/lexicon.py:1277` (raw id 17)

`read_ts_block_kind` routes prev-word `return` and `case` to `object` and everything else to
`statement`. The word before the `{` of `export default {` is `default`, so the block opens as a
statement and `parse_ts_defs`'s `cur in ("object", "class")` arm never runs.

**Impact.** Measured: `export default { readRow: () => 1, writeRow(x: number) { return x; }, };`
returns `([], [], [])`, while the byte-identical `const o = { … }` returns `[('readRow', 2),
('writeRow', 3)]`. Silent under-grade, not a refusal, so the gate greens on names it should judge.
`export default {…}` is the ordinary shape for Vue options objects, route and handler maps and mock
modules. `grep 'export default {' ts-conformance-fixtures.json` is 0 hits, so neither the frozen
corpus nor `TS_SENTINEL` covers it, and it is not enumerated in `parse_ts_defs`'s header.

**Fix.** Add `"default"` to the `("return", "case")` tuple on that line.

**Left-shift.** An `export default { … }` case in `test_ts_constructs` with a positive definition
inside it, observed RED first.

---

### 11 — LOW · an overload signature returning an object type reads as a body

**Site:** `tools/lexicon/lexicon.py:1239` (raw id 9)

`check_ts_body` returns True at the first depth-0 `{` after the parameter list. A `:`-introduced
object type literal opens exactly such a `{`, so the terminating `;` is never reached and the
signature is counted as a definition — contradicting documented refusal 3 in `parse_ts_defs`, which
says an overload signature is not one. Two claims in one file disagree, and the overload wins the
wrong way.

**Impact.** Reproduced: `function f(a: string): { a: string };` twice plus one implementation yields
`[('f', 2), ('f', 3), ('f', 4)]` where the oracle counts one; the plain-return-type control
(`function g(a: string): string;` twice plus impl) correctly yields `[('g', 4)]`. Three graded
records for one definition site, inflating the definition population and any offender count `f`
contributes to. Discriminated-result overloads (`function parse(s): { ok: true; value: T };`) are
ordinary TypeScript.

**Fix.** When the depth-0 `{` follows a `:` return-type annotation, step it with
`read_ts_brace_end` and keep scanning: only a `{` reached after the annotation is the body, and a
`;` first is the overload refusal.

**Left-shift.** Add the object-type overload to the existing overload fixture in
`test_ts_refusals` — the plain-return-type case is already covered, so this is one more arm on a
gate that exists rather than a new one.

---

### 12 — LOW · a bare `<` comparison in semicolon-free source eats definitions

**Site:** `tools/lexicon/lexicon.py:1108` (raw id 8)

`read_ts_angle_end` abandons a candidate generic run only on a depth-0 `;` or an unbalanced closer,
so in semicolon-free source a comparison `<` matches an unrelated later `>` and `parse_ts_defs`
skips every token between (capped at 400).

**Impact.** Reproduced: `const small = a < b` / `const later = () => 1` / `const big = c > d`
returns `[]` — `later` is silently lost; the identical source with semicolons returns
`[('later', 2)]`. Narrower than the rest — it needs a bare unparenthesised `<` comparison plus a
later balanced-depth `>` with no intervening unbalanced closer, and a parenthesised comparison
correctly returns None — but semicolon-free formatting is mainstream, the loss is silent, and the
docstring's own claimed protection is exactly the one that fails. Low as filed.

**Fix.** Also return None from the walk on a token that cannot appear in a type-argument list — the
words `const let var function class return` and the ops `=` and `=>`.

**Left-shift.** Covered by the de-semicoloned-corpus arm proposed in entry 9; add this shape as its
named fixture so the arm has a known red.

---

### 13 — LOW · a multi-line JSX attribute value is refused

**Site:** `tools/lexicon/lexicon.py:984` (raw id 11)

`read_string` breaks on `\n` and raises, and the `jsxtag` state calls it for attribute values.
Break-on-newline is correct for an ECMAScript string literal and wrong for JSX: the grammar defines
`JSXDoubleStringCharacters` as any source character but `"`, and TypeScript's own scanner passes a
`jsxAttributeString` flag precisely to skip its line-break error.

**Impact.** Reproduced: a component containing `<button aria-label="save the\n  current draft" />`
raises `SyntaxError: unterminated " string opened at line 4` and the file is refused as unparseable.
A wrapped attribute value is valid TSX that both `tsc` and Babel accept, and `scan_corpus` turns the
raise into a named refusal that reds the run.

**Fix.** Pass a flag (or use a separate reader) so the `jsxtag` call permits newlines inside the
quoted value and refuses only at EOF.

**Left-shift.** A `.tsx` fixture with a wrapped attribute value in `test_ts_constructs`, observed
RED first.

---

### 14 — LOW · the `decorator`-selector refusal misdiagnoses its own row

**Site:** `tools/lexicon/lexicon_conf.py:414` (raw id 14)

The refusal keys on the MODE token (`declared[ext] != "parser"`) while the reader it protects,
`extract_decorators` (`lexicon.py:1832`), keys on the PATTERN SET
(`(declared.get(ext) or ("", "dark"))[0] != "python-ast"`). After `resolve_extractor` moved reader
selection to the pattern-set id, those two disagree.

**Impact.** Reproduced: a conf declaring `LANGS="py:python-ast:probe"` plus `py.function+decorator:
route` raises `ConfError` saying "a 'probe' language would route an EMPTY subset and grade nothing"
— while in the same interpreter `resolve_extractor("probe", "python-ast")` returns `_python_defs`
and `extract_text` returns a real AST reading of a decorated def. The refused row DOES get a real
parse and its decorators WOULD be read, so the stated cause is false for exactly that row, and a
refusal whose stated cause misdiagnoses the configuration sends the adopter to change the wrong
thing. `extract_decorators`'s docstring compounds it, still claiming the non-parser modes "are
refused earlier and by name, in `lexicon_conf.check_declaration`", which the widening made stale.
Low: it needs a hand-written `python-ast` under `probe`, which the scaffold does not emit — but that
is precisely the shape `read_ts_readers` and `TS_CONF` use deliberately, and the S4 comment at
`selftest.py:696` declares it correct.

**Fix.** Key the refusal on the same fact the reader keys on — refuse when the row's pattern-set id
is not one that yields decorators (today: `pset != "python-ast"`) — and reword the message to name
the pattern set rather than the mode. One line, and it removes the last mode-keyed capability test
in the kit.

**Left-shift.** A `selftest.py` arm asserting that `check_declaration` accepts a `+decorator:` cell
on exactly the rows `extract_decorators` will read from — one predicate, both sides. Same shape as
entry 7's gate, and for the same reason.

---

## What held

- `TOOL-aGradedDialect-1`'s mechanism fork (hand-written tokenizer over a compiler dependency) drew
  no finding that survived a skeptic, for the fourth round running.
- The `.ts` / `.tsx` split into two parser entries, the earned-mode rule, and `read_ts_mode`'s
  demotion to `probe` below the conformance floor are all sound and are what makes entries 8, 9, 10
  and 12 reportable at all — they name a `parser` standing that promises more than it delivers.
- The `resolve_extractor` consolidation is right; entries 6, 7 and 14 are its unfinished edges, not
  arguments against it.
- No credential-shaped literal in the corpus, no injection surface, no new egress path, no
  authorization surface touched. Entry 1 is the whole security story and it is a disclosure
  decision, not a vulnerability.

## The corpus caveat, because it explains eleven of the fourteen

The conformance corpus is a good instrument aimed at one question — does the reader agree with
`tsc` on THIS sample — and eight of these findings are classes the sample does not contain: no shift
operators (only nested generics), no division after a postfix operator, no `export default {`, no
semicolon-free file, no multi-line attribute value, no object-type overload. `TOOL-aGradedDialect-2`
F1 demands exact agreement with the frozen corpus, and it gets it; that is not coverage of
TypeScript, it is coverage of one private codebase's dialect on one day. Two consequences worth
recording:

1. Adding the fixtures named above matters more than raising the floor percentage. A floor measured
   over a sample that lacks a construct cannot be raised into covering it.
2. `test_ts_constructs` — hand-written, adversarial, cheap — is the instrument for these, and it is
   where every left-shift above lands. Nine of the fourteen entries resolve to fixtures in that one
   function.

## Landing recommendation

Entry 1 first, and it is an owner question, not a patch: publish or do not publish. Nothing else
should be pushed until it is answered, because pushing anything on this branch answers it by
default.

Entries 2 through 5 are HIGH and all four are one afternoon in one file: two lexer state bugs, one
missed annotation arm, one regex character. Each needs its failing fixture observed RED before its
fix lands. Entries 6 through 14 are a follow-up unit; none of them blocks a landing, and entry 7 is
the only one outside `tools/lexicon/`.
