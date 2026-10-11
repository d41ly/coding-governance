# TOOL-aTrimmedHook-7 — the generator and manifest-check minors of the closing review, batched

**Status:** SPECCED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling+kickoff · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The closing review's medium M3 and lows L1, L5 and L2, the four that land in the build-index
generator and the manifest checker. Two are crashes where the classifier promises "render": a kit on
another Windows drive, and a non-UTF-8 path. One is an arm that observes a synthetic prefix instead
of the kit derivation it claims. One is C6 undercounting a non-ASCII path in the breadth warning.

## 2. Scope (IN)

- **S1 — M3.** In `tools/memory-tree/gen_build_index.py`, `check_staged_render`'s kit derivation
  catches the `ValueError` `os.path.relpath` raises across drives and answers `kit = None`, the answer
  the out-of-tree branch already gives. Observed by AC1.
- **S2 — L1.** The `cat-file` request is encoded with `surrogateescape`, matching the decode, so a
  non-UTF-8 path cannot raise outside the function's own error handling. Observed by AC2.
- **S3 — L5.** `check_staged_render` takes an optional `here` (default the module's directory), and a
  `test_staged_render` arm builds a fixture with a kit directory under its root, stages a file there,
  and expects a render owed through the DERIVED kit path, with no install prefix spelled. Observed by
  AC3.
- **S4 — L2.** In `skills/session-kickoff/manifest-check.sh`, C6's one listing runs with
  `core.quotePath=false`, so a non-ASCII path compares as itself, and any line git still quotes sends
  every count back to git. Observed by AC4.

## 3. Non-goals (OUT)

- **N1** — the hygiene-side minors are TOOL-aTrimmedHook-6's.
- **N2** — no change to C6's dead-spec verdict, which was always git's.
- **N3** — no other caller of `os.path.relpath` in the kit is touched.

### Edges

none

## 4. Design

S1 and S2 restore the docstring's rule that any git or decode failure answers "render": S1 with the
existing `None` branch, S2 by encoding the same way the name-status output was decoded. S3's parameter
exists only so a fixture can place the kit under its own root; production callers pass nothing. S4 keeps
the listing a single process: with `core.quotePath=false` git prints non-ASCII bytes raw and still
quotes a name holding a quote, a backslash or a control byte, and such a line re-asks git for every
spec rather than guessing.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/guides/SESSION-KICKOFF.md`

### Rollout

Order 5, after TOOL-aTrimmedHook-4 and -5 in the generator. `manifest-check.sh` is watched, so the pass
re-stamps the manifest's `last-audit`.

### Alternatives rejected

- **Revise TOOL-aTrimmedHook-1's AC4 to the narrower observation.** That records the gap instead of
  closing it; the parameter is one line.

## 5. Production-readiness checklist

- security — N/A — local gates.
- perf / scale — none: no extra process in either checker.
- error / empty / loading states — S1 and S2 turn two crashes into the documented answer.
- observability — N/A.
- risks — none: production callers do not pass `here`.
- testing — AC1 to AC3 are `--selftest` arms; AC4 is a manifest-check arm.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `gen_build_index.py --selftest` runs, the arm that makes `os.path.relpath` raise
  `ValueError` sees `check_staged_render` return an answer instead of raising.
  Red when: it raises. Observed RED first against the unguarded call.
- **AC2** — When `gen_build_index.py --selftest` runs, the arm feeding a path holding a lone surrogate
  through the request builder sees no `UnicodeEncodeError`.
  Red when: the strict encode raises.
- **AC3** — When `gen_build_index.py --selftest` runs, the arm with a kit directory under the fixture
  root sees a render owed for a file staged there, reached through `here`.
  Red when: it sees a skip.
- **AC4** — When `manifest-check.sh` runs on a fixture manifest whose watch directory holds 100 ASCII
  files and one non-ASCII file, it prints the breadth WARN for 101 files.
  Red when: no WARN prints, which is what the default quoting produced.

## 7. Gates

`build-index selftest` · `kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: tools/memory-tree/gen_build_index.py test_staged_render · covers AC1 AC2 AC3 · the relpath guard removed, the strict encode, a kit outside the root · none
New arm: skills/session-kickoff/manifest-check.test.sh C6 non-ASCII breadth · covers AC4 · the listing without `core.quotePath=false` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from the closing review's M3, L1, L5 and L2.

## 10. Reuse audit

No new mechanism: S1 reuses the out-of-tree `None` branch, S4 keeps KICK-aTrimmedHook-1's one-listing
count. `python tools/codebase-map/reuse_lookup.py "derive a kit path relative to the repository root"`
named `kit_rel` in `tools/memory-tree/tree_lib.py`, which derives from the module's own checkout and
cannot answer for a fixture root, so it is not the seam here.

Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit
