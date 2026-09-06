# aTunedCompass — the acceptance ledger for unit 8

**Serves:** journal TOOL-aTunedCompass-8

*Node `a`, 2026-09-05, written by the unattended run that built the unit.*

Every line below is `OBSERVED` with the command that made it, or `AMENDED` naming the revision that
changed the criterion. There is no third form.

## Evidences

**Evidences:** TOOL-aTunedCompass-8

- AC1 — `python tools/codebase-map/reuse_lookup.py` on a live probe, reading the row it appended:
  `shown_paths` holds 10 deduped, repo-relative, forward-slashed paths in shortlist order.
- AC2 — the same row: `n_shown` is **39** and `n_sources` is **10**, which is the point of keeping
  them apart — `n_shown` still counts RANKED CANDIDATES and was not redefined, so an analysis
  joining old rows to new ones does not find a field silently changing what it counts. The CAP is
  exercised in the self-test rather than here: a live corpus that never exceeds 40 sources would
  leave the cap unobserved, which is the shape where a constant nothing reads passes for a bound.
- AC3 — the same row against the command's own `## sources to open` block: every entry appears
  there, none carries a backslash, none is absolute. One derivation feeds both, so this holds by
  construction rather than by luck — `derive_source_paths()` produces the set, `_sources()` labels it and
  `write_lookup()` records it.
- AC4 — `CODEBASE_MAP_ROOT` pointed at a scratch tree with no `.git`: the probe still prints its
  candidates, exits **0**, writes **no row anywhere** (`find <scratch> -name lookups.jsonl` returns
  nothing), and this repository's own `lookups.jsonl` is **byte-identical** across the run. rev-3
  named `GIT_DIR`, which reaches nothing under this kit — resolution is `CODEBASE_MAP_ROOT` ->
  `root/.git` -> `commondir`, pure path math with no child process — so that criterion could not
  fail for the reason it gave, and running it as written would have APPENDED to the live corpus AC5
  exists to protect.
- AC5 — `python tools/codebase-map/selftest.py` — **29 executed, 0 skipped, PASS**, with the new
  arm, and the real log's sha256 is unchanged across the suite run (`b17cd70de8e5…` before and
  after). The arm redirects the root to a scratch repo, which is what makes that true.
- AC6 — `bash tools/check-install-prefix.sh` — exit 0. It **failed first**, and the failure was
  correct: this unit's own docstring and unit 6's harness had written kit-path literals into shipped
  bytes, which is the BAN §12 states. Fixed by DERIVING rather than by recording a ratchet row —
  `query.py` names its sibling by module, and `replay-phrases.py` derives its own invocation from
  `__file__` the way `query.py` derives `CLI`.
- AC7 — `bash tools/check-kit-versions.sh` — exit 0 with `KIT_CODEBASE_MAP_VERSION` at `1.7` and the
  `gov:kit codebase-map@` marker moved with it.
- AC8 — `memory/map/features/codebase-map.md` names both new fields, states that their absence on an
  older row means unknown rather than zero, and `python tools/codebase-map/test_codebase_map.py`
  exits 0. That suite failed first on a STALE `inventories.json`, regenerated with
  `python tools/codebase-map/gen_map.py --write`.

- AC9 — `python tools/lexicon/lexicon.py --check` — exit 0 at **467** offenders, exactly the
  declared `VERB_OFFENDER_PIN`. It failed first at **480**: this run had added thirteen function
  names whose leading token is not in the declared verb table, and that ratchet is SHRINK-ONLY, so
  raising the pin was not an option. All thirteen were renamed to declared verbs across four kits —
  `derive_source_paths`, `_derive_dir`, `_derive_shortlist_key`, `run_fusion`,
  `render_empty_spine_diagnosis`, `_read_rows`, `_measure_spine_docs`, and seven in
  `replay-phrases.py`. The table did the job it exists for: it refused names like `grade` and
  `fuse` that read fine and say nothing about what the function does.

## The cap, and why 40

`SOURCE_PATHS_CAP = 40` is measured, not picked. The logged list is the deduped SOURCE set rather
than the ranked candidates — the parent build measured ~17 file-backed sources per probe against ~71
ranked entries, and this row reproduces that shape at 10 against 39. 40 sits above the mean and
below the 188-candidate outlier; at a nominal 40 bytes per path a typical row grows ~700 B against
today's ~255 B, and a capped worst case adds ~1.6 KB, against a recall log that already runs at a
2150 B mean row.

## What this unit does NOT observe

The row says what the probe RETURNED. It does not say whether the reader opened any of it, whether
the question was relevant, or whether the answer helped. The efficacy question this field makes
COMPUTABLE — the parent measured about one useful path in eighteen — still needs somebody to compute
it. This unit ships the substrate for that, and claims nothing more.
