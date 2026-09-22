**Serves:** spec-audit TOOL-dPromptedSeam-1 TOOL-dPromptedSeam-2

## Verdict: BLOCKED

# Spec audit — TOOL-dPromptedSeam-1 (rev-3) · TOOL-dPromptedSeam-2 (rev-2)

**Verdict: BLOCKED · 6 blockers.** Node d, 2026-08-25, branch `branch/prompted-seam-9a4c11`, base `ee6554c3`, specs read at `332d2e01`.

Three lenses fanned out over both specs; 46 raw findings went to a skeptic that defaulted to refuted, 44 survived, and this pass folds them into 26 distinct defects (the duplicate ids below are the same defect raised independently by two lenses, which is itself a signal about which ones are real).

The refutation of rev-1 is not re-litigated. Both specs are honest about what rev-1 got wrong. What they are not yet honest about is what rev-2/rev-3 now cost: **-1 specs a conditional mechanism that does not exist in the renderer it names, and -2 specs a predicate one rule short of the behaviour its own acceptance criteria demand.** Code written from either lands wrong, so this is BLOCKED rather than CLEAN WITH FIXES.

Two structural notes before the findings. Every blocker in -1 traces to one decision nobody has made — whether the new rung is conditional — and resolving that one question retires four findings. Every blocker in -2 traces to §4 being measured over a population the shipped code never sees.

---

## TOOL-dPromptedSeam-1 — blockers

### B1 · §2 S3 · §4 D3 · §10 · §3 · §9 — the "existing conditional-block mechanism" is not in this renderer
*(raised as U1 twice and P1; §3 facet as C1; §9 facet as C3)*

`render_skill()` in `tools/lexicon/adopt-lexicon.sh:95-123` is six literal `${out//{{KEY}}/…}` substitutions — VERBS_TABLE, SUGGEST_CLI, BRIEF_CLI, GATE_CLI, CONF, KIT_VERSION — over two inputs, `.lexicon.conf` via `lexicon_conf.py --print-rows` and `KIT_LEXICON_VERSION` grepped out of `lexicon.py`. There is no fence parser in the file. The `kit:`/`when:` dropper is `OPEN_RE`/`CLOSE_RE`/`remove_fenced` in `tools/playbook/render_playbook.py`, which renders a **charter** against `.governance/deploy.toml` and never sees `SKILL.template.md`. So §10's "The renderer's conditional-block mechanism — REUSED as-is for S3. No new conditional machinery" is false for the artifact S1 edits, and D3 welds two engines into one sentence.

It fails silently in the obvious direction: add `<!-- kit:codebase-map -->` to the template and the comments render verbatim into every adopter's `SKILL.md`, because `check_skill`'s leftover guard is `grep -o '{{[A-Z_]*}}'` and `cmp -s` compares a render against a render carrying the same fences. `tools/lexicon/kit.toml`'s declared `placeholders` array will not red either — nothing in `govkit.py` reads that key.

§3 then forbids both possible replacements by name ("No new conf key, timeout, **discovery logic** or outcome taxonomy") and D3 forecloses the third ("nothing decides anything at run time"), so a builder must violate a stated section whichever way they go. §9's "Tier drops to 1 because rev-2 changes no code path" is false if S3 survives — the rendered Skill is a byte-compared shared contract, which the charter's Tier-1 definition excludes.

**Fix — pick one and write it into S3, §3, §4 D3, §9 and §10:**
- (a) **New machinery.** Teach `render_skill()` a fence pass, extend `check_skill`'s leftover scan to catch an unresolved fence (the `{{}}` grep cannot), add the new placeholder to `kit.toml`, and restate §10 as new code with its own staged-failure arm and §9 as "changes the renderer's substitution path".
- (b) **Build-time presence check.** A condition the lexicon renderer can evaluate alone — a sibling `reuse_lookup.py` under `KITREL`'s parent, or `.codebase-map.conf` — strike "discovery logic" from §3 and delete D3's "not a runtime check" claim.
- (c) **Drop S3.** Ship the rung unconditionally with wording that survives a map-less adopter. This is the branch P6 below argues for, and it makes §9's Tier-1 claim true on its own evidence.

### B2 · §6 AC3 — names a renderer, an input and a target mode that do not exist
*(raised as U2 twice; renderer-mismatch facet as C2, leg facet as C4)*

AC3: "When the renderer runs against a fixture target whose `deploy.toml` declares no `codebase-map`…". `adopt-lexicon.sh` accepts only `--scaffold|--check|--render`, takes **no target**, derives its root from `git rev-parse --show-toplevel`, and never reads `deploy.toml` (zero hits across the whole kit). AC1 names that script; AC3 names `render_playbook.py`. No single renderer satisfies both. The only fixture harness in the kit (`selftest.py:948`) git-inits a sandbox and copies **only** `tools/lexicon/`, so neither half of AC3 has a subject either. And an adopter who takes lexicon without the playbook kit has no `deploy.toml` at all — the declared condition source is absent in exactly the self-contained case S3 exists to protect.

So the unit's only conditionality lands with zero observation. Worse, `lexicon wiring` runs `--check` against gov's own tree, where `codebase-map` is present, so the absent-kit branch never executes on any bar — armed but unreachable, certified by a §5 line asserting coverage is adequate.

**Fix:** rewrite AC3 against whichever mechanism B1 selects — the real command with its real flags, the fixture that must be built (a sandbox holding `tools/lexicon/` **and** `tools/codebase-map/`, plus its negative twin), and the exact assertion. If B1 lands on (c), delete AC3 and say in §5 that there is no kit-absent behaviour left to gate.

---

## TOOL-dPromptedSeam-2 — blockers

### B3 · §2 S1 · §3 · §8 Q1 vs §6 AC2 — the liveness predicate is one rule short
*(raised as U7, U8, C6 and P3 — four independent raisings)*

AC2 requires the helper to report `boundedK` as having no live stem. `subtokens('boundedK') == ['bounded','k']`, object `k`. **`k` is not a stopword.** `map_lib._STOPWORDS` is 21 words (a an the to of in on for and or is be as at by from into with it this that) and `stems()` drops `k` by a *separate* predicate, `len(t) >= 2` at `map_lib.py:627`; its docstring says so in as many words: "Stopwords + 1-char tokens dropped". S1 buys only "a stopword-aware verdict", §3 and §8 Q1 authorise only "a minimal inline set". The minimum-length rule appears nowhere, the set is never enumerated, and the spec never says whether "stem" implies stemming or just means the raw subtoken.

An implementer who ships exactly what §2/§3/Q1 authorise **reds AC2** and will be told the helper is broken when the spec is. Membership is load-bearing, not academic: the 15 non-underscored off-table names with a dead object span six token classes — `of` (`ext_of`, `pin_of`, `cache_of`, `parent_of`, `owners_of`, `message_of`, `index_of`, `openersOf`), `at` (`anchor_at`, `blob_at`), `for` (`grammar_for`, `destinations_for`), `in` (`fan_in`), `with` (`rank_with`), and the single letter `k`. A set covering `of`/`in` alone leaves four classes live and AC2 still passes.

**Fix:** S1 states the predicate as a pair — "a live stem is a subtoken that is neither in the inline stopword set nor shorter than two characters, the same two-rule test `map_lib.stems()` applies (`map_lib.py:621-628`), restated because the layer ban forbids importing it" — and says whether stemming is in or out ("stem" should stop appearing if it is out). Enumerate the inline set in §2 or §4; it is 21 words at most and it *is* the contract. D1 stops calling `boundedK` a stopword case: the real split of the 15 is 14 by membership, 1 by length.

### B4 · §4 D1 · §4 D2 · §2 S2 — the design measures a population the code never sees
*(raised as U6 and U10)*

D1: "68 (29%) yield no object at all, **all of them single-token type names** — `Candidate`, `Corpus`, `Dossier`, `Refusal`." S2 repeats it: "every single-token type name". D2's worked examples are `Dossier`, `Conf`, `Coverage`. **None of those six identifiers is in the population `read_object` is ever applied to.** `extract()` returns `(functions, types_, imports)` and `run_brief` — read_object's only caller — reads `got[0]`, the function list, at `lexicon.py:916` and `:936`. Every one of those six is a ClassDef and reaches `got[1]`. The corpus holds 32 distinct type names in total, so "68 … all of them single-token type names" is arithmetically impossible.

Re-derived over the set `read_object` does see: 326 distinct off-table function names, 234 not `_`-prefixed (the spec's 231), 70 with an empty object (the spec's 68). The **counts reproduce within ~1%; the characterisation does not.** The real group is single-token *function* names: `adopt`, `anchors`, `armed`, `cap`, `census`, `deco`, `enc`, `git`, `key`, `kit`, `lf`, `num`, `opt`, `rrf`, `sub`, `why`. `Dossier` → `parse_dossier` is persuasive precisely because a type and its constructor share a stem; `why`, `lf`, `rrf` and `num` are the population that actually exists, and the fallback reads very differently over them.

Second half of the same defect: D1/D2 were measured over *off-table* symbols, but `--brief` (S3's only consumer) builds its object set from **every** definition the target file extracts, with no off-table filter. Over this corpus that is 866 definitions, 236 with no object, and **97 of those are bare declared verbs** — `load`, `read`, `write`, `render`, `main`, `run`, `check`, `parse`, `__init__`. A full-identifier query on `main` or `run` is unbounded noise, not a 75% hit.

**Fix:** state which population each figure was measured over and which one S3 operates on; re-derive D1 over `got[0]` and publish the command; replace the four type-name exemplars with real members. If types were meant to be in scope, that is a change to `run_brief` to read `got[1]` and it needs its own scope line — nothing proposes it today. If bare declared verbs should be excluded from the non-gradeable group, that is a scope item with its own arm.

### B5 · §2 S2 vs §4 D3 — two contradictory return contracts, one of which silently changes `--brief`
*(raised as C7)*

S2: the helper "reports that fact **rather than an empty string**". D3: "`read_object` **keeps returning a string** and gains a companion", and folding the fallback in "would change `--brief`'s output without `--brief` asking". `lexicon.py:916` is `here = sorted({read_object(n) for n, _ln in (got[0] if got else []) if read_object(n)})` — the caller filters on **truthiness of the return**. Make the return truthy and all ~236 empty-object names silently enter `here`, which is exactly the outcome D3 refuses. Keep it empty and S2's sentence is false. The two cannot both be implemented.

**Fix:** rewrite S2 to match D3 — "When an identifier has no object at all, `read_object` still returns the empty string and the companion reports NO-OBJECT distinctly, so a caller can fall back to the whole identifier." Then say in S3 that `run_brief`'s `:916` truthiness filter is replaced by an explicit branch, so the `--brief` output change is a deliberate S3 act rather than a side effect of the helper.

### B6 · §4 D2 vs §2 · §8 Q2 · §6 — the headline value has no mechanism, no consumer and no AC
*(raised as U8)*

D2 is titled "the fallback is the FULL IDENTIFIER, and it was measured before being specced" and carries the unit's persuasive numbers. **No scope item builds it.** S2 says the helper "reports that fact"; D3 says it "REPORTS, it does not decide" and "Callers choose what to do"; S3's only consumer merely "separates gradeable objects from identifiers with none"; §8 Q2 resolves that `--suggest` will not use it. No AC observes a fallback query being issued by anything.

Q2's own reasoning turns on itself: it refuses `--suggest` because "a fallback with no consumer is dead code, so it is refused before it is written" — after that refusal the fallback has **no consumer at all**, so the spec's own rule condemns speccing it. What ships is a boolean and a changed `--brief` listing. A reader of §4 will believe the recovery landed.

**Fix:** either give the fallback a consumer in S-scope with an AC that observes a fallback query returning a non-self match, or demote D2 to a §3 non-goal — "the fallback is measured and deliberately NOT built here; this unit ships the verdict that lets a future caller do it" — and stop stating recovery rates as deliverables.

---

## TOOL-dPromptedSeam-1 — majors

**M1 · §2 S1 · §6 AC1 · §10 — the sibling kit's path is never derived** *(U3, P2)*
`KITREL` (`adopt-lexicon.sh:66-67`) is the **lexicon's own** dir and is the source of every path the Skill prints; nothing resolves a sibling kit, and the install prefix is a per-target answer (`prefix = "tools"`). AC1 pins the bare token `reuse_lookup.py` with no path, so it cannot distinguish an unrunnable filename from a hardcoded `tools/codebase-map/`. This repo has already paid for this exact class twice: `adopt-drift-audit.sh:101-109` records that its Skill hardcoded `workflows/` so the rendered Skill named two files that do not exist "and `--check` reported 'in sync', because it diffs the render against the template and BOTH carried the same wrong spelling" — fixed by deriving `WORKFLOWS_REL` and declaring `{{WORKFLOWS_DIR}}`; and `TOOL-aRootedPrefix-2` closed with S9's ruling that every path a kit PRINTS resolves from the repo root. §10 asserts the opposite, that this is "exactly the discovery problem rev-2 no longer has to solve" — withdrawing the exec removes the CALL, not the path question.
**Fix:** derive the sibling path from `KITREL`'s parent, surface it as a declared placeholder in `kit.toml`, and rewrite AC1 to assert the rendered path **resolves to an existing file** (`[ -f ]` on the token the Skill prints) — the one assertion a render-vs-render diff cannot fake. Correct §10's recall note.

**M2 · §6 AC2 · §5 — AC2 observes the pre-existing byte-compare, not this unit** *(U4a, P2b)*
`check_skill`'s `cmp -s` reds on any deleted byte; the token's identity is irrelevant. AC2 passes identically against an implementation whose step names the wrong tool, says the wrong thing, or asks for a picked name. §5's "AC2 makes its failing case observed, per §7's rule for a new check" has no subject — §3 and §7 both say this unit adds no check and no leg. That leaves AC1 as the sole load-bearing criterion, with AC3 unrunnable (B2) and AC4 weak (m1).
**Fix:** delete AC2 as coverage this unit does not add, or repoint it at a break in `SKILL.template.md` that violates S2 (swap "behaviour" for picked-name phrasing) and name what observes it. If nothing does, say so in §5.

**M3 · §2 S3 vs §2 S4 · §6 AC5 — S3's absolute is broken by S4 inside the same unit** *(U4b, P5)*
S3: "An adopter without the map must not read an instruction naming a tool it does not have." S4 puts the same instruction into `tools/lexicon/LEXICON.md`, whose first `[[files]]` rule in `kit.toml` is `include = "**"`, `role = "engine"` — it ships verbatim to every adopter with no placeholder and no conditionality possible. AC5 pins the mention unconditionally. Whichever answer the implementer takes, the other section reads as violated, and if S3's principle is what justifies B1's cost, S4 undercuts the justification.
**Fix:** decide conditionality once for the unit and apply it to both carriers.

**M4 · §2 S4 · §6 AC5 — a second authored copy of one invocation, with the drift detector missing on the authored side** *(U5a)*
The Skill copy is generated and byte-compared; `LEXICON.md` is hand-authored and gated by nothing. §8 Q1 resolves in favour of exactly the opposite principle ("Two documents describing one invocation is the class this repo names"). AC5's observation is `grep -c` (which counts matching *lines*) returning ≥1 plus an unmechanised judgement, so the copy can sit stale forever.
**Fix:** make `LEXICON.md` point at the Skill's ladder rather than restate it. If both must carry prose, name the comparator and declare it in §3 as a new leg. Replace AC5 with an assertion that distinguishes the correct sentence from any sentence.

**M5 · §7 — overstates coverage; the sibling spec discloses what this one hides** *(U5b)*
"Unguarded and runs on every bar" verifies for `lexicon wiring` (`guard: []`), but that leg only byte-compares — AC2 and nothing else. Any arm for AC3 lands in `selftest.py`, whose leg is `subject = "kit"` and **HELD unless `GATE_SELFTESTS=1`**. And `lexicon naming predicates` cannot observe this diff at all: `.lexicon.conf` declares `md::dark`, so `SKILL.template.md`, `LEXICON.md` and the rendered `SKILL.md` are graded by no predicate. `-2` §7 discloses its own held-leg caveat in as many words; `-1` §7 is silent.
**Fix:** adopt `-2`'s disclosure sentence, name which leg covers which AC, and drop or qualify `lexicon naming predicates`.

**M6 · §10 — the reuse audit misses three existing carriers of its own sentence** *(P6 — the highest-value non-blocker in the set)*
D1's premise is "a gap between two documents that never mention each other". This repo **already renders that instruction, twice**: `tools/memory-tree/BUILD-METHOD.template.md:140` emits `python {{TOOL_ROOT}}codebase-map/reuse_lookup.py "<behaviour phrase, not a symbol name>"` — S2's exact requirement, already worded — and `SPEC-TEMPLATE.template.md:227` names the same script for §10. Both fill `{{TOOL_ROOT}}` from the kit's own install prefix (`adopt-memory-tree.sh:36-37,84`), and **neither is kit-conditional**. There is even a forcing function: `check-memory-hygiene.sh:744` — "The kit already ships tools/codebase-map/reuse_lookup.py; this is the check that makes anyone use it." §10 names none of the three.
So the audit misses the existing carriers of its sentence, the existing solution to M1's path problem, and the existing precedent that this instruction ships **unconditionally** (which is the cheapest resolution of B1).
**Fix:** add all three to §10, and state in D1 what the new rung adds that the rendered M5 step does not — the *moment* (a refusal mid-code) and the *audience* (an author who already picked a name). That is a real distinction and it is the unit's actual justification. Better still, have the rung point at BUILD-METHOD's M5 step rather than re-word it, which is the discipline §10 already applies to `reuse-lookup.agent.md`.

## TOOL-dPromptedSeam-1 — minors

- **m1 · §6 AC4** *(U6a)* — one identifier's suggestion proves nothing about the engine: `run_suggest`'s docstring says "Reads the declaration and nothing else. NO CORPUS PASS", so AC4 passes byte-identically with `read_object` entirely rewritten. And the anchor is a literal sha that will not be this unit's parent, because `-2` "should land first" and edits the same file — AC4 would measure two units' diffs and attribute the verdict to one. **Fix:** anchor to `-1`'s own merge-base and replace the pin with `git diff --stat <base>...HEAD -- tools/lexicon/lexicon.py tools/lexicon/subtokens.py` being empty. Keep the `--suggest` run as a smoke check, stop calling it proof.
- **m2 · §2 S4 · §6 AC5** *(C12, P5b)* — `LEXICON.md` has no "delivery section"; the nearest is `## How the table reaches whoever is writing the name`, whose body reads "the declaration is delivered **three ways**" above exactly three bullets. A fourth bullet falsifies the count, AC5 cannot see it, and no gate reads that prose count — the repo's own "NO count of a derived population is written in prose" rule, broken by the unit editing the sentence carrying it. **Fix:** name the section by its heading; if a fourth bullet lands, change "three" to "four" and have AC5 assert `grep -c 'three ways'` returns 0.
- **m3 · §9** *(C14)* — entries run rev-1, rev-3, rev-2, so a reader scanning the "rev high-water" bottom-up lands on rev-2 while the header says rev-3; the hygiene gate only checks that the header's rev appears somewhere. `-2`'s §9 is newest-first, so the build carries two directions. **Fix:** one direction, both files.
- **m4 · §5 migration/rollback** *(P8)* — `tools/lexicon/README.md`'s "Uninstalling — the ORDER matters" covers one direction only. After this unit the reverse acquires an unwritten step: removing `codebase-map` leaves the rendered Skill naming a deleted script, and `--check` cannot see it (same render-vs-render reason as M1). §5's "none" and §7's "the codebase-map legs are untouched" are true of code and false of the coupling. **Fix:** one sentence in each place.

---

## TOOL-dPromptedSeam-2 — majors

**M7 · §6 AC1 — the fixture cannot exercise the half the split exists for** *(U9a — fixture-passes-by-finding-nothing)*
`tools/codebase-map/reuse_lookup.py` extracts 14 definitions, 9 with an empty object (`_rank`, `_counts`, `render`, `_line`, `_sources`, `main`, `empty`, `merge`, `add`) and **zero** with a stopword-or-short object. AC1's stated purpose is "proving the split is reached rather than merely coded" — a group of 9 that an implementation with no stopword awareness at all produces.
**Fix:** split AC1 into two arms with a named file each, one holding a single-token definition and one holding a stopword-object definition (`ext_of`, `pin_of`, `fan_in`), and assert expected group **membership**, not non-emptiness.

**M8 · §4 D2 — "75%" never says which query, and the answer ranges 21%–63%** *(U7b)*
D2's closing sentence is "The fallback is not a guess", and 75% is the only number carrying it. Measured over the 70 empty-object off-table function names: exact object-key match against the index `run_brief` builds → 15 (21%); generous subtoken containment → 25 (36%); stem-share intersection, the shape `reuse_lookup` actually uses → 44 (63%). D2 does not say which it measured. At 21–36% the fallback is mostly noise, which is the verdict R2 reached about rev-1's object query at 16.6% — the audit that produced this unit.
**Fix:** name the query shape, publish the command, and re-argue S2 at whatever the number really is.

**M9 · §5 risks · §10 · README detriment — "two callers" is wrong as functions and unstated as sites** *(U10b, C10)*
`read_object` is defined at `lexicon.py:856` and reached only from `run_brief`, at `:916` (twice in one comprehension) and `:936` — **one caller, three call expressions, no test coverage** (`selftest.py` never mentions it). §5 and §10 say "two callers" and use the number to price the blast radius as low; the README says "stays a single-caller helper" as a *detriment of not building*. Neither unit adds a consumer, so that detriment survives the build and the wrap-up could claim otherwise.
**Fix:** "one caller (`run_brief`), two call sites at `lexicon.py:916` and `:936`, no existing test coverage." Then either name the future caller D3's report/decide split is for, or fold the verdict into `--brief` and drop the companion under "delete over disable".

**M10 · §3 · §8 Q1 — the repo has a gated idiom for exactly this, and this kit already uses it** *(P4)*
`adopt-lexicon.sh:26` carries `# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)`, and `tools/lib/resolve-python.test.sh:88-110` is a generic `PARITY_ROWS` engine over those markers with a non-empty-population arm per row. Q1 instead ships "a minimal inline set whose provenance is recorded in the docstring" — a docstring is not a comparator, and the set is declared deliberately smaller than its source, so it starts diverged and nothing notices. Separately worth filing: `subtokens.py`'s docstring and `memory/map/features/lexicon.md:148` both claim "A parity leg asserts the two copies agree" and **no such leg exists** — `PARITY_ROWS` holds only `resolve_python` and `kickoff_region`, its `git grep -l` is scoped to `*.sh`, and `gate-legs.json` carries no lexicon parity leg.
**Fix:** port the set (and B3's length rule) under a `# >>> lexicon_stems — canonical copy: tools/codebase-map/map_lib.py (byte-identical; gated)` marker and add the row — widening that `git grep` to `*.py` is part of this unit — or spec an equivalent arm in `selftest.py`. File the stale subtokens-parity claim separately rather than inheriting it.

**M11 · §2 S1 vs §4 D3 · §6 AC2 — three states specified, two supplied** *(U12)*
S1's outcome is three-way ("tell 'no object' from 'an object made entirely of stopwords'"); D3's mechanism is two-way ("says whether that string has a live stem"), which answers the same for both. AC2 never asks the helper about a single-token identifier, so nothing catches it. It matters because S2 gives the single-token case its own handling.
**Fix:** decide two states or three and make S1, D3 and AC2 agree. If three, name the return shape and add an arm asking about `Dossier` (or a real single-token *function* name, per B4) and getting a distinct answer from `pin_of`.

## TOOL-dPromptedSeam-2 — minor

- **m5 · §3 bullet 2** *(C5, U9b)* — the OUT heading "**No stopword list of this kit's own**" is contradicted by its own final clause ("the shipped shape is the minimal inline set") and by §8 Q1 ("It ships a minimal inline set"). A §3 entry is the cut-line a reviewer greps the diff against, and this one forbids the artifact the unit ships. **Fix:** retitle to "No SECOND AUTHORITY on what a stopword is" and keep the body; move the inline set into §2 as a numbered scope item.

---

## Both specs

- **X1 · status headers · §8** *(C13)* — every §8 fork in both specs is RESOLVED, and `memory/TEMPLATE-SPEC.md:122-124` requires a resolved fork to "add the `ratified <date>` pointer to the header tail". Both headers stop at `… · Tier-1 · base 671e953d · streams tooling`. A fully-resolved spec currently looks identical to one with open forks. **Fix:** append `· ratified 2026-08-25` to both, in the commit that bumps the rev.
- **X2 · `-2` §1 vs the derived build order** *(C11, U11a)* — `-2` §1 says "should land first"; `TEMPLATE-SPEC.md:74-80` makes `order <n>` a status-header verb and states that the README roster and build-order region are DERIVED from it, "which is why the order belongs on the spec and not in README prose". Neither header carries it, the generated region says "No spec under this build declares an `order` verb", and both roster rows show `—`. The derived surfaces a session is told to read carry no ordering, and `-1`'s AC4 base anchor depends on the answer (m1). **Fix:** `· order 1` on `-2`, `· order 2` on `-1`, re-run `gen_build_index.py --write`, keep the §1 sentence as the reason but not as the declaration.

## Build folder — `memory/builds/dPromptedSeam/README.md`

The `## Parked decisions` slot was rewritten to record the refutation; three earlier slots were not, so the folder gives two answers. `gen_build_index.py:103-108` binds only slot 1 as M3's immutable goal, so all of this is amendable.

- **R1 · Expected improvements, bullets 2 and 3** *(C8, U11b)* — "`read_object()` gains its second consumer" is contradicted by `-1` §10 ("NOT used by this unit") and by `-2` leaving `--brief` the sole caller. "object `conf` returns `load_conf` … Three for three" is verbatim the three-hand-picked-objects claim the prior audit refuted at 16.6% over 326 offenders, and `-1` §3 now discards it by name. **Fix:** rewrite bullet 2 to what the build delivers ("`read_object()` stops answering unusably for a third of the corpus, so the one drift class `--brief` measures stops being silently narrowed") and replace bullet 3 with a measured figure or delete it. See also M9 on the matching Detriments bullet.
- **R2 · Build-level rules 2 and 3** *(C9, U11b — armed-but-unreachable)* — rule 2 governs "THE HINT", which no longer exists. Rule 3 enumerates "Map absent, object empty, **lookup timed out**, lookup refused" while `-1` §3 reads "No new conf key, timeout, discovery logic or outcome taxonomy. All four existed in rev-1 to serve a subprocess that no longer happens." Rule 1's second half ("Discovery is optional and absence is a normal outcome") describes the withdrawn step. BUILD-METHOD M2 makes the rules slot what every pass is checked against, so a rule that can never fire reads as live governance while certifying nothing. **Fix:** keep "THE LEXICON KIT STAYS SELF-CONTAINED" (now enforced by `.lexicon.conf`'s LAYERS ban); replace 2 and 3 with the one that binds rev-2 — "THE STEP IS AN INSTRUCTION, NOT A VERDICT: nothing this build adds may move an exit code, a pin or a predicate, and `LAYER_OFFENDER_PIN` stays 0" (verified: `.lexicon.conf` carries `LAYER_OFFENDER_PIN="0"`).

---

## What came back clean

Recording these because a clean lens is a result.

- **The layer ban.** Nothing survived alleging either spec re-opens the refuted cross-kit direction. `-1` §3's withdrawal is complete and correctly reasoned (P3 grades imports, so routing around it via exec is worse, not better), and `-2` §3/§8 Q1 refuse the import for the same declared reason. The refutation held; the specs absorbed it.
- **The `A` lens.** No finding carrying an `A` id survived the skeptic. Nothing held under it.
- **`-1` §5's run-time N/A pricing** was challenged and **defended**: the three N/A lines are scoped "at run time", and the rendered Skill executes nothing at run time whatever the renderer does at build time. Only the §9 tier claim (folded into B1) and the migration line (m4) survive.
- **`-2` §7's gate disclosure** is exemplary and is the model `-1` §7 should copy (M5): it names its leg, names that the leg is held, and says why that is less coverage than it looks.
- **`-2` §8 Q2's reasoning shape** is sound — the "delete over disable" veto is correctly applied; it simply turns on the unit itself, which is B6 rather than a defect in the resolution.
- **`-2` D4** (self-matches excluded by the caller) and **`-2` §5's a11y/i18n line** (declining to appear to fix the carried ASCII finding) both survived every lens untouched.

## The short path out

- Answer one question in `-1` — is the rung conditional? — and B1, B2, M3 and half of M2 retire together. P6/M6 argues the cheapest correct answer is "no": memory-tree already ships this same instruction to every adopter unconditionally, with the path derived and a hygiene check forcing its use.
- Answer one question in `-2` — which population, and which query? — and B3, B4, B6 and M8 all collapse into a re-derivation over `got[0]` plus two extra sentences in S1.
- X1, X2, m3 and R1/R2 are bookkeeping and cost minutes.