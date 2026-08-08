# Review 3 — Tier-2 pass over the landed diff (aDrainedSluice V1-V9 + aBatchedTribunal W1-W2)

**Scope:** `76fcd09..HEAD` — the nine aDrainedSluice units that drained the TOOL backlog, and the
two aBatchedTribunal units that ported inCMS's review protocol into a gate.

**Review shape:** raw **28**, confirmed **28**, refuted **0**, unverified **0**, precision **1.00**.
Every finding was reproduced by RUNNING something — the hook against a planted fixture, the gate
against a mutated tree, a predicate called directly on a synthesised state. Nothing here rests on
reading alone.

**Deduplicated:** the 28 raw findings collapse to **18 distinct defects** (several reviewers hit the
same code site independently — that convergence is signal, not noise, and is recorded per defect).
Merged severity is the max of the merged raw severities; no severity was promoted or demoted.

| Sev | Defects | Raw ids |
|-----|---------|---------|
| blocker | 1 | 7 |
| high | 5 | 1, 2, 8, 9, 10, 15, 16, 25, 26 |
| medium | 10 | 3, 4, 5, 11, 12, 13, 17, 18, 19, 21, 22, 27, 28 |
| low | 2 | 6, 14, 20, 23, 24 |

**The headline.** W1-W2 shipped a control against unbounded verify fan-out and wired it at two
enforcement points (`tools/hooks/agent-cap.js` as a PreToolUse hook, and the merge-bar leg
`tools/workflows/check-verifier-fanout.sh`, which deliberately delegates to the same predicate).
Both entry points share **five independent bypasses**, and the exact incident shape the unit exists
to ban lands green through every one of them. Measured, on this tree:

| Fixture (all with the sanctioned `boundedParallel` helper present) | hook | merge-bar leg |
|---|---|---|
| `allFindings.map((f) => () => agent(f.claim))` — the baseline | **rc=2** | **deny** |
| ...same line + `// gov:fixed-verifiers` | rc=0 | clean |
| `allFindings.filter((f) => f.severity !== 'low').map(...)` | rc=0 | clean |
| `Object.values(byId).map(...)` | rc=0 | clean |
| `const items = [...allFindings]` then `items.map(...)` | rc=0 | clean |
| `const items = [].concat(allFindings)` then `items.map(...)` | rc=0 | clean |
| `let items = [1, 2]` / `items = allFindings` / `items.map(...)` | rc=0 | clean |
| `for (const f of allFindings) out.push(await agent(f.claim))` | rc=0 | clean |

One agent per finding, blessed, in all seven. The rule reds only on the single tidiest spelling.

---

## BLOCKER

### B1 — an unrecognised fan-out receiver is silently ALLOWED instead of denied
`tools/hooks/agent-cap.js:214` (and the byte-identical `.claude/hooks/agent-cap.js:214`) · raw id 7

The enclosing-construct pass binds a receiver with
`/([A-Za-z_$][\w$]*)\s*\.\s*(map|flatMap|forEach)\s*$/` against the text immediately before the
enclosing opener. Any receiver that is not a **bare identifier** — an inline `.filter()` chain, an
`Object.values(...)`, any member expression ending in `)` or `]` — produces no match; the
`Array.from` and `for|while` alternatives do not match either, so `hit` stays `null`, control falls
off the end of the callback, and the `agent()` call is approved with no output.

Measured: `boundedParallel(allFindings.filter((f) => f.severity !== 'low').map((f) => () => agent(...)), 5)`
and `boundedParallel(Object.values(byId).map(...), 5)` both exit 0 from the hook **and** print
`verifier-fanout: clean` from `tools/workflows/check-verifier-fanout.sh`. Assigning the same filter
to a name first IS caught — so the gate turns on tidiness, and the terse inline chain (the commonest
way this stage is actually written) is the one that escapes.

`memory/guides/REVIEW-PROTOCOL.md:54-55` states the opposite: denied includes "a `.map` /
`.flatMap` / `Array.from` over any other receiver". `tools/hooks/agent-cap.test.sh:98-124` enumerates
the must-pass shapes and none is a computed receiver, so this is not a declared ceiling.

**Fix.** Make an unrecognised receiver a DENY. When an enclosing `.map|.flatMap|.forEach` opener is
found but no bare identifier can be bound (`before` ends in `)`, `]`, or a member chain), push a
finding — `why: 'agent() fanned over an expression this file cannot show to be bounded'` — instead
of falling through. Apply to both copies; `tools/hooks/agent-cap.test.sh` gates their byte-parity.

**Left-shift gate.** Add a **mutation arm** to `tools/hooks/agent-cap.test.sh`: for each ALLOW
fixture, assert that mechanically rewriting the receiver `X.map` → `X.filter(Boolean).map` still
DENIES. A whitelist gate whose deny set is not closed under trivial rewrites is not a gate; this arm
turns "closed under rewrite" into something the bar checks rather than something the author believes.

---

## HIGH

### H1 — the `gov:fixed-verifiers` marker on the `agent()` line is an unconditional, shape-unchecked bypass
`tools/hooks/agent-cap.js:179` (and `.claude/hooks/agent-cap.js:179`) · raw ids 1, 9, 25 (three
independent reproductions)

```js
if (raw.includes(FIXED_MARK)) return
```

This sits at the top of the bad-detection loop, before any enclosing-construct or receiver analysis.
The marker's shape check lives only on the **assignment** branch (L129-142); on the `agent()` line
itself there is none. So appending the magic comment to the fan-out line exempts it outright.

Measured: `const verdicts = await boundedParallel(allFindings.map((f) => () => agent(f.claim)), 5) // gov:fixed-verifiers`
exits 0 from the hook and prints `clean` from the merge-bar leg; the byte-identical line without the
comment exits 2 with ``agent() fanned over `allFindings`, which this file does not show to be bounded``.
`scan()` never adds `allFindings` to `ok`, so the shape check is genuinely SKIPPED, not satisfied —
the comment alone buys the pass.

This contradicts the file's own contract at L88-90 ("The marker is the AUTHOR'S CLAIM; the shape
check is what stops the claim being made falsely") and `memory/guides/REVIEW-PROTOCOL.md:58` ("The
marker is a claim; the gate checks the claim's SHAPE"). `tools/hooks/agent-cap.test.sh:85-96` has
three false-marker deny fixtures and every one puts the marker on the ASSIGNMENT line, so none of
them reaches L179 — and there is no allow-fixture for a marker on an `agent()` line. The test file's
own words are that a false marker must red "or the whitelist degenerates into 'write the magic
comment'"; that is exactly what happens one line lower.

**Fix.** Delete L179 in both copies. Verified non-load-bearing: a patched copy with the line removed
still exits 0 against all three shipped harnesses (`tools/workflows/tier2-review.js`,
`tools/workflows/drift-audit-code.js`, `tools/workflows/drift-audit-state.js`) — every legitimate
marker in the tree sits on a `chunk`/`splitInto`/`.filter` assignment line containing no `agent(`.
If a one-line marked fan-out must stay legal, gate it on the same shape check `scan` applies.

**Left-shift gate.** Two arms in `tools/hooks/agent-cap.test.sh`: (a) the incident line with the
marker appended must exit 2; (b) a **marker-placement invariant** — assert that for every deny
fixture, appending ` // gov:fixed-verifiers` to the offending line does not change the verdict. That
second arm is the general statement of "a claim is not a verdict" and would have caught this the day
it landed.

### H2 — the array-literal whitelist counts commas, so a spread or a `[].concat(...)` seed reads as "bounded"
`tools/hooks/agent-cap.js:161-170` · raw ids 4, 8

The literal is measured by counting top-level commas on the bracket-balanced statement, which is an
element count only for comma-separated literals. `const items = [...allFindings]` gives
`inner = '...allFindings'` → `n = 1`; `const items = [].concat(allFindings)` takes
`inner` from `lastIndexOf(']')` at index 1 → `n = 0`. Both satisfy `n <= MAX_LENSES` and enter `ok`
at L170, so the subsequent `.map((f) => () => agent(...))` passes. Measured: both exit 0 from the
hook and both print `clean` from the merge-bar leg.

This is the **silent** branch — unlike the marker path it requires no author claim and emits no
output, so nothing signals that the visible count is not the agent count. It directly violates the
header contract at L91-92 and `memory/guides/REVIEW-PROTOCOL.md:51` ("an array LITERAL with ≤ 6
elements — where the agent count is visible in the source"); neither spelling makes any count
visible. There is no allow-fixture for a spread or concat literal in the self-test.

**Fix.** Before counting: reject the literal if `inner` contains a top-level `...` spread; require
`n >= 1` (an empty literal proves nothing about what a later `.concat`/`.push` puts in it); and
require the statement to END at the closing `]` — bail if the text after `lastIndexOf(']')` carries
a member call such as `.concat(` / `.flat(` / `.push(`. Simplest sufficient form: require the whole
RHS to be the array literal (`/=\s*\[[^\]]*\]\s*$/` after the multi-line join).

**Left-shift gate.** Add both spellings as deny fixtures, and add a **counting-invariant arm**: for
each bounded-literal ALLOW fixture, assert that the reported element count equals the number of
`agent()` calls a runtime would make. The defect is precisely "the number the gate reads is not the
number that matters"; assert the equality rather than the count.

### H3 — a whitelisted receiver is never invalidated: "assigned exactly once" is published but not implemented
`tools/hooks/agent-cap.js:126` · raw ids 6, 12, 16, 27 (four independent reproductions)

```js
const asg = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=/.exec(l)
if (!asg) return
```

`scan` only inspects DECLARATION lines, `ok` is a `Set` with no removal path, and the whitelist is
keyed on identifier name for the whole file. A bare reassignment carries no `const|let|var`, fails
the regex, and returns without disturbing the entry — so a name that qualified once stays bounded
forever.

Measured, all exit 0 from the hook and pass the merge-bar leg:

- `let items = [1, 2]` / `items = allFindings` / `boundedParallel(items.map((f) => () => agent(f.claim)), 5)`
- `let batches = chunk(allFindings, Math.ceil(allFindings.length / MAX_VERIFIERS)) // gov:fixed-verifiers`
  / `batches = allFindings.map((f) => [f])` / `batches.map((g) => () => agent(...))` — i.e. the marked
  path is rebindable too

`memory/guides/REVIEW-PROTOCOL.md:48` and `:51` both specify "an identifier assigned exactly once"
for the two allowed receivers. That document is charter-binding: it asserts a property the predicate
never checks, so a reader who trusts it will believe reassignment is covered. The self-test shows the
authors treat this evasion class as in-scope — the `rule2: renamed receiver → deny` fixture
(`const groups = all`) reds — and the reassignment spelling walks straight past it.

**Fix.** Count assignments per name across the whole file (declarations plus bare
`^\s*NAME\s*=[^=]` at statement start, plus growth calls `NAME.push(` / `NAME.concat(`). Drop a name
from `ok` the moment it is assigned twice, unless the second line itself satisfies a bounded shape.
Alternatively restrict the rule to `const` declarations and deny `let`/`var` receivers outright.

**Left-shift gate.** Add the rebind fixtures as deny cases, then add a **protocol-conformance arm**
to `tools/workflows/check-protocol-parity.test.sh`: for each normative clause in
`memory/guides/REVIEW-PROTOCOL.md` §"allowed receivers", require a named fixture in
`tools/hooks/agent-cap.test.sh` that exercises it. "Assigned exactly once" had no fixture, which is
why nobody noticed it had no implementation.

### H4 — `ARMS_FLOORS` is vacuous for any gate the discovery walk does not find, and green over an empty population
`tools/memory-tree/check-arms.py:260` · raw ids 10, 15, 26 (three independent reproductions)

```python
for gate_rel in sorted({b["gate"] for b in brs}):
    ...
    want = floors.get(gate_rel)
    if not want:
        continue
```

The loop iterates the DISCOVERED population and looks floors up by key, never the reverse. Nothing
asserts that a declared floor's gate exists. The pin walk twenty lines above (L250-257) has the
explicit `r[0] not in scanned` → "the gate is no longer in the population" branch, so the case was
considered for pins and missed for floors.

Measured, two ways:

1. `do_check` with `ARMS_FLOORS` naming two gates outside the tree (a RENAMED hygiene gate and a
   nonexistent one) returns **rc=0 with empty output**. Baseline with the real floors also returns 0,
   so the two are indistinguishable.
2. A one-character cosmetic reformat of the live gate — `fail() {` → `fail () {`, which
   `HELPER_RE` at L52 (`^\s*fail\(\)\s*\{`) does not match — drops `tools/memory-tree/check-memory-hygiene.sh`
   out of `discover()` entirely. 14 fail branches and 14 armed assertions evaporate and `--check`
   still exits 0.

The backstop is inert: `memory/project/unarmed-branches.txt` is comment-only (0 data rows, by
design — 30/30 armed), so the stale-pin path cannot fire either. `.memory-tree.conf:62` and
`memory/HYGIENE.md:189` both state the branch floor is what "catches a DELETED guard" — precisely the
case that goes silent on a rename. This is the exact "guard that gets quieter" failure the module
docstring at L36-38 says the per-gate design exists to prevent.

**Fix.** In `do_check`, after `floors = parse_floors(conf)`, add two assertions:
(a) every key in `floors` must be in `scanned`, else a named failure — "ARMS_FLOORS pins <gate>,
which is not in the discovered population; the gate was renamed or the entry is stale — repoint or
delete it in a commit that says why"; (b) an empty `st["pairs"]` is a failure ("no gate discovered —
the population collapsed, which is not a pass"), matching the `pop_guard` discipline
`tools/memory-tree/check-memory-hygiene.sh` already uses.

**Left-shift gate.** Two selftest arms in the module's own `do_selftest`: a floor keyed on a
non-existent gate must red, and a fixture repo with zero discovered gates must red. Then generalise:
add a **population-liveness convention** to `tools/memory-tree/gotchas.py` so every discovery-driven
gate gets flagged for the same pair of arms at diff time. This repo already asserts liveness for
drift-audit probes ("a probe that cannot move prints DEAD PROBE"); the meta-gate is the one place it
was not applied.

### H5 — `check-wiring --session` auto-rewrites a population it does not bound, corrupting binaries and `settings.json`
`tools/check-wiring.sh:180` (population built at `:162`) · raw id 2

`DO_FIX=1` under both `fix` and `session` (L28), so the SessionStart hook silently rewrites every
tracked `.claude/` path git reports as `eol: lf`, with `tr -d '\r'`. Under a `* text=auto eol=lf`
`.gitattributes` — a common adopter spelling — that population is **everything under `.claude/`**,
because attribute matching is path-pattern only; `text=auto`'s binary detection happens at filter
time, not attr time.

Reproduced in a scratch repo whose `.gitattributes` is `* text=auto eol=lf`:

- `git check-attr eol` returns `eol: lf` for `.claude/settings.json` AND for a planted PNG under
  `.claude/skills/`.
- `bash tools/check-wiring.sh --session` printed `fixed eol` for both.
- The PNG's bytes went from `\x89PNG\r\n\x1a\n…` to `\x89PNG\n\x1a\n…` — 3 CR bytes stripped from
  the middle of a binary, md5 changed, **reported as a repair**.
- `.claude/settings.json` was rewritten — violating the invariant this same file states three times
  (L11-12 "Agent-cap wiring is never auto-applied — it would mean rewriting settings.json, the file
  the SessionStart hook lives in"; L80 and L105 "no mode mutates settings.json").

Reachability is not hypothetical: the adopter runbook copies this script into target repos and wires
`--session` as the SessionStart hook. And the "never reach past its bound" arm is green only because
`tools/check-wiring.test.sh:144` pins the fixture's `.gitattributes` to `.claude/**/*.md text eol=lf`
— the test pre-narrows the very population under test. The comment at L149-153 ("Measured: exactly
the two rendered Skills") is a measurement of THIS tree generalised into a bound.

**Fix.** Narrow the population to what the arm exists for and make it non-destructive by default:
intersect with the rendered-Skill paths the adopt scripts byte-compare (`.claude/skills/*/SKILL.md`);
skip any file `git check-attr -a` reports as `binary` or that contains a NUL byte; and never
auto-repair under `--session` — report UNWIRED there and repair only under an explicit `--fix`.

**Left-shift gate.** Add an AC9 variant whose fixture `.gitattributes` is `* text=auto eol=lf` and
which plants a binary under `.claude/` that must survive **byte-identical**, plus a `settings.json`
that must be unmodified. General rule worth writing into the kit: *a fixture may not narrow the
population its arm is testing* — where a gate's scope depends on repo config, the fixture must use
the widest config an adopter could plausibly have, not the repo's own.

---

## MEDIUM

### M1 — the eol population collapses to a green `skip` on any path containing a space
`tools/check-wiring.sh:162` · raw id 3

`git ls-files .claude/ | xargs -r git check-attr eol --` word-splits, and the result is consumed with
an unquoted `for f in $pop` at L168 — two independent quoting defects on the same path.

Reproduced: with a tracked `.claude/skills/my skill/SKILL.md` pinned `eol=lf` and holding real CRLF,
`git check-attr` was asked about `.claude/skills/my` and `skill/SKILL.md`; both answered
`unspecified`; `pop` was empty; the script printed
`skip eol — no tracked .claude/ path carries an eol=lf pin` and exited 0 with the CRLF still in the
tree. `git ls-files` additionally C-quotes non-ASCII paths, giving the same silent miss. The arm's
only failure mode becomes absence-satisfied, on exactly the `SKILL.md` class it was built for.

**Fix.** NUL-delimited plumbing end to end: `git ls-files -z .claude/ | xargs -0 -r git check-attr -z eol --`,
iterate with `while IFS= read -r -d '' f`, quote `$f` throughout, and accumulate `bad` in an array
rather than a space-joined string.

**Left-shift gate.** A fixture with a space in a `.claude/skills/` directory name that must be
reported UNWIRED, not skipped. Better still, a repo-wide convention arm: `git grep -n 'ls-files' -- '*.sh'`
must show `-z` on every pipeline that feeds `xargs` or a `for` loop. The bug class ("shell splitting
turns a violation into an empty population") belongs in `tools/memory-tree/gotchas.py`.

### M2 — the marked-derivation branch blesses any expression that merely mentions a bounded name
`tools/hooks/agent-cap.js:141` · raw id 17

```js
const refs = l.match(/[A-Za-z_$][\w$]*/g) || []
if (refs.some((r) => r !== name && ok.has(r))) ok.add(name)
```

A bare identifier-mention test, with no inspection of the operation — sitting directly under a
comment (L136-139) that justifies the rule on the grounds that "Neither filter nor slice can GROW an
array". Measured: `const ALL_LENSES = [1,2,3]` / `const LENSES = ALL_LENSES.concat(allFindings) // gov:fixed-verifiers`
/ `boundedParallel(LENSES.map(...), 5)` exits 0. One agent per finding, under a marker the gate
blessed, on a path where no shape is checked at all.

**Fix.** Restrict the derivation branch to a whitelist of non-growing member calls on a bounded
receiver — `.filter(`, `.slice(`, or a ternary whose both arms are in `ok` — and deny anything else
on a marked line.

**Left-shift gate.** A `.concat` deny fixture, plus a doc arm: the derivation case is not described
in `memory/guides/REVIEW-PROTOCOL.md` at all. Extend `tools/workflows/check-protocol-parity.test.sh`
so every branch in `scan` that can add to `ok` must be named in the protocol — an unnamed allow-path
is an unreviewed one.

### M3 — a braceless loop body containing `agent(` is never judged
`tools/hooks/agent-cap.js:237` · raw id 11

The loop detector requires `braces < 0` — an unclosed `{` above the `agent()` line — before it will
even test `/\b(for|while)\s*\(/`, so a braceless single-statement body opens no block and is never
reached. The paren walk cannot catch it either: in `for (const f of allFindings) out.push(await agent(...))`
the for-header's `)` cancels its own `(`, leaving no enclosing opener.

Measured: that line exits 0 from the hook and the merge-bar leg; the brace-wrapped twin exits 2 with
"agent() inside a loop body". `memory/guides/REVIEW-PROTOCOL.md:53-54` names a `for`/`while` body
containing `agent(` as denied — a braceless body is a body — so the rule turns on a formatting choice.

**Fix.** Add a same-line case: if the window text before `agent(` contains a `\b(for|while)\s*\(`
whose parens have already closed on that line with no `{` following, record the `loop` finding.

**Left-shift gate.** Same mutation arm proposed for B1, extended: for each loop deny fixture, assert
the brace-stripped rewrite still denies. Formatting-sensitivity is the recurring shape across B1, M3
and H2 — one property-based arm ("verdict is invariant under whitespace and brace style") covers all
three and is cheaper than three fixtures.

### M4 — `_mid_build` returns False during the rebuild window it exists to protect
`tools/memory-recall/query.py:397-411` · raw id 5

Verified by calling the predicate directly on three synthesised states:

| state | `_mid_build` |
|---|---|
| complete previous cache | False |
| `records.db` unlinked by `_write_set` (L309-310), not yet recreated | **False** |
| `records.db` recreated | True |

The middle state is unambiguously a build in flight, and the docstring (L397-405) explicitly claims
the predicate is "true during ANY build, not just the first" and that "a rebuilding sibling … is
precisely the directory this rule means to protect". It is not: with the previous manifest newest and
`records.db` missing, the `OSError` branch `continue`s and `chunks.db` (written before the manifest
last time) is older, so the function returns False and `evict_over_budget` admits the directory as a
candidate.

Compounding it, `_mid_build` is sampled at plan time (L484) and never re-checked before the delete
(L506). On win32 the open-handle failure masks the consequence; on POSIX — where the kit also ships —
unlink of an open sqlite file succeeds, the concurrent builder's directory disappears, and its
`os.replace(tmp, dirp / "manifest.json")` at L353 raises FileNotFoundError out of the recall CLI as a
traceback. Discounting one claim from the raw finding: `_dir_bytes` runs BEFORE the sampling (sizes
at L478, candidates at L482), so the check-to-delete gap is smaller than first written.

**Fix.** Fail closed: treat a MISSING `records.db` or `chunks.db` as mid-build (return True) rather
than `continue`, matching the never-evict-without-evidence rule the sibling function already uses for
a missing manifest. Then re-evaluate `_mid_build(d)` inside the execution loop immediately before
each `_remove_cache_dir(d)` and skip a directory that has become mid-build — the plan is a proposal,
not a commitment.

**Left-shift gate.** A selftest arm in `tools/memory-recall/selftest.py` that constructs each of the
three states above and asserts the verdict, so the docstring's claim ("true during ANY build") is
something the bar checks. This is a **state-table** arm: when a predicate's docstring enumerates
states, enumerate them in the test.

### M5 — the resolver-parity population is derived from the marker, so a kit that never got one is invisible
`tools/lib/resolve-python.test.sh:85` and `:99`; the escaping consumer is
`tools/drift-audit/adopt-drift-audit.sh:57` · raw id 13

The parity arm derives its population with `git grep -l '^# >>> resolve_python' -- '*.sh'` — only
files that ALREADY carry the block are judged. The idiom ban at L99 is
`git grep -nE 'command -v (python3|python|py)\b'`, which cannot see a bare invocation. So both arms
are green over a population that excludes the one file that needs them.

`tools/drift-audit/adopt-drift-audit.sh:57` is `KIT_REL="$(python -c ...)"` — bare `python`, no
resolver, unconditional, and it sits BEFORE the `--check` branch. Reproduced: with a 9009 stub first
on PATH (the MS-Store shim this whole unit exists for), the real gate leg
`bash tools/drift-audit/adopt-drift-audit.sh --check` exits 1 with a spurious DRIFT diff showing
`{{KIT_DIR}}` substituted with nothing; with a real python it exits 0 "in sync". The exposure is
wider than the MS-Store case: any host where `python` is absent but `python3` exists hits it
identically. `AGENTS.md:67`'s claim that every copy-installed kit carries the resolver inline is
false for this kit — the seven marker-carrying files do not include `tools/drift-audit/`.

**Fix.** Derive the parity population from the CONSUMERS, not from the marker: enumerate tracked
`*.sh` that invoke a python launcher as a command word (comments stripped) and require each to either
source `tools/lib/resolve-python.sh` or carry the inline block. Then inline the block in
`tools/drift-audit/adopt-drift-audit.sh` and use `$(resolve_python)` at L57.

**Left-shift gate.** This is the generalisable one: **a parity gate must never derive its population
from the thing it is checking for.** Write that into `tools/memory-tree/gotchas.py` as a bug class,
so any diff touching a `*.test.sh` that builds a population with `git grep -l '<the marker>'` is
flagged for it. Add a stub-PATH arm (a 9009 shim first on PATH) to the resolver self-test so the
failure mode the unit exists for is exercised, not assumed.

### M6 — a guide IS entry-budget capped, and two shipped docs say it is not
`tools/memory-tree/check-memory-hygiene.sh:345` · raw id 19

`index_set()` (L318) added `memory/guides/*.md` to the set BOTH checks 6 and 7 read, but `ex7`
(L345-346) exempts only `IN-FLIGHT.md`, `in-flight/*.md` and the codebase-map dossiers/FOUNDATION —
no guides clause.

Verified: `--print-index-set` lists `memory/guides/REVIEW-PROTOCOL.md`; appending a 320-char line to
it made the gate emit `HYGIENE check 7 FAILED — index entry lines over 300 chars` (file restored).
The in-code comment at L317 says "Entry-budget exempt: a guide is prose", and `memory/HYGIENE.md:106`
plus `tools/memory-tree/HYGIENE.template.md:106` both say "Entry-budget exempt — a guide is prose,
not index rows". Both doc halves are parity-gated against each other, so the shipped kit states the
same untrue thing twice. Today's guide tops out at 105 chars, so the drift is latent — the first long
prose sentence in a binding guide reds the bar with a message about "index entry lines", and the
documented remedy does not exist.

**Fix.** Add `|/guides/[^/]+\.md$` to both `ex7` assignments.

**Left-shift gate.** An arm in the hygiene self-test with a >300-char line in a `guides/` file
asserting check 7 stays silent while check 6 still caps the file. More generally: when a file class
joins `index_set`, the self-test should assert its membership in EACH check that reads the set — one
arm per check, not one arm per set.

### M7 — the new parity baseline floor accepts the very baseline it exists to reject
`tools/memory-tree/hygiene-parity.test.sh:41` · raw id 21

The floor's stated premise (L33-37) is that "the thing that actually defines when the verdicts
changed is the version constant", and it derives FLOOR via
`git log -S"KIT_MEMORY_TREE_VERSION=$KITV"`. But this diff changed the verdicts **without bumping the
constant**.

Verified: `KIT_MEMORY_TREE_VERSION` is `1.5` at both the merge-base and HEAD; FLOOR resolves to
`93dbbac`; `git merge-base --is-ancestor 93dbbac 76fcd09` succeeds — so the harness accepts the
pre-diff baseline. Yet check 5's selector went `[^/]+\.md$` → `(.+/)?[^/]+\.md$` (L284) and guides
joined the index set feeding checks 6/7. Byte-identity across that baseline cannot hold, so the run
produces exactly the wall of "true and useless" differences the floor was written to prevent.

Impact is bounded — this harness is not a merge-bar leg, so the failure mode is noise, not a false
green — but the guard's invariant is falsified by the same diff that introduces it.

**Fix.** Bump `KIT_MEMORY_TREE_VERSION` to 1.6 in `tools/memory-tree/check-memory-hygiene.sh:13` and
the paired `gov:kit memory-tree@` marker in `tools/memory-tree/HYGIENE.template.md` (which
`tools/check-kit-versions.sh` pairs), so the derived floor advances past this landing.

**Left-shift gate.** Add a leg (or extend `tools/check-kit-versions.sh`): if a diff touches
`tools/memory-tree/check-memory-hygiene.sh` **outside comments** and does not change
`KIT_MEMORY_TREE_VERSION`, red with "the engine's verdicts may have moved without the constant that
dates them". That makes "bump the version when behaviour changes" mechanical instead of remembered —
which is the same lesson as the cap-6 drift below.

### M8 — the two-copy parity arm is satisfied by absence
`tools/hooks/agent-cap.test.sh:159` · raw id 22

```sh
if [ -n "$ROOT" ] && [ -f "$ROOT/.claude/hooks/agent-cap.js" ] && [ -f "$ROOT/tools/hooks/agent-cap.js" ]; then
```

Delete the wired copy and the arm vanishes — no pass, no fail, exit 0. The second conjunct is needed
for adopters (the kit is copy-installed to `.claude/hooks/`, where `tools/hooks/` does not exist),
but the FIRST conjunct disarms the arm in exactly the repo that owns both copies.

`tools/check-wiring.sh:85-89` independently returns `skip agent-cap — not adopted` on the same
absence, while `.claude/settings.json:9` keeps dispatching
`node "${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js"`. Grep confirms no other gate leg references
the wired copy. So the state "settings dispatch a hook script that does not exist" — the state the
recall arm at `tools/check-wiring.sh:130-133` explicitly reports as UNWIRED — leaves the full merge
bar green while both fan-out rules are unenforced at the tool call.

**Fix.** Make the arm two-state, asymmetric (the pattern the recall arm already uses): if
`tools/hooks/agent-cap.js` exists and the wired copy does not while `.claude/settings.json` names
`agent-cap.js`, fail with "the wired copy is missing but settings.json dispatches it".

**Left-shift gate.** A convention arm over `tools/**/*.test.sh`: any `if [ -f … ]` wrapping an
assertion block must have an `else` that either passes deliberately or fails. "Absence-satisfied" is
the single most common shape in this review; a grep-level arm for guarded assertion blocks with no
`else` would surface the whole class.

### M9 — check 15's shape filter is unreachable, and `ended_slash` is dead plumbing
`tools/memory-tree/corpus_ids.py:252` · raw id 18

`is_file_shaped` is `cited.endswith(KNOWN_EXT) or '.' in basename`; `is_dir_shaped` is
`ended_slash or '.' not in basename`. `not is_file_shaped` entails `'.' not in basename`, which
forces `is_dir_shaped` True, so `if not is_file_shaped and not is_dir_shaped: continue` is
identically False. Verified by exhaustive evaluation over 1550 token shapes built from
`{'a', '.', '/', '-', '.md', 'x.'}` up to length 4: **0 reachable cases**, and `KNOWN_EXT` contains
no dotless entry that could break the entailment. `ended_slash` (L232) feeds only `is_dir_shaped`,
which feeds only the dead guard, so it cannot change any outcome.

That is probably the intended widening (introduced by the V8 directory-citation change), and behavior
is unchanged — but the code reads as if a live shape filter still exists, and `ended_slash` is
plumbing a later edit will trust.

**Fix.** Delete `ended_slash`, `is_file_shaped`, `is_dir_shaped` and the dead `continue`, replacing
them with a comment stating that every rooted, non-elided token is now a candidate. Or, if a real
filter was intended, make it one (e.g. reject tokens whose basename contains regex/glob
metacharacters) and arm it.

**Left-shift gate.** The generalisable arm is a **reachability assertion**: a filter branch with no
fixture that reaches it is a branch nobody reviewed. `tools/memory-tree/check-arms.py` already does
this for `fail` branches in shell gates — extend the same discipline to `continue`-shaped filter
branches in the python delegates, or at minimum add a coverage arm to
`tools/memory-tree/check-memory-hygiene.test.sh` asserting each `continue` in the harvest loop is hit
by at least one fixture token.

### M10 — the cap moved 6 → 5 and four adopter-facing statements did not
`tools/hooks/agent-cap.js:19` · raw ids 14, 20, 28

`tools/hooks/agent-cap.js:38` is `const CAP = Number(process.env.AGENT_CAP) || 5`, while L19 of the
same file still reads "CAP: default 6 (override with env AGENT_CAP)" — and the file's own deny text
at L303-304 interpolates CAP as `cap-5`, so the header contradicts the message the file emits.
`memory/guides/REVIEW-PROTOCOL.md:72` explicitly routes readers to that header ("its own header says
so"). The same stale header ships in the byte-identical `.claude/hooks/agent-cap.js:19`.

Still at 6, verified verbatim: `tools/workflows/tier2-review.js:128` ("ONE ≤6-wide wave", while the
same file's `meta` says ≤5 and `boundedParallel` defaults to 5); `README.md:45` ("cap-6") and
`README.md:58` ("never >6 concurrent"); `WIRE-INTO-PROJECT.md:352` ("cap-6"), `:354` ("the
≤6-concurrent rule") and `:355` ("≤6 concurrent").

`git log -S` dates the split precisely: `|| 5` landed in 3c794dc (the W1+W2 commit) while "CAP:
default 6" still dates to bf7f2c2 (the earlier 4→6 raise). The spec at
`memory/builds/aBatchedTribunal/spec/2026-08-09-spec-aBatchedTribunal-1.md:83-87` claims "the sites
are ENUMERATED" and lists five — the enumeration missed the header of an enumerated file and both
adopter-facing docs. Consequence is real if mild: rule 1 does not parse the helper's numeric argument
(stated at L19-20), so a runbook-following adopter's cap-6 helper passes the hook while violating the
≤5 rule the protocol declares. Nothing on the merge bar compares these numbers, so the drift is
permanent and silent.

**Fix.** Change 6 → 5 at `tools/hooks/agent-cap.js:19` (re-copy to the wired copy — the self-test
gates byte-parity), `tools/workflows/tier2-review.js:128`, `README.md:45`, `README.md:58`,
`WIRE-INTO-PROJECT.md:352-355`.

**Left-shift gate.** Single-source the number, then gate it: extend
`tools/workflows/check-protocol-parity.test.sh` with an assertion that no tracked doc under the repo
root states a fan-out cap other than the one in `agent-cap.js`'s `CAP` / `MAX_VERIFIERS` constants
(grep for `cap-\d`, `≤\d-concurrent`, `>\d concurrent`, `default \d`). A number stated in six places
is five places that can drift; the gate should read the constant and enumerate the prose.

---

## LOW

### L1 — the self-test's python launcher is the retired idiom, and an empty payload makes every ALLOW arm vacuous
`tools/hooks/agent-cap.test.sh:22` · raw id 23

`js()` builds its payload with `python3 -c … 2>/dev/null || python -c …` rather than the resolver
this very build introduced. `AGENTS.md:18` claims one resolver "sourced by four scripts and inlined
byte-identical into every copy-installed kit", and `tools/lib/resolve-python.test.sh:99` bans the
retired idiom repo-wide — but the ban only matches `command -v (python3|python|py)`, so this fourth
spelling is invisible to it (same root cause as M5).

If both launchers fail, `payload` is empty and `printf '' | node tools/hooks/agent-cap.js` exits 0
(measured), so all five `js … 0` ALLOW arms print `ok` while asserting nothing. Mitigating: `js()`
does RUN each candidate, so the MS-Store-stub mode is already handled, and if both fail the deny arms
red the whole harness — the vacuity is misleading `ok` lines inside an already-failing run, not a
silent green.

**Fix.** Inline `resolve_python` and use it, or replace the python JSON encoder with the
`node -e JSON.stringify` payload builder already used in `tools/workflows/check-verifier-fanout.sh`.
Also assert `[ -n "$payload" ]` in `js()` before calling `check`.

**Left-shift gate.** Fold into M5's consumer-derived population, and add a rule to the test-harness
conventions: **a helper that constructs a fixture must assert the fixture is non-empty** before
asserting on the verdict. An empty input that exits 0 is the purest form of a green half that would
pass against anything.

### L2 — the gate leg is labelled "12 checks" and runs 19
`tools/gate-legs.json:3` · raw id 24

The engine now runs 19 checks — inline fail branches 1-12 plus the delegated 13-16
(`tools/memory-tree/corpus_ids.py`) and 17-19 (`tools/memory-tree/gotchas.py`) — per `AGENTS.md:60`
and `memory/HYGIENE.md`, which numbers items through 19. `tools/run-gates.sh:22-23` prints the leg
name verbatim on every run, so every full-bar run reports a check count wrong by seven.
`tools/run-gates.test.sh:24-27` validates only that the name is non-empty and argv well-formed, never
the label's content. The label was already stale at the merge-base — this diff reformatted the
manifest without correcting it — so it is carried-over inaccuracy in gate output, not a regression.

**Fix.** Rename to `"memory hygiene (19 checks)"`, or drop the count from the label so the fact lives
only in `AGENTS.md` / `memory/HYGIENE.md`.

**Left-shift gate.** Prefer deletion over synchronisation: a count in a label is a second answer to a
question `memory/HYGIENE.md` already answers. If the count stays, extend
`tools/run-gates.test.sh` to parse it and compare against the gate's own `--list-checks` output (or
the count of `fail <n>` ordinals), so the label becomes derived rather than asserted.

---

## Cross-cutting

Three patterns account for 24 of the 28 raw findings, and each has a cheaper general remedy than the
per-site fixes above:

1. **Absence-satisfied and empty-population arms** (B1, H4, M1, M8, L1). A gate whose only failure
   mode requires the population to be non-empty is not a gate. Every discovery-driven or
   config-derived population in this repo needs the liveness assertion the drift-audit kit already
   applies to its probes ("a probe that cannot move prints DEAD PROBE"), and every `if [ -f … ]`
   guarding an assertion block needs an `else`.
2. **A whitelist keyed on a name that nothing invalidates, plus a shape check that is skipped, plus
   counting a proxy for the thing that matters** (H1, H2, H3, M2, M3). The `agent-cap` receiver
   analysis is five bypasses deep. The structural remedy is to invert the default: an unrecognised
   shape DENIES. Every one of the five holes is a fall-through, and every one closes if the
   unmatched case is a finding rather than a `return`.
3. **A fact stated in prose beside a constant, with no gate comparing them** (M6, M7, M10, L2). Four
   defects, four documents, zero legs. `tools/check-kit-versions.sh` and
   `tools/workflows/check-protocol-parity.test.sh` are the natural homes; the pattern to adopt is
   *the gate reads the constant and enumerates the prose*, never the reverse.

**Recommended merge order.** B1 and H1 close the two paths by which the exact incident W1-W2 was
ported to stop lands green; neither is more than a few lines. H2, H3, M2, M3 close the rest of the
`agent-cap` surface and should land with the mutation-arm gate, not before it. H4 and H5 are the two
places where a *meta*-gate went quiet — H5 additionally destroys data on adopter trees under a common
`.gitattributes`, so it should not wait.
