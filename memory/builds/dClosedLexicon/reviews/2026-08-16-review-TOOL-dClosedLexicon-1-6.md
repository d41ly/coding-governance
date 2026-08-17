# review-dClosedLexicon-6 — Tier-2 code review of the two P3 helpers

**Serves:** diff-review TOOL-dClosedLexicon-1  <!-- inferred: two helpers within the same unit's commit -->

## Verdict: BLOCKED — 1 blocker, 4 high

**Subject:** commit `ab71eee` ONLY, and within it ONLY two functions plus the case tables that now
pin them: `tools/lexicon/lexicon.py::_glob_match` (with its new `_build_glob_rx` helper) and
`tools/lexicon/lexicon.py::resolve_import`, plus `GLOB_CASES` and the `resolve_import` rows in
`tools/lexicon/selftest.py`. · streams `tooling` · node d · 2026-08-16

**Explicitly OUT of scope, by owner instruction:** the rest of the kit, the playbook edits,
`check-placeholders`, the chassis, and the records. Four prior review rounds covered those and their
findings are folded. This is the owner-sanctioned final pass on the two functions that produced every
P3 defect across three rounds.

**Binding spec:** `spec/2026-08-16-spec-dClosedLexicon-1.md`. **Folds:** review-1 (namespace-vs-path
glob), review-4 (the tautological reachability proof), review-5 B1/B2 (the `<dir>/*` raw-escape and
importer-local precedence on dotted imports). All four are FIXED and none is re-raised.

## Review shape

| | |
|---|---|
| raw findings | 22 |
| confirmed (survived an adversarial skeptic) | 19 |
| refuted | 3 |
| unverified / outstanding | 0 |
| precision | 0.86 |

The 19 confirmed findings collapse to **10 distinct defects** — 1 blocker, 4 high, 3 medium, 2 low.
Convergence is heavy and is itself signal: four independent verifiers reproduced the unarmed `?`
conversion (ids 4, 8, 12, 18), three the relative-branch `..` underflow (ids 3, 16, 21), three the
unarmed relative index rescue (ids 5, 9, 22), two the `**` collapse (ids 2, 13) and two the vacuous
`json` row (ids 10, 14). Duplicates are recorded under each defect rather than repeated as rows.

**Every finding below was re-measured by me during write-up**, against the shipped engine in this
worktree, not carried over on the verifiers' word. Two carried impact claims that did not survive
that re-measurement; both are corrected in place and neither refutes its finding.

**Scope note.** Security is out of scope (local developer gate, tracked files, no network surface).
Lenses: CORRECTNESS, VACUITY, ARM-CAPABILITY. The full bar is 60/60 and `selftest.py` reports 64
arms, so **every finding explains why a green gate is wrong**, not merely that something is
unchecked.

**The headline.** Both named fixes are CORRECT: I reverted each and watched its named row red
(`revert-B2` reds `apps/a/internal/deep/x.py vs apps/*/internal/*`; `revert-B1` reds the
FULLY-QUALIFIED dotted row), so the commit's central claim holds and the case-table idea is the right
one. But the fixes are not COMPLETE, and the B1 fix in particular **traded one false negative for a
false negative and two false positives**. `from <package> import <name>` — the commonest Python
crossing spelling there is — resolves to nothing at all (B1 below), so the same example the commit
fixes in one spelling stays blind in the adjacent one. And the dotted branch it added extends
candidates with **no directory scoping whatsoever**, which is a measured regression against `365be1c`
in both languages. Meanwhile the tables leave three of the helpers' branches asserted by nothing —
including the `?` half of the very conversion this commit single-sourced.

---

## Answers to the four questions asked

### (1) Are the two fixes correct and complete, or is there a third input shape either still gets wrong?

Correct, not complete. I walked every shape named in the brief plus the ones they implied. Results,
all measured against the shipped engine:

| shape probed | verdict |
|---|---|
| multiple wildcards (`apps/*/internal/*`, depth 1 and 2) | **FIXED** — this is B2, and it holds |
| trailing `/*` on a pattern that is itself just `*` (`*/*`, `/*`) | correct — `*/*` matches `a/b/c` via the nesting branch, `/*` builds `/.*` and does not match a rootless path |
| `?` wildcard | implemented correctly, **asserted nowhere** — M2 |
| empty pattern `""` | correct — matches only the empty path |
| a target that is a single dot (`require('.')`) | benign — resolves to the importer's own directory (plus a same-named sibling); a rule cannot forbid a file its own directory |
| a target starting with multiple dots (`...shared_core.helper`) | **unreachable, and that is the bug** — see below |
| a relative specifier escaping above the repo root | **BROKEN** — M1, clamped into the tree, fabricates a violation |
| a dotted target whose last segment is empty (`pkg.`) | benign in the dotted branch (the extension filter kills the dotfile stems `index[""]` holds); the same empty key IS live and harmful in the relative branch — M1 |
| **`from <pkg> import <name>`** | **BROKEN — B1**, the blocker |
| **a dotted target whose namespace matches no directory** (`concurrent.futures`) | **BROKEN — H1**, a regression this commit introduced |
| **a dotted JS/npm package name** (`lodash.debounce`) | **BROKEN — H2**, a regression this commit introduced |
| a relative specifier sharing a prefix with a sibling directory (`../shared` vs `shared_core/`) | **BROKEN — H3**, the exact defect class the glob fix removed, unfixed 40 lines away |
| `**` in a LAYERS glob | **BROKEN — H4**, silently collapses to one segment |

On the multiple-dots row: `from ...shared_core import helper` never reaches `resolve_import` in the
shape it was written. `_python_defs` (`lexicon.py:137-139`) records `node.module` alone, discarding
`node.level`, so an explicit-relative Python import is handed to the resolver as if it were absolute,
and `from . import x` (module `None`) is dropped entirely. That is the same root cause as B1 — the
Python extractor throws away the half of the import statement that carries the namespace — so it is
folded into B1's fix rather than filed separately.

### (2) Do the case-table rows actually PIN the two defects?

**Yes for the two blocker rows, and I re-verified both rather than taking the commit message's word.**
I then ran the same revert discipline over every other branch these two helpers have. Measured, in an
isolated copy of the kit, one mutation at a time against all 64 arms:

| mutation (the defect it restores) | arms red | the row that catches it |
|---|---|---|
| nesting branch escapes the RAW pattern (**B2**) | 1 | `glob: apps/a/internal/deep/x.py vs apps/*/internal/*` (selftest.py:273) |
| `re.fullmatch` → `re.match` (**round-1 anchoring**) | 1 | `glob: tools/lexicon-extra/a.py vs tools/lexicon*` (selftest.py:279) |
| local precedence applied to dotted targets (**B1**) | 1 | the FULLY-QUALIFIED dotted row (selftest.py:312) |
| drop the extension filter at `lexicon.py:267` | 2 | the `notes` row (selftest.py:318) + one end-to-end fixture |
| **drop the `?` conversion** (`lexicon.py:187`) | **0 — ALL GREEN** | none exists — **M2** |
| **delete the relative index rescue** (`lexicon.py:246`) | **0 — ALL GREEN** | none exists — **L1** |

So four of six branches are genuinely pinned and two are not. The two unpinned ones are exactly the
condition this commit's own message says it exists to end: "reverting the `_glob_match` rewrite
verbatim left all 48 fixture arms green."

### (3) Is any row's EXPECTATION wrong?

**No.** I checked all sixteen rows — ten `GLOB_CASES` plus six `resolve_import` — against real glob
and real import semantics, and every expected value is right, including the three the author records
as having been corrected. The recorded non-row (the doubled-slash path) is the correct call and the
reasoning for it is sound: `git ls-files` cannot emit one, and the only thing that ever did was the
deleted synthetic.

Two rows are nonetheless defective in a different way, and both are recorded below: one asserts a
property the implementation does not have while killing no mutant (**M3**), and one is introduced by
a comment that names the wrong row as its arm (**L2**). Neither is a wrong expected VALUE.

### (4) Is the table vacuous anywhere?

**Yes, in three places.** The `json` row (selftest.py:323) kills none of the six mutants above — it
passes under every realistic implementation of both scoping rules, because no corpus file shares that
stem, so `index.get("json")` is empty regardless (**M3**). The `?` half of `_build_glob_rx` is
asserted by no row in either table (**M2**). And the relative branch's index rescue is asserted by no
row, because the one relative row uses the extension-carrying spelling that `out.append(cand)` alone
already satisfies (**L1**). Beyond the tables, three of `resolve_import`'s behaviours have no NEGATIVE
arm at all for the dotted branch, which is why H1 could land green.

---

## Findings

### B1 [blocker] — `from <package> import <name>` resolves to nothing, so the commonest Python crossing is missed

**`tools/lexicon/lexicon.py:267`** (with root cause at `tools/lexicon/lexicon.py:137-139`)

`resolve_import` resolves only the LAST dotted segment as a module STEM against
`build_module_index`, whose keys are FILE stems. When the last segment names a DIRECTORY — which is
what `from <package> import <name>` always hands it — `hits` is empty, and the only surviving
candidate is the path-mirror `pkg/shared_core`, which can never match a `<dir>/*` TO glob. The table's
own row at selftest.py:284 pins exactly that: the bare directory is not a member of `<dir>/*`.

`_python_defs` records `node.module` alone for an `ImportFrom` and discards the imported NAME, so
this is not an edge case — it is the dominant spelling of a Python layer crossing.

**Measured end-to-end** in a throwaway repo. Rule `pkg/consumer/* -> pkg/shared_core/*`, importer
`pkg/consumer/a.py`, target file `pkg/shared_core/helper.py` present:

| spelling | result |
|---|---|
| `from pkg.shared_core import helper` | **exit 0, `lexicon OK`** |
| `from shared_core import helper` | **exit 0** |
| `import pkg.shared_core.helper` | exit 1, P3 layer offender |
| `from pkg.shared_core.helper import thing` | exit 1 |

Both globs match tracked files, so `scan_unselective_rules` stays silent and no backstop fires. The
B1 fix therefore closed one spelling of its own example and left the adjacent one blind: **P3's zero
is unfalsifiable again, on the shape this build exists to prevent.** Review-3 had already OBSERVED
`from adapters import db` escaping, as part of what B1's fix was meant to close, and it is still open.
This is core language semantics, not one of the declared Gaps (`memory/map/features/lexicon.md` names
only build-tool aliases, `package.json` exports and re-export barrels, and asserts the resolver
"covers the shapes this tree and its adopters actually write").

**Fix.** Resolve a target that names a PACKAGE as well as one that names a module. Key a second index
on directory paths (or pass the tracked file list into `resolve_import`) and, for any target, extend
candidates with every tracked file whose PARENT DIRECTORY ends with `target.replace('.', '/')`,
matched on a segment boundary. Do it alongside H1's namespace-consistency scoping, not instead of it —
the two touch the same lines and an unscoped directory index would widen H1. While in
`_python_defs`, stop discarding `node.level` and the imported names, which also closes the
explicit-relative-import gap noted in Q1.

**Left-shift gate.** Two case-table rows beside the B1 row, both expecting True and both red today:
`_check_reaches("pkg.shared_core")` and its bare sibling `_check_reaches("shared_core")`. Add an
end-to-end fixture spelling the crossing as `from <pkg> import <name>`, so the resolver and the
extractor are both covered — the extractor half is invisible to a case table.

---

### H1 [high] — the new dotted branch drops ALL directory scoping, not just importer-local precedence

**`tools/lexicon/lexicon.py:275-276`**

`if "." in target: out.extend(hits)` accepts every same-stem candidate ANYWHERE in the tree, with no
requirement that any part of the dotted namespace relate to the candidate's path. The comment
directly above (lines 255-260) names this exact class as the reason the scopings exist: an unscoped
stem lookup "reds a perfectly local import as a layer crossing… and the only escape would be a waiver
that then permanently silences the genuine violation it was hiding."

**Measured** against the selftest's own `RI_INDEX`, importer `src/pkg/consumer/a.py`:

```
resolve_import('thirdparty.helper') -> ['thirdparty/helper', 'src/pkg/consumer/helper.py', 'src/pkg/shared_core/helper.py']
resolve_import('concurrent.helper') -> ['concurrent/helper',  'src/pkg/consumer/helper.py', 'src/pkg/shared_core/helper.py']
```

A package that exists nowhere in the corpus is reported as REACHING `src/pkg/shared_core/*`.
**Verified as a regression introduced by this commit**, by running the `365be1c` copy of the module
side by side: files `src/core/x.py`, `src/core/futures.py`, `src/adapters/futures.py`;
`import concurrent.futures` from `src/core/x.py` gives VIOLATION=False at `365be1c` and VIOLATION=True
at `ab71eee`. Any dotted stdlib or third-party import whose last segment collides with a tracked
filename inside a forbidden directory now reds. `LAYER_OFFENDER_PIN` is shrink-only, so a phantom
offender gets pinned in permanently. **No case-table row asserts the negative direction for the dotted
branch** — the only dotted row is the positive B1 assertion — so the table cannot catch it.

Not firing in this repo today only because `tools/lexicon/*.py` contains no dotted imports at all;
that zero is luck, not scoping (`tools/lexicon/selftest.py` and `tools/codebase-map/selftest.py`
already share a stem).

**Fix.** Keep the branch, scope it by NAMESPACE CONSISTENCY instead of by stem alone: for a dotted
target, require the candidate's extension-stripped path to end with `target.replace('.', '/')` on a
segment boundary. **Prototyped and verified:** `pkg.shared_core.helper` still yields
`['src/pkg/shared_core/helper.py']` so the B1 row stays green, while `concurrent.futures` yields `[]`.

**Left-shift gate.** The missing negative row, which reds today:
`check("resolve: a dotted target whose namespace matches no directory does not resolve",
not _check_reaches("thirdparty.helper"), ...)`. Rule of thumb for this table generally: every
resolver branch needs a row in BOTH directions — the four branches that survived mutation all have
one, and the branch that regressed had only the positive.

---

### H2 [high] — `"." in target` is a Python namespace rule applied to every language, so dotted npm names lose local precedence

**`tools/lexicon/lexicon.py:275`**

The B1 fix decides "fully-qualified" from the presence of a dot. That is true of Python and false of
JS/TS, where `lodash.debounce`, `chart.js` and `core-js/features/array.at` are ordinary bare package
names. `js` is a first-class declared language here (`LANGS` carries `js:js-regex:probe`, and
`RI_INDEX` itself contains `web/consumer/a.js` and `web/shared/thing.js`).

**Measured regression, with the parent-commit contrast run directly.** Index
`{web/consumer/a.js, web/consumer/debounce.js, web/shared/debounce.js}`:

| commit | `resolve_import('lodash.debounce', 'web/consumer/a.js')` | rule `web/consumer/* -> web/shared/*` |
|---|---|---|
| `365be1c` | `['lodash/debounce', 'web/consumer/debounce.js']` | None |
| `ab71eee` | `['lodash/debounce', 'web/consumer/debounce.js', 'web/shared/debounce.js']` | **VIOLATION** |

The bare contrast target `debounce` still returns None today, isolating the cause to the `"." in
target` test. This is a FALSE POSITIVE on an npm import that touches nothing in the tree, and the only
escape is a text-keyed waiver on that import text — which then permanently silences the genuine
crossing spelled the same way. That is precisely the outcome the comment at lines 256-260 exists to
prevent. Not reachable in this repo's own corpus (one Python-only rule), so the live gate stays green
— it had to be found by reading, not by running.

**Fix.** Decide "fully-qualified" from EVIDENCE rather than from a dot. This form was verified in a
scratch copy — all 64 arms stay green, the B1 row included, the live gate still exits 0, and
`lodash.debounce` stops reaching:

```python
pref = target.rsplit(".", 1)[0].replace(".", "/") if "." in target else ""
if pref and any(("/" + pref + "/") in ("/" + h) for h in hits):
    out.extend(hits)
else:
    ...local precedence...
```

Note this is the same predicate H1 needs; implement it once and both close. It does NOT close B1,
which needs the directory index.

**Left-shift gate.** A case-table row with a `.js` importer and a dotted npm-style specifier, so the
language distinction is pinned rather than assumed: `not _check_reaches("lodash.debounce",
"web/consumer/a.js", "web/shared/*")`. More broadly, `RI_INDEX` already carries both languages —
every scoping row should exist in a `.py` and a `.js` variant, since every scoping rule in this
function is a language claim.

---

### H3 [high] — the relative branch's `startswith(cand)` is a boundary-free prefix test: the same defect class the glob fix just removed

**`tools/lexicon/lexicon.py:246`**

`out.extend(p for p in index.get(...) if p.startswith(cand))` is a raw prefix test with no path
boundary — exactly what `re.match` was doing before the anchoring fix, and exactly what GLOB row 279
now pins. It survives unfixed and unrowed in the sibling helper 40 lines away.

**Measured**, corpus `['web/consumer/a.js', 'web/shared.js', 'web/shared_core/shared.js']`:

```
resolve_import('../shared', 'web/consumer/a.js', idx)
  -> ['web/shared', 'web/shared.js', 'web/shared_core/shared.js']
check_layer_violation('web/consumer/a.js', '../shared', [('web/consumer/*','web/shared_core/*')], idx)
  -> ('web/consumer/*', 'web/shared_core/*')
```

The specifier denotes `web/shared.js`; a legal import reds against a rule about
`web/shared_core/`. The branch also skips the extension scoping the dotted branch documents as rule
#1 — with `web/shared/thing.md` present, `../shared/thing` from a `.js` importer resolves to the `.md`.
The waiver key is `f"{rel}->{target}"` (lexicon.py:412), so the escape is a waiver on
`web/consumer/a.js->../shared`, which then silences a real future crossing by that same
importer/target pair. Recorded nowhere: no prior review in `memory/builds/dClosedLexicon/` and no line
in `memory/map/features/lexicon.md` mentions it.

**Fix.** Require a path boundary the way `_glob_match` now does, and apply the same extension filter
the dotted branch uses:

```python
if p == cand or p.startswith(cand + "/") or p.rsplit(".", 1)[0] == cand:
```

**Left-shift gate.** Two rows in the resolve table: `../shared` must NOT reach `web/shared_core/*`,
and `../shared/thing` from a `.js` importer must not denote a `.md`. The generalizable gate is worth
more than either: the anchoring defect has now appeared in two functions, so **a boundary-free
`startswith`/`re.match` over a repo path is a recurring bug class** and belongs in
`tools/memory-tree/gotchas.py`, where `--for-diff` will raise it on any future diff touching a path
comparison in this kit.

---

### H4 [high] — `**` in a LAYERS glob silently collapses to a single segment, and nothing rejects or documents it

**`tools/lexicon/lexicon.py:187` and `:203-204`**

`_build_glob_rx` maps `**` to `[^/]*[^/]*`, which is identical to a single `[^/]*`. And a `<dir>/**`
pattern never reaches the nesting branch at all, because `"tools/lexicon/**".endswith("/*")` is False.
So `<dir>/**` selects strictly LESS than `<dir>/*` — the opposite of what `**` means in every glob
dialect.

**Measured, both halves:**

```
_build_glob_rx('apps/**/consumer/*')                      -> 'apps/[^/]*[^/]*/consumer/[^/]*'
_glob_match('apps/one/two/consumer/a.py', 'apps/**/consumer/*')  -> False
_glob_match('tools/lexicon/deep/a.py', 'tools/lexicon/**')       -> False   (vs 'tools/lexicon/*' -> True)
```

End-to-end: corpus `apps/one/consumer/shallow.py` + `apps/one/two/consumer/a.py` (the crossing) +
`pkg/internal/secret.py`; rule `apps/**/consumer/* -> pkg/internal/*` exits 0 with `lexicon OK`, while
the same corpus under `apps/*/*/consumer/*` reds. **`scan_unselective_rules` cannot catch it**,
because the depth-1 matches keep the rule selective — so the adopter gets an armed, selective rule
reporting a zero no edit can move. That is the unfalsifiable-zero class this predicate exists to
prevent, arriving through the glob dialect instead of the resolver.

Nothing warns: the conf reader (`lexicon_conf.py:108-116`) validates only that both sides are
non-empty, and no glob dialect is documented anywhere in the kit — not `README.md`, not `LEXICON.md`
(whose only LAYERS example uses `*`), not `scaffold_lexicon.py`'s seed comment, not the dossier.
`**` is the idiomatic spelling in gitignore, tsconfig and eslint, so this is what an adopter will
reach for. Latent for gov itself, which uses `*` — but this is a shipped opt-in kit whose adopters
hand-author LAYERS rules.

**Fix.** Fail closed on the ambiguity, per the kit's own "a declared refusal, never a silent skip"
law: raise `ConfError` from `lexicon_conf.py`'s LAYERS reader on any glob containing `**`, naming the
supported dialect (`*` = one segment, trailing `/*` = that directory and everything under it, `?` =
one character). If recursion is wanted instead, convert `**/` to `(?:[^/]+/)*` and a trailing `**` to
`.*` before escaping the rest. Document the dialect in `README.md` and `LEXICON.md` either way.

**Left-shift gate.** `GLOB_CASES` rows for `apps/**/internal/*` at depth 1 and depth 2 and for
`tools/**` at depth 2 — pinning the refusal if you refuse, the match if you implement. The deeper
gate: **the supported dialect is a contract with the adopter and belongs in one table** that the
conf reader validates against and the case table enumerates, so a third wildcard cannot arrive
undocumented.

---

### M1 [medium] — a `..` that escapes above the repo root is silently clamped back in, fabricating an in-repo violation

**`tools/lexicon/lexicon.py:240-241`** (`if stack: stack.pop()`)

The walk drops excess ascents instead of recording them, so a specifier that leaves the repo becomes
a root-relative in-repo path. The function's own docstring (line 228) says empty means EXTERNAL and
external is not a violation — which is the correct answer here.

**Measured, both halves.** `web/consumer/a.js` importing `'../../../../pkg/internal/secret.js'` —
four levels up, definitively outside the repo — resolves to `pkg/internal/secret.js` and is reported
as `web/consumer/* -> pkg/internal/*`, byte-identically to the honest `'../../pkg/internal/secret.js'`
control. And when the stack empties entirely, `cand` is `""`, so the `startswith("")` guard admits
everything `index[""]` holds: over this repo's real corpus, `resolve_import('../..',
'tools/workflows/x.js', idx)` returns `['', '.gitattributes', '.gitignore']` — two root dotfiles
offered as what a JavaScript import denotes, with no extension filter to stop them.

This is a false POSITIVE against a shrink-only pin of 0, so it reds the bar for an import the rule
does not govern. **Correction to one verifier's impact claim:** the assertion that the waiver escape
is permanent does NOT survive — `stale = [w for w in waivers if w not in seen_texts]` (lexicon.py:452)
reds a waiver whose text is gone, so a text-keyed waiver does go stale. The defect itself is real,
reachable through the live js probe, and mechanically confirmed; only that consequence was overstated.

**Fix.** Track the underflow and `return []` when the walk went above the root, since an out-of-repo
specifier is external and unresolvable. Guard the index rescue with `if cand and ...` so an empty
candidate never reaches the corpus lookup. Both are one line each and independent of H3's boundary
fix, though they touch adjacent lines.

**Left-shift gate.** Two rows: `_check_reaches('../../../../pkg/internal/secret.js',
'web/consumer/a.js', 'pkg/internal/*')` expecting False, and one asserting `resolve_import('../..',
...)` denotes nothing. The class-level gate: **`resolve_import` returns a candidate list that only
ever moves a verdict**, so any candidate it cannot justify is a bug in one direction or the other —
worth stating in the docstring as the branch-writing rule.

---

### M2 [medium] — the `?` half of `_build_glob_rx` is asserted by no row in either table

**`tools/lexicon/selftest.py:265-285`** (subject: `tools/lexicon/lexicon.py:187`)

**Mutation-verified by me:** deleting `.replace(r"\?", "[^/]")` leaves the selftest at
`lexicon selftest OK — 64 arm(s)`, exit 0, and the live leg at `lexicon OK`, exit 0. No row in
`GLOB_CASES` contains a `?`, no fixture conf uses one, and `.lexicon.conf`'s single LAYERS rule uses
`*` only. The line is live code, not a no-op: `_build_glob_rx('src/a?/x.py')` yields
`src/a[^/]/x\.py`.

This is the exact condition the commit exists to end — "reverting the `_glob_match` rewrite verbatim
left all 48 fixture arms green" — reproduced on the same helper, in the commit that added the table.
Four independent verifiers found it, which is why it is medium rather than low despite the narrow
blast radius. The consequence of losing the conversion is a MISLEADING red, not a silent zero: a `?`
degrading to a literal makes both glob sides select nothing, so `scan_unselective_rules` reds
UNSELECTIVE and points the adopter at their conf rather than at the matcher.

**Fix / left-shift gate** (same thing here). Three rows, all passing today and all red under the
deletion:

```python
("tools/lexicon/a.py",  "tools/lexicon/?.py", True,  "a ? matches exactly one character"),
("tools/lexicon/ab.py", "tools/lexicon/?.py", False, "and never two"),
("apps/a/deep/x.py",    "apps/?/*",           True,  "? is converted in the nesting branch too"),
```

The third also re-pins the shared-conversion claim through the nesting branch (verified: it reds under
the B2 revert). If `?` support is not wanted, deleting it is equally cheap — but then H4's refusal
must name the dialect without it.

---

### M3 [medium] — the "unresolvable/external target" row asserts a property the resolver does not have, and kills no mutant

**`tools/lexicon/selftest.py:323`**

`not _check_reaches("json")` passes only because no corpus file shares the stem `json`, so
`index.get("json")` is empty under EVERY implementation of both scoping rules. **Verified against all
six mutants above: this row reds under none of them.** Only an always-True `_glob_match` reds it — so
it grades the glob helper, not the resolver it is filed under.

Worse, its label is false of the code. Add `src/pkg/shared_core/json.py` to `RI_INDEX` and
`_check_reaches('json')` returns True: the stdlib `import json` resolves into the forbidden layer.
That half is arguably by design — lines 252-254 say the stem lookup exists precisely to catch flat
`sys.path` imports and cannot tell a stdlib name from a repo module — so the load-bearing part is the
vacuity. A row whose label certifies a safety property the implementation lacks, in the table the
module docstring says P3's correctness rests on, is the same **cited-as-coverage** shape that the
removed reachability proof had and that `scan_unselective_rules`'s docstring was rewritten to stop.

**Fix.** Rename it to what it actually asserts — "a stem absent from the index denotes nothing" — and
add the honest row beside it: `not _check_reaches("thirdparty.helper")`, which reds today and pins
H1. Record the stdlib-collision case as a known false-positive shape in the dossier's Gaps, the same
status aliases and barrels already have.

**Left-shift gate.** The general rule this row breaks is worth writing into the table's header
comment: **a row that cannot fail under any plausible mutation of the function it is filed under is
not an arm.** The cheap mechanical version is the sweep I ran here — six one-line mutants, one run
each — and it is worth keeping as a scripted `--mutate` mode beside the selftest, since it is what
distinguished the four real arms from the two vacuous ones in under a minute.

---

### L1 [low] — the relative branch's index rescue is asserted by no row

**`tools/lexicon/selftest.py:320-322`** (subject: `tools/lexicon/lexicon.py:246`)

**Mutation-verified:** deleting line 246 entirely leaves all 64 arms green. The sole relative row uses
`../shared/thing.js` — extension included — so `cand` is already `web/shared/thing.js` and
`out.append(cand)` at line 245 satisfies the row before the corpus lookup runs. The
extensionless spelling `../shared/thing`, the dominant TS/ESM shape and the only one that needs the
line, appears nowhere; nor does anything exercise the `startswith(cand)` scoping (which is separately
wrong — H3).

**Correction to the verifiers' impact wording:** for a `<dir>/*` TO glob the extensionless spelling
still reaches via the path-mirror candidate, so the line only changes a verdict for a more specific TO
glob. Measured: `../shared/thing` under `web/shared/*.js` reaches on the shipped engine and does not
with the line deleted. The arming gap is real; its reach is narrower than stated.

**Fix / left-shift gate.** Change the row's target to the extensionless `"../shared/thing"` against a
TO glob that only the real file matches — `_check_reaches("../shared/thing", "web/consumer/a.js",
"web/shared/*.js")`, True today and False with line 246 removed — and add a negative row for the
scoping H3 fixes: put `other/thing.js` in `RI_INDEX` and assert it is not offered.

---

### L2 [low] — the ANCHORING comment names a row that cannot catch the defect it claims to pin

**`tools/lexicon/selftest.py:275-279`**

The comment says "this is the pair that catches it". **Measured:** restoring the unanchored matcher
(`re.fullmatch` → `re.match` at lexicon.py:201) reds exactly ONE arm — `tools/lexicon-extra/a.py vs
tools/lexicon*` at line 279. The line-277 row stays green, because the unanchored regex still requires
the literal `tools/lexicon/` prefix that `tools/lexicon-extra/` lacks; the line-278 row expects True
and passes under both implementations. I checked the alternative readings too: mutating the nesting
branch alone is a semantic no-op (the trailing `.*` makes `fullmatch` and `match` equivalent there, 64/64
stays green), and mutating both branches still reds only line 279.

Row 277 earns its place against a different variant — a nesting branch that strips `/*` instead of `*`
— so this is a comment defect, not a row defect. But a comment that names a non-firing row as an arm
is how the round-2 tautology got cited as coverage, and an author trimming on its word could delete
line 279 as redundant with 277 and silently un-arm the round-1 defect.

**Fix.** Name each row's own defect: line 279 pins anchoring; line 277 is a FROM-boundary control that
pins nothing on its own. Optionally add a nesting-shaped anchoring row that does fire, e.g.
`("tools/lexicon/xy/z", "tools/lexicon/x*", False)` — verified to red under the unanchored mutation.

**Left-shift gate.** The mutation sweep from M3 makes this class mechanical: a row-to-defect claim in
a comment is checkable by running the mutant and reading which arm reds. Every "this row pins X"
comment in the table should have been written by observing the red, not by reasoning about it — that
is the discipline the commit applied to its two blocker rows and did not extend to the rest.

---

## What is right about this commit

Worth saying plainly, because the finding count above understates it:

- **Both named fixes are real and correctly reasoned.** B2's diagnosis — two conversions that
  disagreed, one escaping the raw pattern — is exactly right, and single-sourcing them is the right
  repair rather than patching the second site. B1's diagnosis of language semantics is right for
  Python.
- **Verification by revert is the right standard**, and it was actually performed: I reproduced both
  reverts and both named rows red. That is a stronger claim than any prior round in this build made.
- **The case-table idea is correct and was overdue.** "A fixture exercises a PATH through the engine;
  a case table exercises the FUNCTION" is the right diagnosis of why three rounds of end-to-end arms
  missed four defects, and four of the six branches I mutated are now genuinely pinned. The remaining
  work is finishing the table, not rethinking it.
- **The recorded non-row** — the doubled-slash path, written down with its reason rather than silently
  dropped — is exemplary, and so is recording that the table caught two of its author's own wrong
  expectations on the day it was written.

The gap is that the tables were written to pin the two KNOWN defects rather than to cover the two
functions' branches, so the branches that had never yet failed stayed unarmed — and one of those,
the newly added dotted branch, regressed in the same commit.

---

## Summary

| # | sev | file:line | defect |
|---|---|---|---|
| B1 | blocker | `tools/lexicon/lexicon.py:267` | `from <pkg> import <name>` resolves to nothing — the commonest Python crossing is missed |
| H1 | high | `tools/lexicon/lexicon.py:275` | the dotted branch drops ALL directory scoping — phantom crossings, regression vs `365be1c` |
| H2 | high | `tools/lexicon/lexicon.py:275` | `"." in target` is a Python rule applied to JS — dotted npm names lose local precedence, regression vs `365be1c` |
| H3 | high | `tools/lexicon/lexicon.py:246` | boundary-free `startswith` prefix test — the defect class the glob fix just removed, unfixed in the sibling branch |
| H4 | high | `tools/lexicon/lexicon.py:187,203` | `**` silently collapses to one segment; `<dir>/**` selects less than `<dir>/*`; nothing rejects or documents it |
| M1 | medium | `tools/lexicon/lexicon.py:240` | a `..` escaping the repo root is clamped back in, fabricating an in-repo violation |
| M2 | medium | `tools/lexicon/selftest.py:265` | the `?` conversion is asserted by no row — deleting it leaves 64/64 green |
| M3 | medium | `tools/lexicon/selftest.py:323` | the "external target" row kills no mutant and its label certifies a property the code lacks |
| L1 | low | `tools/lexicon/selftest.py:320` | the relative index rescue is asserted by no row — deleting it leaves 64/64 green |
| L2 | low | `tools/lexicon/selftest.py:275` | the ANCHORING comment names a row that cannot catch the defect it claims to pin |

**Recommended order.** H1 and H2 are one fix (namespace consistency, verified to keep all 64 arms
green) and should land first — they are regressions this commit introduced and they red an adopter's
bar today. B1 lands next and touches the same lines plus `_python_defs`. H3 and M1 are the relative
branch and are best done together. H4 is a conf-reader refusal and is independent. M2, M3, L1 and L2
are table work and are cheap; the mutation sweep in M3's gate is what turns "add rows" into "add rows
that provably arm something", and it found two vacuous rows and one wrong comment here in one pass.

**The bar to close on.** Not "60/60 and 64 arms" — that is true of the tree as reviewed. Close on:
every branch of both helpers has a row in both directions, and each row has been observed to red under
a mutation of the branch it names.
