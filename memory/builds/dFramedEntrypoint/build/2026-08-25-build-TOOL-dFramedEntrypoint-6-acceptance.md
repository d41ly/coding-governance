**Serves:** journal TOOL-dFramedEntrypoint-6

# Acceptance ledger — TOOL-dFramedEntrypoint-6

*Node d, 2026-08-25.*

**Evidences:** TOOL-dFramedEntrypoint-6

- AC1 — `python tools/memory-tree/gen_build_index.py --write` — a `gen:spec-records` region renders
  between the status header and `## 1. Goal` in every tracked spec carrying a status header.
- AC2 — `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 with the region present across the
  whole tracked spec corpus, check 12 included. Verified on REAL tracked specs rather than on a
  fixture alone, which is what the criterion asks for: the region needed no eleventh section, no new
  canon and no dated cutoff.
- AC3 — `a CROSS-BUILD record still resolves, which the repo-relative fallback did not` — the arm,
  plus the live tree: a record filed under `aBoundedVerdict` renders in four `dUnstalledConvoy` specs
  as `../../aBoundedVerdict/reviews/…`.
- AC4 — `a spec no record names renders the EXPLICIT empty case` — the arm. An absent region cannot
  be told from a spec nobody has recorded against.
- AC5 — `parse_spec` returns None for a spec with no status header, so no region is rendered into one
  and nothing raises.
- AC6 — `python tools/memory-tree/gen_build_index.py --check` exits 0. A spec with no pair is not
  reported, preserving the create-on-write asymmetry the build-README regions already rely on.
- AC7 — `python tools/memory-tree/gen_build_index.py --selftest` — PASS, 98 `arm ok` lines, six of
  them new.
- AC8 — `invert_bindings` — the inversion keys a record on every id it names rather than on the
  folder it sits in, which is what puts a shared review at each spec a reader is actually looking at.

## Two defects of mine, both caught by a check rather than by reading

`u["path"]` is an ABSOLUTE, mixed-separator path while every other artifact key in `plan` is
repo-relative. The first cut used it as the artifact key, which wrote the correct file only because
`os.path.join` returns an absolute second argument unchanged — and it made the relative-link
computation take its fallback branch on every record. Re-derived from the build root plus the tail,
the way `render_region` already does.

The fallback itself was then wrong: for a cross-build record it emitted the REPO-relative path, which
a markdown reader resolves against the spec's own directory, so all seventeen cross-build edges linked
to nothing. Hygiene check 2 named four of them by file. Replaced with `os.path.relpath`, which is what
should have been there from the start.

## Fork F3, resolved before the code

One commit, no path scoping on `--write`. A verb argument bought for a single migration is a mechanism
with a fan-in of one, and the corpus render is verified by re-running the verb rather than by reading
the diff.
