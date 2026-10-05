# TOOL-aEvidencedLens-10 — `review_replay.py` scores a spec-audit report against a past one by file and section

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-1 · base 028b5cac · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-10-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-10-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-11 |

<!-- /gen:spec-records -->

## 1. Goal

The owner asked for the improved spec audit to be TESTED on this build. `tools/workflows/review_replay.py`
is the repo's one recall instrument, and it reads only diff-review records, scored by file and line.
A spec finding has no line: the harness writes its ref as `<file>:<where>`, a section address. This
unit extends the same tool so a spec-audit record can be the known side and a spec-audit report the
candidate, matched by file and SECTION, which is the instrument the main loop needs to compare the
improved harness against round 1 on this build's own specs.

## 2. Scope (IN)

- **S1** — A KNOWN record whose first non-blank line starts `**Serves:** spec-audit` is read in spec
  mode, from its `## Appendix — every finding` only. With no appendix it is REFUSED as `no-appendix`,
  never scored as a recall of zero; there is no legacy-table fallback in spec mode, because no
  spec-audit record carries the legacy table's raw-id column. Observed by AC2.
- **S2** — In spec mode a ref is split at the first `:` after its path, the drive prefix handled as
  `extract_line_ref` handles it, and the section is extracted from the address by
  `extract_section_ref`: the first `§<n>` or `section <n>`, case ignored; failing both, the first
  `S<n>`, `AC<n>` or `F<n>` reads as §2, §6 or §8, the sections the spec format puts those items in. An
  address yielding none of these is UNSCORABLE and counted. Observed by AC3.
- **S3** — Scoring reuses `measure_recall` unchanged: the section number rides the location slot and
  the window is forced to 0, so a match is the same file and the same section. `--window` is ignored in
  spec mode and the candidate line prints `address section` where it prints `window N`. Observed by
  AC4.
- **S4** — A candidate whose first non-blank line names the OTHER kind's `**Serves:**` binding is
  REFUSED as `kind-mismatch`, naming both kinds. A candidate with no binding line is read in the known
  record's mode. Observed by AC5.
- **S5** — The `replay: known` line carries `kind spec-audit` and the subject pins, or
  `subjects none-stated`; spec mode prints no range and never refuses for one. The pins are every
  `<path>@<hex>` pair on the lines AFTER the `**Serves:**` binding line and before the first `## `
  heading, whether one line carries them all or each sits on its own bullet, as this build's round-1
  record writes them. The binding line itself is never the pin line. Diff mode's `no-range` refusal
  is unchanged. Observed by AC6.
- **S6** — When the known set came from an appendix, in either mode, a `per-lens known:` line follows
  the existing `per-lens:` line, giving per known-side lens the items it confirmed and how many a
  candidate matched. The existing line is byte-identical. Observed by AC7.
- **S7** — `--selftest` gains one named arm per behaviour S1 to S6, at least six, named
  `no-appendix`, `section-ref`, `window-0`, `kind-mismatch`, `subject-pins` and `per-lens-known`,
  and `ARMS_DECLARED` rises by the number added. Observed by AC1.
- **S8** — `tools/workflows/README.md`'s replay section and the tool's module docstring state spec
  mode, its section rule and its refusals. Observed by AC8.
- **S9** — Diff mode is unchanged: every existing arm passes unedited. Observed by AC1.

## 3. Non-goals (OUT)

- Spec records in `--corpus`. A corpus listing resolves ranges to pick a replayable round; a spec
  record has subject pins, not a range, and the main loop names its known record directly.
- A spec-mode legacy table reader. The diff-mode legacy reader scores none of the 168 records that
  open with a spec-audit binding (§4 Evidence), and none of them carries the appendix; the first
  appendix-bearing spec record will be this build's own round 1.
- Any change to the harness. This unit reads what `tools/workflows/tier2-review.js` writes.
- A precision figure. As in diff mode, a candidate-only finding is listed, never counted false.
- Running the live replay. That is the main loop's, which holds `Workflow`.
- A kit version bump. The main loop bumps once at the close (shared invariant 7).

### Edges

none

## 4. Design

### Evidence

Read at base `028b5cac`.

- `tools/workflows/review_replay.py` reads the known side through `parse_record_findings`, which takes
  the appendix when the heading is present and the legacy table otherwise, then refuses with
  `no-scorable` and `no-range`. `parse_candidates` maps confirmed appendix rows through
  `extract_line_ref`, whose `LINE_REF` regex needs `:<digits>`, so a spec ref such as
  `spec/x.md:§2 S5` is unscorable today and a spec report would be refused as `no-scorable`.
- The harness writes a spec finding's ref as `${f.file}:${f.where}`
  (`tools/workflows/tier2-review.template.js:812`), and `where` is a free string the spec finding
  schema requires.
- The harness's spec synthesis orders the record's opening (`:1232-1248`): the `**Serves:**` binding
  line FIRST, then the title, then the subjects as `<path>@<blob>`. This build's round-1 record,
  `reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md`, writes each pin on its own
  bullet under a `**Round: 1.**` line. The record's opening line is therefore never the pin line.
- `measure_recall` matches on `check_same_file` and `abs(line - line) <= window`; with the window 0
  and the section in the `line` slot it is an exact section match and needs no edit.
- MEASURED 2026-10-05, PINNED: `grep -rl "^\*\*Serves:\*\* spec-audit" memory/builds` lists 244 files,
  and none of them carries `## Appendix — every finding`. Of those, 168 OPEN with the binding, and
  `parse_record_findings` run over them in a scratch probe scored none: 133 refused `liveness`, 23
  `no-count`, 10 `no-scorable` and 2 `no-range`.

### Inventory

| Name | Cell | Kind |
|---|---|---|
| `extract_section_ref` | `py.function` | new function: ref -> `(path, section)` or None |
| `read_record_kind` | `py.function` | new function: text -> `spec-audit`, `diff-review` or None |
| `extract_subject_pins` | `py.function` | new function: text -> `[(path, hex)]` |
| `measure_replay` | `py.function` | new function: known text, candidate text, window -> the mode, both sides, the forced window and the score, or the refused side and its error |

`measure_replay` is the one path from two texts to a score, called by `main` and by the `window-0`,
`kind-mismatch` and `per-lens-known` arms alike, so the S3 window forcing and the S4 kind check are
exercised where the CLI runs them rather than re-stated in an arm.

Each was checked with `python tools/lexicon/lexicon.py --suggest <name> --as py.function` and
answered OK. `parse_record_findings`, `parse_candidates` and `print_score` take the mode as a
parameter; no parser is duplicated.

### Files touched (estimate)

- `tools/workflows/review_replay.py`
- `tools/workflows/README.md`

## 5. Production-readiness checklist

- security — reads two files the caller names; no write, no subprocess in the new path.
- perf / scale — one regex per row.
- error / empty / loading states — no appendix, a kind mismatch and no scorable row are each a named
  refusal at exit 2; an address with no section is counted unscorable.
- observability — the known line names the kind and the pins; both per-lens lines print.
- risks — the section heuristic can mis-read an address naming two sections; it takes the first,
  and a mis-read is a MISSED line the operator can read, never a silent score.
- testing — `--selftest` arms, fixture-only.
- migration — none.
- user docs — the README replay section (S8).

## 6. Acceptance criteria

- **AC1** — When `python tools/workflows/review_replay.py --selftest` runs, every arm prints `ok`, the
  output names an arm for each of `no-appendix`, `section-ref`, `window-0`, `kind-mismatch`,
  `subject-pins` and `per-lens-known`, and the closing line reads `selftest: K/K arms` where K
  equals `ARMS_DECLARED` and is at least 25, the base 19 plus six.
  Red when: an existing diff arm moved, a behaviour of S1 to S6 has no arm, or a new arm was stranded
  and `ran` falls short of the count.
  figure: K is DERIVED from the arms list at run time; 19 is the base count, PINNED at `028b5cac`.
- **AC2** — When the tool runs `--known` on a fixture spec-audit record with no appendix, it exits 2
  with `REFUSED known` and `no-appendix`.
  Red when: the record is scored, or falls through to the legacy table reader.
  fixture: written into the run's scratch directory; the tree holds no appendix-bearing spec record.
- **AC3** — When `extract_section_ref` reads the refs "x.md:§2 S5", "x.md:section 2, S5", "x.md:S5",
  "x.md:AC3", "x.md:F1", "C:/r/x.md:§4 Design" and "x.md:status header", it returns sections 2, 2, 2,
  6, 8, 4 and None, the drive-lettered path keeping its suffix.
  Red when: a scope or acceptance id with no section number is unscorable, or the drive prefix
  breaks the split.
- **AC4** — When a spec known record's `x.md:§2 S1` item is scored against candidates `x.md:section 2,
  S4` and `x.md:§3`, the first is MATCHED and the second is CANDIDATE-ONLY, with `--window 10` given.
  Red when: the window lets §3 match §2.
- **AC5** — When the known record is a spec audit and the candidate opens with `**Serves:**
  diff-review`, the tool exits 2 naming `kind-mismatch` and both kinds; when the known record is a
  diff review and the candidate opens with `**Serves:** spec-audit`, it exits 2 the same way; and a
  candidate with no binding line beside a spec known record is scored by section.
  Red when: a report is scored against a record of the other kind in either direction, or an
  unbound candidate is read in diff mode beside a spec record.
- **AC6** — When a spec known record opens with `**Serves:** spec-audit x` and its next non-blank
  line is `a.md@abc1234, b.md@def5678`, the `replay: known` line carries `kind spec-audit` and both
  pins; when the known record's head is copied from
  `memory/builds/aEvidencedLens/reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md`,
  one pin per bullet, it carries all eleven; with no pin it carries `subjects none-stated` and is
  still scored.
  Red when: spec mode refuses for a missing range, reads the binding line as the pin line, or misses
  pins written one per bullet.
- **AC7** — When an appendix known set carries lenses `coherence` and `reuse`, the output carries a
  `per-lens known:` line naming each with its known and matched counts, and the existing `per-lens:`
  line is byte-identical to its diff-mode form.
  Red when: the known side's lenses are not reported, or the candidate line changed shape.
- **AC8** — When `grep -n "spec-audit" tools/workflows/README.md` runs, the replay section names spec
  mode, the section rule and the `kind-mismatch` refusal.
  Red when: the README still says the known set is a past diff-review record only.

## 7. Gates

`review-replay selftest` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/review_replay.py · `no-appendix` a spec-audit record with no appendix, which a fallback would score as zero · `ARMS_DECLARED` raised by one
New arm: tools/workflows/review_replay.py · `section-ref` the AC3 refs, which the base `extract_line_ref` cannot score · `ARMS_DECLARED` raised by one
New arm: tools/workflows/review_replay.py · `window-0` a §3 candidate beside a §2 item under `--window 10` · `ARMS_DECLARED` raised by one
New arm: tools/workflows/review_replay.py · `kind-mismatch` both directions, and an unbound candidate beside a spec record · `ARMS_DECLARED` raised by one
New arm: tools/workflows/review_replay.py · `subject-pins` a one-line pin set after the binding line and a one-pin-per-bullet head · `ARMS_DECLARED` raised by one
New arm: tools/workflows/review_replay.py · `per-lens-known` an appendix known set across two lenses · `ARMS_DECLARED` raised by one

## 8. Open questions

- **F1 — Does a spec known record lacking the subject-pin line refuse, as a diff record lacking a
  range does?** A diff range is what a corpus replay re-runs; spec mode has no corpus route, and the
  pin line is written by the synthesis agent, which may omit it.
  RESOLVED (agent, 2026-10-05, delegated): print `subjects none-stated` and score, S5. A refusal
  would make the build's own round-1 record unusable on one omitted line.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the spec brief's unit 10 and `review_replay.py` read at
  `028b5cac`.
- rev-2 · 2026-10-05 · §4 §7 S5 S7 AC1 AC5 AC6 · round-1 spec audit fold. Id 20 (MEDIUM): S7 and AC1
  name the six arms and require K of at least 25, and §7 declares one arm each. Id 28 (MEDIUM): S5
  reads the pins after the binding line, never from it, one line or one per bullet, and AC6's
  fixtures open with the binding line, one copied from this build's round-1 record. Id 21 (LOW): AC5
  observes `kind-mismatch` in both directions and an unbound candidate beside a spec record.
- rev-3 · 2026-10-05 · §4 · build pass. The Inventory adds `measure_replay`: the S3 window forcing
  lived in `main` alone, where no fixture-only arm can reach it, so `window-0` could not go red on a
  build that dropped it. One function now carries the known-to-score path for `main` and the arms.

## 10. Reuse audit

The seam extended is `tools/workflows/review_replay.py` itself, built by `TOOL-aSightedSkeptic-9`:
`parse_appendix_rows`, `parse_record_findings`, `parse_candidates`, `measure_recall` and `print_score`
take a mode, and `measure_recall` is reused unedited by putting the section in its location slot at a
window of 0. No second tool. `python tools/codebase-map/reuse_lookup.py "score a spec audit report
against a past spec audit by file and section"` returned name-stem neighbours (`score` in
`tools/memory-recall/bench.py`, `render_report`) and no recall scorer other than this file. The recall
query's top hit was `TOOL-aSightedSkeptic-9`, whose §3 kept the tool diff-only and harness-free, both
of which this unit keeps.

Recall terms used: `python tools/memory-recall/query.py "how is a review report scored for recall against a past round, and can a spec audit be replayed" --terms "review_replay recall known candidate appendix spec-audit section address where lens replay corpus"`
