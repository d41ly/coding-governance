**Serves:** diff-review TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-5 TOOL-aLexedStripper-6

# Closing diff review — the `aLexedStripper` landing, both scanners

*Node a, 2026-08-30, round 1. Tier-2 closing review of the four units as they actually landed, not as
they were specced. Priming: both scanners' own headers, the four specs under
`memory/builds/aLexedStripper/spec/`, and the two prior spec-audit rounds under `reviews/` — whose
confirmed-and-folded findings are NOT re-reported here. Every finding below was reproduced against
the wired hook or the installed module before it was written down.*

Reviewed range: `19d9b328c26ca41d9d275ef43abfa76f7efbef20...HEAD` (HEAD = `eb76532e`, the single
product commit `feat(codebase-map,agent-cap): both scanners stop reading prose as code`).

Round 1.

## Verdict: BLOCKED

Two blockers, both in `tools/hooks/agent-cap.js`, both fail-open, both measured end to end as a
DENY at BASE becoming an ADMIT at HEAD on legal JavaScript. `agent-cap` is the only mechanical
control against an unbounded verify-stage agent burst, the file is `role = engine` in
`tools/hooks/kit.toml`, and `.claude/hooks/agent-cap.js` is byte-identical (`diff -q` clean) — so the
live `PreToolUse` guard in this tree has the hole today and every adopting tree takes it on the next
re-pull. Neither blocker is theoretical: each is triggered by an ordinary regex literal or a single
apostrophe.

Both blockers live in `renderCodeView`, the function `TOOL-aLexedStripper-2` added and
`TOOL-aLexedStripper-5` bounded. The `-5` fallback is real and works for the class it was written
for (an unterminated template), but it reads a signal — `unterminated: stack.length > 0` — that two
of the four code-mode branches structurally cannot raise. The safety argument in `-5` ("the verdict
IS the shipped guard's verdict") holds only for the template class; block mode and an unpaired quote
were never enumerated.

The `codebase-map` half is not blocking. Its three findings are index-precision defects in a
subsystem that feeds a ranking and a WARN, never a gate.

## Review shape

- raw 17 · confirmed 11 · refuted 6 · unverified 0 · precision 0.65
- confirmed by severity, as adjudicated here: 2 BLOCKER · 1 HIGH · 2 MEDIUM · 2 LOW
- confirmed blockers: 2

The 11 confirmed filings are presented as **7 rows**. Three merges, because the same defect was
filed from more than one lens and double-listing would overstate how many distinct things are wrong:
ids 1+9+13 are one defect, ids 4+14 are one defect, ids 2+15 are one defect. Both filing ids appear
on each row.

Two severities moved from their filings, and both moves are stated on the row:

- Filing 4 was MEDIUM/HIGH and is adjudicated **BLOCKER**. It is the same measured fail-open as
  filing 14 on the same control, reachable with one apostrophe inside a regex literal.
- Filing 16 was MEDIUM and is adjudicated **HIGH**. Two independent charter rules are broken in a
  shipped engine file, and the foreign-corpus measurement is far worse than the filing estimated
  (0.858 precision against a 0.95 floor).

Precision 0.65 against 0.28 and 0.29 in the two spec-audit rounds. The difference is the target, not
the priming: a landed diff can be executed, and every row below carries a measurement rather than an
argument.

## Confirmed findings

### BLOCKER — 2

---

#### 1. `tools/hooks/agent-cap.js:300` (with `:334`) — block-comment mode is invisible to the fallback, so a regex literal containing `/*` blanks the rest of the script and rule 2 sees no fan-out

*(filings 1, 9, 13 — one defect)*

`renderCodeView` enters block mode on any `/*` byte pair (`:300`) and sets `mode` only; it pushes
nothing onto `stack`. `:334` returns `unterminated: stack.length > 0`. `mode` is declared outside the
per-line loop (`:289`), so block mode persists across lines. A scan that ends in — or merely passes
through — block mode therefore reports `unterminated: false`, `fanoutFindings:343` keeps the blanked
view instead of falling back to the per-line `stripStrings` view, and every line from the `/*` to the
next `*/` or EOF renders empty. The function models no regex literal, which its own comment at
`:277` and the dossier both state, so a regex literal is the ordinary way to reach this.

**Measured**, same `Workflow` payload, BASE `19d9b328` vs HEAD, all legal JavaScript (verified under
`node` / `vm.Script`):

| fixture above an unbounded fan | BASE | HEAD |
|---|---|---|
| `const STRIP = /[/*]+/g` | exit 2 | exit 0 |
| `const OPENER = /\/*/` | exit 2 | exit 0 |
| `const re = /https:\/\/*/` | exit 2 | exit 0 |
| `const re = /a\/*/` plus an ordinary `/* … */` later in the file | exit 2 | exit 0 |
| `const parts = f.file.split(/[/*]+/)` above `all.map((f) => () => agent(f))` | exit 2 | exit 0 |

The fan in each case is the realistic one — `allFindings.map((f) => () => agent(skepticPrompt(f)))`,
or `for (const f of all) out.push(await agent(...))` — i.e. one agent per finding, the ~40-agent
burst and tripped server rate limiter the hook exists to prevent. Control test rules out a corrected
false positive: the identical fan with the construct removed still exits 2 on HEAD, so the ADMIT is
caused solely by the parse bug. Regression, not pre-existing: the parent of `b65ecd42` exits 2 on the
same fixture.

**Fix.** Delete the block branch from `renderCodeView` — the `if (two === '/*') …` at `:300` and its
`else` arm at `:331` — so `/*` stays ordinary characters exactly as the shipped per-line view treated
it. Verified: restores exit 2 on every fixture above, leaves the new rule-2 arms at their expected
exits, and the suite still reports 96 passed / 0 failed.

Do **not** ship the smaller-looking repair. `unterminated: stack.length > 0 || mode !== 'code'`
closes the first three rows and leaves row four open — measured — because a spuriously opened block
that a later *ordinary* comment closes ends the scan in code mode with an empty stack, having blanked
only the region containing the fan. No flag can see that case even in principle. Pushing `'block'`
onto the stack has the same hole. Either delete the branch, or model regex literals; nothing
in between is safe.

Mirror into `.claude/hooks/agent-cap.js` and re-run the parity arm. The file header at `:47-48`
still says block comments are not stripped — true for rule 1, false for rule 2 today, and true again
once the branch is deleted.

**Left-shift gate.** Two arms in `tools/hooks/agent-cap.test.sh`, both staged RED against the tip
first: a fan below `const SEP = /[/*]+/g`, and the closed-block case `const re = /a\/*/` with an
ordinary `/* … */` later in the same script. Instance arms certify nothing about the class, so add
one structural arm beside them: grep the body of `renderCodeView` and red if it contains `'/*'` at
all. That pins the deletion against the next well-meaning re-addition, costs one line, and cannot
drift. The existing group tests only the backtick half of the modelled-no-regex class.

---

#### 2. `tools/hooks/agent-cap.js:302-309` — an unpaired quote in code position swallows the rest of its line, and does not raise the flag either

*(filings 4, 14 — one defect; filing 4 promoted from HIGH)*

On a `'` or `"` in code mode the walk runs `while (i < raw.length && raw[i] !== q) …`. With no
partner on that line it simply exits at end-of-line, `:307` then appends a synthetic closing quote,
and the view claims a balanced empty string the source does not have. Everything after the quote on
that line is gone. `stack` is untouched and `mode` stays `code`, so `unterminated` is false and the
`-5` fallback is skipped. `stripStrings`, which rule 2 read before this diff, left such a line intact
because its regexes require a matching quote.

**Measured**, BASE exit 2 / HEAD exit 0, both legal JavaScript, both an unbounded fan on the same
line as the quote:

- `const q = text.split(/['"]/) ; await Promise.all(all.map((x) => agent(x)))`
- `if (/won't/.test(args.s)) await Promise.all(all.map((f) => agent(f.p)))`

Probed directly, the second renders as `  if (/won''` — the entire fan-out erased. The control
fan-out without the apostrophe still exits 2 on HEAD.

This is **not** closed by finding 1's fix. The swallow completes within a single line and leaves
`mode === 'code'`, so neither deleting the block branch nor any `mode !== 'code'` test touches it.

**Fix.** Treat a quote as a string opener only when its partner is found on the same line; on
reaching end-of-line without one, emit the remainder of the line verbatim — the `stripStrings`
behaviour rule 2 was calibrated against. Leaving the quote characters in the view is harmless: rule 2
counts `agent(` calls and receiver shapes. A `broke` flag OR-ed into `unterminated` also restores
exit 2 on the fixture (measured) and is the belt-and-braces alternative, but it discards the whole
improved view for one odd quote, which is the precision the diff exists to buy.

**Left-shift gate.** Two arms: `/['"]/` and `/won't/`, each paired with a fan on the same line,
asserted exit 2 and staged RED first. Plus one structural arm: feed `renderCodeView` a single line
holding an unpaired quote followed by known text, and assert the rendered line still contains that
text. That gates the class — the dropped-tail — rather than the two spellings.

---

### HIGH — 1

---

#### 3. `tools/codebase-map/selftest.py:1169` and `:1176-1182` — the corpus arm guards on git-ness, not on this-repo-ness, and both skip paths print a green `ok` row

*(filing 16, promoted from MEDIUM)*

The docstring says the arm is "SKIPPED, loudly, outside a git checkout of this repo". The guard is a
`try/except (OSError, CalledProcessError)` around `git ls-files`, which succeeds in *any* git
checkout. `repo_root()` resolves from the installed kit directory, so in an adopter's tree it is the
adopter's root. With ≥1000 ground-truth NAME tokens the arm then asserts this repo's 0.99 / 0.95
floors against the adopter's own corpus.

**Measured.** This repo reproduces exactly: recall 1.0000, precision 0.9810 — 3.1 points of margin.
The same computation over a foreign corpus (CPython 3.14 stdlib, 400 files, 41 661 ground-truth NAME
tokens): recall 1.0000, precision **0.8579** — RED, 9.2 points below the floor. The top false tokens
there are numeric and escape fragments (`x0010`, `x0002`, `f`, `b`, `r`), confirming the floors are
corpus-derived and do not generalise. The adopter's only remedy is editing a shipped engine file.

Second, independent half: both skip paths (`:1182` not-a-git-checkout, `:1206` too-few-tokens)
`return` normally, so `check()` at `:52-59` prints `ok   {name}` and the tally reads PASS. The
printed "NOT a pass." line is the only signal, in the arm whose own docstring cites the
green-by-absence class. §7's "a skip must announce itself" is broken by the code that quotes it.

**Correction to the filing.** The leg is `subject = "kit"`, and `tools/run-gates/run-gates.sh:944-948`
HOLDS every `subject = kit` or `chunk = selftests` leg unless `GATE_SELFTESTS=1`. This is therefore
not an adopter's default bar. It remains reachable through the kit's own declared argv
(`python3 {kit}/selftest.py`) and through the `GATE_SELFTESTS` run AGENTS.md says a DoD owes for kit
work.

**Fix.** Gate the arm on a marker only this tree has — `memory/map/features/` beside
`tools/codebase-map/map_lib.py` — and skip loudly otherwise. Alternatively keep the measurement
everywhere and downgrade it to a printed WARN when the corpus is not this repo's, so an adopter sees
the number without inheriting the floor.

**Left-shift gate.** Give `check()` a third row shape: an arm returns a sentinel (`"skip"`) and
`check()` prints `skip {name}` and counts it in a skipped tally, so no skip can ever print `ok`.
Then one self-test arm asserting a deliberately-skipping arm produces no `ok` row. That closes the
class for all three loudly-skipping arms in the file, not just this one.

---

### MEDIUM — 2

---

#### 4. `memory/map/features/agent-cap.md:168` and `tools/hooks/agent-cap.js:284-286` — the residual is documented as "precision, not safety" in two places, and it is safety, in both

*(filings 2, 15 — one defect)*

The dossier bullet at `:163-169` correctly enumerates the code-mode branch set — `//`, `/*`, a
backtick, the two quote characters — then states the load-bearing sentence: *"The residual is
precision, not safety: such a script is judged at the old view's accuracy."* Its stated mechanism
("opens template mode and never closes" → unterminated → falls back) is the right model for the
backtick and the wrong model for the other two. `/*` and an unpaired quote raise no flag, reach no
fallback, and cost a DENY. Six fixtures in findings 1 and 2 show HEAD admitting what BASE denied.
The hook's own header at `:284-286` says the same wrong thing, so both copies of the answer are
wrong — the repo's two-answers-to-one-question class, with no third copy to arbitrate.

This is the durable record an adopter and the next reviewer read when deciding whether
`renderCodeView` needs a regex model. It currently tells them the known blind spot cannot move a
verdict, which is measurably false, and it is not repaired by the code fixes above.

**Fix.** After findings 1 and 2 land, rewrite the bullet to what is then true: the view models no
regex literal; an unterminated template routes the script to the per-line fallback, which returns the
shipped hook's own verdict; `/*` is deliberately not a branch so a regex-borne one cannot blank code;
an unpaired quote leaves its line intact. Name the three constructs, not just the backtick.

**Left-shift gate.** Do not gate the pair — delete one copy. The hook header should point at
`memory/map/features/agent-cap.md` for the residual instead of restating it, which is §6's own rule
and removes the thing that drifts. If the restatement stays,
`tools/check-agent-cap-restatement.sh` is the existing home for a byte-comparison between the two.

---

#### 5. `tools/codebase-map/map_lib.py:703-722` — the interpolation body scan is bounded by EOF, not by the string's own closing delimiter, so one `{` inside a nested quote swallows the rest of the file into the index

*(filing 11)*

The inner `while k < n` walk counts any bare `{` as nesting, including one inside a quote *within*
the replacement field, so the field's real `}` is consumed and the scan runs to EOF. Line 721's
`j = k + 1 if k < n else k` then sets `j = n`, so the pass ends rather than resuming — the abandon
rule the function's own docstring promises ("the pass resuming just after the opener") never fires,
because the body text was already appended.

**Measured.** `_identifier_tokens('BRACE = f"{\'{\'}"\n# a comment whose PROSE must never reach the
index\ndef alpha():\n    return "a string whose CONTENT must never reach the index"\n', '.py')`
returns `PROSE`, `CONTENT`, `comment`, `whose`, `never`, `reach`, `index`. Same in JS:
`` const s = `${ fn('{') }` `` leaks the next line's comment prose, and so does the realistic
spelling `` `${ name.replace('{', '') }` ``. Reachable on ordinary code — any `.replace('{', …)`,
`.split('{')` or `'{'` inside a template interpolation.

This is the swallow-the-rest-of-the-file class the rewrite exists to remove, arriving in the
over-capture direction. It stays MEDIUM because the index feeds a fan-in ranking and a WARN, never a
gate, and nothing in this repo's own corpus trips it today (measured: zero comment-only tokens leak
from this cause in the 46-file Python corpus).

**Fix.** Bound the inner walk by the string's own delimiter — stop when it reaches an unescaped
`delim` at depth 0, since the field cannot outlive its string — skip quoted spans when counting
`depth`, and on failing to find `interp[1]` abandon properly: emit nothing and set
`j = j + len(interp[0])`.

**Left-shift gate.** Add the `f"{'{'}"` fixture to the `test_identifier_tokens_per_language` case
table with the following line's comment word in the `absent` column, and a `` `${ fn('{') }` ``
fixture for the C profile. That negative column is exactly the direction this defect arrives in and
it already exists.

---

### LOW — 2

---

#### 6. `tools/codebase-map/map_lib.py:745-751` — the Python string-prefix backscan runs for every profile, so a C-profile string can turn on replacement-field parsing

*(filing 6)*

The `_PY_PREFIX_CHARS` walk happens before the profile is consulted. Any identifier ending in
`r/b/u/f` immediately before a double quote sets `fstring`, and since `_PROFILE_C` carries
`interp = ("${", "}")` the field parser turns on inside a plain JS/TS string literal, whose
double-quoted strings never interpolate. `_PROFILE_SH` has `interp = None` and is unaffected.

**Measured, both directions, on valid TypeScript.** Over-capture:
`_identifier_tokens('const t = typeof"${leak}"\nconst z = 1\n', '.ts')` returns
`['const','leak','t','typeof','z']`. Under-capture, which is the direction the rewrite exists to
remove: `'const t = typeof"${x" }; const alive = 1; const s = "y";\nconst nextline = 2\n'` returns
`['const','nextline','t','typeof','x','y']` — `alive` and `s` swallowed as string content.

LOW because reachability is genuinely poor: it needs a prefix-letter identifier glued to a double
quote with no space (`typeof"…"`, `for (c of"abc")`), which is legal and rare.

**Fix.** One `if triple:` around lines 745-751 — the backscan belongs to the row that owns it.

**Left-shift gate.** A `.ts` fixture `typeof"${leak}"` in the per-language case table with `leak` in
the `absent` column, and its under-capture twin asserting `alive` is present.

---

#### 7. `tools/codebase-map/map_lib.py:631-632` — `_LINE_COMMENT_RE` and `_STRING_RE` lost their only reader and are now dead module state

*(filing 12)*

`git grep` over the whole tree finds no consumer of either outside their own definitions — only a
stale `__pycache__` blob and the spec prose naming them as the things being replaced.
`_BLOCK_COMMENT_RE` at `:400` is genuinely live (the JS extractors at `:461` and `:539`), so the
three read as one live set: a later edit reaches for the wrong one, or re-wires a still-compiled
regex and quietly restores the language-blind chain this diff deleted.

**Fix.** Delete lines 631-632. Keep `_BLOCK_COMMENT_RE` and `_IDENT_TOKEN_RE`, both of which have
callers.

**Left-shift gate.** Cheap and general: extend the `drift-audit` dead-symbol probe to module-level
`_*_RE` constants with no readers outside their own assignment. The class — a compiled regex left
behind by a rewrite — is exactly what that audit is for, and this is its first instance.

---

## Checked and clean

Named in the review brief, exercised, nothing found. Stated so a green here is not confused with an
unexamined area.

- **The four `agent-cap` version carriers agree.** `grep -rn "gov:kit agent-cap@" tools/hooks/
  .claude/hooks/` returns four rows, all `1.9`; `tools/hooks/agent-cap.js:52` carries
  `KIT_AGENT_CAP_VERSION = '1.9'` on the same line as its marker; `bash tools/check-kit-versions.sh`
  exits 0; `diff -q tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` is clean. The kit did move
  1.8 → 1.9 for this behavioural change, which is the contract signal an adopter re-pulls on. (The
  standing limitation recorded by `dTieredTribunal` still applies and is not re-filed: that gate
  grades consistency, never movement.)
- **The seven-field profile against real shell and TypeScript in this repo.** Spot-checked the
  constructs the field set was added for: `$#` and `${path#/opt/}` no longer truncate a shell line
  (`marker_needs_word_start`); `#` inside a shell double-quoted string does not open a comment;
  `//` inside a TypeScript string literal does not open one either; a `${ fn(x) }` body is indexed as
  code while the surrounding template text is not. All four behave as specced. The two profile
  defects that do exist are findings 5 and 6, both in the interpolation machinery rather than in the
  field set.
- **Both spec-audit rounds' confirmed findings.** Re-read and not re-reported. Round 2's two blockers
  are genuinely closed by `TOOL-aLexedStripper-5` and `-6` as landed: the S3 unconditional DENY is
  gone (the fallback is real, and it does return the shipped verdict for the template class it
  covers), and the seventh profile field exists with Python's row gated on the `f` prefix. Finding 1
  above is not a re-filing of round 2's S3 blocker — it is the branch that fallback cannot observe.

## What the two blockers say about the unit that introduced the fallback

`TOOL-aLexedStripper-5` is the right shape and reads the wrong signal. Its safety argument is sound
for the class it enumerated and silently empty for the two it did not, and nothing in its acceptance
set could have noticed, because every arm exercises a construct the author already had in mind. The
suite has ~86 arms and not one of them ends a scan outside code mode: its only `/*` (line 816) sits
inside a block comment terminated on the same line.

That is the repo's own could-not-fail class, one level up from where §7 usually catches it — not a
gate satisfied by its own comment prose, but a *fallback* whose trigger condition was never observed
firing on anything but the fixture it was written for. The structural arms suggested on findings 1
and 2 are the cheap answer: pin the branch set itself, so the next construct someone adds to
`renderCodeView` has to argue with a test rather than with a comment.
