# TOOL-aMendedFleet-91 — a spec's status header declares a records-only deliverable, and the product-commit signal reads it

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · closes TOOL-aProbedToolkit-18 · advances TOOL-aReplayedCard-6 · order 91

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`closed_specs_with_no_product_commit` reds a CLOSED unit that no product commit names, and a unit
whose deliverable is records, such as a journal, an evaluation or a census, correctly has none. Today
such a unit's only way out is a row in `memory/project/trace-waiver.txt`, written after it closes,
into a list that promises to shrink; three of its nine rows are this shape. And because the signal
joins by build slug, a waiver row goes stale the moment a sibling unit of the same build lands a
product commit, which `TOOL-aReplayedCard-6` hit twice. This unit lets a spec declare
`records-only` in its status header at speccing time, where its review sees it, and has the signal
read that declaration before the slug join, so a records-only unit needs no row and no sibling can
stale one.

## 2. Scope (IN)

- **S1** — THE VERB. A status header may carry the tail token `records-only`, a `·`-separated field
  of exactly those bytes. It is legal at any status and inert until the spec is CLOSED. It is read on
  the status line alone, never from body prose. Observed by AC1 and AC3.
- **S2** — THE READ. In `signal_closed_specs_untraceable` of `tools/drift-audit/drift_report.py`, a
  spec that passes the existing terminal, id, date, cutoff and slug guards and carries the verb is
  counted in `of` and then set aside BEFORE the slug is matched against commit subjects, so neither
  the presence nor the absence of a sibling's product commit can change its reading. The record gains
  `records_only`, the sorted list of the paths so set aside, so the exemption is auditable from
  `--json` rather than silent. Observed by AC1 and AC4.
- **S3** — ONE FACT IN ONE PLACE. A spec carrying the verb and also named by a waiver row leaves the
  row unconsumed, so the existing stale-waiver sweep reports it, and that row's note names the
  records-only declaration as one of the reasons a row can be left over. Observed by AC2.
- **S4** — THE POINTERS. The `TRACE_WAIVER` comment in `tools/drift-audit/drift_signals.template.py`,
  the signal-6 comment block in `tools/drift-audit/drift_signals.py` and the header comment of
  `memory/project/trace-waiver.txt` send a records-only unit to the verb and keep the waiver for the
  other shape it serves, a unit whose product landed before the id-in-subject convention. The
  drift-audit README's signal-6 row or a paragraph beside the table names the verb. Observed by AC5.
- **S5** — The three RECORDS-ONLY rows in `memory/project/trace-waiver.txt` stay, and their CLOSED
  specs' headers are not edited. NOT OBSERVED by a criterion here: it is an absence of change, and
  §8 F2 records why.
- **S6** — Self-test arms in `tools/drift-audit/selftest.py`: a CLOSED fixture spec with no product
  commit and the verb reads clean and is listed in `records_only`; the same spec with the verb and a
  waiver row reports the row stale; a lookalike token and the word in body prose exempt nothing.
  NOT OBSERVED by a criterion here: the suite runs once at the close, and the arms are declared
  under `New arm:` in §7.

## 3. Non-goals (OUT)

- Documenting the verb in `memory/TEMPLATE-SPEC.md`'s header section. That file is a governance
  carrier and the owner's diet grant covers stale facts, pointers and structural cuts, not new header
  grammar; §8 F1 hands it off.
- Joining signal 6 by unit id instead of by slug, the other half of `TOOL-aReplayedCard-6`, which
  the waiver's pre-cutoff rows still depend on. This unit advances that ask and does not close it.
- Grading whether a spec declaring the verb really ships no product. The closing review reads the
  header in the diff; a gate here would need to parse §4's file estimate and judge it.
- Any change to hygiene check 12's header grammar. It anchors the header's prefix only, so the tail
  token is already legal, and nothing there needs to know it.
- Bumping the drift-audit kit version, owed once at the build's close.

### Edges

- **hands-off** external — the verb's line in the spec format's header section, a governance-carrier
  edit for the owner, filed as an ask at the close.
- **hands-off** external — joining signal 6 by unit id, the remainder of `TOOL-aReplayedCard-6`.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `8312d315`, whose bytes under `tools/drift-audit/` and of
`memory/project/trace-waiver.txt` equal base `7af5f564`'s.

- `signal_closed_specs_untraceable` reads the first 4000 bytes of each spec, keeps CLOSED specs past
  `TRACE_CUTOFF` with an own id and a slug, increments `checked`, and passes a spec whose slug appears
  as a word in any `TRACE_GLOBS` commit subject. Only then does it consult the waiver. A waiver row is
  therefore unconsumed, and reported stale, whenever any commit of the same build names the slug.
- `memory/project/trace-waiver.txt` holds 9 rows, 3 of them RECORDS-ONLY:
  `TOOL-aScannedThrottle-1`, `TOOL-aWeighedCompass-1` and `TOOL-aProbedToolkit-1`. PINNED, measured
  2026-10-04.
- Unit 57 measured that list's low-water at 6 and today's count at 9, so it reads regrown; each new
  records-only unit under today's rule grows it again.
- Hygiene check 12 tests the header against a pattern anchored on its prefix up to `base <sha8>`, and
  `gen_build_index.py` reads only `order`, `closes` and `advances` from the tail, so a new tail token
  reds nothing.
- `git grep` finds no status header carrying `records-only` today.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `records-only` | status-header tail token | none |
| `records_only` | JSON key of signal 6's record | none |
| `_RECORDS_ONLY` | module regex in `drift_report.py` | none; module constants carry no naming cell |

### Data model

```text
  **Status:** CLOSED · rev-2 · 2026-10-20 · node a · Tier-1 · base 7af5f564 · streams tooling · records-only · order 7
```

The token is matched as a whole field between `·` separators, or at the line's end, on the line the
existing `_STATUS` pattern anchors, so `records-only-ish` and a sentence in §1 do not match.

### Rollout

Forward only: a spec opts in when it is written or next revised. Other drift-audit units of this
build move the same files and are ordered first, and this unit rebases onto them.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/drift_signals.template.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/project/trace-waiver.txt`

### Alternatives rejected

- **A records-only key in `drift_signals.py` listing spec paths.** It is the waiver file under another
  name, written after the fact by someone other than the spec's author.
- **Keep the waiver and match its rows by unit id.** It fixes the staleness but keeps a shrink-only
  list growing by one row per records-only unit, which unit 57's low-water grading would then report
  as regrown every time.
- **Infer records-only from a spec whose §4 file estimate names no product path.** An estimate is an
  estimate, and a signal that decides from it inherits every wrong guess silently.

## 5. Production-readiness checklist

- security — N/A: reads tracked spec headers the signal already reads.
- perf / scale — one regex on a line already in hand; no new git spawn.
- error / empty / loading states — a spec without the verb is judged exactly as before; a verb on a
  non-terminal spec does nothing.
- observability — `records_only` lists every exempted path in `--json`.
- risks — any author can declare the verb on a unit that does ship product, and the signal will then
  not ask for the commit. The declaration sits in the spec's header, where the closing review reads
  it, and `records_only` lists it; the waiver it replaces had the same trust model with less
  visibility.
- testing — AC1 to AC5 here; the arms in S6.
- migration — N/A: forward only; the three existing rows keep working.
- user docs — S4.

## 6. Acceptance criteria

- **AC1** — When, in a scratch clone of the unit's tip under a short `%TEMP%` path, the
  `TOOL-aScannedThrottle-1` row is deleted from `memory/project/trace-waiver.txt` and
  `python tools/drift-audit/drift_report.py --json` runs, the `closed_specs_with_no_product_commit`
  value rises by one and a detail row names that spec; when ` · records-only` is then appended to that
  spec's status line, the value returns to its unedited reading and `records_only` lists the spec's
  path.
  Red when: the verb is not read, or the exempted spec is not listed.
- **AC2** — When, in that clone, the waiver row is restored while the verb stays, the report carries a
  `(stale waiver)` detail row for that spec whose note names the records-only declaration.
  Red when: the same fact declared in two places passes silently.
- **AC3** — When, in that clone with the row still deleted, the verb is replaced by
  ` · records-only-ish`, and separately when the words `records-only` are added only to the spec's §1
  prose, the value stays one above its unedited reading in each case.
  Red when: a lookalike token or a body mention exempts a spec.
- **AC4** — When `python tools/drift-audit/drift_report.py --json` runs on the unedited tip, the
  signal's value equals the value the same command reads at the base, and `records_only` is empty.
  Red when: the read changes a verdict for a spec that declares nothing.
  figure: DERIVED at observation time at both shas.
- **AC5** — When `grep -c "records-only" tools/drift-audit/README.md tools/drift-audit/drift_signals.template.py memory/project/trace-waiver.txt`
  runs, each file reports at least 1.
  Red when: a records-only author is still sent only to the waiver list.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `recall floor` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a CLOSED records-only fixture spec with no product commit, the same spec also waived, a lookalike token and a body mention, staged red by matching the verb anywhere in the spec text · `CHECK_FLOOR` moves by the checks the arms add

## 8. Open questions

- **F1** — Where is the verb documented?
  Options: `memory/TEMPLATE-SPEC.md`'s header section, beside `order`, `closes` and `advances`; the
  drift-audit README and the comments that send authors to the waiver today. The first is a
  governance-carrier edit, which the build's diet grant does not name, so it trips M3's veto 2.
  RESOLVED (agent, 2026-10-04, delegated): the drift-audit README and the three comments, per S4; the
  template line is handed off to the owner as an ask filed at the close.
- **F2** — Do the three RECORDS-ONLY waiver rows migrate to the verb?
  Options: edit the three CLOSED specs' headers and drop the rows, which drains the list to its
  low-water; or leave both. A landed record is frozen and this repo does not rewrite one to clear a
  hit, and editing a CLOSED header is the act the waiver file's own header warns pulls a spec into a
  population it was never judged by.
  RESOLVED (agent, 2026-10-04, delegated): leave both, per S5; the verb is forward only.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, split from unit 57's F1; the waiver rows and signal 6's guard
  order re-read at `8312d315`.

## 10. Reuse audit

The seam extended is `signal_closed_specs_untraceable` in `tools/drift-audit/drift_report.py`: its
existing head read, its `_STATUS` anchor and its stale-waiver sweep, which S3 reuses unchanged as the
check that the two declarations never coexist. `python tools/codebase-map/reuse_lookup.py "exempt a
closed spec from a product-commit linkage check by a declaration in its status header"` ranked
`load_affordance_exempt` and `render_affordance_exempt` in the map kit, a shrink-only exemption list
of the waiver's shape rather than a header declaration, then `parse_spec_h1` and `build_spec_path_re`
in `tools/memory-tree/tree_lib.py`, which read a spec's title and path, not its tail; the tail verbs
`order`, `closes` and `advances` are parsed in `tools/memory-tree/gen_build_index.py`, a kit this one
may not import. No existing seam reads a tail token for drift-audit, so the regex lives beside
`_STATUS`. The scan names `.sh` as unscanned; no shell file reads spec headers for this signal.
Recall returned `TOOL-dMuffledSentinel-2` on the waiver's declarable path, `TOOL-aReplayedCard-6` on
slug-joined rows going stale, `TOOL-aScannedThrottle-1`, the first records-only row, and
`TOOL-aProbedToolkit-18` itself. Where the report and the tree disagree: the synthesis filed the ask
as unshipped, and it is; its immediate red was cleared by a waiver row on 2026-09-20, which is the
workaround this unit makes unnecessary for the next records-only unit.

Recall terms used: `python tools/memory-recall/query.py "how does a CLOSED records-only unit escape the
product-commit linkage signal" --terms "closed_specs_with_no_product_commit records-only trace-waiver
TRACE_WAIVER status header verb exemption shrink-only pin"`
