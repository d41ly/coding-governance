# TOOL-dFairHearing-13 — the lens catalogue as data, rendered into the harness's five-slot literals, and a slot count in the fan-out leg

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 1 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0080@8c9e5de7 whole
**Carries:** node:item.review.lens

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

Every review lens is today a literal object typed into `tools/workflows/tier2-review.template.js`
(`DIFF_LENSES` at :774-800, `SPEC_LENSES` at :810-836), so adding or swapping a lens is an edit to the
harness, and the only thing that bounds a literal's size is `tools/hooks/agent-cap.js`, which retires.
This unit moves the lenses into a catalogue file in the review kit, `tools/workflows/lenses.toml`, has
the install render fill the harness's five-slot literals from it, and gives the merge bar's harness
check, the `verifier fan-out` leg, its own count of slots, never of names. It is the primitive the
design-audit preset, the opt-in swap and the whole-design walk add rows to (shared interface S3).

## 2. Scope (IN)

- **S1** — `tools/workflows/lenses.toml` holds one `[[lens]]` row per lens of today's two literals,
  ten rows, in today's slot order, each with the six fields `key`, `brief`, `kinds`, `presets`,
  `default_in` and `optin` (§4 Data model). Observed by AC1 and AC2.
- **S2** — `tools/workflows/render_lenses.py` is the renderer: it reads the catalogue, checks every
  row against the §4 rules, and fills each `{{LENS_SLOTS}}` token in a template from the rows whose
  `default_in` names the literal its marker line declares. It refuses by name, exit 2, on every rule
  §4 lists. Observed by AC1, AC4 and AC7.
- **S3** — In `tools/workflows/tier2-review.template.js` each of the two literals keeps its name and
  its receiver line, its opening line gains the marker `// gov:lens-slots <literal>`, and its body is
  the single line `{{LENS_SLOTS}}`. The comments at :769-773, :806-809 and :838-841 say the catalogue
  is the source and the render fills the literal. The live `tools/workflows/tier2-review.js` is
  re-rendered; its lens text is byte-identical to base. Observed by AC1 and AC2.
- **S4** — `tools/workflows/check-protocol-parity.test.sh`'s `render()` (:476-487) pipes a template
  carrying `{{LENS_SLOTS}}` through `render_lenses.py`, keeping its trailing bytes; the header's token
  list (:37) names the fifth token. `tools/workflows/kit.toml` declares `LENS_SLOTS` in the
  `tier2-review.template.js` rule's `placeholders` (:79) and rewords that rule's one-token comment.
  Observed by AC2 and AC8.
- **S5** — `tools/workflows/check-verifier-fanout.sh` measures, natively and without the hook, every
  array literal whose opening line carries `gov:lens-slots` in the workflow scripts it already scans,
  and reds any that does not hold exactly `LENS_SLOTS=5` top-level elements, counted string-aware.
  In its whole-tree mode it reds when no marked literal exists anywhere. Its clean line stays byte for
  byte; the slot verdict prints on a line of its own. Its header (:15-23) says which rule is native.
  Observed by AC3, AC4, AC5 and AC6.
- **S6** — The two sentences that call `SPEC_LENSES` the catalogue's one source,
  `tools/workflows/README.md:165-167` and `tools/memory-tree/README.md:699`, name `lenses.toml` as
  the source and the literal as its render; the workflows README gains a short catalogue section with
  the row grammar. `memory/map/features/agent-cap.md:187-190`, which says the fan-out leg only
  delegates, names the slot count as the one native rule. Observed by AC9.
- **S7** — `item.review.lens`, the owned node: the lens item is the catalogue row, `key` plus `brief`
  plus where it may run. Observed by AC1 and AC7.

## 3. Non-goals (OUT)

- The `preset` argument, the design-audit literal and its five rows: `TOOL-dFairHearing-2`.
- The `optIn` swap, the six opt-in rows, the opt-in marker form and the slot wrapper the swap needs:
  `TOOL-dFairHearing-3`. This unit validates the `optin` field and renders nothing for it.
- The whole-design literal and its rows: `TOOL-dFairHearing-18`.
- `tools/hooks/agent-cap.js`'s array-literal allowance (`MAX_LENSES`, :486-497, :934-968). It stays:
  it is what ADMITS the finder fan over `LENSES`, so removing it denies the harness. The hook retires
  in dBoundRoles (night pass two, point 7, the table at its lines 555 and 560). The verifier total and the
  loop markers move in `TOOL-dFairHearing-16`.
- A repository's own lens rows, an overlay, or the `lens` kind and namespace: dCalibratedLens
  (`cl-dClosedLoop-0470`). The catalogue ships as an engine file under the kit's `**` rule.
- `memory/guides/BUILD-METHOD.md:133-134` (M4's pointer at `SPEC_LENSES`) and its template. The
  literal still holds every spec brief after this unit, so the pointer still resolves; rewording a
  governance guide is not a change clause 13 names.
- `REVIEW_SHAPE` (:970) and the kit `version:`. No lens prompt changes, so no lens file goes stale;
  versions are minted at landing (`725b97638`, the aTrimmedHook mint over a merge).
- `memory/guides/REVIEW-PROTOCOL.md`'s lens list: `TOOL-dFairHearing-10`.

### Edges

- **hands-off** `TOOL-dFairHearing-2` — the catalogue, the renderer and the `gov:lens-slots` marker its design-audit literal declares, with the five rows it adds
- **hands-off** `TOOL-dFairHearing-3` — the `optin` field this unit validates and renders nothing for, which the swap renders
- **hands-off** `TOOL-dFairHearing-9` — the rule that no lens key equals a literal name, which keeps per-preset lens notes unambiguous
- **hands-off** `TOOL-dFairHearing-16` — the native slot arm in the `verifier fan-out` leg, beside which the moved agent-cap rules land
- **hands-off** `TOOL-dFairHearing-18` — the marker and rows of the whole-design literal
- **hands-off** external — dBoundRoles retires agent-cap's array-literal allowance with the hook
- **hands-off** `TOOL-dFairHearing-23` — finding ids 7, 8, 20, 26, 27, 46 and 47 of the round-1 spec audit: the opt-in marker admitted beside rule 11 (its S14, AC7), the whole-design literal marked (its S15, AC8), the slot count on agent-cap's `topLevelArgs` with `LENS_SLOTS` its one home (its S34, S42, AC25, AC33), one marker predicate through `render_lenses.py --markers` (its S35, AC26), and the `mkfix` and `build_layout` fixtures S5 and S4 break (its S23, S24, AC14, AC15)

## 4. Design

### Evidence

- The two literals and their receiver: `tools/workflows/tier2-review.template.js:774-800`, `:810-836`
  and `const LENSES = isSpec ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers` at :842. Every brief
  is one single-quoted line under a `brief:` line, and the only escape the twenty briefs use is `\'`
  (13 of them), measured 2026-10-23 at `3dca04036`, whose `tools/` equals base.
- A workflow script has no filesystem (`memory/map/features/review-harnesses.md:48-53`), so the
  harness cannot read the catalogue at run time. The install render is its one derivation, as it is
  for the `FANOUT_CAP` token (`tools/workflows/kit.toml:72-79`).
- The hook counts a literal's top-level elements over a string-blanked view and admits five
  (`tools/hooks/agent-cap.js:934-968`); measured 2026-10-23, a copy of `tools/workflows/tier2-review.js`
  with a sixth element planted in `SPEC_LENSES` is denied, exit 2, so the hook's count is live today.
- `check-verifier-fanout.sh` feeds every scanned script to the hook and implements no rule itself
  (:15-23); its whole-tree population is every tracked or untracked `*.js` exporting `meta`, the
  templates excluded (:163-186).
- The kit already reads TOML with `tomllib` elsewhere (`tools/roles/roles_lib.py:339-350`), and govkit
  requires CPython 3.11 for it (`tools/govkit/govkit.py:108`).

### Data model

```toml
# tools/workflows/lenses.toml — one row per lens; a row's place in the file is its slot order.
[[lens]]
key = "coherence"
kinds = ["spec-audit"]
presets = ["unit-spec"]
default_in = ["unit-spec"]
optin = false
brief = "Coherence: does the spec set agree with itself, ..."
```

| Field | Type | Meaning |
|---|---|---|
| `key` | string, `^[a-z][a-z0-9-]*$` | the lens key every reader already uses: `LENS_KEYS`, `lensNotes`, the lens-yield table, a finding's `lens` |
| `brief` | non-empty string, one line | the finder's brief, raw text; the render escapes it |
| `kinds` | non-empty list of `diff-review`, `spec-audit` | the review kinds the row may run under |
| `presets` | non-empty list of literal names | every literal whose slot the row may fill, by default or by a swap |
| `default_in` | list, a subset of `presets` | the literals in which the row fills a default slot |
| `optin` | boolean | whether the row may be swapped into a literal of `presets` it is not a default of |

A LITERAL NAME is what a marker declares: `diff-review` for the diff kind's one literal, and a preset
name of the spec-audit kind otherwise, `unit-spec` today (§8 F1). The literal set is DERIVED from the
markers in the template being rendered and is typed nowhere else, so a preset another unit adds is a
marker and its rows, never a third list.

A row with `default_in = []` and `optin = false` is legal: it is catalogued and selectable by
nothing, the state an opt-in lens holds until its losing test is recorded.

### The rules the renderer checks

`check_catalogue` refuses, exit 2, naming the row's `key` (or its index when the key is the fault)
and the rule:

1. the file is not TOML, or holds a top-level key other than `lens`; a python below 3.11 refuses
   naming the floor and `tomllib`;
2. a row lacks one of the six fields or carries a seventh; a field has the wrong type; `key` breaks
   its pattern; `brief` is empty or carries a CR, LF, U+2028 or U+2029;
3. `kinds` or `presets` is empty or repeats a member, or `kinds` names a value outside the two;
4. `default_in` names a literal `presets` does not;
5. `kinds` disagrees with `presets`: the set of kinds must equal the kinds of its literals, where
   `diff-review` is the diff kind and every other literal the spec-audit kind;
6. two rows share a `key` and a literal of their `presets` (§8 F2: unique per literal, not globally);
7. a `key` equals a literal name;
8. a row names a literal no marker in the template declares;
9. a marker's literal is filled by no default row;
10. an `optin = true` row names no literal outside its `default_in`;
11. a marker line is not followed by a line that is exactly `{{LENS_SLOTS}}`, or that token stands
    without a marker line above it.

It does NOT count slots. The slot count has one owner, S5, so a sixth default row renders a sixth
slot and the fan-out leg reds it: a renderer refusing it too would be a second answer to one question.

### The render

```
python <kit>/render_lenses.py <catalogue>        # stdin: a template, stdout: it with each token filled
```

A marker is a line ending `= [ // gov:lens-slots <literal>`. The line after it, `{{LENS_SLOTS}}`, is
replaced by each default row of that literal, in file order, in exactly today's shape:

```js
  {
    key: 'coherence',
    brief:
      'Coherence: ... today\'s tree ...',
  },
```

`\` renders as `\\` and `'` as `\'`. Input and output are UTF-8 bytes with LF line ends, read from
`sys.stdin.buffer` and written to `sys.stdout.buffer`, never through text mode: on this platform a
text-mode stdout writes CRLF, the class `memory/gotchas/gate-green-by-accident-on-generated-bytes.md`
and `memory/gotchas/text-mode-read-eats-a-bare-cr.md` record. Every byte outside a token passes
through unchanged, the trailing newline included.

`render()` in `tools/workflows/check-protocol-parity.test.sh` runs it only for a template whose text
carries the token, with the python it already resolved at :517 and the catalogue beside the script,
and keeps the trailing bytes by the `printf X` idiom its first line uses (:478-479). A non-zero exit
is the existing "render ... FAILED" branch, and the existing unsubstituted-placeholder arm (:579-583)
still reds a token the renderer missed.

### The slot count

In `tools/workflows/check-verifier-fanout.sh`, after the hook loop and over the same `$SCAN`
population, one `node -e` block named `measureSlots` reads each file and, for every line whose raw
text carries `gov:lens-slots`, walks from that line's `[` to its matching `]` and counts the
top-level elements. The walk is string-aware: single, double and template quotes with `${}` nesting,
line and block comments, and bracket depth; a trailing comma is not an element (the class
`memory/gotchas/trailing-comma-counted-as-an-element.md`). It prints `<file>:<line> <literal> <n>`.

```
LENS_SLOTS=5   # the harness's slot count, its one home; counted per marked literal, never by name
verifier-fanout: SLOTS — <file>:<line> literal <name> holds <n> slot(s); a lens literal holds exactly 5
verifier-fanout: no lens-slot literal (a line marked gov:lens-slots) in any workflow script — the slot count graded nothing, which is not a pass
verifier-fanout: slots — <m> lens-slot literal(s), each holding 5
```

The first two set the exit to 1. The second fires in whole-tree mode only: with explicit files, a
fixture harness carrying no marker is legal, and every existing fixture arm passes explicit files.
The hook's clean line at :223 is unchanged, so no arm keyed on it strands
(`memory/gotchas/arm-literal-strands-on-message-edit.md`).

### Inventory

| Minted | Kind | Where |
|---|---|---|
| `tools/workflows/lenses.toml` | file, engine | the catalogue |
| `tools/workflows/render_lenses.py` | file, engine | `main`, `load_catalogue`, `check_catalogue`, `render_lens_slots` |
| `LENS_SLOTS` | placeholder token and shell constant | the template's literal bodies; `check-verifier-fanout.sh` |
| `gov:lens-slots` | marker | each lens literal's opening line |
| `measureSlots` | inline node function | `check-verifier-fanout.sh` |

Names follow the lexicon's verb cells (`.lexicon.conf`: `py.function snake`, `js.function camel`).

### Files touched (estimate)

- `tools/workflows/lenses.toml`
- `tools/workflows/render_lenses.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (its render)
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/workflows/check-verifier-fanout.sh`
- `tools/workflows/check-verifier-fanout.test.sh`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/kit.toml`
- `tools/workflows/README.md`
- `tools/memory-tree/README.md`
- `memory/map/features/agent-cap.md`

### Alternatives rejected

- **The harness reads the catalogue at run time.** It has no filesystem; a caller would have to pass
  every brief in `args`, and the lens set would then be the caller's, not the kit's.
- **A JSON catalogue.** It needs no python floor, but a brief is a long human-edited line and JSON
  offers no comment for a row's provenance. `tomllib` is stdlib and already a kit dependency.
- **Counting slots in the renderer.** The renderer runs only at install and in the parity leg; a
  hand edit to the live harness would never meet it. The fan-out leg reads what runs.
- **Asking the hook for the count.** It keeps the count in the file that retires, which is the move
  clause 13 reverses.
- **A bash renderer.** Bash cannot parse TOML; a regex reader of a TOML subset is a second parser.

## 5. Production-readiness checklist

- security — the catalogue is a tracked kit file rendered into single-quoted JS strings; rule 2
  refuses every line terminator and the render escapes `\` and `'`, so a brief cannot close its
  string. No new write path: the render writes only the live copies it already writes.
- perf / scale — one python start per parity run and one node walk per scanned script; both about a
  tenth of a second, untimed and not a stated budget.
- error / empty / loading states — an empty catalogue refuses by rule 9; a whole-tree population with
  no marked literal reds rather than passing; a missing catalogue file refuses naming its path.
- observability — the fan-out leg prints the slot line on every clean run, so a live count is visible.
- risks — an adopter whose resolved python is below 3.11 cannot render; it refuses by name rather
  than writing a harness with a placeholder in it. govkit already needs 3.11, so an install that ran
  govkit has one, though `resolve_python` may pick another launcher (`tools/govkit/govkit.py:1151`).
- testing — AC1 to AC9 as probes; the arms in §7.
- migration — an existing install re-renders `tier2-review.js` through the kit's `[[regenerate]]`
  row (`tools/workflows/kit.toml:115-120`); the result differs from today's file by comment lines
  only. The new engine files arrive under `**`.
- user docs — `tools/workflows/README.md` gains the catalogue section; no page under `help/` covers
  the review harness (it holds `README.md`, `measure-legs.md` and `roles.md`).

## 6. Acceptance criteria

- **AC1** — When `python 'tools/workflows/render_lenses.py' 'tools/workflows/lenses.toml' < tools/workflows/tier2-review.template.js`
  runs, the `key:` lines and the brief lines beneath each `brief:` line of the literals marked
  `diff-review` and `unit-spec` equal, byte for byte and in order, those of `DIFF_LENSES` and
  `SPEC_LENSES` in `git show '3708a705:tools/workflows/tier2-review.js'`.
  Red when: a brief is reordered, re-escaped, re-wrapped or changed, or a row is missing.
  figure: the ten keys and ten briefs are PINNED at base `3708a705`; the comparison reads only those
  lines, so a later unit's wrapper around a slot leaves it standing.
- **AC2** — When `git diff -U0 3708a705 -- tools/workflows/tier2-review.js` runs, every changed line
  is a `//` comment line or one of the two marked opening lines.
  Red when: the render changed a lens's text, so the parity leg's live copy no longer equals base's
  prompts.
- **AC3** — When `bash tools/workflows/check-verifier-fanout.sh <copy>` runs on a scratch copy of
  `tools/workflows/tier2-review.js` with a sixth element added to the literal marked
  `gov:lens-slots unit-spec`, it prints the `SLOTS` line naming `unit-spec` and `6` and exits 1.
  Red when: the planted sixth slot leaves the slot verdict silent.
- **AC4** — When a scratch catalogue adds a row with `optin = true`, `default_in = []` and
  `presets = ["unit-spec", "diff-review"]` and `kinds` for both, every literal marked
  `gov:lens-slots` in the render of AC1 over it is byte-identical to the same literal rendered over
  the shipped catalogue, and `check-verifier-fanout.sh` on that render prints the `slots`
  line naming every marked literal and exits 0.
  Red when: a row added as data changes a literal or reds the leg.
- **AC5** — When `check-verifier-fanout.sh` runs on a scratch harness whose marked literal holds five
  elements whose strings carry `,`, `]`, `'` and a template span `${a, b}`, plus a trailing comma, the
  slot verdict reads 5.
  Red when: punctuation inside a string or a trailing comma is counted as a slot.
- **AC6** — When `check-verifier-fanout.sh` runs with no arguments in a scratch git repository under
  `%TEMP%` whose only workflow script exports `meta` and carries no marker, it prints the
  `no lens-slot literal` line and exits 1.
  Red when: an empty marker population reads as clean.
  fixture: a two-file repository built the way the fan-out leg's own suite builds its fixtures.
- **AC7** — When `render_lenses.py` runs over eleven scratch catalogues, each breaking one rule of
  §4's list once, each exits 2 and its stderr names the rule's subject: the floor or the parse, the
  field, the kind set, `default_in`, the kind disagreement, the duplicated key and literal, the key
  equal to `diff-review`, the unknown literal, the unfilled literal, the opt-in with nowhere to go,
  and the orphan token.
  Red when: any of the eleven renders output or exits 0.
- **AC8** — When `grep -c 'LENS_SLOTS' tools/workflows/kit.toml tools/workflows/check-protocol-parity.test.sh`
  runs, each file counts at least one.
  Red when: the token is rendered but undeclared, so the kit-placeholders join cannot see it.
- **AC9** — When `grep -n 'one source' tools/workflows/README.md tools/memory-tree/README.md` runs,
  every hit names `lenses.toml`; and `grep -c 'gov:lens-slots' memory/map/features/agent-cap.md`
  counts at least one.
  Red when: a record still calls the literal the source, or the dossier still says the leg only
  delegates.

## 7. Gates

`verifier fan-out` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `kit placeholders (a declared token its adopter substitutes)` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/check-verifier-fanout.test.sh · covers AC3 AC5 AC6 · a scratch harness with a sixth slot in a marked literal, one whose strings carry commas, brackets and a template span, and a whole-tree fixture with no marker, each red against the base gate that counts nothing itself · none
New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC4 AC7 · the render over the shipped catalogue compared with base's literals, a catalogue with an opt-in row added, and one scratch catalogue per refusal rule, red against a tree with no renderer · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **F1 — What does the catalogue call the diff kind's literal?** `presets` and `default_in` name
  literals, and the diff kind has no preset (S1 refuses `preset` beside it). (a) The kind's own name,
  `diff-review`, as a literal name beside the spec-audit presets. (b) A pseudo-preset `diff`, a fourth
  name nothing else spells. (c) A separate field for diff rows, a seventh field S3 does not list. (c)
  fails S3's fixed field list; (b) mints a name for a thing the kind already names. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — Is a lens key unique across the catalogue, or within a literal?** The design-audit preset
  runs `coherence`, `grounding`, `reuse` and `failure-envelope` with briefs aimed at design records,
  not at unit-spec sections (gap-review-04). (a) Globally unique, so those four get new keys and the
  same concern carries two names in lens notes and the lens-yield table. (b) Unique per literal: a key
  may recur in rows whose `presets` are disjoint. (b) keeps one name per concern and costs rule 6
  instead of a simpler rule. Recommendation (b). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (b).
  widens: none · relaxes: none
- **F3 — Does the slot count cap at five or require five?** (a) At most five, the hook's ceiling.
  (b) Exactly five. A literal of four is a default row lost from the catalogue, which runs a review
  narrower than the kit claims and reads as a full one; the swap keeps five after every swap (S2).
  Recommendation (b). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (b). widens: none ·
  relaxes: none
- **F4 — Does the build's grant lift veto 2 for these files?** Every path under `tools/` is a
  governance carrier on `PLAY-dClosedLoop-10`'s list (`open.py --carriers` at `3dca04036`: the
  routed product paths and every kit). `cl-dClosedLoop-0080` names the catalogue in the review kit,
  the harness's literal filled from it and the merge bar's harness check counting slots; the
  renderer, the parity script's render, the descriptor's token, the fan-out leg and the two README
  sentences that state the moved fact are that change. RESOLVED (agent, 2026-10-23, delegated):
  lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the lens catalogue, its render
  into the review harness and the fan-out leg's slot count · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

The seam extended is the kit's install render, `render()` in
`tools/workflows/check-protocol-parity.test.sh:476-487`, which already fills four derived tokens into
the same template; this unit adds a fifth, filled by a python step because the source is TOML.
`python tools/codebase-map/reuse_lookup.py "render a template placeholder from a declared data file
at install"` ranked `render` first with that file among its homes, and `render_charter_blocks` and
`render_role` in `tools/roles/roles_lib.py`, whose `load_workflows` (:339-350) is the kit's precedent
for reading TOML with `tomllib`. The slot count's precedent is the hook's array-literal walk
(`tools/hooks/agent-cap.js:934-968`, `topLevelArgs` at :1362); it is not called, because the hook
retires and its walk runs on a string-blanked view this leg does not have. `python
tools/codebase-map/reuse_lookup.py "count the elements of an array literal in a workflow script"`
returned only name-stem neighbours (`counts`, `measure_typed_counts`), none a literal counter: no
existing seam fits that half. No hit disagreed with source; the recall hit naming `tier2-review.js:705-773`
for the literals is stale, they sit at :774-836 at base.

Recall terms used: `python tools/memory-recall/query.py "how is the review lens set declared and how
many lenses may a harness literal hold" --terms "lens catalogue SPEC_LENSES DIFF_LENSES five-slot
literal agent-cap MAX_LENSES render template FA-1 swap"`
