# TOOL-dClosedLexicon-12 — the census question, measured: refuse the coupling, close the real hole

**Status:** SPECCED · rev-2 · 2026-08-17 · node d · Tier-2 · base b4f0cf1c · streams tooling

## 1. Goal

Unit 2's F1 asked whether `codebase-map` should CONSUME a lexicon-owned definition census, and
deferred it for want of numbers: it would close `TOOL-aNumeralWarden-4` and "the public-symbols-only
hole", at the cost of making an opt-in kit a prerequisite of one that is not. The deferral said to
reopen with numbers. Here they are, measured on this tree at `b4f0cf1c`:

| | count |
|---|---|
| definitions the lexicon sees (tracked tree, `py` + `js`) | 642 |
| symbols `memory/map/generated/symbols.json` carries | 426 |
| lexicon-only | **219** |
| map-only | 3 |

The 219 split three ways, and the split is the finding:

- **120 leading-underscore Python names.** Excluded by `map_lib.python_symbols` on purpose — "private
  by Python convention (skipped)". The recall index answers "what seam can I reuse", and a private
  helper is not one. Importing these is noise, not coverage.
- **46 nested defs and `.template.py` names.** Also deliberate: `python_symbols` indexes module-body
  nodes only ("a def nested in a class/try is not a top-level seam"), and `_live_py` filters
  templates by suffix with its own raise if the filter ever eats the layer.
- **53 JavaScript definitions**, of which **30 are under `tools/`**, the map's own base. The recall
  index carries **NONE** of them. Its three `kit-js` rows are the workflow scripts' `meta` blocks,
  which are `export const meta = {` — an object, not a function, so the definition probe cannot see
  them either. That is the table's `map-only | 3`, and those three are disjoint from the 30. `boundedK`
  (`tools/hooks/agent-cap.js:125`), the binder every fan-out consumer routes through, is invisible to
  `reuse_lookup.py`. That is `TOOL-aNumeralWarden-4`, verbatim and confirmed.

So the measurement REFUTES half the question and CONFIRMS the other half. There is no
"public-symbols-only hole" — that is the map's doctrine working as designed, and 166 of the 219 rows
consumption would import are rows the map excludes on purpose. There IS a JavaScript hole, it is
real, and closing it needs no lexicon: it is one extractor inside the kit that already owns symbol
extraction.

`map_extractors.py:202-204` states the opposite in a comment — "the only exports are the workflow
`meta` blocks. That is accurate coverage of a layer with few exports, not a hole." Measured, the layer
has 30 definitions and 3 indexed rows, disjoint. The claim is true about EXPORTS and false about the
layer.

## 2. Scope (IN)

- **S1** — a `js_definitions` symbol extractor in `map_lib.py`, statement-leading `function` /
  `class` / arrow-assigned `const|let|var`, emitting `{id, kind, file}` with `kind` drawn from the
  existing frozen `SYMBOL_KINDS`. No vocabulary change.
- **S2** — a LIVENESS floor on it, in this repo's own idiom: a scanned `.js` file that yields zero
  symbols raises `MapError` naming the file. `enumerate_exports` raises on an export form it does not
  recognise, which is a completeness guarantee for exports and buys nothing for a CommonJS file with
  no `export` line at all — the exact shape that made this hole silent. Measured: every one of the
  six `.js` files under `tools/` yields at least one definition today, so the floor is a measurement
  and not an assumption.
- **S3** — `SYMBOL_EXTRACTORS["kit-js"]` becomes the UNION of `enumerate_exports` and
  `js_definitions`, deduped on `(id, file)`. Both are kept: `export const meta = {…}` is an object
  and only the export scan sees it; `boundedK` is a bare declaration and only the definition scan
  does.
- **S4** — the stale comment at `map_extractors.py:202-204` is replaced with what was measured,
  including the number, because "few exports, not a hole" is the sentence that kept this closed. The
  corrected sentence goes into the `js_definitions` DOCSTRING as well, which is where an AC can see it.
- **S5** — a CROSS-CHECK arm in `tools/codebase-map/selftest.py`: over `tools/**/*.js`, the map's
  definition set is a SUPERSET of the lexicon's. It skips LOUDLY when `tools/lexicon/` is absent, so
  an adopter who took one kit is told the arm did not run rather than shown a green it did not earn.
- **S6** — `TOOL-aNumeralWarden-4` closes, and this row closes as REFUTED-with-numbers on the
  consumption question. The measurement above goes into the decision record so it is not reopened a
  third time on the same missing evidence.

## 3. Non-goals (OUT)

- Any consumption of a lexicon-owned census by the GENERATED index — that is, by anything
  `SYMBOL_EXTRACTORS` reaches at render time, in either direction, mandatory or optional. §4 says why
  the optional shape is the worst of the three. S5's TEST-time cross-check is deliberately excepted,
  and the two are different in the way that matters: a skipped ARM announces itself and changes
  nothing on disk, while a skipped EXTRACTOR silently shrinks `symbols.json` and leaves a green gate
  over a smaller index.
- Indexing private, nested, or `.template.py` Python names. That is 166 of the 219 and the map
  excludes them by a stated doctrine this unit did not find a reason to overturn.
- A shared JS-pattern module. The repo's own answer for code two kits need is "carry it inline,
  byte-identical, gated" (`tools/lib/resolve-python.sh`), and that machinery costs more than the
  drift it would prevent here — S5 buys the same protection for one arm. Recorded so a reviewer can
  push back on the trade rather than guess at it.
- The `.claude/hooks/` copies (23 further definitions). They are renders of the `tools/` originals;
  indexing both would put two rows in the recall index for one seam.

## 4. Design

### Why not consume, stated as a cost rather than a preference

Three shapes were available.

**Mandatory consumption** makes `.lexicon.conf` a prerequisite of the map. The lexicon is opt-in by
construction — with no conf it reports NOT ADOPTED and exits 0, and that is its whole off switch. A
map that consumed it would, in a target without the conf, silently produce today's 3-row JS layer:
green, smaller, and with nothing saying so. That is green-by-absence, which is the failure the map's
extractor doctrine exists to ban, so consumption would import the defect it was meant to close.

**Optional consumption** — consume when present, fall back otherwise — needs BOTH implementations and
makes the index's contents depend on which kits a target installed. Two corpora for one question,
selected by a condition nobody reads.

**Neither**, which is this unit: the map extracts what the map needs, in the kit that owns
extraction, and the lexicon's census stays the lexicon's business. The duplication that leaves is one
regex family in two kits, and S5 pins the direction that matters.

### The superset direction is the one worth asserting

S5 asserts map ⊇ lexicon over the shared `.js` corpus. If the lexicon learns a definition form the
map has not, the map is under-indexing and the arm reds. The other direction is not asserted: the map
indexing something the lexicon does not is not a defect — `meta` is exactly that case today and is
correct.

### Data model

`symbols.json` gains rows; its schema, its `SYMBOL_KINDS` vocabulary and its generator are unchanged.
No `baseline.toml` movement and no dossier claim: `SYMBOL_EXTRACTORS` feeds the recall index only and
is never a ratchet, which is stated at `map_lib.py:296` and is why this unit cannot red the coverage
gate by adding rows.

### Files touched (estimate)

`tools/codebase-map/map_lib.py`, `map_extractors.py` and `map_extractors.template.py` (the seed must
carry the same extractor or an adopter inherits the hole), `tools/codebase-map/selftest.py`, the
regenerated `memory/map/generated/symbols.json`, the kit version pair, and the two backlog rows.

## 5. Production-readiness checklist

- security — read-only extraction over tracked source; no new execution path.
- perf / scale — one extra pass over six `.js` files.
- a11y / i18n — N/A.
- error / empty / loading states — a `.js` file with no definition RAISES rather than contributing
  nothing (S2); an absent lexicon makes S5 skip loudly rather than pass.
- observability — `reuse_lookup.py` is the observable: `boundedK` is findable after this unit and is
  the AC.
- risks — the regex is a probe, not a parser, and no stdlib JS parser exists to do better. The ceiling
  is documented on the function the way `enumerate_exports` documents its own, and S2 converts the
  worst case (a file the probe cannot read at all) from silence into a raise. What remains uncovered
  is a definition form the probe forgot in a file where it found something else — S5 pins that
  against the lexicon's independently-authored set.
- testing + left-shift gates — S5 plus the existing `python tools/codebase-map/selftest.py` and
  `test_codebase_map.py` freshness byte-compare, all already legs.
- migration / rollback — the generated artifact is regenerated by the gate's own command; no target
  state migrates.
- user docs — the extractor docstring and the corrected `map_extractors.py` comment (S4).

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/reuse_lookup.py boundedK` runs, `tools/hooks/agent-cap.js`
  is in the result.
- **AC2** — When the map is regenerated, `symbols.json`'s `kit-js` rows number at least **33** — the
  30 measured definitions PLUS the three `meta` rows, which are disjoint from them — so an extractor
  finding only 27 of the 30 cannot satisfy it by borrowing the export scan's three.
- **AC3** — When a `.js` file under the scanned base yields no symbol, generation RAISES `MapError`
  naming that file.
- **AC4** — When the lexicon's js pattern set finds a definition the map's extractor does not, the
  cross-check arm FAILS; when `tools/lexicon/` is absent, it prints a skip naming what did not run
  and the selftest still passes.
- **AC5** — When `python tools/codebase-map/test_codebase_map.py` runs, the generated artifacts
  byte-compare against a fresh render and no `baseline.toml` key moves.
- **AC6** — When S4's corrected sentence is checked, the `js_definitions` docstring states the
  measured 30-vs-3 gap, and `python tools/codebase-map/selftest.py` asserts that docstring names a
  number — an uncorrected copy of "few exports, not a hole" reds.
- **AC7** — When S6 lands, `TOOL-aNumeralWarden-4` and `TOOL-dClosedLexicon-12` both read CLOSED in
  `memory/backlog/TOOL.md`, and the §1 table's four figures (642 / 426 / 219 / 3) appear in the minted
  `memory/DECISIONS.md` row, so the measurement survives where the next reopening would look.
- **AC8** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

`python tools/codebase-map/selftest.py`, `python tools/codebase-map/test_codebase_map.py`,
`bash tools/check-kit-versions.sh`, `python tools/lexicon/selftest.py`. All existing legs; no new leg.

## 8. Open questions

None open. F1's consumption question is ANSWERED — refused, with the measurement in §1 as the reason
— rather than deferred again. The one judgement a reviewer should press is the OUT on a shared
pattern module (§3), where the cheaper arm was chosen over the repo's inline-and-gate idiom. Pressed
once in `review-dClosedLexicon-9` and REFUTED there: S5 is drift protection rather than a second
opinion, and its own inert-operand vacuity is already armed one leg over by
`tools/lexicon/selftest.py`'s frozen per-pattern-set sentinel (`lexicon.py:94-96`).

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft. The deferral asked for numbers before reopening; §1 is those
  numbers, and they moved the answer from "should we couple these kits" to "no, and here is the
  30-symbol hole that has nothing to do with coupling".
- rev-2 · 2026-08-17 · folds `review-dClosedLexicon-9`, 4 defects, no blockers; the audit re-derived
  every census figure in §1 and all of them reproduce. §1 said the index "carries 3 of them" while its
  own table said `map-only | 3` — the three `meta` rows are DISJOINT from the 30, so the index carries
  none, and AC2's floor rises from 30 to 33 (12-1). §3's OUT is scoped to render-time consumption, so
  it no longer forbids the S5 arm it also promotes to an AC (12-2). S4 and S6 gain criteria — a
  comment and two backlog rows were the two scope items no gate could observe (12-3). §10 records what
  the probes actually returned (12-4, X-1).

## 10. Reuse audit

**Probe 1, `reuse_lookup.py` — RE-RUN, and it MISSES.**
`python tools/codebase-map/reuse_lookup.py "javascript symbol extraction"` returns
`render_symbols_json`, `all_symbols`, `python_symbols`, `t_symbol_extractors_fail_closed`,
`t_symbols_render_deterministic_and_fail_closed`, then neighbours from the same file. It does NOT
return `enumerate_exports`, which IS in the corpus (`symbols.json` carries it against
`tools/codebase-map/map_lib.py`) — so this is a ranking miss, not an absence, and rev-1's "surfaces
only `enumerate_exports`" was false twice over. Recorded as an answer per M5. The §1 inference rests
on the measured 30-vs-3 gap, which reproduces exactly, and never on this probe.

**Probe 2, `query.py` — terms recorded for M7 (satisfied once for the SET, per M5).**
Question: *how does this repo retire a finished record and start a fresh one without losing the old
bytes, and how does a preview verb stay in step with the verb that acts.*
Terms: `rotation archive retired record terminal phase preflight refusal preview parity plan apply
divergence symbol corpus census`. Relevant hit for this unit: `TOOL-aCandidStub-2`
(`memory/backlog/TOOL.md:13`), this repo's `vacuous-selector-empty-population` class — which is
exactly what S2's per-file liveness floor exists to prevent on the JS side.

**Reuse, hand-verified.** `_live_py` (`map_extractors.py:190`, inside its docstring) is the direct
precedent for S2 — a layer-level assertion that the extractor still sees something, raising rather
than returning a smaller index — and this unit copies its shape rather than inventing one.
`enumerate_exports` is REUSED unchanged rather than replaced (S3); its raise-on-unrecognised-export is
a guarantee the definition probe does not offer, and dropping it to avoid two scans would trade a
strong guarantee for a weak one.
