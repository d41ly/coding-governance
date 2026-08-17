# review-dClosedLexicon-4 — Tier-2 code review of the rev-7 FIX commit

**Serves:** diff-review TOOL-dClosedLexicon-1  <!-- inferred: the fix commit for the blocker raised against that unit -->

## Verdict: BLOCKED — 1 blocker, 2 high

**Subject:** commit `77d276d` ONLY — the fix for the blocker raised by
`reviews/2026-08-16-review-TOOL-dClosedLexicon-1-3.md`. Files judged: `tools/lexicon/lexicon.py`,
`tools/lexicon/selftest.py`, `tools/lexicon/scaffold_lexicon.py`, `tools/lexicon/adopt-lexicon.sh`,
`tools/lexicon/kit.toml`, `.gitattributes` · streams `tooling` · node d · 2026-08-16

**Binding spec:** `spec/2026-08-16-spec-dClosedLexicon-1.md` at rev-7. **Folds:**
`reviews/2026-08-16-review-TOOL-dClosedLexicon-1-3.md` — its findings are already folded into this commit
and are NOT re-raised here. The kit as a whole is out of scope; only the three parts of the fix are
judged.

## Review shape

| | |
|---|---|
| raw findings | 24 |
| confirmed (survived an adversarial skeptic) | 22 |
| refuted | 2 |
| unverified / outstanding | 0 |
| precision | 0.92 |

The 22 confirmed findings collapse to **12 distinct defects** — 1 blocker, 2 high, 5 medium, 4 low.
Four independent verifiers reproduced the reachability-scan tautology (ids 1, 11, 19, 22), four
reproduced the stem-collision false positive (ids 2, 7, 12, 20), three the unarmed CRLF fix
(ids 4, 9, 16) and three the unarmed reachability arm (ids 3, 8, 22). Duplicates are recorded under
each defect rather than repeated as rows; the convergence is itself signal.

**Scope note.** Security is out of scope (local developer gates, tracked files, no network surface,
no untrusted input). Lenses: CORRECTNESS, VACUITY, INTEGRATION SEAMS. The full bar is 60/60 green and
selftest reports 41 arms, so **every finding below explains why a green gate is wrong**, not merely
that something is unchecked.

**The headline.** The commit's own thesis is that `NOT ARMED` tests emptiness, `DEAD PROBE` tests
extractor population, and neither tests whether a non-empty rule can FIRE — so a third arm proves
reachability **by CONSTRUCTION**. That claim is repeated in the docstring, the commit message,
`memory/map/features/lexicon.md` and `AGENTS.md`. It is not true of the code that shipped: the
synthetic specifiers are derived from the target PATH and round-trip through the resolver's own
path-mirroring readings, so the check reduces to *"both globs match at least one tracked file"* — the
two branches immediately above it. Measured decisively: **monkeypatch `resolve_import` back to the
pre-fix body (`return [target.replace('.','/')]`) and `scan_unmatchable_rules` still certifies this
repo's real rule `tools/lexicon/* -> tools/codebase-map/*` REACHABLE.** The arm written to catch the
blocker cannot catch the blocker. Both halves of the fix are additionally unarmed: the reachability
loop's failure branch fires 0 times across all 41 arms, and reverting either half of the CRLF fix
leaves the suite 41/41 green.

Direct answers to the four questions the brief asked:

| Question | Answer |
|---|---|
| Can `resolve_import` produce a FALSE POSITIVE? | **Yes — two independent shapes.** Stem collision with no importer-local precedence (H1) and an untested dotted-namespace candidate matching an external package (M1). Both reproduced. |
| Can `scan_unmatchable_rules` pass vacuously? | **Yes, always** (B1). It also **wrongly reds a legitimate rule** whose TO glob carries an extension over a multi-dot basename (H2). |
| Does the CRLF fix close the inverted-refusal path on both sides? | The **behaviour** is fixed on both sides; the **arming** is absent on both sides (M3), and `.gitattributes` still documents the interaction as harmless (L4). |
| Are the new selftest arms capable of failing? | Three are not, for the reason they name: the reachability arm (M2), the CRLF arm (M3), and the P2 exemption removal has no arm at all (L1). The P3 red fixtures were additionally weakened by this same commit (M4). |

---

# BLOCKER

## B1 — `scan_unmatchable_rules` proves reachability against itself; the third vacuity arm cannot fail

**`tools/lexicon/lexicon.py:258`** (loop at 253-267) · ids 1, 11, 19, 22 · four independent
reproductions

The synthetics are derived from the target path `t`:

```python
for synthetic in (stem, t.rsplit(".", 1)[0].replace("/", "."), "./" + t):
    if check_layer_violation(probe_src, synthetic, [(frm, to)], index):
```

Synthetic #1 is `t`'s own basename stem, and `resolve_import`'s `index.get(target.rsplit('.',1)[-1])`
returns `t` itself, while `_glob_match(t, to)` is true **by construction** because `t` was selected
by `to` from the same file list that built `index`. Synthetic #2 round-trips dots back to slashes
through the namespace-as-path reading. So `reachable` is True whenever both globs are non-empty,
regardless of what the resolver can actually do.

**Measured, not inferred.**

- With `resolve_import` monkeypatched back to the pre-fix body, `scan_unmatchable_rules` on the real
  rule `tools/lexicon/* -> tools/codebase-map/*` returns `[]` — certified reachable — via the
  synthetic `tools.codebase-map..codebase-map.conf`, a string containing a hyphen and a double dot
  that **no import statement can spell**. It only "matches" because `target.replace('.','/')`
  mangles it to `tools/codebase-map//codebase-map/conf` and `_glob_match`'s unanchored second
  `re.match(rx, path)` (line 166) accepts it as a prefix hit.
- The certifying `probe_src` is `tools/lexicon/LEXICON.md` (`md::dark` — can never yield an import)
  and the certifying target is `tools/codebase-map/.codebase-map.conf.example` (`example::dark`).
  Neither side can participate in an import at all.
- Every non-empty glob pair probed returns `[]`: `memory/gotchas/* -> memory/guides/*` (both sides
  `dark`-declared markdown, no extractor can ever emit an import), `tools/memory-tree/* -> .githooks/*`,
  `memory/map/* -> tools/lexicon/*`.
- Brute force over the real corpus: 23,870 directory-pair rules, reachable 23,870, third
  `bad.append` 0. A 4,000-pair fuzz over both-sides-non-empty rules judged 32 bad, **0** via the
  construction loop.
- Branch instrumentation across all 41 selftest arms: the empty-TO early return fires **7** times,
  the `if not reachable` branch fires **0** times.

**Impact.** The mechanism this commit exists to add does not detect the defect class it was added
for. A future LAYERS rule — or a regression of the resolver — reporting an unfalsifiable
`LAYER_OFFENDER_PIN=0` goes green again, which is exactly the blocker review-3 raised. Meanwhile the
docstring (232-241), the commit message, `memory/map/features/lexicon.md` and the new `AGENTS.md`
bullet all assert reachability is proved BY CONSTRUCTION. This is a false coverage claim in a repo
whose stated law is that every fail branch carries a positive assertion naming its own failure text.

**Fix.** Make the proof non-self-fulfilling and language-aware:

1. Restrict `sources` and `targets` to files whose `LANGS` mode is **not `dark`** (pass `declared`
   in), so a rule spanning never-extracted trees reds instead of certifying.
2. Build each synthetic only in a shape a real extractor can emit for the target's declared language
   — for `python-ast`, a bare stem that is a valid identifier, and the dotted form **only** when
   every path segment is a valid identifier (reject the hyphen case rather than mirroring it).
3. Require the match to come from a candidate that is an **exact tracked path equal to `t`**, i.e.
   require `t in resolve_import(synthetic, probe_src, index)`, not merely "something glob-matching
   `to`".
4. Drop the `'./' + t` synthetic (see H2) or rebuild it as a real relative specifier.
5. Anchor `_glob_match`'s prefix fallback (line 166) to a `/` boundary —
   `re.match(rx + '(/.*)?$', path)` — so a mangled path cannot satisfy a glob by prefix. This is what
   let the mangled `tools/codebase-map//codebase-map/conf` match at all.

**Left-shift gate.** Add a selftest arm that **cripples the matcher and asserts the scan reds**:
monkeypatch `resolve_import` to the pre-fix `[target.replace('.','/')]` body and assert
`scan_unmatchable_rules` reports the production-shape rule (`pkg/consumer/* -> pkg/shared-core/*`)
as `non-empty but UNREACHABLE`. That single arm is the falsifiability test the whole defence needs,
and it fails today. Generalise it as a house rule in `memory/gotchas/armed-but-unreachable-rule.md`:
**a reachability proof whose witness is derived from the thing being proved is not a proof** — the
witness must be constructible from the language's own grammar, never from the corpus lookup that is
guaranteed to hit.

---

# HIGH

## H1 — `resolve_import`'s stem lookup has no importer-local precedence and indexes non-code files, so compliant imports red

**`tools/lexicon/lexicon.py:216`** (index built at 169-185; violation at 220-228) · ids 2, 7, 12, 20
· four independent reproductions

```python
out.extend(index.get(target.rsplit(".", 1)[-1], []))
```

returns **every** tracked file sharing that basename, and `check_layer_violation` reds if **any**
candidate matches `to`. There is no preference for the importer's own directory — yet the flat
`sys.path`-insert idiom the comment at 213-215 explicitly targets resolves to the sibling.

**Reproduced, three shapes.**

- `pkg/consumer/a.py` containing `import shared_thing`, with **both** `pkg/consumer/shared_thing.py`
  and `pkg/shared-core/shared_thing.py` tracked, reds
  `P3 layer ... forbidden import direction pkg/consumer/* -> pkg/shared-core/*` — while CPython
  resolves to the local sibling. Same for `core/db.py` vs `adapters/db.py` end-to-end through the
  installed engine.
- `import json` (stdlib) reds once `pkg/shared-core/json.py` exists.
- The index is **extension-blind** (`build_module_index` indexes ALL tracked files): in this repo,
  `check_layer_violation('tools/lexicon/lexicon.py', 'kit', …)` fires via
  `tools/codebase-map/kit.toml`, `'README'` via `README.md`, and `'selftest'` via
  `tools/codebase-map/selftest.py`. 14 colliding stems exist in the live corpus.
- `_python_defs` drops the level of an `ast.ImportFrom`, so an ordinary package-relative
  `from .config import X` yields target `config` and reds whenever any same-stem file exists under
  the forbidden dir.

**Impact.** False reds on a compliant tree, on a merge-bar leg (`tools/gate-legs.json:543`). Not live
in gov today (no `tools/lexicon` import stem collides with `tools/codebase-map`), but reachable on a
plausible edit precisely because this kit **ports** files from codebase-map: a port keeping its source
name (`tools/lexicon/map_lib.py` + `import map_lib`) reds while resolving to its own sibling. The
integrity consequence is second-order: the only escape is a waiver keyed `f"{rel}->{target}"`
(line 361), which then **permanently silences a genuine later violation of the same target from that
file**, and the stale-waiver check cannot notice. Same-basename modules across layers (`config.py`,
`models.py`, `db.py`) are the normal shape in exactly the layered repos this rule targets, so an
adopter's `LAYER_OFFENDER_PIN` measures noise — the very pin this fix exists to make trustworthy.
Undeclared: the dossier's Gaps (`memory/map/features/lexicon.md:127-134`) name only false NEGATIVES —
aliases, exports maps, barrels.

**Fix.** Rank candidates by proximity instead of unioning them. Before consulting the corpus-wide
stem index, check the importer's own directory (and its package ancestors) for a file with that stem
— if one exists, that is the resolution and the stem index must not be consulted. Skip the stem
lookup entirely when the target is in `sys.stdlib_module_names`. Restrict the index to extensions
whose `LANGS` mode is `parser`/`probe`, so `.toml` and `.md` basenames can never be import targets.
Where a stem is genuinely ambiguous across two layers, report the ambiguity as its own named problem
rather than silently selecting the forbidden reading. Fix `_python_defs` to honour `ImportFrom.level`.

**Left-shift gate.** The existing green arm (`selftest.py:137-142`) uses non-colliding stems
(`unrelated_thing` vs `shared_thing`), which is why the suite cannot see this. Add the **collision**
fixture as an arm: `pkg/consumer/a.py` + `pkg/consumer/shared_thing.py` +
`pkg/shared-core/shared_thing.py`, asserting green. Add a second asserting `import json` is green
with `pkg/shared-core/json.py` present, and a third asserting `import kit` cannot resolve to
`kit.toml`. Generalise: **a green arm whose fixture avoids the collision the resolver must handle
certifies coverage the production tree does not have** — the same lesson the commit already recorded
for the `import adapters.db` fixture, applied one level down.

## H2 — the `'./' + t` synthetic is a repo-root path with a relative prefix, so it re-anchors under the importer's dir and reds legitimate rules

**`tools/lexicon/lexicon.py:258`** (relative branch at 196-208) · id 6

`t` is already a repo-ROOT path; prefixing `./` sends it through the relative branch, which
re-anchors it under the importer's directory:
`resolve_import('./pkg/types/index.d.ts', 'pkg/app/a.js')` returns
`['pkg/app/pkg/types/index.d.ts']` — unmatchable by construction. The other two synthetics also miss
on a multi-dot basename: the stem of `index.d.ts` is `index.d` (both `build_module_index:183` and
line 257 `rsplit` on the LAST dot), so the lookup keys on `d`; and the dotted form
`pkg.types.index.d -> pkg/types/index/d` fails an extension-bearing TO glob.

**Reproduced.** Rule `pkg/app/* -> pkg/types/*.ts` over `['pkg/app/a.js','pkg/types/index.d.ts']`
reds with *"the rule is non-empty but UNREACHABLE"* — yet
`check_layer_violation('pkg/app/a.js', '../types/index.d.ts', layers, index)` returns that rule: a
real import **does** violate it. Same red for `('src/*','src/*.test.js')` over
`['src/y.js','src/x.test.js']` while `'./x.test.js'` is correctly caught.

**Impact.** A false UNREACHABLE red on a legitimate, genuinely reachable rule, and it is
**unwaivable and merge-bar-blocking**: `problems` sets `exit_code = 1` unconditionally
(lexicon.py:427-428), only `offenders` have waiver registries, and `lexicon naming predicates` is a
gate leg. The adopter's only escape is deleting the rule. Any TO glob carrying an extension over
multi-dot basenames hits this: `*.d.ts`, `*.test.js`, `*.min.js`, `*.config.json`. Non-extension TO
globs escape only because `_glob_match`'s prefix fallback rescues them — i.e. the same leak that
powers B1 is what hides the blast radius of H2.

**Fix.** Build the specifier the way an importer writes it:

```python
rel = os.path.relpath(t, start=os.path.dirname(probe_src)).replace(os.sep, "/")
spec = rel if rel.startswith("..") else "./" + rel
```

and split the basename on the FIRST dot when deriving a stem for multi-dot names, or derive the stem
set `{index, index.d}` and try both.

**Left-shift gate.** Add a green arm on a JS/TS rule with an extension-bearing TO glob
(`pkg/app/* -> pkg/types/*.ts` over a real `index.d.ts`) asserting the scan does **not** report
UNMATCHABLE, paired with a red arm asserting the real `../types/index.d.ts` import IS caught. Any
predicate that both flags offenders and certifies reachability needs a **consistency arm**: for one
fixture, assert the two verdicts agree (see M1 — they demonstrably do not today).

---

# MEDIUM

## M1 — the dotted-namespace candidate is never membership-tested, so one run can flag an offender against a rule it simultaneously calls unmatchable

**`tools/lexicon/lexicon.py:211`** · ids 13, 21

`out.append(target.replace(".", "/"))` emits a candidate with no check that it corresponds to a
tracked path, contradicting `resolve_import`'s own documented invariant at line 190 (*"a rule can only
forbid what it can locate"*). Meanwhile `scan_unmatchable_rules` quantifies over tracked files. The
two disagree.

**Reproduced with the kit's own fixture** (`selftest.py:111`): `{core/a.py: 'import adapters.db'}`
under `LAYERS: core/* -> adapters/*` with no `adapters/` file tracked prints **both**

```
core/a.py:1: P3 layer: core/a.py->adapters.db — forbidden import direction core/* -> adapters/*
UNMATCHABLE LAYERS RULE core/* -> adapters/* — the TO glob 'adapters/*' matches no tracked file
```

Exactly one of those can be true. Practically this also hard-reds the prophylactic use of P3 —
forbidding imports into a layer that does not exist yet, or that a refactor has just emptied — which
is where the rule is most valuable and demonstrably still fires (`src/core/* -> src/adapters/*` reds
on a corpus with no `src/core/`). It is also a genuine false positive on external packages whose
top-level name coincides with a repo directory glob.

**Fix.** Keep the dotted reading only when `target.replace('.','/')` (with a declared source
extension appended, or as a package-dir prefix) corresponds to a tracked path. That removes the
external-package false positive and makes the offender scan and the reachability scan quantify over
the same population. For the empty-TO case, report the rule as *unfalsifiable-today* rather than
*unmatchable*, keeping the hard refusal for the construction branch.

**Left-shift gate.** Add a cross-predicate consistency arm: for every fixture in the suite, assert
that no run emits both an offender naming a rule and an `UNMATCHABLE` line naming the same rule. That
is a two-line loop over the captured output and it catches this whole class, not just this instance.

## M2 — the "P3 unreachable" arm exercises only the empty-TO-glob branch; the construction loop ships with zero arms

**`tools/lexicon/selftest.py:147`** (assertions 149-150) · ids 3, 8, 22

The fixture declares `core/* -> nowhere/at-all/*`, which exits at the `no tracked file` branch
(lexicon.py:250-251) before `probe_src` or any synthetic is built.
`scan_unmatchable_rules([('core/*','nowhere/at-all/*')], ['core/a.py','.lexicon.conf'], index)`
returns *"the TO glob 'nowhere/at-all/*' matches no tracked file"*. The assertion checks only the
shared prefix `UNMATCHABLE`, emitted for all three reasons, so it passes on the emptiness reason
while the comment at 144-146 presents it as *"the reachability arm — the third vacuity defence"*.

**Proved mechanically, twice.** Branch instrumentation across the 41 arms: emptiness branch 7 hits,
construction branch 0. And neutering only the construction red (`if not reachable:` → `if False:`,
leaving both emptiness branches intact) still prints `lexicon selftest OK — 41 arm(s)`.

**Impact.** The distinctive half of the third vacuity defence is unarmed, contrary to this repo's own
meta-gate rule that every `fail` branch carries a positive assertion naming its own failure text. A
reader of the 41-arm count sees the reachability defence as covered when only the trivial half is.
This is precisely how B1 and H2 shipped green.

**Fix.** Add a fixture whose two globs BOTH select tracked files but that no writable import can
satisfy — e.g. `LANGS` declaring `md::dark` with a rule `docs/* -> assets/*` over only `.md` and
`.png` files — and assert the specific wording `non-empty but UNREACHABLE`. Rename the existing arm
to say what it actually proves (*"a TO glob matching no tracked file"*) so the two branches are
separately visible.

**Left-shift gate.** Make the three refusal reasons carry **distinct, separately asserted** message
tokens (`UNMATCHABLE:FROM-EMPTY`, `UNMATCHABLE:TO-EMPTY`, `UNMATCHABLE:UNREACHABLE`) and extend
`tools/memory-tree/check-arms.py`'s rule to this kit: an assertion matching only a shared prefix does
not arm the branch beneath it. That converts "the arm passed for a different reason" from a review
finding into a gate finding.

## M3 — neither half of the CRLF fix is armed; reverting either leaves 41/41 green

**`tools/lexicon/selftest.py:246`** · `tools/lexicon/scaffold_lexicon.py:128` ·
`tools/lexicon/adopt-lexicon.sh:77` · ids 4, 9, 16 · three independent reproductions

Measured on this Windows node, three runs:

1. Revert only `newline=""` in `scaffold_lexicon.py:129` → the seed is written with 43 CRLFs, and
   `python tools/lexicon/selftest.py` still prints `lexicon selftest OK — 41 arm(s)`, exit 0. The
   new `tr -d '\r'` in `adopt-lexicon.sh:77` masks it from the one arm that observed it.
2. Revert **both** halves → exactly one arm fails: *"scaffold: --check REDS on the unratified seed"*,
   i.e. the unratified-seed refusal inverts. That is the live bug this commit fixed, and it is
   observable only when both halves are gone.
3. Revert only `tr -d '\r'` → 41/41 green again, because the writer now emits LF. No fixture ever
   feeds a CRLF conf to `adopt --check`.

`conf_text = (root / ".lexicon.conf").read_text(...)` at line 246 does universal-newline translation
and `load_conf` uses `splitlines`, so **no assertion in the file can observe the bytes**. The comment
at `scaffold_lexicon.py:124-128` — *"Caught by the scaffold arm in selftest.py"* — is therefore false
as the arm now stands.

**Impact.** The control at stake is the unratified-seed refusal: the only gate stopping an uncurated
verb table reaching the merge bar. It silently inverted once; it can invert again with no arm to
notice. The reader half matters independently of the scaffolder: an adopter whose checkout smudges
`.lexicon.conf` to CRLF (`core.autocrlf`, no `.gitattributes` pin in their tree) hits the reader path
the writer fix does not cover.

**Fix.** Two byte-level arms. (1) In the scaffold block:
`check("scaffold: writes LF, never CRLF", b"\r" not in (root / ".lexicon.conf").read_bytes(), …)` —
`read_text` cannot express this. (2) A case that writes a conf with explicit CRLF line endings and
`ratified=""`, runs `bash tools/lexicon/adopt-lexicon.sh --check`, and asserts non-zero exit naming
`ratified`; that arm fails the moment `tr -d '\r'` is dropped.

**Left-shift gate.** Generalise as a house rule: **a fix whose subject is bytes must be asserted on
bytes** — `read_text`, `splitlines` and `$(…)` all normalise the thing under test. Worth a line in
`memory/gotchas/` beside the existing CRLF entries, and worth a `check-arms.py`-style predicate that
flags a comment claiming "caught by <arm>" where the named arm makes no assertion over the changed
surface.

## M4 — the new reachability scan contaminates three pre-existing RED fixtures, weakening the P1 arm to exit-code-only

**`tools/lexicon/selftest.py:92`** (also `:99`, `:111`; assertion at `:93`) · id 15

`LAYER_SIDES` (added at line 85) was spread into the **green** arms only. `BASE_CONF` declares
`core/* -> adapters/*`, and the red fixtures at lines 92, 99 and 111 stage no `adapters/` file, so
each now also emits `UNMATCHABLE LAYERS RULE core/* -> adapters/*` — a refusal unrelated to the
predicate the arm names.

The material regression is line 93, which asserts `code != 0` **alone**. Verified: neutralising P1 by
adding `frobnicate` to the VERBS table still exits 1, printing only the UNMATCHABLE line — so the arm
passes with the predicate it names entirely gone. That is the exit-code-only / red-for-an-unrelated-
reason shape this file's own docstring (lines 6-9) forbids by name. Mitigating but not disqualifying:
the sibling arms at 94-96 assert message text and the `:99`/`:112` arms assert `ThingManager` /
`P3 layer`, so suite-level coverage of P1 survives.

**Fix.** Spread `**LAYER_SIDES` into the red fixtures at 92, 99 and 111 (the empty-LAYERS fixture at
119 correctly needs none), and strengthen line 93 to assert `'P1 verb' in out`.

**Left-shift gate.** Add a predicate to the run-gates canary or `check-arms.py` covering this kit:
**no arm in a `*selftest.py` may assert `code != 0` without also asserting a message token**. This
commit introduced the violation into a file whose docstring already forbids it, which is exactly the
gap a mechanical check closes and a code comment does not.

## M5 — `kit.toml`'s hand-enumerated engine list removes automatic coverage of new kit files, and nothing gates the enumeration against the directory it mirrors

**`tools/lexicon/kit.toml:16`** · id 17

`govkit apply` special-cases `include = "**"` (`govkit.py:802-803`) to pool every tracked file under
`home`; the enumeration bypasses that pool. `govkit selfcheck`'s completeness arm
(`govkit.py:496-520`) computes `surface_paths` with glob `tools/*`, collapsing deeper paths to their
depth-1 segment, and `entry_members` (`govkit.py:165-178`) claims the whole `tools/lexicon`
directory because the entry is not `kind = "flat"`. So a future `tools/lexicon/newthing.py` is
already claimed, reds nothing, and is **silently never deployed to any adopter**. Arm 3 checks
declared sources exist — one direction only; no arm asserts the reverse. The list is complete today
(12 tracked files = 9 engine + 3 seed); the defect is the ungated drift.

The trade-off the comment records is real — an `include = "**"` engine rule would clobber the
adopter's waiver registries before the project-owned rule is reached — so the fix must keep the split
without giving up derivation.

**Fix.** Keep `include = "**"` for the engine rule and give it an `exclude` naming the three waiver
files (or make the seed rule's members subtract from the pool), so completeness stays derived.
Failing that, add a `govkit selfcheck` arm asserting that every tracked file under a
directory-shaped entry's `home` is named by exactly one of its file rules.

**Left-shift gate.** That selfcheck arm IS the left-shift, and it belongs in `govkit`, not in this
kit: it is the declaration-vs-reality class govkit exists to close, one granularity finer than it
currently checks. Every directory-shaped entry in the registry benefits, not just `lexicon`.

---

# LOW

## L1 — the P2 `name != suf` exemption removal has no arm

**`tools/lexicon/selftest.py:100`** (behaviour at `lexicon.py:351`) · id 10

Proved by regression injection: restoring `if name.endswith(suf) and name != suf:` — exactly the
exemption the comment at 348-350 says was deliberately removed — still prints
`lexicon selftest OK — 41 arm(s)`. The only P2 red fixture is `class ThingManager` (line 99), which
reded before the change too; the only P2 green fixture is an imported/parameter `ThingManager`; the
js sentinel is `class ThingManager`. No arm defines a type named **exactly** `Manager`. The case the
commit calls *"the PUREST instance of a type nobody scoped"* is the one case asserted only in prose.

**Fix.** Add:
`code, out = run_case({'core/a.py': 'def build_x():\n    pass\n\n\nclass Manager:\n    pass\n', **LAYER_SIDES}, BASE_CONF)`
with `check('P2 red: a type named EXACTLY the banned suffix reds', code != 0 and 'P2 suffix' in out and 'Manager' in out, out)`.

**Left-shift gate.** House rule worth a line in the review protocol: **a diff that removes a
condition from a predicate must add the arm that distinguishes the two behaviours** — the reviewer
question is "which fixture changes verdict?", and if the answer is "none", the change is unasserted.

## L2 — `--measure` has no caller, no documentation outside its own module, and no arm

**`tools/lexicon/lexicon.py:383`** (branch 383-392, allow-list 438-439) · id 18

`grep -rn measure tools/lexicon/` finds `--measure` only inside `lexicon.py`. `README.md`'s Adopting
block (57-62) lists `--scaffold`, `--check`, the bare gate and `--list` but not `--measure`;
`LEXICON.md` never mentions `lexicon.py` at all; `adopt-lexicon.sh` never invokes it; no gate leg runs
it; no selftest arm passes any argv. It was added as the fix for review-3's M4, which asked for both
a documented path and an arm asserting idempotence — neither shipped. Contrast
`corpus_ids.py --measure`, cited in the README, `HYGIENE.md` and the conf.

**Fix.** One arm asserting `--measure` exits 0 and prints all three `*_OFFENDER_PIN="<n>"` lines for
a known fixture, plus a citation in `tools/lexicon/README.md` and in the `.lexicon.conf` pin comment
the way `.memory-tree.conf` cites its own.

**Left-shift gate.** Extend the codebase-map coverage inventory (or a small `kit.toml` predicate) to
**every verb in an engine's argv allow-list**: a verb with no caller, no doc citation and no arm reds
until one of the three exists. That makes undiscoverable plumbing a gate finding, not a review one.

## L3 — the scaffolded conf still says MEASURED over two hardcoded zeros and never names `--measure`

**`tools/lexicon/scaffold_lexicon.py:100`** (literals at 103-104) · id 23

`lexicon.py:378-382` names the defect explicitly (*"two of these three shipped as a hardcoded `0`
under a comment that called them MEASURED"*), but the emitting code is unchanged.
`SUFFIX_OFFENDER_PIN="0"` is asserted, never measured — the scaffold tallies `types_seen` (line 78)
but never tests a name against the eight `BANNED_SUFFIXES` it seeds.

**Reproduced end to end.** Scaffolding a repo containing `class ThingManager` and `class
WidgetHandler` emits `# MEASURED against this corpus at scaffold time` above two literal zeros; after
curating only `ratified` and a LAYERS row, the adopter's first gate run reds
`lexicon: suffix offenders 2 over pin 0`, while `--measure` on the same tree prints
`SUFFIX_OFFENDER_PIN="2"`. `'--measure' in conf` is `False`; it appears in no adopter-facing file.

**Fix.** Change the emitted comment to
``# PROVISIONAL — re-run `python tools/lexicon/lexicon.py --measure` after curating the table and paste what it prints``,
and either compute the suffix pin at scaffold time from the types already extracted, or say in the
emitted text that it is not measured.

**Left-shift gate.** An arm asserting the scaffolded conf contains no `MEASURED` claim over a literal
the scaffold never computed — mechanically: for each `*_OFFENDER_PIN` the scaffold emits, assert
either that the value is derived from a counter in the same function or that its comment says
PROVISIONAL. Cheap, and it generalises to every seed-writing kit here.

## L4 — `.gitattributes` still calls the CRLF interaction "Harmless today", which this commit disproves

**`.gitattributes:131`** (rationale at 126-130) · id 24

The pin rationale reads *"…the anchor stops matching. Harmless today because the check only asks
whether the value is non-empty"* — and non-emptiness is precisely the mechanism through which an
empty `ratified=""` becomes the non-empty `"\r` that **inverts** the refusal. The same commit's
`adopt-lexicon.sh:74-76` and `scaffold_lexicon.py:124-128` both now record that inversion.
`git show --name-only HEAD` confirms `.gitattributes` was not touched.

**Impact.** Two answers to one question, with the wrong one in the file a maintainer consults to
decide whether the `eol=lf` pin is load-bearing. The note is also copy-shaped for an adopter's
`.gitattributes`, where the `tr` half may be absent.

**Fix.** Rewrite the last paragraph to state the observed inversion and that BOTH halves are required
— the pin so the committed bytes are LF, and the `tr -d '\r'` so a CRLF working copy cannot invert
the refusal — matching the wording already in the two source files.

**Left-shift gate.** This is the "two answers to one question" class the drift-audit kit already
owns. Add a `drift_signals.py` signal: when a commit adds a comment describing a failure mode, any
other tracked file whose comment calls the same interaction harmless is flagged. Cheaper approximation
that would have caught this one: a signal that reds when a `.gitattributes` rationale paragraph names
a file whose handling changed in the same commit and the rationale did not.

---

## What would have caught this commit before the bar

Ranked by leverage:

1. **Falsifiability arm for every new refusal.** B1, M2 and M3 are one shape: a defence shipped with
   no proof it can fire. The cheapest general control is a suite-level requirement that each new
   refusal branch carries an arm that **breaks the mechanism and asserts the red** — for B1 that is
   monkeypatching the pre-fix resolver; for M3 it is reverting each half in turn. `check-arms.py`
   already encodes this law for the memory-tree engine; it does not reach this kit.
2. **Distinct message tokens per refusal reason.** M2 and M4 both turn on an assertion matching a
   shared prefix or nothing at all. Distinct tokens plus a "no exit-code-only assertion" predicate
   converts both into gate findings.
3. **Cross-predicate consistency arm.** M1's contradiction (offender + UNMATCHABLE for the same rule
   in one run) is a two-line check over captured output and it covers the whole class.
4. **Collision fixtures for any resolver.** H1 and H2 both hide behind fixtures easier than
   production — the exact lesson `memory/gotchas/armed-but-unreachable-rule.md` records for the
   `import adapters.db` case, not yet applied to the resolver's own arms.
5. **A govkit completeness arm at file granularity** (M5), which pays off across every
   directory-shaped entry in the registry.
