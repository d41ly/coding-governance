# review-dClosedLexicon-5 — Tier-2 code review of the round-2 REMOVAL commit

## Verdict: BLOCKED — 2 blockers, 3 high

**Subject:** commit `f917466` ONLY — the second fix round, which REMOVES the construction-based
reachability proof that `reviews/2026-08-16-review-dClosedLexicon-4.md` measured to be a tautology,
and narrows what the kit claims. Files judged: `tools/lexicon/lexicon.py`,
`tools/lexicon/selftest.py`, `tools/lexicon/adopt-lexicon.sh`, `memory/map/features/lexicon.md`,
`memory/gotchas/armed-but-unreachable-rule.md`, `AGENTS.md`, `.gitattributes` · streams `tooling` ·
node d · 2026-08-16

**Binding spec:** `spec/2026-08-16-spec-dClosedLexicon-1.md`, still at **rev-7**. **Folds:** none —
and that is finding H3. Round-3's findings (review-3) and round-4's (review-4) are not re-raised
except where this commit's fix for them introduced something new.

## Review shape

| | |
|---|---|
| raw findings | 29 |
| confirmed (survived an adversarial skeptic) | 26 |
| refuted | 3 |
| unverified / outstanding | 0 |
| precision | 0.90 |

The 26 confirmed findings collapse to **14 distinct defects** — 2 blockers, 3 high, 5 medium, 4 low.
Convergence was heavy and is itself signal: four independent verifiers reproduced the `_glob_match`
nesting regression (ids 2, 7, 15, 26), four the map-dossier self-contradiction (ids 5, 11, 17, 23),
three the un-folded spec (ids 12, 19, 25), three the surviving call-site over-claim (ids 10, 16, 22),
three the garbled `UNSELECTIVE` remedy (ids 9, 18, 28) and two the stale selftest comments (13, 20).
Duplicates are recorded under each defect rather than repeated as rows.

**Scope note.** Security is out of scope (local developer gate, tracked files, no network surface, no
untrusted input). Lenses: CORRECTNESS, VACUITY, ARM-CAPABILITY, RECORD-VS-REALITY. The full bar is
60/60 green and `selftest.py` reports 48 arms, so **every finding below explains why a green gate is
wrong**, not merely that something is unchecked.

**The headline.** The removal itself is right, and the reasoning behind it is the best thing in this
diff: a vacuity check that is itself vacuous is worse than none, and removing it rather than patching
it is the correct call. But the commit did two other things while it was in there — it rewrote
`_glob_match` and it scoped the stem lookup — and **both of those are silent false-negative
regressions against `77d276d`**, measured end to end. The gate now misses forbidden imports it used
to catch, with no output, in exactly the shapes adopters write. Meanwhile the retraction is
half-applied: four prose carriers still assert the removed proof, including the call-site comment
directly above the renamed function and the spec of record, which is still at rev-7 describing an
`UNMATCHABLE LAYERS RULE` refusal the engine no longer emits.

---

## Answers to the five questions asked

**(1) Does `scan_unselective_rules()` claim only what it does, and can it pass vacuously?**
The literal claim — both LAYERS globs select a tracked file — is TRUE of the code, and the name
matches the behaviour. The docstring's "WHAT THIS IS NOT" preamble is honest and well written. But
**yes, it can pass vacuously**, in a shape live for every adopter: a FROM glob selecting only files
whose LANGS mode is `dark`. `scan_unselective_rules` quantifies over all tracked `files`; the
extraction loop skips `dark` files outright, so the two populations differ. Reproduced — see **M2**.
Separately, its operator-facing remedy sentence is garbled (**M3**) and provably false in a run that
flags an offender for the same rule (**M4**).

**(2) Does the new anchoring break a legitimate match, and is the nesting rule correct?**
**Yes, and no.** The `<dir>/*` nesting branch is incorrect for any pattern carrying a wildcard before
the trailing `/*`, and it breaks matches that worked at `77d276d`. This bites **both** call sites in
`check_layer_violation` — the `frm` side (importers nested deeper than one level stop being selected)
and the `to` side (a resolved candidate nested deeper escapes the rule). The third call site,
`scan_unselective_rules`, does **not** catch it, because depth-1 files still match both globs, so the
rule still reads "selective". Measured, end to end — see **B2**. Note also that the docstring's own
worked example (`tools/codebase-map//codebase-map/conf`) still matches under the new code, so the
stated rationale for the rewrite is not demonstrated by it (**M5**).

**(3) Does the extension + importer-local scoping introduce a false negative?**
**Yes, on the package `__init__` / fully-qualified dotted case.** Measured regression against
`77d276d`: with `LAYERS: src/pkg/consumer/* -> src/pkg/shared_core/*`, an importer doing
`import pkg.shared_core.helper` alongside a local `helper.py` sibling now resolves to the sibling and
nothing else, so the genuine cross-layer import goes unreported. Control: delete only the local
sibling and the offender fires. See **B1**. The other two shapes asked about:
- *A same-extension file in a third directory* — still resolves. `local` is empty, so `local or hits`
  yields `hits`, which retains it. No false negative.
- *A JS bare specifier* — the extension filter is a real narrowing: a `.js` importer resolving to a
  `.ts`, `.jsx`, `.mjs` or `.cjs` file no longer resolves at all. That is a defensible trade for the
  false positives it removes, but it is recorded only in a source comment, not in the dossier's Gaps
  enumeration where the kit makes its limits claim. See **L4**.

**(4) Are the new arms genuinely capable of failing?**
I verified each by revert, since that is the standard this same diff writes down at `selftest.py:297`.

| arm | revert applied | result |
|---|---|---|
| P2 bare suffix (`name.endswith(suf)` with no `name != suf` exemption) | restored the exemption | **RED** — `P2 red: a type named EXACTLY the banned suffix reds` |
| FROM-glob-empty branch | deleted the branch | **RED** — `P3 unselective: a rule whose FROM glob matches no tracked file reds` |
| importer-local precedence | dropped `local or` | **RED** — `P3 green: an importer-local file WINS…` |
| extension scoping | dropped the `ext_of(p) == ext` filter | **RED** — `P3 green: a same-stem file of a DIFFERENT extension is not a resolution` |
| CRLF half A (exit code, `selftest.py:311`) | (verified by the author) | RED |
| CRLF half B (message, `selftest.py:313`) | — | **NOT CAPABLE** — asserts `"ratified" in out`, a substring the adopter's SUCCESS line also contains. See **L1** |
| `_glob_match` rewrite (`lexicon.py:174-188`) | restored the pre-diff matcher verbatim | **GREEN — 48/48, and the live gate over 472 files still exits 0.** See **M1** |

So four of the five you had not checked are genuinely armed. The two that are not are the CRLF
message half (a false arm inflating the 48 count) and — more importantly — the diff's single largest
surviving code change, which has no arm at all. That is the direct reason **B2** shipped unnoticed.

**(5) Does any prose still claim the removed reachability proof?**
**Yes, in four places.** Clean: `AGENTS.md` (no lexicon reachability claim survives),
`memory/gotchas/armed-but-unreachable-rule.md` (correctly rewritten — it now records the tautology as
the instructive failure), `.gitattributes`, and both engine docstrings (`lexicon.py:44-45`, `267-285`),
which are accurate. Surviving carriers:

| carrier | severity |
|---|---|
| `tools/lexicon/lexicon.py:330` — the call-site comment, three lines above the renamed function | **H1** |
| `memory/map/features/lexicon.md:139` — the Gaps bullet, contradicting line 58 of the same file | **H2** |
| `memory/builds/dClosedLexicon/spec/2026-08-16-spec-dClosedLexicon-1.md:456` — still rev-7 | **H3** |
| `tools/lexicon/selftest.py:82`, `:149` — comment headers still say "the reachability arm" | **L2** |

The commit message states the removed claim "was cited as coverage — in a docstring, a commit
message, a dossier and a charter bullet". Four were fixed. Four more were missed, and one of them is
the spec the build method treats as binding.

---

## BLOCKERS

### B1 — `resolve_import`'s importer-local precedence is applied to FULLY-QUALIFIED dotted imports, where the language grants the importer's directory no precedence at all

`tools/lexicon/lexicon.py:251` (the `local or hits` at `:252`; justification comment at `:247-248`)

```python
ext = ext_of(importer)
hits = [p for p in index.get(target.rsplit(".", 1)[-1], []) if ext_of(p) == ext]
local = [p for p in hits if (p.rsplit("/", 1)[0] if "/" in p else "") == here]
out.extend(local or hits)          # <-- `local or hits` DISCARDS every remote candidate
```

**Measured regression against `77d276d`.** Fixture: `LAYERS: src/pkg/consumer/* -> src/pkg/shared_core/*`;
`src/pkg/consumer/a.py` does `import pkg.shared_core.helper`; both `src/pkg/consumer/helper.py` and
`src/pkg/shared_core/helper.py` exist.

- HEAD: **no layer offender reported.**
- Control — delete only `src/pkg/consumer/helper.py`, change nothing else: `src/pkg/consumer/a.py:1:
  P3 layer: src/pkg/consumer/a.py->pkg.shared_core.helper — forbidden import direction
  src/pkg/consumer/* -> src/pkg/shared_core/*`.
- The pre-diff engine on the *original* fixture: exit 1, offender named.

So the importer-local sibling, and nothing else, is what suppresses the hit. The stem is `helper`,
`local` is non-empty, `local or hits` throws away the `shared_core` candidate, and the path-mirror
candidate `pkg/shared_core/helper` cannot match the `src/`-prefixed glob. This is the **src-layout
shape** — where the LAYERS glob carries a path prefix the namespace does not — which is precisely the
case the stem lookup was added for in round 1. `LAYER_OFFENDER_PIN="0"` goes back to being an
unfalsifiable zero for it: the exact class this build was opened to close.

The comment's justification — "which is what the language itself does" — is false twice over. Python
gives the importer's directory no precedence whatsoever over a fully-qualified absolute import; and
for the bare-stem `sys.path.insert(0, <other dir>)` shape the resolver was built around, the inserted
directory *precedes* the script's own.

**Why the selftest misses it:** the arm that covers precedence (`P3 green: an importer-local file WINS
over a same-stem file in the forbidden dir`) uses a **bare** stem — `import helper` — so nothing in
the suite distinguishes bare from dotted.

**Fix.** Apply local-wins only to a bare single-segment target, which is the only shape a flat
`sys.path` insert resolves that way, and keep both candidates rather than exempting dotted targets
wholesale:

```python
bare = "." not in target
local = [p for p in hits if (p.rsplit("/", 1)[0] if "/" in p else "") == here] if bare else []
out.extend(local or hits)
```

Verified: this reds the fixture above and leaves the suite at 48/48.

**Left-shift gate.** Add a selftest arm whose target is DOTTED and whose importer has a same-stem
local sibling, asserting the offender IS reported. Generalisable rule for this kit: **every resolver
narrowing needs an arm in both the shape it is meant to suppress and the shape it must not** — a
precedence rule armed only on the case it exists to allow is half a test.

---

### B2 — the `<dir>/*` nesting branch escapes the whole prefix, so any wildcard earlier in the pattern becomes a literal and nesting silently stops working

`tools/lexicon/lexicon.py:186`

```python
if pattern.endswith("/*"):
    prefix = re.escape(pattern[:-1])        # <-- re-escapes the RAW pattern; `*` -> `\*`
    return re.fullmatch(prefix + ".*", path) is not None
```

`re.escape` is applied to the raw pattern, so `src/*/internal/` becomes `src/\*/internal/` and the
branch demands a **literal asterisk** in the path. Only the depth-exact `re.fullmatch(rx, path)` at
`:183` survives, so nesting works exclusively for globs with no other wildcard.

Measured at unit level against the shipped file:

| call | HEAD | pre-diff |
|---|---|---|
| `_glob_match('tools/lexicon/sub/x.py', 'tools/*/*')` | **False** | True |
| `_glob_match('src/a/foo/b/c', 'src/*/foo/*')` | **False** | True |
| `_glob_match('apps/web/internal/deep/x.py', 'apps/*/internal/*')` | **False** | True |
| `_glob_match('apps/web/internal/top.py', 'apps/*/internal/*')` | True | True |

End to end in a scratch repo: under `LAYERS: apps/*/internal/* -> adapters/*`, the identical
`import adapters.db` is flagged in `apps/web/internal/top.py` and **passes green** in
`apps/web/internal/deep/x.py`. Same on the TO side: a rule `core/* -> apps/*/internal/*` misses a
stem resolving to `apps/web/internal/sub/deep_mod.py`. `?` is affected identically (`dir?/*`).

This is a **narrowing versus `77d276d`**, not a tightening of a sloppy match — the replaced
`re.match(rx, path)` was unanchored on the right, so `apps/[^/]*/internal/[^/]*` matched the nested
path as a prefix. And the failure is silent in the worst way: because the depth-exact files still
match, `scan_unselective_rules` stays quiet and the rule keeps reading as armed while whole subtrees
are invisible to it — a confident 0 over a partially unselectable population, which is the exact
failure class this kit exists to refuse.

It also falsifies the function's own new docstring at `:175`: "A `<dir>/*` pattern also matches
anything nested under `<dir>/`" is false whenever `<dir>` contains a glob character.

Gov's single rule (`tools/lexicon/* -> tools/codebase-map/*`) has no interior wildcard, so this ships
**dormant here and live to adopters**, whose LAYERS blocks are free text.

**Fix.** Translate once, reuse twice — never re-escape the raw pattern:

```python
def _rx(p: str) -> str:
    return re.escape(p).replace(r"\*", "[^/]*").replace(r"\?", "[^/]")

def _glob_match(path: str, pattern: str) -> bool:
    if re.fullmatch(_rx(pattern), path):
        return True
    if pattern.endswith("/*"):
        return re.fullmatch(_rx(pattern[:-1]) + ".*", path) is not None
    return False
```

**Left-shift gate.** A direct case table over `_glob_match` in `selftest.py` (it already imports
`lexicon as lex`), covering at minimum `('src/a/internal/deep/f.py','src/*/internal/*')->True`,
`('tools/lexicon/sub/x.py','tools/*/*')->True`, `('adapters/db_extra.py','adapters/db')->False`,
`('adapters/sub/db.py','adapters/*')->True`. Generalisable rule: **a pure predicate rewritten for
correctness gets a case table, not an end-to-end fixture** — an integration fixture only ever
exercises the one glob shape it happens to spell.

---

## HIGH

### H1 — the call-site comment above `scan_unselective_rules()` still states the removed reachability claim, verbatim

`tools/lexicon/lexicon.py:330-331`

```python
# The THIRD vacuity defence. Emptiness and dead extractors were armed from the start; a
# non-empty rule that cannot fire was not, and that is the gap a real rule shipped through.
for frm, to, why in scan_unselective_rules(layers, files, module_index):
```

Byte-identical to `HEAD~1` (it was at `:306`). The commit rewrote the module header and the function
docstring and left this untouched, so one file now gives two answers to one question **with the false
one nearest the code**. The docstring 60 lines above opens "This does NOT prove a rule is reachable.
It cannot."

The second clause is not merely stale, it is factually false of the surviving check: the real rule
that shipped through the gap — `.lexicon.conf:67`, `tools/lexicon/* -> tools/codebase-map/*` — has
both globs matching tracked files, so `scan_unselective_rules` is *silent* on it. Confirmed by the
live gate exiting 0 with that rule declared.

This is the highest-authority carrier of the over-claim this round exists to delete: a maintainer
reads the call site first, and the next one who trusts it re-acquires exactly the false confidence
that shipped the round-1 blocker.

**Fix.** Replace with what the call now does:

```python
# The emptiness half of the third vacuity defence: both globs must SELECT a tracked file.
# Reachability is deliberately NOT checked — see `scan_unselective_rules` for why a
# construction proof was removed rather than patched.
```

**Left-shift gate.** When a function is renamed to narrow its claim, grep the OLD name and the old
claim's distinctive nouns across the whole tree before committing — here, `reachab|UNMATCHABLE|cannot
fire`. Mechanisable: a `check-arms.py`-style predicate that reds when a retired refusal token
(`UNMATCHABLE`) survives anywhere outside `memory/builds/*/reviews/`.

---

### H2 — the map dossier's Gaps section still cites the removed arm, contradicting a paragraph the same commit rewrote 83 lines above

`memory/map/features/lexicon.md:139`

Line 58 (rewritten by this commit): *"Reachability itself is NOT proved, and the failed attempt is
the more useful record… It was removed rather than patched."*
Line 139 (untouched), closing the P3 resolver-gap bullet: *"…and P3 reported an unfalsifiable 0.
**That is why the reachability arm exists.**"*

The dossier is the governed record the codebase-map coverage gate holds for this kit, and Gaps is the
section a future reviewer reads to decide what P3 is *proved* to do. It now asserts both that
reachability is unproved and that an arm proves it, and the surviving half is the one an agent
grepping `reachab` in Gaps lands on.

**Fix.** End the bullet at "…and P3 reported an unfalsifiable 0." and point at the honest paragraph:
"That is the defect the resolver rewrite fixed; reachability itself is not proved — see the Design
section and `armed-but-unreachable-rule`."

**Left-shift gate.** The map dossier and the engine docstring are two carriers of one claim. Add the
dossier to the same grep sweep as H1, and treat "a dossier that contradicts itself" as a
`kit-dogfood-parity`-shaped check: any dossier asserting both X and not-X about the same mechanism is
a red, detectable by pinning the retired token.

---

### H3 — the spec of record is still rev-7 and its newest revision entry describes the removed mechanism as shipped; no rev-8 folds this round

`memory/builds/dClosedLexicon/spec/2026-08-16-spec-dClosedLexicon-1.md:456` (status header, `:3`)

> "S3 gains a THIRD vacuity arm: a non-empty rule that cannot fire is an `UNMATCHABLE LAYERS RULE`
> refusal, **proved by constructing the rule's own synthetic violation**."

`git log` on the spec shows its last touch is `77d276d`. `f917466` did not touch it; `grep rev-8`
returns nothing; `README.md:85` and `RUN.md:12` both still read rev-7. Both the refusal token and the
mechanism are gone from the engine — `UNMATCHABLE` now survives in the tree only in this spec line
and in review records.

`memory/guides/BUILD-METHOD.md:103` states the convention as a rule ("Fold fixes into the spec —
rev bump + §9 line"), `:43` requires the fold be a `rev-N` bump on the existing spec file, and the
predecessor commit `77d276d` did exactly that (+24 lines, rev-7). So the fold convention is
established and this round breaks it: `review-dClosedLexicon-4.md` was committed **in this same diff**
without being folded, and the build index, `RUN.md` and `LIVE.md` were regenerated while the document
they summarise was left over-claiming. The commit's own trailer asserts "Manifest re-audit: §B
re-verified, nothing stale. Delta: none."

Net effect: the four carriers that WERE corrected are outvoted by the one the build method treats as
authoritative.

**Fix.** Add a rev-8 entry folding review-4 — construction proof measured a tautology and REMOVED;
`scan_unmatchable_rules` → `scan_unselective_rules`, claiming emptiness only; `UNMATCHABLE` →
`UNSELECTIVE`; resolver scoped by extension with importer-local precedence; P2/CRLF/FROM-glob arms
added — bump the status header, regenerate the build index.

**Left-shift gate.** Mechanical and cheap: red when a commit adds a file under
`memory/builds/<slug>/reviews/` without bumping the `rev-` in that build's spec status header in the
same commit. That is a `check-memory-hygiene.sh` predicate, and it would have caught this diff.

---

## MEDIUM

### M1 — the `_glob_match` rewrite, the diff's largest surviving code change, carries no arm

`tools/lexicon/lexicon.py:174`

**Measured.** With `_glob_match`'s body restored verbatim to the pre-diff
`re.match(rx + "$", path) is not None or re.match(rx, path) is not None`:

```
$ python tools/lexicon/selftest.py
lexicon selftest OK — 48 arm(s)
```

…and the live gate over 472 tracked files exits 0 with the identical line. Nothing in the corpus or
the fixtures distinguishes anchored from unanchored. `grep` confirms `_glob_match` has no caller
outside `lexicon.py`, so no other leg could cover it either. The only LAYERS-glob arms
(`selftest.py:152-161`) use `core/* -> nowhere/at-all/*` and `nowhere/at-all/* -> adapters/*`,
neither of which exercises an interior wildcard or a non-glob prefix.

The anchoring is therefore a claim rather than a behaviour — the exact standard this same diff writes
down at `selftest.py:297` ("Reverting either one used to leave every arm green, which made the fix a
claim rather than a behaviour") and that `check-arms.py` enforces elsewhere in this repo. It is also
the direct reason B2 shipped.

**Fix / left-shift gate.** The case table in B2's fix covers this. Broader rule worth writing into the
kit: **`check-arms.py`'s discipline should extend to pure predicates, not just `fail` branches** — a
rewritten matcher with no differentiating fixture is the same defect shape.

### M2 — `scan_unselective_rules` quantifies the FROM glob over ALL tracked files, but P3 only extracts from non-`dark` files, so a dark-only rule passes while being incapable of firing

`tools/lexicon/lexicon.py:288` (extraction skip at `:344-345`)

**Reproduced.** `LAYERS: docs/* -> adapters/*`, `LANGS="py:python-ast:parser md::dark conf::dark"`,
tracked `docs/x.md` containing `import adapters.db`, tracked `adapters/db.py`:

```
lexicon OK — 3 tracked file(s); coverage: .conf=dark, .md=dark, .py=parser
EXIT=0
```

Both globs select a tracked file, so the check is silent — yet no import is ever extracted from
`docs/`, so `LAYER_OFFENDER_PIN="0"` is a measurement over a population that can never be non-empty.
That is the kit's own named dominant failure mode surviving *inside the check written to bound it*.

I considered refuting this as the documented "reachability is NOT proved" limitation and rejected the
refutation: that disclaimer's stated justification is that a construction-based proof is a tautology,
which does not apply here — the dark case is **decidable** with the same file list the function
already walks, needing only a mode filter. The shape is live for adopters: `scaffold_lexicon.py` seeds
every extension outside `{py, js}` as `dark`, and gov's own conf carries `md`, `sh`, `json`, `txt`,
`toml` dark. A rule over docs or scripts is inert while its pin reads a confident, unmovable 0.

**Fix.** Pass the extractable population in and test against it, with a distinct reason string:

```python
if not any(_glob_match(f, frm) for f in files if declared.get(ext_of(f), (None, "dark"))[1] != "dark"):
    bad.append((frm, to, f"the FROM glob {frm!r} selects only files declared `dark`, "
                          "from which no import is ever extracted"))
```

**Left-shift gate.** Arm it with the `docs/* -> adapters/*` fixture above. Generalisable: **whenever
two predicates quantify over "the corpus", assert they quantify over the SAME corpus** — this is the
second instance in this file (see M4), which makes it a pattern rather than a slip.

### M3 — the `UNSELECTIVE` remedy sentence is a half-applied edit and now asserts the inverse of its own point

`tools/lexicon/lexicon.py:333-335`

Verbatim from a live run:

```
lexicon: UNSELECTIVE LAYERS RULE `core/* -> adapters/*` — the TO glob 'adapters/*' matches no
tracked file. A rule whose globs fire is worse than no rule: it reports a confident 0 that no edit
can ever move.
```

`HEAD~1` read "A rule **that cannot** fire is worse than no rule". The edit swapped `that cannot` for
`whose globs` and left `fire` stranded, dropping the negation, so the one sentence explaining WHY the
run is red now says a *firing* rule is the problem — directly contradicting the `why` clause
immediately before it. `UNSELECTIVE` is a hard refusal on the merge bar and this sentence is its
entire remedy surface; as written, the obvious operator response (weaken or delete a firing rule) is
the wrong one.

**Fix.** `f"… A rule whose globs select nothing is worse than no rule: it reports a confident 0 …"`.

**Left-shift gate.** The arms at `selftest.py:155, 161` assert only the substring `UNSELECTIVE` plus a
non-zero exit. **Assert the full remedy sentence, not the refusal token** — operator-facing text is
the product for a gate whose only output is a refusal, and a token match cannot see a broken sentence.

### M4 — the `UNSELECTIVE` refusal fires on a rule that produced an offender in the SAME run, because the two predicates quantify over different domains

`tools/lexicon/lexicon.py:333` (domain gap at `:233`)

**Reproduced** with the kit's own fixture shape (`core/a.py: import adapters.db`, no `adapters/`
file), one run:

```
lexicon: layer offenders 1 over pin 0:
  core/a.py:3: P3 layer: core/a.py->adapters.db — forbidden import direction core/* -> adapters/*
lexicon: UNSELECTIVE LAYERS RULE `core/* -> adapters/*` — the TO glob 'adapters/*' matches no
tracked file. … it reports a confident 0 that no edit can ever move.
```

The count it just printed was **1**. `scan_unselective_rules` quantifies over tracked files;
`check_layer_violation` quantifies over `resolve_import` candidates, including the dotted mirror
appended unconditionally at `:233`, which is never membership-tested against the corpus. So an adopter
is told, in the same run, that a rule just caught an offender and that it can never move off zero.

**Fix.** Either membership-test the dotted-mirror candidate against `files` before matching it — which
matches `resolve_import`'s own docstring, "a rule can only forbid what it can locate" — or suppress
the `UNSELECTIVE` line for any rule that produced an offender in the same run. The first is better; the
second is a band-aid over the domain gap.

**Left-shift gate.** An arm asserting the two outputs are **mutually exclusive per rule**: no run may
print both an offender for rule R and `UNSELECTIVE` for rule R. That is a cheap, general invariant and
it directly encodes the domain-agreement rule from M2.

### M5 — the `_glob_match` docstring's worked example is refuted by the function it documents

`tools/lexicon/lexicon.py:174-181`

**Measured:** `_glob_match('tools/codebase-map//codebase-map/conf', 'tools/codebase-map/*')` returns
**True** under the new anchoring — the `/*` nesting branch accepts `/codebase-map/conf` after the
prefix, and `.` matches `/`. The pre-fix matcher returns True as well. So the docstring presents as
*the* defect an example whose verdict the rewrite did not change, under a header reading "Fully
ANCHORED" that implies it is now rejected. The cases the rewrite actually flips are wildcard-free
prefixes: `('adapters/db_extra.py','adapters/db')` goes True → False.

A maintainer reasoning about the anchoring from this example will be wrong, and it matters because
this docstring is now the kit's only written account of why the matcher was rewritten.

**Fix.** Use an example the new matcher genuinely rejects (`adapters/db_extra.py` no longer matches
`adapters/db`), or state plainly that the double-slash synthetic is still accepted by the nesting rule
and was not what made the removed arm tautological.

**Left-shift gate.** Same case table as B2 — **every example cited in a docstring as a behaviour
change should appear as a row in the arm table**, so a claim about a verdict is a tested verdict.

---

## LOW

### L1 — the new CRLF message arm asserts a substring the SUCCESS line also contains, so it cannot fail for the reason its label states

`tools/lexicon/selftest.py:313` (identical pre-existing defect at `:295`)

```python
check("scaffold: and still names it unratified rather than passing", "ratified" in out, out)
```

Verified by running the adopter, not by reading it: the green path prints
`lexicon-adopt OK — .lexicon.conf parses, ratified, N verb(s) declared` — which contains the asserted
substring. If `tr -d '\r'` is removed from `adopt-lexicon.sh`, `--check` exits 0 and prints that line,
and this arm stays green on the exact output it exists to exclude. Only its sibling
`r.returncode != 0` at `:311` catches the revert.

That makes it an exit-code arm wearing a message arm's label, in a file whose own preamble
(lines 6-9) states the law it breaks — "EVERY ARM ASSERTS A MESSAGE OR AN EFFECT, never an exit code
alone". It also inflates the advertised 48-arm count with an arm carrying no independent power.

**Fix.** Assert the refusal's own distinguishing text (e.g. ``"EMPTY `ratified` key" in out``), or
change the success line so it does not spell the word.

**Left-shift gate.** A meta-arm over `selftest.py` in the spirit of `check-arms.py`: **a message
assertion whose needle also appears on the green path is not an arm.** Mechanisable by running the
green path once and refusing any asserted substring found in its output.

### L2 — two selftest comment blocks still call the emptiness check "the reachability arm"

`tools/lexicon/selftest.py:82-84` and `:149-151`

The `check(...)` labels beneath them were correctly renamed to `P3 unselective` / `UNSELECTIVE`, but
`:149` still heads its block "The reachability arm — the third vacuity defence" and `:82` still says
"The reachability arm reds a rule whose globs select nothing … so they were unreachable too" — calling
one-sided fixtures "unreachable", which is the exact conflation this commit exists to retract. The
framing at `:150-151` ("neither tests whether a NON-EMPTY rule can ever FIRE") reads as a gap this
check closes.

**Fix.** Rename both to "the unselective arm" and drop the "can ever fire" / "unreachable" framing,
pointing at `scan_unselective_rules`'s docstring for what is deliberately not checked.

**Left-shift gate.** Covered by H1's grep sweep — `selftest.py` is the file a reviewer reads to learn
what is covered, so it belongs in the same retired-token scan.

### L3 — `scan_unselective_rules(layers, files, index)` no longer reads `index`

`tools/lexicon/lexicon.py:267` (call at `:332`)

Verified by reading the full body (`:286-292`): it iterates `layers` and calls `_glob_match` over
`files` only. The parameter was carried over unchanged from `scan_unmatchable_rules`, which *did*
consult the resolver index for the removed construction branch, and the call site still computes and
threads `module_index` in — advertising a dependency on the resolver that the check no longer has,
which is precisely the claim this commit was written to retract. No behavioural bug; real dead
plumbing that misleads.

**Fix.** Drop the parameter from the signature and the call.

**Left-shift gate.** An unused-parameter lint over `tools/**/*.py` would catch this class generally;
cheaper still, make it a review-checklist item that a removal commit must leave no parameter unread.

### L4 — the dossier's resolver-Gaps enumeration omits the two narrowings this commit adds

`memory/map/features/lexicon.md:132-139`

The bullet still lists only build-tool path aliases, `package.json` `exports` maps and re-export
barrels. The same-extension filter and importer-local-wins added at `lexicon.py:249-252` are recorded
**only in a source comment**. Both are genuinely permissive limits an adopter cannot discover from the
record: a `.js` bare specifier resolving to a `.ts`/`.jsx` file no longer resolves at all, and a
same-stem sibling shadows every other candidate including a genuine forbidden one (see B1). The
dossier is where this kit's Gaps claim is made, so an omission here is a record-vs-reality gap.

**Fix.** Extend the bullet: "The stem lookup is also scoped to the importer's own EXTENSION and yields
to an importer-local file exclusively, so a cross-extension bare specifier (`.js` → `.ts`) does not
resolve, and a same-stem sibling shadows a genuine forbidden target." (The same bullet's closing
sentence is H2 and must be fixed in the same edit.)

**Left-shift gate.** Fold into H3's proposed hygiene predicate: a commit that narrows a documented
capability must touch the dossier's Gaps section. Weaker but automatable — red when
`tools/<kit>/*.py` gains a filtering comprehension in a function the dossier names, without the
dossier changing in the same commit.

---

## Refuted (recorded, not raised)

Three raw findings did not survive the skeptic and are not counted above: a claimed false negative on
"a same-extension file in a third directory" (`local` is empty there, so `hits` is retained and the
candidate survives — no regression); a claim that removing the reachability proof left P3 with no
vacuity coverage at all (`NOT ARMED`, `DEAD PROBE` and the emptiness half all remain armed and were
verified firing); and a claim that the `dark` gap is the documented "reachability is NOT proved"
limitation (rejected — the dark case is decidable from the file list the function already walks; kept
as M2).

## What is right about this commit

Worth recording, because the removal is the correct call and the reasoning generalises. The decision
to **remove rather than patch** a vacuity check that was itself vacuous is right, and the stated
reason — that such a check is worse than none because it gets cited as coverage — is borne out by this
very review: four of its citations were cleaned, four survive, and the surviving ones are H1-H3 and
L2. `scan_unselective_rules`'s docstring is the strongest prose in the kit: it states what it is NOT
before what it is, names the measurement that killed the predecessor, and points at the gotcha class
for the general question. The gotcha file's rewrite is likewise honest. Four of the five new arms are
genuinely armed, verified by revert. The failure mode this round leaves behind is not dishonesty about
what was removed — it is that two unrelated "also fixed" changes rode along in a retraction commit
without arms, and both regressed.

## Suggested disposition

Fix B1 and B2 with arms before this lands; they are silent false negatives in the gate's selector and
resolver, both regressions against `77d276d`, and B2 ships live to adopters while lying dormant here.
H1-H3 and L2 are one coordinated sweep — the retired-token grep — and H3 additionally needs the rev-8
fold that this repo's own build method requires. M1's case table is the arm that would have caught B2
and should land with it.
