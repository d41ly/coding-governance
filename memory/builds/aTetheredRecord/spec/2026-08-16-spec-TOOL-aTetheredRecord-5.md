# TOOL-aTetheredRecord-5 — the rendered Records table and the coverage join

**Status:** SPECCED · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Put the binding where a reader lands, and compute the one thing no grep can: which spec ids no record
names. A build README's generated region already lists every unit; it says nothing about the records
beside them. This unit renders each record under the ids it serves and derives the two-sided gap.

## 2. Scope (IN)

- **S1** — The generated region gains a records table, below the existing sentence that names the
  three record folders, listing each record with the ids it serves and its recorded rev where one is
  present. Rows are sorted by path; links use the build-relative form the region already emits.
- **S2** — A derived line naming the spec ids that no record in the build names, computed from the
  same two functions `TOOL-aTetheredRecord-2` supplies.
- **S3** — `--selftest` arms covering a build with records, a build with none, and the population
  assertion that keeps the table from silently rendering empty.

## 3. Non-goals (OUT)

- **The derived line is NOT labelled "unreviewed".** It reports ids no record names. Whether a record
  is a spec audit or a cumulative-diff review is Fork E, deferred, and a coverage claim this build
  cannot support is worse than an honest gap. `memory/guides/BUILD-METHOD.md` M4 selects on rev too,
  and this build's rev is optional.
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
- **AC4** — When `bash tools/memory-tree/marker-contract.test.sh` runs, it is green — the table sits
  inside the single existing generated-region pair.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, the existing arms over
  the folder sentence all still pass, and the new positive-population arm fails against a stub that
  renders an empty table.
- **AC6** — When `bash tools/run-gates.sh` runs, every leg is green.

## 7. Gates

`memory hygiene (20 checks)` — check 9's byte-compare · `build-index selftest` ·
`marker-region contract` · `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

**Fork B — does this unit land at all?** It is separable: cutting it leaves units 1 through 4 and 6
unchanged, because it is a subtraction rather than a rewrite.

- *Option 1 (RECOMMENDED)* — build it, after check 21. It buys the coverage join and converts the
  authored line into a byte-compared one, which is what stops a stale binding from sitting unnoticed.
- *Option 2* — cut it, and reach the same information with a query the reader must know to run. The
  owner's ask was for convergence at a glance, and a command nobody runs is not a glance.

**Fork E — does a record declare a relation KIND?** A cumulative-diff review and a spec audit are
different relations and this build binds ids without distinguishing them.

- *Option 1 (RECOMMENDED)* — defer, and meanwhile do not claim M4 coverage anywhere. The vocabulary
  is a real design question and inventing it under time pressure is how a closed enum acquires a
  value nobody can define.
- *Option 2* — add a kind token now. It would make the derived line a true review-coverage report,
  and it would need the rev from Fork C to be honest, which is unsatisfiable across this corpus.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the adversarial design pass recorded under this build's
  `build/` folder.

## 10. Reuse audit

The render seam is `gen_build_index.py`'s existing region renderer and its marker-region contract,
which four live readers already share and which `tools/memory-tree/marker-contract.test.sh` drives
over one case table. Nothing new is introduced: the table is another block inside the pair that
exists, and both derivations come from `TOOL-aTetheredRecord-2`'s functions rather than from a second
parse. Recall terms: `build slug spec artifact filename header adversarial review closeout journal
bookkeeping convergence naming hygiene`.
