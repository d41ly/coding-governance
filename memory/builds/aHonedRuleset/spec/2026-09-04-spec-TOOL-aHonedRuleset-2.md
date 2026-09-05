# TOOL-aHonedRuleset-2 — the charter stops restating the micro-format grammar a gate holds

**Status:** SPECCED · rev-3 · 2026-09-04 · node a · Tier-2 · base 102e98f0 · streams tooling+playbook · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |
| [2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md) | spec-audit | TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |

<!-- /gen:spec-records -->

## 1. Goal

Delete from the charter's `§16` the three grammar sentences that `tools/check-microformats.sh`
already enforces as predicates, and leave every sentence that governs what a session EMITS standing
verbatim. This is the charter's own "point at the source, or gate the pair" rule applied to the
charter, on a pair that is already gated.

## 2. Scope (IN)

- **S1 — cut three sentences from the `§16` grammar paragraph.** The paragraph is
  `coding-governance-agents.template.md` lines 363 to 374, measured 1218 bytes with
  `awk 'NR>=363 && NR<=374' … | wc -c`. The three are `G3`, `G5` and `G6` in the §4 table, and each
  maps one-to-one onto a numbered `fail` arm of `tools/check-microformats.sh`.
- **S2 — add one connective sentence** in their place, naming no path, marking the boundary between
  the gated half and the ungated half so a later editor does not re-add what was cut. Measured at 86
  bytes with `printf … | wc -c`.
- **S3 — re-wrap the surviving paragraph to the file's ~100-column house width** and leave every
  surviving sentence's words byte-identical. Only line breaks move.
- **S4 — re-render `AGENTS.md`** with `bash tools/playbook/adopt-playbook.sh --target .`, because the
  rendered region is where a session actually reads this text.
- **S5 — `memory/guides/SESSION-KICKOFF.md` gets its `last-audit` re-stamp in the same commit**,
  because `coding-governance-agents.template.md` is a watched pathspec on line 6 of that file
  (verified: the `watch:` list continues past `.memory-tree.conf` and names the template outright).
  The staged arm at `skills/session-kickoff/manifest-check.sh:412-421` fails check 5 whenever a
  watched file is staged and the staged manifest's block stamp still equals HEAD's, and
  `.githooks/pre-commit:53-55` runs that arm unconditionally — so the bundled re-stamp is the only
  green path at the commit boundary. Re-verify the §B claims the template feeds before stamping;
  the mechanism is unit 5's S8, copied.

## 3. Non-goals (OUT)

- **The `R1` bullet is not touched at all.** It is `coding-governance-agents.template.md` lines 375
  to 381, measured 624 bytes. It governs emission end to end and no gate reads an emission.
- **No sentence that governs emission is cut**, shortened, merged or moved. That includes the pinned
  structural glyphs, the optional-field bracket notation and the syntax-versus-value-bytes rule.
- **No definition line inside the `<!-- microformats -->` fence changes.** The keyword set, the
  shapes and their fields are out of scope; this unit edits prose above the fence only.
- **No other `§16` bullet is edited**, and no other charter section is. The `§8` agent-cap paragraph
  is the census's separate rank-3 row and belongs to its own unit.
- **The size gate's high-water is not bumped.** `tools/template-size-highwater.txt` records 48378 for
  the template and 60930 for `AGENTS.md`; both carriers sit above their record and the advisory WARN
  survives this cut. Bumping would record the growth this build exists to reverse.
- **No emission validator is built.** `PLAY-aFusedCharter-2` §8 F1 is RESOLVED (owner, 2026-08-18) as
  "doc-binding plus a gate over the definitions", with a Stop-hook emission validator named as a
  follow-up and deliberately left behind. That ruling is the reason the emission half must survive in
  prose, and reopening it here would answer someone else's question.

## 4. Design

### The discriminator

`tools/check-microformats.sh` states in its own header that it holds SYNTAX, and that a shape whose
fields are wrong passes. Read literally against its code, its authority is narrower still: it grades
only the lines inside the `<!-- microformats -->` fence pair, and it carries six numbered `fail`
arms. Arm 1 is the frozen `SENTINEL=committed` liveness pin and grades no rule. Arms 2 through 6
grade one rule each.

A sentence is therefore removable when, and only when, a `fail` arm of that script reds on its
violation. Every other sentence in the paragraph either binds an EMISSION, which no gate reads, or
binds the definition block with no predicate behind it — and a rule with no predicate behind it is
carried by the prose alone.

### Inventory

The paragraph's eleven sentences, in file order, with the arm that holds each.

| id | sentence, abbreviated | held by | verdict |
|---|---|---|---|
| G1 | A shape is a HEAD, the joiner, and a TAIL. | nothing directly | KEEP |
| G2 | The head is one keyword from the closed set below, with its case fixed per keyword. | nothing — the set is derived FROM the block, so the gate cannot compare an emission to it | KEEP |
| G3 | The joiner appears exactly ONCE and nothing but the head precedes it. | arms 2 and 3 | **CUT** |
| G4 | Tail fields are separated by the middle dot and by nothing else. | nothing — there is no separator predicate | KEEP |
| G5 | No parentheses, except markdown-link syntax. | arm 4 | **CUT** |
| G6 | No colon as a joiner or a label; a colon survives only glued to a value, as a port. | arm 5 | **CUT** |
| G7 | Placeholders are lowercase angle-bracket names, and alternation inside one is the ASCII pipe. | arm 6 holds the first clause only | KEEP whole |
| G8 | the optional-field bracket notation, which never appears in an emission | nothing | KEEP |
| G9 | Five glyphs are pinned as STRUCTURE. | nothing | KEEP |
| G10 | The grammar binds shape SYNTAX and never value BYTES. | nothing | KEEP |
| G11 | A deploy-time double-brace token inside a shape is a VALUE, not structure. | nothing | KEEP |

The `id` column is this spec's own labelling, and the sentence column is abbreviated so it fits a
table cell. The three sentences that go are quoted verbatim, with their bytes, in the next block.

`G7` is kept WHOLE rather than split. Arm 6 covers `Placeholders are <lowercase-name>` and stops
there; the alternation clause has no predicate. Splitting a sentence to cut its gated half would
leave a rewritten ungated half beside it, which is `memory/gotchas/amendment-leaves-its-other-half-standing.md`
performed deliberately. The 40-odd bytes are not worth it.

`G4` and `G11` are the finding that reranks the census. Both read like definition-syntax rules and
both are therefore natural candidates for a cut justified by the gate — and the gate holds neither.
There is no separator predicate in the script, and nothing rejects a `{{…}}` token, so cutting either
one would delete a rule this repo enforces nowhere.

### The three cut sentences, quoted

Each is deleted whole, including its trailing space. Measured with `printf '%s' … | wc -c`.

| id | exact text | bytes |
|---|---|---|
| G3 | `The joiner ` — ` appears exactly ONCE and nothing but the head precedes it. ` | 78 |
| G5 | `No parentheses, except markdown-link syntax. ` | 45 |
| G6 | `No colon as a joiner or a label — a colon survives only glued to a value, as a port. ` | 87 |

The em dashes are three bytes each, which is why `G6` outweighs its character count.

### The connective that replaces them

One sentence, placed where `G7` ends and `G8` begins, so the paragraph reads as two halves rather
than as a list with holes in it:

`A gate holds the block's own syntax; what follows binds EMISSION, which no gate sees. `

It names no script and no path. The charter is a template an adopter renders, and
`tools/check-microformats.sh` is gov-internal — it appears in `tools/gate-legs.json` and in
`WIRE-INTO-PROJECT.md` nowhere, verified by `grep -n check-microformats` over both. Naming it would
ship a dangling pointer to every adopter, and `§7` already routes a gov session to the leg manifest
for leg names. Measured at 86 bytes.

### The measured recovery, against the census estimate

The census ranked this cut first at an estimated 900 to 1150 bytes. That estimate assumed the
paragraph goes. Measured against a real replacement written to a scratch file and counted with
`wc -c`, the recovery is **126 bytes per carrier**:

| quantity | bytes | how measured |
|---|---|---|
| paragraph today, template lines 363–374 | 1218 | `awk 'NR>=363 && NR<=374' … \| wc -c` |
| paragraph today, `AGENTS.md` lines 427–438 | 1218 | `awk 'NR>=427 && NR<=438' AGENTS.md \| wc -c` |
| the three cut sentences | 210 | `printf '%s' … \| wc -c`, summed |
| the connective added | 86 | same |
| proposed paragraph, re-wrapped | 1092 | `wc -c` over the drafted replacement |
| **net per carrier** | **126** | 1218 − 1092 |
| *why not 210 − 86 = 124* | *2* | *re-wrapping redistributes whitespace; the drafted-file delta governs* |
| **net across both carriers** | **252** | the paragraph is byte-identical in both |

The census estimate was high by roughly an order of magnitude, and the reason is the `G4`/`G11`
finding above: only three of eleven sentences map to a predicate. **The measurement wins and the
census's rank-1 row is worth 126 bytes, not 900.** Whether the ranked list should be re-ordered on
that basis is `§8` F1.

The two paragraphs are byte-identical today — `diff` over the two ranges is empty, and both measure
1218 — because `tools/playbook/render_playbook.py:69` declares
`PLACEHOLDER_RE = re.compile(r'\{\{([A-Z][A-Z0-9_]*)\}\}')`, so the `{{…}}` token in `G11` carries a
horizontal ellipsis, matches nothing, and renders through verbatim. The cut therefore lands the same
126 bytes in each.

### Migration

None. This is a prose edit to one tracked file plus its re-render.

### Rollout

One commit holding the template edit and the re-rendered `AGENTS.md`. `tools/gate-legs.json`'s
`playbook render wiring` leg runs `bash tools/playbook/adopt-playbook.sh --target . --check`, which
byte-compares the rendered region against a fresh render, so the two files must move together or the
bar reds.

### Files touched (estimate)

| file | change |
|---|---|
| `coding-governance-agents.template.md` | lines 363–374 replaced by the re-wrapped paragraph |
| `AGENTS.md` | the same region, regenerated by the adopter, never hand-edited |
| `memory/guides/SESSION-KICKOFF.md` | S5 — re-verify §B, re-stamp `last-audit` in the same commit |

### Alternatives rejected

- **Cut the whole paragraph and let the gate carry the grammar.** This is what the census's estimate
  prices. It deletes `G4`, `G8`, `G9`, `G10` and `G11`, none of which any predicate holds, and `G8`
  through `G10` bind emission specifically. It is the amendment-leaves-its-other-half-standing class
  at paragraph scale.
- **Move the emission half into `R1`.** `R1` is already a distinct rule about markdown framing, and
  merging two bullets to save the second bullet's `- ` marker recovers a handful of bytes for a
  restructure this unit's mechanism does not justify.
- **Name `tools/check-microformats.sh` in the connective.** Rejected above: gov-internal path in an
  adopter-facing template.
- **Add a `{{MICROFORMAT_GATE}}` placeholder** so an adopter's own gate can be named. It needs a
  descriptor key, a value for every adopter, and it costs bytes in a file with eight free. The
  definition block is twenty lines below the paragraph and `R1` already says to copy it.

## 5. Production-readiness checklist

- security — N/A. A prose edit to a tracked governing document adds no write path or surface.
- perf / scale — N/A, except that both carriers get smaller, which is the point.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A. No runtime.
- observability — the `micro-format definitions` leg prints
  `microformats OK — 11 definition(s) graded, 11 keyword(s) derived`, and `govkit`'s acceptance
  matrix pins that prefix at `tools/govkit/matrix.py:61`. A silent change to the definition count
  would surface there.
- risks — the single risk is over-cutting into the emission half. It is addressed structurally by
  the §4 inventory, which grades every sentence rather than the ones the census named, and by AC2,
  which compares the surviving words rather than eyeballing them.
- testing + left-shift gates — no new gate. `tools/check-microformats.sh` is the pre-existing
  left-shift for the half being removed; that is the whole mechanism. The half that stays is
  doc-bound by owner ruling `PLAY-aFusedCharter-2` §8 F1 and remains ungated after this unit, which
  is stated here rather than left for a reader to infer from a green bar.
- migration / rollback — `git revert` of one commit restores both carriers.
- user docs — N/A. The charter is the doc.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'appears exactly ONCE'`, `grep -c 'except markdown-link syntax'` and
  `grep -c 'glued to a value, as a port'` are run over `coding-governance-agents.template.md` and
  over `AGENTS.md`, every one of the six counts is 0.
- **AC2** — When the paragraph before and after is normalized to one whitespace-squeezed string and
  diffed, the only differences are the three sentences of the §4 cut table and the one connective of
  the §4 connective block. Every other word survives byte-for-byte; `git diff --word-diff` over
  `coding-governance-agents.template.md` shows no other changed token.
- **AC3** — When each carrier is squeezed to one line first — `tr -s '[:space:]' ' ' < <carrier> |
  grep -o '<phrase>' | wc -l` — the phrase `Five glyphs are pinned as STRUCTURE` and the phrase
  `R1 — an emitted micro-format is a markdown list item` each occur exactly once, in both carriers,
  and `git diff` shows those sentences unchanged apart from where the line wraps. The squeeze is
  load-bearing: a raw `grep` grades the WRAP, not the sentence. Measured at base, `grep -c 'pinned
  as STRUCTURE'` returns **0** in both carriers today, because the phrase straddles template lines
  369–370, and S3 moves exactly those breaks. All four squeezed counts return 1 at base.
- **AC4** — When `bash tools/check-microformats.sh` runs, it exits 0 and prints
  `microformats OK — 11 definition(s) graded, 11 keyword(s) derived`, unchanged from the pre-edit
  run recorded in §4.
- **AC5** — When `bash tools/check-template-size.sh` runs, it reports
  `coding-governance-agents.template.md` at more than 100 bytes under 49152, against the 8 bytes
  measured before this unit.
- **AC6** — When `bash tools/check-template-size.sh AGENTS.md` runs, it reports `AGENTS.md` more
  than 100 bytes under 64512, and the byte delta equals the template's, because the paragraph is
  byte-identical in both.
- **AC7** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, it exits 0, proving
  `AGENTS.md` was re-rendered rather than hand-edited.
- **AC8** — When `bash tools/check-playbook-parity.sh` runs, it exits 0 and prints
  `pairs in agreement`, so none of its five S2 extractions was disturbed and no kit lost its only
  mention in the charter.
- **AC9** — The re-wrapped range holds no line longer than **102 CHARACTERS**, which is the range's
  measured maximum today (template lines 370 and 372; line 368 is 101). Measured by decoding UTF-8, not by
  `awk 'length'`: awk counts BYTES here, and line 370 is 102 characters but 115 bytes because of the
  pinned glyphs. This is a documented manual check, not a gate — see §7 for why the `line length`
  leg cannot bind it.
- **AC10** — When `git diff -- tools/template-size-highwater.txt` is run at the end of the unit, it
  is empty, proving no `--bump` was taken to make a shrinking file look intentional.
- **AC11** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary, it is GREEN.
- **AC12** — S5 is observed twice. With the template edit and the `SESSION-KICKOFF.md` re-stamp
  staged together, `bash skills/session-kickoff/manifest-check.sh --staged` exits 0; and with the
  template staged ALONE it fails check 5 naming `coding-governance-agents.template.md`. The second
  half is the failing case, so the obligation is proven rather than assumed.

## 7. Gates

Leg names as `tools/gate-legs.json` spells them, which is where they are owned:

- `micro-format definitions` — the mechanism this unit leans on. Must stay green.
- `template size <=48KiB` and `charter size` — the two legs this unit exists to relieve.
- `playbook render wiring` — proves template and `AGENTS.md` moved together.
- `playbook parity` — its five S2 pairs all extract from the `§8` agent-cap paragraph, verified by
  reading `PAIRS` in `tools/check-playbook-parity.sh`; none reads `§16`. Green before the edit and
  must stay green.
- `kickoff-manifest ratchet` — `bash skills/session-kickoff/manifest-check.sh`. Owed because S1
  stages a watched pathspec; `chunk: records`, `subject: repo`, unguarded, so it runs on every bar.
  S5 is what keeps it green, and AC12 exercises both of its arms.
- `line length` — **does NOT constrain the re-wrap.** `tools/line-length-limits.txt:22-23` declares
  450 characters for both carriers, and the widest line in the region today is 102 characters, so no
  re-wrap this unit could plausibly write reds that leg. The ~100-column house width is a property of
  this paragraph and not of the file — 188 of the template's 409 lines exceed 100 characters, to a
  maximum of 449 — so it is ungated and AC9 carries it as a documented manual check instead. The leg
  must stay green, but it is not evidence about the wrap.
- `micro-format gate selftest` — a `subject = kit` leg, off the default bar. It writes its own
  synthetic `charter.md` at `tools/check-microformats.test.sh:30` and never reads the real template,
  so this unit cannot red it. Said here rather than left as an unexplained absence.

No new gate. Adding one would duplicate `tools/check-microformats.sh`, and the rule this unit
removes is the one that script already holds.

## 8. Open questions

- **F1 — does a 126-byte recovery still earn a Tier-2 unit, and does the census's ranked list get
  re-ordered?** The census ranked this first on a 900-to-1150-byte estimate. Measured, it is 126.
  *Recommendation: land it anyway, and re-rank separately.* 126 bytes takes the template from 8 bytes
  free to 134 and `AGENTS.md` from 6 to 132, which is the difference between a file that cannot take
  a sentence and one that can. The rank-2 row moves 1200 to 1400 bytes out of a different carrier and
  is unaffected by this measurement, so the re-ranking question is the census's to answer, not this
  unit's.
- **F2 — does the connective survive, at 86 bytes?** Dropping it lifts the recovery from 126 bytes
  to roughly 210, the exact figure depending on how the range re-wraps without it. *Recommendation: keep it.* Its job is to stop the next editor re-adding `G3`, `G5` and `G6`
  on the reasonable-looking grounds that the paragraph reads incomplete without them, and to mark the
  gated/ungated boundary that is this cut's whole risk. Eighty-six bytes to prevent the cut being
  silently reverted is cheap.
- **F3 — an adopter's rendered charter loses the grammar and has no gate to replace it.**
  `tools/check-microformats.sh` does not ship; the adopter receives the definition block, `R1`, and
  the surviving emission rules, and nothing grades their block if they add a shape to it.
  *Recommendation: accept, and do not build for it here.* An adopter's block arrives rendered and
  correct, `R1`'s closing instruction is to copy a bullet rather than to compose one, and the
  alternative is shipping a gate no adopter asked for. If the owner wants it covered, it is a
  deployer-stream unit about which top-level gov scripts join the adopter payload, which is adjacent
  to `TOOL-aScouredKit-23` and not to this cut.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-04 · folded the round-1 spec audit
  ([2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md)),
  three findings. **Audit S1** — scope item S1 stages a watched pathspec with no re-stamp in scope
  and §7 named no ratchet leg: added S5 (the
  bundled `memory/guides/SESSION-KICKOFF.md` `last-audit` re-stamp, unit 5's S8 copied), its
  files-touched row, the `kickoff-manifest ratchet` leg in §7, and AC12 to observe both arms.
  **Audit A1** — AC3 grepped `pinned as STRUCTURE`, which returns 0 in both carriers because the phrase
  straddles template lines 369–370, so it graded the wrap S3 moves rather than G9's survival: AC3
  now squeezes whitespace first and counts `Five glyphs are pinned as STRUCTURE`, verified at 1 in
  each carrier. **Audit A8** — §7 called `line length` the re-wrap's only constraint, but
  `tools/line-length-limits.txt:22-23` declares 450 for both carriers so it cannot bind; §7 now says
  the width is ungated and AC9 became a character-counted manual check at the region's measured
  102-character maximum. The audit reported that maximum as 115, which is its BYTE length — awk's
  `length` counts bytes here and line 370 carries the multi-byte pinned glyphs. All three §8 forks
  stay UNRESOLVED and unsigned.

- rev-3 · 2026-09-04 · fold-verification nits: AC9's 102-character line list dropped line 368
  (101 characters, 102 bytes); §4's cut table now states why the 210 − 86 decomposition is 2 bytes
  short of the measured 126, and F2's 210 is marked approximate for the same reason.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade the charter micro-format definition block against
its grammar"` returns no code seam this unit extends, and that is the correct answer: the seam
already exists and is a gate leg, not a function. The probe named it directly —
`micro-format definitions [gate-legs]` and `micro-format gate selftest [gate-legs]`, both claimed by
the `playbook` dossier at `memory/map/features/playbook.md` — alongside
`amendment-leaves-its-other-half-standing.md [gotcha-classes]`, which is this unit's named risk. No
new machinery is built, no inventory key is created, and nothing in `tools/` is touched. The corpus
probe added the governing prior record: `PLAY-aFusedCharter-2` §8 F1, RESOLVED (owner, 2026-08-18) as
"doc-binding plus a gate over the definitions", with the emission validator left as a follow-up —
which is the ruling that makes the emission half unremovable, and `TOOL-dScaffoldedMirror-10` in
`memory/backlog/TOOL.md` supplied the standing "the charter POINTS and must be net-negative in bytes"
precedent this unit follows.

Recall terms used: `python tools/memory-recall/query.py "why does the charter restate the
micro-format grammar that check-microformats.sh already gates" --terms "micro-format grammar charter
definition block emission joiner placeholder gate template size ceiling restatement"`
