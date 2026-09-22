# TOOL-aTetheredRecord-5 — the rendered Records table and the coverage join

**Status:** CLOSED · rev-4 · 2026-08-20 · node a · Tier-2 · base 96141aed · streams tooling · ratified 2026-08-17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-17-review-TOOL-aTetheredRecord-1-1.md](../reviews/2026-08-17-review-TOOL-aTetheredRecord-1-1.md) | spec-audit | TOOL-aTetheredRecord-1 TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-3 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-6 TOOL-aTetheredRecord-7 |

<!-- /gen:spec-records -->

## 1. Goal

Put the binding where a reader lands, and compute the one thing no grep can: which spec ids no record
names. A build README's generated region already lists every unit; it says nothing about the records
beside them. This unit renders each record under the ids it serves and derives the two-sided gap.

## 2. Scope (IN)

- **S1** — The generated region gains a records table, below the existing `Records live under …`
  sentence (whose folder list is DERIVED from the record kinds present, so it is not always three), listing each record with the ids it serves and its recorded rev where one is
  present. Rows are sorted by path; links use the build-relative form the region already emits.
- **S2** — Two derived lines, computed from the same two functions `TOOL-aTetheredRecord-2` supplies:
  the spec ids no record of ANY kind names, and — now that Fork E ratified the kind vocabulary — the
  spec ids no `spec-audit` record names, which is the closest this build gets to the M4 question.
- **S3** — The table carries the kind as its own column, so a reader can tell a spec audit from a
  closing diff review without opening either.
- **S4** — `--selftest` arms covering a build with records, a build with none, and the population
  assertion that keeps the table from silently rendering empty.
- **S5** — Bump `KIT_MEMORY_TREE_VERSION` and the `gov:kit memory-tree@` markers, re-rendering the
  three doc pairs: `gen_build_index.py` is in the verdict-epoch delegate set and §4 changes it.

## 3. Non-goals (OUT)

- **Neither derived line is labelled "unreviewed".** With the kind token the second line can restrict
  to `spec-audit` records, which is much closer to M4 — but M4 also selects on REV, and the reviewed
  rev is optional under Fork C. So the line reports ids no spec-audit record names EVER, not ids
  whose current rev is unreviewed. A spec reviewed at rev-1 and since bumped to rev-4 does not appear.
  The rendered label says exactly that; an "unreviewed" label would be a coverage claim the data
  cannot support, which is worse than an honest gap.
- **The existing sentence is not replaced.** It is kept, because the strip helper that manages it
  drives nine existing arms; replacing it removes the thing a mis-segmentation arm detects the
  absence of.
- **No second marker pair.** The table renders inside the one generated-region pair that exists.
- **No authored input.** The render derives entirely from the record head lines and the spec H1s.

## 4. Design

### Data model

Two derivations, both from `TOOL-aTetheredRecord-2`'s functions:

- **records to ids** — one row per record, the ids it serves, the rev where present. A record
  carrying the unbound form renders with its reason rather than an id list, so the escape is visible
  in the index and not only in the file.
- **ids to records, inverted** — the spec-defined ids of this build minus every id any record names.
  This is the two-sided computation, and it is the reason the render is worth a generator change at
  all: a filename cannot express it and a grep cannot perform it.

### Rollout

Lands after check 21, on a corpus already conformant, so the first render is complete rather than
mostly empty. Once rendered, the region is byte-compared like the rest of the generated index — which
means a later edit to a record's binding that is not re-rendered becomes a red, closing the drift
window the authored line would otherwise have.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` and every build README the re-render touches.

### Alternatives rejected

**Replace the folder sentence with the table.** It reads tidier and it deletes the anchor nine arms
depend on, including the one that detects a mis-segmented record selector by noticing the sentence
went missing. Additive keeps both.

**Render a whole-build binding as a wildcard that expands at render time.** Rejected in the design
pass. A build's roster is a reservation range in which two thirds of the ids in this corpus have no
spec, so an expanding wildcard rewrites history in the false-green direction as the roster moves. Ids
are enumerated at authoring time.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one extra pass over a corpus of 76 records during a render that already walks them.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a build with no records renders neither the table nor the derived
  line; the arm for that case is explicit.
- observability — the table IS the observation; the derived line is the coverage report.
- risks — an empty table rendering silently is the failure that matters, so a positive-population arm
  is a scope item rather than an afterthought. The byte-compare is CRLF-sensitive on this platform
  and the generated paths are already pinned to LF.
- testing + left-shift gates — `--selftest`, plus the marker-contract harness over the region.
- migration / rollback — one re-render commit; revertible.
- user docs — the region is self-describing and already carries a do-not-hand-edit notice.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs after `--write`, it is
  clean across every build.
- **AC2** — When `memory/builds/aSiftedPlaybook/README.md` is read, its generated region lists each
  of that build's records with the ids it serves.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --write` renders a build whose records
  leave a spec id unnamed, the derived line names that id, and the line is absent from a build whose
  every id is named.
- **AC3b** — When a build holds a `diff-review` record but no `spec-audit` record for a given id, the
  second derived line names that id while the first does not, and its rendered label says it reports
  ids never spec-audited rather than ids unreviewed at their current rev.
- **AC4** — When `bash tools/memory-tree/marker-contract.test.sh` runs, it is green — the table sits
  inside the single existing generated-region pair.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, the existing arms over
  the folder sentence all still pass, and the new positive-population arm fails against a stub that
  renders an empty table.
- **AC6** — When `bash tools/run-gates.sh` runs, every leg is green.

## 7. Gates

`memory hygiene (20 checks)` — check 9's byte-compare · `build-index selftest` ·
`marker-region contract` · `verdict epoch` · `kit version markers` ·
`bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none — the forks below are RESOLVED and kept for the record.

**Fork B — does this unit land at all?** RESOLVED (owner, 2026-08-17): build it, after check 21. It
buys the coverage join and converts the authored binding into a byte-compared one, which is what
stops a stale binding from sitting unnoticed.

**Fork E — does a record declare a relation KIND?** RESOLVED (owner, 2026-08-17): yes, now, against
this spec's recommendation to defer. The vocabulary is DERIVED from the measured corpus rather than
invented under time pressure — the four tokens and their evidence are in `TOOL-aTetheredRecord-2` §4
— which answers the recommendation's actual objection.

What the resolution does NOT buy is stated in §3 rather than left implied: the kind token sharpens
the derived line from "no record" to "no spec audit", and it cannot reach M4's rev-keyed question,
because Fork C left the reviewed rev optional. Two of the owner's resolutions interact here, and this
is the interaction.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the adversarial design pass recorded under this build's
  `build/` folder.
- rev-2 · 2026-08-17 · folded the owner's fork resolutions. Fork B ratified BUILD-IT. Fork E ratified
  ADD-NOW against this spec's recommendation, adding the kind column, the second derived line, and
  the §3 statement of what the two resolutions together still cannot answer.
- rev-4 · 2026-08-17 · BUILT. The render exposed a retrofit defect the M4 audit could not: two
  aSiftedPlaybook M4 records had bound NINE and TEN ids, because `TOOL-aTetheredRecord-3`'s rule-1
  scan read forty lines and swept up ids the reviews CITE as prior decisions. The table made it
  visible at a glance, which is the argument for the table. Both corrected to the set they actually
  audit, and renamed; only the deliberate cross-build record now binds a foreign slug.
- rev-3 · 2026-08-17 · folded the M4 audit. S5 adds the kit-version bump this unit's own edit to
  `gen_build_index.py` obliges, and §7 gains the two gates that date it. The "three-folder sentence"
  S1 anchored to does not exist — that sentence's folder list is DERIVED from the record kinds, and
  this build's own README renders two folders, not three — so S1 now anchors to the sentence by name
  rather than by a count that varies per build.

## 10. Reuse audit

The render seam is `gen_build_index.py`'s existing region renderer and its marker-region contract,
which four live readers already share and which `tools/memory-tree/marker-contract.test.sh` drives
over one case table. Nothing new is introduced: the table is another block inside the pair that
exists, and both derivations come from `TOOL-aTetheredRecord-2`'s functions rather than from a second
parse. Recall terms: `build slug spec artifact filename header adversarial review closeout journal
bookkeeping convergence naming hygiene`.
