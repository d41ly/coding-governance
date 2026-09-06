**Serves:** diff-review TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-7 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14

# Closing diff review — the gate that grades everything except its own declaration

Tier-2 closing review, round 1 · 2026-09-06 · node `a` · build `aSurfacedLexicon` · streams tooling ·
twelve units, six passes, 70 files, 14813 insertions against 2438 deletions. This is the first review
of the CODE; the eight records already under this folder audited the SPECS before any of it existed.

**Reviewed range: `6c670b024644bf6bbcc28ee74d2265c0efd453c6...HEAD`** (HEAD = `672ae990`).

## Verdict: BLOCKED

Three blockers, four highs, six mediums, four lows — seventeen distinct defects adjudicated from
twenty-seven confirmed findings. Nothing here is an argument against the build. The convention
predicate is real, the anti-mirror discipline held everywhere I looked for a breach, coverage moved
40.4% to 99.3% on a tokenizer that actually tokenizes, and the two-sided pin is the right shape. What
blocks is narrower and, in two of three cases, one line each: the merge bar does not grade the file
this build moved its verdicts into, and the SUPPLY half answers `OK` for names the DEMAND half reds.
Both are the kit's own stated failure classes, landed inside the build that names them.

## Review shape

Raw 29 · confirmed 27 · refuted 2 · unverified 0 · precision 0.93.

Twenty-seven confirmed findings collapse to seventeen rows here: eight pairs and one triple were the
same defect reached from different lenses, and merging them is the report's job, not the finder's.
Every merge is named in its row. Precision 0.93 is high enough that the fan was well primed and low
enough that the skeptic was doing something; no row below rests on a skeptic's silence.

I re-derived the three blockers on this worktree myself rather than inheriting them, because a
blocker verdict on a closing review should not be a citation. The commands are in each row.

**Severity is mine, not the finders'.** Six rows moved. `B1`, `B2` and `B3` came in as *high* and I
raised them: each is a mechanism that cannot fail, or a shipped answer that contradicts the gate, on
the tree as it stands. `H1`, `H3` and `H4` came in split or as *medium* and settle at *high*. The
rest held where they arrived.

## The table

| # | Sev | Site | Defect | From |
|---|-----|------|--------|------|
| B1 | BLOCKER | `tools/gate-legs.json:961` | `.lexicon.conf` is in no leg's guard, so a conf-only commit skips the only leg that grades it | 1, 17 |
| B2 | BLOCKER | `tools/lexicon/lexicon.py:2169` | `--suggest` returns `OK` for names the bar reds on, because no CELLS row arms `vocab`/`notail` | 4, 21 |
| B3 | BLOCKER | `tools/lexicon/scaffold_lexicon.py:222` | `--scaffold` emits no `CELLS:` block, so a fresh adopter's `--suggest` exits 2 on every call | 5, 22 |
| H1 | HIGH | `tools/drift-audit/drift_report.py:916` | An unshipped parser id raises `KeyError` through an unguarded comprehension and kills all eight signals | 2, 13 |
| H2 | HIGH | `tools/lexicon/SKILL.template.md:53` | The shipped Skill states the one-sided pin rule this build deleted, and is gated as correct | 3 |
| H3 | HIGH | `tools/lexicon/lexicon.py:2132` | `cell.split(".")[1]` is not selector-aware, so a routed `file` cell is graded with its extension | 6, 14 |
| H4 | HIGH | `tools/lexicon/lexicon.py:1909` | The `PATTERNS REPLACES` report is ungated, and its only arm passes when the mechanism is deleted | 23 |
| M1 | MEDIUM | `tools/lexicon/lexicon.py:2116` | `read_routed_cell` routes on the raw argument, `scan_routes` on the stem | 9, 27 |
| M2 | MEDIUM | `tools/lexicon/lexicon_conf.py:43` | Three pin shapes parse, pass `check_declaration`, and are never evaluated by anything | 8, 16, 24 |
| M3 | MEDIUM | `tools/lexicon/lexicon.py:2065` | First-matching prefix selector wins in the suggester where the grader refuses `AMBIGUOUS SELECTOR` | 15 |
| M4 | MEDIUM | `tools/lexicon/lexicon.py:285` | `render_swapped_name`'s case-inheritance branches are ungated | 7 |
| M5 | MEDIUM | `tools/lexicon/lexicon.py:34` | The stated reason for omitting the refinement figure is false about the commit that states it | 25 |
| M6 | MEDIUM | `tools/lexicon/README.md:147` | The sample `--check` transcript is stale on the day it lands, beside a gated copy that is correct | 26 |
| L1 | LOW | `tools/lexicon/lexicon.py:574` | The `<<-` tab-stripping terminator match is ungated | 10 |
| L2 | LOW | `tools/lexicon/README.md:517` | "Three registries beside this file" — two ship | 11, 20 |
| L3 | LOW | `tools/lexicon/lexicon.py:949` | The `self-containment is UNJUDGED` refusal has no arm | 18 |
| L4 | LOW | `tools/lexicon/lexicon.py:887` | The `cannot be read as source` refusal has no arm | 19, 29 |

---

## Blockers

### B1 — the declaration is graded by a leg that a declaration-only commit skips

**`tools/gate-legs.json:961`** (also `.lexicon.conf:272`, the pin the skip protects). Merged from
findings 1 and 17.

Every ratchet this build added lives in `.lexicon.conf`: the two-sided scalar pins, the `CELLS`
conventions, the `PINS` conv rows, the `CANON` overlay's effect on the DEBT/UNRULED split. Exactly one
leg grades any of it — `lexicon naming predicates` — and its guard is
`["tools/", "skills/session-kickoff/", ".githooks/", ".claude/"]`. `.lexicon.conf` is at the repo root
and matches none of the four.

`changed()` at `tools/run-gates/run-gates.sh:151` is a plain pathspec diff
(`! git diff --quiet "$BASE" -- "$@"`), so a branch whose entire diff against BASE is `.lexicon.conf`
skips the one leg that would grade the change. I confirmed the guard array and the `changed()` body on
this tree. No other leg closes it: `lexicon wiring` (guard `[]`) runs `adopt-lexicon.sh --check`, which
parses the declaration, checks the `ratified`/`canon_unfrozen` stamps and byte-compares the Skill — it
never runs `lexicon.py` over the real root, so no pin equality, no conv verdict, no `DEAD CELL` and no
`AMBIGUOUS SELECTOR` arm is ever exercised. `drift-audit records` reads `VERBS`/`LANGS` only.

Concretely landable today with no verdict computed: raising `VERB_OFFENDER_PIN="968"` to any number,
flipping `py.function snake` to `py.function dark` (`dark` is a `CONVENTIONS` member, so it parses
clean), or deleting the `py.file.conv 8` row together with its `py.file` cell.

This is why it is a blocker rather than a scoping nit. The two-sided pin's own red text says *paste this
row into `.lexicon.conf`* — so the branch shape the tool actively instructs an author to produce is
precisely the branch shape that skips its own verifier. A ratchet whose drain is invisible on the
commit that drains it is not a ratchet. `.githooks/pre-push` forces `GATE_FULL=1` when no recorded full
green covers the tip, which catches many landings, but a scoped push inside `GATE_FULL_MAX_LAG=10`
still skips the leg, and unlike a too-narrow guard this omission never expires.

**Fix.** Add `.lexicon.conf` to that leg's `guard` array. The leg is `subject = repo` with a 300 s
ceiling and one corpus walk, so dropping the guard entirely is also defensible — `drift-audit records`,
the other declaration reader, correctly carries none.

**Left-shift gate.** The class is *a leg whose guard omits a file the leg reads*, and it is
machine-derivable: for each leg, intersect the paths its argv opens against its guard pathspecs, and red
on a file the leg is known to read that no guard pathspec matches. Cheaper interim version that catches
this instance and its siblings: a `run-gates` canary arm asserting that every leg naming a
tracked top-level dotfile in its argv or its script body carries that dotfile in its guard. Whichever is
built, stage a conf-only pin bump and watch the leg RUN and red before calling it landed — this build's
own rule.

### B2 — the supply verb says OK to names the merge bar refuses

**`tools/lexicon/lexicon.py:2169`** (banned-suffix twin at `:2139`; declaration at `.lexicon.conf:259-270`).
Merged from findings 4 and 21.

Reproduced on this worktree, both commands exit 0:

```
$ python tools/lexicon/lexicon.py --suggest fetch_remote --as py.function
OK — fetch_remote satisfies snake for cell `py.function`
$ python tools/lexicon/lexicon.py --suggest FooManager --as py.type
OK — FooManager satisfies pascal for cell `py.type`
```

Both names are gate offences. `fetch` is off the VERBS table — it is the NEGATIVE clause of `load` at
`.lexicon.conf:321` — and grades against `VERB_OFFENDER_PIN="968"`, a two-sided equality; `Manager` is
the first entry in `BANNED_SUFFIXES` against `SUFFIX_OFFENDER_PIN="0"`.

The asymmetry is the defect. `--suggest` gates its verb check on the cell's `vocab` flag and its
banned-tail check on `notail`, while P1 and P2 grade the corpus unconditionally — the walk appends to
`offenders["verb"]` for any leading token not in VERBS regardless of cell flags. This repo's `CELLS`
block has six rows and arms neither flag on any of them, which I read directly. So the advisor's verb
path is dead here while the grader's is live.

Blocker because of who reads it. `.claude/skills/lexicon/SKILL.md` instructs every agent in this repo to
ask this verb before writing a name, and documents ``use `load_remote` — the declaration says `load`,
NOT `fetch``` as the primary answer — an answer this declaration cannot produce. AGENTS.md §12 carries
the same promise. Suggester and grader now give two answers about one name, which is the exact
surface-blindness `TOOL-aSurfacedLexicon-8` was built to remove. A reviewer's confusion is cheap; an
advisor that confidently green-lights the offence, on the tree that ships the advisor, is not.

Two further consequences worth stating with the row. Every AC for the verb path in spec-8 was graded
against a scratch declaration carrying `py.function snake vocab`, never against the declaration that
ships — so the acceptance ledger is green with the mechanism dead on the real tree. And the README's own
worked example is wrong here: `--suggest fetch_remote --as js.function` returns `fetchRemote`, where
`README.md:404` promises `loadRemote`.

**Fix.** Root-cause it at the asymmetry, not at the declaration. P1 and P2 have no per-cell arming, so
`run_suggest` should run the verb check and the banned-tail check whenever `VERBS`/`BANNED_SUFFIXES` are
non-empty, with `vocab`/`notail` NARROWING rather than enabling. The one-line alternative — add `vocab`
to the three function cells and `notail` to `py.type`, then paste the `.debt`/`.unruled` rows `--measure`
emits — fixes this tree and leaves every other adopter carrying the defect.

**Left-shift gate.** A selftest arm that closes the loop rather than testing either side alone: over a
fixture corpus, take every name `--check` reports as an offender, feed each back through `--suggest` on
its own cell, and assert not one of them comes back `OK`. That arm fails on any future divergence between
the two surfaces, whatever causes it, and it is the only shape that catches a whole class rather than
today's two flags.

### B3 — a scaffolded adopter's supply half cannot answer anything

**`tools/lexicon/scaffold_lexicon.py:222`** (refusal at `lexicon.py:2039`; `--as` required at `:2271-2274`).
Merged from findings 5 and 22.

`grep -n "CELLS\|PINS" tools/lexicon/scaffold_lexicon.py` returns nothing, which I confirmed: the seed
emits `LANGS`, `VERBS`, both scalar pins, `ratified=""` and comments. No `CELLS:` block, and no mention
that one is owed. But `--as <ext>.<surface>` is now REQUIRED and `resolve_cell` refuses any spec no
`CELLS` row names.

Reproduced end to end in a fresh repo: `bash tools/lexicon/adopt-lexicon.sh --scaffold` writes the conf
and renders and installs `SKILL.md` in the same run, and then the very command that Skill documents —
`python tools/lexicon/lexicon.py --suggest fetch_thing --as py.function` — exits 2 with ``cell
`py.function` is UNDECLARED — no CELLS row names it … Declared cells: none``. `--as function` exits 2
with the bare-surface menu reading `none — this declaration carries no cell for that surface`. There is
no fallback path.

Blocker because this is the shipped product's first-run experience, and nothing surfaces the gap:
`kit.toml` declares `[[hole]]` rows for `lexicon-ratified` and `lexicon-pins` only, and the README's
Adopting section (lines 522-545) covers curating VERBS, ratifying and re-measuring pins without ever
mentioning cells. The kit's own canon-overlay test fixture hand-writes a `CELLS` block
(`adopt-lexicon.sh:295-296`) — the same gap seen from the inside. Every new adopter installs a Skill
whose only documented invocation cannot succeed until they hand-author a block nothing points them at.

**Fix.** Emit a seeded `CELLS:` block from the walk — one row per `(ext, surface)` actually extracted,
defaulting to `dark` where no convention can be honestly proposed, with an emitted comment naming which
rows the adopter should arm. Failing that, add a `[[hole]]` with id `lexicon-cells` so the adopter is
told the declaration is incomplete instead of discovering it through a refusal.

**Left-shift gate.** Extend the `lexicon wiring` leg's existing scaffold-into-a-temp-dir arm by one step:
after `--scaffold`, run the exact `--suggest` invocation the rendered `SKILL.md` documents, and assert
exit 0. That arm binds the scaffolder to the Skill it installs, which is the actual contract, and it
would have caught this the moment `--as` became mandatory.

---

## High

### H1 — an unshipped parser id takes down all eight drift signals

**`tools/drift-audit/drift_report.py:916`** and **`:849`**; raise originates at `tools/lexicon/lexicon.py:824`.
Merged from findings 2 and 13.

`_build_armed_exts` drops `dark` rows and `probe` rows with an unknown set, but KEEPS a `parser` row whose
pattern-set id the kit does not ship. `extract_text` then reaches `PARSERS[pset]` and raises `KeyError`.
`PARSERS` ships `python-ast` and `shell-tokens` only.

Nothing upstream names the bad row: `lexicon_conf.langs()` validates the mode token and not the pset,
`check_declaration` validates CELLS/PINS cross-refs and not parser ids, and `adopt-lexicon.sh --check`
only parses. Nothing downstream catches it either — `drift_report.py:853` catches
`(SyntaxError, OSError)`, `:964` catches `(SyntaxError, ValueError)`, neither covers `KeyError`, and
`main()` evaluates `out = [s(ctx) for s in SIGNALS]` unguarded at `:1563`. One legal-looking `LANGS` row
therefore costs all eight signals and a traceback, on a leg (`drift-audit records`) that carries no guard
and runs on every bar. `_load_lexicon`'s docstring promises "never a raise and never a red" for exactly
this class.

The engine's own `scan_corpus` guards this case with a named refusal at `lexicon.py:875`, so the two
readers of one declaration diverge — and the guard's existence is direct evidence the authors treat the
state as reachable and owed a message. The crash path is new: before `TOOL-aSurfacedLexicon-14`, `parser`
ignored its set id and always ran the Python parser. Held at high rather than blocker because it needs a
declaration nobody has written; it is an adopter typo away, not live.

**Fix.** Mirror `scan_corpus`'s refusal at both call sites — skip when
`mode == "parser" and pset not in lex.PARSERS`, the way the `probe` arm already skips on
`pset not in sets`. Belt and braces, add `KeyError` to the two `except` tuples. Also correct the
docstring at `:907-909`, which asserts unknown pattern sets are dropped and is now false for the parser
arm.

**Left-shift gate.** Validate the pset against `PARSERS`/`PATTERN_SETS` in `check_declaration`, where
every other cross-block reference is already checked, so a bad row is a named refusal at parse time and
no reader has to guard it. That is the "one shared core, thin adapters" fix; the two call-site skips are
the local one. Add one drift-audit arm that stages `py:bogus-parser:parser` and asserts a named line
rather than a traceback.

### H2 — the shipped Skill teaches the rule this build deleted, and the gate certifies it

**`tools/lexicon/SKILL.template.md:53`**, rendering verbatim to `.claude/skills/lexicon/SKILL.md:75`.
Finding 3.

The template still reads ``{{GATE_CLI}}` reds when an unwaived offender count exceeds the declared pin`.
Commit `e354db0a` made every pin a two-sided equality: `lexicon.py:1726-1738` reds on BOTH sides
(`elif len(unwaived) < pin: … UNDER pin … Paste this row`), and the same rule is applied to the per-cell
`.conv` pins at `:1771` and the `.debt`/`.unruled` rows at `:1793`.

What makes it high rather than a doc nit is the certification. `adopt-lexicon.sh --check` byte-compares
render against render, so the stale sentence is GATED AS CORRECT and structurally cannot drift into
notice. Meanwhile `tools/lexicon/README.md:100` states the opposite in bold — "Every pin is a TWO-SIDED
equality. A count that falls reds exactly as one that rises does" — so the kit ships two adopter-facing
documents contradicting each other on the single behaviour this build changed, and the one an agent loads
as instructions is the wrong one. An author who deletes offenders is told the gate cannot red, then gets
a red naming a row nobody told them to paste: the precise confusion the two-sided pin's failure text was
written to prevent.

The same section also documents `main`/`cmd`/`test` reserved rows and mentions no cell or convention
predicate at all, while `CELLS` is the build's headline feature. One sub-claim from the finder does not
carry and I drop it: `--brief` appears nowhere in the template.

**Fix.** Replace the sentence with the two-sided statement, add one line for the `<cell>.conv` verdicts,
re-render with `bash tools/lexicon/adopt-lexicon.sh --render`.

**Left-shift gate.** The general form is hard and the specific form is cheap: a selftest arm asserting the
Skill body contains no sentence describing a pin as one-sided (grep for `exceeds the declared pin` and
its near neighbours, red on a hit). Better, and worth the unit: make the Skill's pin paragraph a rendered
token filled from the same constant the checker's failure text uses, so the two cannot disagree —
byte-comparing a render against a render tests the renderer, never the claim.

### H3 — a routed `file` cell is graded with its extension

**`tools/lexicon/lexicon.py:2132`**. Merged from findings 6 and 14.

`graded = read_stem(...) if cell.split(".")[1] == "file"` runs AFTER `read_routed_cell` has reassigned
`cell` to the selector'd key. For a routed cell the key is `py.file+prefix:test`, so `cell.split(".")[1]`
is `file+prefix:test`, the test fails, the stem is never taken, and `graded` keeps the extension. Because
`.` is outside `_SEPARATORS`, the name is then unspellable in the target convention and the advisor emits
a false refusal.

Reproduced with `py.file snake` + `py.file+prefix:check kebab` and a tracked `core/check-arms.py`:
`--check` reports `py.file+prefix:check.conv 0 of 1 against kebab` — the stem `check-arms` SATISFIES —
while `--suggest check-arms.py --as py.file` prints "does not satisfy kebab … this verb will not re-spell
it". Two surfaces, one name, opposite answers. `README.md:388` tells the adopter the opposite of what the
code does.

Every other cell-key reader in this kit routes through `parse_cell_key`. Unrouted `file` cells are
unaffected, so the defect is exactly the routed case: latent in gov, live for any adopter using the
documented `+prefix:` selector.

**Fix.** `parse_cell_key(cell)[1] == "file"` — the reader is already imported at module top. The same
`cell.split(".")[1]` idiom appears in two `check_pass` messages (`:1738`, `:1767`) and mis-labels a
selector'd cell there too; fix all three in one pass.

**Left-shift gate.** Ban the idiom rather than fixing the instance: a selftest (or a `check-arms` scan
arm) asserting `cell.split(".")` appears nowhere in `lexicon.py`, with `parse_cell_key` as the one
reader. That is the gate-the-class rule applied to a parsing habit, and it is a one-line predicate. Pair
it with a fixture declaring a `+prefix:` selector on a `file` cell so the routed path has any coverage at
all — H3, M1 and M3 are three defects on a code path with zero fixtures.

### H4 — the `PATTERNS REPLACES` report has an arm that passes when the report is deleted

**`tools/lexicon/lexicon.py:1909`**. Finding 23.

`over = [k for k in patterns if k.split(".")[0] in PATTERN_SETS]` has exactly one consumer, the print at
`:1911-1912`. Replacing it with `over = []` in a kit copy leaves `selftest.py` green at 467 arms.

The only selftest line mentioning the report is `selftest.py:1894`:
`check("a declaration touching no SHIPPED key prints no REPLACES line", "REPLACES" not in out, out)` — an
assertion of ABSENCE, which passes *precisely because* the mechanism is gone. That is the
fixture-passes-by-finding-nothing shape, guarding the report whose job is to stop it, in the build whose
first rule is that a gate must have been seen to fail. Two other hits are a direct unit call to
`resolve_pattern_sets` (never the printed report) and an unrelated canon-cluster arm.

What it costs when it rots: `resolve_pattern_sets` replaces per key, so an adopter row that WEAKENS a
shipped regex rather than emptying it silently grades a smaller population, and this printed line is the
kit's only way to see that. Nothing on any bar would notice the report's removal.

**Fix.** Add the positive arm beside `:1894` — a `run_case` declaring `js-regex.types` (a shipped key) and
asserting both `PATTERNS REPLACES a SHIPPED extractor key` and `js-regex.types` appear in the output. The
`_TS_PATTERNS` fixture already exists a few lines up; it only ever declares unshipped ids.

**Left-shift gate.** The instance is one arm. The class is the interesting one and this build has now hit
it twice (here and, differently, in M4/L1): an absence assertion with no positive twin. A selftest
meta-arm can find them — flag any `check(...)` whose predicate is a bare `X not in out` with no sibling
arm asserting `X in out` for the same token. Not free to write, but this build's evidence says the class
is live.

---

## Medium

### M1 — the suggester and the grader partition on different strings

**`tools/lexicon/lexicon.py:2116`**. Merged from findings 9 and 27. Same ordering bug as H3, opposite
half: H3 is what happens after routing hits, M1 is that routing is asked the wrong question.

`read_routed_cell` is handed the RAW `--suggest` argument; `graded` (the `read_stem` result) is computed
thirteen lines below at `:2129`. The grader's `scan_routes` matches on the stem, because its population
comes from `scan_file_stems` at `:1000`. So the same file routes into different cells on the two
surfaces. Reproduced against this repo's corpus with `py.file+prefix:test kebab`: `--check` routes three
tracked stems into that cell and reports `3 of 3 against kebab — violation 3`, while
`--suggest tools/codebase-map/test_codebase_map.py --as py.file` answers `OK — test_codebase_map
satisfies snake for cell py.file`, because the raw argument starts with `tools/` and misses the prefix.
The path form is in-contract by the implementation's own hand — `:2135` deliberately strips `\` and `/`.

**Fix.** Hoist the `graded` computation above the routing call (with H3's `parse_cell_key` correction) and
pass `graded` as the name to route on. The surface is already known from `resolve_cell`'s return, so the
reorder is free.

**Left-shift gate.** Covered by B2's closed-loop arm if it is written over a corpus that includes a
selector'd `file` cell — feed every `--check` verdict back through `--suggest` and assert agreement,
including which cell each surface chose.

### M2 — three pin shapes parse, pass validation, and are graded by nothing

**`tools/lexicon/lexicon_conf.py:43`** and **`:406`**. Merged from findings 8, 16 and 24.

Three well-formed declarations that can never fire:

- `<cell>.suffix` on any cell. `suffix` is a member of the closed `PIN_PREDICATES` and is documented at
  `README.md:41` as one of four declarable predicates, but no code path reads it. Verified by diff: two
  runs over one fixture corpus, one carrying `py.type.suffix 99` and one not, produced byte-identical
  output at the same exit code.
- `<cell>.debt` / `<cell>.unruled` on a cell lacking `vocab`. `check_pass` iterates
  `measured["vocab_cells"]`, which `measure_vocab_cells` populates only for `vocab` cells — and this repo
  declares none (see B2).
- `<cell>.conv` on a `dark` cell. The comparison at `lexicon.py:1770` sits below the `dark` branch's
  `continue` at `:1766`.

Observed: a declaration carrying `py.function.debt 9999`, `py.function.unruled 4242` and
`py.type.conv 777` (with `py.type dark`) produces no line at all about any of the three. Control: with
`py.type` left at `pascal` the same 777 pin does red, so the silence is specifically the unevaluated-key
path. `check_declaration` refuses a PINS row whose cell has no CELLS row — three lines away — so the
sibling case is already handled and these are the gap beside it. There is a `STALE WAIVERS` arm and no
`STALE PIN` arm.

**Fix.** Add an UNREAD PIN refusal in `check_declaration` covering all three shapes, naming the row's
line the way the two refusals beside it do. For `suffix` specifically, choose: wire it (census banned-suffix
offenders per cell the way `measure_vocab_cells` censuses the verb split) or drop it from `PIN_PREDICATES`
and from the README so a `suffix` row becomes the named refusal every other typo gets.

**Left-shift gate.** The generalisation is worth more than the three cases: after a pass, diff the set of
declared `PINS` keys against the set of keys any verdict path actually consumed, and red on the
difference. That is a `STALE PIN` arm by construction, it needs no enumeration of shapes, and it catches
the next unevaluated predicate somebody adds to the closed set.

### M3 — the suggester resolves an ambiguity the grader refuses

**`tools/lexicon/lexicon.py:2065`**. Finding 15.

`read_routed_cell` returns the FIRST prefix selector whose literal matches, in dict order. `scan_routes`
refuses the same name as `AMBIGUOUS SELECTOR` and grades it by neither cell. Reproduced with
`py.function+prefix:Test pascal` and `py.function+prefix:Te camel`: `--suggest TestThing --as py.function`
exits 0 with `OK — TestThing satisfies pascal for cell py.function+prefix:Test`, while `--check` exits 1
with `AMBIGUOUS SELECTOR … graded by NEITHER`. The early `return` also swallows the `decorator` note when
a prefix row is declared above a decorator row.

`scan_routes`' own docstring calls this resolution disqualifying — "a naming gate whose verdict depends on
which row the reader saw first is not a declaration" — and the suggester does exactly it. Severity holds at
medium on an honest caveat: any overlapping-prefix pair is already red at `--check` (AMBIGUOUS if some
name matches both, DEAD CELL otherwise), so the divergence is only reachable while the declaration is
already failing. But `--suggest` is the ask-before-you-write verb, and it answers confidently in that
window.

**Fix.** Collect every matching prefix selector rather than returning on the first, and refuse with the
wording `scan_routes` uses, naming both literals. Minimum acceptable: answer in the parent's convention
and emit a `note —` line, the way the `decorator` branch already does.

**Left-shift gate.** One selftest arm asserting `--suggest` and `--check` return the same verdict class on
an overlapping-selector declaration. Subsumed by B2's closed-loop arm if that arm compares cell choice and
not just OK/not-OK.

### M4 — the case-inheritance branches are load-bearing and ungated

**`tools/lexicon/lexicon.py:285`**. Finding 7.

Replacing the three-branch `cased` block with `cased = want` leaves `selftest.py` green at 473 arms, and
`--check` and `--list` (253,995 lines, 79 DEBT rows) diff byte-identical against the shipped engine. The
branches are real: shipped `render_swapped_name('FetchThing','load')` returns `LoadThing` and
`('GETData','read')` returns `READData`; reverted they return `loadThing` / `readData`.

Two reasons for the invisibility, both verified in source. Every AC2/AC4 input is lowercase-leading
(`fetchUserData`, `getUserURLs`, `fetch_v2_data`, `create$data`), so `surface[:1].isupper()` is never
True. And on the `--suggest` path `render_convention` re-cases the answer and masks the difference. The
one unmasked consumer is the P1 DEBT detail line at `:1461`, which never calls the re-caser — and this
corpus happens to carry no capitalised DEBT offender.

**Fix and left-shift gate are the same thing.** Add a selftest arm on the `--check`/`--list` DEBT line —
not `--suggest`, which masks it — with a Pascal-led and a SCREAMING-led off-table name, asserting the
rename preserves the caller's case.

### M5 — a provenance claim that is false about the commit carrying it

**`tools/lexicon/lexicon.py:34`** and **`tools/lexicon/README.md:244`**. Finding 25.

Both carriers justify omitting the refinement figure by asserting the refinement "was never committed, so
no reader could re-derive either". `memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-14.md:157-186`
is tracked, landed in `2d487019` — the same build — and carries the refinement as a runnable snippet that
prints `94 608 336 272`. The engine header's own pointer ("it lives in the build record with the command")
points at the record carrying both commands.

Medium, not low, because the sentence is the SOLE stated reason for the omission, which makes it
load-bearing provenance rather than colour — and the kit's own `KNOWN_EXTS` comment states the rule it
breaks: "A fix comment is read as provenance, so an overstated one is worse than none." A future reader
deletes the spec snippet believing nothing depends on it.

**Fix.** Point both carriers at the snippet that does re-derive the figure, and keep the omission argued on
the ground that actually holds — two disagreeing prose copies — rather than on a false claim about the
tree.

**Left-shift gate.** Not gateable as stated, and I would not invent one. It belongs in the recurring-bug-class
checklist as a named class: *a comment justifying an omission by asserting a record does not exist* — a
claim about the tree, checkable by grep at review time, and this build produced one.

### M6 — an ungated copy of a gated number, already disagreeing on landing day

**`tools/lexicon/README.md:147`**. Finding 26.

The sample `py.constant.conv` block prints `0 of 352 … teeth camel=352 kebab=352 pascal=241 snake=352;
population 352 of 736`. The live run on this worktree prints `0 of 353 … camel=353 kebab=353 pascal=242
snake=353; population 353 of 828`. All five figures differ, and the block is a verbatim transcript, not an
abstract format example.

The sharp part: `.lexicon.conf:143,145` carries the same two numbers and is GATED — `selftest.py:1812-1819`
reads the armed row's and the widest row's `graded` out of the conf by anchored regex and compares each
against what `--check` prints, which is why the conf copy is correct at 353/828. So the tree holds a gated
carrier and an ungated copy of one fact, already disagreeing, in the file an adopter reads first. Six of
this diff's corrections were made against exactly this shape.

**Fix.** Replace the literal figures with `<n>`/`<d>` placeholders and point at
`python tools/lexicon/lexicon.py --check` for the real ones. Cheaper than a gate, and drift-proof by
construction.

**Left-shift gate.** If the transcript must stay literal, extend `selftest.py:1812-1819` to read the block
out of `README.md` the same way AC5 reads it out of `.lexicon.conf` — one more anchored regex, same arm.
The placeholder route is the lazier and better answer.

---

## Low

### L1 — the `<<-` heredoc terminator match is ungated

**`tools/lexicon/lexicon.py:574`**. Finding 10.

Replacing `(raw.lstrip("\t") if strip else raw) == delim` with `raw == delim` leaves `selftest.py` green at
473 arms and `--check` byte-identical, because `git grep -l -- '<<-' -- '*.sh'` returns nothing in this
repo and no fixture carries one. The branch is load-bearing: on a `<<-EOF` heredoc with a tab-indented
terminator the shipped tokenizer reaches the following definition, the reverted one raises
`unterminated heredoc`, which `:881` turns into a `declared 'parser' but does not parse` refusal — a red
gate for any adopter whose shell uses `<<-`. Correct code, zero coverage.

**Fix and gate.** One `scan_shell_tokens` fixture: a `<<-` heredoc with a tab-indented terminator followed
by a real definition.

### L2 — "Three registries beside this file", and two ship

**`tools/lexicon/README.md:517`**. Merged from findings 11 and 20.

`git ls-files tools/lexicon/` lists two `.txt` registries, `WAIVER_FILES` at `lexicon.py:74-77` has two
keys, `KINDS` at `:93` is `("verb", "suffix")`, and `kit.toml:26` lists two. `lexicon-layer-waivers.txt`
was deleted by this build in `9eda7282`, and `kit.toml`'s comment was corrected in that same commit
("The three waiver registries" → "The waiver registries") while the README was not.

**Fix.** Drop the numeral the way `kit.toml`'s line did.

**Left-shift gate.** The class is this build's own — an authored count beside a derived population — and
it is worth one cheap arm rather than one edit: a selftest that greps the kit's markdown for a spelled
cardinal immediately preceding `registries`/`waiver` and reds on a hit. Narrow, but this exact sentence
has now survived the commit that falsified it.

### L3 — the `UNJUDGED` self-containment refusal has no arm

**`tools/lexicon/lexicon.py:949`**. Finding 18.

`grep -c UNJUDGED tools/lexicon/selftest.py` is 0. Every SIBLING branch of `check_self_containment` is
staged — foreign import, from-import dedupe, relative-plus-stdlib silence, both DEAD PROBE shapes, the
green control — so this one reads as covered by association. It is the branch deciding whether a broken
sibling module degrades the walk silently or reds, and its failing case has never been observed.

**Fix and gate.** One arm beside the existing `build_kit_copy` fixtures at `selftest.py:220-247`: append
`\ndef (:\n` to a copied module, call `check_self_containment(_kit)`, assert the problem list carries
`UNJUDGED` and names the file. The walk root is a parameter precisely so this can be staged.

### L4 — the `cannot be read as source` refusal has no arm

**`tools/lexicon/lexicon.py:887`**. Merged from findings 19 and 29.

`grep -c "cannot be read as source" tools/lexicon/selftest.py` is 0; the SyntaxError sibling has one at
`selftest.py:552`. The split's entire justification is that the two refusals say different things —
`run_brief` reported both as "does not parse", a true refusal under a false reason for half of them — so
what nothing exercises is exactly the distinction the split buys. A future edit re-merging them reds
nothing. Reachable: `tracked_files` does not filter for existence and `extract` calls `path.read_text`, so
a tracked file deleted from the worktree lands here.

Not a duplicate of the OPEN row `TOOL-aSurfacedLexicon-21`, which asks for a meta-gate over Python refusal
branches and explicitly defers the fix — deferring a meta-gate does not waive a newly landed unarmed
branch, and it is not the same remedy as the one arm this needs.

**Fix and gate.** In an existing `run_case`, `git add` a `.py` then delete it from the worktree before
invoking the engine; assert the output carries `cannot be read as source` and not `does not parse`.

---

## What the build got right, and where the defects cluster

The anti-mirror rule held. I went looking for a predicate whose standard was derived from the graded
population and did not find one: the canon is frozen and external, the corpus admits as evidence only
which spellings become DEBT, and the CANON overlay is stamped, owner-gated and prints on every run. That
was the rule most worth breaking and it is intact.

The seventeen defects are not scattered. They fall into four clusters, and each cluster is one of this
project's own named classes landing inside the build that names it:

- **A gate that cannot fail** — B1, M2, and the reason B2 went undetected. Six of the seventeen.
- **Two answers to one question** — B2, H2, H3, M1, M3, M6. The suggester and the grader; the Skill and
  the README; the README and the conf. Six more.
- **A branch nobody has watched fail** — H4, M4, L1, L3, L4. Five, and H4's arm is worse than absent
  because it is a false green.
- **A count or a claim in prose beside the thing that owns it** — M5, L2, M6. The class this build
  corrected eight times elsewhere.

The pattern under the pattern is that the new SUPPLY surface (`--suggest`, the scaffolder, the Skill) is
tested against scratch declarations while the DEMAND surface (`--check`) is tested against the real tree.
Every blocker and three of four highs live in that gap. One arm closes most of it and is worth building
before any of the individual fixes: **take every offender `--check` reports, feed each back through
`--suggest` on its own cell, and assert the two surfaces agree — on the verdict AND on the cell.** B2, M1
and M3 all fail it today; H3 fails it on a corpus with one selector row. If only one thing is built from
this report, build that.

The recommended landing order is B1 first — it is one array element, and until it lands, no fix below is
graded on the commit that makes it.
